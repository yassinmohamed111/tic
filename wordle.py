import random
import pandas as pd
from termcolor import colored

words = pd.read_csv("wordle.csv")

def game():
    lastindex = words['word'].count()
    randomnumber = random.randint(0 , lastindex)

    wordforgame = words.iloc[randomnumber][0]

    arrayofchars = ['_' , '_' , '_' , "_" , '_']
    common_letters = ""
    unique_letters = ""
   
   
    counter = 0 
    game = 'sha8ala'
    while counter!=7  or game != 'done':
        
        play = input(f"please enter a word consist of 5 letters ({6 - counter } tries left) :")
    

    
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

        
       
        
        formatted_arrayofchars = f"{green_text}{arrayofchars}{reset_color}"
        formatted_common_letters = f"{yellow_text}{common_letters}{reset_color}"
        formatted_unique_letters = f"{red_text}{unique_letters}{reset_color}"


        # Print the text
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