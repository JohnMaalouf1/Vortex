from flask import Flask
from flask_restful import Api, Resource
from Server import *
from Server_Transfer import *

app = Flask(__name__)
api = Api(app)

class check_file_exists(Resource):
	def get(self):
		return {"data": check_if_file_exists()}

class check_file_hierarchy(Resource):
	def get(self):
		return {"data": check_server_file_hierarchy()}

class send_server_file(Resource):
    def get(self):
    		return {"data": send_file_driver()}



api.add_resource(check_file_exists, "/check_file_exists")
api.add_resource(check_file_hierarchy, "/check_file_hierarchy")
api.add_resource(send_server_file, "/send_server_file")



if __name__ == "__main__":
	app.run(host="192.168.1.51", debug=True)
