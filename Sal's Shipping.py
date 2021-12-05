weight = float(input("What's the weight of your package?"))
sales_tax = .08
# Ground Shipping
if weight <= 2:
    cost_ground = (1.5 * weight + 20)
elif weight <= 6:
    cost_ground = (3 * weight + 20)
elif weight <= 10:
    cost_ground = (4 * weight + 20)
else:
    cost_ground = (4.75 * weight + 20)

cost_ground_tax = cost_ground * sales_tax
cost_ground_total = cost_ground + cost_ground_tax
print("Price for Ground: $" + str(format(cost_ground_total, '.2f')))

# Premium Ground Shipping
cost_ground_premium = 125
cost_ground_premium_tax = cost_ground_premium * sales_tax
cost_ground_premium_total = cost_ground_premium + cost_ground_premium_tax
print("Price for Ground Premium: $" + str(format(cost_ground_premium_total, '.2f')))

# Drone Shipping
if weight <= 2:
    cost_drone = 4.5 * weight
elif weight <= 6:
    cost_drone = 9 * weight
elif weight <= 10:
    cost_drone = 12 * weight
else:
    cost_drone = 14.25 * weight

cost_drone_tax = cost_drone * sales_tax
cost_drone_total = cost_drone + cost_drone_tax
print("Price for Drone Shipping $" + str(format(cost_drone_total, '.2f')))
