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

def test_E():
    assert checkout_solution.checkout("EE") == 80

def test_all_of_one_type():
    assert checkout_solution.checkout("ABCDE") == 155

def test_one_E_discount():
    assert checkout_solution.checkout("EEB") == 80

def test_two_E_discounts():
    assert checkout_solution.checkout("EEEEBB") == 160

# these tests below favour the supermarket, hence not in accordance with the brief

def test_E_discount_1():
    assert checkout_solution.checkout("ABCDEABCDE") == 280

def test_E_discount_2():
    assert checkout_solution.checkout("CCADDEEBBA") == 280


