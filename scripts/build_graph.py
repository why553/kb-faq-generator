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
    节点类别               -> CSV 显式列 subject_category / object_category 优先；
                              未填则按 CATEGORY_RULES 关键词自动归类（主体/产品/场景/制度/概念/其他）
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


# ============ 分类标准（关键词自动归类） ============
# 优先级从上到下，命中即停；CSV 显式列 subject_category/object_category 可覆盖
CATEGORY_RULES = [
    ("主体", ["用户", "客户", "个人", "企业", "公司", "银行", "机构", "部门",
              "商户", "运营", "人行", "监管", "员工", "柜员", "经理"]),
    ("产品", ["钱包", "卡", "账户", "存单", "理财", "基金", "保险", "贷款",
              "产品", "应用", "APP", "小程序", "币"]),
    ("场景", ["公交", "地铁", "缴费", "购物", "商超", "门店", "场景", "试点",
              "食堂", "校园", "园区", "政务", "医疗"]),
    ("制度", ["办法", "规定", "公告", "通知", "制度", "条例", "细则", "指引",
              "协议", "合同", "文件"]),
    ("概念", ["利息", "利率", "费率", "费用", "限额", "额度", "余额", "金额",
              "汇率", "期限", "概念", "流程", "标准", "权益", "风险"]),
]


def classify(name: str) -> str:
    for cat, keywords in CATEGORY_RULES:
        if any(kw in name for kw in keywords):
            return cat
    return "其他"


def build_data(triples):
    """节点按首次出现顺序编号 n1..nX；类别 = CSV 显式列 > 关键词规则 > 其他。"""
    node_ids, nodes = {}, []
    for t in triples:
        for ent, ent_cat_key in ((t["subject"], "subject_category"), (t["object"], "object_category")):
            if ent and ent not in node_ids:
                explicit = t.get(ent_cat_key, "")
                cat = explicit if explicit else classify(ent)
                node_ids[ent] = f"n{len(node_ids) + 1}"
                nodes.append({"id": node_ids[ent], "name": ent, "category": cat})
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
