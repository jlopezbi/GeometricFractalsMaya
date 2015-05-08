import maya.cmds as cmds

"""
Josh Lopez-Binder May 2015
Make a geometric branching fractal "residue"
Run script in Maya and then run MakeArray() in Python Command Line. Move around the 
two children of the root node. Try scaling them by about 0.5 to get not-self-intersecting
patterns.

"""

axes = ['X', 'Y', 'Z']
translate = ['translate'+x for x in axes]
rot = ['rotate'+x for x in axes]
scale = ['scale'+x for x in axes]
attrs = translate + rot + scale

def makeArray(nLevels=7):
    baseObj = cmds.polyCube(w=1,d=1,h=1)[0] 
    makeTree(baseObj,baseObj,nLevels,1)
        

def makeTree(parentObj,siblingObj,maxDepth,currDepth):
    
    if currDepth >= maxDepth:
        return
    else:
       
        [obj1,obj2] = make2Children(parentObj,siblingObj,currDepth!=1) 
        
        currDepth = currDepth+1
        
        makeTree(obj1,obj2,maxDepth,currDepth)
        makeTree(obj2,obj1,maxDepth,currDepth)
        
        
def make2Children(parentObj,siblingObj,makeCon=True,):
     
    # DUPLICATE
    newObj1 = cmds.duplicate(parentObj,rr=True,ilf=True,rc=True)[0]
    newObj2 = cmds.duplicate(newObj1,rr=True,ilf=True,rc=True)[0]
    
    
    # PARENT
    cmds.parent(newObj1,parentObj)
    cmds.parent(newObj2,parentObj)
    
    # CONNECT XFORM ATTRS
    if makeCon:
        for attr in attrs:
            cmds.expression(s = newObj1+'.' +attr+ ' = ' + parentObj+'.' +attr)
            cmds.expression(s = newObj2+'.' +attr+ ' = ' + siblingObj+'.' +attr)
    
    return [newObj1,newObj2]
          


         
