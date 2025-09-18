### Sandwich Maker Module ###

class SandwichMaker:

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        """Display current resources"""
        for resource, amount in self.machine_resources.items():
            unit = "slice(s)" if resource in ["bread", "ham"] else "ounces"
            print(f"{resource.capitalize()}: {amount} {unit}")