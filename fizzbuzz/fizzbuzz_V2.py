# Play the game up 100.
for i in range(1, 100):
    # Case 'Fizz'
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
        
    # Case 'Buzz'.
    if i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    
    # Case 'FizzBuzz'.
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")

    # Default case.
    if i % 3 != 0 and i % 5 != 0:
        print(i)