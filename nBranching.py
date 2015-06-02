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

def makeTree(parentObj,parentList,nBranch,maxDepth,currDepth,finalGen):      
    
    if currDepth >= maxDepth:
        finalGen.append(parentObj)
        return
    else:
        newGen = makeNChildren(nBranch,parentObj,parentList,currDepth!=1) 
        currDepth = currDepth+1
        
        for i in xrange(nBranch):
            obj = newGen[i]
            makeTree(obj,newGen,nBranch,maxDepth,currDepth,finalGen)


def makeNChildren(nChildren,parentObj,parentList,makeCon=True):
    objList = []
    prevDup = parentObj
    for i in xrange(nChildren):
        # DUPLICATE
        newObj = cmds.duplicate(prevDup,rr=True,ilf=True,rc=True)[0]

        # PARENT
        if i==0: cmds.parent(newObj,parentObj)

        # CONNECT XFORM ATTRS
        if nChildren == len(parentList):
            connectAttrs(newObj,parentList[i])
        elif len(parentList) <= 1:
            connectAttrs(newObj,parentObj)

        objList.append(newObj)
        prevDup = newObj

    return objList



def grow(generation,nBranch):
    assert areLeaves(generation), "generation was not the final one!"
    updatedGen = []
    for obj in generation:
        updatedGen.extend(makeNChildren(nBranch,obj,getParentGen(obj),makeCon=True))
    return updatedGen

def getParentGen(obj):
    grandParent = getGrandParent(obj)
    assert grandParent!=None
    return cmds.listRelatives(grandParent,typ="transform",c=True)

def getGrandParent(obj):
    parent = cmds.listRelatives(obj,p=True)
    return cmds.listRelatives(parent,p=True)


def areLeaves(generation):
    if None == cmds.listRelatives(generation,c=True, typ="transform"):
        return True
    else:
        return False

def prune(generation):
    updatedGen = getParents(generation)
    cmds.delete(generation)
    return updatedGen

def getParents(generation):
    # get parent nodes of each even individual in a generation
    redundantList =  cmds.listRelatives(generation, p=True)
    return list(set(redundantList))
    
def getFinalGen(root):
    # get the final gen from the root
    def getChildrenRec(obj,finalGen):
        if areLeaves(obj):
            finalGen.append(obj)
            return
        else:
            getChildrenRec(obj,finalGen)
    finalGen = []
    getChildrenRec(root,finalGen)
    return finalGen

def connectAttrs(newObj,oldObj):
    for attr in attrs:
        cmds.expression(s = newObj+'.' +attr+ ' = ' + oldObj+'.' +attr)

if __name__ == "__main__":

    # This is for debbuging purposes
    cmds.select(all=True)
    cmds.delete()
    gen = makeArray(nBranch=2,nLevels=4)
    
    # TEST areLeaves
    print "TEST areLeaves"
    print cmds.listRelatives(gen,c=True, typ="transform")
    assert areLeaves(gen)==True
    assert areLeaves("pCube1")==False
    assert areLeaves("pCube2")==False
    print "passed areLeaves test\n"

    print "TEST getGrandParent"
    assert [u'pCube1']== getGrandParent("pCube4")
    assert getGrandParent("pCube7")== getGrandParent("pCube6")
    print getGrandParent("pCube2")
    print "Passed getGrandParent Test!\n"

    print "TEST getParentGen"
    assert [u'pCube4',u'pCube5']== getParentGen("pCube6")
    print cmds.listRelatives("pCube2",typ="transform",c=True) 
    print "Passed getParentGen Test!\n"
    
    print "TEST prune"
    print "Initial leaf  generation: ",
    print gen
    print "Leaf generation after prune:",
    gen = prune(gen)
    print gen
    print "Finished prune display\n"
    
    print "TEST grow"
    print "Grown Leafs: ",
    print grow(gen,2)
    print "Finished grow display\n"
    
    print "TEST getFinalGen"
    assert True == areLeaves("pCube18")
    print cmds.listRelatives("pCube18",c=True)
    assert False== areLeaves("pCube1")
    print "all children of root:",
    print getFinalGen("pCube1")
    #print "Passed getFinalGen test!"
