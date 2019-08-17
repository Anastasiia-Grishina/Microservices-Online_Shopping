from flask_restful import Resource
from tracking import api
from flask import jsonify, request
from datetime import datetime
from bson import json_util, ObjectId


from tracking.helper import pretty
from tracking.models import Delivery


class TrackingList(Resource):
	# create new tracking entry
	def post(self):
		data = request.get_json()

		delivery = Delivery(destination=data['destination'], order_id=data['order_id'])
		delivery.save()

		return jsonify(pretty(delivery))

	# get all tracking, for admin purposes
	def get(self):
		data = request.get_json()

		query = {}
		if 'active' in data and data['active'] is True:
			query = { 'status': { '$ne': 'delivered'} }

		deliveries = Delivery.objects.raw(query)

		return jsonify(pretty(deliveries))


class TrackingE (Resource):
	
	# get tracking info
	def get(self, delivery_id):
		delivery = Delivery.objects.get({ '_id': ObjectId(delivery_id) })
		delivery.to_son()

		return jsonify(pretty(delivery))

	# update tracking status
	def put(self, delivery_id):
		data = request.get_json()

		delivery = Delivery.objects.get({ '_id': ObjectId(delivery_id) })

		delivery.status = data['status']

		delivery.save()

		return jsonify(pretty(delivery))


api.add_resource(TrackingList, '/tracking')
api.add_resource(TrackingE, '/tracking/<delivery_id>')