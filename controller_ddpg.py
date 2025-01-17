import os
import gym
import gym_panda
import numpy as np
from stable_baselines3 import DDPG
from stable_baselines3.ddpg.policies import MlpPolicy
from stable_baselines3.common.noise import OrnsteinUhlenbeckActionNoise
from stable_baselines3.common.env_util import make_vec_env



models_dir = "models/DDPG/R1_L1"
logdir = "logs"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)


env = make_vec_env('panda-v0', n_envs=1)

n_actions = env.action_space.shape[-1]
action_noise = OrnsteinUhlenbeckActionNoise(mean=np.zeros(n_actions), sigma=float(0.5) * np.ones(n_actions))

model = DDPG(MlpPolicy, env, verbose=1, action_noise=action_noise, tensorboard_log=logdir)

TIMESTEPS = 100000
i = 1
while i <= 10:
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name='R1_L1_DDPG')
    print("Saving.....")
    model.save(f"{models_dir}/{TIMESTEPS*i}")
    i += 1
