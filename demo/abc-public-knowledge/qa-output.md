# 生成产物：农业银行公开业务知识问答对

生成批次：QA-101（来源文件 demo/abc-public-knowledge/source-material.md）
生成模式：kb-faq-generator，问答对输出，不生成图谱（按用户要求跳过三元组渲染）
字段规范：references/qa-schema.md 16 字段
说明：source_quote 引用的官方公示原文保留原标点（含分号与半角逗号），属逐字引用，不受本 skill 行文风格约束。

## 问答对清单

### QA-101-001
- question: 个人通过柜台跨行转账，手续费怎么收？
- question_type: fact | user_profile: novice
- difficulty_retrieval: easy | difficulty_reasoning: direct
- answer: 个人通过柜台办理跨行转账汇款，手续费按政府指导价分档收取。0.2万元以下每笔2元，0.2万至0.5万元每笔5元，0.5万至1万元每笔10元，1万至5万元每笔15元，5万元以上按汇款金额的0.03%收取，最高不超过50元。也可使用掌上银行等电子渠道办理，有机会享受更优惠的费率。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：个人通过柜台办理跨行转账汇款，手续费按政府指导价分档收取。0.2万元以下每笔2元，0.2万至0.5万元每笔5元，0.5万至1万元每笔10元，1万至5万元每笔15元，5万元以上按汇款金额的0.03%收取，最高不超过50元。您也可以使用掌上银行等电子渠道办理，有机会享受更优惠的费率。相关收费与利率标准以正式公示为准。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（政府指导价政府定价项目价格标准）
- source_location: 政府指导价第1项
- source_quote: 每笔0.2万元以下(含0.2万元),每笔收费2元;0.2万-0.5万元(含0.5万元),每笔收费5元;0.5万-1万元(含1万元),每笔收费10元;1万-5万元(含5万元),每笔收费15元;5万元以上,每笔按汇款金额的0.03%收取,最高不超过50元
- category: 收费标准 | audience: external | confidence: high
- needs_review: yes | review_note: 涉及具体金额，需业务部门复核后启用

### QA-101-002
- question: 我要转3万元，柜台跨行转账手续费是多少？
- question_type: fact | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: calculation
- answer: 3万元属于1万至5万元档，柜台跨行转账手续费为每笔15元。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：3万元属于1万至5万元档，柜台跨行转账手续费为每笔15元。相关收费与利率标准以正式公示为准。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（政府指导价政府定价项目价格标准）
- source_location: 政府指导价第1项
- source_quote: 1万-5万元(含5万元),每笔收费15元
- category: 收费标准 | audience: external | confidence: high
- needs_review: yes | review_note: 涉及具体金额，需业务部门复核后启用

### QA-101-003
- question: 柜台跨行转账多长时间能到账，能不能加急？
- question_type: condition | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: direct
- answer: 柜台跨行转账汇款资金应不迟于2个工作日内到账。如需实时到账，可选择实时到账方式，收费标准在普通标准基础上上浮不超过20%，每笔最高收费标准不变。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：柜台跨行转账汇款资金应不迟于2个工作日内到账。如需实时到账，可选择实时到账方式，收费标准在普通标准基础上上浮不超过20%，每笔最高收费标准不变。以上内容可能随政策调整发生变化，请以最新官方公告为准。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（政府指导价政府定价项目价格标准）
- source_location: 价目表备注第1条
- source_quote: 汇款金额应不迟于2个工作日内到账 若银行客户要求实时到账,收费标准在此基础上上浮不超过20%,但每笔最高收费标准不变
- category: 收费标准 | audience: external | confidence: high
- needs_review: yes | review_note: 涉及费率上浮比例，需业务部门复核后启用

### QA-101-004
- question: 个人现金汇款收多少手续费？
- question_type: fact | user_profile: novice
- difficulty_retrieval: easy | difficulty_reasoning: direct
- answer: 个人现金汇款手续费按汇款金额的0.5%收取，最高不超过50元。向本行账户的个人现金汇款目前暂免收费。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：个人现金汇款手续费按汇款金额的0.5%收取，最高不超过50元。向本行账户的个人现金汇款目前暂免收费。相关收费与利率标准以正式公示为准。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（政府指导价政府定价项目价格标准）
- source_location: 政府指导价第3项及备注
- source_quote: 每笔按汇款金额的0.5%收费,最高不超过50元 本行个人现金汇款暂免收费
- category: 收费标准 | audience: external | confidence: high
- needs_review: yes | review_note: 涉及具体金额，需业务部门复核后启用

### QA-101-005
- question: 柜台跨行转账手续费的定价依据是哪份文件？
- question_type: fact | user_profile: reviewer
- difficulty_retrieval: structural | difficulty_reasoning: direct
- answer: 个人跨行柜台转账汇款手续费的收费依据为发改价格[2014]268号。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：个人跨行柜台转账汇款手续费的收费依据为发改价格[2014]268号。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（政府指导价政府定价项目价格标准）
- source_location: 政府指导价第1项收费依据列
- source_quote: 发改价格[2014]268号
- category: 收费标准 | audience: internal | confidence: high
- needs_review: no | review_note:

### QA-101-006
- question: 办支票、本票还要交工本费和挂失费吗？
- question_type: fact | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: direct
- answer: 自2021年9月30日起，支票的工本费和挂失费，以及本票和银行汇票的手续费、工本费、挂失费均已取消收取。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：自2021年9月30日起，支票的工本费和挂失费，以及本票和银行汇票的手续费、工本费、挂失费均已取消收取。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（政府指导价政府定价项目价格标准）
- source_location: 价目表备注第3条
- source_quote: 自2021年9月30日起,取消收取支票工本费、挂失费,以及本票和银行汇票的手续费、工本费、挂失费
- category: 收费标准 | audience: external | confidence: high
- needs_review: yes | review_note: 涉及收费项目变动，需业务部门复核后启用

### QA-101-007
- question: 借记卡年费和小额账户管理费怎么免？
- question_type: condition | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: direct
- answer: 客户可申请对本行一个指定账户（不含信用卡、贵宾账户）免收年费和账户管理费。未申请的，我行会主动对客户在本行开立的唯一账户免收年费和账户管理费。持有多个账户的客户可前往网点办理免费账户申请手续。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：客户可申请对本行一个指定账户（不含信用卡、贵宾账户）免收年费和账户管理费。未申请的，我行会主动对客户在本行开立的唯一账户免收年费和账户管理费。如需指定其他账户享受免费政策，请您携带本人有效身份证件前往网点办理申请手续。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（免费服务项目）
- source_location: 免费项目第2项及备注
- source_quote: 对其指定的一个本行账户(不含信用卡、贵宾账户)免收年费和账户管理费(含小额账户管理费,下同)。客户未申请的,主动对其在本行开立的唯一账户(不含信用卡、贵宾账户),免收年费和账户管理费
- category: 免费项目 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-008
- question: 个人养老金资金账户有哪些费用减免？
- question_type: fact | user_profile: novice
- difficulty_retrieval: easy | difficulty_reasoning: direct
- answer: 个人养老金资金账户免收年费、账户管理费、短信费、转账手续费。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：个人养老金资金账户免收年费、账户管理费、短信费、转账手续费。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（免费服务项目）
- source_location: 免费项目第5项
- source_quote: 个人养老金资金账户免收年费、账户管理费、短信费、转账手续费
- category: 免费项目 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-009
- question: 在外地农行柜台取现金要收手续费吗？
- question_type: condition | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: direct
- answer: 个人异地本行柜台取现手续费免收，信用卡取现除外。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：个人异地本行柜台取现手续费免收，信用卡取现除外。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（免费服务项目）
- source_location: 免费项目第3项
- source_quote: 个人异地本行柜台取现手续费(不含信用卡取现)
- category: 免费项目 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-010
- question: 一个人最多能开几张农行借记卡？
- question_type: fact | user_profile: novice
- difficulty_retrieval: easy | difficulty_reasoning: direct
- answer: 个人客户在中国农业银行开立借记卡（含附属卡）每人不得超过4张。社会保障卡、医疗保险卡、军人保障卡、已销户的借记卡不计算在内。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：个人客户在中国农业银行开立借记卡（含附属卡）每人不得超过4张。社会保障卡、医疗保险卡、军人保障卡、已销户的借记卡不计算在内。开卡请您本人携带有效身份证件前往我行网点办理。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 金穗借记卡章程ABC(2021)4001
- source_location: 第三条
- source_quote: 个人客户在中国农业银行开立借记卡(含附属卡)每人不得超过4张。社会保障卡、医疗保险卡、军人保障卡、已销户的借记卡除外。
- category: 借记卡章程 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-011
- question: 卡是家人帮我办的，我自己怎么激活？
- question_type: process | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: direct
- answer: 委托他人代理申领的借记卡，须持卡人本人凭借记卡及本人有效身份证件，到中国农业银行指定网点办理激活。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：委托他人代理申领的借记卡，须持卡人本人凭借记卡及本人有效身份证件，到中国农业银行指定网点办理激活。请您携带卡片和本人有效身份证件前往网点办理。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 金穗借记卡章程ABC(2021)4001
- source_location: 第四条
- source_quote: 委托他人代理申领金穗借记卡的,须持卡人本人凭借记卡及本人有效身份证件到中国农业银行指定网点办理激活。
- category: 借记卡章程 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-012
- question: Ⅰ类户借记卡和Ⅱ类户借记卡有什么区别？
- question_type: comparison | user_profile: novice
- difficulty_retrieval: structural | difficulty_reasoning: comparison
- answer: Ⅰ类户借记卡具有存取现金、转账结算、消费、购买投资理财、缴费等全部或部分功能。Ⅱ类户借记卡具有限定金额存取现金、非绑定账户转账结算、购买投资理财等金融产品、消费和缴费支付等功能。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：Ⅰ类户借记卡具有存取现金、转账结算、消费、购买投资理财、缴费等全部或部分功能。Ⅱ类户借记卡具有限定金额存取现金、非绑定账户转账结算、购买投资理财等金融产品、消费和缴费支付等功能。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 金穗借记卡章程ABC(2022)4001
- source_location: 第一条
- source_quote: Ⅰ类户借记卡具有存取现金、转账结算、消费、购买投资理财、缴费等全部或部分功能,Ⅱ类户借记卡具有限定金额存取现金、非绑定账户转账结算、购买投资理财等金融产品、消费和缴费支付等功能。
- category: 借记卡章程 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-013
- question: 我想给家里人办一张附属卡，可以吗？
- question_type: condition | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: direct
- answer: Ⅰ类户借记卡申领人可为本人或其近亲属（配偶、父母、子女等）申领附属卡，贵宾卡不设附属卡。我行不向附属卡提供开立个人存款证明和投资理财服务。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：Ⅰ类户借记卡申领人可为本人或其近亲属（配偶、父母、子女等）申领附属卡，贵宾卡不设附属卡。请注意，我行不向附属卡提供开立个人存款证明和投资理财服务。开卡请您本人携带有效身份证件前往我行网点办理。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 金穗借记卡章程ABC(2021)4001
- source_location: 第一条
- source_quote: Ⅰ类户借记卡申领人可为本人或其近亲属(配偶、父母、子女等)申领附属卡(贵宾卡不设附属卡) 中国农业银行不向附属卡提供开立个人存款证明和投资理财服务。
- category: 借记卡章程 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-014
- question: 卡丢了，卡里的电子现金能挂失吗？
- question_type: abnormal | user_profile: novice
- difficulty_retrieval: structural | difficulty_reasoning: direct
- answer: 电子现金视同现金，不计息，不挂失。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：电子现金视同现金，不计息，不挂失。卡片丢失建议您立即通过掌上银行安全中心对卡片进行紧急止付，或携带本人有效身份证件前往就近网点办理挂失。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 金穗借记卡章程ABC(2022)4001
- source_location: 第六条
- source_quote: 电子现金视同现金,不计息,不挂失。
- category: 借记卡章程 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-015
- question: 单位卡账户的资金怎么存入？
- question_type: process | user_profile: expert
- difficulty_retrieval: structural | difficulty_reasoning: direct
- answer: 金穗借记卡单位卡账户的资金必须由申领单位基本存款账户转账存入，不得办理现金收付业务。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：金穗借记卡单位卡账户的资金必须由申领单位基本存款账户转账存入，不得办理现金收付业务。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 金穗借记卡章程ABC(2021)4001
- source_location: 第五条
- source_quote: 金穗借记卡单位卡账户的资金必须由申领单位基本存款账户转账存入,不得办理现金收付业务。
- category: 借记卡章程 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-016
- question: 在ATM上跨行转账，每天最多能转多少，多久到账？
- question_type: condition | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: direct
- answer: 自助设备跨行转账每日累计限额一般在50000元以下，各地略有不同。跨行转账实时到账。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：自助设备跨行转账每日累计限额一般在50000元以下，各地略有不同。跨行转账实时到账。以上内容可能随政策调整发生变化，请以最新官方公告为准。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网自助设备跨行转账业务介绍
- source_location: 每日累计转账限额与到账时间问答
- source_quote: 跨行转账一般在50000元以下,各地略有不同。 跨行轉賬實時到賬的。
- category: 电子银行 | audience: external | confidence: medium
- needs_review: no | review_note:

### QA-101-017
- question: 哪些银行的卡能在农行ATM上办跨行转账？
- question_type: fact | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: direct
- answer: 拥有银联标准卡并通过银联账户验证的银行均可办理自助设备跨行转账。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：拥有银联标准卡并通过银联账户验证的银行均可办理自助设备跨行转账。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网自助设备跨行转账业务介绍
- source_location: 支持银行问答
- source_quote: 拥有银联标准卡并通过银联账户验证的银行均可。
- category: 电子银行 | audience: external | confidence: high
- needs_review: no | review_note:

### QA-101-018
- question: 小微企业柜台跨行转账有手续费优惠吗？
- question_type: condition | user_profile: expert
- difficulty_retrieval: structural | difficulty_reasoning: direct
- answer: 对小微企业和个体工商户通过柜台渠道进行的单笔10万元（含）以下的对公跨行转账汇款业务，按照不高于现行政府指导价的9折实行优惠，优惠期为2024年9月30日至2027年9月30日。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：对小微企业和个体工商户通过柜台渠道进行的单笔10万元（含）以下的对公跨行转账汇款业务，按照不高于现行政府指导价的9折实行优惠，优惠期为2024年9月30日至2027年9月30日。以上内容可能随政策调整发生变化，请以最新官方公告为准。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（政府指导价政府定价项目价格标准）
- source_location: 政府指导价第2项备注
- source_quote: 对小微企业和个体工商户通过柜台渠道进行的单笔10万元(含)以下的对公跨行转账汇款业务,按照不高于现行政府指导价的9折实行优惠,优惠期为2024年9月30日至2027年9月30日
- category: 对公收费 | audience: external | confidence: high
- needs_review: yes | review_note: 涉及优惠期限时效，需业务部门复核后启用

### QA-101-019
- question: 转一笔大额比如20万，柜台跨行转账手续费会不会特别贵？
- question_type: reasoning | user_profile: novice
- difficulty_retrieval: paraphrase | difficulty_reasoning: calculation
- answer: 不会超过50元。柜台跨行转账5万元以上按汇款金额的0.03%收取，最高不超过50元。转20万元按0.03%计算为60元，已超过上限，实际按最高50元收取。
- customer_answer: 您好，关于您咨询的问题，为您解答如下：柜台跨行转账手续费有上限保护，5万元以上按汇款金额的0.03%收取，最高不超过50元。转20万元实际手续费按最高50元收取，不会更高。相关收费与利率标准以正式公示为准。希望以上解答对您有帮助。如有其他疑问，欢迎您随时咨询。
- source_file: 农业银行官网服务价目表（政府指导价政府定价项目价格标准）
- source_location: 政府指导价第1项
- source_quote: 5万元以上,每笔按汇款金额的0.03%收取,最高不超过50元
- category: 收费标准 | audience: external | confidence: high
- needs_review: yes | review_note: 涉及具体金额计算，需业务部门复核后启用

## 生成报告

数量：共 19 条。

问型分布矩阵（question_type × user_profile）：

| question_type | novice | expert | reviewer |
|---|---|---|---|
| fact | 7 | 0 | 1 |
| condition | 5 | 1 | 0 |
| comparison | 1 | 0 | 0 |
| process | 1 | 1 | 0 |
| abnormal | 1 | 0 | 0 |
| reasoning | 1 | 0 | 0 |

问型覆盖 6 类全部，画像覆盖 3 类全部，满足每批至少 3 种问型、2 种画像的要求。

难度分布：

- difficulty_retrieval：easy 4 条，paraphrase 10 条，structural 5 条
- difficulty_reasoning：direct 16 条，calculation 2 条（QA-101-002、QA-101-019），comparison 1 条（QA-101-012）

待人工复审清单（needs_review 为 yes，共 7 条）：QA-101-001、QA-101-002、QA-101-003、QA-101-004、QA-101-006、QA-101-018、QA-101-019。原因均为涉及具体金额、费率或优惠期限，官网公示版本与网点执行版本可能存在时间差，须业务部门复核后方可进入正式话术库。

不适合转问答对的标题：无。本次来源为价目表与章程条文，全部条文均可直接转问答对。

## 溯源校验

全部 19 条的 source_quote 与 source-material.md 逐字比对通过，零误差。两处繁体字形（来源五第 2 条）按页面原样保留。
