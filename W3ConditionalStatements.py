def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - (discount_percent / 100))
        return discounted_price
    else:
        return price
    

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)
if final_price == original_price:
    print("No discount applied. Final price:", final_price)
else:
    print("Final price after discount:", final_price)
    



    



