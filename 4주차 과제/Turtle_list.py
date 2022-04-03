import turtle
import random


##변수 선언##
myTurtle,tX,tY,tColor,tSize,tShape,tSum=[None]*7   #tSum: x좌표와 y좌표의 합
playerTurtles=[] #거북이 2차원 리스트
swidth,sheight=500,500
a=random.randint(1,360)


'''
2021041025
강희주
'''

##메인 코드##
if __name__=="__main__":
    turtle.title("거북이 리스트 활용(정렬)")
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.setheading(a)
      
    
 
    #랜덤으로 거북이 5마리 생성 후 playerTurtles에 넣기
    for i in range(0,5): 
        myTurtle=turtle.Turtle("turtle")               #거북이 개체 생성
        myTurtle.setheading(random.randrange(1, 360))
        tX=random.randrange(-swidth / 2, swidth / 2)   #거북이 위치 tX 생성
        tY=random.randrange(-sheight / 2, sheight / 2) #거북이 위치 tY 생성
        r=random.random(); g=random.random(); b=random.random()
        tSize=random.randrange(1,100)/10
        tSum=tX+tY
        playerTurtles.append([myTurtle,tX,tY,tSize,r,g,b,tSum]) 

    sortedTurtles=sorted(playerTurtles,key=lambda turtles:turtles[7],reverse=True)


    for index,tList in enumerate(sortedTurtles[0:]): #enumerate는 index값을 원소와 함께 반환해줌
        myTurtle=tList[0]
        myTurtle.color((tList[4],tList[5],tList[6]))
        myTurtle.pencolor((tList[4],tList[5],tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        if index==0:    #첫 번째 거북이는 이전 거북이가 없기 때문에 
            myTurtle.goto(tList[1],tList[2]) #해당 위치로만 이동
            continue

        #선을 그을 거북이를 이전의 거북이 위치로 이동
        myTurtle.goto(sortedTurtles[index-1][1],sortedTurtles[index-1][2]) 

        myTurtle.pendown()               #선 긋기
        myTurtle.goto(tList[1],tList[2]) #설정된 거북이의 좌표로 이동

turtle.done()


 
