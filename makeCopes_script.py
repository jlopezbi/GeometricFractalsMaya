import maya.cmds as cmds

axes = ['X', 'Y', 'Z']
translate = ['translate'+x for x in axes]
rot = ['rotate'+x for x in axes]
scale = ['scale'+x for x in axes]
attrs = translate + rot + scale

num = 2
newCubeName = 'pCube%s' %num
cmds.duplicate('pCube1',n=newCubeName)