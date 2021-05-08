from flask_restful import Resource

habilidades = ['Python', 'Java', 'PHP', 'MySql', 'Ruby']

class Habilidades(Resource):
    def get(self):
        return habilidades