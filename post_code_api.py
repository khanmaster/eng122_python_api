# import the required package
import requests

# valid post-code or invalid - url of the API address
url = "http://api.postcodes.io/postcodes/"


# store the data

postcode = "e147le"
url_arg = url + postcode # ("http://api.postcodes.io/poscodes/e147le")


# display the outcome
response = requests.get(url_arg)
#print(response.status_code)
response_dict = response.json()
result_dict = response_dict['result']
for key in result_dict.keys():
    if key == "postcode":
        print(f"Please confirm this is your postcode {}") # enter values/key that would print the postcode
    print(key) #
#print(result_dict)


# please print the post code from the data received from the API call

# print longitude - and latitude
# once completed - create a function to do return the required value - 1 function MUST only REtURN 1 VALUE
# Create a function that checks if the post code is valid - prompt the user to input the postcode

# create a class with all of these functions
# create a file called postcode_checker.py
# import this file and class
# call these functions in postcode_check.py



# display url together with given postcode


# check the type of data scrapped from the web - response

# convert data type if needed to iterate through the data and print required information


# display longitude - latitude - postcode - etc.