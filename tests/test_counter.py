from lib.counter import *

def test_counter_is_initially_set_to_zero():
    counter = Counter()
    report = counter.report()
    assert report == "Counter to 0 so far."

def test_counter_can_add_a_number():
    counter = Counter()
    counter.add(3)
    report = counter.report()
    assert report == "Counter to 3 so far."

def test_counter_can_add_multiple_numbers():
    counter = Counter()
    counter.add(3)
    counter.add(5)
    report = counter.report()
    assert report == "Counter to 8 so far."
