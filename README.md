# API
## Python API
### What is an API
#### benefits of API
##### install requests

- pip install package_name `pip install requests`

```python
import requests

response = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")

print(response)
```

- Second Iteration
```python
import requests

response = requests.get("https://www.bbc.co.uk/iplayer/live/bbws")


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
```