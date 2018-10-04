
from gym.envs.registration import register

from .movecomtobeacon import MoveComtoBeacon


environments = [['MoveComtoBeacon', 'v0']]

for environment in environments:
    register(
        id='{}-{}'.format(environment[0], environment[1]),
        entry_point='gym_bandits:{}'.format(environment[0]),
        timestep_limit=1,
        nondeterministic=True,
    )
