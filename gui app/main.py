import tkinter as tk
app = tk.Tk()
app.title("My GUI App")
app.geometry("700x400")

first_lable =tk.Label(app, text="First Number")
first_lable.pack()
first_number = tk.Entry(app)
first_number.pack()

second_lable =tk.Label(app, text="Second Number")
second_lable.pack()
second_number = tk.Entry(app)
second_number.pack()

result = tk.Label(app, text="Result")
result.pack()
def add():
    first = int(first_number.get())
    second = int(second_number.get())
    total = first + second
    result.config(text="Result: " + str(total))

button = tk.Button(app, text="Add", command=add)
button.pack()
app.mainloop()