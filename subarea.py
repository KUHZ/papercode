#subarea
import vnode
import odnode
import math
import turtle
#level = 0
#angle = 60
#r = 5 #radius
#px = 0
#py = -5
p1 = math.sqrt(3)/2
p2 = 3.0/2
class SubArea:
    def __init__(self,level,r,px,py,angle):
        self.level = level
        self.r = r
        self.px = px
        self.py = py
        self.angle = angle

    def draw(self):
        #window = turtle.Screen()
        n = [0,1,2,3,4,5,6]
        n[0] = vnode.VNode(self.level,self.angle,self.r,self.px,self.py)
        n[1] = odnode.OdNode(1,self.r,self.px-p2*self.r,self.py+p1*self.r)
        n[2] = odnode.OdNode(2,self.r,self.px,self.py+p1*2*self.r)
        n[3] = odnode.OdNode(3,self.r,self.px+p2*self.r,self.py+p1*self.r)
        n[4] = odnode.OdNode(4,self.r,self.px+p2*self.r,self.py-p1*self.r)
        n[5] = odnode.OdNode(5,self.r,self.px,self.py-p1*2*self.r)
        n[6] = odnode.OdNode(6,self.r,self.px-p2*self.r,self.py-p1*self.r)
        for i in range(0,7):
            n[i].draw()
        #window.exitonclick()

#sub1 = SubArea(1)
#sub1.draw()
