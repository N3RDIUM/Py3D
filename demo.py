# Py3D demo

from Py3D.__init__ import *

win = Py3dWindow(title="Py3D")
win.init_window()

quad1 = Mesh(win)

quad1.add_line([0, 0, 0], [1, 0, 0])
quad1.add_line([0, 0, 0], [0, 1, 0])
quad1.add_line([0, 0, 0], [1, 1, 0])
quad1.add_line([1, 0, 0], [1, 1, 0])
quad1.add_line([0, 1, 0], [1, 1, 0])

quad1.position[1] = 1
win.add_mesh(quad1)

quad2 = Mesh(win)

quad2.add_line([0, 0, 0], [1, 0, 0])
quad2.add_line([0, 0, 0], [0, 1, 0])
quad2.add_line([0, 0, 0], [1, 1, 0])
quad2.add_line([1, 0, 0], [1, 1, 0])
quad2.add_line([0, 1, 0], [1, 1, 0])

quad2.rotation[1] = 90
win.add_mesh(quad2)

def move(events):
    for i in events:
        if i.type == 771:
            if i.text == 'w':
                win.camera[0][2] += 1
            if i.text == 's':
                win.camera[0][2] -= 1
            if i.text == 'a':
                win.camera[0][0] += 1
            if i.text == 'd':
                win.camera[0][0] -= 1

    win.camera[1][1] -= 0.1

win.on_events(move)
win.run()
