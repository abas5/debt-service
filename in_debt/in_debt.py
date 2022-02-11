import requests
import json


def get_response(url):
    """
    Given a valid url link returns the response in json
    """
    response = requests.get(url)
    if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type', ''):
        return response.json()
    else:
        return 'Invalid Link'


"""
USER_DEBT example:
                [{'amount': 123.46, 'id': 0},
                    {'amount': 100, 'id': 1}]
"""
USER_DEBT = get_response(
    'https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/debts')


"""
USER_PAYMENTS example:
[{'amount': 51.25, 'date': '2020-09-29', 'payment_plan_id': 0},
                          {'amount': 51.25, 'date': '2020-10-29',
                              'payment_plan_id': 0},
                          {'amount': 25, 'date': '2020-08-08', 'payment_plan_id': 1},
                          {'amount': 25, 'date': '2020-08-08', 'payment_plan_id': 1}]
"""
USER_PAYMENTS = get_response(
    'https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payments')

"""
USER_PAYMENT_PLANS example:
                    [{'amount_to_pay': 102.5,
                        'debt_id': 0,
                        'id': 0,
                        'installment_amount': 51.25,
                        'installment_frequency': 'WEEKLY',
                        'start_date': '2020-09-28'}]
"""
USER_PAYMENT_PLANS = get_response(
    'https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payment_plans')


class InDebt:

    def users_in_payment_plans(self, users):
        """
        Given a list of user id return a list of each user debt information.
        """

        users_debt_info = []

        for user_id in users:
            user_debt_info = self.is_in_payment_plan(user_id)
            users_debt_info.append(user_debt_info)

        return users_debt_info

    def is_in_payment_plan(self, user_id):
        """
        Checks whether the given user_id is in a payment plan or not.
        Then returns the user_debt json object with "is_in_payment_plan".
        """

        amount_owed = self.get_amount_owed(user_id)
        if amount_owed == 0:
            return self.user_debt_with_variation(user_id, amount_owed, is_in_payment_plan=False)
        else:
            amount_to_pay = self.get_amount_to_pay(user_id)
            # check payment plans and see how much they paid
            total_amount_in_payments = self.total_amount_in_payments(user_id)
            amount_owed = amount_to_pay - total_amount_in_payments

            if amount_owed == 0:
                return self.user_debt_with_variation(user_id, amount_owed, is_in_payment_plan=False)
            else:
                return self.user_debt_with_variation(user_id, amount_owed, is_in_payment_plan=True)

    def get_amount_to_pay(self, user_id):
        """
        Gets the value for "amount_to_pay" from user_payments_plans object
        """

        amount_to_pay = 0

        for user in USER_PAYMENT_PLANS:
            if user.get('id') == user_id:
                amount_to_pay = user.get('amount_to_pay')
                return amount_to_pay

        return amount_to_pay

    def get_amount_owed(self, user_id):
        """
        Given the user_id, returns the amount the user
        owes.
        """

        for user in USER_DEBT:
            if user.get('id') == user_id:
                return user.get('amount')

    def user_debt_with_variation(self, user_id, amount, is_in_payment_plan=is_in_payment_plan):
        """
        Returns the user_object with the addition of "is_in_payment_plan"
        field. Also makes a change "amount" field depending on how much 
        the user has paid in payments. 
        """
        user_debt = {
            'id': user_id,
            'amount': amount,
            'is_in_payment_plan': is_in_payment_plan
        }

        return json.dumps(user_debt)

    def total_amount_in_payments(self, user_id):
        """
        Iter thru the payment_plans object. Calcaulte the total
        amount the user_id has paid in total.
        """
        total_amount_in_payments = 0

        for user in USER_PAYMENTS:
            if user_id == user.get('payment_plan_id'):
                total_amount_in_payments += user.get('amount')

        return total_amount_in_payments

if __name__ == '__main__':
    users = [0, 1, 2, 3, 4, 5]
    user_one_info = InDebt().is_in_payment_plan(1)
    print("USER 1:")
    print(user_one_info)

    users_info = InDebt().users_in_payment_plans(users)
    print("USERS:")
    print(users_info)
