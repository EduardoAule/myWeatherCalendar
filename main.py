# importing whole module
from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk, Image

# importing strftime function to
# retrieve system's time
from time import strftime

# from services import  ds18b20 as ds

# Calling the Tk (The initial constructor of tkinter)
root = Tk()

# We will make the title of our app as Image Viewer
root.title("Image Viewer")

# The geometry of the box which will be displayed
# on the screen
root.geometry("1024x600")
# Set window color
# root.configure(bg='black')
root['background']='#000000'

# Imagen
image_no_1 = ImageTk.PhotoImage(Image.open("imgs/cloudy256.png"))
List_images = [image_no_1]

# Styling the label widget so that clock
# will look more attractive
lbl_time = Label( font=('Calibri', 100, 'bold'),
            background='black',
            foreground='white')
lbl_sensor = Label( font=('Calibri', 70, 'bold'),
            background='black',
            foreground='white')
lbl_img_cloudy = Label(image=image_no_1, background='black')

# Placing clock at the centre
# of the tkinter window
# lbl.pack(anchor='center')

# This function is used to
# display time on the label
def time():
    # %I para hora en formato 12h, %H 24h
    string = strftime('%I:%M:%S %p')
    lbl_time.config(text=string)
    lbl_time.after(1000, time)

def temperature():
    # read sensor
    temperature = str(25.6) + "°C" # ds.read_temp()
    lbl_sensor.config(text=temperature) # temperature[0]
    lbl_sensor.after(3000, time)

time()
temperature()



# We have to show the box so this below line is needed
lbl_time.grid(row=0, column=0, sticky = "nsew", padx=25, pady=5)
lbl_img_cloudy.grid(row=0, column=1, sticky = W, padx=5, pady=5)
lbl_sensor.grid(row=1, column=1, sticky = W, padx=5, pady=5)


# mainloop()
root.mainloop()