import json


def list_sities():
    cities = []
    open_file ='static/json/by.json'
    with open(open_file) as my_file:
        data = json.loads(my_file.read())
        for i in data:
            cities.append(i['city'])
    return cities
