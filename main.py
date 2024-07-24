import traceback
from typing import List, Union

from InquirerPy import inquirer

class PurchaseItem:
    def __init__(self, option):
        self.price = option.p
        self.name = str(option)

    def __str__(self):
        return self.name

def get_total_order_amount(order: List[PurchaseItem]) -> float:
    """
    Calculate the total cost of all items in the order.
    """
    return sum(item.price for item in order)

def get_service_charge(order: List[PurchaseItem]) -> float:
    """
    Calculate the service charge based on the total amount of the order.
    For every Rs. 100, the service charge increases by 1% of the order amount,
    up to a maximum of 20% of the order amount.
    """
    total_amount = get_total_order_amount(order)
    service_charge = min((total_amount // 100) * (total_amount * 0.01), total_amount * 0.2)
    return service_charge

class Option:
    def __init__(self, n: str = None, pu: str = None, p: float = None, d: dict = None):
        if d:
            self.n = d.get("name")
            self.p = d.get("price")
        else:
            self.n = n
            self.p = p
        self.pu = pu or "Rs."
        if self.p is None:
            self.p = 0
        if self.n is None:
            raise AttributeError("Name must be provided")
        
    def __str__(self):
        return f"{self.n} {self.pu} {self.p}" if self.p else self.n

# Options for food and beverages
MCDONALDS_FOOD_OPTIONS = [
    Option(d={"name": "Veg Burger", "price": 115.00}),
    Option(d={"name": "Veg Wrap", "price": 130.00}),
    Option(d={"name": "Veg Happy Meal", "price": 215.00}),
    Option(d={"name": "Chicken Burger", "price": 175.00}),
    Option(d={"name": "Chicken Wrap", "price": 195.00}),
    Option(d={"name": "No, that's all", "price": 0.00}),
]

MCDONALDS_BEVERAGES_OPTIONS = [
    Option(d={"name": "Sprite (M)", "price": 115.00}),
    Option(d={"name": "Sprite (L)", "price": 130.00}),
    Option(d={"name": "Mango Smoothie", "price": 215.00}),
    Option(d={"name": "Chocolate Smoothie", "price": 175.00}),
    Option(d={"name": "Chocolate Smoothie w/ Icecream", "price": 195.00}),
    Option(d={"name": "No, that's all", "price": 0.00}),
]

def get_option_from_result(result: str, options: List[Option]) -> Option:
    """
    Retrieve an Option object from the result string.
    """
    for option in options:
        if str(option) == result:
            return option
    raise ValueError("Option not found")

def print_order(order: List[PurchaseItem]):
    """
    Print the final order summary, including total amount, service charge, and final amount.
    """
    print("\nFinal Order")
    for i, item in enumerate(order):
        print(f"{i+1}. {item.name}")

    try:
        total_amount = get_total_order_amount(order)
    except Exception:
        traceback.print_exc()
        total_amount = "ERROR"

    service_charge = "ERROR"
    if total_amount != "ERROR":
        try:
            service_charge = get_service_charge(order)
        except Exception:
            traceback.print_exc()
            service_charge = "ERROR"

    final_amount = (
        total_amount + service_charge 
        if isinstance(total_amount, (int, float)) and isinstance(service_charge, (int, float))
        else 'ERROR'
    )

    print(f"Order Amount: {total_amount}")
    print(f"Service Charge: {service_charge}")
    print(f"Final Amount: {final_amount}")

def main():
    print("\nWelcome to McDonalds on your shell :)")
    print("Here you can place your order")
    print("And then we will show you your bill\n")

    order = []

    while True:
        options = [str(option) for option in MCDONALDS_FOOD_OPTIONS]
        result = inquirer.select(
            message="Add an item",
            choices=options,
            pointer="=>"
        ).execute()

        if result == str(MCDONALDS_FOOD_OPTIONS[-1]):
            break
        option = get_option_from_result(result, MCDONALDS_FOOD_OPTIONS)
        order.append(PurchaseItem(option))
        print(f"{result} is added to your order")

    while True:
        options = [str(option) for option in MCDONALDS_BEVERAGES_OPTIONS]
        result = inquirer.select(
            message="Add a beverage",
            choices=options,
            pointer="=>"
        ).execute()

        if result == str(MCDONALDS_BEVERAGES_OPTIONS[-1]):
            break
        option = get_option_from_result(result, MCDONALDS_BEVERAGES_OPTIONS)
        order.append(PurchaseItem(option))
        print(f"{result} is added to your order")

    print_order(order)

if __name__ == "__main__":
    main()

