import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def draw_charts(canvas):
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

    # 创建图表
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x_day, day_total_counts, width=bar_width, label='DAY', alpha=0.7)
    ax.bar(x_night, night_total_counts, width=bar_width, label='Night', alpha=0.7)

    # 设置图表标题和标签
    ax.set_title('Total Counts of Each Road Condition')
    ax.set_xlabel('Road Condition')
    ax.set_ylabel('Count')
    ax.set_xticks(x)
    ax.set_xticklabels(road_conditions, rotation=45)
    ax.legend()

    # 清除之前的图表
    for widget in canvas.winfo_children():
        widget.destroy()

    # 将新的图表嵌入到 Canvas 中
    canvas_widget = FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget.draw()
    canvas_widget.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)