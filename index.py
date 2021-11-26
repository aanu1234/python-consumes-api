import requests
# import json
import pprint

response = requests.get('https://api.github.com/users')

json_parsed = pprint.pformat(response.json())
# print(json.dumps(json_parsed, indent=4, sort_keys=True))
# print(response.json()[])
print(json_parsed)