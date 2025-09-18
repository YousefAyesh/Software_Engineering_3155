### Main Module - Entry Point ###

import data_module
import sandwich_maker_module
import cashier_module

# Create variables based on data dictionaries
recipes = data_module.recipes
resources = data_module.resources

# Create instances from each class
sandwich_machine = sandwich_maker_module.SandwichMaker(resources)
cash_register = cashier_module.Cashier()

# Main program loop
is_on = True

while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        sandwich_machine.report()
    elif choice in ["small", "medium", "large"]:
        # Get the recipe for the chosen sandwich
        sandwich_recipe = recipes[choice]
        order_ingredients = sandwich_recipe["ingredients"]
        sandwich_cost = sandwich_recipe["cost"]
        
        # Check if there are sufficient resources
        if sandwich_machine.check_resources(order_ingredients):
            # Process payment
            payment = cash_register.process_coins()
            
            # Check if payment is sufficient
            if cash_register.transaction_result(payment, sandwich_cost):
                # Make the sandwich
                sandwich_machine.make_sandwich(choice, order_ingredients)
    else:
        print("Invalid selection. Please choose small, medium, large, off, or report.")