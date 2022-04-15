from tkinter import *
from tkinter import ttk


'''
2021041025
강희주
'''


window = Tk()
window.iconbitmap('C:/Python/gif/python.ico')

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text='강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text = '고양이')

baseTab.pack(expand=1, fill="both")

photoDog = PhotoImage(file = "C:/Python/gif/dog7.gif")
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

photoCat = PhotoImage(file = "C:/Python/gif/cat5.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()
