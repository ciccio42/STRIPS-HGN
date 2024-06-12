import os
import torch
import numpy as np
import random
import sys
from os.path import dirname
sys.path.append(
    "/raid/home/frosa_Loc/period_abroad/heuristic-computation/STRIPS-HGN/src")


def seed_everything(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


if __name__ == "__main__":

    import debugpy
    from default_args import get_training_args, DomainAndProblemConfiguration
    from train import train_wrapper

    # debugpy.listen(('0.0.0.0', 5678))
    # print("Waiting for debugger attach")
    # debugpy.wait_for_client()
    # seed_everything(seed=42)

    _CONFIGURATION = DomainAndProblemConfiguration(
        base_directory="../benchmarks/blocks-slaney",
        domain_pddl="domain.pddl",
        # {3, 4, 5 blocks} x 10 problems = 30 problems
        problem_pddls=[
            "blocks3/task01.pddl",
            "blocks3/task02.pddl",
            "blocks3/task03.pddl",
            "blocks3/task04.pddl",
            "blocks3/task05.pddl",
            "blocks3/task06.pddl",
            "blocks3/task07.pddl",
            "blocks3/task08.pddl",
            "blocks3/task09.pddl",
            "blocks3/task10.pddl",
            "blocks4/task01.pddl",
            "blocks4/task02.pddl",
            "blocks4/task03.pddl",
            "blocks4/task04.pddl",
            "blocks4/task05.pddl",
            "blocks4/task06.pddl",
            "blocks4/task07.pddl",
            "blocks4/task08.pddl",
            "blocks4/task09.pddl",
            "blocks4/task10.pddl",
            "blocks5/task01.pddl",
            "blocks5/task02.pddl",
            "blocks5/task03.pddl",
            "blocks5/task04.pddl",
            "blocks5/task05.pddl",
            "blocks5/task06.pddl",
            "blocks5/task07.pddl",
            "blocks5/task08.pddl",
            "blocks5/task09.pddl",
            "blocks5/task10.pddl",
        ],
    )
    assert len(_CONFIGURATION.problems) == 30

    train_wrapper(
        args=get_training_args(
            configurations=[_CONFIGURATION],
            # 10 minutes
            max_training_time=10 * 60,
        )
    )
