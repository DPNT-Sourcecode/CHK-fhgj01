import py
from lib.solutions.CHK import checkout

def test_bad_imput():
    assert checkout("1@E") == -1

def test_no_offers():
    assert checkout("ABCD") == 115

def test_offers():
    assert checkout("AAABBB") == 205