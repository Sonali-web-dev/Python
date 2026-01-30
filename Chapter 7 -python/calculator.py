#Product price calculator
#input("Enter a original price:")
original_price = float(input("Enter a original price:"))
#input("Enter discount %:")
discount_percent= float(input("Enter a discount %:"))
discount_amount = (discount_percent/100*original_price)
final_price = original_price - discount_amount
print(f'Final price after {discount_percent} % discount: {final_price}')