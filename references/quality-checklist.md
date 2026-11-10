# 质量自检清单（Quality Checklist）

每批问答对交付前，逐项自检。任何一项不通过，先修正再交付，禁止跳过。

## A. 完整性检查

- [ ] 每条问答对包含 qa-schema.md 要求的全部 12 个字段，无缺失、无空值（review_note 仅在 needs_review=no 时允许为空）
- [ ] qa_id 编号连续、无重复，格式符合 `QA-{来源序号3位}-{条目序号3位}`
- [ ] Markdown 表格与 CSV 内容一致

## B. 溯源检查（最高优先级）

- [ ] 每条 source_quote 均能在源文件中逐字找到（抽查至少 30%，confidence=low 或 needs_review=yes 的条目 100% 核对）
- [ ] source_location 精确到章节/页码/条款号，无"见全文"式模糊标注
- [ ] answer 中所有数字、日期、金额、利率均能在 source_quote 或原文中找到，无任何外推
- [ ] 无一条问答对引用了不在本次输入材料中的来源

## C. 质量检查

- [ ] question 符合 style-guide.md：口语化、单一问题、疑问句结尾、8-30 字
- [ ] answer 直接回答 question，无答非所问
- [ ] 无重复问答对（同问同答）；同义问法已按规范标注
- [ ] needs_review=yes 的条目均有 review_note
- [ ] confidence 分级合理：直接引用制度原文=high；来自培训材料/综合推断=medium；模糊或歧义=low

## D. 安全合规检查

- [ ] 全部条目无客户真实姓名、身份证号、账号、手机号等个人信息
- [ ] audience=customer 的条目不含内部系统名、内部流程细节、内部联系方式
- [ ] 无对客户的收益承诺性表述（如"稳赚""保本""绝对安全"）
- [ ] 涉及利率、费用、限额的表述与原文一致且未简化到产生歧义

## 交付报告（随批附送）

除问答对文件外，同时输出一份简短生成报告（Markdown）：
- 源文件清单及各文件生成条数
- 分类分布统计（category 计数）
- needs_review=yes 条目清单及原因摘要
- 未能转化为问答对的标题清单及原因（对应 style-guide.md 覆盖度要求）
- 本批质量自检结果（以上 A-D 各项的通过情况）
