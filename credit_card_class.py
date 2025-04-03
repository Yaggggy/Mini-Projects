# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class CreditCard:
    def __init__(self, card_number, cardholder_name, expiration_date, limit, balance=0):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.expiration_date = expiration_date
        self.limit = limit
        self.balance = balance

    def make_payment(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        if amount > self.balance:
            raise ValueError("Payment amount exceeds current balance.")
        self.balance -= amount
        print(f"Payment of ${amount} made successfully. New balance: ${self.balance:.2f}")

    def make_purchase(self, amount):
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")
        if self.balance + amount > self.limit:
            raise ValueError("Purchase exceeds credit limit.")
        self.balance += amount
        print(f"Purchase of ${amount} made successfully. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

    def get_available_credit(self):
        available_credit = self.limit - self.balance
        print(f"Available credit: ${available_credit:.2f}")
        return available_credit

    def apply_interest(self, interest_rate):
        if interest_rate <= 0:
            raise ValueError("Interest rate must be positive.")
        interest_amount = self.balance * (interest_rate / 100)
        self.balance += interest_amount
        print(f"Interest of ${interest_amount:.2f} applied. New balance: ${self.balance:.2f}")

    def is_expired(self, current_date):
        card_month, card_year = map(int, self.expiration_date.split('/'))
        current_month, current_year = map(int, current_date.split('/'))

        if current_year > card_year or (current_year == card_year and current_month > card_month):
            print("Card has expired.")
            return True
        print("Card is valid.")
        return False

    def __str__(self):
        return f"Credit Card Info:\nCardholder: {self.cardholder_name}\nCard Number: {self.card_number}\n" \
               f"Expiration Date: {self.expiration_date}\nCredit Limit: ${self.limit:.2f}\nBalance: ${self.balance:.2f}"


class RewardsCreditCard(CreditCard):
    def __init__(self, card_number, cardholder_name, expiration_date, limit, reward_rate, balance=0):
        super().__init__(card_number, cardholder_name, expiration_date, limit, balance)
        self.reward_rate = reward_rate
        self.rewards_balance = 0

    def make_purchase(self, amount):
        super().make_purchase(amount)
        reward_points = amount * (self.reward_rate / 100)
        self.rewards_balance += reward_points
        print(f"Earned {reward_points:.2f} reward points. Total rewards: {self.rewards_balance:.2f}")

    def redeem_rewards(self, amount):
        if amount > self.rewards_balance:
            raise ValueError("Insufficient reward points.")
        self.rewards_balance -= amount
        self.balance -= amount
        print(f"Redeemed ${amount:.2f} in rewards. New balance: ${self.balance:.2f}")

    def __str__(self):
        return super().__str__() + f"\nReward Rate: {self.reward_rate}%\nRewards Balance: ${self.rewards_balance:.2f}"


class PremiumCreditCard(RewardsCreditCard):
    def __init__(self, card_number, cardholder_name, expiration_date, limit, reward_rate, balance=0, premium_features=None):
        super().__init__(card_number, cardholder_name, expiration_date, limit, reward_rate, balance)
        self.premium_features = premium_features if premium_features else ["Free Lounge Access", "Concierge Service"]

    def show_premium_features(self):
        print("Premium Features:")
        for feature in self.premium_features:
            print(f"- {feature}")

    def __str__(self):
        return super().__str__() + f"\nPremium Features: {', '.join(self.premium_features)}"


def main():
    print("Welcome to the Credit Card Management System")

    # Sample card initialization
    card = PremiumCreditCard("1234567812345678", "John Doe", "12/25", 10000, 2, 2000)

    while True:
        print("\nPlease choose an option:")
        print("1. View Credit Card Info")
        print("2. Make a Purchase")
        print("3. Make a Payment")
        print("4. Check Balance")
        print("5. Check Available Credit")
        print("6. Apply Interest")
        print("7. Redeem Rewards")
        print("8. Show Premium Features")
        print("9. Check if Card is Expired")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                print(card)
            elif choice == 2:
                amount = float(input("Enter the purchase amount: "))
                card.make_purchase(amount)
            elif choice == 3:
                amount = float(input("Enter the payment amount: "))
                card.make_payment(amount)
            elif choice == 4:
                card.check_balance()
            elif choice == 5:
                card.get_available_credit()
            elif choice == 6:
                interest_rate = float(input("Enter the interest rate: "))
                card.apply_interest(interest_rate)
            elif choice == 7:
                amount = float(input("Enter the amount to redeem: "))
                card.redeem_rewards(amount)
            elif choice == 8:
                card.show_premium_features()
            elif choice == 9:
                current_date = input("Enter the current date (MM/YY): ")
                card.is_expired(current_date)
            elif choice == 0:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")



if __name__ == "__main__":
    main()
