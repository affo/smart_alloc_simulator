# The real simulation
if __name__ == '__main__':
	from sim.utils import HISTORY_FILE, LOG_FILE, logger
	from sim.utils.sim_file_gen import CMDS 
	import json

	cmds_list = []
	with open(HISTORY_FILE, 'r') as f:
		data = json.load(f)
		#TODO use cfg to create PMs and so on so forth
		def mapping_fn(cmd_string):
			keyword = cmd_string.split(' ')[0]
			return CMDS[keyword]().get_concrete_command(cmd_string)

		cmds_list = map(mapping_fn, data['history'])

	def do_sim():
		for cmd in cmds_list:
			cmd.execute()

	logger.info('Simulation started')
	do_sim()
	logger.info('Simulation ended')
	print 'Simulation ended! Results in ' + LOG_FILE