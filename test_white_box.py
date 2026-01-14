import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

def test_deposit_error_branch():
    with pytest.raises(ValueError):
        deposit(1000, -50)

def test_withdraw_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -100)

def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(300, 500)

def test_transfer_success_path():
    from_bal, to_bal = transfer(1000, 200, 400)
    assert from_bal == 600
    assert to_bal == 600

def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -10)

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(100, 300, 200)

def test_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 10, 2)

def test_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)

def test_interest_valid_path():
    result = calculate_interest(2000, 5, 1)
    assert round(result, 2) == 2100.00
