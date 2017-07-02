import random

# Tosses a coin a designated amount of times and prints the results
def toss_coin(times_to_toss):
    heads = 0
    tails = 0
    answer = "tail!"
    for i in range(times_to_toss + 1):
        # random float between 0 and 1
        rnd_value = random.random()
        # rounds to 0 or 1
        result = round(rnd_value)
        if result == 1:
            heads += 1
            answer = "head!"
        else:
            tails += 1
            answer = "tail!"
        print "Attempt #", i, ": Throwing a coin... It's a ", answer, " ... Got ", heads, "head(s) so far and ", tails, "tail(s) so far"

print "Starting the program..."
toss_coin(5000)
print "Ending the program, thank you!"