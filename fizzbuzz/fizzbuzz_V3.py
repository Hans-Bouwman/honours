# Play the game up 100.
for i in range(1, 100): 
    # Case 'FizzBuzz'.
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")

    # Case 'Fizz'
    elif i % 3 == 0:
        print("Fizz")
        
    # Case 'Buzz'.
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")

    # Default case.
    else:
        print(i)