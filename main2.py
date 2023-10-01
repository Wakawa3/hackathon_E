import random
import tkinter as tk
import decide_dots

class FoodBasicInfo:
    def __init__(self, name, type, vertical, horizontal):
        self.name = name
        self.type = type
        self.vertical = vertical
        self.horizontal = horizontal

class FoodInfo(FoodBasicInfo):
    def __init__(self, name, type, vertical, horizontal):
        super().__init__(name, type, vertical, horizontal) #FoodBasicInfoの要素を継承
        self.pos = (0.0, 0.0)
    
    def __init__(self, base: FoodBasicInfo):
        super().__init__(base.name, base.type, base.vertical, base. horizontal)
        self.pos = (0.0, 0.0)
        

def creat_dots():

    x_dots=[120,240]
    random_x = random.choice(x_dots)

    y_dots=[70,160]
    random_y = random.choice(y_dots)

    # print(random_x)
    # print(random_y)    
    return (random_x,random_y)

def check_dup(pos: tuple[int,int], food_list: list[FoodInfo]):
    for food in food_list:
        if food.pos == pos:
            return False
    return True

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x420")


    # Canvasの作成
    canvas = tk.Canvas(root, bg = "white")
    # Canvasを配置
    canvas.pack(fill = tk.BOTH, expand = True)

    def main_loop():
        canvas.delete("all")
        type_list1 = ["staple", "main"]
        type_list1 = random.sample(type_list1, 2)
        type_list2 = ["side", "side","side","side"]
        type_list2 = random.sample(type_list2, 4)

        staple_list = [FoodBasicInfo("ご飯","主食",180,250), FoodBasicInfo("パスタ","主食",180,160)]
        main_list = [FoodBasicInfo("唐揚げ","主菜",300,200), FoodBasicInfo("ハンバーグ","主菜",300,200), FoodBasicInfo("にくじゃが","主菜",200,300), FoodBasicInfo("コロッケ","主菜",200,300)]
        side_list = [FoodBasicInfo("もやし炒め","副菜",100,150), FoodBasicInfo("ほうれん草のおひたし","副菜",100,200), FoodBasicInfo("煮物","副菜",70,200)]
        food_list = []
        i = 0
        for type in type_list1:
            food:FoodBasicInfo
            if(type == "staple"):
                food = random.choice(staple_list)

            if(type == "main"):
                food = random.choice(main_list)

            if(type == "side"):
                food = random.choice(side_list)
            
            # pos = creat_dots()
            pos = decide_dots.decide_dots(food_list,520,420,food.horizontal, food.vertical)
            food_list.append(FoodInfo(food))
            # while check_dup(pos, food_list) == False:
            #     pos = creat_dots()
            food_list[-1].pos = pos
        
        for type in type_list2:
            food:FoodBasicInfo
            if(type == "staple"):
                food = random.choice(staple_list)

            if(type == "main"):
                food = random.choice(main_list)

            if(type == "side"):
                food = random.choice(side_list)
            
            # pos = creat_dots()
            pos = decide_dots.decide_dots(food_list,520,420,food.horizontal, food.vertical)
            food_list.append(FoodInfo(food))
            # while check_dup(pos, food_list) == False:
            #     pos = creat_dots()
            food_list[-1].pos = pos


        for food in food_list:
            if food.pos[0] == 0.0 and food.pos[1] ==0.0:
                continue
            canvas.create_rectangle(food.pos[0]-food.horizontal/2,food.pos[1]+food.vertical/2,food.pos[0]+food.horizontal/2,food.pos[1]-food.vertical/2, fill = "white", width = 5)
            canvas.create_text(food.pos[0],food.pos[1], text=food.name, anchor="center", font=("HG丸ｺﾞｼｯｸM-PRO",15))
            canvas.create_text(food.pos[0],food.pos[1]-20, text=food.type, anchor="center", font=("HG丸ｺﾞｼｯｸM-PRO",10))
            
        for i in food_list:
            print(i.name)
            print(i.pos)
            

    button=tk.Button(root,text="push",command = main_loop)
    button.pack()

    tk.mainloop()