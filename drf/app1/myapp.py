import requests
import json

URL = "http://127.0.0.1:8000/drf/sapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,data = json_data)
    data = r.json()
    print(data)

#get_data(1)



def post_data():
    data = {
        'name': 'Aditya',
        'roll': 103,
        'city': 'Latur'
            }
    json_data = json.dumps(data)
    r = requests.post(url = URL,data = json_data)
    data = r.json()
    print(data)
post_data()



def update_data():
    data = {
        'id': 2,
        'name': 'Rahul',
        # 'roll' : 104,
        # 'city': 'Thane'
            }
    json_data = json.dumps(data)
    r = requests.put(url = URL,data = json_data)
    data = r.json()
    print(data)
#update_data()


def delete_data():
    data = {
        'id': 3
            }
    json_data = json.dumps(data)
    r = requests.delete(url = URL,data = json_data)
    data = r.json()
    print(data)
#delete_data()
