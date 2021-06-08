
secret_word = "Tree"
users_guess = ""
left_guesses = 5
win = False

while users_guess != secret_word and left_guesses > 0:
    users_guess = input("\nLeft guesses: " + str(left_guesses) + ".\nEnter a guess: ")
    left_guesses -= 1
    if users_guess == secret_word:
        win = True

if win:
    print("You won.")
else:
    print("You lost.")
