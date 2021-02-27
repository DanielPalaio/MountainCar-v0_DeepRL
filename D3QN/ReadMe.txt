Trained on a NVIDIA GeForce MX 250

env = gym.make("MountainCar-v0")
spec = gym.spec("MountainCar-v0")

num_episodes=1400
lr=0.001
discount_factor=0.99
num_actions=3
epsilon=1.0
batch_size=64
input_dim=[2]
update_rate=150

Test - 'saved_networks/d3qn_model300'