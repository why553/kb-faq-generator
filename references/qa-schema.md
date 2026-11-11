# 问答对字段规范（QA Schema）

每条生成的问答对必须包含以下全部字段，缺一不可。字段名固定，顺序固定，不得增删改名。

| 字段 | 类型 | 说明 | 示例 |
|---|---|---|---|
| qa_id | string | 问答对唯一编号，格式 `QA-{来源文件序号3位}-{条目序号3位}`，如 `QA-001-003` | QA-001-003 |
| question | string | 用户视角的问题，见 style-guide.md 的改写规则 | 数字人民币实名钱包计息吗？ |
| question_type | string | 问型分类，见下方问型分类定义 | fact |
| user_profile | string | 提问者画像，见下方画像分类定义 | novice |
| answer | string | 基于原文的回答，不得引入原文之外的信息 | 计息。自2026年1月1日起…… |
| source_file | string | 依据的源文件名 | 数字人民币白皮书.pdf |
| source_location | string | 出处定位：章节号/页码/条款号，尽量精确 | 第二章第3节，第12页 |
| source_quote | string | 支撑答案的原文片段（原文摘录，不得改写），不超过100字 | "实名钱包余额自2026年1月1日起按……计付利息" |
| category | string | 主题分类，从知识库主题体系中选取（如：基础概念/钱包管理/计息规则/受理环境/智能合约/其他） | 计息规则 |
| audience | string | 目标使用场景：`internal`（员工内部）/ `customer`（对客答复，需更谨慎）/ `both` | internal |
| confidence | enum | `high`（制度原文直接依据）/ `medium`（培训材料或间接推导）/ `low`（需人工确认） | high |
| needs_review | enum | `yes` / `no`。出现以下任一情况必须为 yes：confidence=low；答案涉及具体金额/期限/利率；原文表述存在歧义；答案跨越多个条款综合推断 | no |
| review_note | string | needs_review=yes 时必填，说明需要人工确认什么 | 涉及计息利率具体数值，请与运营条线核对 |

## 问型多样性矩阵（question_type 与 user_profile）

灵感来自 DataMorgana（ACL 2025）：单条问答对的质量不是瓶颈，问法单一才是。模型天然只会生成什么是X这种直球问题，导致入库后只能答住一种问法。解决方式是给每条问答对标两个维度，批量生成时强制分布。

### question_type 取值（6 类）

| 取值 | 含义 | 典型问法 |
|---|---|---|
| fact | 事实型，问某个定义或数值 | 什么是实名钱包？/ 单笔限额是多少？ |
| procedure | 流程型，问操作步骤 | 怎么把匿名钱包升级成实名钱包？ |
| condition | 条件型，问资格或前提 | 什么条件才能开对公钱包？ |
| comparison | 对比型，问区别或选择 | 软钱包和硬钱包有什么区别？ |
| exception | 异常型，问出错怎么办 | 钱包开立失败怎么办？ |
| reasoning | 推理型，需要结合多条信息得出答案 | 我月转账超限额了，还有别的办法吗？ |

### user_profile 取值（3 类）

| 取值 | 含义 | 问题风格 |
|---|---|---|
| novice | 新手员工或普通客户 | 口语化短句，不用术语：钱包里的钱有利息吗？ |
| expert | 熟练员工 | 可用业务术语，问得具体：M0 定位下实名钱包的计息口径是什么？ |
| reviewer | 检查或审核人员 | 偏核对视角：实名钱包计息的依据条款是哪一条？ |

### 分布要求（生成与自检都按此执行）

1. 每批 10 条及以上的问答对，question_type 至少覆盖 3 类，user_profile 至少覆盖 2 类
2. 同一知识点的多条问答对（含同义问法）必须使用不同的 question_type 或不同的 user_profile，禁止只是换个问号的重复
3. reasoning 类数量占比建议不超过 20%，且每条 reasoning 必须挂靠多条原文（对应多个出处时拆分成多条问答对再综合，需标 needs_review=yes）
4. 生成报告必须附问型分布统计（question_type 与 user_profile 的计数矩阵），分布不达标时先补齐再交付

## 输出格式

1. **主交付物**：Markdown 表格（用于人工阅读、评审）
2. **入库交付物**：CSV 文件（UTF-8 with BOM，用于批量导入知识库），文件名 `{主题}-{日期YYYYMMDD}-faq.csv`
3. 两种格式内容必须完全一致，同一批生成，不允许只交付其一。

## 禁止事项

- 禁止编造 source_quote：引用必须是源文件原文，逐字摘录
- 禁止在 answer 中添加原文没有的数字、日期、金额
- 禁止合并多个 source_location 到一条问答对（一条问答对一个精确出处；综合型问题拆成多条）
- 禁止生成 needs_review=yes 但 review_note 为空的条目
