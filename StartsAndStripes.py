# -*- coding:utf-8 -*-
import turtle

#星条旗的大框
def drawBigRect() :
    turtle.up()
    turtle.goto(-380, 200)
    turtle.down()
    turtle.fd(760)
    turtle.right(90)
    turtle.fd(400)
    turtle.right(90)
    turtle.fd(760)
    turtle.right(90)
    turtle.fd(400)
    turtle.right(90)

#星条旗的小框
def drawSmallRect() :
    turtle.color("blue")
    turtle.begin_fill()
    turtle.fd(304)
    turtle.right(90)
    turtle.fd(215.4)
    turtle.right(90)
    turtle.fd(304)
    turtle.right(90)
    turtle.fd(215.4)
    turtle.end_fill()
    turtle.right(90)

#星条旗红色条纹
def drawRedStripes(x, y, len = 760) :
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color("red")
    turtle.begin_fill()
    turtle.fd(len)
    turtle.left(90)
    turtle.fd(30.76)
    turtle.left(90)
    turtle.fd(len)
    turtle.left(90)
    turtle.fd(30.76)
    turtle.end_fill()
    turtle.left(90)

#小框的星星
def drawStar(x, y) :
    turtle.up()
    turtle.goto(x-12.32, y)
    turtle.down()
    turtle.color("white")
    turtle.begin_fill()
    turtle.fd(24.64)
    turtle.right(144)
    turtle.fd(24.64)
    turtle.right(144)
    turtle.fd(24.64)
    turtle.right(144)
    turtle.fd(24.64)
    turtle.right(144)
    turtle.fd(24.64)
    turtle.end_fill()
    turtle.right(144)

drawBigRect()

drawSmallRect()

#小框内的星星
for idx in range(0, 9) :
    if idx % 2 == 0 :
        for idj in range(0, 6) :
            spacex = 25.32
            spacey = 21.52
            drawStar(-380 + idj * 2 * spacex + spacex, 200 - idx * spacey - spacey)
    else :
        for idj in range(0, 5) :
            spacex = 25.32 * 2
            spacey = 21.52
            drawStar(-380 + idj * spacex + spacex, 200 - idx * spacey - spacey)

#长的红色条纹
for idx in range(0, 3) :
    drawRedStripes(-380, -200 + idx * 2 * 30.76)
#短的红色条纹
for idx in range(0, 4) :
    drawRedStripes(-380 + 304, -215.4 + 200 + idx * 2 * 30.76, 456)

#画完隐藏箭头
turtle.hideturtle()

input("enter key to exit")