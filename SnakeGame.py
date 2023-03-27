from tkinter import *
import random
import math
GAME_width = 1000
GAME_height = 700

SPEED = 100
SPACE_size = 50
BODY_PARTS = 1
SNAKE_color = "#0D82A8"
FOOD_color = "#FF0000"
BACKGROUND_COlOR = "#000000"

class Snake:
    def __init__(self):
        global SNAKE_color
        self.body = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x + SPACE_size,y + SPACE_size,fill=SNAKE_color,tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x = random.randint(0,(GAME_width/SPACE_size)-1)*SPACE_size
        y = random.randint(0,(GAME_height/SPACE_size)-1)*SPACE_size

        self.coordinates = [x,y]

        canvas.create_oval(x,y,x+SPACE_size,y+SPACE_size,fill=FOOD_color,tag="food")

def getRandomColor():
    letters = '0123456789ABCDEF';
    color = '#';
    for  i in range(6):
        color += random.choice(letters);
   
    return color; 


def next_turn(snake,food):
    x , y = snake.coordinates[0]

    if direction =="up":
        y -=SPACE_size
    elif direction == "down":
        y += SPACE_size
    elif direction == "left":
        x -= SPACE_size
    elif direction == "right":
        x += SPACE_size


    
    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y,x+SPACE_size,y+SPACE_size,fill="#00FF00")

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y ==food.coordinates[1]:
        global BODY_PARTS
        global score

        score+=1
        BODY_PARTS -=1
        label.config(text="Score:{}".format(score))
        SNAKE_color=getRandomColor()
        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED,next_turn,snake,food)

def change_direction(new_direction):
    global direction

    if new_direction =="left":
        if direction !="right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction =="up":
        if direction !="down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

def check_collision(snake):
    x,y =snake.coordinates[0]

    if x<0 or x>=GAME_width:
        return True
    elif y<0 or y>=GAME_height:
        return True

    for body_part in snake.coordinates[1:]:
        if x== body_part[0] and y ==body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       font=("consolas",70), text="GAME OVER", fill="red" , tag="game_over")


window = Tk()
window.title("Snake Game")
window.resizable(False,False)

score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score),font=("consolas",40))
label.pack()

canvas = Canvas(window,bg=BACKGROUND_COlOR,height=GAME_height,width=GAME_width)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int(screen_width/2-(window_width/2))
y = int(screen_height/2-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake,food)


window.mainloop()