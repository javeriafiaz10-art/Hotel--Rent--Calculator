#Hostal room rent calculator and divide in persons
#Take input From the user
 
    
rent = int(input("Enter your Hostel Room Rent = "))
food = int(input("Enter the amount of food Ordered = "))
electricity_units = int(input("Enter the total of electricity units"))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the no of Persons living in room = "))

total_bill = electricity_units * charge_per_unit

output = (rent + food + total_bill) // persons

print("Each person will pay", output)