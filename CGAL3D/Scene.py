from visual import *
scene.title = "VPython: Draw a rotating cube"
 
scene.range = 2
scene.autocenter = True
 
print "Drag with right mousebutton to rotate view."
print "Drag up+down with middle mousebutton to zoom."
 
deg45 = math.radians(45.0)  # 0.785398163397

x= box()
cube = box()    # using defaults, see http://www.vpython.org/contents/docs/defaults.html 
cube.rotate( angle=deg45, axis=(1,0,0) )
cube.rotate( angle=deg45, axis=(0,0,1) )

cube1 = box( pos = vector(-1.47,0,0))
cube1.rotate( angle=deg45, axis=(1,0,0) )
cube1.rotate( angle=deg45, axis=(0,0,1) )

 


