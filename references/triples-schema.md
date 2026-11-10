# 知识三元组规范（Triples Schema）

三元组是问答对的机器可读形态：问答对给人看，三元组给图谱/程序用。仅在用户要求"同时抽取三元组"时生成本交付物。

## 字段定义

| 字段 | 类型 | 说明 | 示例 |
|---|---|---|---|
| triple_id | string | 唯一编号，`T-{来源文件序号3位}-{条目序号3位}` | T-001-001 |
| subject | string | 主语实体名（名词短语，≤15字） | 实名钱包 |
| predicate | string | 谓语关系（动词或动词短语） | 计付利息 |
| object | string | 宾语实体名或属性值 | 利息 |
| condition | string | 限定条件（时间/地域/主体范围），无则留空 | 自2026-01-01 |
| polarity | enum | `positive`（肯定）/ `negative`（否定） | positive |
| source_qa_id | string | 挂靠的问答对编号，必填（三元组不独立存在） | QA-001-001 |
| source_file | string | 源文件名 | 数字人民币计息新规公告.pdf |
| source_location | string | 出处定位 | 第2条 |

## 抽取规则

1. **每条三元组必须挂靠一条已生成的问答对**（source_qa_id），禁止从源文件直接抽取独立三元组——保证三元组与问答对同源、可互查
2. **condition 必填抽取**：原文中一切时间、地域、适用范围限定语进入 condition 字段。宁可 condition 冗长，不可丢失限定条件——丢失条件的三元组是错误知识
3. **否定语义用 polarity=negative 表达**（如"不计息"），而不是把否定词塞进 predicate
4. **实体归一化**：同一概念的不同叫法（"数币钱包/数字人民币钱包/实名钱包"）在生成报告中列出"同义实体清单"，交人工归一；首次出现按原文命名
5. **数值型宾语**保留原始数值+单位，如 object="1.5%"，不要抽成"有利率"
6. 不抽取模糊、歧义、修辞性的句子；跳过的在生成报告中说明

## 后续用途（写进交付说明）

- 生成图谱：运行 `scripts/build_graph.py triples.csv -o graph.html`，自动转换为交互式图谱网页（系统浏览器打开）
- 机器查询：subject/object 为节点，predicate+condition 为边属性，polarity 用于冲突检测；格式通用，可导入任何图数据库或图分析工具
- 冲突候选：同一对 (subject, object) 之间存在 polarity 相反或语义相反的 predicate → 高优先级人工复核
