import tkinter as tk
from random import randint
from tkinter import messagebox as mb



MAX = 50

class Task:
    def __init__(self):
        global MAX
        self.x = randint(1, MAX)
        self.y = randint(1, MAX-1)
        self.sign = randint(0, 1)

        if self.sign == 0:
            self.sign = -1

        if self.x + self.y*self.sign < 0:
            temp = self.x
            self.x = self.y
            self.y = temp


        if self.sign == 1:
            label.configure(text=(str(self.x) + '+' + str(self.y)))
        else:
            label.configure(text=(str(self.x) + '-' + str(self.y)))


class Apple:
    def __init__(self):
        task.__init__()
        self.answer = task.x + task.sign*task.y
        self.points = [0, 0]
        self.points_box = []
        self.fake_answers = []
        self.create_rand_pos()


        self.food = []
        self.food_box = []

        self.food_box.append(canvas.create_polygon(self.points_box, outline="red", fill="#fff"))
        self.food.append(canvas.create_text(self.points,text=str(self.answer)))


        self.create_rand_pos()
        self.create_fake_answer()
        self.food_box.append(canvas.create_polygon(self.points_box, outline="red", fill="#fff"))
        self.food.append(canvas.create_text(self.points,text=str(self.fake_answer)))

        self.create_rand_pos()
        self.create_fake_answer()
        self.food_box.append(canvas.create_polygon(self.points_box, outline="red", fill="#fff"))
        self.food.append(canvas.create_text(self.points,text=str(self.fake_answer)))

        # itemcget

    def create_rand_pos(self):
        x = randint(0, 19)
        y = randint(0, 19)
        pos = [i for i in range(100, 300, 10)]
        x = pos[x] + 6
        y = pos[y] + 5
        if self.points[0] == x and self.points[1] == y:
            self.create_rand_pos()
        else:
            self.points = [x, y]
            self.points_box = [x-6, y-5, x-6, y+5, x+5, y+ 5, x+5, y-5]


    def create_fake_answer(self):
        x = randint(-15, 15)
        if x == 0:
            x = -1
        self.fake_answer = self.answer + x
        self.fake_answers.append(self.fake_answer)

class Snake:
    def __init__(self, length):
        x=randint(100, 300)
        y=randint(100, 300)
        x = x // 10 * 10
        y = x // 10 * 10
        self.length = length
        self.prevs = []
        self.prev_x = 10
        self.prev_y = 0
        self.x = x
        self.y = y
        self.iter = 0
        self.speed = 200
        self.direction_x = -10
        self.direction_y = 0
        self.points = [x, y, x, y+10, x+11, y+10, x+11, y]
        self.objects = []
        self.head = canvas.create_polygon(self.points, outline="red", fill="#fff")
        self.points[0] += 10
        self.points[2] += 10
        self.points[4] += 10
        self.points[6] += 10
        for self.i in range(1, self.length):
            self.objects.append(canvas.create_polygon(self.points, outline="green", fill="#fff"))
            self.points[0] += 10
            self.points[2] += 10
            self.points[4] += 10
            self.points[6] += 10
        
        x=randint(0, 500)
        y=randint(0, 500)

    
    def check_collision(self):
        x = canvas.coords(self.head)[0]
        y = canvas.coords(self.head)[1]
        if x >= 500 or x <= 0 or y >= 500 or y <= 0:
            for i in apple.food:
                canvas.delete(i)
            for i in apple.food_box:
                canvas.delete(i)
            self.game_over()
        for j in self.objects:
            if canvas.coords(self.head) == canvas.coords(j):
                self.game_over()

    
    def game_over(self):
        global score
        answer = mb.askyesno("Game Over", "Try again? Your score is " + str(score))
        if answer == 1:
            for i in range(len(self.objects)):
                canvas.delete(self.objects[i])
            canvas.delete(self.head)
            canvas.delete(apple.food)
            del self.objects
            del self.points
            score = 0
            snake.__init__(6)
            apple.__init__()
        else:
            quit()


    def move(self):
        x = canvas.coords(self.head)[0]
        y = canvas.coords(self.head)[1]
        canvas.move(self.head, self.direction_x, self.direction_y)
        temp_x = 0
        temp_y = 0
        prev_y = 0
        prev_x = 0
        for j in self.objects:
            if prev_x == 0 or prev_y == 0:
                prev_y = canvas.coords(j)[1]
                prev_x = canvas.coords(j)[0]
                canvas.move(j, x-prev_x, y-prev_y)
            else:
                temp_x = prev_x
                temp_y = prev_y
                prev_y = canvas.coords(j)[1]
                prev_x = canvas.coords(j)[0]
                canvas.move(j, temp_x-prev_x, temp_y-prev_y)


    def check_food(self):
        global score
        for food in apple.food_box:
            if canvas.coords(self.head)[1] == canvas.coords(food)[1] and canvas.coords(self.head)[0] == canvas.coords(food)[0]:
                for i in apple.food:
                    canvas.delete(i)
                for i in apple.food_box:
                    canvas.delete(i)


                if apple.food_box.index(food) == 0:

                    del apple.food
                    del apple.food_box
                    apple.__init__()
                    score += 10
                    self.length += 1
                    canvas.move(self.head, self.direction_x, self.direction_y)
                    self.points[0] = canvas.coords(self.head)[0] - self.direction_x
                    self.points[2] = canvas.coords(self.head)[2] - self.direction_x
                    self.points[4] = canvas.coords(self.head)[4] - self.direction_x
                    self.points[6] = canvas.coords(self.head)[6] - self.direction_x
                    self.points[1] = canvas.coords(self.head)[1] - self.direction_y
                    self.points[3] = canvas.coords(self.head)[3] - self.direction_y
                    self.points[5] = canvas.coords(self.head)[5] - self.direction_y
                    self.points[7] = canvas.coords(self.head)[7] - self.direction_y
                    self.objects.insert(0, canvas.create_polygon(self.points, outline="green", fill="#fff"))
                    if self.speed > 100:
                        self.speed -= 20
                    elif self.speed > 50:
                        self.speed -= 10
                    elif self.speed > 30:
                        self.speed -= 5
                    elif self.speed > 20:
                        self.speed -= 2
                    self.iter = 0
                    break
                else:
                    self.game_over()
                    break

            else:
                self.iter += 1


    def motion(self):
        self.check_collision()
        self.check_food()
        self.move()
        root.after(self.speed, self.motion)

    def check_event(self, event):
        e = event.keysym
        if e == "Up":
            self.Up()
        if e == "Down":
            self.Down()
        if e == 'Right':
            self.Right()
        if e == 'Left':
            self.Left()


    def Up(self):
        if self.direction_y != 10 and self.direction_y != -10:
            self.direction_y = -10
            self.direction_x = 0


    def Down(self):
        if self.direction_y != 10 and self.direction_y != -10:
            self.direction_y = 10
            self.direction_x = 0

    def Right(self):
        if self.direction_x != 10 and self.direction_x != -10:
            self.direction_x = 10
            self.direction_y = 0

    def Left(self):
        if self.direction_x != 10 and self.direction_x != -10:
            self.direction_x = -10
            self.direction_y = 0

root = tk.Tk()
root.title("Snake")

root.configure(bg='#fff')

label = tk.Label(bg='#fff', text='0+0=?', font=13)
label.pack()

canvas = tk.Canvas(root, bg='#fff', width=500, height=500)
canvas.pack()

score = 0

task = Task()
snake = Snake(6)
apple = Apple()




root.bind_all('<Key>', snake.check_event)

snake.motion()


root.mainloop()



