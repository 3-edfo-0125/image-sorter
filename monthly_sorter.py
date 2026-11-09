import os
from tkinter import filedialog
import sys

home_dir = os.path.expanduser('~')
base_path = filedialog.askdirectory(initialdir = home_dir)

if not base_path:
    print('フォルダが選択されませんでした')
    sys.exit()

c = 0

# 日付フォルダを全部スキャン
for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if not os.path.isdir(folder_path):
        continue  # フォルダだけ対象

    for f in os.listdir(folder_path):
        full_path = os.path.join(folder_path, f)
        if not os.path.isfile(full_path):
            continue
        if not f.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        # 日付フォルダ名から年月を取得
        # フォルダ名が 'YYYY-MM-DD' の場合
        year_month = '-'.join(folder.split('-')[:2])
        month_folder_path = os.path.join(base_path, year_month)
        os.makedirs(month_folder_path, exist_ok=True)

        # 移動
        new_path = os.path.join(month_folder_path, f)
        os.rename(full_path, new_path)
        c = c + 1

    # 元の日付フォルダが空になったら削除
    if not os.listdir(folder_path):
        os.rmdir(folder_path)

print(c, '枚の画像を整理しました')