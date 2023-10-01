import tkinter as tk
import random

root = tk.Tk()
root.geometry("300x300")

okazu = ["からあげ","にくじゃが","コロッケ"]

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

# 図形の描画 
def hyozi():
    canvas.create_rectangle(20,10,140,100, fill = "white", width = 5)
    canvas.create_rectangle(140,10,260,100, fill = "white", width = 5)
    canvas.create_rectangle(20,100,140,190, fill = "white", width = 5)
    canvas.create_rectangle(140,100,260,190, fill = "white", width = 5)

    canvas.create_text(120,70, text=random.choice(okazu), anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",15))
    canvas.create_text(240,70, text=random.choice(okazu), anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",15))
    canvas.create_text(120,160, text=random.choice(okazu), anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",15))
    canvas.create_text(240,160, text=random.choice(okazu), anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",15))

button=tk.Button(root,text="push",command = hyozi)
button.pack()

tk.mainloop()
