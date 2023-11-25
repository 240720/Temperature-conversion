def convert_temperature():
    while True:
        try:
            value = float(input("Enter a temperature value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    while True:
        source_unit = input("Enter the original unit (C/F): ").upper()
        if source_unit not in ["C", "F"]:
            print("Unsupported unit. Please enter C or F.")
        else:
            break

    while True:
        target_unit = input("Enter the converting unit (C/F): ").upper()
        if target_unit not in ["C", "F"]:
            print("Unsupported unit. Please enter C or F.")
        else:
            break

    if source_unit == "C":
        if target_unit == "F":
            result = (value * 9/5) + 32
            print(f"{value}C is {result}F.")
        else:
            print("Invalid conversion. Please try again.")
    elif source_unit == "F":
        if target_unit == "C":
            result = (value - 32) * 5/9
            print(f"{value}F is {result}C.")
        else:
            print("Invalid conversion. Please try again.")
    else:
        print("Invalid conversion. Please try again.")

convert_temperature()
