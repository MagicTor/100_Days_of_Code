import tkinter

class Distance_Program():
    def __init__(self):

        window = tkinter.Tk()
        window.title("Distance Converter")
        window.config(padx=20, pady=20)

        self.radio_state = tkinter.IntVar()
        self.radiobutton1 = tkinter.Radiobutton(text="Miles to Km", value=0, variable=self.radio_state, command=self.radio_used)
        self.radiobutton2 = tkinter.Radiobutton(text="Km to Miles", value=1, variable=self.radio_state, command=self.radio_used)
        self.radiobutton1.grid(column=0, row=0)
        self.radiobutton2.grid(column=3, row=0)

        self.equate_label = tkinter.Label(text="is equal to", padx=5, pady=5)
        self.equate_label.grid(column=0, row=2)

        self.entry_field = tkinter.Entry(width=7)
        self.entry_field.insert(tkinter.END, string="0")
        self.entry_field.grid(column=1, row=1)

        self.entry_field_label = tkinter.Label(text="Miles", padx=5, pady=5)
        self.entry_field_label.grid(column=2, row=1)

        self.result = tkinter.Label(text="0", padx=5, pady=5)
        self.result.grid(column=1, row=2)

        self.result_label = tkinter.Label(text="Km", padx=5, pady=5)
        self.result_label.grid(column=2, row=2)

        self.button = tkinter.Button(text="Calculate", command=self.get_km, padx=5, pady=5)
        self.button.grid(column=1, row=3)

        window.mainloop()

    def get_km(self):
        miles_value = float(self.entry_field.get())
        km_value = round(miles_value * 1.60934, 2)
        self.result.config(text=km_value)

    def get_miles(self):
        km_value = float(self.entry_field.get())
        miles_value = round(km_value * 0.6213712, 2)
        self.result.config(text=miles_value)

    def radio_used(self):
        self.result.config(text="0")
        if self.radio_state.get() == 0:
            self.entry_field_label.config(text="Miles")
            self.result_label.config(text="Km")
            self.button.config(command=self.get_km)
        elif self.radio_state.get() == 1:
            self.entry_field_label.config(text="Km")
            self.result_label.config(text="Miles")
            self.button.config(command=self.get_miles)

if __name__ == "__main__":
    app = Distance_Program()
