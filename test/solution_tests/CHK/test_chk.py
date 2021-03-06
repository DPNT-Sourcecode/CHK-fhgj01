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

#=================================================================================

def test_1_F():
    assert checkout_solution.checkout("F") == 10

def test_2_F():
    assert checkout_solution.checkout("AAAFF") == 150

def test_3_F():
    assert checkout_solution.checkout("BBFFFEE") == 130

def test_4_F():
    assert checkout_solution.checkout("FFFF") == 30

def test_F_jumble():
    assert checkout_solution.checkout("FFABCDECBAABCABBAAAEEAAFF") == 695

def test_non_offered_SKUs():
    assert checkout_solution.checkout("CDGIJLMOSTWXYZ") == 383

def test_H():
    assert checkout_solution.checkout("HHHHHHHHHHHHHHHH") == 135

def test_K_P_Q():
    assert checkout_solution.checkout("KKPPPPPQQQKPQ") == 580

def test_N_offer():
    assert checkout_solution.checkout("NNNMM") == 135

def test_R_offer():
    assert checkout_solution.checkout("RRRQ") == 150

# def test_complex_R_offer():
#     assert checkout_solution.checkout("RRRQQQ") == 210

def test_4_U():
    assert checkout_solution.checkout("UUUU") == 120

def test_V():
    assert checkout_solution.checkout("VVVVV") == 220

def test_PQRUV_jumble():
    assert checkout_solution.checkout("PPPPQRUVPQRUVPQRUVSU") == 730

def test_group_discount():
    assert checkout_solution.checkout("SSTXYYYZ") == 127

def test_mupltiples_of_K():
    assert checkout_solution.checkout("KKKK") == 240
