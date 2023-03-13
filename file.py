import json

def get_file():
    with open('objectives.json') as fp:
        return json.loads(fp.read()) 

def write_file(dataTraining):
    object_to_json = json.dumps(dataTraining)
    with open('objectives.json','w') as fp:
        fp.write(object_to_json)