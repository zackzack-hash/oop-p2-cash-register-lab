class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, value):
        # discount must be an integer between 0-100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        self.total -= self.total * (self.discount / 100)
        print(f"After the discount, the total comes to ${self.total:g}.")
    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no previous transaction to void.")
            return
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])