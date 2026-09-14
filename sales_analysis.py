import csv

with open("data/sales_data.csv", 'r') as file:
  data=list(csv.DictReader(file))
print("Number of records:",len(data))
print("First record:",data[0])

#cal total revenue
total_revenue=0
for row in data:
   total_revenue+=float(row['Revenue'])
print("Total revenue:",total_revenue)

#cal Average Revenue per order
Average_revenue=total_revenue/len(data)
print("Average Revenue per Order :",Average_revenue)

#Highest-Value Order
Highest_revenue=0
for row in data:
  if(float(row['Revenue'])>Highest_revenue):
    Highest_revenue=float(row['Revenue'])
print("Highest order Value:", Highest_revenue)
for row in data:
  if(float(row['Revenue'])==Highest_revenue):
    print("Order:",row["Order_ID"])
    print("Product:",row["Product"])
    print("Revenue:",row["Revenue"])
#Lowest-value Order

lowest_revenue=float(data[0]['Revenue'])
for row in data:
  if(float(row['Revenue'])<lowest_revenue):
    lowest_revenue=float(row['Revenue'])
print("lowest order Value:", lowest_revenue)
for row in data:
  if(float(row['Revenue'])==lowest_revenue):
    print("Order:",row["Order_ID"])
    print("Product:",row["Product"])
    print("Revenue:",row["Revenue"])
#Best-Selling Product
print("Product:Revenue")
product_revenue={}
for row in data:
  product=row["Product"]
  revenue=float(row["Revenue"])
  if product in product_revenue:
    product_revenue[product]+=revenue
  else:
    product_revenue[product]=revenue
print("Revenue by product")
for product,revenue in product_revenue.items():
  print(product,":",revenue)

print("Best Selling Product")
best_product=''
product_highest_revenue=0
for product in product_revenue.keys():
  if(product_revenue[product]>product_highest_revenue):
    product_highest_revenue=product_revenue[product]
    best_product=product
print(best_product,":",product_highest_revenue)

#Best-selling Region
print("Region:Revenue")
region_revenue={}
for row in data:
  Region=row["Region"]
  revenue=float(row["Revenue"])
  if Region in region_revenue:
    region_revenue[Region]+=revenue
  else:
    region_revenue[Region]=revenue
print("Revenue by product")
for Region,revenue in region_revenue.items():
  print(Region,":",revenue)

print("Best Selling Region")
best_Region=''
Region_highest_revenue=0
for Region in region_revenue.keys():
  if(region_revenue[Region]>Region_highest_revenue):
    Region_highest_revenue=region_revenue[Region]
    best_Region=Region
print(best_Region,":",Region_highest_revenue)

# Best-selling Category

print("Category:Revenue")
category_revenue = {}

for row in data:
    category = row["Category"]
    revenue = float(row["Revenue"])

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print("Revenue by Category")
for category, revenue in category_revenue.items():
    print(category, ":", revenue)

print("Best Selling Category")
best_category = ''
category_highest_revenue = 0

for category in category_revenue.keys():
    if category_revenue[category] > category_highest_revenue:
        category_highest_revenue = category_revenue[category]
        best_category = category

print(best_category, ":", category_highest_revenue)
# Best Salesperson

print("Salesperson:Revenue")
salesperson_revenue = {}

for row in data:
    salesperson = row["Salesperson"]
    revenue = float(row["Revenue"])

    if salesperson in salesperson_revenue:
        salesperson_revenue[salesperson] += revenue
    else:
        salesperson_revenue[salesperson] = revenue

print("Revenue by Salesperson")
for salesperson, revenue in salesperson_revenue.items():
    print(salesperson, ":", revenue)

print("Best Salesperson")
best_salesperson = ''
salesperson_highest_revenue = 0

for salesperson in salesperson_revenue.keys():
    if salesperson_revenue[salesperson] > salesperson_highest_revenue:
        salesperson_highest_revenue = salesperson_revenue[salesperson]
        best_salesperson = salesperson

print(best_salesperson, ":", salesperson_highest_revenue)