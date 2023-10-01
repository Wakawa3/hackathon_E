import random

def decide_dots(container_width, container_height, 
                number, 
                min_rect_width, 
                max_rect_width, 
                min_rect_height, 
                max_rect_height):
    
    box =[]
    for a in range(number):
        width = random.randint(min_rect_width, max_rect_width)
        height = random.randint(min_rect_height,max_rect_height)
        x = random.randint(0,container_width - width)
        y = random.randint(0,container_height - height)

        box.append((x,y,width,height))

    return box

container_width = 200
container_height = 200
num_rectangles = 5
min_rect_width = 10
max_rect_width = 50
min_rect_height = 10
max_rect_height = 50

rectangles = decide_dots(container_width, container_height, num_rectangles, min_rect_width, max_rect_width, min_rect_height, max_rect_height)

for i, rect in enumerate(rectangles):
    print(f"Rectangle {i+1}: {rect}")
