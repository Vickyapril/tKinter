"""import numpy as np #importing numpy
import pandas as pd #importing pandas
import matplotlib.pyplot as plt #importing matplot

#Reading the text file with Read a table of fixed-width formatted lines into DataFrame.
df = pd.read_fwf("villes copy.txt",header=None,names=['Ville','latitude','A','B','longitude','D','E'])
#Selecting the Ville,latitude,longitude and forming a new dataframe1
df1 = df.iloc[:,[0,1,4]]
df1.round()
df1.to_csv("Trail",index=False) #optional

df1.head(10) # To check the first 10 datas 

# Creating a BoundBox by selecting the min and max lat,long
BBox =((df1.longitude.min(), df1.longitude.max(),      
         df1.latitude.min(), df1.latitude.max()))
print(BBox) # to check the values 

#Loading our first map image 
fmap =plt.imread('map_france_742x773.gif')


#Using Scatterplot and ploting the sub plots 
fig, ax = plt.subplots(figsize = (7,7))
ax.scatter(df1.longitude, df1.latitude, zorder=1, alpha= 1, c='b', s=20 ,marker ='^')
ax.set_title('France Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(fmap, zorder=0, extent = BBox, aspect= 'equal')
plt.axis('off')
plt.savefig('map_france1',bbox_inches='tight')"""


from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Villes de France')

my_image1 = ImageTk.PhotoImage(Image.open("map_france1.png"))
my_label = Label(image = my_image1)
my_label.grid(row =1,columns=2)

button_exit = Button(root, text="Quitter",command=root.quit).grid(row=2,columns = 3)
root.mainloop()