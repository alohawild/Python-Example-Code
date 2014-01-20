# Guess a number improved.py
# Written by Michael R Wild
# Maybe be used as you wish. No license. Version 1.0
# Just hacking in IDLE on my Black Mac

"""This is an example program that guesses a number between 1-20. It uses two methods, random and picking 1/2 way each time."""


import random
import string

def questionUser(questionText="Answer (Y=YES, N=No, E=End):"):

  """This function is the basic ask a user a question and force a Y/N/E reply. Just a basic question routine. Forces on error to END."""


  print(questionText)

  while(True):

    try:
      answerUser = input()
    except: # force I/O failure to be and End request
      return "E"

    if (answerUser == "Y"):
      return "Y"

    if (answerUser == "N"):
      return "N"
     
    if (answerUser == "E"):
      return "E"

    print("Try again")


# End def

while (True): # will break out when End Request


  print("Guess your number")
  print(" ")
  print("Please mentally pick a number between 1 - 20")

  dataInput = input('Press enter when ready (enter "End" to stop)')
  if (dataInput == "End"): break # << BREAK is here

  # intialize the search loop

  numberOfGuesses = 0
  remainingNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ,20]
  randomGuess = True


  while (True):

    countOfNumbers = len(remainingNumbers)
    numberOfGuesses += 1
    
    # Null case, users makes an error

    if (countOfNumbers == 0):
      print("There are no numbers left so one of us forgot their number or missed a question")
      print("Lets try that again...I win!")
      break # << Break is here if user makes a mistake

    # Null case, number is known

    if (countOfNumbers == 1):
      print("Your number is:",remainingNumbers)
      print("It took only", numberOfGuesses)
      break # << Break is here when guess made 
    
    if (randomGuess): # Just guess
      guessPosition = random.randint(0, (countOfNumbers-1))
      randomGuess = False
    else: # Take mid-point
      guessPosition = int((countOfNumbers-1) / 2)
      randomGuess = True
    guess = remainingNumbers[guessPosition]
    

    questionText = "Is your number " + str(guess) + " ? (Y/N)"
    userResponse = questionUser(questionText)

    # process user information

    if (userResponse == "Y"):
      print("It took only", numberOfGuesses)
      break # << Break is here when guess made

    if (userResponse == "E"):
      break # << Break is here to end loop


    # Need to move to next question

    questionText = "Is your number greater than my guess of " + str(guess) + " ? (Y/N)"
    userResponse = questionUser(questionText)
      
    if (userResponse == "E"):
      break # << Break is here to end loop

    if (userResponse == "Y"):
      for listNumber in remainingNumbers[:]:
        if listNumber <= guess:
          remainingNumbers.remove(listNumber)
    else :
      for listNumber in remainingNumbers[:]:
        if listNumber >= guess:
          remainingNumbers.remove(listNumber)

    
    print("Remaining Guesses:", remainingNumbers,".")
    print(" ")

  # End of loop


# End of loop
print("End of line...")
                            
