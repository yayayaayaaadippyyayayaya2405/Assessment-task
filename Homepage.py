import customtkinter as ctk
from PIL import Image


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("red.json")

root = ctk.CTk()


root.title('MathMarvels:Capturing Volume')
root.iconbitmap('img1')
root.geometry('800x500')
root.config(bg="#C1E1C1")


def learn ():
    pass
    
Learn_button = ctk.CTkButton (
    root, 
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
Learn_button.pack (
    pady=60

)


def formulae ():
    pass

Formulae_button = ctk.CTkButton (
    root, 
    text = "FORMULAE", 
    bg_color="#C1E1C1",
    corner_radius= 20,
    height=50,
    width=150,
    command=formulae,

)
Formulae_button.pack(
    pady= 1
    
)



root.mainloop()