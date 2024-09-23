import requests, json

# URL = "http://127.0.0.1:8000/createclient"
# data = {
#     'client_name':'FCT',
#     'created_at':'2024-09-24',
#     'created_by':'Prasanaa'
# }
# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
# data = r.json()
# print(data)

# URL = "http://127.0.0.1:8000/createproject"
# data = {
#     'project_name':'Fuel Delivery System',
#     'client': '6',
#     'user': 'Shree',
#     'created_at': '',
#     'created_by': 'Shree'
#
# }
# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
# data = r.json()
# print(data)

# URL = "http://127.0.0.1:8000/project_details"
# r = requests.get(url=URL)
# data = r.json()
# print(data)

URL = "http://127.0.0.1:8000/project_details"
r = requests.get(url=URL)
data = r.json()
print(data)