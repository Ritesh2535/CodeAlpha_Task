# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 310
}

portfolio = {}
total_value = 0

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish entering stocks.\n")

# Input loop
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Stock not found in the list.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❗ Please enter a valid number.\n")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save = input("\nWould you like to save the portfolio to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
    try:
        with open(filename, 'w') as f:
            f.write("Stock,Quantity,Price,Total Value\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                f.write(f"{stock},{qty},{price},{value}\n")
            f.write(f"\nTotal Investment Value: ${total_value}\n")
        print(f"✅ Portfolio saved to {filename}")
    except Exception as e:
        print("❌ Error saving file:", e)
