import gym
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import axes3d, Axes3D
from mpl_toolkits import mplot3d

import seaborn as sns

import math

from gym import Env
from gym.envs.registration import register
from gym.utils import seeding
from gym import spaces
from gym.envs.classic_control.cartpole import CartPoleEnv
import numpy as np

from numpy import linalg as LA


class MoveComToBeacon(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 50
    }

    def __init__(self):
        self.action_space = spaces.Box(low=-1, high=1, shape=(1,))
        self.observation_space = spaces.Box(low=-1, high=1, shape=(1,))

        self.seed()
        self.viewer = None
        self.state = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):


        action = np.clip(action, -0.025, 0.025)
        self.state = np.clip(self.state + action, -1, 1)

        #print(self.state)

        reward = 0

        if self.state < 0:
          reward = self.state+1

        if self.state >= 0:
          reward = -1*self.state+1

        if (self.state == -1) or (self.state == 1):
          reward = 0.00001


        return np.array(self.state), reward, False, {} #obs, reward, done, info  #(1/(LA.norm(x[k])))

      #(np.linalg.norm(self.state))
      # 1/(LA.norm(self.state)) # kinda shitty normal distribution

    def reset(self):
        while True:
            self.state = self.np_random.uniform(low=-1, high=1, size=(1,))
            # Sample states that are far away
            if np.linalg.norm(self.state) > 0.9:
                break
        return np.array(self.state)

    # def _render(self, mode='human', close=False):
    #     pass

    def render(self, mode='human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return

        screen_width = 800
        screen_height = 200

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)

            agent = rendering.make_circle(
                min(screen_height, screen_width) * 0.03)
            origin = rendering.make_circle(
                min(screen_height, screen_width) * 0.03)
            trans = rendering.Transform(translation=(0, 0))
            agent.add_attr(trans)
            self.trans = trans
            agent.set_color(0, 0, 0)
            origin.set_color(1, 0, 0)
            origin.add_attr(rendering.Transform(translation=(screen_width // 2, screen_height // 2)))
            self.viewer.add_geom(agent)
            self.viewer.add_geom(origin)

        #self.trans.set_translation(0, 0)

        self.trans.set_translation((self.state[0] + 1) / 2 * screen_width, screen_height // 2)


        #self.trans.set_translation(
        #    (self.state[0] + 1) / 2 * screen_width,
        #    (self.state[1] + 1) / 2 * screen_height,
        #)

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')
