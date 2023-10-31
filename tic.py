

def game():
        arr1 = [0, 1, 2]
        arr2 = [3, 4, 5]
        arr3 = [6, 7, 8]

        arr = [arr1, arr2, arr3]

        player1 = input("Please enter x or o : ")

        if player1 == 'x':
            player2 = 'o'
        elif player1 == 'o':
            player2 = 'x'

        print(f'player 1 - > {player1}')
        print(f'player 2 - > {player2}' )

        current_player = player1

        x = 0
        draw_condition = 9  

        while x != draw_condition:
            
            for row in arr:
                #asked chatgpt here to make it look like this -> 0 | 1 | 2 instead of [0,1,2]
                print(f" {row[0]:<4} |  {row[1]:<4}  |   {row[2]:<4} ")
                print("---------------------")
            
            choice = input(f"Player {current_player}, please enter a number slot: ")
            choice = int(choice)

            if choice <= 2:
                array = arr[0]
            elif 2 < choice < 6:
                array = arr[1]
            elif 5 < choice < 9:
                array = arr[2]
            else:
                print("Invalid choice. Try again.")
                continue

            if choice in array:
                index = array.index(choice)
                array[index] = current_player
                x = x + 1
            else:
                print("Slot already taken. Try again.")
                continue

            cond1hor = arr1[0] == arr1[1] == arr1[2] == current_player
            cond2hor = arr2[0] == arr2[1] == arr2[2] == current_player
            cond3hor = arr3[0] == arr3[1] == arr3[2] == current_player

            cond1ver = arr1[0] == arr2[0] == arr3[0] == current_player
            cond2ver = arr1[1] == arr2[1] == arr3[1] == current_player
            cond3ver = arr1[2] == arr2[2] == arr3[2] == current_player

            diagonal1 = arr1[0] == arr2[1] == arr3[2] == current_player
            diagonal2 = arr1[2] == arr2[1] == arr3[0] == current_player

            if cond1hor or cond2hor or cond3hor or cond1ver or cond2ver or cond3ver or diagonal1 or diagonal2:
                #asked chatgpt here to make it look like this -> 0 | 1 | 2 instead of [0,1,2]
                for row in arr:
                    print(f" {row[0]:<4} |  {row[1]:<4}  |   {row[2]:<4} ")
                    print("---------------------")
                print(f"Player {current_player} wins!")
                x = draw_condition
                break

            if x == draw_condition:
                print("It's a draw!")
                break

            # asked chatgpt how to switch to the second player
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1



def startgame():
    cond = 'y'
    while cond == 'y':
        game()
        cond = input("do you want to play again ? y/n : ")
        


game()