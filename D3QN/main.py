

from agent import Agent
import gym


env = gym.make("MountainCar-v0")
spec = gym.spec("MountainCar-v0")
train = 0
test = 1
num_episodes = 100
graph = True

file_type = 'tf'
file = 'saved_networks/d3qn_model300'

d3qn_agent = Agent(lr=0.001, discount_factor=0.99, num_actions=3, epsilon=1.0, batch_size=64, input_dim=[2])

if train and not test:
    d3qn_agent.train_model(env, num_episodes, graph)
else:
    d3qn_agent.test(env, num_episodes, file_type, file, graph)
