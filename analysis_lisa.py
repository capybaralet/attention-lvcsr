

#from utils import *
import os
import cPickle as pickle
import numpy as np
from pylab import *


"""
TODO: add "False" entries....
"""



if len(sys.argv) > 1:
    paths = [sys.argv[1]]
else:
    paths = []
    if 1:
        #paths.append('/data/lisatmp3/bahdanau/wsj3/wsj_paper6/pretraining_log.zip')
        #paths.append('/data/lisatmp4/kruegerd/dk_wsj_paper6/pretraining_log.zip')
        paths.append('/data/lisatmp3/bahdanau/wsj3/wsj_paper6/main_log.zip')
        paths.append('/data/lisatmp3/bahdanau/wsj3/wsj_paper6/annealing2_log.zip')
        #paths.append('/data/lisatmp4/kruegerd/dk_wsj_paper6/main_log.zip')
        #paths.append('/data/lisatmp4/kruegerd/dk_wsj_paper6_continue/main_log.zip') # TODO: restart (bart5)
        # currently running (?) (local disk...):
        paths.append('/Tmp/kruegerd/dk_wsj_paper6_cost100unnormalized_continue/main_log.zip') # bart10
        paths.append('/Tmp/kruegerd/dk_wsj_paper6_cost100unnormalized_continue/annealing2_log.zip') # bart10
        #paths.append('/data/lisatmp4/kruegerd/dk_wsj_paper6_cost100unnormalized_continue/main_log.zip')
        #paths.append('/Tmp/kruegerd/wsj_paper6_cost100unnormalized/main_log.zip') # bart2
        #paths.append('/data/lisatmp4/kruegerd/wsj_paper6_cost100unnormalized/main_log.zip')
    if 0:
        paths.append('/data/lisatmp3/bahdanau/wsj3/wsj_paper6/annealing1_log.zip')
        paths.append('/Tmp/kruegerd/dk_wsj_paper6/annealing1_log.zip')
        paths.append('/data/lisatmp3/bahdanau/wsj3/wsj_paper6/annealing2_log.zip')
        paths.append('/Tmp/kruegerd/dk_wsj_paper6/annealing2_log.zip')

labels = []
all_valid_results = []
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

        all_valid_results.append(valid_results)

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

