from ursina import *
from ursina.duplicate import duplicate


class Prismatoid(Mesh):
    def __init__(self, base_shape=Quad, origin=(0,0), path=((0,0,0),(0,1,0)), thicknesses=((1,1),), mode='triangle', **kwargs):
        if type(base_shape) == type:
            base_shape = base_shape()

        self.base_shape = base_shape
        shape = base_shape.vertices
        # make the base shape and rotate it
        b = Entity(position=path[0], color=color.lime, scale=thicknesses[0], origin=origin)
        for p in shape:
            Entity(parent=b, position=Vec3(p), model='cube', scale=(.05, .05, .05), color=color.yellow)

        b.look_at(path[1])
        e = duplicate(b)

        verts = list()

        # cap start
        for i in range(len(b.children)):
            verts.append(path[0])
            verts.append(b.children[i].world_position)
            if i >= len(b.children)-1:
                verts.append(b.children[0].world_position)
            else:
                verts.append(b.children[i+1].world_position)

        for i in range(1, len(path)):
            b.position = path[i-1]
            b.look_at(path[i])
            e.position = path[i]
            if i+1 < len(path):
                e.look_at(path[i+1])

            # for debugging sections
            # clone = duplicate(e)
            # clone.color=color.brown
            # clone.scale *= 1.1

            try:
                e.scale = thicknesses[i]
            except:
                pass

            for j in range(len(e.children)):
                n = j+1
                if j == len(e.children)-1:
                    n = 0
                verts.append(e.children[j].world_position)
                verts.append(b.children[n].world_position)
                verts.append(b.children[j].world_position)

                verts.append(e.children[n].world_position)
                verts.append(b.children[n].world_position)
                verts.append(e.children[j].world_position)

        # cap end
        for i in range(len(e.children)):
            if i >= len(e.children)-1:
                verts.append(e.children[0].world_position)
            else:
                verts.append(e.children[i+1].world_position)
            verts.append(e.children[i].world_position)
            verts.append(path[-1])


        super().__init__(vertices=verts, mode=mode, **kwargs)
        destroy(b)
        destroy(e)



if __name__ == '__main__':
    app = Ursina()
    # e = Entity(model=Prism(mode='line'))
    e = Entity(model=Prismatoid())
    # e2 = duplicate(e)
    # e2.x=2
    # e2.color=color.red

    EditorCamera()
    origin = Entity(model='cube', color=color.magenta)
    origin.scale *= .25
    app.run()
