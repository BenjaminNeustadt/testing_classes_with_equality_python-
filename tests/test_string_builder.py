from lib.string_builder import *

def test_string_builder_can_add_and_returns_hello():
    string_builder = StringBuilder()
    string_builder.add("hello")
    result = string_builder.output()
    assert result == "hello"


def test_string_builder_can_add_and_returns_hello_annexing_1():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" again")
    result = string_builder.output()
    assert result == "Hello again"

def test_string_builder_can_add_and_returns_hello_annexing_2():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" again")
    string_builder.add(", and again.")
    result = string_builder.output()
    assert result == "Hello again, and again."

def test_string_builder_and_returns_string_length():
    string_builder = StringBuilder()
    string_builder.add("Length please?")
    output_result = string_builder.output()
    length_result = string_builder.size()
    assert output_result == "Length please?"
    assert length_result == 14
