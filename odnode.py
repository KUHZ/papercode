#omnidirectional node
import turtle

class OdNode():
    def __init__(self,n,radius,px,py):
        self.n = n
        self.radius = radius
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
        node.pendown()
        node.speed(0)
        node.circle(self.radius)
        #print(node.heading())
        #window.exitonclick()
        

#node1 = OdNode(1,50,-100,-200)

#node1.draw()
