class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        
        cost = price * quantity
        self.total += cost
        self.previous_transactions.append(cost)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total) if self.total.is_integer() else self.total}.")

    def void_last_transaction(self):
        if self.previous_transactions:
            last_cost = self.previous_transactions.pop()
            self.total -= last_cost