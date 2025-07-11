# Stock_Portfolio_Tracker
Internship Task 2 for CodeAlpha: A Python-based Stock Portfolio Tracker that calculates total investment value using hardcoded stock prices.

## 📌 Project Overview

This project is a **command-line-based Stock Portfolio Tracker**, developed in Python.  
It allows users to input the name and quantity of stocks they hold, then calculates the **total investment value** based on **predefined stock prices**.

If desired, the portfolio summary can be saved to a text file.

---

## 🚀 What This Project Does

- Accepts user input of stock names and quantity
- Uses **fuzzy string matching** to understand partially or mistyped stock names
- Displays **interpreted stock**, **unit price**, **subtotal**, and **total investment**
- Optionally **saves results to `portfolio_summary.txt`**

---

## 🔧 Key Concepts & Technologies Used

| Concept         | Description |
|----------------|-------------|
| `dict`         | To store stock names and prices  
| `input()`      | For user interaction  
| `difflib`      | To match user input to closest valid stock name  
| `if-else`      | Input validation and control flow  
| `File Handling`| To save portfolio summary as `.txt`  
| `loops`        | To repeat prompts and track multiple stocks  

---

## 💼 Real-World Applications

This type of portfolio tracker can be used by:

- 📊 **Retail Investors** – to calculate and log their investments
- 🏢 **Small Financial Firms** – for demo/training tools
- 👨‍💻 **Python Learners** – to understand practical use of dictionaries, string matching, file handling
- 📚 **Beginners in Finance/Tech** – for learning investment calculations

---

## 📈 Features

- ✅ Clean and simple console UI
- ✅ Fuzzy matching of stock names (`TSLA` or `Tsl` → TSLA)
- ✅ Prevents invalid input (non-integer quantity, zero, negative)
- ✅ Allows multiple stocks
- ✅ Final report can be saved for records

---

## 💻 Technologies Used

- **Language:** Python 3  
- **Libraries:** `difflib`, `os` (if extended for future automation)  
- **Platform:** Console / Terminal  
- **File Output:** Text file (`portfolio_summary.txt`)
