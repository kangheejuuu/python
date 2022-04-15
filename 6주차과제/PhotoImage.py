from tkinter import *
from tkinter.filedialog import *

##함수 선언##
def keyUp(event) :
    photo = PhotoImage(file = filename)
    photo = photo.zoom(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo


def keyDown(event) :
    photo = PhotoImage(file = filename)
    photo = photo.subsample(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo

'''
2021041025
강희주
'''

##메인 코드##
window = Tk()
window.geometry("500x500")
window.title("이미지 확대 축소")
filename = "C:/Python/gif/jeju4.gif"
photo = PhotoImage(file = filename)
pLabel = Label(window, image = photo)
pLabel.pack()

window.bind("<Up>", keyUp)
window.bind("<Down>", keyDown)
window.mainloop()
