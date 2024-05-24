from customtkinter import *
from PIL import Image,ImageTk
from LINKtest import Test 

#Fonts used throughout the code 
Title_font = ("Courior", 50, "bold", "underline")
Button_font = ("Times", 20, "italic")

class Homepage ():
    def __init__(self) :

        #Window Geometry and Set up 
        self.homepage = CTk()
        self.homepage.title("Math Marvels:Capturing Volume")
        self.homepage.minsize(width=1000, height = 600)
        self.homepage.maxsize(width=1000, height = 600)
        self.homepage.resizable(False,False)
        self.homepage.config(bg= "#C1E1C1")
        self.gui_name = (CTkLabel(self.homepage, text=('Math Marvels: Capturing Volume'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
        self.gui_name.place(x=150,y=20)

        #Buttons 

        def Formula_Sheet ():
            start = Test()
        

        self.formulae_button = CTkButton (
            self.homepage,
            text = "FORMULAE",
            bg_color = "#C1E1C1",
            corner_radius = 10,
            font = Button_font,
            height = 50,
            width = 150,
            fg_color = "#32a8a0",
            hover_color = "#144a46",
            command = Formula_Sheet,
            )
        self.formulae_button.place(x=40,y=400)
        
        

        self.homepage.mainloop()

Homepage()