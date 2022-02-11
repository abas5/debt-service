import unittest
from in_debt.in_debt import InDebt
from in_debt.in_debt import get_response


class InDebtTest(unittest.TestCase):

    mock_user_debt = [{'amount': 123.46, 'id': 0},
                      {'amount': 100, 'id': 1},
                      {'amount': 4920.34, 'id': 2},
                      {'amount': 12938, 'id': 3},
                      {'amount': 9238.02, 'id': 4}]

    def test_get_response(self):
        valid_url = 'https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/debts'
        results = get_response(valid_url)

        self.assertListEqual(results, self.mock_user_debt)

    def test_users_in_payment_plans(self):
        user_ids = [0, 1, 2]
        results = InDebt().users_in_payment_plans(user_ids)
        expected = ['{"id": 0, "amount": 0.0, "is_in_payment_plan": false}',
                    '{"id": 1, "amount": 50, "is_in_payment_plan": true}',
                    '{"id": 2, "amount": 607.6700000000001, "is_in_payment_plan": true}']

        self.assertListEqual(results, expected)

    def test_is_in_payment_plan(self):
        user_id = 2
        results = InDebt().is_in_payment_plan(user_id)
        expected = '{"id": 2, "amount": 607.6700000000001, "is_in_payment_plan": true}'

        self.assertEqual(results, expected)

    def test_get_amount_to_pay(self):
        user_id = 2
        results = InDebt().get_amount_to_pay(user_id)
        expected = 4920.34

        # Check if the results and expected is equal
        self.assertEqual(results, expected)

    def test_get_amount_owed(self):
        """
        Tests the InDebt.get_amount_owed function
        """
        user_id = 1
        results = InDebt().get_amount_owed(user_id)
        expected = 100

        self.assertEqual(results, expected)

    def test_total_amount_in_payments(self):
        """
        Tests the InDebt.total_amount_in_payments function
        """
        user_id = 0
        results = InDebt().total_amount_in_payments(user_id)
        expected = 102.50

        self.assertEqual(results, expected)

    def test_user_debt_with_variation(self):
        """
        Tests the InDebt.user_debt_with_variation function
        """
        user_id = 1
        amount = 100
        is_in_payment_plan = True

        expected = '{"id": 1, "amount": 100, "is_in_payment_plan": true}'

        results = InDebt().user_debt_with_variation(user_id, amount, is_in_payment_plan)
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
