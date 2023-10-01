import random


#縦横の長さ1組を引数、例(100,100)
# 計算した座標を返す
def decide_dots(bento_width, bento_height, 
                number, 
                min_width, 
                max_width, 
                min_height, 
                max_height):
    
    box =[]
    for a in range(number):
        x_width = random.randint(min_width, max_width)
        y_height = random.randint(min_height,max_height)
        x = random.randint(0,bento_width - x_width)
        y = random.randint(0,bento_height - y_height)

        box.append((x,y,x_width,y_height))

    return box


