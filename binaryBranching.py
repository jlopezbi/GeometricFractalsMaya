import maya.cmds as cmds

def makeArray():
    
    
    axes = ['X', 'Y', 'Z']
    translate = ['translate'+x for x in axes]
    rot = ['rotate'+x for x in axes]
    scale = ['scale'+x for x in axes]
    attrs = translate + rot + scale
    
    nCubes = 10
    
    
    baseObj = cmds.polyCube(w=1,d=1,h=1)[0]
    prevObj = baseObj
    newObjs = None
    
    #for i in xrange(nCubes-1):   
    #    prevObj = makeChild(prevObj)

    make2Children(baseObj,3,1)
        

def make2Children(parentObj,maxDepth,currDepth):
    if currDepth >= maxDepth:
        return
    else:
        child1 = makeChild(parentObj)
        child2 = makeChild(parentObj)
        
        currDepth = currDepth+1
        make2Children(child1,maxDepth,currDepth)
        make2Children(child2,maxDepth,currDepth)
        
 


def makeChild(parentObj):
     
    # DUPLICATE
    #newCubeName = 'pCube%s' %parentObj[-1]
    newObj = cmds.duplicate(parentObj,rr=True,ilf=True,rc=True)[0]
    
    
    # PARENT
    cmds.parent(newObj,parentObj)
    
    # CONNECT XFORM ATTRS
    for attr in attrs:
        cmds.expression(s = newObj+'.' +attr+ ' = ' + parentObj+'.' +attr)
    
    return newObj
         
