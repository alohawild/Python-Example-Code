# number request.py
# Written by Michael R Wild
# Maybe be used as you wish. No license. 

import random

while (True): # will break out when End Request


  print("Guess your number")
  print(" ")
  print("Please mentally pick a number between 1 - 20")
  dataInput = input('Press enter when read (enter "End" to stop)')
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
    
    while (True):
      
      print("Is your number", guess, "? (Y/N)")
      answerGuess = input( )

      if (answerGuess == "Y" or answerGuess == "N"):
        break
      else:
        print("Try again")

    # End of Loop

    # process user information

    if (answerGuess == "Y"):
      print("It took only", numberOfGuesses)
      break # << Break is here when guess made

    # determine question to ask


    if (countOfNumbers > 1): # handle null case

      while (True):
      
        print("Is your number greater than my guess of", guess, "? (Y/N)")
        answerGuess = input()

        if (answerGuess == "Y" or answerGuess == "N"):
          break
        else:
          print("Try again")

      # End of Loop
      

      if (answerGuess == "Y"):
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
                          
