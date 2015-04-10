import random


counter = 0
name = raw_input("Howdy, what's your name?")

print "%s, I'm thinking of a number between 1 and 100" % name
print "Try to guess my number"

random_number = random.randrange(1,101)


while True:
    guess = int(raw_input("Your guess?"))
    counter += 1
    if guess > 0 and guess < 101:
        if guess < random_number:
            print "Your guess is too low, try again."
        elif guess < random_number:
            print "Your guess is too high, try again."
        else:
            print "Well done, %s! You found my number in %d tries!" % (name, counter)
            break
    else:
        "Guess must be between 1 and 100"
