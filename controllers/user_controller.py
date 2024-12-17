from flask import request, jsonify,Blueprint

from models.user import User

# 创建一个名为 'user_bp' 的蓝图，设置前缀为 '/users'
user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

def add_user():
    print(jsonify({"id": 1}))
    return jsonify({"id": 1, "name": "test"}), 200

def get_users():
    users = User.query.all()
    user_list = [{"id": user.id, "name": user.name, "phone": user.phone} for user in users]
    return jsonify(user_list), 200



@user_bp.route('',methods=['GET'])
def users_post():
    print("6666666666666")
    return add_user()