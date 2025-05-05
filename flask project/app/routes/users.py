from flask import Blueprint, jsonify, request 
from app.models.user import User
from app import db 

users_bp = Blueprint('users', __name__, url_prefix='/api')

@users_bp.route('/')
def home():
    return jsonify({'message':'Hello from home route'}),200 



# -------------- GET ---------------
@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])



# ---------------- GET by ID ---------------
@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)

    if not user:
        return jsonify({'Error':'User not found'})
    return jsonify(user.to_dict()), 200





# -------------- POST ---------------
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({'Error':'Name required to create a user'})
    
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201




# ------------- PUT --------------
@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)

    if not user:
        return jsonify({'error': 'User not found'}), 404 
    
    if not data or 'name' not in data:
        return jsonify({'error':'Name is required to update'}), 400
    
    user.name = data['name']
    db.session.commit()

    return jsonify(user.to_dict()),200



# --------------- DELETE -----------
@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    if not user:
        return jsonify({'Error':'User not found'}), 404 
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({'Message':'User deleted successfully'}), 200
