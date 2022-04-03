import turtle
import math
import random

##변수 선언##
t1,t2,t3=[None]*3               #거북이 세마리를 저장할 변수
t1X,t1Y,t2X,t2Y,t3X,t3Y=[0]*6   #각 거북이의 X,Y좌표
swidth,sheight=300,300          #윈도우 창 크기를 저장할 변수

'''
2021041025
강희주
'''

##메인 코드##
if __name__=="__main__":
    turtle.title("거북이 만나기")
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)

    t1=turtle.Turtle("turtle"); t1.color("red"); t1.penup()   #색상이 다른 거북이 세마리 생성
    t2=turtle.Turtle("turtle"); t2.color("green"); t2.penup() #선을 그리지 않도록 penup()
    t3=turtle.Turtle("turtle"); t3.color("blue"); t3.penup()

    t1.goto(-100,-100); t2.goto(0,0); t3.goto(100,100)        #거북이 세마리 초기위치를 서로 다르게 설정

    while True:
        angle=random.randrange(0,360)       #각도 임의 추출
        dist=random.randrange(1,50)         #거리 임의 추출
        t1.left(angle); t1.forward(dist)
        angle=random.randrange(0,360)
        dist=random.randrange(1,50)
        t2.left(angle); t2.forward(dist)
        angle=random.randrange(0,360)
        dist=random.randrange(1,50)
        t3.left(angle); t3.forward(dist)
 
        t1X=t1.xcor(); t1Y=t1.ycor()        #각 거북이의 현재 위치 추출
        t2X=t2.xcor(); t2Y=t2.ycor()
        t3X=t3.xcor(); t3Y=t3.ycor()

                                                                     #거북이끼리 거리 30 이하면 만난 
        if math.sqrt(((t1X-t2X)*(t1X-t2X))+((t1Y-t2Y)*(t1Y-t2Y))) <=30 or \
           math.sqrt(((t1X-t3X)*(t1X-t3X))+((t1Y-t3Y)*(t1Y-t3Y))) <=30 or \
           math.sqrt(((t2X-t3X)*(t2X-t3X))+((t2Y-t3Y)*(t2Y-t3Y))) <=30:
           t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)      #거북이끼리 만나면 크기 세배 확
           break

turtle.done()
