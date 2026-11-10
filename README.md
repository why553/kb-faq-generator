# kb-faq-generator

从制度文件、培训材料、业务手册等源文档批量生成结构化知识库问答对（FAQ）的 AI Agent Skill。适用于银行/企业知识工程中的"知识入库"工序。

## 为什么做这个

企业知识工程里最耗人力的工序之一，是把成堆的制度文件、培训材料转化成可入库、可检索的问答对。手工整理又慢又容易漏；直接让大模型"随便生成"又缺乏一致性——每次口径不同、出处缺失、无法审计。

本 skill 把这道工序**固化**下来：

- **强制溯源**：每条答案必须携带逐字原文引用 + 精确到章节/页码的出处，禁止模型补写源文件之外的任何知识
- **口径一致**：12 字段统一规范（qa_id / question / answer / source_file / source_location / source_quote / category / audience / confidence / needs_review / review_note），任何人任何批次产出同一标准
- **人工终审**：涉及金额、利率、歧义表述的条目自动标记 `needs_review`，对齐金融场景"AI 辅助、人工终审"的合规底线
- **三件套交付**：Markdown（评审用）+ CSV（知识库批量导入用）+ 生成报告（分类统计、待复审清单、自检结果）

## 效果示例

输入一份制度文件，输出：

| qa_id | question | answer | source_file | source_location | source_quote | category | audience | confidence | needs_review | review_note |
|---|---|---|---|---|---|---|---|---|---|---|
| QA-001-001 | 数字人民币钱包里的钱有利息吗？ | 计息。自2026年1月1日起实名钱包余额按相应标准计付利息。 | 数字人民币计息新规公告.pdf | 第2条 | "自2026年1月1日起，数字人民币实名钱包余额计付利息" | 计息规则 | internal | high | no | |

生成报告同时告知：共生成 N 条、各分类分布、哪些条目待人工复审及原因、哪些标题不适合转问答对。

## 安装

将本目录复制到 Agent 的技能目录下即可（WorkBuddy 用户级：`~/.workbuddy/skills/kb-faq-generator`；项目级：`.workbuddy/skills/kb-faq-generator`）。

## 使用

对 Agent 说：

```
用 kb-faq-generator 把这份文件生成问答对 [附上文件]
```

Skill 会按四步工作流执行：

1. **读取盘点** —— 建立知识点清单，与用户确认生成规模
2. **生成问答对** —— 按 `references/qa-schema.md` 字段规范 + `references/style-guide.md` 问法风格
3. **质量自检** —— 按 `references/quality-checklist.md` 的完整性/溯源/质量/安全四类检查
4. **交付** —— Markdown 表格 + CSV 入库文件 + 生成报告三件套

## 目录结构

```
kb-faq-generator/
├── SKILL.md                    # 技能本体：工作流、溯源铁律、边界
├── references/
│   ├── qa-schema.md            # 问答对 12 字段规范与禁止事项
│   ├── style-guide.md          # "条文语言 → 办事语言"问法转换规则
│   └── quality-checklist.md    # 交付前 A-D 四类自检清单
└── assets/
    └── faq-output-template.csv # CSV 入库模板（UTF-8 with BOM）
```

## 设计边界

- 只做"知识的搬运与格式化"，不生产新知识——答案中一切事实均须来自源文件
- 不处理含未脱敏个人信息的文件，发现即停止并提示先脱敏
- `needs_review=yes` 的条目必须经人工确认后方可入正式知识库

## 迭代机制

使用中发现的新问法、常见误判，追加到 `references/style-guide.md` 对应章节，规则随使用持续积累——skill 是活文档，不是一次性 prompt。

## License

版权所有。本项目为个人学习实习期间的作品，仅供学习交流使用，未经许可不得商用或二次分发。
