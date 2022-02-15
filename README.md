# API Account Manager

The API Account Manager is a command-line application to help you create or maintain an account with CodingNomad's demo API site.

## Imports

```python
import requests # To call the API
import time # For the user interface
```

## Usage

To call the API and return JSON data:
```python
url = 'http://demo.codingnomads.co:8080/tasks_api/users'
response = requests.get(url)
data = response.json() # Dict of list of data
```
What the data looks like, including a few accounts:
```javascript
{
data: [
  {
    id: 1,
    email: "harry@potter.com",
    first_name: "Harry",
    last_name: "Potter",
    created_at: 1642541428000,
    updated_at: 1644020694000
  },
  {
    id: 2,
    email: "ccallow1@xinhuanet.com",
    first_name: "Corrinne",
    last_name: "Callow",
    created_at: 1642541428000,
    updated_at: 1642541428000
  },
  {
    id: 3,
    email: "nwolland2@over-blog.com",
    first_name: "Niall",
    last_name: "Wolland",
    created_at: 1642541428000,
    updated_at: 1642541428000
  },

...

error: {
    message: "none"
  },
status: "200 OK"
}
```

To access all account data as individual dictionaries, you must iterate or index through the data:
```python
for account in data['data']:
  # access account information
```
Or
```python
account = data['data']
```


### POST request - Create a new account
If '1' is entered upon running the program, it will create a new account for the user based on the credentials asked:
```python
first = input('What is your first name? ')
last = input('What is your last name? ')
email = input('What is your email address? ')
```
Once the input has been given, the program will run the ```new_account(first, last, email)``` function:

```python
body = {
'first_name': first,
'last_name': last,
'email': email,
}

response = requests.post(url, json=body)
```
Based on the credentials, the API will post a new account. It will return a ```400``` error if the email already exists. The ID will be automatically given and is also unique. 

### GET request - View account information
If '2' is entered upon running the program, it will create a new account for the user based on email inputted:

```python
email = input('What is your email address? ')
```
Once the input has been given, the program will run the ```view_account_info(email)``` function and if the email address can be found in the system, it will be returned and printed:
```python
info = []
...
for account in data['data']:
      if account['email'] == email:
          info.append(account)
...
elif info[0]:
      print("Here is the info for the account associated with your email address: \n")
      print(account) # Returns JSON data for the account
```
Otherwise the function will return no account or a 400 error:
```python
if info == []:
      print("It doesn't appear you have an account based on the email address provided. Try again or try creating one with option 1.")
      quit()
...
else:
      response.status_code = 400
      print(response.status_code)
      print('Sorry there appears to be an error. Please try again.')
```

### PUT request - Edit account information
If '3' is entered upon running the program, it will create a new account for the user based on email inputted:



### DELETE request - Delete account 

## References
[CodingNomads Python Web Development](https://codingnomads.co/career-track/professional-python-web-development-course)
