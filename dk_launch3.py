

import os
import time

str1 = "THEANO_FLAGS=device=gpu" 
str2 = ",floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/dk_run.py train "
savepath = '/work/capybara/results/wsj/'
str4 = ' /home/capybara/attention-lvcsr/exp/wsj/configs/'

fnames = []
fnames += ['wsj_paper6']
#fnames += ['wsj_paper6_noise_05']
fnames += ['wsj_paper6_no_max_norm']
fnames += ['wsj_paper6_noise_05_no_max_norm']
fnames += ['dk_wsj_paper6']
#fnames += ['dk_wsj_paper6_noise_05']
fnames += ['dk_wsj_paper6_no_max_norm']
# DIED??
fnames += ['dk_wsj_paper6_noise_05_no_max_norm']

for n in range(6):
    old_fname = fnames[n]
    new_fname = old_fname + '_continue'
    launch_str = str1 + str(n) + str2 + "--params=" + savepath + old_fname + "/main.zip " + savepath + new_fname + str4 + old_fname + '.yaml &'
    print launch_str
    os.system(launch_str)
    time.sleep(100)


