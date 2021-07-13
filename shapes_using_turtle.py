import turtle as t    # aliasing the module name
from turtle import Screen

tutsy_turtle = t.Turtle()
                                # meaning is same as tutsy_turtle = Turtle() but other is pref as its
                                # more expressive like it tells that class comes from t ie turtle module
tutsy_turtle.shape("turtle")
tutsy_turtle.color('DeepPink')

# Active recall - How to calculate each angle?
# keep range as no of times it will repeat or change directions ie sides
# angle for a shape is (360/no.of.sides)  ex triangle its 360/3 ie each angle 180

# choice = int(input("Enter no of sides of figure: "))
def draw_shape(no_of_sides):
    angle = 360/no_of_sides
    for _ in range(no_of_sides):
        tutsy_turtle.forward(100)
        tutsy_turtle.right(angle)


for i in range(3, 11):       # AR - what does it do?
    draw_shape(i)

screen = Screen()
screen.exitonclick()