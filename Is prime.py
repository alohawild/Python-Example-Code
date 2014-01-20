# number request.py


while (True):

  dataInput = input('Choose a number (or enter a non-number to end): ')


  try:
    number = int(dataInput)
  except: # anything
    break

  print("Number is ",number,".")
  print(" ")

  if number < 2: print("Is not prime.")
  else :
    print("Number might be prime--working....") # The sledhammer approach

    primeYes = True
    x = 2
    y = int(number ** 0.5) + 1 # rounding issue is avoided
    while (x<y):
        z = number % x
        if (z == 0) :
            primeYes = False
            break
        print("Test number: ",x, "Result: ",z)
        x=x+1
    
    if (primeYes): print("Yes this is a prime!")
    else : print("No this is not a prime:",number," factor of", x)

print("End of line...")
                            
