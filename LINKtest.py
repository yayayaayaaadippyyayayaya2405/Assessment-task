from customtkinter import *
from PIL import Image,ImageTk

#Fonts used throughout the code 
Title_font = ("Courior", 50, "bold", "underline")
Button_font = ("Times", 20, "italic")

class Test ():
    def __init__(self) :

        #Window Geometry and Set up 
        self.test = CTk()
        self.test.title("Please work yaar")
        self.test.minsize(width=1000, height = 600)
        self.test.maxsize(width=1000, height = 600)
        self.test.resizable(False,False)
        self.test.config(bg= "#C1E1C1")
        self.gui_name = (CTkLabel(self.test, text=('Math Marvels: Capturing Volume'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
        self.gui_name.place(x=150,y=20)

        self.test.mainloop()

Test()
