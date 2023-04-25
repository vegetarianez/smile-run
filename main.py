from time import *
from random import *
from tkinter import *


def move(event):
    if event.keysym == 'Up':
        canvas.move(2, 0, -10)
        scene.update()
    elif event.keysym == 'Down':
        canvas.move(2, 0, 10)
        scene.update()
    elif event.keysym == 'Left':
        canvas.move(2, -10, 0)
        scene.update()
    elif event.keysym == 'Right':
        canvas.move(2, 10, 0)
        scene.update()
scene = Tk()
scene.title('Смайлик ходячий')
scene.geometry('1280x720')
scene.resizable(width=False, height=False)
canvas = Canvas(scene, width=1280, height=720)
canvas.pack()

back = PhotoImage(file='les.png')
canvas.create_image(0, 0, anchor=NW, image=back)
obj = PhotoImage(file='smile.png')
canvas.create_image(randint(50, 1150), randint(50, 570), anchor=NW, image=obj)

scene.bind('<Key>', move)




scene.mainloop()
