import random

tryNumber = 5
chosenFruit = None
rightLetters = None

def init():
    global rightLetters
    global chosenFruit
    fruits = ('Orange', 'Apple', 'Avocado', 'Mango', 'Peach', 'Cherry', 'Grape', 'Banana', 'Watermelon', 'Strawberry', 'Blueberry', 'Guava', 'Raspberry', 'Kiwi', 'Apricot', 'Pear', 'Fig', 'Lemon', 'Papaya', 'Pomegranate', 'Plum', 'Passion fruit', 'Coconut', 'Lychee')
    chosenFruit = random.choice(fruits).upper()
    rightLetters = ['_'] * len(chosenFruit)

def numberOfTries():
    global tryNumber
    tryNumber -= 1
    if(tryNumber > 1):
        print('You can try {} more times'.format(tryNumber))
    elif(tryNumber > 0):
        print('!!! It\'s your last chance !!!')

def guessCheck(guess):
    index = 0
    for letter in chosenFruit:
        if(letter == guess):
            rightLetters[index] = guess
        index += 1

def run():
    init()
    print('***************************************')
    print('** Welcome to Hangman game - Fruits! **')
    print('***************************************') 
    winner = False
    while(tryNumber > 0):
        print(rightLetters)
        guess = input("\nGive me a letter\n").upper()
        if(guess in rightLetters):
            print('You gave me a repeated letter')
        elif(guess in chosenFruit):
            guessCheck(guess)
        else:
            numberOfTries(    )
        if(not '_' in rightLetters):
            winner = True
            break

    if(winner):
        print('Congratulations, you win!!!')
    else:
        print("Sorry, the fruit was {}. \nThank you for playing".format(chosenFruit))

if __name__ == "__main__":
    run()