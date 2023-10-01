


def hyozi(Food_list:list[FoodInfo]):
    for food in Food_list:
        canvas.create_rectangle(food.pos.index(0)-60,food.pos.index(1)+45,food.pos.index(0)+60,food.pos.index(1)-45, fill = "white", width = 5)
        canvas.create_text(food.pos.index(0),food.pos.index(1), text=food.name, anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",15))
