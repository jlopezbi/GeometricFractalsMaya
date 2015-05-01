import maya.cmds as cmds

axes = ['X', 'Y', 'Z']
translate = ['translate'+x for x in axes]
rot = ['rotate'+x for x in axes]
scale = ['scale'+x for x in axes]
attrs = translate + rot + scale



nCubes = 10
num = 0
baseObj = cmds.polyCube(w=1,d=1,h=1)[0]
print baseObj
prevObj = baseObj
newObjs = None

for i in xrange(nCubes-1):

    # DUPLICATE
    num = i+2
    newCubeName = 'pCube%s' %prevObj[-1]
    newObj = cmds.duplicate(prevObj,n = newCubeName,rr=True)[0]
 
   
    # PARENT
    cmds.parent(newObj,prevObj)
    
    prevObj = newObj
    
    # for attr in attrs:
    # cmds.expression(s = str(newObjs[0]) +attr+ ' = prevObj +attr)