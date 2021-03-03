# A Reinforcement Learning Training Game

## What?
There's an old saying: "the harder you work, the better you get." This is true, not only for human, but also for AI! In this game, the user can choose how many rounds the AI has to train. Then, to access his performance, the user have the option to choose how many rounds the AI will be tested on. Similar to human, the more rounds the AI trains, the better it gets! 

In the enviroment, there are 4 locations, and the AI has to pick up the passenger at one location, and drop them off at another. Note that, we don't actually tell the AI what to do and how to play the game. Rather, we let it explore and try out different actions in each rounds, reward it when it do something correctly, and punish it when it do something bad (just like how you train a dog to pee in the right place!) As you will see, rewards and punishment alone are enough for the agent to learn how to play the game. That's the magic of Reinforcememnt Learning! 

## How?
The game can be run directly on terminal, or on any IDE. 

First, the user can choose how many rounds the agent will be trained. Note that, this is where the agent will explore different actions, and learn more about the environment. 

Then, the user can choose how many rounds the agent will be tested on. Note that, the agent will no longer explore the environment, but act to perform the best sequence actions, based on the knowledge it learn from the training rounds. 

## Performance

Just like human, the AI perform better the more time it trains! Below are the AI's performance when it was trained 100 times and when it was trained 1000 times. 


## Improvement

The environment implemented in the game is the 'Taxi-v2' environment provided by [OpenAI](https://gym.openai.com/envs/#classic_control). In the future, we can include other environments for the AI to train on. 
All of the hyperparameter are already tuned. We can include the options for the users to play around with different paramaters, and how it affect the learning performance. 
The learning method implemented in the program is Q-learning. We can include other learning meathods (Sarsa,...) to let the users observe how their performance stack with each others. 



