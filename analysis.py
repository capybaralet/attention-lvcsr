

#from utils import *
import os
import cPickle as pickle
import numpy as np
from pylab import *

basedir = os.path.join(os.environ['SAVE_PATH'], 'wsj')
paths = []

for dir in os.listdir(basedir):
    if 'wsj' in dir:
        paths.append(os.path.join(basedir, dir, 'main_log.zip'))

labels = []
for path in paths:
    print path
    if 1:#try:
        with open(path, 'rb') as f_:
            log = pickle.load(f_)
        print "len(log.keys()) =", len(log.keys())
        loglen = len(log.keys())

        strs = ['valid_per', 'valid_sequence_log_likelihood', 'sequence_log_likelihood']
        results = []

        def search_log(log, str):
            """ Returns a list extracted from the log"""
            rval = []
            for kk in log.keys():
                entry = log[kk]
                try:
                    rval.append(entry[str])
                except:
                    pass
            return rval

        for str in strs:
            results.append(search_log(log, str))

        def get_all_keys(log):
            keys = []
            for kk in log.keys():
                entry = log[kk]
                for key in entry.keys():
                    if not key in keys:
                        keys.append(key)
            return keys

        keys = get_all_keys(log)
        valid_keys = [k for k in keys if 'valid' in k]

        valid_results = []
        for key in valid_keys:
            res = search_log(log, key)
            valid_results.append(res)
            print key, ":    length =", len(res)

        figure(51)
        plot(results[0])
        figure(52)
        plot(results[1])
        figure(53)
        plot(results[2][::100])
        labels.append(path)

    if 0:#except Exception:
        print '\n'
        print "could not load???", path
        print Exception
        print '\n'


    legend(labels)

