import gym
import gym_manipulation
import time
env = gym.make('gym_manipulation:panda-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        for step in range(100):
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            time.sleep(1)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()