KFC MealMate
Imagine you're at a fast-food chain with friends, each craving different things—one wants chicken, another prefers a burger, and someone is sticking to snacks. But you have a fixed budget. My project, 'MealMate,' acts like a smart personal assistant, suggesting perfect meal combinations that satisfy everyone's tastes while staying within the budget. It even offers flexibility, suggesting a bit over the budget if needed, ensuring you don't miss out on that ideal combo
Menu Representation: The menu items are stored in a list of dictionaries, where each dictionary represents an item with attributes like name, price, type, and serves. This structure allows for easy access and manipulation of menu data.
Function Definitions:

get_combinations(items, num_people, max_price): This function filters and returns meal combinations that serve at least num_people and are within the max_price. It is used to identify valid options based on the constraints of serving size and price.
find_dynamic_combinations(num_customers, budget, preferences): This is the core function that computes meal combinations based on the number of customers, budget, and specific food preferences. It divides the menu into categories (Chicken Buckets, Burgers/Box Meals, Snacks) and then checks for valid combinations that meet the preferences and budget constraints.
print_combinations(combinations): This function formats and prints the list of valid meal combinations in a user-friendly manner. It provides a clear and concise output for the user to review.
Budget Flexibility:

The system allows for a budget range extending up to ₹120 above the specified budget. This feature is implemented by adjusting the max_price variable in the find_dynamic_combinations function.
Preferences Handling:

Mixed Preferences: The system can handle mixed preferences by iterating through different categories (Chicken Buckets, Burgers, Snacks) and combining them to meet the overall needs of the group.
Exact Preferences: It specifically checks if the preferences for chicken, burgers, or snacks can be satisfied within the given budget.
User Input:

Interactive Input: The main() function prompts the user for input regarding the number of customers, budget, and preferences. It then processes this input to generate and display meal suggestions.
Error Handling: Basic error handling is implemented to manage invalid inputs, ensuring that the user provides numerical values for budget and counts.
Algorithm Efficiency:

The algorithm uses nested loops to combine items from different categories, which can become computationally intensive as the number of items increases. For larger menus or more complex scenarios, optimizations or alternative approaches like dynamic programming could be considered.
Extensibility:

Menu Updates: The system can be easily extended by adding more items to the menu_items list or adjusting the parameters for different scenarios.
Additional Features: Further functionalities, such as prioritizing certain types of items or integrating with external APIs for real-time pricing, can be incorporated to enhance the system's capabilities.
