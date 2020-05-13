from tkinter import *

#Create root widget--the window
root = Tk()

#Create title label widget
titleL = Label(root, text = 'Organize WEPP erosion results via CSV')

#Place title in the root widget using grid method
titleL.grid(column = 0, row = 0)

#Create working folder label widget
wfolderL = Label(root, text = 'Select your working folder:')
wfolderL.grid(column = 0, row = 1)
#Create first input box via entry widget and place
e1 = Entry(root)
e1.grid(column = 1, row = 1)

#Define button click functions
def browseClick():
    print('This is where the Browse function goes')
def createClick():
    print('This is where the Create CSV function goes')
    
#Create a Browse button
browseB = Button(root, text = 'Browse', command = browseClick)
browseB.grid(column = 2, row = 1)

#Create Unburnt section
unburntL = Label(root, text = 'Name of Unburnt simulation folder:')
unburntL.grid(column = 0, row = 2)
e2 = Entry(root)
e2.grid(column = 1, row = 2)

#Create Burnt section
burntL = Label(root, text = 'Name of Burnt simulation folder:')
burntL.grid(column = 0, row = 3)
e3 = Entry(root)
e3.grid(column = 1, row = 3)

#Create Save section
saveL = Label(root, text = 'Save this CSV as:')
saveL.grid(column = 0, row = 4)
e4 = Entry(root)
e4.grid(column = 1, row = 4)
createB = Button(root, text = 'Create CSV', command = createClick)
createB.grid(column = 1, row = 5)





#Create an event loop
root.mainloop()

