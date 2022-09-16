from turtle import *
import turtle
import math


def killturtles(x1,y1,x2,y2):
  t=turtle.Turtle()
  t.pendown()
  t.goto(x1,y1)
  t.penup()
  t.pendown()
  t.goto(x2,y2)
  t.penup()
  gradient1=yfirst/xfirst
  gradient2=ysecond/xsecond
  tantheta=(gradient2-gradient1)/(1+(gradient1*gradient2))
  radians=(math.atan(tantheta))
  print(radians*(180/(math.pi)))


def main():
  print("This program requires you,the user, to enter 2 co-ordinates from which the angle between the 2 lines worked out will be outputted")
  x1=float(input("Enter the x value of your first co-ordinate"))
  y1=float(input("Enter the y value of your first co-ordinate"))
  x2=float(input("Enter the x value of your second co-ordinate"))
  y2=float(input("Enter the y value of your second co-ordinate"))
  killturtles(x1,y1,x2,y2)

if __name__=="__main__":
    main()
