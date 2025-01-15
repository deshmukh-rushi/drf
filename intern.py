import requests
import json

URL = "http://127.0.0.1:8000/drf/iapi/"

def get_data(intern_id = None):
    data = {}
    if intern_id is not None:
        data = {'intern_id':intern_id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)

#get_data()



def post_data():
    data = {
        'intern_id': 4,
        'intern_name': 'Samyak',
        'intern_city': 'Dharashiv',
        'intern_phone' : '30345678',
            }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)
post_data()



def update_data():
    data = {
        'intern_id': 2,
        'intern_name': 'Rahul',
        # 'roll' : 104,
        # 'city': 'Thane'
            }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)
#update_data()


def update_partial_data():
    data = {
        'intern_id': 2,
        'intern_name': 'Rahul',
        # 'roll' : 104,
        # 'city': 'Thane'
            }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.patch(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)
#update_partial_data()

def delete_data():
    data = {
        'intern_id': 3
            }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)
#delete_data()
