'''
Disclaimer: This solution is not scalable for creating a big world.
But it can make a deep game chunk.
'''

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )


for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x,0,z))     #This area here determines how deep you want your chunk!
        voxel = Voxel(position=(x,-1,z))
        voxel = Voxel(position=(x,-2,z))
        voxel = Voxel(position=(x,-3,z))
        voxel = Voxel(position=(x,-4,z))
        voxel = Voxel(position=(x,-5,z))
        voxel = Voxel(position=(x,-6,z))
        voxel = Voxel(position=(x,-7,z))


def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)



player = FirstPersonController()
app.run()
