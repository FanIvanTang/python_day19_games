from turtle import Turtle, Screen
import random


is_race_on = False
s = Screen()

s.setup(width=500, height=400)
user_bet = s.textinput(
    title="make your bet", prompt="which turtel will win the race? Enter a color: "
)
print(user_bet)

# t.speed('fastest')
# t.penup()
# t.goto(x=-230,y=150)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

y = 145

for c in colors:
    t = Turtle(shape="turtle")
    t.color(c)
    t.penup()
    t.speed("fastest")
    t.goto(x=-230, y=y)
    y -= 50

    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:

    for t in turtles:
        t.forward(random.randint(0, 10))

        if t.pos()[0] >= 230:
            winner = t.color()[0]
            is_race_on = False


if user_bet == winner:
    print(f"You win, the winner is {winner}")
else:
    print(f"You lost, the winner is {winner}")
s.exitonclick()
