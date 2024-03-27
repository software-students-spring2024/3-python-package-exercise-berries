
import pytest
from ribbet.ribbet import hello, encourage, frogmode, feed, kill, goodbye
# hello
def test_hello(capsys):
    hello("Alice")
    captured = capsys.readouterr()
    assert "\U0001F438: Hi there Alice!" in captured.out

# encourage  
def test_encourage(capsys):
    encourage()
    captured = capsys.readouterr()
    assert "\U0001F438:" in captured.out

@pytest.mark.parametrize("seed", [1, 2, 3])
def test_encourage_variants(capsys, monkeypatch, seed):
    def mock_randint(a, b):
        return seed
    monkeypatch.setattr("random.randint", mock_randint)
    encourage()
    captured = capsys.readouterr()
    if seed == 1:
        assert "\U0001F438: You are the smartest frog in the pond!" in captured.out
    elif seed == 2:
        assert "\U0001F438: You got this! Leap by leap!" in captured.out
    else:  # seed == 3
        assert "\U0001F438: You are amazing!" in captured.out

# frogmode     
def test_frogmode(capsys):
    frogmode()
    captured = capsys.readouterr()
    assert "\U0001F438: I EAT BUGS, let's eat bugs together" in captured.out

# feed  
def test_feed(capsys):
    feed("flies")
    captured = capsys.readouterr()
    assert "\U0001F438: Thanks for the sweet little treat! Flies is yummy! nom nom nom" in captured.out

# kill  
def test_kill(capsys):
    kill("the bad vibes")
    captured = capsys.readouterr()
    assert "\U0001F438:" in captured.out

@pytest.mark.parametrize("seed,expected", [
    (1, "I killed the bad vibes for you! You are safe now!"),
    (2, "I don't like the bad vibes, I only eat yummy snacks! nom nom nom")
])
def test_kill_variants(capsys, monkeypatch, seed, expected):
    def mock_randint(a, b):
        return seed
    monkeypatch.setattr("random.randint", mock_randint)
    kill("the bad vibes")
    captured = capsys.readouterr()
    assert "\U0001F438: " + expected in captured.out

# goodbye
def test_goodbye(capsys):
    goodbye("Alice")
    captured = capsys.readouterr()
    assert "\U0001F438: Bye bye Alice, go catch some flies for me!" in captured.out


"""
# help
def test_help(capsys):
    help()
    captured = capsys.readouterr()
    assert "hello(your name): the frog says hello to you ;)" in captured.out
    assert "encourage(): the frog gives you a silly little pep talk <3" in captured.out
    assert "frogmode(): the frogs gets into frog mode and eats bugs with you!" in captured.out
    assert "feed(snack): feed the frog a yummy snack!" in captured.out
    assert "kill(anything): the fighter frog kills anything for you!" in captured.out
    assert "goodbye(your name): frog says goodbye to you!" in captured.out
"""


