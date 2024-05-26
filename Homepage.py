from customtkinter import *
from PIL import Image, ImageTk

#Fonts used throughout the code 
Title_font = ("Impact", 50, "bold", "underline")
Button_font = ("Times", 20, "italic")
Subittle_font = ("Impact", 30, "bold", "italic")
Text_font = (("courior", 13))

#Homepage Code 
def open_homepage ():
    homepage = CTk()
    homepage.title("Math Marvels:Capturing Volume")
    homepage.minsize(width=1000, height = 600)
    homepage.maxsize(width=1000, height = 600)
    homepage.resizable(False,False)
    homepage.config(bg= "#C1E1C1")
    gui_name = (CTkLabel(homepage,text=('Math Marvels: Capturing Volume'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
    gui_name.place(x=150,y=20)


    # Commands for buttons on Homepage
    def Learn_Window ():
        homepage.destroy ()
        open_Learn_window ()

    def Formula_Sheet ():
        homepage.destroy ()
        open_formula_sheet ()

    def Quiz ():
        pass

    def Homepage_Quit ():
        homepage.destroy ()

    #buttons
    Learn_button = CTkButton(
        homepage, 
        text = "LEARN VOLUME!!!",
        bg_color = "#C1E1C1",
        corner_radius = 10,
        font = Button_font,
        height = 50,
        width = 300,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = Learn_Window,
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
        fg_color = "#32A8A0",
        hover_color = "#144A46",
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
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = Quiz,
    )
    Quiz_button.place(x=350,y=420)


    Homepage_Quit_button = CTkButton(
        homepage, 
        text = "Close",
        bg_color = "#C1E1C1",
        corner_radius = 20,
        font = Button_font,
        height = 30,
        width = 60,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = Homepage_Quit,
    )
    Homepage_Quit_button.place(x=15,y=20)

    #images for homepage 
    Mr_octopus_homepage = CTkImage(light_image=Image.open("Images/homepage_img1.png"), 
                                   dark_image=Image.open("Images/homepage_img1.png"),
                                   size=(300,300)
                                   )
    Mr_octopus_homepage_display = CTkLabel(homepage,text="",
                                                    image=Mr_octopus_homepage,
                                                    bg_color="#C1E1C1")
    Mr_octopus_homepage_display.place(x=675,y=180)
    

    homepage.mainloop()


def open_Learn_window ():
    learn_window = CTk()
    learn_window.title("Math Marvels:Capturing Volume")
    learn_window.minsize(width=1000, height = 600)
    learn_window.maxsize(width=1000, height = 600)
    learn_window.resizable(False,False)
    learn_window.config(bg= "#C1E1C1")
    learn_window_tittle = (CTkLabel(learn_window, text=('LETS LEARN ABOUT VOLUME!!!'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
    learn_window_tittle.place(x=20,y=20)

    # Teaching and explaining Volume 
    learning_window_subtittle = (CTkLabel(learn_window, text=("What is Volume"),
                                          text_color="#3F49A4",
                                          bg_color="#C1E1C1",
                                          font = Subittle_font)
                                          )
    learning_window_subtittle.place(x=40,y=120)
    Volume_definition= (CTkLabel(learn_window, text=("Let's imagine you have a big box. Volume is a way to measure how much space is inside that box. It's like asking, 'How many little cubes can fit inside this box?'"
                                                            "THINK ABOUT A BOX: Imagine you have a box. It could be a toy box, a cereal box, or even a shoebox."
                                                            "FILL IT WITH CUBES: Now, think about filling this box with tiny cubes, each one the same size. These cubes fit perfectly inside without any gaps."
                                                            "Count the Cubes: The volume is the total number of these little cubes that can fit inside the box. The more cubes you can fit, the bigger the volume."),
                                        text_color="#3F49A4",
                                        bg_color="#C1E1C1",
                                        font = Text_font,
                                        wraplength=800,
                                        anchor="w"))
    Volume_definition.place(x=40,y=160)



    learn_window.mainloop()


def open_formula_sheet ():
    formula_sheet = CTk()
    formula_sheet.title("Math Marvels:Capturing Volume")
    formula_sheet.minsize(width=1000, height = 600)
    formula_sheet.maxsize(width=1000, height = 600)
    formula_sheet.resizable(False,False)
    formula_sheet.config(bg= "#C1E1C1")
    formulae_page_gui = (CTkLabel(formula_sheet, text=('Math Marvels: Capturing Volume'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
    formulae_page_gui.place(x=150,y=20)



    formula_sheet.mainloop()

open_homepage()