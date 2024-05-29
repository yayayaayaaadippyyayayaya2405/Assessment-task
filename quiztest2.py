from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

#Fonts used throughout the code 
Title_font = ("Impact", 50, "bold", "underline")
Button_font = ("Times", 20, "italic")
Subittle_font1 = ("Impact", 30, "bold", "italic")
Subheading_font = ("Impact", 20, "italic")
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
        homepage.destroy ()
        open_quiz ()


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
        fg_color = "#F54E42",
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
        command = homepage.destroy,
    )
    Homepage_Quit_button.place(x=15,y=20)

    #images for homepage 
    Mr_octopus_homepage = CTkImage(light_image=Image.open("Images/homepage_img1.png"), 
                                   dark_image=Image.open("Images/homepage_img1.png"),
                                   size=(300,300)
                                   )
    Mr_octopus_homepage_display = CTkLabel(homepage,text="",
                                                    image=Mr_octopus_homepage,
                                                    bg_color="#C1E1C1"
                                                    )
    Mr_octopus_homepage_display.place(x=675,y=180)
    
    Shapes_Image_homepage = CTkImage(light_image=Image.open("Images/homepage_img2.png"), 
                                   dark_image=Image.open("Images/homepage_img2.png"),
                                   size=(350,350)
                                   )
    Shapes_Image_homepage_display = CTkLabel(homepage,text="",
                                                    image=Shapes_Image_homepage,
                                                    bg_color="#C1E1C1"
                                                    )
    Shapes_Image_homepage_display.place(x=0,y=150)



    homepage.mainloop()

#Code for Learn Window 
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
                                          font = Subittle_font1)
                                          )
    learning_window_subtittle.place(x=40,y=120)

    # Adding volume definition with separate lines and subheadings
    Volume_definition1 = CTkLabel(learn_window, text="Let's imagine you have a big box.",
                                  text_color="#3F49A4",
                                  bg_color="#C1E1C1",
                                  font=Text_font,
                                  wraplength=900,
                                  anchor="w")  # 'w' stands for "West" and makes the test left aligned whereas 'e' (East) would make it right aligned text
    Volume_definition1.place(x=40, y=160, relwidth=0.95)

    Volume_definition2 = CTkLabel(learn_window, text="Volume is a way to measure how much space is inside that box.",
                                  text_color="#3F49A4",
                                  bg_color="#C1E1C1",
                                  font=Text_font,
                                  wraplength=900,
                                  anchor="w") 
    Volume_definition2.place(x=40, y=185, relwidth=0.95)

    Volume_definition3 = CTkLabel(learn_window, text="It's like asking, 'How many little cubes can fit inside this box?'",
                                  text_color="#3F49A4",
                                  bg_color="#C1E1C1",
                                  font=Text_font,
                                  wraplength=900,
                                  anchor="w")  
    Volume_definition3.place(x=40, y=210, relwidth=0.95)

    # Smaller Subheadings and their corresponding texts
    subheading1 = CTkLabel(learn_window, text="THINK ABOUT A BOX:",
                           text_color="#3F49A4",
                           bg_color="#C1E1C1",
                           font=Subheading_font,
                           anchor="w")  
    subheading1.place(x=40, y=250, relwidth=0.95)

    subheading1_text = CTkLabel(learn_window, text="Imagine you have a box. It could be a toy box, a cereal box, or even a shoebox.",
                                text_color="#3F49A4",
                                bg_color="#C1E1C1",
                                font=Text_font,
                                wraplength=900,
                                anchor="w")  
    subheading1_text.place(x=40, y=280, relwidth=0.95)

    subheading2 = CTkLabel(learn_window, text="FILL IT WITH CUBES:",
                           text_color="#3F49A4",
                           bg_color="#C1E1C1",
                           font=Subheading_font,
                           anchor="w")  
    subheading2.place(x=40, y=330, relwidth=0.95)

    subheading2_text = CTkLabel(learn_window, text="Now, think about filling this box with tiny cubes, each one the same size. These cubes fit perfectly inside without any gaps.",
                                text_color="#3F49A4",
                                bg_color="#C1E1C1",
                                font=Text_font,
                                wraplength=900,
                                anchor="w")  
    subheading2_text.place(x=40, y=360, relwidth=0.95)

    subheading3 = CTkLabel(learn_window, text="COUNT THE CUBES:",
                           text_color="#3F49A4",
                           bg_color="#C1E1C1",
                           font=Subheading_font,
                           anchor="w")  
    subheading3.place(x=40, y=410, relwidth=0.95)

    subheading3_text = CTkLabel(learn_window, text="The volume is the total number of these little cubes that can fit inside the box. The more cubes you can fit, the bigger the volume.",
                                text_color="#3F49A4",
                                bg_color="#C1E1C1",
                                font=Text_font,
                                wraplength=900,
                                anchor="w")  
    subheading3_text.place(x=40, y=440, relwidth=0.95)

    
    #Image for kids entertainment (Canva Produced)
    Relateable_Kid = CTkImage(light_image=Image.open("Images/definition_img1.png"),
                             dark_image=Image.open("Images/definition_img1.png"),
                             size = (250,250)
                             )
    Relateable_Kid_display = CTkLabel(learn_window, text="",
                                     image=Relateable_Kid,
                                     bg_color="#C1E1C1"
                                     )
    Relateable_Kid_display.place(x=600,y=55)


    #commands for buttons on Learn window 
    def back_to_homepage ():
        learn_window.destroy ()
        open_homepage ()

    def examples_page ():
        learn_window.destroy ()
        open_learn_window2 ()


    #Buttons for Learn Window 
    homepage_return = CTkButton (
        learn_window,
        text = "Back",
        bg_color = "#C1E1C1",
        corner_radius = 20,
        font = Button_font,
        height = 30,
        width = 60,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = back_to_homepage,
        )
    homepage_return.place(x=900,y=20)

    next_page = CTkButton (
        learn_window,
        text = "Next Page (Examples)",
        bg_color = "#C1E1C1",
        corner_radius = 10,
        font = Button_font,
        height = 50,
        width = 150,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = examples_page,
        )
    next_page.place(x=750,y=500)

    close_program = CTkButton (
        learn_window,
        text = "Close",
        bg_color = "#C1E1C1",
        corner_radius = 20,
        font = Button_font,
        height = 30,
        width = 60,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = learn_window.destroy,
        )
    close_program.place(x=900,y=60)


    learn_window.mainloop()

#code for page with examples 
def open_learn_window2 ():
    examples_window = CTk()
    examples_window.title("Math Marvels:Capturing Volume")
    examples_window.minsize(width=1000, height = 600)
    examples_window.maxsize(width=1000, height = 600)
    examples_window.resizable(False,False)
    examples_window.config(bg= "#C1E1C1")
    examples_window_tittle = (CTkLabel(examples_window, text=('Examples of Volume'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
    examples_window_tittle.place(x=20,y=15)

    #Pictures containing examples (Made on Canva)
    Prism_example = CTkImage(light_image=Image.open("Images/Example1.png"),
                             dark_image=Image.open("Images/Example1.png"),
                             size = (350,350)
                             )
    Prism_example_display = CTkLabel(examples_window, text="",
                                     image=Prism_example,
                                     bg_color="#C1E1C1"
                                     )
    Prism_example_display.place(x=10,y=70)


    Sphere_example = CTkImage(light_image=Image.open("Images/example2.png"),
                             dark_image=Image.open("Images/example2.png"),
                             size = (350,350)
                             )
    Sphere_example_display = CTkLabel(examples_window, text="",
                                     image=Sphere_example,
                                     bg_color="#C1E1C1"
                                     )
    Sphere_example_display.place(x=330,y=70)


    Cylinder_example = CTkImage(light_image=Image.open("Images/example3.png"),
                             dark_image=Image.open("Images/example3.png"),
                             size = (350,350)
                             )
    Cylinder_example_display = CTkLabel(examples_window, text="",
                                     image=Cylinder_example,
                                     bg_color="#C1E1C1"
                                     )
    Cylinder_example_display.place(x=650,y=70)


    Cube_example = CTkImage(light_image=Image.open("Images/example4.png"),
                             dark_image=Image.open("Images/example4.png"),
                             size = (350,350)
                             )
    Cube_example_display = CTkLabel(examples_window, text="",
                                     image=Cube_example,
                                     bg_color="#C1E1C1"
                                     )
    Cube_example_display.place(x=10,y=330)


    Tri_prism_example = CTkImage(light_image=Image.open("Images/example5.png"),
                             dark_image=Image.open("Images/example5.png"),
                             size = (350,350)
                             )
    Tri_prism_display = CTkLabel(examples_window, text="",
                                     image=Tri_prism_example,
                                     bg_color="#C1E1C1"
                                     )
    Tri_prism_display.place(x=330,y=330)


    pyramid_example = CTkImage(light_image=Image.open("Images/example6.png"),
                             dark_image=Image.open("Images/example6.png"),
                             size = (350,350)
                             )
    pyramid_example_display = CTkLabel(examples_window, text="",
                                     image=pyramid_example,
                                     bg_color="#C1E1C1"
                                     )
    pyramid_example_display.place(x=650,y=330)

    
    #Image for Kids entertainment (Canva produced)
    Example_giving_Kid = CTkImage(light_image=Image.open("Images/definition_img2.png"),
                             dark_image=Image.open("Images/definition_img2.png"),
                             size = (100,100)
                             )
    Example_giving_kid_display = CTkLabel(examples_window, text="",
                                     image=Example_giving_Kid,
                                     bg_color="#C1E1C1"
                                     )
    Example_giving_kid_display.place(x=450,y=5)


    #Commands for buttons on Examples Window 
    def back_to_homepage ():
        examples_window.destroy ()
        open_Learn_window ()


    #Buttons on Examples Page 
    learn_window_return = CTkButton (
        examples_window,
        text = "Back",
        bg_color = "#C1E1C1",
        corner_radius = 20,
        font = Button_font,
        height = 30,
        width = 60,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = back_to_homepage,
        )
    learn_window_return.place(x=900,y=20)


    close_program = CTkButton (
        examples_window,
        text = "Close",
        bg_color = "#C1E1C1", 
        corner_radius = 20,
        font = Button_font,
        height = 30,
        width = 60,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = examples_window.destroy,
        )
    close_program.place(x=900,y=60)


    examples_window.mainloop()

#Code for Fomrulae Window 
def open_formula_sheet ():
    formula_sheet = CTk()
    formula_sheet.title("Math Marvels:Capturing Volume")
    formula_sheet.minsize(width=1000, height = 700)
    formula_sheet.maxsize(width=1000, height = 700)
    formula_sheet.resizable(False,False)
    formula_sheet.config(bg= "#C1E1C1")
    formulae_page_tittle = (CTkLabel(formula_sheet, text=('Formula Sheet For Quiz!!!'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
    formulae_page_tittle.place(x=20,y=20)

    #Commands for Buttons on Formulae Window 
    def back_to_homepage ():
        formula_sheet.destroy ()
        open_homepage ()


    #Buttons for Formulae Window 
    homepage_return = CTkButton (
        formula_sheet
        ,
        text = "Back",
        bg_color = "#C1E1C1",
        corner_radius = 20,
        font = Button_font,
        height = 30,
        width = 60,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = back_to_homepage,
        )
    homepage_return.place(x=900,y=20)

    

    close_program = CTkButton (
        formula_sheet,
        text = "Close",
        bg_color = "#C1E1C1",
        corner_radius = 20,
        font = Button_font,
        height = 30,
        width = 60,
        fg_color = "#32A8A0",
        hover_color = "#144A46",
        command = formula_sheet.destroy,
        )
    close_program.place(x=900,y=60)

    #Images for Formulae (Make with canva)
    Prism_Volume = CTkImage(light_image=Image.open("Images/Prism_Volume.png"),
                             dark_image=Image.open("Images/Prism_Volume.png"),
                             size = (350,350)
                             )
    Prism_Volume_display = CTkLabel(formula_sheet, text="",
                                     image=Prism_Volume,
                                     bg_color="#C1E1C1"
                                     )
    Prism_Volume_display.place(x=10,y=90)


    Triangular_Prism_Volume = CTkImage(light_image=Image.open("Images/Triangular_prism.png"),
                             dark_image=Image.open("Images/Triangular_prism.png"),
                             size = (350,350)
                             )
    Triangular_Prism_display = CTkLabel(formula_sheet, text="",
                                     image=Triangular_Prism_Volume,
                                     bg_color="#C1E1C1"
                                     )
    Triangular_Prism_display.place(x=335,y=90)


    Pyramind_Volume = CTkImage(light_image=Image.open("Images/Pyramid_volume.png"),
                             dark_image=Image.open("Images/Pyramid_volume.png"),
                             size = (350,350)
                             )
    Pyramind_Volume_display = CTkLabel(formula_sheet, text="",
                                     image=Pyramind_Volume,
                                     bg_color="#C1E1C1"
                                     )
    Pyramind_Volume_display.place(x=660,y=90)


    Sphere_Volume = CTkImage(light_image=Image.open("Images/sphere_volume.png"),
                             dark_image=Image.open("Images/sphere_volume.png"),
                             size = (350,350)
                             )
    Sphere_Volume_display = CTkLabel(formula_sheet, text="",
                                     image=Sphere_Volume,
                                     bg_color="#C1E1C1"
                                     )
    Sphere_Volume_display.place(x=10,y=380)

    
    Cube_Volume = CTkImage(light_image=Image.open("Images/cube_volume.png"),
                             dark_image=Image.open("Images/cube_volume.png"),
                             size = (350,350)
                             )
    Cube_Volume_display = CTkLabel(formula_sheet, text="",
                                     image=Cube_Volume,
                                     bg_color="#C1E1C1"
                                     )
    Cube_Volume_display.place(x=335,y=380)


    cylinder_Volume = CTkImage(light_image=Image.open("Images/cylinder_volume.png"),
                             dark_image=Image.open("Images/cylinder_volume.png"),
                             size = (350,350)
                             )
    Cylinder_Volume_display = CTkLabel(formula_sheet, text="",
                                     image=cylinder_Volume,
                                     bg_color="#C1E1C1"
                                     )
    Cylinder_Volume_display.place(x=660,y=380)


    formula_sheet.mainloop()

def open_quiz():
    quiz_window = CTk()
    quiz_window.title("Math Marvels: Capturing Volume")
    quiz_window.minsize(width=1000, height=600)
    quiz_window.maxsize(width=1000, height=600)
    quiz_window.resizable(False, False)
    quiz_window.config(bg="#C1E1C1")

    quiz_window_title = CTkLabel(quiz_window, text='Quiz Regarding Volume ;)',
                                  text_color="#4263F5", bg_color="#C1E1C1", font=Title_font)
    quiz_window_title.place(x=150, y=20)

    # Questions and Answers
    questions = [
        "1. What is the volume of a cube with side length 3 units?",
        "2. What is the volume of a cylinder with radius 2 units and height 5 units?",
        "3. What is the volume of a sphere with radius 4 units?",
        "4. What is the volume of a cone with radius 3 units and height 9 units?",
        "5. What is the volume of a rectangular prism with dimensions 4x5x6 units?",
        "6. What is the volume of a pyramid with base area 10 square units and height 3 units?",
        "7. What is the volume of a cube with side length 7 units?",
        "8. Type the volume of a sphere with radius 5 units (in terms of π):",
        "9. Type the volume of a cylinder with radius 3 units and height 7 units (in terms of π):",
        "10. Type the volume of a cube with side length 2 units:",
        "11. True or False: The volume of a cube with side length 4 units is 64 cubic units.",
        "12. True or False: The volume of a sphere is given by the formula V = 4/3 πr³.",
        "13. True or False: The volume of a cone with radius 3 units and height 6 units is 18π cubic units.",
        "14. True or False: The volume of a rectangular prism is calculated as length × width × height.",
        "15. True or False: The volume of a cylinder with radius 2 units and height 5 units is 20 cubic units."
    ]

    options = [
    [("9 cubic units", "a1"), ("27 cubic units", "a2"), ("18 cubic units", "a3"), ("36 cubic units", "a4")],
    [("20π cubic units", "b1"), ("40π cubic units", "b2"), ("60π cubic units", "b3"), ("80π cubic units", "b4")],
    [("64π cubic units", "c1"), ("128π cubic units", "c2"), ("256π cubic units", "c3"), ("512π cubic units", "c4")],
    [("27π cubic units", "d1"), ("81π cubic units", "d2"), ("54π cubic units", "d3"), ("108π cubic units", "d4")],
    [("120 cubic units", "e1"), ("110 cubic units", "e2"), ("130 cubic units", "e3"), ("140 cubic units", "e4")],
    [("10 cubic units", "f1"), ("20 cubic units", "f2"), ("30 cubic units", "f3"), ("40 cubic units", "f4")],
    [("343 cubic units", "g1"), ("421 cubic units", "g2"), ("512 cubic units", "g3"), ("729 cubic units", "g4")],
    [("True", "h1"), ("False", "h2")],
    [("True", "i1"), ("False", "i2")],
    [("True", "j1"), ("False", "j2")],
    [("True", "k1"), ("False", "k2")],
    [("True", "l1"), ("False", "l2")]
    ]


    correct_answers = ["a2", "b2", "c2", "d2", "e1", "f1", "g1", "500/3 π", "63π", "8", "h1", "i1", "h2", "h1", "h2"]

    # Store user's answers
    user_answers = {i + 1: StringVar() for i in range(15)}
    user_entries = {}

    # Function to display question
    def display_question(index):
        for widget in quiz_window.winfo_children():
            if widget not in [homepage_return, close_program, quiz_window_title]:
                widget.destroy()

        question_label = CTkLabel(quiz_window, text=questions[index], text_color="#3F49A4", bg_color="#C1E1C1", font=Text_font)
        question_label.place(x=40, y=100)

        if index < 7:
            option_y_offset = 130
            for option_text, option_value in options[index]:
                option_button = CTkRadioButton(quiz_window, text=option_text, value=option_value, variable=user_answers[index + 1], bg_color="#C1E1C1", text_color="#3F49A4", font=Text_font)
                option_button.place(x=60, y=option_y_offset)
                option_y_offset += 30
        elif 7 <= index < 10:
            user_entries[index + 1] = CTkEntry(quiz_window, textvariable=user_answers[index + 1], font=Text_font, width=200)
            user_entries[index + 1].place(x=60, y=130)
        else:
            option_y_offset = 130
            for option_text, option_value in options[index - 3]:
                option_button = CTkRadioButton(quiz_window, text=option_text, value=option_value, variable=user_answers[index + 1], bg_color="#C1E1C1", text_color="#3F49A4", font=Text_font)
                option_button.place(x=60, y=option_y_offset)
                option_y_offset += 30

        previous_button = CTkButton(quiz_window, text="Previous", bg_color="#C1E1C1", corner_radius=10, font=Button_font, height=50, width=150, fg_color="#32A8A0", hover_color="#144A46", command=lambda: handle_navigation(index - 1)) if index > 0 else None
        if previous_button:
            previous_button.place(x=200, y=500)

        next_button_text = "Submit" if index == len(questions) - 1 else "Next"
        next_button = CTkButton(quiz_window, text=next_button_text, bg_color="#C1E1C1", corner_radius=10, font=Button_font, height=50, width=150, fg_color="#32A8A0", hover_color="#144A46", command=lambda: handle_navigation(index + 1))
        next_button.place(x=400, y=500)

    # Function to handle navigation between questions
    def handle_navigation(index):
        if 0 <= index < len(questions):
            display_question(index)
        elif index == len(questions):
            show_score()

    # Function to check the answers and show the score
    def show_score():
        score = 0
        for i, correct_answer in enumerate(correct_answers):
            if user_answers[i + 1].get().strip() == correct_answer:
                score += 1
        percentage = (score / len(questions)) * 100
        for widget in quiz_window.winfo_children():
            if widget not in [homepage_return, close_program, quiz_window_title]:
                widget.destroy()
        result_text = f"You scored {score} out of {len(questions)} ({percentage:.2f}%)"
        result_label = CTkLabel(quiz_window, text=result_text, text_color="#4263F5", bg_color="#C1E1C1", font=Subheading_font)
        result_label.place(x=400, y=250)

        back_to_home_button = CTkButton(quiz_window, text="Back to Home", bg_color="#C1E1C1", corner_radius=20, font=Button_font, height=50, width=150, fg_color="#32A8A0", hover_color="#144A46", command=back_to_homepage)
        back_to_home_button.place(x=400, y=350)

    # Commands for buttons on Quiz window
    def back_to_homepage():
        quiz_window.destroy()
        open_homepage()

    # Buttons for Quiz Window
    homepage_return = CTkButton(quiz_window, text="Back", bg_color="#C1E1C1", corner_radius=20, font=Button_font, height=30, width=60, fg_color="#32A8A0", hover_color="#144A46", command=back_to_homepage)
    homepage_return.place(x=900, y=20)

    close_program = CTkButton(quiz_window, text="Close", bg_color="#C1E1C1", corner_radius=20, font=Button_font, height=30, width=60, fg_color="#32A8A0", hover_color="#144A46", command=quiz_window.destroy)
    close_program.place(x=900, y=60)

    # Initial display of the first question
    display_question(0)

    quiz_window.mainloop()



open_homepage()