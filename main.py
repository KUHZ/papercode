import network
import turtle
import target
import random
import math
import xlsxwriter

nodepowercost = []
transpowerlist = []
detectpowerlist = []
targetlist = []
p1 = 2 + 2*math.sqrt(3)
p2 = 1 + math.sqrt(3)
n = input("please input the layer number:")
r = input("please input the radius of node:")
r2 = ((1+math.sqrt(3))*r)**2
drawpath = input("Do you want to print the target?1/0:")#1 draw,0 not draw
#steplength = input("Please input the length of the step:")
t = input("please input the target unmber:")
step = input("Please input the number of the step:")
net1 = network.Network(n,r)
net1.getpos()
vpos = net1.returnvpos()
for i in range(0,len(vpos)):
    nodepowercost.insert(i,0)
vlevel = net1.returnvlevel()
#print vlevel
#print "vlevel\n"
vposlength = len(vpos)
initalpos = vpos[vposlength-6*n+6:vposlength]
window = turtle.Screen()
#net1.draw()
p = random.choice(initalpos)
workbook = xlsxwriter.Workbook('rawdata.xlsx')
worksheet1 = workbook.add_worksheet('sheet1')
worksheet2 = workbook.add_worksheet('sheet2')
for i in range(0,t):
    p = random.choice(initalpos)
    targetlist.append(target.Target(1.6*p1*r,step,p,drawpath))
    targetlist[i].draw()
    tarpos = targetlist[i].returntarpos()
    transpower = 0
    detectpower = 0
    k=0
    worksheet1.write(i+1,0,i+1) #mark the number of the expriments
    for (tx,ty) in tarpos:
        worksheet1.write(i+1,2*k+1,tx)
        worksheet1.write(i+1,2*k+2,ty)
        k = k+1
        c = 0
        for (vx,vy) in vpos:
            dis2 = (vx-tx)**2+(vy+r-ty)**2
            if dis2 <= r2:
                transpower = transpower + vlevel[c]
                detectpower = detectpower + 1
                #print c
                #print vlevel[c]
                nodepowercost[c] = nodepowercost[c] + 1
            c = c + 1
        #print "\n"
    #print "target position"
    #print tarpos
    worksheet1.write(i+1,2*len(tarpos)+1,transpower)
    worksheet1.write(i+1,2*len(tarpos)+2,detectpower)
    #print "power used for transmission"
    #print transpower
    transpowerlist.append(transpower)
    detectpowerlist.append(detectpower)
    targetlist[i].deltarpos()            
    #print tarpos
v = 0
for (px,py) in vpos:
    worksheet2.write(v+1,1,px)
    worksheet2.write(v+1,2,py)
    worksheet2.write(v+1,3,nodepowercost[v])
    v = v + 1
workbook.close()
print "transpower:"
print transpowerlist
print "detectpower:"
print detectpowerlist
window.exitonclick()


