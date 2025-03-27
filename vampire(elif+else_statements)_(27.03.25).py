print('Hello, now I will determine whether you are Alice, grannie or an immortal vampire. Are you ready?')
response = input().lower()

if response == 'yes':
    print('Okay, what is your name?')
else:
    print('You definetely are not Alice cuz you are scared to be checked.')


name = input().lower()

print('What is your age?')

age = int(input())


if name == 'alice' and age == 12 :
    print ('Hi, Alice.')

elif age < 12:
    print('You are not Alice, kiddo. Alice is older than you.')
elif age < 65:
    print("You are not Alice cause Alice is younger tham you.")
elif age > 2000:
    print('You are not Alice. Unlike you, Alice is not undead, immortal vampire.')
elif age > 65:
    print('You are not Alice, grannie.')

