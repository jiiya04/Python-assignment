# NAME - JIYA GUPTA
# DATE - 6-11-25
# PROJECT TITLE- CALORIE TRACKER
print("WELCOME! This is a simple command-line tool to track daily calorie intake. ")
meals = []
calories = []
num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    print(f"\nEnter details for meal{i + 1}:")
    meal_name = input("Meal name: ")
    calorie_amount = float(input("Calories in this meal: "))
    meals.append(meal_name)
    calories.append(calorie_amount)

total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))


if total_calories > daily_limit:
    status = "Warning: You have exceeded your daily calorie limit!"
else:
    status = "Great! You are within your daily calorie limit."


print("\nDaily Calorie Summary")
print("Meal Name\tCalories")


for meal, cal in zip(meals, calories):
    print(f"{meal}\t\t{cal}")


print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories}")
print(f"Status:\t\t{status}\n")


save_option = input("Would you like to save this session to a file? (yes/no): ")

if save_option == "yes":
    filename = "calorie_intake.txt"

    with open(filename, "a") as file:
        for meal, cal in zip(meals, calories):
            file.write(f"{meal}\t{cal}\n")
        file.write(f"Total Calories: {total_calories}\n")
        file.write(f"Average Calories: {average_calories}\n")
        file.write(f"Daily Limit: {daily_limit}\n")
        file.write(f"Status: {status}\n")

    print(f"\nSession saved successfully to '{filename}'.")
else:
    print("\nSession not saved!")

print("\nThank you for using the Daily Calorie Tracker! \n")
