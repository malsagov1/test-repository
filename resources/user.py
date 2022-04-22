from flask_restful import Resource, reqparse
from models.user import UserModel
import sqlite3


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True,
    help = "This field can not be left blank"
        )
    parser.add_argument('password',
    type = str,
    required = True,
    help = "This field can not be left blank"
        )
    
    def post (self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User with this name already exists"}, 400
            
        user = UserModel(**data) #** unpacks dictionary values into separate values
        user.save_to_db()

        return {'message':"User is reated successfully"}, 201

