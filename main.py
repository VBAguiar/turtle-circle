import turtle

s = turtle.getscreen()
t = turtle.Turtle()
turtle.title('Turtle-circle')
c = 0
t.pen(pencolor='white', speed=600)
turtle.bgcolor('black')

for x in range(1, 40 + 1):
    t.circle(180)
    t.right(100 + c)
    t.circle(180)
    t.left(200 + c)
    c += 40

