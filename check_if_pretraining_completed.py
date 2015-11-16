
import os

def pyload(filepath):
    with open(filepath, 'rb') as file_:
        return pickle.load(file_)

basedir = '/work/capybara/results/wsj/'
for dir in os.listdir(basedir):
    try:
        log = pyload(basedir + dir + '/pretraining_log.zip')
        print dir, len(log)

    except:
        print dir, "NONE!"


