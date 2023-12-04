from ProgramExerciseSJ import Shopping

def create_food_order_list():
    food_list = []
    num_items = int(input("Enter the number of items to purchase: "))
    while num_items < 1:
        print("Please enter a number greater than or equal to 1.")
        num_items = int(input("Enter the number of items to purchase: "))

    for _ in range(num_items):
        food_name = input("Enter the name of the food: ")
        amount = float(input("Enter the amount of the food in pounds: "))
        while amount <= 0:
            print("Please enter a positive value for the amount.")
            amount = float(input("Enter the amount of the food in pounds: "))

        food_order = Shopping(food_name, amount)
        food_list.append(food_order)

    return food_list


def display_order_list(food_orders):
    for order in food_orders:
        print(order)


def calculate_total_cost(food_orders):
    total_cost = 0.0
    for order in food_orders:
        total_cost += order.calculate_total_price()
    return total_cost


def main():
    orders = create_food_order_list()
    display_order_list(orders)
    total_cost = calculate_total_cost(orders)
    print(f"\nTotal Cost of All Items: ${total_cost:.2f}")


main()

            






