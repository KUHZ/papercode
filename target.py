import turtle
import random

tarpos = []

class Target:
     def __init__(self,steplength,step,p,drawpath):
         self.steplength = steplength
         self.step = step
         self.drawpath = drawpath
         self.p = p 
        
         
     def draw(self):
         #window = turtle.Screen()
         tar = turtle.Turtle()
         tar.speed(0)
         tar.color("red")
         tar.penup()
         tar.setpos(self.p)#set start position
         tarpos.append(tar.position())
         if self.drawpath == 1:
             tar.pendown()
         for i in range (0,self.step):
             tar.right(random.randrange(0,360))
             tar.forward(self.steplength)
             tarpos.append(tar.position())
         #window.exitonclick()
     
     def returntarpos(self):
         return tarpos

     def deltarpos(self):
          del tarpos[:]
        
'''     
tar1 = Target(10,20,10,20,0)
tar1.draw()
print tar1.returntarpos()
'''
