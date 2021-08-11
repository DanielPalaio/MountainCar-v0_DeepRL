# OpenAI MountainCar-v0 DeepRL-based solutions

Investigation under the development of the master thesis "DeepRL-based Motion Planning for Indoor Mobile Robot Navigation" @ Institute of Systems and Robotics - University of Coimbra (ISR-UC)  

## Requirements
Module | Software/Hardware
------------- | -------------
Python IDE | Pycharm
Deep Learning library | Tensorflow + Keras
GPU | GeForce GTX 1060
Interpreter | Python 3.8
Packages | requirements.txt

**To setup Pycharm + Anaconda + GPU, consult the setup file [here](setup.txt)**.  
**To import the required packages ([requirements.txt](DQN/requirements.txt)), download the file into the project folder and type the following instruction in the project environment terminal:**  
> pip install -r requirements.txt

## :warning: **WARNING** :warning:  
The training process generates a [.txt file](DQN/saved_networks.txt) that track the network models (in 'tf' and .h5 formats) which achieved the solved requirement of the environment. Additionally, an overview image (graph) of the training procedure is created.   
To perform several training procedures, the .txt, .png, and directory names must be change. Otherwise, the information of previous training models will get overwritten, and therefore lost.  

Regarding testing the saved network models, if using the .h5 model, a 5 episode training is required to initialize/build the keras.model network. Thus, the warnings above mentioned are also appliable to this situation.   
Loading the saved model in 'tf' is the recommended option. After finishing the testing, an overview image (graph) of the training procedure is also generated.  

## OpenAI MountainCar-v0
**Actions:**<br />
0 - Push car to the left    
1 - No action  
2 - Push car to the right

**States:**<br />
0 - Car position [-1.2, 0.6]  
1 - Car velocity [-0.07, 0.07]  

**Rewards:**<br />
Scalar value (-1) for every step taken

**Episode termination:**<br />
Car position (State 0) == 0.5  
Episode length > 200

**Solved Requirement:**<br />
Average reward of -110.0 over 100 consecutive trials  

## Deep Q-Network (DQN)

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
| Actions | 3 |
| States | 2 |

</td><td>

| Parameter | Value |
|--|--|
| Number of episodes | 100 |
| Epsilon | 0.01 |
| Actions | 3 |
| States | 2 |

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

## Dueling DQN

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
| Actions | 3 |
| States | 2 |

</td><td>

| Parameter | Value |
|--|--|
| Number of episodes | 100 |
| Epsilon | 0.01 |
| Actions | 3 |
| States | 2 |

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

## Dueling Double DQN (D3QN)

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
| Actions | 3 |
| States | 2 |

</td><td>

| Parameter | Value |
|--|--|
| Number of episodes | 100 |
| Epsilon | 0.01 |
| Actions | 3 |
| States | 2 |

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
