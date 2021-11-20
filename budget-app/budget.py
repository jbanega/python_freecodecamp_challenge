class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    

    def deposit(self, amount, description=""):
        assert isinstance(amount, float) or isinstance(amount, int), \
            "The amount to deposit must be a number"
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=""):
        assert isinstance(amount, float) or isinstance(amount, int), \
            "The amount to withdraw must be a number"

        enough_balance = self.check_funds(amount)
        if enough_balance:
            self.ledger.append({"amount": - amount, "description": description})
            return True
        else:
            return False


    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance


    def transfer(self, amount, another_budget_category):
        assert isinstance(amount, float) or isinstance(amount, int), \
            "The amount to transfer must be a number"
        
        enough_balance = self.check_funds(amount)
        if enough_balance:
            self.withdraw(amount, "Transfer to " + another_budget_category.name)
            another_budget_category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False


    def check_funds(self, amount):
        assert isinstance(amount, float) or isinstance(amount, int), \
            "The amount to check must be a number"
        balance = self.get_balance()
        if balance >= amount:
            return True
        else:
            return False


    def __str__(self):
        budget_str = ""

        title_line = self.name.center(30, "*") + "\n"
        budget_str += title_line

        for item in self.ledger:
            budget_str += item["description"][:23].ljust(23) + "{:.2f}".format(item["amount"]).rjust(7) + "\n"
        budget_str += "Total: " + "{:.2f}".format(self.get_balance())
        return budget_str


def create_spend_chart(categories):
    categories_spend_dict = {}
    total_spend = 0
    for category in categories:
        category_spend = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spend += -(item["amount"])
        categories_spend_dict[category.name] = category_spend
        total_spend += category_spend
    
    chart = ""
    title = "Percentage spent by category" + "\n"
    chart += title

    line = ""
    for n in range(100, -10, -10):
        line += str(n).rjust(3) + "|"
        for category, spent in categories_spend_dict.items():
            percentage_spent_by_cat = round((spent / total_spend) * 100)
            if percentage_spent_by_cat >= n:
                line += " o "
            else:
                line += "   "
        line += " \n"
    chart += line

    botton_line = 4*" " + 3*"-"*len(categories_spend_dict.items()) + "-" + "\n"
    chart += botton_line

    cat_char_line = ""
    longest_cat_name = max([cat_name for cat_name, _ in categories_spend_dict.items()], key=len)
    max_n_char = len(longest_cat_name)
    mod_cat_name_list = [cat_name.ljust(max_n_char) for cat_name, _ in categories_spend_dict.items()]
 
    for n in range(max_n_char):
        cat_char_line += 4*" "
        for category in mod_cat_name_list:
            cat_char_line += " " + category[n] + " "
        if n != max_n_char - 1:
            cat_char_line += " \n"
        else:
            cat_char_line += " "
    chart += cat_char_line
    return chart


# Testing
if __name__ == "__main__":

    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print("Balance:", food.get_balance(), "\n")
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55, "withdraw")
    clothing.withdraw(100, "withdraw")
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15, "withdraw")

    print(food, "\n")
    print(clothing, "\n")
    print(auto, "\n")

    print(create_spend_chart([food, clothing, auto]))