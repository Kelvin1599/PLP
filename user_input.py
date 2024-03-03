name = input('What is your name:')
print('You entered:', name)

AGE = input ('what is your age:')
print('You entered:', AGE)


location = input ('what is your location:')
print('You entered:', location)

def generate_personalized_message(name):
    message = f"Hello {name} from {location}, you're {AGE} years old thank you for reaching out to us.  How can I help you?"
    return message

personalized_message = generate_personalized_message(name)
print(personalized_message)
