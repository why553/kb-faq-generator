---
name: kb-faq-generator
description: |
  把制度文件、培训材料、业务手册等文档整理成知识库问答对。
  每条答案都带原文引用和出处位置。
  输出 Markdown 表格、CSV 文件和生成报告。
  需要时同时输出知识三元组 CSV 和可交互的图谱网页。
  当用户上传 PDF、Word、txt、md 文件并要求生成问答对、FAQ、知识库问答、
  培训问答，或要求抽取三元组、生成知识图谱时使用。
agent_created: true
---

# 知识库问答对生成器

## 作用

把文档整理成问答对。每条问答对包含问题、答案、出处文件、出处位置、原文引用。

答案里的内容必须来自源文件。源文件没有的内容不写进答案。

## 需要的输入

开始前确认以下内容，缺少时询问用户：

1. 源文件，必需，支持 PDF、Word、Excel、txt、md
2. 分类体系，可选。用户没有提供时，按内容自拟 4 到 8 个分类，并在报告里列出
3. 使用对象，可选，取值为 internal、customer、both，默认 internal
4. 数量要求，可选。用户没有要求时按内容多少生成，不设上限，具体规则见 style-guide.md
5. 是否生成三元组和图谱，可选。用户提到三元组、知识图谱、可视化时生成，没提到就不生成

## 执行步骤

### 第 1 步 读取文件并清点内容

逐份读取源文件，列出可提取的内容，包括定义、流程、条件、数值标准（利率、费率、限额、期限）、注意事项。

文件超过 30 页时先建立章节索引，再按章节分批处理，避免漏掉后半部分。

输出清点清单，写明每份文件预计生成多少条、按什么分类。用户确认后再进入第 2 步。

### 第 2 步 生成问答对

- 字段规范：按 references/qa-schema.md 的 15 个字段定义、编号规则和禁止事项填写
- 问题写法：按 references/style-guide.md 把条文语言改成办事语言。数值、日期、利率、限额必须写清楚
- 问型分布：每条问题先按 references/qa-schema.md 的问型矩阵定好 question_type 和 user_profile 再写。每批 10 条及以上时，问型至少覆盖 3 类，提问者画像至少覆盖 2 类。同一知识点的多条问答对必须用不同的问型或画像
- 难度标定：每条问答对标 difficulty_retrieval 和 difficulty_reasoning，取值和规则见 references/qa-schema.md。每批 10 条及以上时，两个难度维度各至少覆盖 2 档。需要计算的答案要把计算过程写进 review_note，需要比较的答案标 needs_review
- 答案依据：每条答案的事实必须能在 source_quote 的原文摘录里找到。需要推断的内容，confidence 只能填 medium 或 low，并且 needs_review 填 yes
- 输出格式：CSV 参照 assets/faq-output-template.csv，编码用 UTF-8 with BOM

### 第 3 步 自检

按 references/quality-checklist.md 逐项检查：

- A 完整性：字段齐全，编号连续，Markdown 与 CSV 内容一致
- B 出处：抽查 source_quote 是否与原文逐字一致。confidence 为 low 或 needs_review 为 yes 的条目全部检查
- C 质量：问题写法合规，答案回答问题，没有重复条目
- D 安全：没有个人信息，没有内部信息，没有收益承诺
- F 问型：question_type 和 user_profile 取值合规，分布达到矩阵要求，reasoning 类都标了 needs_review
- G 难度：难度取值合规，分布达到要求，calculation 类的答案能由原文数值算出，calculation 和 comparison 类都标了 needs_review

生成了三元组时追加 E 类检查：每条三元组都有 source_qa_id，condition 没有丢失，同义实体已列入清单。

检查不通过的条目先修改再交付。

### 第 4 步 交付

必交三件：

1. faq-{主题}-{日期}.md，Markdown 表格，供人工评审
2. faq-{主题}-{日期}.csv，供知识库批量导入
3. 生成报告，内容包括源文件清单、分类分布、问型分布矩阵、难度分布统计、needs_review 条目及原因、没有转化的内容及原因、自检结果

用户要求三元组或图谱时追加两件：

4. triples.csv，按 references/triples-schema.md 的字段填写，每条挂在一条问答对下面
5. graph.html，运行 `python scripts/build_graph.py triples.csv -o graph.html` 生成。节点按主体、产品、场景、制度、概念、其他六类自动着色。生成后用系统浏览器打开（Windows 执行 cmd /c start 加文件路径），不要用内置预览，内置预览加载不了 CDN 脚本

交付时说明两件事：

- needs_review 为 yes 的条目，人工确认后才能进正式知识库
- triples.csv 是通用图数据格式，主语和宾语是节点，谓语和 condition 是边的属性，可以导入图数据库或图分析工具做机器查询

## 不做的事

- 不回答用户基于问答对提出的业务问题。本技能只生成问答对
- 不修改源文件内容，不改写制度条文
- 不处理含未脱敏客户个人信息的文件。发现后停止，提示用户先脱敏
- 不在答案里补充源文件之外的知识

## 维护

用户反馈新的问法或常见错误时，把案例追加到 references/style-guide.md 对应章节，不要只写在对话里。

问型矩阵的取值和分布标准集中在 references/qa-schema.md 里维护。实际使用中发现某类问型用户从不问，或者缺了某类高频问型，先改 qa-schema.md 的定义再改生成行为。

难度档位的取值同理，集中在 references/qa-schema.md 里维护。知识库运营方如果对难度分层有新要求，先改定义再改行为。
