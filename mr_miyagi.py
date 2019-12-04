 #mr Miyagi trainee ##projct

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi respond with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'



while True:
    user_input = input('Hello! Start interacting with MR. Miyagi:')
    sensei_input = user_input[0:8]
    if user_input == 'Sensei, I am at peace':
        break
    elif 'Sensei' not in (sensei_input):
        print('You are smart, but not wise - address me as Sensei, please')
    elif '?' in user_input:
        print('Questions are wise, but for now...Wax on, Wax off!')
    elif 'block' in user_input:
        print('Remember, best block, not to be there..')
    else:
        print('Do not lose focus. Wax on. Wax off.')
print('Sometimes, what heart know, head forgets')
