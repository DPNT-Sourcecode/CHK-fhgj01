import py
from lib.solutions.CHK import checkout_solution

def test_bad_imput():
    assert checkout_solution.checkout("1@E") == -1

def test_no_offers():
    assert checkout_solution.checkout("ABCD") == 115

def test_offers():
    assert checkout_solution.checkout("AAABBB") == 205