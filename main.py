# 21 Sep 2025

class Convert:
    def __init__(self):
        pass


    def mile_to_km(self):
        print("how many Miles do you want to convert to Kilometer ?")
        mile = input()
        km = float(mile) * 1.60934
        print(f"{mile} Mile is {km:.3f} Kilometer")


    def pound_to_kg(self):
        print("how many Pound do you want to convert to Kilogram ?")
        pound = input()
        kg = float(pound) * 0.453592
        print(f"{pound} Pound is {kg:.3f} Kilogram")


    def foot_to_cm(self):
        print("how many Foot do you want to convert to Centimeter ?")
        foot = input()
        cm = float(foot) * 30.48
        print(f"{foot} Foot is {cm:.3f} Centimeter")


    def title(self):
        us_mile = "1 : Mile to Kilometer"
        us_pound = "2 : Pound to Kilogram"
        us_foot = "3 : Foot to Centimeter"

        print("Select your units")
        print(us_mile)
        print(us_pound)
        print(us_foot)


    def main(self):

        while True:

            self.title()
            user_select_unit = input("What items do you want to convert ?: ")
            try:
                user_select_unit = int(user_select_unit)
                if user_select_unit == 1:
                    self.mile_to_km()
                if user_select_unit == 2:
                    self.pound_to_kg()
                if user_select_unit == 3:
                    self.foot_to_cm()

                print("Do you want to convert the units again ?")
                ask_again = input("Y/N?: ").upper()
                if ask_again == "N":
                    break
            except:
                print("please input the number")

            # print("Do you want to convert the units again ?")
            # ask_again = input("Y/N?: ").upper()
            # if ask_again == "N":
            #     break

convert = Convert()
convert.main()  

if __name__ == "__main__":
    convert.main()