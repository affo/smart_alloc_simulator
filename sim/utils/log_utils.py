from oslo.config import cfg
import logging

log_group = cfg.OptGroup(name='logs')
log_opts = [
	cfg.StrOpt(
		'sim_log_file',
		default= 'logs/sim.log',
		help='Simulation log file'
	),
	cfg.StrOpt(
		'compute_log_file',
		default='logs/compute.log',
		help='Compute log file'
	),
	cfg.StrOpt(
		'scheduler_log_file',
		default='logs/scheduler.log',
		help='Scheduler log file'
	),
]
CONF = cfg.CONF
CONF.register_group(log_group)
CONF.register_opts(log_opts, log_group)

def setup_logger(name, file_name):
	logger = logging.getLogger(name)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fileHandler = logging.FileHandler(file_name, mode='w')
	fileHandler.setFormatter(formatter)
	streamHandler = logging.StreamHandler()
	streamHandler.setFormatter(formatter)

	logger.setLevel(logging.INFO)
	logger.addHandler(fileHandler)
	logger.addHandler(streamHandler)