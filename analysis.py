

from utils import *

import sys
path = sys.argv[1]

#path = '/data/lisatmp3/bahdanau/wsj3/wsj_paper6/annealing2_log.zip'

log = pyload(path)
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


