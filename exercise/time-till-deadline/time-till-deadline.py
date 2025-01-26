import datetime

user_input = input("Enter your goal with a deadline seperated with a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
calculated_time = deadline_date - today_date

hour_till = int(calculated_time.total_seconds() / 60 / 60)
print(f"Dear user! Time remaining for your goal: {goal} is {hour_till} hours ")