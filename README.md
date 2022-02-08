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
To access all account data as individual dictionaries, you must iterate or index through the data:
```python
for account in data['data']:
  # access account information
```
Or
```python
account = data['data']
```



# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## References
[CodingNomads Python Web Development](https://codingnomads.co/career-track/professional-python-web-development-course)
