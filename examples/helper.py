def days_to_unit(number_of_days, conversion_unit):
        if conversion_unit == "hours":
            return f"{number_of_days} days are {number_of_days*24} {conversion_unit}"
        elif conversion_unit == "minutes":
            return f"{number_of_days} days are {number_of_days*24*60} {conversion_unit}"
        else:
             return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:

        user_input_number=int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_vale=days_to_unit(user_input_number, days_and_unit_dictionary["units"])
            print(calculated_vale)
        elif user_input_number == 0:
              print("You entered a 0, please enter valid positive number")
        else:
              print("You entered a Negative number, please enter valid positive number")
    except ValueError:
        print("Your input is not a number, don't ruin my program")


user_input_message="Hey User, Enter number of days and conversion unit\n"