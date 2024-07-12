import pytest

from bank_account import BankAccount


@pytest.mark.parametrize(
    "initial_amount, deposit_amount, expected_balance",
    [
        (0, 1000, 1000),
        (1000, 1500, 2500),
        (999999, 1, 1000000)
    ]
)
def test_deposit(initial_amount, deposit_amount, expected_balance):
    amount = BankAccount(initial_amount)
    assert amount.deposit(deposit_amount) == expected_balance, "残高計算が正しくありません。"
