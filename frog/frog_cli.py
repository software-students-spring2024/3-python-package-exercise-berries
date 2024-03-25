
import argparse
from frog import frog

def main():
    parser = argparse.ArgumentParser(description="Welcome to the frog module!")
    
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
    
    try: 
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(e)
    
    if args.command == "hello":
        frog.hello(args.name)
    elif args.command == "encourage":
        frog.encourage()
    elif args.command == "frogmode":
        frog.frogmode()
    elif args.command == "feed":
        frog.feed(args.snack)
    elif args.command == "kill":
        frog.kill(args.anything)
    elif args.command == "goodbye":
        frog.goodbye(args.name)
    else:
        parser.print_help()     # print all the available commands
    
    
"""
    parser.add_argument("name", help="your name")
    parser.add_argument("action", help="action to perform")
    parser.add_argument("target", help="target of the action")
    
    args = parser.parse_args()
    
    print(args.name)
    print(args.action)
    print(args.target)
"""
    

# running the main functino for developement testing
if __name__ == "__main__":
    main()