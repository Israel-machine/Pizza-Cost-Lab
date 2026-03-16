'''Define the variables and default values:'''
small = 8
large = 12

toppings = 1

'''Define the distance variables'''
close_by = 2 
extra_mile = 1 


'''Define input types and prompts'''
user_size = input("What size pizza would you like? large or small?")
user_toppings = int(input("How many toppings would you like on your pie?"))
user_distance = int(input("How many miles away is your delivery address from our shop?"))

'''Use default variables and conditional statements to determine total cost'''
'''to calculate cost based on small pizza with close delivery address'''
if user_size == "small" and user_distance <= 5:
     total_cost = small + (user_toppings * toppings) + close_by
     print(f"Wow! you get the neighbor discount. Your total cost is ${total_cost}")
elif user_size == "small" and user_distance > 5:
     total_cost =  small + (user_toppings * toppings) + (user_distance - 3)
     print(f"your total cost is ${total_cost}")
elif user_size == "large" and user_distance <= 5:
     total_cost =  large + (user_toppings * toppings) + close_by
     print(f"Wow! you get the neighbor discount. your total cost is ${total_cost}")
elif user_size == "large" and user_distance > 5:
     total_cost =  large + (user_toppings * toppings) + (user_distance - 3)
     print(f"your total cost is ${total_cost}")

else:
     print(f"Have a good day!")

     
    

