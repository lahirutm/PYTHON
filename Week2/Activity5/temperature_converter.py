class Temperature():
    def get_input(self):
        user_input = input("Enter temperature in Farenhite or Celcius: ")
        temp_unit = user_input[0]
        temp_value = user_input[1:]

        self.temp_unit = temp_unit
        self.temp_value = temp_value

    def calculate_temp(self):

        if self.temp_unit == "F":
            celcius = float(self.temp_value)
            farenhite = (celcius * 9/5) + 32
            print("Value in Farenhite: ", str(round(farenhite,2)))

        elif self.temp_unit == "C":
            farenhite = float(self.temp_value)
            celcius = (farenhite - 32) * 5/9
            print("Value in Celcius: ", str(round(celcius,2)))

        else:
            print("Invalid temperature value !")


def main():
    temperature = Temperature()
    temperature.get_input()
    temperature.calculate_temp()



if __name__ == "__main__":
    main()