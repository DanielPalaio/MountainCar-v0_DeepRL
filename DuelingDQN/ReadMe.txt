Trained on a NVIDIA GeForce MX 250

env = gym.make("MountainCar-v0")
spec = gym.spec("MountainCar-v0")

num_episodes=1250
lr=0.00075
discount_factor=0.99
num_actions=3
epsilon=1.0
batch_size=64
input_dim=[2]
update_rate=120

Test - 'saved_networks/duelingdqn_model172'