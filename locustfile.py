from locust import HttpLocust, TaskSet, task, TaskSequence, seq_task
import time

class MyTaskSequence(TaskSequence):
	@seq_task(1)
	def list_inventory(self):
		self.client.get("/catalog")
		time.sleep(1.0)

	@seq_task(2)
	@task(3)
	def view_item_details(self):
		self.client.get("/details/5c1258cfcaf5690001b1e9e5")
		time.sleep(2.5)

	@seq_task(3)
	def create_order(self):
		# time.sleep(5.0)
		data = {'name': 'Anastasiia-locust', \
		'items': ['5c1258cfcaf5690001b1e9e5', '5c1258dbcaf5690001b1e9e6'], \
		'address': 'Skelleftea'}
		response = self.client.post("/purchase", json=data)
		time.sleep(0.5)

	@seq_task(4)
	def view_order(self):
		self.client.get("/view-order/5c125add99e18f00014b6aed")
		time.sleep(1.5)

	@seq_task(5)
	def view_tracking(self):
		self.client.get("/track/5c1259cfcf478e0001d83acc")
		time.sleep(0.5)

class MyLocust(HttpLocust):
	task_set = MyTaskSequence
	min_wait = 1000
	max_wait = 1000