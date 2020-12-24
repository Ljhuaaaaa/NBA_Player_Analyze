# NBA_Player_Analyze
NBA现役球员分析

##一 数据爬取
对NBA中文网（https://china.nba.com/playerindex/） 进行现役球员的数据爬取。

爬取的字段包括：

姓名，所在球队，位置，身高，体重，NBA年限，国籍，球员详情页url，
场数(职业生涯)，先发(职业生涯)，分钟(职业生涯)，命中率(职业生涯)，三分命中率(职业生涯)
，罚球命中率(职业生涯)，攻击(职业生涯)，防守(职业生涯)，场数(职业生涯)，
场均得分(职业生涯)，场均篮板(职业生涯)，场均助攻(职业生涯)，场均抢断(职业生涯)
，场均盖帽(职业生涯)，失误(职业生涯)，犯规(职业生涯)



##二 数据预处理

处理步骤：

1. 剔除没有出过场的球员

2. 删除球员详情页url列

3. 数据类型转换



##三 数据探索

1.球员身高分布（饼图）

2.球员体重分布（玫瑰图）

3.国籍分布（环形图）

4.球龄分布（条形图）

5.球员数量分布图(地图)



##四 数据建模

使用因子分析对球员计算公因子得分以及综合得分，得到在职业生涯表现TOP5的现役球员

步骤：

1.数据抽取

2.数据标准化

3.逆指标正向化

4.kmo检验和bartlett检验

5.因子分析建模

6.TOP5的现役球员
