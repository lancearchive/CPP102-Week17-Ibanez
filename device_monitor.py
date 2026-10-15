readings = [28, 31, 35, 37, 29]

def get_initial_readings():
    """Return the initial list of temperature readings."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Return True if text represents a valid whole number."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def add_reading(readings):
    """Prompt user and add a valid reading to the list."""
    while True:
        text = input("Enter new reading: ")
        if len(text) == 0:
            print("\nInvalid input. The reading cannot be empty.\n")
            return
        elif not is_whole_number(text):
            print("\nInvalid input. Enter a whole number only.\n")
            return
        value = int(text)
        if value < 0 or value > 100:
            print("\nInvalid reading. Enter a value from 0 to 100.\n")
            return
        else:
            readings.append(value)
            print("\nReading added successfully.\n")
            return


def classify_reading(reading, warning_limit, critical_limit):
    """Return classification: NORMAL, WARNING, or CRITICAL."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    """Return sum of all readings using a loop only."""
    total = 0
    for value in readings:
        total = total + value
    return total


def compute_average(readings):
    """Return average of all readings."""
    total = compute_total(readings)
    return total / len(readings)


def find_minimum(readings):
    """Return the smallest reading using a loop."""
    minimum = readings[0]
    for value in readings:
        if value < minimum:
            minimum = value
    return minimum


def find_maximum(readings):
    """Return the largest reading using a loop."""
    maximum = readings[0]
    for value in readings:
        if value > maximum:
            maximum = value
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Count how many readings belong to the given category."""
    count = 0
    for value in readings:
        if classify_reading(value, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Return overall system status based on counts."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_menu():
    """Display the main program menu."""
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    """Show all readings with their position numbers."""
    print("\nCURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")
    print()


def display_classifications(readings):
    """Show each reading with its classification."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for value in readings:
        category = classify_reading(value, 30, 35)
        print(f"{value} °C -> {category}")
    print()


def display_summary(readings):
    """Calculate and display full monitoring summary."""
    warning_limit = 30
    critical_limit = 35
    count_readings = len(readings)

    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning_count = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical_count = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    normal_pct = (normal_count / count_readings) * 100
    warning_pct = (warning_count / count_readings) * 100
    critical_pct = (critical_count / count_readings) * 100

    status = determine_overall_status(warning_count, critical_count)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {count_readings}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print()
    print(f"NORMAL   : {normal_count} ({normal_pct:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_pct:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_pct:.2f}%)")
    print()
    print(f"Overall Status: {status}")
    print()


def main():
    """Main program loop."""
    global readings
    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            display_classifications(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.\n")


main()