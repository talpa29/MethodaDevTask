from flask import Flask, jsonify, request 
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})


Statuses = [
    {
    'id' : uuid.uuid4().hex,
    'name' : 'gever',
    'type' : 'orphan',
    }
]

Transitions = [
    {
    'id' : uuid.uuid4().hex,
    'name' : 've',
    'from' : 'gevveer',
    'to' : 'gegeg',
    }
]


@app.route('/', methods=['GET', 'POST'])
def all_status():
    response_object = {'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        if post_data.get('type') != '':
            Statuses.append({
                'id' : uuid.uuid4().hex,
                'name': post_data.get('name'),
                'type': post_data.get('type')})
            response_object['message'] = 'Status Added!'
        else:
            Transitions.append({
                'id' : uuid.uuid4().hex,
                'name': post_data.get('name'),
                'from': post_data.get('from'),
                'to': post_data.get('to')})
            response_object['message'] = 'Transition Added!'
    else:
        response_object['Statuses'] = Statuses
        response_object['Transitions'] = Transitions
    return jsonify(response_object)


#PUT and DELETE route handler
@app.route('/<status_id>', methods=['PUT','DELETE'])
def single_status(status_id):
    print("HEREEEEE1\n")
    response_object = {'status':'success'}
    if request.method == 'PUT':
        print(post_data)
        print("HEREEEEE2\n")
        post_data = request.get_json()
        print("putt print \n")
        remove_status(status_id)
        Statuses.append({
            'id' : uuid.uuid4().hex,
            'name': post_data.get('name'),
            'type': post_data.get('type')})
        response_object['message'] = 'Status updated!'
    if request.method == 'DELETE':
        print("HEREEEEE3\n")
        post_data = request.get_json()
        print(post_data)
        print("heree\n")
        if post_data.get('type') != '':
            remove_status(status_id)
            response_object['message'] = 'Status Removed!'
        else:
            remove_transition(status_id)
            response_object['message'] = 'Transition Removed!'
    return jsonify(response_object)

def remove_status(status_id):
    for status in Statuses:
        if status['id'] == status_id:
            Statuses.remove(status)
            return True
        
def remove_transition(transition_id):
    for transition in Transitions:
        if transition['id'] == transition_id:
            Transitions.remove(transition)
            return True
    return False






if __name__ == "__main__":
    app.run(debug=True)
