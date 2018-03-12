from turtle import*
import turtle
def tree(f_lenght, min_lenght=10):
        turtle.forward(f_lenght)
        if f_lenght > min_lenght:
                turtle.left(45)
                tree(0.6*f_lenght, min_lenght)
                turtle.right(90)
                tree(0.6*f_lenght, min_lenght)
                turtle.left(45)
                turtle.back(f_lenght)

turtle.left(90)
tree(100)
turtle.exitonclick()


    

