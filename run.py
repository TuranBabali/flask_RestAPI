from api import create_app
from flask import jsonify, request

app=create_app()


tutorials = [
    {
        'id': '1',
        'title': 'Video 1',
        'description': 'GET , POST routes'  
    },
    {
        'id': '2',
        'title': 'Video 2',
        'description': 'PUT , DELETE routes'  
    }
]

client = app.test_client()

from api.tutorials.models import * 

@app.route('/tutorials',methods=['GET'])
def get_or_update_list():
    if request.method=='GET':
        return jsonify(tutorials)
    
@app.route('/tutorials',methods=['POST'])
def update_list():
    new_one= request.json
    tutorials.append(new_one)
    return jsonify(tutorials)


@app.route('/tutorials/<int:tutorial_id>',methods=['PUT'])
def update_tutorial(tutorial_id):

    item= next((x for x in tutorials if x['id'] == tutorial_id), None)
    params= request.json
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    
    item.update(params)
    return item


@app.route('/tutorials/<int:tutorial_id>',methods=['DELETE'])
def delete_tutorial(tutorial_id):

    idx, _ = next((x for x in enumerate(tutorials)
                   if x[1]['id'] == tutorial_id), (None, None))
    
    tutorials.pop(idx )
    return "", 204 
     
    
    
       








if __name__ == '__main__':
    app.run(debug=True)
