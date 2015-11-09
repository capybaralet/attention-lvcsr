

import os
import time

os.system("THEANO_FLAGS=device=gpu0,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/run.py train /work/capybara/results/wsj/wsj_paper6 /home/capybara/attention-lvcsr/exp/wsj/configs/wsj_paper6.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu1,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/run.py train /work/capybara/results/wsj/wsj_paper6_noise_05 /home/capybara/attention-lvcsr/exp/wsj/configs/wsj_paper6_noise_05.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu2,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/run.py train /work/capybara/results/wsj/wsj_paper6_no_max_norm /home/capybara/attention-lvcsr/exp/wsj/configs/wsj_paper6_no_max_norm.yaml &")
time.sleep(50)
os.system("THEANO_FLAGS=device=gpu3,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/run.py train /work/capybara/results/wsj/wsj_paper6_noise_05_no_max_norm /home/capybara/attention-lvcsr/exp/wsj/configs/wsj_paper6_noise_05_no_max_norm.yaml &")
time.sleep(50)
if 1:
    os.system("THEANO_FLAGS=device=gpu4,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/run.py train /work/capybara/results/wsj/dk_wsj_paper6 /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6.yaml &")
    time.sleep(50)
    os.system("THEANO_FLAGS=device=gpu5,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/run.py train /work/capybara/results/wsj/dk_wsj_paper6_noise_05 /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_noise_05.yaml &")
    time.sleep(50)
    os.system("THEANO_FLAGS=device=gpu6,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/run.py train /work/capybara/results/wsj/dk_wsj_paper6_no_max_norm /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_no_max_norm.yaml &")
    time.sleep(50)
    os.system("THEANO_FLAGS=device=gpu7,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/run.py train /work/capybara/results/wsj/dk_wsj_paper6_noise_05_no_max_norm /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_noise_05_no_max_norm.yaml &")
    time.sleep(50)


