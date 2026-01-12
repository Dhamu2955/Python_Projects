def Unit_Converter(value: int, units: str):
    match units:
        case "mi":
            return f"{round((value * 1.60934), 2)} km"
        case "km":
            return f"{round((value / 1.60934), 2)} Mi"
        case "lb":
            return f"{round((value / 2.20462), 2)} kg"
        case "kg":
            return f"{round((value * 2.20462), 2)} lb"
        case "c":
            return f"{round((value * 9/5 + 32), 2)} F"
        case "f":
            return f"{round((value - 32) * 5/9, 2)} C"


print("Welcome to the Unit Converter")
running = True
while running:
    print("You can convert either: \n"
          "Miles (Mi) <-> Kilometers (km)\n"
          "Pounds (lb) <-> Kilograms (kg)\n"
          "Celsius (C) <-> Fahrenheit (F)\n")
    print("What would you like to convert: \n"
          "Enter a value followed by a Unit like so (value, unit).\n"
          "Units are referenced in brackets above.")
    options = ""
    while len(options.split(",")) != 2:
        options = input(
            "Please enter a value and unit (or quit at any time to exit): ")
        if options.lower() == "quit":
            running = False
            break
    if running:
        value, unit = options.split(",")
        int_value = int(value.strip())
        str_unit = unit.strip().lower()

    print(Unit_Converter(int_value, str_unit))

    another_one = ""
    while another_one != "yes":
        another_one = input(
            "Would you like to convert another number? (Yes / No): ").lower()
        if another_one == "no":
            running = False
            another_one = "yes"
