import difflib  

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "INFY": 1600,
    "RELIANCE": 2400,
    "META": 320,
    "TCS": 3700,
    "WIPRO": 430,
    "MSFT": 330,
    "AMAZON": 142,
    "HDFC": 2900,
    "ICICIBANK": 1200,
    "ADANIPORTS": 890,
    "SBIN": 590
}

portfolio = {}  # Stores selected stock → quantity

print("="*50)
print("📈 Welcome to the Stock Portfolio Tracker")
print("="*50)
print("\n🧾 This tool will help you calculate your total stock investments.\n")
print("💡 Tip: You can type partial stock names like 'goo' for GOOGL or 'tsl' for TSLA.")
print("📋 Available Stocks:", ", ".join(sorted(stock_prices.keys())))
print("🔚 Type 'done' when you're finished adding stocks.\n")
while True:
    user_input = input("📝 Enter stock name (or 'done' to finish): ").strip().upper()
    if user_input == "DONE":
        break   

 match = difflib.get_close_matches(user_input, stock_prices.keys(), n=1, cutoff=0.6)

    if not match:
        print("❌ Could not recognize that stock. Please try again.")
        continue

    stock = match[0]
    print(f"✅ Interpreted as: {stock} - ₹{stock_prices[stock]} per share")

       try:
        qty = int(input(f"🔢 Enter quantity of {stock} shares: "))
        if qty <= 0:
            print("❌ Quantity must be greater than zero.")
            continue
    except ValueError:
        print("❌ Invalid number entered. Please try again.")
        continue

    # 🗃️ Update portfolio
    portfolio[stock] = portfolio.get(stock, 0) + qty
    print(f"📦 Added: {qty} shares of {stock}\n")


if not portfolio:
    print("⚠️ No stocks were entered. Portfolio is empty.")
else:
    print("\n📑 Final Portfolio Summary")
    print("-"*40)
    total = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        subtotal = price * qty
        total += subtotal
        print(f"{stock}: {qty} shares × ₹{price} = ₹{subtotal}")
    print("-"*40)
    print(f"💰 Total Investment Value: ₹{total}")

   
    save = input("\n📁 Would you like to save this summary to a file? (yes/no): ").strip().lower()
    if save == "yes":
        with open("portfolio_summary.txt", "w") as f:
            f.write("📑 Portfolio Summary\n")
            f.write("-"*30 + "\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                subtotal = price * qty
                f.write(f"{stock}: {qty} × ₹{price} = ₹{subtotal}\n")
            f.write("-"*30 + "\n")
            f.write(f"Total Investment Value: ₹{total}\n")
        print("✅ Saved as 'portfolio_summary.txt'")

print("\n🚀 Thank you for using the Stock Portfolio Tracker!")
