import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest, check_loan_eligibility

@pytest.mark.parametrize("balance, amount, expected", [
    (1000, 500, 1500),
    (0, 100, 100)
])
def test_deposit_positive(balance, amount, expected):
    assert deposit(balance, amount) == expected

@pytest.mark.parametrize("balance, amount", [
    (1000, 0),
    (1000, -100)
])
def test_deposit_invalid(balance, amount):
    with pytest.raises(ValueError):
        deposit(balance, amount)

def test_withdraw_success():
    assert withdraw(1000, 300) == 700

def test_withdraw_more_than_balance():
    with pytest.raises(ValueError):
        withdraw(500, 1000)

def test_transfer_success():
    from_bal, to_bal = transfer(1000, 500, 300)
    assert from_bal == 700
    assert to_bal == 800


def test_transfer_failure():
    with pytest.raises(ValueError):
        transfer(200, 500, 400)

def test_calculate_interest():
    result = calculate_interest(1000, 10, 2)
    assert round(result, 2) == 1210.00
    
@pytest.mark.parametrize("balance, credit_score, expected", [
    (6000, 750, True),
    (4000, 750, False),
    (6000, 650, False)
])
def test_loan_eligibility(balance, credit_score, expected):
    assert check_loan_eligibility(balance, credit_score) == expected
