from oslo import messaging
from oslo.config import cfg
from sim.nova import rpc
# as they do in OpenStack
rpcapi_opts = [
	cfg.StrOpt(
		'compute_topic',
		default='compute',
		help='The topic compute nodes listen on'
	),
]

CONF = cfg.CONF
CONF.register_opts(rpcapi_opts)

class ComputeTaskAPI(object):
	def __init__(self):
		super(ComputeTaskAPI, self).__init__()
		self.client = rpc.get_client(CONF.compute_topic)

	def build_instance(self, id, flavor, smart=False):
		# wait to have synchronous calls
		self.client.call({'smart': smart}, 'build_instance', id=id, flavor=flavor)

	def delete(self, id, smart=False):
		# wait to have synchronous calls 
		self.client.call({'smart': smart}, 'delete', id=id)

	def resize(self, id, flavor, smart=False):
		return self.client.call({'smart': smart}, 'resize', id=id, flavor=flavor)
	
	def live_migrate(self, vm_id, flavor, host_id, smart=False):
		self.client.call({'smart': smart}, 'live_migrate', vm_id=vm_id, flavor=flavor, host_id=host_id)

