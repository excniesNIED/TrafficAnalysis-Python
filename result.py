import os
import re
import pandas as pd

def natural_sort_key(s):
    """自然排序的辅助函数，用于对文件名进行排序"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def summarize_labels(label_dir, output_csv):
    # 类别编号到类别名称的映射
    category_mapping = {
        0: 'bus',
        1: 'traffic light',
        2: 'traffic sign',
        3: 'person',
        4: 'bike',
        5: 'truck',
        6: 'motor',
        7: 'car',
        8: 'rider'
    }

    results = []

    # 按自然排序顺序遍历文件
    for file_name in sorted(os.listdir(label_dir), key=natural_sort_key):
        if file_name.endswith('.txt'):
            category_counts = {category: 0 for category in category_mapping.values()}

            with open(os.path.join(label_dir, file_name), 'r') as file:
                for line in file:
                    category_id = int(line.split()[0])
                    category_name = category_mapping.get(category_id, 'unknown')
                    if category_name != 'unknown':
                        category_counts[category_name] += 1

            results.append({
                'image_name': file_name.replace('.txt', ''),
                **category_counts
            })

    # 将结果转换为DataFrame
    df_results = pd.DataFrame(results)

    # 保存到CSV文件
    df_results.to_csv(output_csv, index=False)
    print(f"Summary CSV has been created at {output_csv}")

# 标签文件所在目录
label_dirs = [
    (r"./runs/detect/exp/labels", r"./day_result.csv"),
    (r"./runs/detect/exp2/labels", r"./night_result.csv")
]

# 分别处理每个目录并保存结果
for label_dir, output_csv in label_dirs:
    summarize_labels(label_dir, output_csv)