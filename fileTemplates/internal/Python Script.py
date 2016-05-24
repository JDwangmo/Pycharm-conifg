#encoding=utf8
__author__ = '${USER}'
__date__ = 'create date: ${YEAR}-${MONTH}-${DAY}'
import numpy as np
import pandas as pd
import logging
import timeit
import yaml
logging.basicConfig(filename='${YEAR}${MONTH}${DAY}.log',filemode = 'w',format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
config = yaml.load(file('./config.yaml'))
config = config['']
print 'start running!'
start_time = timeit.default_timer()
logging.debug(config['describe'])




end_time = timeit.default_timer()
print 'end! Running time:%ds!'%(end_time-start_time)
