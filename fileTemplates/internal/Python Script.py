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
logging.basicConfig(filename=''.join(config['log_file_path']),filemode = 'w',format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
start_time = timeit.default_timer()
print('='*30)
print config['describe']
print('='*30)
print 'start running!'
logging.debug('='*30)
logging.debug(config['describe'])
logging.debug('='*30)
logging.debug('start running!')
logging.debug('='*20)






end_time = timeit.default_timer()
print 'end! Running time:%ds!'%(end_time-start_time)
logging.debug('='*20)
logging.debug('end! Running time:%ds!'%(end_time-start_time))
