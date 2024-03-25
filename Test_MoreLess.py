import pytest

def user_entry(input):
    return 30 <= input <= 100

def test_valide_input():
    assert user_entry(50) == True

def test_invalide_input():
    assert user_entry(20) == False

pytest.main()