# 问答对输出示例（节选）

> 源文件：《数字人民币计息新规公告（示例）》——本示例为演示样例，非真实文件。
> 完整字段定义见 `references/qa-schema.md`，配套三元组示例见 `triples-example.csv`。

## Markdown 评审表（节选）

| qa_id | question | question_type | user_profile | difficulty_retrieval | difficulty_reasoning | answer | source_file | source_location | source_quote | category | audience | confidence | needs_review | review_note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| QA-001-001 | 数字人民币钱包里的钱有利息吗？ | fact | novice | easy | direct | 计息。自2026年1月1日起，数字人民币实名钱包余额计付利息。 | 数字人民币计息新规公告.pdf | 第2条 | "自2026年1月1日起，数字人民币实名钱包余额计付利息" | 计息规则 | internal | high | no | |
| QA-001-002 | 数字人民币钱包分哪几种？ | fact | novice | easy | direct | 分为实名钱包和硬钱包两类。 | 数字人民币计息新规公告.pdf | 第1条 | "数字人民币钱包分为实名钱包与硬钱包" | 钱包体系 | internal | high | no | |
| QA-001-003 | 硬钱包有利息吗？ | exception | novice | paraphrase | direct | 不计息。现行规定下硬钱包余额不计付利息，具体以最新公告为准。 | 数字人民币计息新规公告.pdf | 第3条 | "硬钱包余额不计付利息" | 计息规则 | internal | high | no | |
| QA-001-004 | 硬钱包能在哪些场合用？ | condition | expert | paraphrase | comparison | 已在深圳公交场景试点受理，覆盖范围以运营公告为准。 | 数字人民币试点场景通报.pdf | 场景二 | "硬钱包于深圳公交场景开展受理试点" | 受理环境 | both | medium | yes | 受理范围随试点动态变化，建议人工确认时效性 |
| QA-001-005 | 实名钱包计息的口径依据是什么？ | fact | reviewer | easy | direct | 依据公告第2条。 | 数字人民币计息新规公告.pdf | 第2条 | "自2026年1月1日起，数字人民币实名钱包余额计付利息" | 计息规则 | internal | high | no | |

## 生成报告（节选）

- 源文件：2 份（数字人民币计息新规公告.pdf、数字人民币试点场景通报.pdf）
- 生成问答对：5 条；分类分布：计息规则 2 / 钱包体系 1 / 受理环境 1 / 钱包管理 1
- 问型分布矩阵：

| | novice | expert | reviewer |
|---|---|---|---|
| fact | 2 | 0 | 1 |
| exception | 1 | 0 | 0 |
| condition | 0 | 1 | 0 |

- 难度分布：检索难度 easy 3 / paraphrase 2；推理难度 direct 4 / comparison 1
- needs_review：1 条（QA-001-004，受理范围时效性待人工确认）
- 未能转化条目：公告第4条（立法说明性文字，不含可办事信息）→ 跳过
- 同义实体清单（供人工归一）：「实名钱包 / 数币实名钱包」视为同一实体
- 自检结果：A/B/C/D/F/G 六类全部通过；三元组 6 条，其中 1 条 negative 待复核

## 配套图谱

运行 `python scripts/build_graph.py examples/triples-example.csv -o graph.html`，
用系统浏览器打开 graph.html 即可交互探索（搜索 / 最短路径 / 冲突候选高亮）。
