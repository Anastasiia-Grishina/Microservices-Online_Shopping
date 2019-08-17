from flask_restful import Resource
from front import app
from flask import jsonify, request
from datetime import datetime
from bson import json_util, ObjectId
import requests


inventory_api = 'http://inventory:5000'
tracking_api = 'http://tracking:5000'
ordering_api = 'http://ordering:5000'


    # "_id": "5c0813ff64e9ae0001cf59ef",
    # "bill": 759,
    # "creation_date": 1544033279,
    # "delivery_id": "5c0813ffee77180001d07679"


@app.route('/catalog')
def catalog():
	r = requests.get(inventory_api + '/items', json={'available': True})

	return jsonify(r.json())



@app.route('/purchase', methods=['POST'])
def purcahse():
	data = request.get_json()

	params = {'name': data['name'], 'items': data['items'], 'address': data['address']}

	r = requests.post(ordering_api + '/orders', json=params)

	return jsonify(r.json())


@app.route('/view-order')
def view_order():
	data = request.get_json()

	r = requests.get(ordering_api + '/orders/{}'.format(data['order-id']))

	return jsonify(r.json())


@app.route('/track')
def track_order():
	data = request.get_json()

	r = requests.get(tracking_api + '/tracking/{}'.format(data['tracking-id']))

	return jsonify(r.json())