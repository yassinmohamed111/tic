import random
import pandas as pd
from termcolor import colored




from colorama import Fore, Style

# Define the ASCII art lines
w = [
    " ___       __      ",
    "|\\  \\     |\\  \\    ",
    "\\ \\  \\    \\ \\  \\   ",
    " \\ \\  \\  __\\ \\  \\  ",
    "  \\ \\  \\|\\__\\_\\  \\ ",
    "   \\ \\____________\\",
    "    \\|____________|",
]

# Define the ASCII art lines
o = [
    " ________     ",
    "|\\   ___ \\  ",
    "\\ \\  \\_|\\ \\  ",
    " \\ \\  \\ \\\\ \\ ",
    "  \\ \\  \\_\\\\ \\",
    "   \\ \\_______\\",
    "    \\|_______|",
]



r = [
    " ________     ",
    "|\\   __  \\    ",
    "\\ \\  \\|\\  \\   ",
    " \\ \\   _  _\\  ",
    "  \\ \\  \\\\  \\| ",
    "   \\ \\__\\\\ _\\ ",
    "    \\|__|\\|__|",
]


d = [
    "  _____  ",
    " |  __ \\ ",
    " | |  | |",
    " | |  | |",
    " | |__| |",
    " |_____/",
]

l = [
    " ___          ",
    "|\  \         ",
    "\\ \  \        ",
    " \\ \  \       ",
    "  \\ \  \____  ",
    "   \\ \_______\\",
    "    \|_______|",
]

e = [
    "  ______ ",
    " |  ____|",
    " | |__   ",
    " |  __|  ",
    " | |____ ",
    " |______",
]

# Define the color for the ASCII art
colored_w = [f"{Fore.GREEN}{line}{Style.RESET_ALL}" for line in w]
colored_o = [f"{Fore.GREEN}{line}{Style.RESET_ALL}" for line in o]
colored_r = [f"{Fore.GREEN}{line}{Style.RESET_ALL}" for line in r]
colored_d = [f"{Fore.GREEN}{line}{Style.RESET_ALL}" for line in d]
colored_l = [f"{Fore.GREEN}{line}{Style.RESET_ALL}" for line in l]
colored_e = [f"{Fore.GREEN}{line}{Style.RESET_ALL}" for line in e]

# Print "W" and "O" characters side by side
for line_w, line_o , line_r  , line_d , line_l , line_e , in zip(colored_w, colored_o , colored_r , colored_d , colored_l , colored_e):
    print(line_w + line_o + line_r  , line_d , line_l , line_e)



from colorama import Fore, Style

# Define the ASCII art lines
ascii_art = [
    "   ___    ___           ",
    "   |\\  \\  |\\  \\          ",
    " __\\_\\  \\_\\_\\  \\_____    ",
    "|\\____    ___    ____\\   ",
    "\\|___| \\  \\__|\\  \\___|   ",
    "    __\\_\\  \\_\\_\\  \\_____ ",
    "   |\\____    ____   ____\\",
    "   \\|___| \\  \\__|\\  \\___|",
    "         \\ \\__\\ \\ \\__\\   ",
    "          \\|__|  \\|__|"
]

# Define the color for the ASCII art (blue)
colored_ascii_art = [f"{Fore.BLUE}{line}{Style.RESET_ALL}" for line in ascii_art]

# Print the colored ASCII art
for line in colored_ascii_art:
    print(line)



print("")
print("welcome to wordle game in Python")
print("You have 2 random char hints only to use !")
print("goodluck :)")

words = pd.read_csv("wordle.csv")

def game():
    lastindex = words['word'].count()
    randomnumber = random.randint(0 , lastindex)

    wordforgame = words.iloc[randomnumber][0]
   

    arrayofchars = ['_' , '_' , '_' , "_" , '_']
    common_letters = ""
    unique_letters = ""
   
   
    counter = 0 
    hintcounter = 0
    game = 'sha8ala'
    while counter!=7  or game != 'done':
        
        play = input(f"please enter a word consist of 5 letters ({6 - counter } tries left) :")
    

        hint = 'hint'
        randomhint = random.randint(0 , 4)

        if play == hint and counter<3 :
              arrayofchars[randomhint] = wordforgame[randomhint]
              print(arrayofchars)
              hintcounter = hintcounter + 1
              print(f"{2 - hintcounter} hints left !")

        elif play == hint and counter > 3:
              print("you used all of your hints !")
              continue
        

        if not words['word'].astype(str).str.contains(play, case=False, na=False).any() or len(play) != 5:
            print("That's not a word. Try again!")
            continue

        

        for letter in play:
                    if letter in wordforgame and letter not in common_letters:
                        common_letters += letter
                        

        for letter in play:
                    if letter not in wordforgame and letter not in common_letters:
                        unique_letters += letter

        
        
        for i in range(5) :
          
            if play[i] == wordforgame[i] :
                arrayofchars[i] = play[i]
                
            elif play[i] != wordforgame[i]:
                None
           


     
        green_text = "\033[92m"
        yellow_text = "\033[93m"
        red_text = "\033[91m"
        reset_color = "\033[0m"

        
       
        sorted_uniqe = sorted(unique_letters)
        formatted_arrayofchars = f"{green_text}{arrayofchars}{reset_color}"
        formatted_common_letters = f"{yellow_text}{common_letters}{reset_color}"
        formatted_unique_letters = f"{red_text}{sorted_uniqe}{reset_color}"


        print(formatted_arrayofchars, " ", f" ({formatted_common_letters})", " ", f" ({formatted_unique_letters})")
        counter = counter + 1 

        if arrayofchars == list(wordforgame):
                    print(f"You got it right in {counter} tries ! welldone :) ")
                    game = 'done'
                    break

        if counter == 6 : 
            print(f"the answer is : {wordforgame} " )
            print("you have used all of you chances , Try again later ;)")
            break


            
def startgame():
    cond = 'y'
    while cond == 'y':
        game()
        print("################################################")
        cond = input("do you want to play again ? y/n : ")
        print("################################################")
        

startgame()