import random
import main2
import math

def decide_dots(food_list: list[main2.FoodInfo], bento_x, bento_y, yoko, tate):
    # x_pos = 0
    # y_pos = 0

    for x_pos in range(bento_x):
        for y_pos in range(bento_y):
            #これから置く箱の左上、右下
            x1 = x_pos - yoko/2
            y1 = y_pos - tate/2
            x2 = x_pos + yoko/2
            y2 = y_pos + tate/2

            # 各頂点が弁当箱に収まっているか
            if x1 > 0 and y1 > 0 and x2 < bento_x and y2 < bento_y:
                for food in food_list:
                    #foodのはこの左上、右下
                    # food_x1 = food.pos[0] - food.horizontal/2
                    # food_y1 = food.pos[1] - food.vertical/2 
                    # food_x2 = food.pos[0] + food.horizontal/2
                    # food_y2 = food.pos[1] + food.vertical/2 

                    # if (x1 < food_x2 and y1 < food_y2) or (x2 < food_x1 and y1 < food_y1)
                    if (math.fabs(x_pos - food.pos[0]) > yoko/2 + food.horizontal/2) and (math.fabs(y_pos - food.pos[1]) > tate/2 + food.vertical/2):
                        continue
                    else:
                        break
                else:
                    return (x_pos, y_pos)
    
    return (0,0) #エラー　見つからなかった

                
