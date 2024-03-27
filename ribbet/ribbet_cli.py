
import argparse
import sys
from ribbet import ribbet

class Custom_ArgParser(argparse.ArgumentParser):
    def error(self, message):
        # stderr -> standard error in linux
        sys.stderr.write(f'ERROR: {message}\n')
        sys.stderr.write("Please enter the correct amount of arguments.\n")
        print()
        # prints help table to show commands & args 
        # this line is key in overriding generic error handler 
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
            ribbet.hello(args.name)
        elif args.command == "encourage":
            ribbet.encourage()
        elif args.command == "frogmode":
            ribbet.frogmode()
        elif args.command == "feed":
            ribbet.feed(args.snack)
        elif args.command == "kill":
            ribbet.kill(args.anything)
        elif args.command == "goodbye":
            ribbet.goodbye(args.name)
    except Exception as e:  # Catching generic exception for demonstration; customize as needed
        #handle_argument_error()
        print(e)  # Optionally print the error message

if __name__ == "__main__":
    main()

