from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Villes de France')

my_image1 = ImageTk.PhotoImage(Image.open("map_france1.png"))
my_label = Label(image = my_image1)
my_label.grid(row =1,columns=2)

button_exit = Button(root, text="Quitter",command=root.quit).grid(row=2,columns = 3)
root.mainloop()