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