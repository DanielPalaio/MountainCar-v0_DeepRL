# OpenAI MountainCar-v0 DeepRL-based solutions
Using Deep Q-Network (DQN), Dueling DQN, and Dueling Double DQN (D3QN)  

Investigation under the development of the master thesis "DeepRL-based Motion Planning for Indoor Mobile Robot Navigation" @ Institute of Systems and Robotics - University of Coimbra (ISR-UC)  

# Software/Requirements
Module | Software/Hardware
------------- | -------------
Python IDE | Pycharm
Deep Learning library | Tensorflow + Keras
GPU | GeForce MX 250
Interpreter | Python 3.8
Python Environment | Anaconda
Packages | requirements.txt

**To setup Pycharm + Anaconda + GPU, consult the setup file [here](setup.txt)**.  
**To import the required packages, [requirements.txt](DQN/requirements.txt), type the following instruction in the project environment terminal:**  
> pip install -r requirements.txt

# :warning: **WARNING** :warning:  
The training generates a [.txt file](DQN/saved_networks.txt) that tracks the network models (in 'tf' and .h5 formats) that achieved the solved requirement of the environment. Additionally, an overview image (graph) of the training procedure is created.   
Keep in mind that to perform several training processes, the .txt, .png, and directory names must be change. Otherwise, information of previous trainings will get overwritten, and lost.  

Regarding testing, if you choose to load the .h5 model, a 5 episode training is done to initialize/build the keras.model network. Thus, the warnings above mentioned are also appliable to this situation.   
Loading the saved model in 'tf' is the recommended option. After finishing the testing, an overview image (graph) of the training procedure is also generated.  

# OpenAI MountainCar-v0
**Actions:**<br />
0 - Push car to the left    
1 - No action  
2 - Push car to the right

**States:**<br />
0 - Car position  
1 - Car velocity  

**Rewards:**<br />
Scalar value (-1) for every step taken

**Episode termination:**<br />
Car reaches position 0.5  
Episode length is greater than 200

**Solved Requirement:**<br />
Average reward of -110.0 over 100 consecutive trials

# Deep Q-Network (DQN)
<p align="center">
  <img width="804" height="415" src="https://user-images.githubusercontent.com/79323290/109340337-cb6c5480-7860-11eb-9411-42b8e0d5941d.png">
</p>

<table>
<tr><th> Train </th><th> Test </th></tr>
<tr><td>

| Parameter | Value |
|--|--|
| Number of episodes | 1500 |
| Learning rate  | 0.001 |
| Discount Factor | 0.99 |
| Epsilon | 1.0 |
| Batch size | 64 |
| TargetNet update rate (steps) | 100 |
| Actions (MountainCar-v0 env) | 3 |
| States (MountainCar-v0 env) | 2 |

</td><td>

| Parameter | Value |
|--|--|
| Number of episodes | 100 |
| Epsilon | 0.01 |
| Actions (MountainCar-v0 env) | 3 |
| States (MountainCar-v0 env) | 2 |

</td></tr> </table>

<p align="center">
  <img src="DQN/MountainCar_Train.png" width="400" height="250" />
  <img src="DQN/MountainCar_Test.png" width="400" height="250"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/79323290/109392669-5a3aa900-7915-11eb-8bda-c4b3f1525713.gif" width="400" height="250" />
  <img src="https://user-images.githubusercontent.com/79323290/109392675-5b6bd600-7915-11eb-8c98-411ff05ab74f.gif" width="400" height="250"/>
</p>

> **Network model used for testing:** 'saved_networks/dqn_model20' ('tf' model, also available in .h5)  

# Dueling DQN
<p align="center">
  <img width="804" height="415" src="https://user-images.githubusercontent.com/79323290/109340340-cc9d8180-7860-11eb-9011-1ea05ef7fc75.png">
</p>

<table>
<tr><th> Train </th><th> Test </th></tr>
<tr><td>

| Parameter | Value |
|--|--|
| Number of episodes | 1250 |
| Learning rate  | 0.00075 |
| Discount Factor | 0.99 |
| Epsilon | 1.0 |
| Batch size | 64 |
| TargetNet update rate (steps) | 120 |
| Actions (MountainCar-v0 env) | 3 |
| States (MountainCar-v0 env) | 2 |

</td><td>

| Parameter | Value |
|--|--|
| Number of episodes | 100 |
| Epsilon | 0.01 |
| Actions (MountainCar-v0 env) | 3 |
| States (MountainCar-v0 env) | 2 |

</td></tr> </table>

<p align="center">
  <img src="DuelingDQN/MountainCar_Train.png" width="400" height="250" />
  <img src="DuelingDQN/MountainCar_Test.png" width="400" height="250"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/79323290/109392672-5ad33f80-7915-11eb-81e8-f24c04f80f01.gif" width="400" height="250" />
  <img src="https://user-images.githubusercontent.com/79323290/109392994-47c16f00-7917-11eb-86cd-cd1d69ecba95.gif" width="400" height="250" />
</p>

> **Network model used for testing:** 'saved_networks/duelingdqn_model172' ('tf' model, also available in .h5)  

# Dueling Double DQN (D3QN)
<p align="center">
  <img width="804" height="415" src="https://user-images.githubusercontent.com/79323290/109341984-1e470b80-7863-11eb-9c5b-33a967d6bdd9.png">
</p>

<table>
<tr><th> Train </th><th> Test </th></tr>
<tr><td>

| Parameter | Value |
|--|--|
| Number of episodes | 1400 |
| Learning rate  | 0.001 |
| Discount Factor | 0.99 |
| Epsilon | 1.0 |
| Batch size | 64 |
| TargetNet update rate (steps) | 150 |
| Actions (MountainCar-v0 env) | 3 |
| States (MountainCar-v0 env) | 2 |

</td><td>

| Parameter | Value |
|--|--|
| Number of episodes | 100 |
| Epsilon | 0.01 |
| Actions (MountainCar-v0 env) | 3 |
| States (MountainCar-v0 env) | 2 |

</td></tr> </table>

<p align="center">
  <img src="D3QN/MountainCar_Train.png" width="400" height="250" />
  <img src="D3QN/MountainCar_Test.png" width="400" height="250"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/79323290/109392674-5b6bd600-7915-11eb-80ff-1c7152beeb0c.gif" width="400" height="250" />
  <img src="https://user-images.githubusercontent.com/79323290/109393685-15197580-791b-11eb-86ec-fb315f90467b.gif" width="400" height="250" />
</p>

> **Network model used for testing:** 'saved_networks/d3qn_model300' ('tf' model, also available in .h5)  
