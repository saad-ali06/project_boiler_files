import requests
def request_func():
    # Replace this URL with the actual URL you want to request
    url = 'https://jsonplaceholder.typicode.com/todos/1'

    # Making a GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the content of the response (assumes it's JSON in this example)
        print("Response JSON:")
        print(response.json())
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")
