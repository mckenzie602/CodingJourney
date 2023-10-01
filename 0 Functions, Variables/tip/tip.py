def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_input = d
    dollar_input = dollar_input.lstrip("$")
    dollar_input = float(dollar_input)
    return dollar_input

def percent_to_float(p):
    percentage_input = p
    percentage_input = percentage_input.rstrip("%")
    percentage_input = float(percentage_input)/100.0
    return percentage_input


main()