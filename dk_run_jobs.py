

import os
import time

#os.system("THEANO_FLAGS=device=gpu0,lib.cnmem=0 $LVSR/bin/run.py train /work/capybara/results/wsj/wsj_paper6 /home/capybara/attention-lvcsr/exp/wsj/configs/wsj_paper6.yaml &")
#time.sleep(50)
os.system("THEANO_FLAGS=device=gpu1,lib.cnmem=0 $LVSR/bin/run.py train /work/capybara/results/wsj/wsj_paper6_noise_05 /home/capybara/attention-lvcsr/exp/wsj/configs/wsj_paper6_noise_05.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu2,lib.cnmem=0 $LVSR/bin/run.py train /work/capybara/results/wsj/wsj_paper6_no_max_norm /home/capybara/attention-lvcsr/exp/wsj/configs/wsj_paper6_no_max_norm.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu3,lib.cnmem=0 $LVSR/bin/run.py train /work/capybara/results/wsj/wsj_paper6_noise_05_no_max_norm /home/capybara/attention-lvcsr/exp/wsj/configs/wsj_paper6_noise_05_no_max_norm.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu4,lib.cnmem=0 $LVSR/bin/run.py train /work/capybara/results/wsj/dk_wsj_paper6 /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu5,lib.cnmem=0 $LVSR/bin/run.py train /work/capybara/results/wsj/dk_wsj_paper6_noise_05 /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_noise_05.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu6,lib.cnmem=0 $LVSR/bin/run.py train /work/capybara/results/wsj/dk_wsj_paper6_no_max_norm /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_no_max_norm.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu7,lib.cnmem=0 $LVSR/bin/run.py train /work/capybara/results/wsj/dk_wsj_paper6_noise_05_no_max_norm /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_noise_05_no_max_norm.yaml &")
time.sleep(50)


