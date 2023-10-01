import random

class FoodBasicInfo:
    def __init__(self, name, vertical, horizontal):
        self.name = name
        # self.type = ""
        self.vertical = vertical
        self.horizontal = horizontal

class FoodInfo(FoodBasicInfo):
    def __init__(self, name, vertical, horizontal):
        super().__init__(name, vertical, horizontal) #FoodBasicInfoの要素を継承
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
    type_list = ["staple", "main", "side", "side"]
    random.sample(type_list, 4)
    staple_list = [FoodBasicInfo("ご飯",120,90), FoodBasicInfo("パスタ",120,90)]
    main_list = [FoodBasicInfo("唐揚げ",120,90), FoodBasicInfo("ハンバーグ",120,90), FoodBasicInfo("にくじゃが",120,90), FoodBasicInfo("コロッケ",120,90)]
    side_list = [FoodBasicInfo("もやし炒め",120,90), FoodBasicInfo("ほうれん草のおひたし",120,90)]
    food_list = []
    for type in type_list:
        if(type == "staple"):
            food = random.choice(staple_list)
            food_list.append(FoodInfo(food.name, food.vertical, food.horizontal))
            pos = creat_dots()
            # pos = creat_dots(food_list[-1].vertical, food_list[-1].horizontal)
            while check_dup(pos, food_list) == False:
                pos = creat_dots()
            food_list[-1].pos = pos

        if(type == "main"):
            food = random.choice(main_list)
            food_list.append(FoodInfo(food.name, food.vertical, food.horizontal))
            pos = creat_dots()
            # pos = creat_dots(food_list[-1].vertical, food_list[-1].horizontal)
            while check_dup(pos, food_list) == False:
                pos = creat_dots()
            food_list[-1].pos = pos

        if(type == "side"):
            food = random.choice(side_list)
            food_list.append(FoodInfo(food.name, food.vertical, food.horizontal))
            pos = creat_dots()
            # pos = creat_dots(food_list[-1].vertical, food_list[-1].horizontal)
            while check_dup(pos, food_list) == False:
                pos = creat_dots()
            food_list[-1].pos = pos

    #draw(food_list) #ここで描画
    
    for i in food_list:
        print(i.name)
        print(i.pos)