import requests

response = requests.get("https://www.bbc.co.uk/iplayer/live/bbws")
# API call to bbc to get response


# # if the web-page status code is live welcome the user with the status
# if response.status_code == 200: # if true execute the next line - if false execute the next/else block
#     print(f"The status code is {response.status_code} Welcome to BBC ")
#     #print(type(response.content)) # get the content from the web-app/endpoint
#     # find a way to change this type to json or dict or list or any type which we could
#     # iterate through with loops
#     #print(response.headers.values())
# # or print a messages OOPs something went wrong
# # should give us the status code only - numbers 200 - 404 -501 etc
# elif response.status_code == 404:
#     print(f"The site is unavailable until further notice the status code is {response.status_code} Please try later")
# else:
#     print(f"OOPs something went wrong the status code is {response.status_code} Please try later")

# second iteration -
if response: # what is it checking
    print("success")
elif response.status_code == 404: # what is it checking
    print("unsuccessfull")

else: # what is it checking
    print(f" OOps something went wrong please try later the status code is {response.status_code}")

# requests goes one step further in simplifying this process for us.
# If you use a response_bcc instance in a conditional expression,
# It will evaluate to True if the status code was between 200 and 400, and False otherwise.
# Therefore, you can simplify the last example by rewriting the if statement as above:

# Third Iteration
# Create a function that returns the status code with appropriate message
# use control flow to make the right decision
# USE RETURN not print inside your function









