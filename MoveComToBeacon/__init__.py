
from gym.envs.registration import register

from .MoveComtoBeacon import MoveComtoBeacon


environments = [['MoveComToBeacon', 'v0']]

for environment in environments:
    register(
        id='{}-{}'.format(environment[0], environment[1]),
        entry_point='MoveComToBeacon:{}'.format(environment[0]),
        timestep_limit=1,
        nondeterministic=True,
    )
