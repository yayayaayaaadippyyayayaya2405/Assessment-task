from customtkinter import *
from PIL import Image, ImageTk

#Fonts used throughout the code 
Title_font = ("Impact", 50, "bold", "underline")
Button_font = ("Times", 20, "italic")

homepage = CTk()
homepage.title("Math Marvels:Capturing Volume")
homepage.minsize(width=1000, height = 600)
homepage.maxsize(width=1000, height = 600)
homepage.resizable(False,False)
homepage.config(bg= "#C1E1C1")
gui_name = (CTkLabel(homepage, text=('Math Marvels: Capturing Volume'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
gui_name.place(x=150,y=20)

homepage.mainloop()