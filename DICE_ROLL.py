import tkinter as tk
from PIL import Image, ImageTk
import random 

window =tk.Tk()
window.geometry("500x360")
window.title("DICE ROLL")


dice=["DICE_1.jpg","DICE_2.jpg","DICE_3.jpg","DICE_4.jpg","DICE_5.jpg","DICE_6.jpg"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image2)

label1.image_names=image1
label2.image_names=image2

label1.place(x=0,y=100)
label2.place(x=300,y=100)

def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image_names=image1

    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image_names=image2
button=tk.Button(window,text="ROLL",bg="black",fg="white",font="times 20 italic",command=dice_roll)

#dice=["dice.png"]#same file image
button.place(x=200,y=0)
window.mainloop()