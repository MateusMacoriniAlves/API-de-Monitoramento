from flask_restful import Resource, reqparse
from app.models.user import User


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name is required')

    def get(self, user_id=None):
        if user_id is not None:
            user = User.query.get_or_404(user_id)
            return {'id': user.id, 'name': user.name}
        else:
            users = User.query.all()
            return [{'id': user.id, 'name': user.name} for user in users]

    def post(self):
        args = self.parser.parse_args()
        user = User(name=args['name'])
        db.session.add(user)
        db.session.commit()
        return {'id': user.id, 'name': user.name}, 201

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        args = self.parser.parse_args()
        user.name = args['name']
        db.session.commit()

