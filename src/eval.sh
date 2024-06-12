#/bin/bash

DOMAIN="/raid/home/frosa_Loc/period_abroad/heuristic-computation/STRIPS-HGN/benchmarks/blocks-slaney/domain.pddl"
PROBLEMS="/raid/home/frosa_Loc/period_abroad/heuristic-computation/STRIPS-HGN/benchmarks/blocks-slaney/blocks10/task01.pddl"
CHECKPOINT="/raid/home/frosa_Loc/period_abroad/heuristic-computation/STRIPS-HGN/results/train-strips-hgn-2024-06-11T15:37:47.921910/model-best.ckpt"
HEURISTIC="h_add"
SEARCH_TIME=300

python eval.py -d ${DOMAIN} -p ${PROBLEMS} -c ${CHECKPOINT} -H ${HEURISTIC} -t ${SEARCH_TIME}
