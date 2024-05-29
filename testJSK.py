from customtkinter import *
from PIL import Image, ImageTk

#Fonts used throughout the code 
Title_font = ("Impact", 50, "bold", "underline")
Button_font = ("Times", 20, "italic")
Subittle_font1 = ("Impact", 30, "bold", "italic")
Subheading_font = ("Impact", 20, "italic")
Text_font = (("courior", 13))

current_question_index = 0
score = 0

questions = [
    {
        "question": "What year did World War II start?",
        "options": ["1939", "1941", "1942", "1945"],
        "answer": "1939"
    },
    {
        "question": "When did World War II end?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1945"
    },
    {
        "question": "Which country was not part of the Axis Powers in World War II?",
        "options": ["Germany", "Japan", "Italy", "France"],
        "answer": "France"
    },
    {
        "question": "Who was the Prime Minister of the United Kingdom during most of World War II?",
        "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
        "answer": "Winston Churchill"
    },
    {
        "question": "Which event led to the United States entering World War II?",
        "options": ["Attack on Pearl Harbor", "Battle of Stalingrad", "D-Day", "Bombing of Hiroshima"],
        "answer": "Attack on Pearl Harbor"
    },
    {
        "question": "What year did World War II start?",
        "options": ["1939", "1941", "1942", "1945"],
        "answer": "1939"
    },
    {
        "question": "When did World War II end?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1945"
    },
    {
        "question": "Which country was not part of the Axis Powers in World War II?",
        "options": ["Germany", "Japan", "Italy", "France"],
        "answer": "France"
    },
    {
        "question": "Who was the Prime Minister of the United Kingdom during most of World War II?",
        "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
        "answer": "Winston Churchill"
    },
    {
        "question": "Which event led to the United States entering World War II?",
        "options": ["Attack on Pearl Harbor", "Battle of Stalingrad", "D-Day", "Bombing of Hiroshima"],
        "answer": "Attack on Pearl Harbor"
    },
    {
        "question": "What year did World War II start?",
        "options": ["1939", "1941", "1942", "1945"],
        "answer": "1939"
    },
    {
        "question": "When did World War II end?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1945"
    },
    {
        "question": "Which country was not part of the Axis Powers in World War II?",
        "options": ["Germany", "Japan", "Italy", "France"],
        "answer": "France"
    },
    {
        "question": "Who was the Prime Minister of the United Kingdom during most of World War II?",
        "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
        "answer": "Winston Churchill"
    },
    {
        "question": "Which event led to the United States entering World War II?",
        "options": ["Attack on Pearl Harbor", "Battle of Stalingrad", "D-Day", "Bombing of Hiroshima"],
        "answer": "Attack on Pearl Harbor"
    },
    {
        "question": "What year did World War II start?",
        "options": ["1939", "1941", "1942", "1945"],
        "answer": "1939"
    },
    {
        "question": "When did World War II end?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1945"
    },
    {
        "question": "Which country was not part of the Axis Powers in World War II?",
        "options": ["Germany", "Japan", "Italy", "France"],
        "answer": "France"
    },
    {
        "question": "Who was the Prime Minister of the United Kingdom during most of World War II?",
        "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
        "answer": "Winston Churchill"
    },
    {
        "question": "Which event led to the United States entering World War II?",
        "options": ["Attack on Pearl Harbor", "Battle of Stalingrad", "D-Day", "Bombing of Hiroshima"],
        "answer": "Attack on Pearl Harbor"
    }
]

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
        Open_Quiz()


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

# Code for the quiz
def Open_Quiz():
    global current_question_index, score
    current_question_index = 0
    score = 0
    quiz = CTk()
    quiz.title("Math Marvels:Capturing Volume")
    quiz.minsize(width=1000, height = 700)
    quiz.maxsize(width=1000, height = 700)
    quiz.resizable(False,False)
    quiz.config(bg= "#C1E1C1")
    quiz_page_tittle = (CTkLabel(quiz, text=('Formula Sheet For Quiz!!!'), 
                                  text_color="#4263F5",
                                  bg_color="#C1E1C1", 
                                  font = Title_font)
                                  )
    quiz_page_tittle.place(x=20,y=20)

    def check_answer(selected_option):
        global current_question_index, score
        print(current_question_index)
        correct_answer = questions[current_question_index]["answer"]
        if selected_option == correct_answer:
            score += 1
        current_question_index += 1
        if current_question_index < len(questions):
            question_text.set(questions[current_question_index]["question"])
            score_label.config(text="Score: {}/{}".format(score, len(questions)))
            for i in range(4):
                option_buttons[i].config(text=questions[current_question_index]["options"][i])
        else:
            score_label.config(text="Score: {}/{}".format(score, len(questions)))
            question_text.set("Quiz Completed! Your Final Score: {}/{}".format(score, len(questions)))
            for button in option_buttons:
                button.config(state=DISABLED)
            submit_button.config(state=DISABLED)
            back_button.config(state=NORMAL)

    def restart_quiz():
        Open_Quiz.destroy()
        open_homepage()

    question_text = StringVar()
    question_text.set(questions[current_question_index]["question"])

    question_label = CTkLabel(Open_Quiz, textvariable=question_text, font=("Arial", 15))
    question_label.pack()

    option_buttons = []
    for i in range(4):
        option_button = CTkButton(Open_Quiz, text="", font=("Arial", 12),
                                   command=lambda i=i: check_answer(questions[current_question_index]["options"][i]))
        option_button.pack()
        option_buttons.append(option_button)

    for i in range(4):
        option_buttons[i].config(text=questions[current_question_index]["options"][i])

    score_label = CTkLabel(Open_Quiz, text="Score: 0/{}".format(len(questions)), font=("Arial", 12))
    score_label.pack()

    submit_button = CTkButton(Open_Quiz, text="Next", bg="lightgreen", font=("Arial", 15), command=lambda: check_answer(""))
    submit_button.pack()
    submit_button.place(x=100, y=400)

    back_button = CTkButton(Open_Quiz, text="Back", bg="lightgreen", font=("Arial", 15), command=restart_quiz)
    back_button.pack()
    back_button.place(x=200, y=400)
    back_button.config(state=DISABLED)

    Open_Quiz.mainloop()



open_homepage()