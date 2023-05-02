from flask import Flask
from flask_restful import Resource, Api, reqparse
from random import randint
import logging

logging.basicConfig(filename='record.log', level=logging.DEBUG)

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of video", required=True)
video_put_args.add_argument("views", type=int, help="views of video", required=True)
video_put_args.add_argument("likes", type=int, help="likes of video", required=True)

videos = {}

def validate(args):
	app.logger.debug(args.name)
	if not any (args.name or args.views or args.likes):
		abort(404, message="arrguments not found")

class general(Resource):
	def get(self):
		return videos

	def put(self):
		args = video_put_args.parse_args()
		validate(args)
		randomlist = []
		rand_id =  randint(1,100)
		videos[rand_id] = args
		return videos[rand_id]


api.add_resource(general, "/general/") 

if __name__ == "__main__":
	app.run(debug=True) 
