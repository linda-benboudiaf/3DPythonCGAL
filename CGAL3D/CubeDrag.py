from __future__ import division, print_function
from visual import *
scene.range=5
box1 = box(pos=(-1, 0,0), size=(2,2,2),color= color.yellow)
drag_pos = None

def take_obj(event):
    global drag_pos
    if event.pick == box1:
        drag_pos = event.pickpos
        scene.bind('mousemove', move, box1)
        
def move(evt, obj):
    global drag_pos
    # project onto xy plane, even if scene rotated:
    new_pos = scene.mouse.project(normal=(0,0,1))
    if new_pos != drag_pos: # if mouse has moved
        # offset for where the ball was touched:
        obj.pos += new_pos - drag_pos 
        drag_pos = new_pos # update drag position

def drop(evt):
    scene.unbind('mousemove', move)
    scene.unbind('mouseup', drop)

scene.bind('mousedown', take_obj)
        
#for i in range(1, 15):
#    box1 = box (pos= vector(-i, 0, 0), raduis= 0.5, color = color.yellow)    
#    for j in range(15-i):
#        box2 = box (pos= vector(j, 0, 0), raduis= 0.5, color = color.red)
#    for j in range(1, i):
#        box1
#    for i in range(i, 0, -1):
#        box1
#        print(i*j, end = "\t")
#    print("\n")
