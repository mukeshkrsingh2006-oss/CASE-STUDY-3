# Smart Payment Processing System using OOP in Python 
# MUKESH KUMAR
# 202501100700200

from abc import ABC, abstractmethod

# 🔹 Abstract Base Class
class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self, original_amount, final_amount):
        print("\n----- PAYMENT RECEIPT -----")
        print(f"User Name        : {self.user_name}")
        print(f"Original Amount  : ₹{original_amount}")
        print(f"Final Amount     : ₹{final_amount}")
        print("----------------------------\n")


# 🔹 Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        gateway_fee = amount * 0.02
        gst = gateway_fee * 0.18
        final_amount = amount + gateway_fee + gst

        print("Payment Method: Credit Card")
        print(f"Gateway Fee: ₹{gateway_fee}")
        print(f"GST on Fee: ₹{gst}")

        self.generate_receipt(amount, final_amount)


# 🔹 UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        cashback = 0

        if amount > 1000:
            cashback = 50
            print("Cashback Applied: ₹50")
        else:
            print("No Cashback")

        final_amount = amount - cashback

        print("Payment Method: UPI")
        self.generate_receipt(amount, final_amount)


# 🔹 PayPal Payment
class PayPalPayment(Payment):
    def pay(self, amount):
        international_fee = amount * 0.03
        conversion_fee = 20

        final_amount = amount + international_fee + conversion_fee

        print("Payment Method: PayPal")
        print(f"International Fee: ₹{international_fee}")
        print(f"Conversion Fee: ₹{conversion_fee}")

        self.generate_receipt(amount, final_amount)


# 🔹 Wallet Payment
class WalletPayment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        print("Payment Method: Wallet")

        if amount > self.balance:
            print("Transaction Failed: Insufficient Balance\n")
        else:
            self.balance -= amount
            print(f"Remaining Balance: ₹{self.balance}")
            self.generate_receipt(amount, amount)


# 🔹 Function for Runtime Polymorphism
def process_payment(payment, amount):
    payment.pay(amount)


# 🔹 Main Program (Testing)
if __name__ == "__main__":
    # Creating objects
    p1 = CreditCardPayment("Mukesh")
    p2 = UPIPayment("Rahul")
    p3 = PayPalPayment("Amit")
    p4 = WalletPayment("Neha", 500)

    # Processing payments
    process_payment(p1, 1000)
    process_payment(p2, 1200)
    process_payment(p3, 2000)
    process_payment(p4, 600)   # Should fail
    process_payment(p4, 300)   # Should succeed