from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.store import StoreModel
class Store(Resource):
    parser=reqparse.RequestParser()

    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store not Found'},404
    def post(self,name):
        if StoreModel.find_by_name(name):
            return{'message': 'Already Exists'}
        store=StoreModel(name)
        store.save_to_db()
        return store.json()
    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message':'Store Deleted'}


class StoreList(Resource):
     def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
