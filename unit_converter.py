import tkinter as tk
from tkinter import ttk

class UnitConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Simple Unit Converter")
        self.geometry("400x250")
        self.resizable(False, False)

        # Conversion factors (relative to a base unit)
        self.CONVERSIONS = {
            "Length": {"Meters": 1.0, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084},
            "Weight": {"Grams": 1.0, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
            "Temperature": {"Celsius": 1.0, "Fahrenheit": 33.8, "Kelvin": 274.15}
        }
        
        self.create_widgets()

    def create_widgets(self):
        # Frame for input and dropdowns
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input value
        ttk.Label(main_frame, text="Value:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.value_entry = ttk.Entry(main_frame, width=15)
        self.value_entry.grid(row=0, column=1, padx=5, pady=5)
        self.value_entry.insert(0, "1")

        # Category dropdown
        ttk.Label(main_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.category_var = tk.StringVar()
        self.category_menu = ttk.Combobox(main_frame, textvariable=self.category_var, values=list(self.CONVERSIONS.keys()))
        self.category_menu.grid(row=1, column=1, padx=5, pady=5)
        self.category_menu.set("Length")
        self.category_menu.bind("<<ComboboxSelected>>", self.update_units)

        # From unit dropdown
        ttk.Label(main_frame, text="From:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.from_unit_var = tk.StringVar()
        self.from_unit_menu = ttk.Combobox(main_frame, textvariable=self.from_unit_var)
        self.from_unit_menu.grid(row=2, column=1, padx=5, pady=5)

        # To unit dropdown
        ttk.Label(main_frame, text="To:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.to_unit_var = tk.StringVar()
        self.to_unit_menu = ttk.Combobox(main_frame, textvariable=self.to_unit_var)
        self.to_unit_menu.grid(row=3, column=1, padx=5, pady=5)
        
        # Initial population of unit menus
        self.update_units()

        # Convert button
        convert_button = ttk.Button(main_frame, text="Convert", command=self.perform_conversion)
        convert_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Result label
        self.result_label = ttk.Label(main_frame, text="Result: -", font=("Helvetica", 12, "bold"))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def update_units(self, event=None):
        """Update the 'from' and 'to' unit dropdowns based on the selected category."""
        category = self.category_var.get()
        units = list(self.CONVERSIONS[category].keys())
        self.from_unit_menu['values'] = units
        self.to_unit_menu['values'] = units
        self.from_unit_menu.set(units[0])
        self.to_unit_menu.set(units[1] if len(units) > 1 else units[0])

    def perform_conversion(self):
        """Calculate and display the conversion result."""
        try:
            value = float(self.value_entry.get())
            category = self.category_var.get()
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()

            if from_unit == "" or to_unit == "":
                self.result_label.config(text="Result: Select units")
                return
            
            # Special handling for Temperature, as it's not a simple multiplication
            if category == "Temperature":
                if from_unit == "Celsius":
                    if to_unit == "Fahrenheit": result = (value * 9/5) + 32
                    elif to_unit == "Kelvin": result = value + 273.15
                    else: result = value # Celsius to Celsius
                elif from_unit == "Fahrenheit":
                    if to_unit == "Celsius": result = (value - 32) * 5/9
                    elif to_unit == "Kelvin": result = (value - 32) * 5/9 + 273.15
                    else: result = value # Fahrenheit to Fahrenheit
                elif from_unit == "Kelvin":
                    if to_unit == "Celsius": result = value - 273.15
                    elif to_unit == "Fahrenheit": result = (value - 273.15) * 9/5 + 32
                    else: result = value # Kelvin to Kelvin
            else: # Standard conversion for Length and Weight
                factors = self.CONVERSIONS[category]
                from_factor = factors[from_unit]
                to_factor = factors[to_unit]
                
                # Convert to base unit first, then to the target unit
                base_value = value / from_factor
                result = base_value * to_factor
            
            self.result_label.config(text=f"Result: {result:.4f}")

        except ValueError:
            self.result_label.config(text="Result: Invalid input")
        except Exception as e:
            self.result_label.config(text=f"Result: Error ({e})")

if __name__ == "__main__":
    app = UnitConverterApp()
    app.mainloop()
