![Workflow Status](https://github.com/software-students-spring2024/3-python-package-exercise-berries/actions/workflows/run-tests.yml/badge.svg)
# Python Package Exercise

We are building a frog 🐸, named ribbet, virtual pet that has four behaviors that can be called upon each with their own unique message/response. 


The unique responses will be: 
* **help**: List of commands 
* **hello(name)**: "🐸: Hi there (name)"
* **encourage**: "🐸: You are the smartest frog in the pond!",</br> 
"You got this! Leap by leap!" or </br>
"You are amazing!" selected based on the frog's mood! (randomly)
* **frogmode**: "🐸: I EAT BUGS, let's eat bugs together"
* **feed(snack)**: "🐸: Thanks for the sweet little treat! (snack) is yummy! Nom nom nom"
* **kill(anything)**: "🐸: I killed (anything) for you! You are safe now!" or </br>
"I don't like (anything), I only eat yummy snacks! nom nom nom" selected based on the frog's mood! (randomly)
* **bye(name)**: "🐸: Bye bye (name), go catch some flies for me!"


## Install 

Install the frog module using pip

```bash
  pip install frog 
```


## Usage
Call frog from the command line to interact with your virtual frog while coding.

To access menu with all functions: 
```bash
  frog
```
Functions: 
* hello
```bash
  frog hello {name}
```
* encourage
```bash
  frog encourage
```
* frogmode
```bash
  frog frogmode
```
* feed
```bash
  frog feed {snack}
```
* kill
```bash
  frog kill {anything}
```
* goodbye 
```bash
  frog goodbye {name}
```

## Contributors
* [Bonny](https://github.com/BonnyCChavarria) 
* [Christina](https://github.com/crb623)
* [Damla](https://github.com/damlaonder)
* [Yura](https://github.com/yurawu27)
