

import os

if 1: # RELAUNCH...
    os.system("THEANO_FLAGS=device=gpu1,floatX=float32,lib.cnmem=0.9 $LVSR/bin/dk_run.py train --params=" + os.environ['SAVE_PATH'] + "/dk_wsj_paper6/main.zip " + os.environ['SAVE_PATH'] + "/dk_wsj_paper6_continue_rm_cost $LVSR/exp/wsj/configs/dk_wsj_paper6_continue_rm_cost.yaml &")
