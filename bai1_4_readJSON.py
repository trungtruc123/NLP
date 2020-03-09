import requests
import json
#json from "https://quotes.rest/qod.json"
r = requests.get("https://quotes.rest/qod.json")
res = r.json()
print(json.dumps(res, indent = 4))
# #extract contents
#  q = res['contents']['quotes'][0]

# #extract only quote
# print(q['quote'], '\n--', q['author'])