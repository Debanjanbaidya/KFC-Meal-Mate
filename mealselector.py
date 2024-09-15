menu_items = [
    {"name": "Wednesday Bucket", "price": 699.05, "type": "Chicken Buckets", "serves": 3},
    {"name": "5pc Leg Piece Bucket Meal", "price": 628.57, "type": "Chicken Buckets", "serves": 2},
    {"name": "Wednesday Strips Bucket", "price": 350.48, "type": "Chicken Buckets", "serves": 2},
    {"name": "Ultimate Savings Bucket", "price": 828.57, "type": "Chicken Buckets", "serves": 3},
    {"name": "Big 12", "price": 719.05, "type": "Chicken Buckets", "serves": 3},
    {"name": "Chick & Share", "price": 448.57, "type": "Chicken Buckets", "serves": 2},
    
    {"name": "Veg Zinger Burger", "price": 179.05, "type": "Burgers", "serves": 1},
    {"name": "Classic Zinger Burger", "price": 189.52, "type": "Burgers", "serves": 1},
    {"name": "Tandoori Zinger Burger", "price": 199.05, "type": "Burgers", "serves": 1},
    {"name": "Classic Zinger Box", "price": 313.33, "type": "Box Meals", "serves": 1},
    {"name": "Veg Zinger Box", "price": 313.33, "type": "Box Meals", "serves": 1},
    
    {"name": "Medium Popcorn", "price": 164.76, "type": "Snacks", "serves": 1},
    {"name": "Large Fries", "price": 119.05, "type": "Snacks", "serves": 1},
    {"name": "2 pc Hot & Crispy Chicken", "price": 229.52, "type": "Snacks", "serves": 1},
    {"name": "4pc Hot Chicken Wings", "price": 164.76, "type": "Snacks", "serves": 1},
    
    {"name": "Pepsi PET 500 ml", "price": 57.14, "type": "Beverages", "serves": 1}
]

def get_combinations(items, num_people, max_price):
    combinations = []
    for item in items:
        if item['serves'] >= num_people and item['price'] <= max_price:
            combinations.append((item['name'], item['price']))
    return combinations

def find_dynamic_combinations(num_customers, budget, preferences):
    max_price = budget + 120  # Allowing up to ₹120 over the budget
    possible_combinations = []

    # Filter items by type
    chicken_items = [item for item in menu_items if 'Chicken Buckets' in item['type']]
    burger_items = [item for item in menu_items if 'Burgers' in item['type'] or 'Box Meals' in item['type']]
    snack_items = [item for item in menu_items if 'Snacks' in item['type']]
    
    # Handle mixed preferences
    if preferences['Chicken'] > 0 and preferences['Burgers'] > 0:
        for chicken_item in chicken_items:
            for burger_item in burger_items:
                total_price = chicken_item['price'] + burger_item['price']
                total_serves = chicken_item['serves'] + burger_item['serves']
                if total_serves >= num_customers and budget <= total_price <= max_price:
                    possible_combinations.append((f"Mixed Combo: {chicken_item['name']} + {burger_item['name']}", total_price))
    
    # Check combinations for exact preferences
    if preferences['Chicken'] > 0:
        chicken_combos = get_combinations(chicken_items, preferences['Chicken'], max_price)
        for combo in chicken_combos:
            if combo[1] <= max_price:
                possible_combinations.append((f"Chicken Combo: {combo[0]}", combo[1]))
    
    if preferences['Burgers'] > 0:
        burger_combos = get_combinations(burger_items, preferences['Burgers'], max_price)
        for combo in burger_combos:
            if combo[1] <= max_price:
                possible_combinations.append((f"Burger Combo: {combo[0]}", combo[1]))
    
    if preferences['Snacks'] > 0:
        snack_combos = get_combinations(snack_items, preferences['Snacks'], max_price)
        for combo in snack_combos:
            if combo[1] <= max_price:
                possible_combinations.append((f"Snack Combo: {combo[0]}", combo[1]))

    return possible_combinations

def print_combinations(combinations):
    if not combinations:
        print("No valid combinations found within the budget.")
        return
    
    print("Possible Combinations:")
    for i, combo in enumerate(combinations, start=1):
        name, price = combo
        print(f"Combination {i}: {name} - ₹{price:.2f}")

def main():
    # Take user inputs
    try:
        num_customers = int(input("Enter the number of customers: "))
        budget = float(input("Enter the budget: ₹"))
        
        # Collect preferences
        chicken_count = int(input("Enter the number of people preferring chicken: "))
        burger_count = int(input("Enter the number of people preferring burgers: "))
        snack_count = int(input("Enter the number of people preferring snacks: "))
        
        # Define preferences
        preferences = {
            'Chicken': chicken_count,
            'Burgers': burger_count,
            'Snacks': snack_count
        }
        
        # Find and print combinations
        result = find_dynamic_combinations(num_customers, budget, preferences)
        print_combinations(result)
        
    except ValueError:
        print("Invalid input. Please enter numerical values for budget and counts.")

if __name__ == "__main__":
    main()
