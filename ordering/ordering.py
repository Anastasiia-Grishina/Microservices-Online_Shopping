from ordering import api
from flask_restful import Resource, reqparse
from ordering.models import Order
from ordering.helper import CustomJSONEncoder, pretty
from bson import json_util, ObjectId
from flask import jsonify
import datetime
import json
import sys
import requests



parser = reqparse.RequestParser()
parser.add_argument('address')
parser.add_argument('bill', type=float)
parser.add_argument('name')
parser.add_argument('items', action='append')
parser.add_argument('_id')

class OrderEntity(Resource):
	# View order by ID
	def get(self, order_id):
		order = Order.objects.get({'_id': ObjectId(order_id)})
		order.to_son()
		return jsonify(pretty(order))

	# Delete order
	def delete(self, order_id):
		order = Order.objects.get({'_id': ObjectId(order_id)})
		order.delete()
		resp = jsonify(success=True)
		return resp

api.add_resource(OrderEntity, '/orders/<order_id>')

class OrderList(Resource):

	# Create a new order
	def post(self):
		args 	= parser.parse_args()
		name 	= args['name']
		items_id= args['items']
		destination = args['address']
		creation_date = datetime.datetime.now()

		bill = 0

		# Update items availability in inventory
		for item_id in items_id:
			resp_get_item = requests.get("http://inventory:5000/items/"+ item_id)
			data = resp_get_item.json()
			curr_availability = data['availability']
			resp_update_item = requests.put("http://inventory:5000/items/"+\
			item_id, json={'availability': curr_availability - 1})

			bill += data['price']

		# TODO: add id and delivery at saving Order

		order = Order( name=name, bill=bill, items=items_id, \
			creation_date=creation_date, destination=destination)
		order.save()

		resp_create_delivery = requests.post("http://tracking:5000/tracking", \
			json={'destination': destination, 'order_id': str(order._id)})
		print(resp_create_delivery.text, '\n\n')
		order.delivery_id = resp_create_delivery.json()['_id']
		order.save()
		return jsonify(pretty(order))

	# Get list of orders
	# Filter by user name (optional)
	def get(self):
		orders = Order.objects.all()
		try:
			args = parser.parse_args()
			name = args['name']
			orders = Order.objects.get_queryset().raw({'name': name})
			return jsonify(pretty(orders))
		except:
			pass

		return jsonify(pretty(orders))

api.add_resource(OrderList, '/orders')