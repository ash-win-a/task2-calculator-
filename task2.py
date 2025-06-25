import tkinter as tk
from tkinter import messagebox


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


root = tk.Tk()
root.title("Simple Calculator")


tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root, width=20)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root, width=20)
entry2.pack(pady=5)

tk.Label(root, text="Choose Operation:").pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="", width=5, command=lambda: calculate("")).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="/", width=5, command=lambda: calculate("/")).grid(row=0, column=3, padx=5, pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()