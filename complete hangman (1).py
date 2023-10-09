from tkinter import *
from tkinter.messagebox import showinfo
import random

def ok_func():                # moiz work
    def guess_func():         # to evaluate guess
        global tries, alpha, warnings
        guess = entered.get().lower()

        alpha = alpha.split()
        alphabet = ''
        for i in alpha:  # to edit available letters strings
            if not (i == guess):
                alphabet += i + ' '
        alpha = alphabet
        if guess != '':                  #guess should contain something to evalaute on
            if not (guess.isalpha()):  # to check if entered character is invalid
                warnings -= 1
                invalid_lab = Label(hangman, text='That is not a valid character',font=("Arial", 10, "bold"),fg='#000000',bg='#FFD700')
                invalid_lab.place(x=50,y=340)

            if guess in l:             # to check if character is already entered
                warnings -= 1
                already_lab = Label(hangman, text='You have already entered the letter',font=("Arial", 10, "bold"),fg='#000000',bg='#FFD700')
                already_lab.place(x=50,y=340)

            if guess not in word:
                if guess in vowels:  # to check if entered character is a vowel
                    tries -= 2
                    not_lab = Label(hangman, text='That is not in the word',font=("Arial", 10, "bold"),fg='#000000',bg='#ff0000')
                    not_lab.place(x=50,y=340)

                elif guess.isalpha():  # to check if entered character is valid
                    tries -= 1
                    not_lab = Label(hangman, text='That is not in the word',font=("Arial", 10, "bold"),fg='#000000',bg='#ff0000')
                    not_lab.place(x=50,y=340)

            elif guess not in l:
                good_guess = Label(hangman, text='Good guess', font=("Arial", 10, "bold"),fg='#000000',bg='#00e600')
                good_guess.place(x=50,y=340)
                for k in range(len(word)):  # to replace the letter in the list in accordance with the index
                    if word[k] == guess:
                        l[k: k + 1] = [word[k]]

            if warnings < 1:
                tries -= 1

    name = name_entry.get()
    game.destroy()

    f = open('words.txt')             #Huzaifa work
    lst = f.read()
    lst = lst.split()
    word = random.choice(lst)
    print(word)
    f.close()

    unique = 0              # Moiz work
    for u in word:          # to count unique letters
        if word.count(u) == 1:
            unique += 1

    l = ['_']
    mis = len(word) - len(l)
    for i in range(mis):
        l[len(l):] = ['_']

    global tries, warnings, alpha, vowels, guess
    tries = 6
    warnings = 3
    alpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    vowels = 'aeiou'
    guess = ''
    while True:
        hangman = Tk()
        hangman.title("Hangman")            # window formatting
        hangman.geometry("852x480+180+80")
        hangman.configure(background="#000000")

        if tries >= 5:
            photo1 = PhotoImage(file='hangman1.png')
            photo_lab = Label(hangman, image= photo1,bg='#000000')
            photo_lab.image= photo1
            photo_lab.place(x=500,y=40)
        elif tries >= 3:
            photo1 = PhotoImage(file='hangman2.png')
            photo_lab = Label(hangman, image= photo1,bg='#000000')
            photo_lab.image= photo1
            photo_lab.place(x=500,y=40)
        else:
            photo1 = PhotoImage(file='hangman3.png')
            photo_lab = Label(hangman, image= photo1,bg='#000000')
            photo_lab.image= photo1
            photo_lab.place(x=500,y=40)
        
        player_name = Label(hangman, text=f"Player Name = {name}", font=("Muara Slant", 18), fg="#F4E409",bg="#000000")
        player_name.place(x=40,y=30)

        tries_lab = Label(hangman, text=f"Guesses = {tries}", font=("Helvecta", 11, "bold"), fg="#EAEAEA",bg="#000000")
        tries_lab.place(x=40,y=80)

        warn_lab = Label(hangman, text=f"Warnings = {warnings}", font=("Helvecta", 11, "bold"), fg="#EAEAEA",bg="#000000")
        warn_lab.place(x=300,y=80)

        length = Label(hangman, text=f'I am thinking of a word that is {len(word)} letters long',font=("Helvecta", 12, "bold"),fg='#FFFFFF',bg='#000000')
        length.place(x=50,y=140)

        str1 = ''
        for i in l:
            str1 += i

        str2 = ''
        for j in str1:
            str2 += j + ' '

        if str1 == word:                 # Shahzaib's work
            global score                 # to use it in high score function
            global Win_score             # to use the whole function Win_score for displaying high scores
            score = tries * unique
            hangman.destroy()

            fs = open("high score list.txt", "a+")
            fs.write(name + "\t" + str(score) + "\n")

            Win_score = Tk()             # winning window
            Win_score.geometry("852x480+180+80")
            Win_score.configure(background="black")

            C_label = Label(Win_score,text="CONGRATULATIONS!\nYOU WON",font=("Rubik Medium", 35,"bold"),fg="#F4E409",bg="black",pady=20)
            C_label.place(x=100,y=20)

            fs = open("high score list.txt", "r+")
            content = fs.read().split()

            D = {}                 # for storing names and scores
            for i in content:
                if i.isalpha():
                    key = i
                if i.isdigit():
                    value = i
                    D[key] = value

            sorted_L = sorted(D.items(),key=lambda x: x[1])         #converts dict to a sorted List
            fs.close()

            if len(sorted_L) >= 3:
                global scr1, scr2, scr3, name1, name2, name3
                scr1 = int(sorted_L[-1][1])                         # needs to be in int when comparing with score below
                scr2 = sorted_L[-2][1]
                scr3 = sorted_L[-3][1]

                name1 = sorted_L[-1][0]
                name2 = sorted_L[-2][0]
                name3 = sorted_L[-3][0]
            else:
                scr1 = 0
                scr2 = 0
                scr3 = 0
                name1 = "NA"
                name2 = "NA"
                name3 = "NA"

            if score > scr1:                                         # condition for displaying new high score
                beatHS = Label(Win_score,text="You achieved a new high score:\n " + str([score]) + "\n\n",font=("Rubik Medium", 25),fg="#4ce4f5",bg="black",pady=20)
                beatHS.place(x=130,y=180)
            else:
                s_lab = Label(Win_score,text="Your score for this game is:\n" + str([score]) + "\n\n",font=("Rubik Medium", 25),fg="#4ce4f5",bg="black",pady=30)
                s_lab.place(x=130,y=180)

            win_pic = PhotoImage(file='win.png')
            photoLab = Label(Win_score,image=win_pic,bg='#000000')
            photoLab.image = win_pic
            photoLab.place(x=600,y=190)

            main_menu = Button(Win_score,text="Main Menu",font=("Helvecta",12,'bold'),fg="#000000",bg="#FF9001",relief="raised",bd=9,command=Win_score.destroy)
            main_menu.place(x=290,y=380)

            Win_score.mainloop()
            break

        lst_lab = Label(hangman, text=str2,font=("Helvecta", 12, "bold"),fg='#FFFFFF',bg='#000000')        # Moiz work
        lst_lab.place(x=120,y=190)

        available = Label(hangman, text=f'Available letters: \t {alpha}',font=("Helvecta", 12, "bold"),fg='#FFFFFF',bg='#000000')
        available.place(x=50,y=240)

        guess_lab = Label(hangman, text='Enter your guess:', font=("Helvecta", 12, "bold"),fg='#FFFFFF',bg='#000000')
        guess_lab.place(x=50,y=290)

        entered = Entry(hangman, width=6,font=("Helvecta", 12))
        entered.place(x=200,y=290)

        ok_b = Button(hangman, text='>', command=guess_func,font=("Helvecta", 8, "bold"),fg='#000000',bg='#F4E409',relief="raised",bd=3)
        ok_b.place(x=270,y=290)

        if tries <= 0:                               # shahzaib work
            hangman.destroy()

            Lose_score = Tk()                        # losing window
            Lose_score.geometry("852x480+180+80")
            Lose_score.configure(background="black")

            L_label = Label(Lose_score, text="YOU LOSE!\n",font=("Rubik Medium", 35, "bold"),fg="#F4E409",bg="black",pady=20)
            L_label.place(x=200,y=20)

            word_lab = Label(Lose_score,text='The word was:\n\n\" ' + word.upper() + ' \"', font=("Rubik Medium", 28),fg="#4ce4f5",bg="black",pady=30)
            word_lab.place(x=200,y=150)

            lose_pic = PhotoImage(file='lose.png')
            photoLab = Label(Lose_score,image=lose_pic,bg='#000000')
            photoLab.image = lose_pic
            photoLab.place(x=530,y=150)

            main_menu = Button(Lose_score,text="Main Menu",font=("Helvecta",12,'bold'),fg="#000000",bg="#FF9001",relief="raised",bd=9,command=Lose_score.destroy)
            main_menu.place(x=260,y=370)

            Lose_score.mainloop()
            break

        confirm_b = Button(hangman, text='Next',font=('Helvecta',12,'bold'),fg='#000000',bg='#FF9001', command=hangman.destroy,relief="raised",bd=6)          # Moiz work
        confirm_b.place(x=300,y=370)
        
        hangman.mainloop()


def game_func():                 #moiz work
    Player.destroy()
    global game

    game = Tk()
    game.title("Name")
    game.geometry("600x360+340+130")
    game.configure(background="#000000")

    empty = Label(game,text='',bg='#000000')
    empty.pack(anchor='center',pady=40)
 
    name = Label(game, text="Enter your Name:",  font=("Helvecta", 15, 'bold'), fg="#F4E409", bg="#000000", pady=20)
    name.pack(anchor='nw',padx=160)
    
    global name_entry
    name_entry = Entry(game, width=30, font=("Helvecta", 12))
    name_entry.pack(anchor='center')

    ok_button = Button(game, text="Ok",font=("Helvecta", 12, 'bold'), fg="#000000", bg="#FF9001", relief="raised", bd=12, command=ok_func)
    ok_button.pack(anchor='center',pady=50)

    game.mainloop()


def add_word():            # Huzaifa work
    word_entry.delete(0,END)
    word = word_entry.get()
    with open("words.txt", "a") as file:
        file.write(word + " ")

def C1():                 # Huzaifa work
    global addword
    administrator.destroy()
    addword = Tk()          # to add a word into file
    addword.title("Administrator Interface")
    addword.geometry("600x360+340+130")
    addword.configure(background="#000000")

    lab10 = Label(addword, text="ADD WORD", font=("Muara Slant", 20), fg="#F4E409", bg="#000000", pady=30)
    lab10.pack()

    word_label = Label(addword, text="Enter a word: ", font=("Helvecta", 12, 'bold'), fg="#F4E409", bg="#000000")
    word_label.place(x=160, y=100)

    global word_entry
    word_entry = Entry(addword, width=30, font=("Helvecta", 12, 'bold'), fg="#F4E409")
    word_entry.place(x=160, y=135)

    wd_submit = Button(addword, text="Add Word", font=("Helvecta", 12, 'bold'), fg="#000000", bg="#FF9001",
                       relief="raised", bd=7, command=add_word)
    wd_submit.place(x=240, y=180)

    wd_back = Button(addword, text="Back", font=("Helvecta", 12, 'bold'), fg="#000000", bg="#FF9001", relief="raised",
                     bd=7, command=addword.destroy)
    wd_back.place(x=255, y=240)

    
def ad_func():          # admin function            # Huzaifa work
    def submit():
        if id_entry.get() == "kashif" and pass_entry.get() == "12345678":
            global administrator
            administrator = Tk()
            administrator.title("Administrator Interface")
            administrator.geometry("600x360+340+130")
            administrator.configure(background="#000000")
            admin.destroy()

            lab9 = Label(administrator, text="ADMINISTRATOR INTERFACE", font=("Muara Slant", 20), fg="#F4E409", bg="#000000", pady=30)
            lab9.pack()

            Addword = Button(administrator, text="Add Word", font=("Helvecta", 12, 'bold'), fg="#000000", bg="#FF9001",
                            relief="raised", bd=7, command=C1)
            Addword.place(x=242, y=115)

            rstbutton = Button(administrator, text="Reset High Score", font=("Helvecta", 12, 'bold'), fg="#000000", bg="#FF9001",
                             relief="raised", bd=7)
            rstbutton.place(x=212, y=180)

            ad_back = Button(administrator, text="Back", font=("Helvecta", 12, 'bold'), fg="#000000", bg="#FF9001",
                             relief="raised", bd=7, command=administrator.destroy)
            ad_back.place(x=257, y=243)

        else:
            showinfo(message='Access Denied')

    admin = Tk()                         # Login window        # Huzaifa work
    admin.geometry("600x360+340+130")
    admin.title("Authentication")
    admin.configure(background="#000000")
    window.destroy()

    loginLabel = Label(admin, text="Admin Login", font=("Muara Slant", 25,"bold"), fg="#F4E409", bg="#000000", pady=20)
    loginLabel.pack()

    ad_label = Label(admin, text="Enter Admin ID: ", font=("Helvecta", 14), fg="#4ce4f5", bg="#000000")
    ad_label.place(x=160, y=80)

    id_entry = Entry(admin, width=30, font=("Helvecta", 12))
    id_entry.place(x=160, y=105)

    pass_label = Label(admin, text="Enter Password:", font=("Helvecta", 14), fg="#4ce4f5", bg="#000000")
    pass_label.place(x=160, y=155)

    pass_entry = Entry(admin, width=30, font=("Helvecta", 12))
    pass_entry.place(x=160, y=180)

    submit = Button(admin, text="Confirm", font=("Helvecta", 12, 'bold'), fg="#000000", bg="#FF9001", relief="raised", bd=7, command=submit)
    submit.place(x=260, y=240)


def user_func():                   # player function
    def high_score():              # Shahzaib work
        global name
        Player.destroy()
        hs_window = Tk()           # this window will display top 3 high scores
        hs_window.geometry("700x460+340+130")
        hs_window.configure(background="black")
        hs_window.title("High Scores")

        hs_lab = Label(hs_window,text="High Score List",fg="#F4E409",bg="#000000",font=("Rubik Medium",30,'bold'),pady=20)
        hs_lab.grid(row=0,column=1)

        name_lab = Label(hs_window,text="Name",fg="white",bg="#000000",font=("Helvecta",22,'bold'),pady=20)
        name_lab.grid(row=1,column=0)

        scor_lab = Label(hs_window,text="Score",fg="white",bg="#000000",font=("Helvecta", 22,'bold'),padx=40)
        scor_lab.grid(row=1,column=2)

        name1_lab = Label(hs_window,text=name1,fg="#4ce4f5",bg="#000000",font=("Helvecta",20),padx=40)
        name1_lab.grid(row=2,column=0)

        HS_lab = Label(hs_window,text=scr1,fg="#4ce4f5",bg="#000000",font=("Helvecta", 20))
        HS_lab.grid(row=2,column=2)

        name2_lab = Label(hs_window,text=name2,fg="#4ce4f5",bg="#000000",font=("Helvecta",20),padx=40)
        name2_lab.grid(row=3,column=0)

        SHS_lab = Label(hs_window,text=scr2,fg="#4ce4f5",bg="#000000",font=("Helvecta",20))
        SHS_lab.grid(row=3,column=2)

        name3_lab = Label(hs_window,text=name3,fg="#4ce4f5",bg="#000000",font=("Helvecta",20),padx=30)
        name3_lab.grid(row=4,column=0)

        THS_lab = Label(hs_window,text=scr3,fg="#4ce4f5",bg="#000000",font=("Helvecta",20))
        THS_lab.grid(row=4,column=2)

        hs_window.mainloop()

    global Player            # Moiz work
    Player = Tk()
    Player.geometry("852x480+180+80")
    Player.title("Player")
    Player.configure(background="#000000")
    window.destroy()

    lab1 = Label(Player, text="User", font=("Muara Slant", 30), fg="#F4E409", bg="#000000", pady=30)
    lab1.pack()

    play_game = Button(Player, text="Play Game", font=("Helvecta", 15, 'bold'), fg="#000000", bg="#FF9001",
                       relief="raised", bd=12, command=game_func)
    play_game.pack(anchor='center', pady=18)

    dis_score = Button(Player, text="High Scores", font=("Helvecta", 15, 'bold'), fg="#000000", bg="#FF9001",
                       relief="raised", bd=12,command=high_score)
    dis_score.pack(anchor='center', pady=18)

    back_button = Button(Player, text="Back", font=("Helvecta", 15, 'bold'), fg="#000000", bg="#FF9001", relief="raised",
                     bd=12, command=Player.destroy)
    back_button.pack(anchor='center', pady=18)


def quit_func():       # quit function       # Moiz work
    quit()


while True:                      # shahzaib work
    window = Tk()                # first most window
    window.geometry("852x480+180+80")
    window.title("Hangman")
    window.configure(background="#000000")

    lab1 = Label(window, text="WELCOME TO HANGMAN", font=("Muara Slant", 24), fg="#F4E409", bg="#000000", pady=30)
    lab1.pack()

    UserButton = Button(window,text="User",font=("Arial", 15, 'bold'),fg="#000000",bg="#FF9001",relief="raised",bd=12,command=user_func)
    UserButton.pack(anchor='center',pady=18)

    AdminButton = Button(window,text="Administrator",font=("Arial",15,'bold'),fg="#000000",bg="#FF9001",relief="raised",bd=12,command=ad_func)
    AdminButton.pack(anchor='center',pady=18)

    Q_Button = Button(window,text="Quit",font=('Arial',15,'bold'),fg="#000000",bg="#FF9001",relief="raised",bd=12,command=quit_func)
    Q_Button.pack(anchor='center',pady=18)

    window.mainloop()
