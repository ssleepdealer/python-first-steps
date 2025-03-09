# This program says hello and asks for my name.
print("Hello!")
print("What is your name?")  # Ask for the name
my_name = input()
print("It is good to meet you, " + my_name)
print("The length of your name is: ")
print(len(my_name))
print("What is your age?")  # Ask for the age
my_age = input()
print("You will be " + str(int(my_age) + 3) + " in three years.")
print(
    "If you'll keep working hard, by that time you'll be happy and fulfilling your dreams!"
)
print('Do you promise to your future self working hard to get the "shit" done?')
response = input().lower()
if response == "yes":
    print("Good luck then!")
else:
    print("Then what you want?")
