### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount_needed in ingredients.items():
            if self.machine_resources[ingredient] < amount_needed:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        
        total = (large_dollars * 1.0) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            else:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        """Display current resources"""
        for resource, amount in self.machine_resources.items():
            unit = "slice(s)" if resource in ["bread", "ham"] else "pound(s)"
            print(f"{resource.capitalize()}: {amount} {unit}")

### Make an instance of SandwichMachine class and write the rest of the codes ###

# Create an instance of the SandwichMachine
sandwich_machine = SandwichMachine(resources)

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
            payment = sandwich_machine.process_coins()
            
            # Check if payment is sufficient
            if sandwich_machine.transaction_result(payment, sandwich_cost):
                # Make the sandwich
                sandwich_machine.make_sandwich(choice, order_ingredients)
    else:
        print("Invalid selection. Please choose small, medium, large, off, or report.")
