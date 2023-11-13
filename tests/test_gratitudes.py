from lib.gratitudes import *

def test_gratitudes_returns_1_gratitude():
    gratitude = Gratitudes()
    gratitude.add("being alive")
    result = gratitude.format()
    assert result == "Be grateful for: being alive"

def test_gratitudes_returns_2_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("being alive")
    gratitude.add("being healthy")
    result = gratitude.format()
    assert result == "Be grateful for: being alive, being healthy"

def test_gratitudes_returns_3_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("being alive")
    gratitude.add("being healthy")
    gratitude.add("and doing something you enjoy")
    result = gratitude.format()
    assert result == "Be grateful for: being alive, being healthy, and doing something you enjoy"
