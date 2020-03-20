# Maps each number to a word.
mapping = {
    3: "Fizz",
    5: "Buzz",
    7: "Fuzz",
    11: "Bizz"
}

# Play the game up 100.
for i in range(1, 100):
    # Output each loop.
    output = ""

    # Check each map from a number to a word.
    for j in mapping:
        if i % j == 0: output += mapping[j]

    if not output: output = i

    print(output)