#/bin/bash

DOMAIN="/raid/home/frosa_Loc/period_abroad/heuristic-computation/planning-learning-heuristic/baseline_evaluation/blocks_world/domain.pddl"
PROBLEMS="/raid/home/frosa_Loc/period_abroad/heuristic-computation/planning-learning-heuristic/baseline_evaluation/blocks_world/easy/5/task01.pddl"
CHECKPOINT="/raid/home/frosa_Loc/period_abroad/heuristic-computation/planning-learning-heuristic/STRIPS-HGN/results/train-strips-hgn-2024-06-14T15:36:31.043115/model-best.ckpt"
HEURISTIC="h_add"
SEARCH_TIME=300

python eval.py -d ${DOMAIN} -p ${PROBLEMS} -c ${CHECKPOINT} -H ${HEURISTIC} -t ${SEARCH_TIME}
