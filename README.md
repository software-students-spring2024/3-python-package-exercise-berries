![Workflow Status](https://github.com/software-students-spring2024/3-python-package-exercise-berries/actions/workflows/run-tests.yml/badge.svg)
# 🐸 FrogPy: Python Package

We are building a frog 🐸 named Ribbet, a virtual pet that has multiple behaviors that can be called upon each with their own unique message/response. 

NOTE: This is a python packaged that can be installed and utilized in your terminal. This is not a python package that can be imported into a python file.   

The unique responses will be: 
* **-h/--help**: List of commands 
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

Install the ribbet module using pip

```bash
  pip install ribbet 
```


## Usage
Call ribbet from the command line to interact with your virtual frog while coding.

To access menu with all functions: 
```bash
  ribbet
```
Functions: 
* hello
```bash
  ribbet hello {name}
```
* encourage
```bash
  ribbet encourage
```
* frogmode
```bash
  ribbet frogmode
```
* feed
```bash
  ribbet feed {snack}
```
* kill
```bash
  ribbet kill {anything}
```
* goodbye 
```bash
  ribbet goodbye {name}
```

## Command Examples

* hello
```bash
Your-MacBook-Pro:Documents username$ ribbet hello Name
🐸: Hi there Name!
```
* encourage
```bash
Your-MacBook-Pro:Documents username$ ribbet encourage
🐸: You are amazing!
```
* frogmode
```bash
Your-MacBook-Pro:Documents username$ ribbet frogmode
🐸: I EAT BUGS, let's eat bugs together
```
* feed
```bash
Your-MacBook-Pro:Documents username$ ribbet feed worm
🐸: Thanks for the sweet little treat! Worm is yummy! nom nom nom
```
* kill
```bash
Your-MacBook-Pro:Documents username$ ribbet kill bugs
🐸: I don't like bugs, I only eat yummy snacks! nom nom nom
```
* goodbye 
```bash
Your-MacBook-Pro:Documents username$ ribbet goodbye Name
🐸: Bye bye Name, go catch some flies for me!
```

## How to Contribute to ribbet
1. **Clone the repository:**
```bash
git clone https://github.com/software-students-spring2024/3-python-package-exercise-berries.git
```

2. **Create a virtual environment:**
```bash
python -m venv env
source env/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requires.txt
```
### Make Changes & Testing
* Add your changes in a new branch
* Make sure all changes are passing by running:
```bash
pytest
```

### Submit Your Contribution
* Contribute your changes via pull requests

## PyPI Website
[ribbet 0.1.2](https://pypi.org/project/ribbet/0.1.2/)

## Contributors
* [Bonny](https://github.com/BonnyCChavarria) 
* [Christina](https://github.com/crb623)
* [Damla](https://github.com/damlaonder)
* [Yura](https://github.com/yurawu27)
