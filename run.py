from api import create_app
from flask import jsonify, request
from flask_jwt_extended import JWTManager

from api.tutorials.models import Video
from api.database import db

app=create_app()

jwt= JWTManager(app)

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



@app.route('/tutorials',methods=['GET'])
def get_or_update_list():
    videos= Video.query.all()
    serialized = []
    for video in videos:
        serialized.append({
            'id': video.id,
            'name': video.name,
            'description': video.description
        }) 
    return jsonify(serialized) 
    
@app.route('/tutorials',methods=['POST'])
def update_list():
    new_one= Video(**request.json) 
    db.session.add(new_one)
    db.session.commit()
    serialized = [
        {
            'id': new_one.id,
            'name': new_one.name,
            'description': new_one.description
        }
    ]

    return jsonify(serialized)


@app.route('/tutorials/<int:tutorial_id>',methods=['PUT'])
def update_tutorial(tutorial_id):
    item= Video.query.filter(Video.id == tutorial_id).first() 
    params= request.json
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    
    for key, value in params.items():
        setattr(item, key, value) 
    db.session.commit()
    serialized = {
        'id': item.id,
        'name': item.name,
        'description': item.description
    }
    return item


@app.route('/tutorials/<int:tutorial_id>',methods=['DELETE'])
def delete_tutorial(tutorial_id):

    item= Video.query.filter(Video.id == tutorial_id).first() 
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    
    db.session.delete(item) 
    db.session.commit() 
    return "", 204 
     
    
    
       








if __name__ == '__main__':
    app.run(debug=True)
