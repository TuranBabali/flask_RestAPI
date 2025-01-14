from api import create_app
from flask import jsonify, request

app=create_app()


tutorials = [
    {
        'title': 'Video 1',
        'description': 'GET , POST routes'  
    },
    {
        'title': 'Video 2',
        'description': 'PUT , DELETE routes'  
    }
]

client = app.test_client()


@app.route('/tutorials',methods=['GET'])
def get_or_update_list():
    if request.method=='GET':
        return jsonify(tutorials)
    else:
        new_one = request.json
        tutorials.append(new_one) 
        return jsonify(tutorials)








if __name__ == '__main__':
    app.run(debug=True)
