import turtle as t 
import random 
import time

def find_card(x, y):
    min_idx = -1
    min_dis = 100
    for i in range(16):
        distance = turtles[i].distance(x, y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i 
    return min_idx 

def hide_cards(first, second):
    turtles[first].shape(default_img)
    turtles[second].shape(default_img)

def play(x, y):
    global click_num  
    global score  
    global attemp 
    global first_pick 
    global second_pick 
    
    if attemp >= 12:
        t.goto(0, -60)
        t.write("Game over", False, "center", ("", 30, "bold"))
        return
    
    click_num += 1
    card_idx = find_card(x, y)
    print(f"Clicked on card index: {card_idx}")  

    if card_idx != -1 and turtles[card_idx].shape() == default_img:  # 기본 이미지일 때만 클릭 가능
        turtles[card_idx].shape(img_list[card_idx]) 
        
        if first_pick == 0:
            first_pick = card_idx
        elif second_pick == 0:
            second_pick = card_idx
            
            # 카드 매칭 확인
            if img_list[first_pick] == img_list[second_pick]:
                score += 1
                print("매칭 성공!")
                first_pick = 0
                second_pick = 0
            else:
                # 매칭 실패 시 카드 숨기기
                t.ontimer(lambda: hide_cards(first_pick, second_pick), 1000)  # 1초 후 카드 숨기기
                first_pick = 0
                second_pick = 0
            
            attemp += 1

t.bgcolor("pink")
t.setup(700, 700)
t.penup()
t.hideturtle()
t.goto(0, 280)
t.write("카드매칭게임", False, "center", ("", 30, ''))

turtles = [] 

pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.color("pink")
        new_turtle.speed(0)
        new_turtle.goto(pos_x[x], pos_y[y])
        turtles.append(new_turtle)

default_img = "images/default_img.gif"
t.addshape(default_img)

img_list = []

for y in range(8):
    img = f"images/img{y}.gif"
    t.addshape(img)
    img_list.append(img)
    img_list.append(img)
random.shuffle(img_list)

for i in range(16):
    turtles[i].shape(default_img)  # 초기 상태에서 기본 이미지로 설정
    
click_num = 0
score = 0 
attemp = 0 
first_pick = 0 
second_pick = 0 

t.onscreenclick(play)

t.mainloop()
