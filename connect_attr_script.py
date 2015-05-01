import pymel.core as pm

axes = ['X', 'Y', 'Z']
translate = ['translate'+x for x in axes]
rot = ['rotate'+x for x in axes]
scale = ['scale'+x for x in axes]
attrs = translate + rot + scale
attrs
for attr in attrs:
   pm.expression(s='pCube1.'+attr+ ' = pCube2.'+attr)
