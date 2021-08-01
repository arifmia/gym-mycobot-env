from gym.envs.registration import register

register(
    id='mycobot-v0',
    entry_point='gym_manipulation.envs:ManipulationEnv',
)
register(
    id='panda-v0',
    entry_point='gym_manipulation.envs:PandaEnv',
)
