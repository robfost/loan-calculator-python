# Loan Calculator App
# Author: Robert Foster

import tkinter as tk
from tkinter import messagebox

# Functions
def calculate_payment():
    try:
        loan_amount = float(entry_amount.get())
        annual_rate = float(entry_rate.get()) / 100
        years = int(entry_years.get())
        
        monthly_rate = annual_rate / 12
        months = years * 12

        # Amortization formula
        monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
        total_payment = monthly_payment * months

        result_label.config(
            text=f"Monthly Payment: ${monthly_payment:.2f}\nTotal Payment: ${total_payment:.2f}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values.")

def clear_fields():
    entry_amount.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_years.delete(0, tk.END)
    result_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Loan Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Loan Amount ($)").pack(pady=5)
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Annual Interest Rate (%)").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Loan Term (Years)").pack(pady=5)
entry_years = tk.Entry(root)
entry_years.pack()

tk.Button(root, text="Calculate", command=calculate_payment).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack()

result_label = tk.Label(root, text="", fg="blue", font=("Arial", 10))
result_label.pack(pady=20)

# Run App
root.mainloop()
