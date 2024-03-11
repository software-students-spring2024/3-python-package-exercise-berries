import random
import argparse

# function that lists all the available functions in the module
def help():
    
    print("hello(your name): the frog says hello to you ;)  (replace 'your name' with your name!)")
    print("encourage(): the frog gives you a silly little pep talk <3")
    print("frogmode(): the frogs gets into frog mode and eats bugs with you! ")
    print("feed(snack): feed the frog a yummy snack!    (replace 'snack' with your choice of snack!)")
    print("kill(anything): the fighter frog kills anything for you!  (replace 'anything' with anything you want to kill!)")
    print("goodbye(your name): frog says goodbye to you!  (replace 'your name' with your name!)")
    

    
    
# ---------------------------------------------------------------------------- #
#                              available functions                             #
# ---------------------------------------------------------------------------- #


def hello(user):
    print('\U0001F438: Hi there ' + user + '!')


def encourage():
    print('\U0001F438: You got this!')
    

def frogmode():
    print('\U0001F438: I EAT BUGS, lets eat bugs together')


def feed(snack):
    cap_snack = snack.capitalize()
    print("\U0001F438: Thanks for the sweet little treat! " + cap_snack + " is yummy! nom nom nom")
    
    
def kill(anything):
    frogs_decision = random.randint(1, 2)
    
    # frog is willing to kill for you!
    if frogs_decision == 1:
        print("\U0001F438: I killed " + anything + " for you! You are safe now!")
    
    # nuarr the frog is a pacifist
    else:
        print("\U0001F438: I don't like " + anything + ", I only eat yummy snacks! nom nom nom")
    
    
def goodbye(user):
    print('\U0001F438: Bye bye ' + user+ ', go catch some flies!')
    



def main():
    print("Welcome to the frog module!")
    
    
    
    
    
if __name__ == "__main__":
    main()
