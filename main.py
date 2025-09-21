# 21 Sep 2025
# converts Mile to Kilometers
# converts Pound to Kilogram
# converts Inches to Centimeter

# note:
# 1) fix input unit - if users input with letter?
# 2) fix number input - if users input with letter?
# 3) fix if user select outof 1-3 - show text message to select only 1-3

def mile_to_km():
    print("how many Miles do you want to convert to Kilometer ?")
    mile = input()
    km = float(mile) * 1.60934
    return print(f"{mile} Mile is {km:.3f} Kilometer")


def pound_to_kg():
    print("how many Pound do you want to convert to Kilogram ?")
    pound = input()
    kg = float(pound) * 0.453592
    return print(f"{pound} Pound is {kg:.3f} Kilogram")


def foot_to_cm():
    print("how many Foot do you want to convert to Centimeter ?")
    foot = input()
    cm = float(foot) * 30.48
    return print(f"{foot} Foot is {cm:.3f} Centimeter")


def title():
    us_mile = "1 : Mile to Kilometer"
    us_pound = "2 : Pound to Kilogram"
    us_foot = "3 : Foot to Centimeter"

    print("Select your units")
    print(us_mile)
    print(us_pound)
    print(us_foot)


def main():

    while True:

        title()
        user_select_unit = input("What items do you want to convert ?: ")
        user_select_unit = int(user_select_unit)
        if user_select_unit == 1:
            mile_to_km()
        if user_select_unit == 2:
            pound_to_kg()
        if user_select_unit == 3:
            foot_to_cm()

        print("Do you want to convert the units again ?")
        ask_again = input("Y/N?: ").upper()
        if ask_again == "N":
            break
    

if __name__ == "__main__":
    main()