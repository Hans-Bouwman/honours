# Play the game up 100.
for i in range(1, 100):
    # Output each loop.
    output = ""
    
    if i % 3 == 0:
        output += "Fizz"

    if i % 5 == 0:
        output += "Buzz"

    if output == "":
        output += str(i)

    print(output)