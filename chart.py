import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
day_data = pd.read_csv('day_result.csv')
night_data = pd.read_csv('night_result.csv')

# 计算每种路况的总数
day_total_counts = day_data.iloc[:, 1:].sum()
night_total_counts = night_data.iloc[:, 1:].sum()

# 获取路况的标签
road_conditions = day_total_counts.index

# 设置柱状图的宽度
bar_width = 0.35

# 设置柱状图的位置
x = range(len(road_conditions))
x_day = [i - bar_width/2 for i in x]
x_night = [i + bar_width/2 for i in x]

# 绘制簇状柱状图
plt.figure(figsize=(10, 6))
plt.bar(x_day, day_total_counts, width=bar_width, label='DAY', alpha=0.7)
plt.bar(x_night, night_total_counts, width=bar_width, label='Night', alpha=0.7)

# 设置图表标题和标签
plt.title('Total Counts of Each Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Count')
plt.xticks(x, road_conditions, rotation=45)
plt.legend()

# 显示图表
plt.show()