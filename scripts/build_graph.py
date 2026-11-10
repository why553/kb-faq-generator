#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_graph.py —— 将 triples.csv 转换为交互式知识图谱 graph.html

用法:
    python build_graph.py triples.csv [-o graph.html] [-t 模板路径] [--title 标题]

输入: 按 references/triples-schema.md 规范的 CSV（UTF-8，允许 BOM）
输出: 单文件交互式图谱网页（用系统浏览器打开）

映射规则:
    subject / object      -> 节点
    predicate             -> 边标签
    condition             -> 边上的限定条件标签
    polarity = negative   -> 边标红虚线（needsReview，冲突候选）
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

DEFAULT_TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "graph-template.html"


def load_triples(path: Path):
    rows = []
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required = {"subject", "predicate", "object"}
        for i, row in enumerate(reader, 1):
            missing = required - {k for k, v in row.items() if v}
            if missing:
                print(f"[warn] 第 {i} 行缺少 {missing}，跳过", file=sys.stderr)
                continue
            rows.append({k: (v or "").strip() for k, v in row.items()})
    return rows


def build_data(triples):
    """节点按首次出现顺序编号 n1..nX；negative 极性边标记待复核。"""
    node_ids, nodes = {}, []
    for t in triples:
        for ent in (t["subject"], t["object"]):
            if ent and ent not in node_ids:
                node_ids[ent] = f"n{len(node_ids) + 1}"
                nodes.append({"id": node_ids[ent], "name": ent, "category": "其他"})
    links = []
    for t in triples:
        links.append({
            "source": node_ids[t["subject"]],
            "target": node_ids[t["object"]],
            "relation": t["predicate"],
            "condition": t.get("condition", ""),
            "needsReview": t.get("polarity", "positive").lower() == "negative"
                           or bool(t.get("needs_review", "").lower() in ("yes", "true", "1")),
        })
    return nodes, links


DATA_BLOCK = re.compile(
    r"/\* ================= 由 Agent 注入数据 =================.*?/\* ================= 以下为引擎逻辑",
    re.S,
)


def render(template: Path, nodes, links, title: str) -> str:
    html = template.read_text(encoding="utf-8")
    injected = (
        "/* ================= 由 Agent 注入数据 =================\n"
        "   nodes: [{ id, name, category }]\n"
        "   links: [{ source, target, relation, condition, needsReview }] */\n"
        f"var nodes = {json.dumps(nodes, ensure_ascii=False, indent=2)};\n"
        f"var links = {json.dumps(links, ensure_ascii=False, indent=2)};\n"
        "/* ================= 以下为引擎逻辑"
    )
    if not DATA_BLOCK.search(html):
        sys.exit("模板格式不正确：未找到数据注入标记")
    html = DATA_BLOCK.sub(injected.replace("\\", "\\\\"), html, count=1)
    if title:
        html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1)
    return html


def main():
    ap = argparse.ArgumentParser(description="triples.csv -> interactive graph.html")
    ap.add_argument("triples", help="triples.csv 路径")
    ap.add_argument("-o", "--output", default="graph.html", help="输出 HTML 路径")
    ap.add_argument("-t", "--template", default=str(DEFAULT_TEMPLATE), help="模板路径")
    ap.add_argument("--title", default=None, help="页面标题")
    args = ap.parse_args()

    src = Path(args.triples)
    if not src.exists():
        sys.exit(f"找不到输入文件: {src}")

    triples = load_triples(src)
    if not triples:
        sys.exit("triples.csv 中没有有效数据")
    nodes, links = build_data(triples)
    html = render(Path(args.template), nodes, links, args.title or f"知识图谱 - {src.stem}")

    out = Path(args.output)
    out.write_text(html, encoding="utf-8")
    conflict = sum(1 for l in links if l["needsReview"])
    print(f"[ok] 已生成 {out.resolve()}（{len(nodes)} 节点 / {len(links)} 关系 / {conflict} 条待复核）")
    print("     请用系统浏览器打开查看（Windows: cmd /c start <路径>）")


if __name__ == "__main__":
    main()
