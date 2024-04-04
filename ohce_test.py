import pytest
import ohce
from datetime import time

def test_reverseWord():
    assert ohce.reverseWord("abcd") == "dcba"
    assert ohce.reverseWord("lula") == "alul"
    assert ohce.reverseWord("123") == "321"
    assert ohce.reverseWord("ubereats") == "staerebu"

def test_is_palindrome():
    assert ohce.isPalindrome("owo", "owo") == "¡Bonita palabra!"
    assert ohce.isPalindrome("hooh", "hooh") == "¡Bonita palabra!"
    assert ohce.isPalindrome("ala", "ala") == "¡Bonita palabra!"
    assert ohce.isPalindrome("racecar", "racecar") == "¡Bonita palabra!"

def test_isnt_palindrome():
    assert ohce.reverseWord("abcd") == "dcba"
    assert ohce.reverseWord("lula") == "alul"
    assert ohce.reverseWord("123") == "321"
    assert ohce.reverseWord("ubereats") == "staerebu"

def test_greet_morning():
    name = "Lula"
    assert ohce.greet(name, time(10,10)) == f"¡Buenos días {name}!"
    assert ohce.greet(name, time(6,30)) == f"¡Buenos días {name}!"
    assert ohce.greet(name, time(11,59)) == f"¡Buenos días {name}!"
    assert ohce.greet(name, time(6,0)) == f"¡Buenos días {name}!"

def test_greet_afternoon():
    name = "Lula"
    assert ohce.greet(name, time(13,10)) == f"¡Buenas tardes {name}!"
    assert ohce.greet(name, time(15,30)) == f"¡Buenas tardes {name}!"
    assert ohce.greet(name, time(12,1)) == f"¡Buenas tardes {name}!"
    assert ohce.greet(name, time(19,59)) == f"¡Buenas tardes {name}!"

def test_greet_night():
    name = "Lula"
    assert ohce.greet(name, time(20,0)) == f"¡Buenas noches {name}!"
    assert ohce.greet(name, time(21,57)) == f"¡Buenas noches {name}!"
    assert ohce.greet(name, time(4,10)) == f"¡Buenas noches {name}!"
    assert ohce.greet(name, time(5,0)) == f"¡Buenas noches {name}!"

def test_stop():
    name = "Lula"
    assert ohce.stop(name) == f"Adios {name}"



