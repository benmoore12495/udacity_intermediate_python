import requests
import json

post = requests.post('https://ssd-api.jpl.nasa.gov/cad.api?date-min=1900-01-01&date-max=2100-01-01&dist-max=1')
json_data = json.loads(post.text)


with open("cad.json", "w") as outfile:
    json.dump(json_data, outfile)
