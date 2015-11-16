
import os
import cPickle as pickle

def pyload(filepath):
    with open(filepath, 'rb') as file_:
        return pickle.load(file_)

basedir = '/work/capybara/results/wsj/'
print basedir

for dir in os.listdir(basedir):
    print "\n", dir
    try:
        print len(pyload(basedir + dir + '/pretraining_log.zip'))
    except:
        print "NONE!"
    try:
        print len(pyload(basedir + dir + '/main_log.zip'))
    except:
        print "NONE!"
    try:
        print len(pyload(basedir + dir + '/annealing1_log.zip'))
    except:
        print "NONE!"
    try:
        print len(pyload(basedir + dir + '/annealing2_log.zip'))
    except:
        print "NONE!"
