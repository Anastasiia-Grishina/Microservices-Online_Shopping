from flask_restful import Resource
from inventory import api
from flask import jsonify, request
from datetime import datetime
from bson import json_util, ObjectId
import json


from inventory.helper import pretty
from inventory.models import Item


class ItemList(Resource):

	# get items list
	def get(self):

		data = request.get_json()

		min_availability = 0
		if 'available' in data and data['available'] is True:
			min_availability = 1

		return jsonify(pretty(Item.objects.raw({ "availability": { "$gte" : min_availability } }).all()))

	# add new item
	def post(self):
		data = request.get_json()

		item = Item(name=data['name'], category=data['category'], price=data['price'], updated_on=datetime.now())

		item.save()

		return jsonify(pretty(item))

class ItemE(Resource):

	# get item details
	def get(self, item_id):

		item = Item.objects.get({ "_id": ObjectId(item_id) })
		item.to_son()

		# print(item._data._python_data)

		return jsonify(pretty(item))

	# update availability
	def put(self, item_id):
		data = request.get_json()

		item = Item.objects.get({ "_id": ObjectId(item_id) })

		item.updated_on = datetime.now()
		item.availability = data['availability']
		item.save()

		return jsonify(pretty(item))



api.add_resource(ItemList, '/items')
api.add_resource(ItemE, '/items/<item_id>')