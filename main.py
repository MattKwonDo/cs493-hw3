from google.cloud import datastore
from flask import Flask, request
import json
import constants

app = Flask(__name__)
client = datastore.Client()

@app.route('/')
def index():
    return "Please navigate to /slips to use this API"\

@app.route('/slips', methods=['POST','GET'])
def slips_get_post():
    if request.method == 'POST':
        content = request.get_json()
        if "number" in content:
            new_slip = datastore.entity.Entity(key=client.key(constants.slips))
            # None ~= Null in python
            new_slip.update({"number": content["number"], "current_boat": None})
            print(new_slip) # <Entity('slips', 5746980898734080) {'number': 1}>
            client.put(new_slip)
            # putResult = client.put(new_slip) # print(putResult) == "None"
            # need to return object and also append the id to the object, 
            # append ex was in one of lectures I think
            # return (f"{new_slip.key.id}",201)
            query = client.query(kind=constants.slips)
            results = list(query.fetch())
            
            # slip_num = new_slip['number']
            # print(str(slip_num)) # == 1
            slip_key = client.key(constants.slips, new_slip.key.id)
            print(str(slip_key))
            slip = client.get(key=slip_key)
            
            # for e in slip:
            slip["id"] = new_slip.key.id
            slip["self"] = str(request.url_root) + 'slips/' + str(new_slip.key.id)
            return (json.dumps(slip), 201)
        else:
            return (json.dumps({"Error": "The request object is missing the required number"}), 400)
    elif request.method == 'GET':
        query = client.query(kind=constants.slips)
        results = list(query.fetch())
        for e in results:
            e["id"] = e.key.id
        return json.dumps(results)
    else:
        return 'Method not recognized'

@app.route('/slips/<id>', methods=['PUT','DELETE','GET'])
def slips_put_delete(id):
    if request.method == 'PUT':
        content = request.get_json()
        slip_key = client.key(constants.slips, int(id))
        slip = client.get(key=slip_key)
        slip.update({"name": content["name"], "description": content["description"],
          "price": content["price"]})
        client.put(slip)
        return ('',200)
    elif request.method == 'DELETE':
        key = client.key(constants.slips, int(id))
        client.delete(key)
        return ('',200)
    elif request.method == 'GET':
        slip_key = client.key(constants.slips, int(id))
        slip = client.get(key=slip_key)
        return json.dumps(slip)
    else:
        return 'Method not recognized'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)