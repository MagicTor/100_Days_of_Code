import tkinter

def get_km():
    miles_value = float(miles.get())
    km_value = round(miles_value * 1.60934, 2)
    km_result_label.config(text=km_value)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles = tkinter.Entry(width=7)
miles.insert(tkinter.END, string="0")
miles.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", padx=5, pady=5)
miles_label.grid(column=2,row=0)

equate_label = tkinter.Label(text="is equal to", padx=5, pady=5)
equate_label.grid(column=0,row=1)

km_result_label = tkinter.Label(text="0", padx=5, pady=5)
km_result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", padx=5, pady=5)
km_label.grid(column=2,row=1)

button = tkinter.Button(text="Calculate", command=get_km, padx=5, pady=5)
button.grid(column=1, row=2)

window.mainloop()
