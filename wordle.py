import random
import pandas as pd


words = pd.read_csv("wordle.csv")


lastindex = words['word'].count()
randomnumber = random.randint(0 , lastindex)
print(randomnumber)
wordforgame = words.iloc[randomnumber][0]
print(wordforgame)
arrayofchars = ['_' , '_' , '_' , "_" , '_']

counter = 0 
game = 'sha8ala'
while counter!=7  or game != 'done':
    play = input(f"please enter a word consist of 5 letters ({6 - counter } tries left) :")

    if not words['word'].astype(str).str.contains(play, case=False, na=False).any() or len(play) != 5:
        print("That's not a word. Try again!")
        continue

    

    for i in range(5) :
        if play[i] == wordforgame[i] :
            arrayofchars[i] = play[i]
            
        elif play[i] != wordforgame[i]:
             None

    print(arrayofchars)
    counter = counter + 1 

    if arrayofchars == list(wordforgame):
                print(f"You got it right in {counter} tries ! welldone :) ")
                game = 'done'
                break

    if counter == 6 : 
        print("you have used all of you chances , Try again later ;)")
        break


        
