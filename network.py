import turtle
import math
import subarea

p1 = 3 + math.sqrt(3)
p2 = math.sqrt(3)/2
sub = []
vpos = []
vlevel = []

class Network:
      
    def __init__(self,n,r):
        self.n = n #the layer number
        self.j = 0
        self.level = 1
        self.r =r
        self.px = 0
        self.py = 0
        self.angle = 60

    def getpos(self):
        #window = turtle.Screen()
        sub.insert(self.j,subarea.SubArea(0,self.r,self.px,self.py,self.angle))
        vpos.append((self.px,self.py))
        vlevel.append(0)
        #sub[self.j].draw()
        self.j = self.j + 1
        self.px = self.px + p1*self.r
        for n in range(0,self.n-1):
            sub.insert(self.j,subarea.SubArea(self.level,self.r,self.px,self.py,self.angle))
            vpos.append((self.px,self.py))
            vlevel.append(self.level)
            #sub[self.j].draw()
            self.j = self.j + 1
            #print self.j
             
            for i in range(0,self.level):
                self.px = self.px - p1/2*self.r
                self.py = self.py + p2*p1*self.r
                sub.insert(self.j,subarea.SubArea(self.level,self.r,self.px,self.py,self.angle))
                vpos.append((self.px,self.py))
                vlevel.append(self.level)
                #sub[self.j].draw()
                self.j = self.j + 1
                #print self.j
            
            for i in range(0,self.level):
                self.px = self.px - p1*self.r
                sub.insert(self.j,subarea.SubArea(self.level,self.r,self.px,self.py,self.angle))
                vpos.append((self.px,self.py))
                vlevel.append(self.level)
                #sub[self.j].draw()
                self.j = self.j + 1
                #print self.j

            for i in range(0,self.level):
                self.px = self.px - p1/2*self.r
                self.py = self.py - p2*p1*self.r
                sub.insert(self.j,subarea.SubArea(self.level,self.r,self.px,self.py,self.angle))
                vpos.append((self.px,self.py))
                vlevel.append(self.level)
                #sub[self.j].draw()
                self.j = self.j + 1
                #print self.j

            for i in range(0,self.level):
                self.px = self.px + p1/2*self.r
                self.py = self.py - p2*p1*self.r
                sub.insert(self.j,subarea.SubArea(self.level,self.r,self.px,self.py,self.angle))
                vpos.append((self.px,self.py))
                vlevel.append(self.level)
                #sub[self.j].draw()
                self.j = self.j + 1
                #print self.j

            for i in range(0,self.level):
                self.px = self.px + p1*self.r
                sub.insert(self.j,subarea.SubArea(self.level,self.r,self.px,self.py,self.angle))
                vpos.append((self.px,self.py))
                vlevel.append(self.level)
                #sub[self.j].draw()
                self.j = self.j + 1
                #print self.j

            for i in range(0,self.level-1):
                self.px = self.px + p1/2*self.r
                self.py = self.py + p2*p1*self.r
                sub.insert(self.j,subarea.SubArea(self.level,self.r,self.px,self.py,self.angle))
                vpos.append((self.px,self.py))
                vlevel.append(self.level)
                #sub[self.j].draw()
                self.j = self.j + 1
                #print self.j
            
            self.px = self.px + 3*p1/2*self.r
            self.py = self.py + p2*p1*self.r
            self.level = self.level + 1
        #window.exitonclick()

    def printvpos(self):
        print vpos

    def returnvpos(self):
        return vpos

    def returnvlevel(self):
        return vlevel
    
    def draw(self):
        for i in range(0,self.j):
            sub[i].draw()
        
#network1 = Network(1)
#network1.draw()
 
            
      
