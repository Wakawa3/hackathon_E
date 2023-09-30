#test
#test2
#test3
#test4
#内容:複数の座標のうちから、座標をランダムに選んで、座標を返す関数

import random

def creat_dots():

    x_dots=[100,200,300,400]
    random_x = random.choice(x_dots)

    y_dots=[100,200,300,400]
    random_y = random.choice(y_dots)

    print(random_x)
    print(random_y)    
    return (random_x,random_y)

class FoodInfo:
    def __init__(self):
        self.name = ""
        # self.type = ""
        # self.vertical = ""
        # self.horizontal = ""
        self.pos = (0.0, 0.0)

if __name__ == "__main__":
    type_list = ["staple", "main", "side"]
    random.sample(type_list, 3)
    staple_list = ["ご飯", "パスタ"]
    main_list = ["唐揚げ", "ハンバーグ"]
    side_list = ["もやし炒め", "ほうれん草のおひたし"]
    food_list = []
    for type in type_list:
        food_list.append(FoodInfo())
        if(type == "staple"):
            food_list[-1].name = random.choice(staple_list)
            food_list[-1].pos = creat_dots() #仮
        if(type == "main"):
            food_list[-1].name = random.choice(main_list)
            food_list[-1].pos = creat_dots() #仮
        if(type == "side"):
            food_list[-1].name = random.choice(side_list)
            food_list[-1].pos = creat_dots() #仮
    #draw(food_list)