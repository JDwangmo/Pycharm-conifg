#encoding=utf8
__author__ = '${USER}'
__date__ = 'create date: ${YEAR}-${MONTH}-${DAY}'
import numpy as np
import pandas as pd
import logging
import timeit
import yaml
config = yaml.load(file('./config.yaml'))
config = config['']
logging.basicConfig(filename=config['log_file_path'],filemode = 'w',format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
start_time = timeit.default_timer()
print config['describe']
print 'start running!'
logging.debug(config['describe'])
logging.debug('start running!')




end_time = timeit.default_timer()
print 'end! Running time:%ds!'%(end_time-start_time)
