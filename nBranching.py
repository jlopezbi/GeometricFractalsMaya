import maya.cmds as cmds

"""
Josh Lopez-Binder May 2015
Make a geometric branching fractal with "residue"
Run script in Maya. Then select base-object and run MakeArray(<nLevels>) in Python Command Line. Move around the 
two children of the root node. Try scaling them by about 0.5 to get not-self-intersecting
patterns.

"""

axes = ['X', 'Y', 'Z']
translate = ['translate'+x for x in axes]
rot = ['rotate'+x for x in axes]
scale = ['scale'+x for x in axes]
attrs = translate + rot + scale
finalGen = []


def makeArray(nBranch=2,nLevels=7):
    
    selected = cmds.ls(sl=1)
    if len(selected) == 0:
        baseObj = cmds.polyCube(w=1,d=1,h=1)[0] 
    else:
        baseObj = selected[0] #right now hard coded for the first selection  
        #TODO: filter selection for polygons, nurbs, etc.
    finalGen = []
    makeTree(baseObj,baseObj,nBranch,nLevels,1,finalGen)
    return finalGen

def prune(generation):

    cmds.delete(generation)

def makeTree(parentObj,prevGen,nBranch,maxDepth,currDepth,finalGen):      
    
    if currDepth >= maxDepth:
        finalGen.append(parentObj)
        return
    else:
        newGen = makeNChildren(nBranch,parentObj,prevGen,currDepth!=1) 
        currDepth = currDepth+1
        
        for i in xrange(nBranch):
            obj = newGen[i]
            makeTree(obj,newGen,nBranch,maxDepth,currDepth,finalGen)

def makeNChildren(nChildren,parentObj,prevGen,makeCon=True):

    objList = []
    prevDup = parentObj
    for i in xrange(nChildren):
        # DUPLICATE
        newObj = cmds.duplicate(prevDup,rr=True,ilf=True,rc=True)[0]

        # PARENT
        if i==0: cmds.parent(newObj,parentObj)

        # CONNECT XFORM ATTRS
        if nChildren == len(prevGen):
            connectAttrs(newObj,prevGen[i])
        elif len(prevGen) <= 1:
            connectAttrs(newObj,parentObj)

        objList.append(newObj)
        prevDup = newObj

    return objList

def connectAttrs(newObj,oldObj):
    for attr in attrs:
        cmds.expression(s = newObj+'.' +attr+ ' = ' + oldObj+'.' +attr)


if __name__ == "__main__":
    # This is for debbuging purposes
    cmds.select(all=True)
    cmds.delete()
    gen = makeArray(nBranch=2,nLevels=4)
        
