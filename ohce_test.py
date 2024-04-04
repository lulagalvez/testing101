import pytest
import ohce
import datetime

def test_reverseWord():
    assert ohce.reverseWord("abcd") == "dcba"
    assert ohce.reverseWord("lula") == "alul"
    assert ohce.reverseWord("123") == "321"
    assert ohce.reverseWord("ubereats") == "staerebu"



