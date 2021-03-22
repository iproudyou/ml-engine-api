import json
from flask import request, jsonify, make_response
from flask_cors import CORS

from app import create_app, database
from app.models import Cats
from app.helpers import encode_auth_token, decode_auth_token, is_unauthorized
from app.helpers.logger import logger

app = create_app()

# auth api token
# @app.before_request
def server_api_auth():
    try:
        if 'x-api-token' in request.headers:
            token = request.headers['x-api-token']
            decode_auth_token(token)
            logger.debug('ML-ENGINE-API SUCCESSFULLY ACCESSED')
        else:
            raise Exception('x-api-token not found')
    except Exception as e:
        logger.error(f'Error while authenticating API TOKEN: {e}')
        return is_unauthorized()

# override 404 error handler
@app.errorhandler(404)
def resource_not_found(error):
    """This will be response returned if the user attempts to access
    a non-existent respurce or url"""

    response_payload = dict(
        message = 'The requested URL was not found on the server.'
    )
    return make_response(jsonify(response_payload), 404)
    
    
@app.route('/', methods=['GET'])
def welcome_loco():
    return jsonify({'message': 'Welcome K-POP LOCO'})

@app.route('/all', methods=['GET'])
def fetch():
    cats = database.get_all(Cats)
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)

    return json.dumps(all_cats), 200

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    database.add_instance(Cats, name=name, price=price, breed=breed)
    return json.dumps("Added"), 200

@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200

@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)


