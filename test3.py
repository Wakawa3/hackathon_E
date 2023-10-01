import random
import main2

#縦横の長さ1組を引数、例(100,100)
# 計算した座標を返す
def decide_dots(bento_width, bento_height, 
                number, 
                min_width, 
                max_width, 
                min_height, 
                max_height,
                food_list: list[main2.FoodInfo]):
    
    # food_list[0].pos 0番目の品の中心座標を取得
    # food_list[0].horizontal 0番目の品の横の長さが取得
    # food_list[0].vertical 0番目の品の縦の長さが取得

    box =[]
    for a in range(number):
        x_width = random.randint(min_width, max_width)
        y_height = random.randint(min_height,max_height)
        x = random.randint(0,bento_width - x_width)
        y = random.randint(0,bento_height - y_height)

        box.append((x,y,x_width,y_height))

    return box #新しく置く箱の中心座標
    # return (x_pos, y_pos) タプルの形で返す


