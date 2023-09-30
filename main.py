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

sample1=creat_dots()
print(sample1)
