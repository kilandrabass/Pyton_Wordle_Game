"""
Name
Group members (first names): Kilandra 
COSC-010
Wordle Assignment

"""
import random

def main():
    secretWord = random.choice(getListOfWords("wordleAnswerWords.txt"))
    incorrectLetters = [] #Intialize Incorrect Guesses
    print("Incorrect letters so far: ", incorrectLetters)
    maxGuesses = 6
    guessesLeft = maxGuesses
  
    while guessesLeft > 0:
    #Ensure that the user enters a 5-letter word
      someGuess = input(f"Enter a five-letter word (guessesLeft: {guessesLeft}): ")
      while len(someGuess) != 5:
        print(someGuess, "is not a 5-letter word. Try again.")
        someGuess = input("Enter a five-letter word: ")
      
    #Check if the user's guess is correct
      evaluation = guess(someGuess, secretWord)
      print(someGuess)
      print(evaluation)
    
      incorrectLetters = updateIncorrectLetters(someGuess, secretWord, incorrectLetters)
      print("Incorrect letters so far:", incorrectLetters)
    
      if secretWord.upper() == evaluation:
          print("You win!")
          return
      else:
          guessesLeft -= 1
          print("Sorry, that's not correct. You have", guessesLeft, "guesses left.")
          if guessesLeft == 0:
            print("Sorry - you are out of guesses. The secret word was", secretWord)
            return

def getListOfWords(fileName):
    with open(fileName, "r") as myfile:
      fileText = myfile.read()
    fileLines = fileText.split("\n")
    return fileLines

def guess(someGuess, secretWord):
# Define your guessing logic here
  outputString = ""
  for i in range(len(someGuess)):
    if someGuess[i] == secretWord[i]:
      outputString += someGuess[i].upper()
    elif someGuess[i] in secretWord:
      outputString += "o"
    else:
      outputString += "x"
  return outputString

def updateIncorrectLetters(someGuess, secretWord, incorrectLetters):
  for char in someGuess:
      if char not in secretWord and char not in incorrectLetters:
          incorrectLetters.append(char)
  incorrectLetters.sort()
  return incorrectLetters

  
main()