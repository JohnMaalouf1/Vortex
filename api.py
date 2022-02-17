from flask import Flask
from flask_restful import Api, Resource
from Server import *

app = Flask(__name__)
api = Api(app)

class Vortex(Resource):
	def get(self):
		return {"data": check_if_file_exists()}

api.add_resource(Vortex, "/check_files")

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
