from turtle import *
import turtle

# 전역 변수
inStr = ''
swidth, sheight = 300, 300
tX, tY, tAngle, tSize = [0]*4

# 메인 코드
turtle.title ('거북이 글자 쓰기 (모듈버전)')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight +50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(5)

inStr = getString()

for ch in inStr : 
    tX, tY, tAngle, tSize = getXYAS(swidth, sheight)
    turtle.pencolor(getRGB())
    
    turtle.goto(tX,tY)
    turtle.left(tAngle)
    
    turtle.write(ch,font=('맑은고딕',tSize, 'bold'))
    
turtle.done() 