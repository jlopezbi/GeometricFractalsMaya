import maya.cmds as cmds

axes = ['X', 'Y', 'Z']
translate = ['translate'+x for x in axes]
rot = ['rotate'+x for x in axes]
scale = ['scale'+x for x in axes]
attrs = translate + rot + scale


nCubes = 10


baseObj = cmds.polyCube(w=1,d=1,h=1)[0]
prevObj = baseObj
newObjs = None

for i in xrange(nCubes-1):

    # DUPLICATE
    num = i+2
    newCubeName = 'pCube%s' %prevObj[-1]
    newObj = cmds.duplicate(prevObj,n = newCubeName,rr=True,ilf=True)[0]
 
   
    # PARENT
    cmds.parent(newObj,prevObj)
    
    # CONNECT XFORM ATTRS
    for attr in attrs:
        cmds.expression(s = newObj+'.' +attr+ ' = ' + prevObj+'.' +attr)
    
    prevObj = newObj
    
   