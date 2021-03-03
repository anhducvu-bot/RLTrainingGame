import gym
import numpy as np
import sys
import time
from IPython.display import clear_output
import progressbar
from time import sleep


gamma=0.9
alpha=0.25
epsilon=0.4

def update_progress(job_title, progress):
    length = 20 # modify this to change the length
    block = int(round(length*progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
    if progress >= 1: msg += " DONE\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()

def choose_action(q_table,state,epsilon):
    x = np.random.uniform(0,1)
    if (x < epsilon): action = np.random.randint(6)
    else: action = np.argmax(q_table[state,:])
    return action
print("Welcome to my game!")
print("-------------")
print("In this game, we will train a driver to pick up and drop off the passenger from blue spot to pink spot!")
print("Hint: The more time your driver train, the better he will be at his job! ;)")

start = True
while start:

    n_episodes = input("How many times do you want to train your driver (number of training set)?: ")
    n_episodes = int(n_episodes)

    env = gym.make("Taxi-v3").env
    q_table = np.zeros((env.observation_space.n,env.action_space.n))

    for i in range(n_episodes):
        state = env.reset()
        done = False
        while(not done):
            action = choose_action(q_table,state,epsilon)
            next_state,reward,done,info = env.step(action)
            q_table[state,action] = q_table[state,action] + alpha*(reward + gamma*np.max(q_table[next_state,:]) - q_table[state,action])
            state = next_state
        update_progress("Training", i/n_episodes)
    update_progress("Some job", 1)
    clear = "\n" * 8
    print("Training is complete! The driver is exhausted!")
    trial = input("How many trips do you want your driver to work (number of test set)?: ")
    print(clear)
    print('Start!')
    for i in range(int(trial)):
        state = env.reset()
        done = False
        count = 0
        while not done:
            count = count + 1
            clear_output(wait = True)
            print(f'Episode {i+1}')

            env.render()
            if (n_episodes < 500): action = choose_action(q_table,state,0.5)
            else: action = np.argmax(q_table[state,:])
            next_state,reward,done,info = env.step(action)
            state = next_state

            time.sleep(0.1)
            if (count > 20):
                print("The passenger got pissed off and left!")
                print("Fail!")
                time.sleep(1)
                break
            if done:
                print('Episode done')
                print('Success!')
                time.sleep(1)
                break
    continue_to_play = input("Do you want to keep playing (y/n)?: ")
    if (continue_to_play == "y"): start = True
    else: start = False

print("Thanks for playing!")


