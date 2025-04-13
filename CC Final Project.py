import tkinter as tk
from tkinter import messagebox

# Superscript Conversion
def parse_superscript(chars):
    """
    Converts a superscript string (e.g., '⁻²') into an integer.
    """
    superscripts = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', 
                    '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-'}
    number = ''.join(superscripts.get(c, '') for c in chars)
    return int(number) if number else 0

def superscript(num):
    """
    Converts an integer into its superscript representation.
    """
    sup_map = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
               '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻'}
    num_str = str(num)
    return ''.join(sup_map.get(c, c) for c in num_str)

# Parsing Dimensions
def parse_dimensions(dim_str):
    """
    Parses a dimension string like 'M¹L⁰T⁻²' and returns a list of exponents for each dimension.
    """
    powers = {'M': 0, 'L': 0, 'T': 0, 'I': 0, 'θ': 0, 'N': 0, 'J': 0}
    i = 0
    while i < len(dim_str):
        char = dim_str[i]
        if char in powers:
            # Default power is 1
            power = 1  
            if i + 1 < len(dim_str) and dim_str[i + 1] in "⁻¹²³⁴⁵⁶⁷⁸⁹⁰":
                j = i + 1
                while j < len(dim_str) and dim_str[j] in "⁻¹²³⁴⁵⁶⁷⁸⁹⁰":
                    j += 1
                power = parse_superscript(dim_str[i + 1:j])
                i = j - 1  # Adjust the pointer to the last processed character
            powers[char] = power
        i += 1
    return [powers['M'], powers['L'], powers['T'], powers['I'], powers['θ'], powers['N'], powers['J']]

# Formatting Dimensions
def format_dimensions(powers):
    """
    Formats a list of dimension powers into a string (e.g., [1, 0, -2] -> 'M¹T⁻²').
    """
    dims = ['M', 'L', 'T', 'I', 'θ', 'N', 'J']
    result = []
    for dim, power in zip(dims, powers):
        if power != 0:
            result.append(f"{dim}{superscript(power)}")
    return ''.join(result)

# Calculate Dimensions
def calculate_expression(expression):
    try:
        terms = []
        operators = []

        # Parse the expression into terms and operators
        i = 0
        while i < len(expression):
            if expression[i] in "*/":
                operators.append(expression[i])
                i += 1
            else:
                term = ""
                while i < len(expression) and expression[i] not in "*/":
                    term += expression[i]
                    i += 1
                terms.append(term.strip().upper())

        if len(terms) - 1 != len(operators):
            raise ValueError("Invalid expression format. Check the use of '*' or '/'.")

        # Look up dimensions for each term
        dimensions = []
        for term in terms:
            if term in my_dict:
                dimensions.append(parse_dimensions(my_dict[term]))
            else:
                raise ValueError(f"'{term}' not found in the database.")

        # Apply operations
        result = dimensions[0]
        for op, dim in zip(operators, dimensions[1:]):
            if op == "*":
                result = [r + d for r, d in zip(result, dim)]  # Add powers for multiplication
            elif op == "/":
                result = [r - d for r, d in zip(result, dim)]  # Subtract powers for division

        # Format and display result
        result_str = format_dimensions(result)
        messagebox.showinfo("Result", f"Resultant Dimensions: {result_str}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Data Dictionary
# Data Dictionary with Additional Quantities
my_dict = {
    'MASS': 'M¹L⁰T⁰',
    'ACCELERATION': 'M⁰L¹T⁻²',
    'FORCE': 'M¹L¹T⁻²',
    'VELOCITY': 'M⁰L¹T⁻¹',
    'TIME': 'M⁰L⁰T¹',
    'LENGTH': 'M⁰L¹T⁰',
    'ENERGY': 'M¹L²T⁻²',
    'POWER': 'M¹L²T⁻³',
    'KINETIC_ENERGY': 'M¹L²T⁻²',  # Same as ENERGY
    'MOMENTUM': 'M¹L¹T⁻¹',
    'PRESSURE': 'M¹L⁻¹T⁻²',
    'DENSITY': 'M¹L⁻³T⁰',
    'WORK': 'M¹L²T⁻²',  # Same as ENERGY
    'IMPULSE': 'M¹L¹T⁻¹',  # Same as MOMENTUM
    'FREQUENCY': 'M⁰L⁰T⁻¹',
    'VOLUME': 'M⁰L³T⁰',
    'AREA': 'M⁰L²T⁰',
    'CHARGE': 'M⁰L⁰T¹I¹',
    'CURRENT': 'M⁰L⁰T⁰I¹',
    'POTENTIAL': 'M¹L²T⁻³I⁻¹',
    'RESISTANCE': 'M¹L²T⁻³I⁻²',
    'CAPACITANCE': 'M⁻¹L⁻²T⁴I²',
    'INDUCTANCE': 'M¹L²T⁻²I⁻²',
}

# Show About Us
def show_about_us():
    about_us_text = (
        "About Us\n\n"
        "Kartik Modi [24BAI10522]\n"
        "Hardik Jain [24BAI10355]\n"
        "Anushka Pundir [24BAI10102]\n"
        "Jiya Jaiswal [24BAI10275]\n"
        "Arun Tomar [24BAI10315]\n\n"
        "Under Supervision of Dr. Sumit Mittal"
    )
    messagebox.showinfo("About Us", about_us_text)

# Main GUI
def show_main_menu():
    main_menu = tk.Tk()
    main_menu.title("Dimensional Analysis Tool")
    main_menu.geometry("600x400")
    main_menu.configure(bg="#e8f5e9")

    header = tk.Label(main_menu, text="Dimensional Analysis Tool", font=("Arial", 24, "bold"), bg="#e8f5e9", fg="black")
    header.pack(pady=20)

    calc_button = tk.Button(
        main_menu, text="Dimensional Calculator", font=("Arial", 14), bg="#4caf50", fg="white",
        command=lambda: open_calculator(main_menu)
    )
    calc_button.pack(pady=10)

    theory_button = tk.Button(
        main_menu, text="Theory", font=("Arial", 14), bg="#2196f3", fg="white",
        command=lambda: show_theory(main_menu)
    )
    theory_button.pack(pady=10)

    # Adding About Us button
    about_button = tk.Button(
        main_menu, text="About Us", font=("Arial", 14), bg="#ffc107", fg="black",
        command=show_about_us
    )
    about_button.pack(pady=10)

    main_menu.mainloop()

def open_calculator(parent):
    parent.destroy()
    calculator_window = tk.Tk()
    calculator_window.title("Dimensional Calculator")
    calculator_window.geometry("600x400")
    calculator_window.configure(bg="#e8f5e9")

    header = tk.Label(calculator_window, text="Dimensional Calculator", font=("Arial", 24, "bold"), bg="#e8f5e9", fg="black")
    header.pack(pady=20)

    label = tk.Label(calculator_window, text="Enter Expression (e.g., MASS*ACCELERATION or FORCE/AREA):",
                     font=("Arial", 14), bg="#e8f5e9", fg="black")
    label.pack(pady=10)

    expression_input = tk.Entry(calculator_window, font=("Arial", 14), width=40)
    expression_input.pack(pady=10)

    calculate_btn = tk.Button(
        calculator_window, text="Calculate Dimensions", font=("Arial", 14), bg="#4caf50", fg="white",
        command=lambda: calculate_expression(expression_input.get())
    )
    calculate_btn.pack(pady=20)

    back_btn = tk.Button(
        calculator_window, text="Back to Main Menu", font=("Arial", 14), bg="#f44336", fg="white",
        command=lambda: go_back(calculator_window)
    )
    back_btn.pack(pady=10)

    calculator_window.mainloop()

def show_theory(parent):
    parent.destroy()
    theory_window = tk.Tk()
    theory_window.title("Dimensional Analysis Theory")
    theory_window.geometry("600x400")
    theory_window.configure(bg="#e8f5e9")

    header = tk.Label(theory_window, text="Dimensional Analysis - Theory", font=("Arial", 24, "bold"), bg="#e8f5e9", fg="black")
    header.pack(pady=10)

    # Create a frame to hold the scrollable content
    container = tk.Frame(theory_window, bg="#e8f5e9")
    container.pack(fill="both", expand=True, padx=10, pady=10)

    # Add a canvas for scrolling
    canvas = tk.Canvas(container, bg="#e8f5e9", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas
    scrollable_frame = tk.Frame(canvas, bg="#e8f5e9")
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Add the theory content
    text = (
        "Dimensional analysis is a powerful technique used in physics and engineering "
        "to simplify the study of physical quantities and their relationships.\n\n"
        "### Key Concepts:\n"
        "1. **Fundamental Dimensions:**\n"
        "   - M: Mass\n"
        "   - L: Length\n"
        "   - T: Time\n"
        "   - I: Electric Current\n"
        "   - θ: Temperature\n"
        "   - N: Amount of Substance\n"
        "   - J: Luminous Intensity\n\n"
      "2. **Dimensional Formula:**\n"
        "   Each physical quantity can be expressed as a combination of fundamental dimensions.\n"
        "   Example:\n"
        "   - Force = Mass × Acceleration → M¹L¹T⁻²\n"
        "   - Energy = Force × Distance → M¹L²T⁻²\n\n"
          "3. **Applications of Dimensional Analysis:**\n"
        "   - **Unit Consistency:** Ensures that equations are dimensionally consistent.\n"
        "   - **Conversion of Units:** Helps convert quantities between unit systems.\n"
        "   - **Deriving Relationships:** Assists in deriving formulas when the relationship between variables is unknown.\n"
        "   - **Checking Errors:** Identifies errors in equations or computations by analyzing dimensions.\n\n"
        "4. **Principle of Homogeneity:**\n"
        "   An equation is dimensionally correct only if all terms on both sides of the equation have the same dimensions.\n\n"
        "5. **Limitations of Dimensional Analysis:**\n"
        "   - It cannot determine dimensionless constants (like π).\n"
        "   - It cannot distinguish between different physical quantities with the same dimensions (e.g., Torque and Energy).\n\n"
        "### Examples:\n"
        "   - Velocity = Distance / Time → M⁰L¹T⁻¹\n"
        "   - Pressure = Force / Area → M¹L⁻¹T⁻²\n"
        "   - Work = Force × Distance → M¹L²T⁻²\n\n"
        "Dimensional analysis provides a foundational understanding of the relationships "
        "between physical quantities and is an essential tool for students and professionals alike."
    )

    theory_label = tk.Label(scrollable_frame, text=text, font=("Arial", 12), bg="#e8f5e9", justify="left")
    theory_label.pack(padx=10, pady=5)

    # Back to main menu button
    back_button = tk.Button(
        theory_window, text="Back to Main Menu", font=("Arial", 14), bg="#f44336", fg="white",
        command=lambda: go_back(theory_window)
    )
    back_button.pack(pady=10)

    theory_window.mainloop()

def go_back(window):
    window.destroy()
    show_main_menu()

# Start the main menu
show_main_menu()
