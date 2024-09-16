#Assignment: Python Syntax

#3. Arithmetic Operations in Daily Life
#Task 1. Grocery Store Math

bacon = float(7.99)
egg = float(13.99)
milk = float(8.95)

checkout_items = bacon + egg + milk
purchase = float(checkout_items)
state_sales_tax = purchase * .07
total_price = purchase + state_sales_tax 

formatted_number = "%.2f" % total_price


print("Your checkout total is ", formatted_number)


#Task 2. Bank Interest

savings_account_amount = float(13453.00)
APR = .07
APY = savings_account_amount *+ APR
end_of_year_yield = savings_account_amount + APY

formatted_number2 = "%.2f" % end_of_year_yield

print("Your end of the year balance is ", formatted_number2)