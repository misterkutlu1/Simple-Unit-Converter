# 📏 Simple Unit Converter GUI

A user-friendly desktop application for performing common unit conversions. This application is built entirely with Python's standard `tkinter` library, making it lightweight and cross-platform without requiring any external dependencies.

![Screenshot of the Unit Converter App](screenshot.png)
*(Note: You should take a screenshot of the running application and save it as `screenshot.png` in your repository for this image to display.)*

## ✨ Features

-   **Intuitive Interface**: A clean and simple GUI for easy interaction.
-   **Multiple Categories**: Supports conversions for Length, Weight, and Temperature.
-   **Dynamic Dropdowns**: The unit options change dynamically based on the selected category.
-   **Real-time Calculation**: Get instant results with the click of a button.
-   **No External Dependencies**: Runs out-of-the-box with a standard Python installation.

## 🚀 How to Run

Since `tkinter` is part of the Python standard library, you don't need to install anything extra.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/unit-converter-gui.git
    cd unit-converter-gui
    ```

2.  **Run the application:**
    ```bash
    python unit_converter.py
    ```

The application window should appear, ready for you to start converting!

## 🔧 How to Extend

Adding new units or categories is straightforward.

1.  Open `unit_converter.py`.
2.  Locate the `self.CONVERSIONS` dictionary in the `__init__` method.
3.  Add a new category or add new units to an existing category.

**Example: Adding "Volume"**

```python
self.CONVERSIONS = {
    "Length": {"Meters": 1.0, "Kilometers": 0.001, ...},
    "Weight": {"Grams": 1.0, "Kilograms": 0.001, ...},
    "Temperature": {"Celsius": 1.0, ...},
    "Volume": {"Liters": 1.0, "Milliliters": 1000, "Gallons": 0.264172} # New Category
}
```

The application will automatically pick up the new category and units when you run it. Note that you may need to add special logic for non-linear conversions, as was done for Temperature.
