# importing the tkinter module and PIL
# that is pillow module
from tkinter import *
from PIL import ImageTk, Image

# Calling the Tk (The initial constructor of tkinter)
root = Tk()

# We will make the title of our app as Image Viewer
root.title("Image Viewer")

# The geometry of the box which will be displayed
# on the screen
root.geometry("1024x600")

# Adding the images using the pillow module which
# has a class ImageTk We can directly add the
# photos in the tkinter folder or we have to
# give a proper path for the images
image_no_1 = ImageTk.PhotoImage(Image.open("imgs/cloudy128.png"))
# image_no_2 = ImageTk.PhotoImage(Image.open("sample.png"))
# image_no_3 = ImageTk.PhotoImage(Image.open("Sample.png"))
# image_no_4 = ImageTk.PhotoImage(Image.open("sample.png"))

# List of the images so that we traverse the list
#  List_images = [image_no_1, image_no_2, image_no_3, image_no_4]
List_images = [image_no_1]

label = Label(image=image_no_1)

# We have to show the box so this below line is needed
label.grid(row=0, column=0, columnspan=3, padx=25)

root.mainloop()