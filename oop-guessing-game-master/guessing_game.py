class GuessingGame():
    answer = 17
    user_guess = None
    guessing_game_solved = False

    while guessing_game_solved == False:
        if user_guess != None:
            if user_guess > answer:
                print("High")
            elif user_guess < answer:
                print("Low")
            else:
                guessing_game_solved = True
                print("Correct")
                break

        user_guess = int(input("Enter your guess here => "))
    

GuessingGame()