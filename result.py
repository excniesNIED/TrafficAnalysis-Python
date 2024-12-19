import os
import re
import pandas as pd

def natural_sort_key(s):
    """自然排序的辅助函数，用于对文件名进行排序"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def summarize_labels(label_dirs, output_csv):
    results = []

    for label_dir in label_dirs:
        # 按自然排序顺序遍历文件
        for file_name in sorted(os.listdir(label_dir), key=natural_sort_key):
            if file_name.endswith('.txt'):
                people_num = 0
                vehicle_num = 0
                with open(os.path.join(label_dir, file_name), 'r') as file:
                    for line in file:
                        category = int(line.split()[0])
                        if category == 3:
                            people_num += 1
                        elif category in [0, 4, 5, 6, 7]:
                            vehicle_num += 1

                results.append({
                    'image_name': file_name.replace('.txt', ''),
                    'people_num': people_num,
                    'vehicle_num': vehicle_num,
                })

    # 将结果转换为DataFrame
    df_results = pd.DataFrame(results)

    # 保存到CSV文件
    df_results.to_csv(output_csv, index=False)
    print(f"Summary CSV has been created at {output_csv}")

# 标签文件所在目录
label_dirs = [
    r".\runs\detect\exp\labels",
    r".\runs\detect\exp2\labels"
]

# 输出CSV文件的路径
output_csv = r".\Dy2024_287.csv"

# 调用函数
summarize_labels(label_dirs, output_csv)