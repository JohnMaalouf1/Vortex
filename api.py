from flask import Flask
from flask_restful import Api, Resource
from Server import *

app = Flask(__name__)
api = Api(app)

class check_file_exists(Resource):
	def get(self):
		return {"data": check_if_file_exists()}

class check_file_hierarchy(Resource):
	def get(self):
		return {"data": check_server_file_hierarchy()}




api.add_resource(check_file_exists, "/check_file_exists")
api.add_resource(check_file_hierarchy, "/check_file_hierarchy")


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
