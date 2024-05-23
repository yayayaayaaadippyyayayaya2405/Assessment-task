import customtkinter as ctk
from PIL import Image, ImageTk


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("assessment-task/red.json")


class Homepage():
    def __init__ (self):
        self.root = ctk.CTk()


        self.root.title('MathMarvels:Capturing Volume')
        self.root.iconbitmap('img1')
        self.root.geometry('1000x600')
        self.root.config(bg="#C1E1C1")


        def learn ():
            pass
    
        Learn_button = ctk.CTkButton (
        self.root, 
        text = "LEARN", 
        bg_color="#C1E1C1",
        fg_color="#FFFFFF",
        corner_radius= 20,
        height=50,
        width=300,
        border_color="#82d660",
        border_width=10,
        font=("Times New Roman",12),
        text_color= "#000000",
        command=learn,

        )
    
        


        def formulae ():
            pass

        self.Formulae_button = ctk.CTkButton (
        self.root, 
        text = "FORMULAE", 
        bg_color="#C1E1C1",
        corner_radius= 20,
        height=50,
        width=150,
        command=formulae,

        )

       
    
        



Homepage()