import csv
import datetime


# ============================================================
# LOAD DATA
# ============================================================

with open("data/sales_data.csv", "r") as file:
    data = list(csv.DictReader(file))

print("Number of records:", len(data))
print("First record:", data[0])


# ============================================================
# TOTAL REVENUE
# ============================================================

total_revenue = 0

for row in data:
    total_revenue += float(row["Revenue"])

print("\nTotal Revenue:", total_revenue)


# ============================================================
# AVERAGE REVENUE PER ORDER
# ============================================================

average_revenue = total_revenue / len(data)

print("Average Revenue per Order:", average_revenue)


# ============================================================
# HIGHEST-VALUE ORDER
# ============================================================

highest_revenue = 0

for row in data:
    revenue = float(row["Revenue"])

    if revenue > highest_revenue:
        highest_revenue = revenue

print("\nHighest Order Value:", highest_revenue)

for row in data:
    if float(row["Revenue"]) == highest_revenue:
        print("Order:", row["Order_ID"])
        print("Product:", row["Product"])
        print("Revenue:", row["Revenue"])


# ============================================================
# LOWEST-VALUE ORDER
# ============================================================

lowest_revenue = float(data[0]["Revenue"])

for row in data:
    revenue = float(row["Revenue"])

    if revenue < lowest_revenue:
        lowest_revenue = revenue

print("\nLowest Order Value:", lowest_revenue)

for row in data:
    if float(row["Revenue"]) == lowest_revenue:
        print("Order:", row["Order_ID"])
        print("Product:", row["Product"])
        print("Revenue:", row["Revenue"])


# ============================================================
# BEST-SELLING PRODUCT BY REVENUE
# ============================================================

product_revenue = {}

for row in data:

    product = row["Product"]
    revenue = float(row["Revenue"])

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue


print("\nREVENUE BY PRODUCT")

for product, revenue in product_revenue.items():
    print(product, ":", revenue)


best_product = ""
product_highest_revenue = 0

for product, revenue in product_revenue.items():

    if revenue > product_highest_revenue:
        product_highest_revenue = revenue
        best_product = product


print("\nBEST-SELLING PRODUCT")
print(best_product, ":", product_highest_revenue)


# ============================================================
# BEST-SELLING REGION BY REVENUE
# ============================================================

region_revenue = {}

for row in data:

    region = row["Region"]
    revenue = float(row["Revenue"])

    if region in region_revenue:
        region_revenue[region] += revenue
    else:
        region_revenue[region] = revenue


print("\nREVENUE BY REGION")

for region, revenue in region_revenue.items():
    print(region, ":", revenue)


best_region = ""
region_highest_revenue = 0

for region, revenue in region_revenue.items():

    if revenue > region_highest_revenue:
        region_highest_revenue = revenue
        best_region = region


print("\nBEST-SELLING REGION")
print(best_region, ":", region_highest_revenue)


# ============================================================
# BEST-SELLING CATEGORY BY REVENUE
# ============================================================

category_revenue = {}

for row in data:

    category = row["Category"]
    revenue = float(row["Revenue"])

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue


print("\nREVENUE BY CATEGORY")

for category, revenue in category_revenue.items():
    print(category, ":", revenue)


best_category = ""
category_highest_revenue = 0

for category, revenue in category_revenue.items():

    if revenue > category_highest_revenue:
        category_highest_revenue = revenue
        best_category = category


print("\nBEST-SELLING CATEGORY")
print(best_category, ":", category_highest_revenue)


# ============================================================
# BEST SALESPERSON BY REVENUE
# ============================================================

salesperson_revenue = {}

for row in data:

    salesperson = row["Salesperson"]
    revenue = float(row["Revenue"])

    if salesperson in salesperson_revenue:
        salesperson_revenue[salesperson] += revenue
    else:
        salesperson_revenue[salesperson] = revenue


print("\nREVENUE BY SALESPERSON")

for salesperson, revenue in salesperson_revenue.items():
    print(salesperson, ":", revenue)


best_salesperson = ""
salesperson_highest_revenue = 0

for salesperson, revenue in salesperson_revenue.items():

    if revenue > salesperson_highest_revenue:
        salesperson_highest_revenue = revenue
        best_salesperson = salesperson


print("\nBEST SALESPERSON")
print(best_salesperson, ":", salesperson_highest_revenue)


# ============================================================
# STEP 11: MONTHLY SALES ANALYSIS
# ============================================================

month_revenue = {}

for row in data:

    date = row["Date"]
    revenue = float(row["Revenue"])

    date = datetime.datetime.strptime(date, "%Y-%m-%d")

    if date.month in month_revenue:
        month_revenue[date.month] += revenue
    else:
        month_revenue[date.month] = revenue


print("\nMONTHLY SALES REPORT")

for month, revenue in month_revenue.items():
    print(month, ":", revenue)


# BEST MONTH

best_month = ""
month_highest_revenue = 0

for month, revenue in month_revenue.items():

    if revenue > month_highest_revenue:
        month_highest_revenue = revenue
        best_month = month


print("\nBEST MONTH")
print(best_month, ":", month_highest_revenue)


# WORST MONTH

worst_month = ""
month_lowest_revenue = float("inf")

for month, revenue in month_revenue.items():

    if revenue < month_lowest_revenue:
        month_lowest_revenue = revenue
        worst_month = month


print("\nWORST MONTH")
print(worst_month, ":", month_lowest_revenue)


# ============================================================
# STEP 13: MONTHLY PRODUCT PERFORMANCE
# ============================================================

best_month_products = {}
worst_month_products = {}

for row in data:

    date = datetime.datetime.strptime(row["Date"], "%Y-%m-%d")
    revenue = float(row["Revenue"])
    product = row["Product"]

    # Worst month
    if date.month == worst_month:

        if product in worst_month_products:
            worst_month_products[product] += revenue
        else:
            worst_month_products[product] = revenue

    # Best month
    if date.month == int(best_month):

        if product in best_month_products:
            best_month_products[product] += revenue
        else:
            best_month_products[product] = revenue


print("\nBEST MONTH - PRODUCT : REVENUE")

for product, revenue in best_month_products.items():
    print(product, ":", revenue)


print("\nWORST MONTH - PRODUCT : REVENUE")

for product, revenue in worst_month_products.items():
    print(product, ":", revenue)


# ============================================================
# STEP 14: MONTHLY REGIONAL PERFORMANCE
# ============================================================

monthly_region_revenue = {}

for row in data:

    date = datetime.datetime.strptime(row["Date"], "%Y-%m-%d")
    month = date.month

    revenue = float(row["Revenue"])
    region = row["Region"]

    if month not in monthly_region_revenue:
        monthly_region_revenue[month] = {}

    if region in monthly_region_revenue[month]:
        monthly_region_revenue[month][region] += revenue
    else:
        monthly_region_revenue[month][region] = revenue


print("\nMONTHLY REGIONAL PERFORMANCE")

for month, regions in monthly_region_revenue.items():

    print("\nMonth:", month)

    for region, revenue in regions.items():
        print(region, ":", revenue)


# ============================================================
# STEP 15: BEST REGION FOR EACH MONTH
# ============================================================

print("\nBEST REGION FOR EACH MONTH")

for month, regions in monthly_region_revenue.items():

    highest_revenue = 0
    best_region_month = ""

    for region, revenue in regions.items():

        if revenue > highest_revenue:
            highest_revenue = revenue
            best_region_month = region

    print("Month:", month)
    print("Best Region:", best_region_month)
    print("Revenue:", highest_revenue)


# ============================================================
# STEP 16: MONTHLY SALESPERSON PERFORMANCE
# ============================================================

monthly_salesperson_revenue = {}

for row in data:

    date = datetime.datetime.strptime(row["Date"], "%Y-%m-%d")
    month = date.month

    revenue = float(row["Revenue"])
    salesperson = row["Salesperson"]

    if month not in monthly_salesperson_revenue:
        monthly_salesperson_revenue[month] = {}

    if salesperson in monthly_salesperson_revenue[month]:
        monthly_salesperson_revenue[month][salesperson] += revenue
    else:
        monthly_salesperson_revenue[month][salesperson] = revenue


print("\nMONTHLY SALESPERSON PERFORMANCE")

for month, salespersons in monthly_salesperson_revenue.items():

    print("\nMonth:", month)

    for salesperson, revenue in salespersons.items():
        print(salesperson, ":", revenue)


# BEST SALESPERSON FOR EACH MONTH

print("\nBEST SALESPERSON FOR EACH MONTH")

for month, salespersons in monthly_salesperson_revenue.items():

    highest_revenue = 0
    best_salesperson_month = ""

    for salesperson, revenue in salespersons.items():

        if revenue > highest_revenue:
            highest_revenue = revenue
            best_salesperson_month = salesperson

    print("Month:", month)
    print("Best Salesperson:", best_salesperson_month)
    print("Revenue:", highest_revenue)


# ============================================================
# STEP 17: MONTHLY CATEGORY PERFORMANCE
# ============================================================

monthly_category_revenue = {}

for row in data:

    date = datetime.datetime.strptime(row["Date"], "%Y-%m-%d")
    month = date.month

    revenue = float(row["Revenue"])
    category = row["Category"]

    if month not in monthly_category_revenue:
        monthly_category_revenue[month] = {}

    if category in monthly_category_revenue[month]:
        monthly_category_revenue[month][category] += revenue
    else:
        monthly_category_revenue[month][category] = revenue


print("\nMONTHLY CATEGORY PERFORMANCE")

for month, categories in monthly_category_revenue.items():

    print("\nMonth:", month)

    for category, revenue in categories.items():
        print(category, ":", revenue)


# BEST CATEGORY FOR EACH MONTH

print("\nBEST CATEGORY FOR EACH MONTH")

for month, categories in monthly_category_revenue.items():

    highest_revenue = 0
    best_category_month = ""

    for category, revenue in categories.items():

        if revenue > highest_revenue:
            highest_revenue = revenue
            best_category_month = category

    print("Month:", month)
    print("Best Category:", best_category_month)
    print("Revenue:", highest_revenue)


# ============================================================
# STEP 18: PAYMENT METHOD ANALYSIS
# ============================================================

payment_revenue = {}

for row in data:

    payment_method = row["Payment_Method"]
    revenue = float(row["Revenue"])

    if payment_method in payment_revenue:
        payment_revenue[payment_method] += revenue
    else:
        payment_revenue[payment_method] = revenue


print("\nREVENUE BY PAYMENT METHOD")

for payment_method, revenue in payment_revenue.items():
    print(payment_method, ":", revenue)


# BEST PAYMENT METHOD

highest_payment_revenue = 0
best_payment_method = ""

for payment_method, revenue in payment_revenue.items():

    if revenue > highest_payment_revenue:
        highest_payment_revenue = revenue
        best_payment_method = payment_method


print("\nBEST PAYMENT METHOD")
print(best_payment_method, ":", highest_payment_revenue)


# ============================================================
# STEP 19: PRODUCT QUANTITY ANALYSIS
# ============================================================

product_quantity = {}

for row in data:

    product = row["Product"]
    quantity = int(row["Quantity"])

    if product in product_quantity:
        product_quantity[product] += quantity
    else:
        product_quantity[product] = quantity


print("\nQUANTITY SOLD BY PRODUCT")

for product, quantity in product_quantity.items():
    print(product, ":", quantity)



# BEST-SELLING PRODUCT BY QUANTITY

highest_quantity = 0
best_selling_product = ""

for product, quantity in product_quantity.items():

    if quantity > highest_quantity:
        highest_quantity = quantity
        best_selling_product = product


print("\nBEST-SELLING PRODUCT BY QUANTITY")
print(best_selling_product, ":", highest_quantity)


# ============================================================
# STEP 20: FINAL BUSINESS SUMMARY
# ============================================================

print("\n" + "=" * 50)
print("FINAL BUSINESS ANALYSIS SUMMARY")
print("=" * 50)

print("Total Revenue:", total_revenue)

print("Average Revenue per Order:", average_revenue)

print("Highest Value Order:", highest_revenue)

print("Lowest Value Order:", lowest_revenue)

print("Best Product by Revenue:",
      best_product, ":", product_highest_revenue)

print("Best Region:",
      best_region, ":", region_highest_revenue)

print("Best Category:",
      best_category, ":", category_highest_revenue)

print("Best Salesperson:",
      best_salesperson, ":", salesperson_highest_revenue)

print("Best Month:",
      best_month, ":", month_highest_revenue)

print("Worst Month:",
      worst_month, ":", month_lowest_revenue)

print("Best Payment Method:",
      best_payment_method, ":", highest_payment_revenue)

print("Best-Selling Product by Quantity:",
      best_selling_product, ":", highest_quantity)

print("=" * 50)