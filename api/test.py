from index import handler

# Simulate a request to the root path
request = {
    'path': '/'
}
context = {}

# Call the handler function
response = handler(request, context)

# Print the status code and headers
print(f"Status Code: {response.get('statusCode')}")
print(f"Headers: {response.get('headers')}")
print("First 200 chars of body:")
print(response.get('body')[:200] + "...")

# Test API path
api_request = {
    'path': '/api/france'
}

# Call the handler function for API
api_response = handler(api_request, context)

# Print the API response
print("\nAPI Response:")
print(f"Status Code: {api_response.get('statusCode')}")
print(f"Headers: {api_response.get('headers')}")
print("First 100 chars of body:")
print(api_response.get('body')[:100] + "...") 