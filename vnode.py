#video node
import turtle
import math
p1 = math.sqrt(3)
p2 = 1 + p1
vpos = []#position of Vnode
class VNode():
    
    def __init__(self,level,angle,radius,px,py):
        self.level = level
        self.radius = radius
        self.angle = angle #vision of video node
        self.px = px #position x
        self.py = py #position y

    def draw(self):
        #window = turtle.Screen()
        node = turtle.Turtle()
        node.shape("circle")
        node.shapesize(0,0,0)
        node.color("black")
        node.penup()
        node.goto(self.px,self.py)
        #print(node.position())
        vpos.append(node.pos())
        node.pendown()
        node.speed(0)                               
        node.circle(self.radius)
        node.penup()
        node.goto(self.px,self.py-p1*self.radius)
        #print(node.position())
        node.pendown()
        node.circle(p2*self.radius)
        #window.exitonclick()
        

#node1 = VNode(1,1,50,0,-50)

#node1.draw()
