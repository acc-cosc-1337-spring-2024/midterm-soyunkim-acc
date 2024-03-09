import question_a



option = "y"

while option.upper() == "Y":

        user_guess = int(input("Guess a number from 1 - 5:  "))
        random_num = question_a.get_random_number()

        if user_guess == random_num:
                print("Congratulations! You guessed it correctly.")

        elif user_guess != random_num:
                print("Random number was", random_num)

        option = input("Try again? (y/n): ")

print('Bye!')
