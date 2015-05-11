# Geometric Fractals In Maya
## take a base object and make copies of it, link translation, rotation and scale (Transform)

###Based on blender array modifiers: http://wiki.blender.org/index.php/Doc:2.6/Manual/Modifiers/Generate/Array

####Branching Arrays
Run nBranches.py in Maya python script editor (Windows -> General Editors -> Script Editor) to make a tree with nBranches at each node.
Then run makeArray() in the Python Command line (defautl is MEL). This makes many cubes in the same place. Select a child node of the root node in the Outliner (Window -> Outliner). Try scaling, translating and rotating these children nodes. 

Run binaryBranching.py in Maya python script editor to make a binary tree. 
####Linear Arrays (Spirals)
Run linearArray.py in Maya python script editor. Then type makeArray() in to python command line in Maya. Play with position, rotation and scale of child of root node (pCube1). To view nodes look at Window -> Outliner.


