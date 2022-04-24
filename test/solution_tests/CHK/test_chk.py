from tabnanny import check
import py
from lib.solutions.CHK import checkout_solution

def test_bad_imput():
    assert checkout_solution.checkout("1@E") == -1

def test_no_offers():
    assert checkout_solution.checkout("ABCD") == 115

def test_first_A_offer_and_B_offer():
    assert checkout_solution.checkout("AAABBB") == 205

def test_second_A_offer():
    assert checkout_solution.checkout("AAAAA") == 200

def test_both_A_offers():
    assert checkout_solution.checkout("AAAAAAAAAAAAA") == 530

