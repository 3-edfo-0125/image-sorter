import os
from tkinter import filedialog
import sys
from datetime import datetime

home_dir = os.path.expanduser('~')
path = filedialog.askdirectory(initialdir = home_dir)

if not path:
    print('フォルダが選択されませんでした')
    sys.exit()

c = 0
for f in os.listdir(path):
    full_path = os.path.join(path,f)
    
    if not os.path.isfile(full_path):
        continue
    
    if f.lower().endswith(('.jpg', '.png')):  

        # 画像の更新日を取得
        mtime = os.path.getmtime(full_path)
        rtime = datetime.fromtimestamp(mtime)

        # フォルダを作成
        folder_name = rtime.strftime('%Y-%m-%d')
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # 画像をnew_pathへ
        new_path = os.path.join(folder_path, f)
        if os.path.exists(new_path):
            continue
        os.rename(full_path, new_path)

        c = c + 1

print(c, '枚の画像を整理しました')