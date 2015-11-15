

import os
import time


if 0: # RELAUNCH!
    os.system("THEANO_FLAGS=device=gpu3,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 /home/capybara/attention-lvcsr/bin/dk_run.py train --params=/work/capybara/results/wsj/dk_wsj_paper6_no_max_norm/main.zip /work/capybara/results/wsj/dk_wsj_paper6_no_max_norm_continue /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_no_max_norm.yaml")
    time.sleep(100)
    os.system("THEANO_FLAGS=device=gpu2,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/dk_run.py train --params=/work/capybara/results/wsj/dk_wsj_paper6_cost300unnormalized/pretraining.zip /work/capybara/results/wsj/dk_wsj_paper6_cost300unnormalized_continue /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_cost300unnormalized_continue.yaml &")

elif 1: # RELAUNCH...
    os.system("THEANO_FLAGS=device=gpu0,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/dk_run.py train --params=/work/capybara/results/wsj/dk_wsj_paper6_cost30unnormalized/pretraining.zip /work/capybara/results/wsj/dk_wsj_paper6_cost30unnormalized_continue /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_cost30unnormalized_continue.yaml &")
    time.sleep(100)
    os.system("THEANO_FLAGS=device=gpu1,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/dk_run.py train /work/capybara/results/wsj/dk_wsj_paper6_cost1000unnormalized /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_cost1000unnormalized.yaml &")
    time.sleep(100)

else: # ORIGINAL:
    os.system("THEANO_FLAGS=device=gpu0,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/dk_run.py train /work/capybara/results/wsj/dk_wsj_paper6_cost30unnormalized /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_cost30unnormalized.yaml &")
    time.sleep(100)
    os.system("THEANO_FLAGS=device=gpu1,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/dk_run.py train /work/capybara/results/wsj/dk_wsj_paper6_cost1000unnormalized /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_cost1000unnormalized.yaml &")
    time.sleep(100)
    os.system("THEANO_FLAGS=device=gpu2,floatX=float32,lib.amdlibm=0,lib.cnmem=0.5 $LVSR/bin/dk_run.py train /work/capybara/results/wsj/dk_wsj_paper6_cost300unnormalized /home/capybara/attention-lvcsr/exp/wsj/configs/dk_wsj_paper6_cost300unnormalized.yaml &")
    time.sleep(100)
