
#Cost for each item (float)
flowerpot_price = 4.00
flower_seeds_price = 1.00
soil_price = 5.00

# Tax rate is 6% (float)
tax_rate = 0.06

#Ask the user how many of each item they want (integer)
flowerpot = int(input('How many flowerpots? '))
flower_seeds = int(input('How many packs of flower seeds? '))
soil  = int(input('How many bags of soil? '))

#Calculate the total cost for each item using multiplication (float)
total_flowerpot_cost = flowerpot * flowerpot_price
total_flower_seeds_cost = flower_seeds * flower_seeds_price
total_soil_cost = soil * soil_price

#Calculate the total cost of all items combined using addition (float)
total_cost_of_items = total_flowerpot_cost + total_flower_seeds_cost + total_soil_cost

#Calculate the total cost with sales tax (float)
total_cost = (total_cost_of_items * tax_rate) + total_cost_of_items

print("--------- Receipt ---------")
print(f"{flowerpot} flowerpots: ${total_flowerpot_cost}")
print(f"{flower_seeds} flower seeds (pack): ${total_flower_seeds_cost}")
print(f"{soil} soil (bag): ${total_soil_cost}")
print(f"Total: ${total_cost_of_items}")
print(f"Total (with tax): ${total_cost}")
