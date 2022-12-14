from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(all_directors)

        return result, 200


@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    def get(self, uid: int):
        director = director_service.get_one(uid)
        result = DirectorSchema().dump(director)

        return result, 200
