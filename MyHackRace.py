__author__ = 'Dream Team'
#import check
import numpy as np
import pandas
import locale


def getPolyFromLine(X1,Y1,X2,Y2):
    coord=[]
    halfLineThickness=0.1/2

    if X1==X2:
        coord.append([X1-halfLineThickness,Y1])
        coord.append([X1-halfLineThickness,Y2])
        coord.append([X1+halfLineThickness,Y2])
        coord.append([X1+halfLineThickness,Y1])

    if Y1==Y2:
        #X2=X2-halfLineThickness
        coord.append([X1,Y1-halfLineThickness])
        coord.append([X2,Y1-halfLineThickness])
        coord.append([X2,Y1+halfLineThickness])
        coord.append([X2,Y1+halfLineThickness])
    return coord


data = pandas.read_csv('coordinates.csv',';',decimal=',',header=None, names=['pinnumber','icnumber','x','y'])
headers=['field1', 'field2']
connect= pandas.read_csv('connect.csv',';',decimal=',', header=None, names=headers)
connect.head()



# for obj in connect.iteritems():
#     print obj


#print "connect.columns[1]"
#connect.columns=['field1','field2']

connectProc=list(connect['field1'])
connectMem=list(connect['field2'])

print connectProc
print connectMem
#print connectProc
#connectProc=list(connect.field)
#connectMem=list(connect.field)

#print connectProc
#print connectMem

from Paint import *
from Tkinter import *

procPins=data[data.icnumber==1].pinnumber
procX=data[data.icnumber==1].x
procY=data[data.icnumber==1].y

memPins=data[data.icnumber==2].pinnumber
memX=data[data.icnumber==2].x
memY=data[data.icnumber==2].y

windowScaleX=800
windowScaleY=500

#print("procXmax="+str(procX.max()))

scaleX1=procX.max()
scaleY1=procY.max()

scaleX2=memX.max()
scaleY2=memY.max()

scaleListX=np.array([scaleX1,scaleX2])
scaleListY=np.array([scaleY1,scaleY2])

scaleX=windowScaleX/scaleListX.max()
scaleY=windowScaleY/scaleListY.max()

print("scaleX="+str(scaleX))
print("scaleY="+str(scaleY))
#---------- drawing img

root = Tk()
root.geometry(str(windowScaleX)+"x"+str(windowScaleY)+"+100+100")
p=Paint(root)
scaleX=scaleX*0.7
scaleY=scaleY*0.7
indent=50 #to see all img
circleDiameter=0.1*scaleX
widthLine=0.1*scaleX
for i in range(procPins.size):
    p.drawCircle(newX=procX[i]*scaleX+indent, newY=procY[i]*scaleY+indent,newBrushSize=circleDiameter,newColor="green")

for i in range(40, 40+memPins.size):
    p.drawCircle(newX=memX[i]*scaleX+indent, newY=memY[i]*scaleY+indent,newBrushSize=circleDiameter,newColor="red")

myLineMas=[]

for i in range(40):

    curXproc=procX[connectProc[i]-1]
    curYproc=procY[connectProc[i]-1]

    curXmem=memX[40+connectMem[i]-1]
    curYmem=memY[40+connectMem[i]-1]

    curMiddleX=curXproc
    curMiddleY=curYmem

    myLineMas.append([curXproc,curYproc,curMiddleX,curMiddleY,curXmem,curYmem])

    p.canv.create_line(
       curXproc*scaleX+indent,
       curYproc*scaleY+indent,
       curMiddleX*scaleX+indent,
       curMiddleY*scaleY+indent,
       width=widthLine,fill="blue")

    p.canv.create_line(
       curMiddleX*scaleX+indent,
       curMiddleY*scaleY+indent,
       curXmem*scaleX+indent,
       curYmem*scaleY+indent,
       width=widthLine,fill="blue")
    p.canv.update()
    p.canv.after(700)

root.mainloop()

print "-------------------------------"

f = open('solution.csv','w')
for o in myLineMas:
    curPoly1=getPolyFromLine(o[0], o[1], o[2], o[3])
    curPoly2=getPolyFromLine(o[2], o[3], o[4], o[5])

    f.write( "POLY 4,1\n")
    f.write( str(curPoly1[0][0]).replace(".", ",")+";"+str(curPoly1[0][1]).replace(".", ",")+"\n")
    f.write( str(curPoly1[1][0]).replace(".", ",")+";"+str(curPoly1[1][1]).replace(".", ",")+"\n")
    f.write( str(curPoly1[2][0]).replace(".", ",")+";"+str(curPoly1[2][1]).replace(".", ",")+"\n")
    f.write( str(curPoly1[3][0]).replace(".", ",")+";"+str(curPoly1[3][1]).replace(".", ",")+"\n")
    f.write( "POLY 4,1\n")
    f.write( str(curPoly2[0][0]).replace(".", ",")+";"+str(curPoly2[0][1]).replace(".", ",")+"\n")
    f.write( str(curPoly2[1][0]).replace(".", ",")+";"+str(curPoly2[1][1]).replace(".", ",")+"\n")
    f.write( str(curPoly2[2][0]).replace(".", ",")+";"+str(curPoly2[2][1]).replace(".", ",")+"\n")
    f.write( str(curPoly2[3][0]).replace(".", ",")+";"+str(curPoly2[3][1]).replace(".", ",")+"\n")
f.close()

