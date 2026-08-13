hours = int(input("Enter parking hours: "))

if hours <= 2:
    charge = hours * 30
elif hours <= 5:
    charge = hours * 25
else:
    charge = hours * 20

if charge > 150:
    service = 20
else:
    service = 0

final_amount = charge + service

print("Parking Charge: ₹", charge)
print("Service Charge: ₹", service)
print("Final Amount: ₹", final_amount)