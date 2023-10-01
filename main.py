import random
import tkinter as tk

class FoodInfo:
    def __init__(self):
        self.name = ""
        # self.type = ""
        self.pos = (0.0, 0.0)


#内容:複数の座標のうちから、座標をランダムに選んで、座標を返す関数
def creat_dots():

    x_dots=[120,240]
    random_x = random.choice(x_dots)

    y_dots=[70,160]
    random_y = random.choice(y_dots)

    return (random_x,random_y)

def check_dup(pos: tuple[int,int], food_list: list[FoodInfo]):
    for food in food_list:
        if food.pos == pos:
            return False
    return True


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")


    # Canvasの作成
    canvas = tk.Canvas(root, bg = "white")
    # Canvasを配置
    canvas.pack(fill = tk.BOTH, expand = True)

    def main_loop():
        type_list = ["staple", "main", "side", "side"]
        random.sample(type_list, 4)
        staple_list = ["ご飯", "パスタ"]
        main_list = ["唐揚げ", "ハンバーグ", "にくじゃが", "コロッケ"]
        side_list = ["もやし炒め", "ほうれん草のおひたし"]
        food_list = []
        for type in type_list:
            food_list.append(FoodInfo())
            if(type == "staple"):
                food_list[-1].name = random.choice(staple_list)
                pos = creat_dots()
                while check_dup(pos, food_list) == False:
                    pos = creat_dots()
                food_list[-1].pos = pos

            if(type == "main"):
                food_list[-1].name = random.choice(main_list)
                pos = creat_dots()
                while check_dup(pos, food_list) == False:
                    pos = creat_dots()
                food_list[-1].pos = pos

            if(type == "side"):
                food_list[-1].name = random.choice(side_list)
                pos = creat_dots()
                while check_dup(pos, food_list) == False:
                    pos = creat_dots()
                food_list[-1].pos = pos

            for food in food_list:
                canvas.create_rectangle(food.pos[0]-60,food.pos[1]+45,food.pos[0]+60,food.pos[1]-45, fill = "white", width = 5)
                canvas.create_text(food.pos[0],food.pos[1], text=food.name, anchor="center", font=("HG丸ｺﾞｼｯｸM-PRO",15))
        
        for i in food_list:
            print(i.name)
            print(i.pos)

    button=tk.Button(root,text="push",command = main_loop)
    button.pack()

    tk.mainloop()