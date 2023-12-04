class Shopping:
    def __init__(self,food, pound):
        self.food_name = food
        self.pound = pound
        self.standard_price_per_pound = self.__PriceList()
        self.calculate_cost = self.calculate_total_price()
    def __PriceList(self):
        if self.food_name == "Dry Cured Iberain Ham":
            return 177.80
        elif self.food_name == "Wagyu":
            return 450.00
        elif self.food_name == "Matsutake Mushrooms":
            return 272.00
        elif self.food_name == "Kopi Luwak Coffee":
            return 306.50
        elif self.food_name == "Moose Cheese":
            return 487.20
        elif self.food_name == "White Truffles":
            return 3600.00
        elif self.food_name == "Blue Fin Tuna":
            return 3603.00
        elif self.food_name == "Le Bonnotte Potatoes":
            return 270.81
        else:
            return 0.00
    def calculate_total_price(self):
        return self.standard_price_per_pound * self.pound
    def __str__(self):
        return f'Food: {self.food_name} Amount: {self.pound} Price: {self.calculate_cost}'
    



    