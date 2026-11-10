---
name: kb-faq-generator
description: |
  从制度文件、培训材料、业务手册等源文档批量生成结构化知识库问答对（FAQ），
  每条问答对强制携带原文出处与逐字引用，按统一字段规范输出 Markdown 表格和
  CSV 入库文件，并随批输出质量自检报告；可选生成知识三元组 CSV 与交互式
  知识图谱 HTML。适用于银行/企业知识工程中的"知识入库"工序。
  This skill should be used when the user provides documents
  (PDF/Word/txt/md) and asks to generate FAQs, 问答对, 知识库问答, FAQ 库,
  培训问答, 知识图谱, 三元组, or asks to 把文件整理成问答/入库格式.
agent_created: true
---

# 知识库问答对生成器（KB FAQ Generator）

## Overview

将制度文件、培训材料、业务手册等源文档批量转换为结构化知识库问答对。每条问答对强制溯源（逐字原文引用 + 精确出处定位），按固定 12 字段规范交付 Markdown 表格 + CSV 入库文件，并随批输出质量自检报告。可选增强：抽取知识三元组（含限定条件字段）并渲染为可交互的知识图谱 HTML（双击即可在浏览器查看，无需安装任何软件）。

核心立场：本技能只做"知识的搬运与格式化"，不生产新知识。答案中的一切事实均须来自源文件，这是金融场景不可逾越的底线。

## 输入要求

开始前确认以下输入，缺失时先询问：

1. **源文件**（必需）：1 份或多份，支持 PDF/Word/Excel/txt/md
2. **主题分类体系**（可选）：知识库已有的 category 分类；未提供时按源文件内容自拟 4-8 个分类并在报告中列出
3. **audience 定位**（可选）：internal / customer / both；未提供时默认 internal
4. **数量期望**（可选）：无要求时按覆盖度规则生成（见 style-guide.md），不设上限
5. **三元组与图谱**（可选）：用户提及"三元组/知识图谱/可视化"时生成；未提及则不生成，保持交付物精简

## Workflow

### Step 1: 读取与盘点

逐份读取源文件，盘点全部可提取的知识点：定义、流程、条件、数值标准（利率/费率/限额/期限）、注意事项。对长文件（>30 页）先建立章节索引再分批处理，避免遗漏后半部分内容。

输出一个简短盘点清单：每份文件将生成多少条、按什么分类。让用户确认后再进入 Step 2（批量任务前置确认，避免大规模返工）。

### Step 2: 生成问答对

按以下规范逐条生成：

- **字段规范**：严格遵循 `references/qa-schema.md` 的 12 字段定义、qa_id 编号规则和禁止事项
- **问题风格**：遵循 `references/style-guide.md`，完成"条文语言 → 办事语言"转换；数值、日期、利率、限额等硬信息必须全覆盖
- **溯源铁律**：每条 answer 的事实必须能在 source_quote（逐字摘录）中找到支撑；综合推断类答案 confidence 只能为 medium/low 且 needs_review=yes
- **输出模板**：CSV 格式参照 `assets/faq-output-template.csv`（UTF-8 with BOM）

### Step 3: 质量自检

按 `references/quality-checklist.md` 的 A-D 四类检查项逐项自检：

- A 完整性：字段齐全、编号连续、双格式一致
- B 溯源：抽查 source_quote 逐字核对（low/review 条目全查）
- C 质量：问法合规、答案对题、无重复
- D 安全：无个人信息、无内部信息泄露、无收益承诺表述

生成了三元组时，追加 E 类检查（见 quality-checklist.md）：每条三元组有 source_qa_id、condition 无丢失、同义实体已列入清单。

任何一项不通过，先修正再交付。

### Step 4: 交付

核心三件套，缺一不可：

1. `faq-{主题}-{日期}.md` —— Markdown 表格，供人工评审
2. `faq-{主题}-{日期}.csv` —— CSV，供知识库批量导入
3. **生成报告** —— 按 quality-checklist.md 的"交付报告"章节输出：源文件清单、分类分布、needs_review 条目及原因、未能转化条目的说明、自检结果

可选增强件（用户要求三元组/图谱时交付）：

4. `triples.csv` —— 知识三元组，按 `references/triples-schema.md` 字段规范，每条挂靠问答对
5. `graph.html` —— 交互式知识图谱（内置节点搜索、两节点最短路径查询、邻居子图展开、关系过滤、冲突候选一键高亮），由 `scripts/build_graph.py` 从 triples.csv + `assets/graph-template.html` 模板自动生成；节点按分类标准着色（主体/产品/场景/制度/概念/其他，规则见 `references/triples-schema.md`，CSV 显式列可覆盖自动归类）；生成后**必须用系统浏览器打开**（Windows 执行 `cmd /c start <graph.html 绝对路径>` 或 PowerShell `Start-Process`），不要在工作台内置预览中打开——独立浏览器才能完整加载 CDN 资源与交互功能

交付时明确提醒用户：

- needs_review=yes 的条目必须经人工确认后方可入正式知识库
- triples.csv 是通用图数据格式（subject/object 为节点，predicate+condition 为边属性），可导入任何图数据库或图分析工具，用于冲突检测等机器查询

## 边界（不做的事）

- 不回答用户基于问答对的追问业务问题——本技能只生成问答对，不做问答服务
- 不修改源文件内容，不对制度条文做任何"优化改写"
- 不处理含未脱敏客户个人信息的文件——发现即停止并提示用户先脱敏
- 不在 answer 中补充源文件之外的任何知识，哪怕模型"知道"——知识以库内文件为准

## 迭代与沉淀

用户反馈常见误判或新增问法时，将案例追加到 `references/style-guide.md` 的对应章节（而非写进对话），使规则随使用持续积累。
