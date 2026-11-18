# kb-faq-generator

从制度文件、培训材料、业务手册等源文档批量生成结构化知识库问答对（FAQ）的 AI Agent Skill，并配套**答题模式**：用问答对库按固定话术回答用户问题，不知道的拒答。适用于银行/企业知识工程中的“知识入库”与“知识服务”两个工序。

## 为什么做这个

企业知识工程里最耗人力的工序之一，是把成堆的制度文件、培训材料转化成可入库、可检索的问答对。手工整理又慢又容易漏；直接让大模型“随便生成”又缺乏一致性：每次口径不同、出处缺失、无法审计。

本 skill 把这道工序**固化**下来：

- **强制溯源**：每条答案必须携带逐字原文引用 + 精确到章节/页码的出处，禁止模型补写源文件之外的任何知识
- **问型多样性矩阵**：每条问答对标 `question_type`（事实/流程/条件/对比/异常/推理 6 类）× `user_profile`（新手/专家/审核 3 类）两个维度，每批强制覆盖至少 3 种问型、2 种画像，避免模型只会生成“什么是X”式的单调问法（参考 DataMorgana, ACL 2025）
- **双轴难度标定**：每条问答对标 `difficulty_retrieval`（easy/paraphrase/structural）× `difficulty_reasoning`（direct/calculation/comparison）两个独立维度，生成报告附难度分布，知识库运营可按难度分层抽检（参考 GRADE, 2025）
- **口径一致**：16 字段统一规范（qa_id / question / question_type / user_profile / difficulty_retrieval / difficulty_reasoning / answer / **customer_answer** / source_file / source_location / source_quote / category / audience / confidence / needs_review / review_note），任何人任何批次产出同一标准
- **人工终审**：涉及金额、利率、歧义表述的条目自动标记 `needs_review`，对齐金融场景“AI 辅助、人工终审”的合规底线
- **对客固定话术**：`answer` 保持纯事实本体，礼貌话术壳单独放 `customer_answer` 字段（开头 + answer 原文 + 特殊场景提示 + 结尾），配套禁用语清单（承诺类/含糊类/命令式/行内术语），事实与话术分离、互不污染
- **核心三件套**：Markdown（评审用）+ CSV（知识库批量导入用）+ 生成报告（分类统计、问型分布矩阵、待复审清单、自检结果）

## 知识图谱增强（可选）

在生成问答对的基础上，可要求同时抽取**知识三元组**并渲染为**交互式图谱**：

- **triples.csv**：主语-谓语-宾语三元组，带 `condition`（时间/地域限定条件，防止语境丢失）和 `polarity`（否定语义独立表达）字段，每条挂靠问答对（source_qa_id），保证人读机器读同一份知识
- **graph.html**：单文件交互式知识图谱（零依赖，浏览器直接打开），内置：
  - 节点搜索、按关系过滤子图
  - 两节点最短路径查询（BFS）
  - 邻居子图展开
  - **实体分类着色**：主体/产品/场景/制度/概念/其他 六类标准配色（关键词自动归类，CSV 显式列可覆盖）
  - **冲突候选一键高亮**：否定语义或语义相反的边标红虚线，为制度冲突检测预留接口
- **build_graph.py**：`python scripts/build_graph.py triples.csv -o graph.html` 一键把三元组 CSV 转成图谱网页

三元组 CSV 为通用图数据格式（subject/object 为节点，predicate+condition 为边属性），可导入任何图数据库或图分析工具做机器查询。

**在线示例**：直接在浏览器打开 [`examples/graph-example.html`](examples/graph-example.html) 体验（6 实体 / 6 关系，含 1 条故意埋入的“计息 vs 不计息”矛盾边）；问答对输出示例见 [`examples/qa-example.md`](examples/qa-example.md)。

## 答题模式（知识服务）

生成问答对只是入库，答题模式是知识服务：给定问答对库和用户问题，Agent 按 `references/answer-protocol.md` 输出标准答复。

- **答案不许偏**：大模型只做三件事：听懂问题、从库中检索匹配、按固定公式拼装。答复的事实本体与命中条目的 `answer` 逐字一致，不改写、不总结、不扩写，不把多条问答对揉成一段
- **四种命中情形**：明确命中直接答 / 模糊命中先确认 / 命中多条列选项 / 未命中就拒答
- **六类问题拒答**：他人隐私、客户个人信息、违规操作、内部信息、投资建议、未公示信息，各有固定拒答话术，只拒不给、给出正规渠道、语气不责备
- **固定话术拼装**：开头话术 + answer 原文 + 特殊场景提示（时效、资金安全、费用利率）+ 结尾话术，全部话术收录在 `references/tone-guide.md`，配有禁用语清单

示例：用户问“帮我查一下我朋友的账户余额”，按他人隐私类固定话术拒答；用户问“硬钱包坐公交能用吗”，模糊命中后输出套壳答复并注明依据条目编号。完整演示见 [`examples/qa-example.md`](examples/qa-example.md) 答题模式章节。

## 效果示例

输入一份制度文件，输出：

| qa_id | question | question_type | user_profile | answer | source_file | source_location | source_quote | category | audience | confidence | needs_review | review_note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| QA-001-001 | 数字人民币钱包里的钱有利息吗？ | fact | novice | 计息。自2026年1月1日起实名钱包余额按相应标准计付利息。 | 数字人民币计息新规公告.pdf | 第2条 | “自2026年1月1日起，数字人民币实名钱包余额计付利息” | 计息规则 | internal | high | no | |
| QA-001-002 | 实名钱包计息的口径依据是什么？ | fact | reviewer | 依据公告第2条。 | 数字人民币计息新规公告.pdf | 第2条 | “自2026年1月1日起，数字人民币实名钱包余额计付利息” | 计息规则 | internal | high | no | |

同一知识点生成两条问答对时使用不同画像（novice 问结果，reviewer 问依据），这就是问型矩阵的作用。

生成报告同时告知：共生成 N 条、各分类分布、问型分布矩阵（question_type × user_profile 交叉计数）、哪些条目待人工复审及原因、哪些标题不适合转问答对。

## 安装

将本目录复制到 Agent 的技能目录下即可（WorkBuddy 用户级：`~/.workbuddy/skills/kb-faq-generator`；项目级：`.workbuddy/skills/kb-faq-generator`）。

## 使用

对 Agent 说：

```
用 kb-faq-generator 把这份文件生成问答对 [附上文件]
用 kb-faq-generator 处理这份文件，同时生成三元组和知识图谱 [附上文件]
用 kb-faq-generator 答题模式，按这份问答对库回答用户问题 [附上库文件]
```

生成模式按四步工作流执行：

1. **读取盘点**：建立知识点清单，与用户确认生成规模
2. **生成问答对**：按 `references/qa-schema.md` 字段规范（含问型矩阵、双轴难度、对客话术）+ `references/style-guide.md` 问法风格
3. **质量自检**：按 `references/quality-checklist.md` 的完整性/溯源/质量/安全/问型/难度/话术七类检查（含三元组 E 类检查）
4. **交付**：Markdown 表格 + CSV 入库文件 + 生成报告；要求图谱时另附 triples.csv + graph.html（系统浏览器打开）

单独转换图谱也可以：

```bash
python scripts/build_graph.py your-triples.csv -o graph.html
```

## 目录结构

```
kb-faq-generator/
├── SKILL.md                    # 技能本体：两种模式的工作流、溯源铁律、边界
├── references/
│   ├── qa-schema.md            # 问答对 16 字段规范 + 问型矩阵 + 双轴难度 + 对客答复字段 + 禁止事项
│   ├── style-guide.md          # “条文语言 → 办事语言”问法转换规则 + 矩阵与难度写作指引
│   ├── tone-guide.md           # 对客固定话术：开头/结尾/特殊场景/禁用语/套用公式
│   ├── answer-protocol.md      # 答题模式规范：匹配流程/命中判定/原封不动铁律/拒答机制
│   ├── quality-checklist.md    # 交付前 A-D + E(三元组) + F(问型) + G(难度) + H(话术) 自检清单
│   └── triples-schema.md       # 知识三元组字段规范与抽取规则
├── scripts/
│   └── build_graph.py          # triples.csv → 交互式 graph.html 转换器
├── assets/
│   ├── faq-output-template.csv # CSV 入库模板（UTF-8 with BOM）
│   └── graph-template.html     # 图谱引擎模板（ECharts 单文件）
└── examples/
    ├── qa-example.md           # 问答对输出示例和生成报告样例
    ├── triples-example.csv     # 三元组示例数据
    └── graph-example.html      # 可直接浏览器打开的示例图谱
```

## 设计边界

- 只做“知识的搬运与格式化”，不生产新知识：答案中一切事实均须来自源文件
- 不处理含未脱敏个人信息的文件，发现即停止并提示先脱敏
- `needs_review=yes` 的条目必须经人工确认后方可入正式知识库

## 迭代机制

使用中发现的新问法、常见误判，追加到 `references/style-guide.md` 对应章节，规则随使用持续积累：skill 是持续更新的文档，不是一次性的提示词。

## License

版权所有。本项目为个人学习实习期间的作品，仅供学习交流使用，未经许可不得商用或二次分发。
