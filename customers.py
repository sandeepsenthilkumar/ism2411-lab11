"""Lab 11: Customer Dictionary & Lookup"""

# EXERCISE 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 2500
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# EXERCISE 2: Update and add
customer["phone"] = "555-1234"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# EXERCISE 3: Safe lookup
result = customer.get("email", "no email on file")
print(result)

try:
    bracket_result = customer["email"]
except KeyError:
    print("KeyError: 'email' not found using bracket notation")

# EXERCISE 4: Iterate
for key, value in customer.items():
    print(f"{key}: {value}")

print("Iterating without .items():")
for key in customer:
    print(key)
print("Without .items(), iteration gives keys only, not values")

# EXERCISE 5: Lookup table
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
price = 100
discount_rate = tier_discounts.get(customer["tier"], 0)
discount_amount = price * discount_rate
final_price = price - discount_amount
print(f"Tier: {customer['tier']}, Discount: {discount_rate*100}%, Final price: ${final_price}")

# EXERCISE 6: List of dicts
customers = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 2500},
    {"name": "Bob", "tier": "silver", "ytd_spend": 800},
    {"name": "Charlie", "tier": "bronze", "ytd_spend": 150}
]

tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

for cust in customers:
    discount = tier_discounts.get(cust["tier"], 0)
    print(f"{cust['name']} · Tier: {cust['tier']} · Discount: {discount*100}%")

# EXERCISE 7: Nested catalog
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
    "Tool B": {"price": 25.00, "stock": 5}
}

for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"Alert: {product_name} stock low ({details['stock']})")

# EXERCISE 8: Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}
for trans in transactions:
    region = trans["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + trans["amount"]

print(sales_by_region)

# REFLECTION
print("""
Q1: Using .get() in this case makes the code safe. In practice, I would use .get() to retrieve optional fields, or data from APIs or configuration files with the intention that if certain keys are missing, then we just return a default value, without causing errors in the program.

Q2: This method is similar to using accumulators. We loop through our list of transactions, extract some data (region) and add them to a dictionary using the keys. This is very similar to how we group data in pandas later in the course.
""")