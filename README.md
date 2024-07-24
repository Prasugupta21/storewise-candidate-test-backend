## Storewise Backend Challenge
### Overview
This repository contains the backend code for the Storewise candidate test. The backend application is designed to handle orders for a McDonald's shell application, calculating the total order amount and service charge. It uses Python and the InquirerPy library for the command-line interface.

### Setup Instructions
- Ensure that you have [python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed in your machine
- Clone this repository
- `cd` into the new directory (that you cloned)
- `pip install InquirerPy`
- `python main.py`

### Code Explanation

**Main Components**
**PurchaseItem**: Represents an item in the order, with attributes for price and name.
**Option**: Represents a food or beverage option available for order.
**get_total_order_amount**: Calculates the total cost of all ordered items.
**get_service_charge**: Computes the service charge based on the total order amount.
**print_order**: Displays the final order, including total amount, service charge, and final amount.

### CLI Library
The application uses InquirerPy for interactive command-line prompts due to compatibility issues with the bullet library on Windows.

### Example Usage
Add Items to Order: Follow prompts to add items from the menu.
View Final Order: The application will display the total amount, service charge, and final amount.


### Success


https://github.com/user-attachments/assets/ba78b83c-b15d-4fd7-a7f8-1f32c7b3b5a6




