import random


import argparse
import sys


# function that lists all the available functions in the module
### the parser help is used instead ###
### help() not used in main, can be deleted/commented out ###
'''
def help():
    
    print("hello(your name): the frog says hello to you ;)  (replace 'your name' with your name!)")
    print("encourage(): the frog gives you a silly little pep talk <3")
    print("frogmode(): the frogs gets into frog mode and eats bugs with you! ")
    print("feed(snack): feed the frog a yummy snack!    (replace 'snack' with your choice of snack!)")
    print("kill(anything): the fighter frog kills anything for you!  (replace 'anything' with anything you want to kill!)")
    print("goodbye(your name): frog says goodbye to you!  (replace 'your name' with your name!)")
'''

    
    
# ---------------------------------------------------------------------------- #
#                              available functions                             #
# ---------------------------------------------------------------------------- #


def hello(name):
    print('\U0001F438: Hi there ' + name + '!')


def encourage():
    frogs_decision = random.randint(1, 3)
    
    if frogs_decision == 1:
        print('\U0001F438: You are the smartest frog in the pond!')
    elif frogs_decision == 2:
        print('\U0001F438: You got this! Leap by leap!')
    else:
        print('\U0001F438: You are amazing!')
    

def frogmode():
    print("\U0001F438: I EAT BUGS, let's eat bugs together")


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
    
    
def goodbye(name):
    print('\U0001F438: Bye bye ' + name+ ', go catch some flies for me!')
    


import argparse

class Custom_ArgParser(argparse.ArgumentParser):
    def error(self, message):
        # stderr -> standard error in linux
        sys.stderr.write(f'ERROR: {message}\n')
        sys.stderr.write("Please enter the correct amount of arguments.\n")
        print()
        self.print_help()
        sys.exit(2)
        
def args_parser():
    parser = Custom_ArgParser(description="Welcome to the frog module!")
    
    # the function wanted to be called
    subparsers = parser.add_subparsers(help="command", dest="command")

    
    hello_parser = subparsers.add_parser("hello", help="the frog says hello to you")
    hello_parser.add_argument("name", help="your name")
    
    subparsers.add_parser("encourage", help="the frog gives you a silly little pep talk <3")
    
    subparsers.add_parser("frogmode", help="the frogs gets into frog mode and eats bugs with you!")
    
    feed_parser = subparsers.add_parser("feed", help="feed the frog a yummy snack!")
    feed_parser.add_argument("snack", help="the snack you would like to feed the frog")
    
    kill_parser = subparsers.add_parser("kill", help="the fighter frog kills anything for you!")    
    kill_parser.add_argument("anything", help="anything you want the frog to kill for you")
    
    goodbye_parser = subparsers.add_parser("goodbye", help="frog says goodbye to you!")
    goodbye_parser.add_argument("name", help="your name")
    
    return parser

""" 
# this function doesnt work - needs to override this with custom class 
def handle_argument_error(e):
    print(f"Error: {str(e)}")
    print("Please enter the correct amount of arguments")
"""

def main():
    parser = args_parser()
    
    try:
        args = parser.parse_args()
        # call respective function
        if args.command == "hello":
            hello(args.name)
        elif args.command == "encourage":
            encourage()
        elif args.command == "frogmode":
            frogmode()
        elif args.command == "feed":
            feed(args.snack)
        elif args.command == "kill":
            kill(args.anything)
        elif args.command == "goodbye":
            goodbye(args.name)
    except Exception as e:  # Catching generic exception for demonstration; customize as needed
        #handle_argument_error()
        print(e)  # Optionally print the error message

if __name__ == "__main__":
    main()

