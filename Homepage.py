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


# Commands for buttons 
def Explanation_Sheet ():
    pass

def Formula_Sheet ():
    pass

def Quiz ():
    pass

#buttons
Learn_button = CTkButton(
    homepage, 
    text = "LEARN VOLUME!!!",
    bg_color = "#C1E1C1",
    corner_radius = 10,
    font = Button_font,
    height = 50,
    width = 300,
    fg_color = "#32a8a0",
    hover_color = "#144a46",
    command = Explanation_Sheet,
)
Learn_button.place(x=350,y=180)


formulae_button = CTkButton(
    homepage, 
    text = "FORMULAE!!!",
    bg_color = "#C1E1C1",
    corner_radius = 10,
    font = Button_font,
    height = 50,
    width = 300,
    fg_color = "#32a8a0",
    hover_color = "#144a46",
    command = Formula_Sheet,
)
formulae_button.place(x=350,y=300)


Quiz_button = CTkButton(
    homepage, 
    text = "QUIZ YOURSELF!!!",
    bg_color = "#C1E1C1",
    corner_radius = 10,
    font = Button_font,
    height = 50,
    width = 300,
    fg_color = "#32a8a0",
    hover_color = "#144a46",
    command = Quiz,
)
Quiz_button.place(x=350,y=420)




homepage.mainloop()