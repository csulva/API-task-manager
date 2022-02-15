# API account manager to update API information from the URL

# Imports
import requests
import time
url = 'http://demo.codingnomads.co:8080/tasks_api/users'

def get_id(email):
    """Function used to return the user's ID based on the email provided

    Args:
        email (string): the email address provided and used to search the API for the corresponding ID

    Returns:
        int: ID in the API account
    """
    response = requests.get(url)
    data = response.json()
    for accounts in data['data']:
        if accounts['email'] == email:
            id = accounts['id']
    return id

def new_account(first, last, email):
    """POST request -- Creates a new account for the user based on the credentials provided.

    Args:
        first (string): First name for the account
        last (string): Last name for the account
        email (string): Email for the account
    """
    # Info to be added to the API. User's ID is created automatically
    body = {
    'first_name': first,
    'last_name': last,
    'email': email,
    }
    response = requests.post(url, json=body)
    # If email is already in use
    if response.status_code == 400:
        time.sleep(1)
        print('Email address is already in use. Please try again.\n')
        request()
    # If POST is successful
    elif response.status_code == 201:
        time.sleep(1)
        print(response.status_code)
        print(f'Account successfully created with email address "{email}"')
    # Other errors
    else:
        time.sleep(1)
        print('Sorry, there was an error. Please try again.\n')
        request()

def view_account_info(email):
    """GET request -- Returns the user's account information based on the email provided

    Args:
        email (string): the email address provided and used to search the API for the account info.
    """
    response = requests.get(url)
    data = response.json()
    info = []
    time.sleep(1)
    for account in data['data']:
        if account['email'] == email:
            info.append(account)
    # If no account can be yielded
    if info == []:
        print("It doesn't appear you have an account based on the email address provided. Try again or try creating one with option 1.")
        quit()
    # If email is accessible in the API -- if it exists
    elif info[0]:
        print("Here is the info for the account associated with your email address: \n")
        print(account)
    else:
        response.status_code = 400
        print(response.status_code)
        print('Sorry there appears to be an error. Please try again.')

def update_account(email):
    """PUT request -- This function lets the user update the account info based
    on the email provided

    Args:
        email (string): the email address provided and used to search the API for the account info.
    """
    # GETs the account info from the email provided and prints it
    view_account_info(email)
    # GET the ID of the account - this is required in order to update the account
    id = get_id(email)
    # User input
    print('Please update your information...')
    time.sleep(1)
    first = input('What is your first name? ')
    last = input('What is your last name? ')
    new_email = input('What is your email address? ')
    # Updates the account based on the ID and user input provided
    body = {
        'id': id,
        'first_name': first,
        'last_name': last,
        'email': new_email,
    }
    put_url = f'http://demo.codingnomads.co:8080/tasks_api/users/{id}'
    response = requests.put(put_url, json=body)
    # Prints successful -- will only get this far if the email exists (see view_account_info() function)
    print(response.status_code)
    if response.status_code == 201:
        print('Your account has been successfully updated.')
    else:
        print('Looks like there was an error updating the account. Please try again')
        request()


def delete_task(email):
    """DELETE request - deletes the user's account based on the email provided but first checks to
    make sure it is the right account before the user deletes it.

    Args:
        email (string): the email address provided and used to search the API for the account info.
    """
    # GETs the account info from the email provided and prints it
    view_account_info(email)
    # GET the ID of the account - this is required in order to delete the account
    id = get_id(email)
    # Loop to confirm the user wants to delete the account based on the info printed, or not.
    while True:
        verify = input('If this is correct, hit the "enter" key now to delete your account. Otherwise, type "quit" to enter a new one... ').lower()
        # To quit the request -- it will restart the process
        if verify == 'quit':
            request()
        # Hit enter/return to move forward with the DELETE request
        elif verify == '':
            # The call to the API, deletes the account based on the ID returned earlier (see get_id())
            response = requests.delete(url + f'/{id}')
            time.sleep(1)
            print(response.status_code)
            print(f'Successfully deleted account of "{email}" email address.')
            quit()
        # If "quit" is not typed, nor enter not clicked, it will ask again
        else:
            continue

def request():
    """Running request runs the application to complete the API requests given the user's input.
    """
    while True:

    # Input to let the user make a request
        make_a_request = input('''Greetings, please select an action:
Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View your account info. (GET)
3) Update an existing task (PUT)
4) Delete a task (DELETE)
''')

        # POST request
        if make_a_request == '1':
            print('Great, I will help you make an account.')
            time.sleep(1)
            first = input('What is your first name? ')
            last = input('What is your last name? ')
            email = input('What is your email address? ')
            new_account(first, last, email)
            quit()

        # GET request
        if make_a_request == '2':
            print('I can help you view your account information but will need some information from you.')
            time.sleep(1)
            email = input('What is your email address? ')
            view_account_info(email)
            quit()

        # PUT request
        if make_a_request == '3':
            print("I can help update your account information.")
            email = input('Let me find your account information. What is your email address? ')
            update_account(email)
            quit()

        # DELETE request
        if make_a_request == '4':
            print('You would like to delete your account. To do so I can look up your account based on your email address.')
            time.sleep(1)
            email = input('What is your email address? ')
            delete_task(email)
            quit()

        else:
            continue


request()