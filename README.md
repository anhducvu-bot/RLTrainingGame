# A Reinforcement Learning Training Game

## What?
There's an old saying: "the harder you work, the better you get." This is true, not only for humans but also for AI! In this game, the user can choose how many rounds the AI has to train. Then, to access his performance, the user has the option to choose how many rounds the AI will be tested on. Similar to human, the more rounds the AI trains, the better it gets! In this game, the player will teach the AI to be a taxi driver! In the environment, there are 4 locations, and the AI has to pick up the passenger at one location and drop them off at another. 

Note that, we ***do not*** implicitly tell the AI what to do and how to play the game. Rather, we let it explore and try out different actions in each round. We ***reward*** it when it does something correctly, and ***punish*** it when it does something bad (just like how you train a dog to pee in the right place!) As you will see, rewards and punishment alone are ***enough*** for the agent to learn how to play the game. That's the magic of ***Reinforcement Learning!*** 

## How?
The game can be run directly on terminal, or on any IDE. A playthrough of the program can be find [here](https://www.youtube.com/watch?v=xtqAbc157JQ)

First, the user choose how many rounds the agent will be trained. Note that, this is when the agent will explore different actions, and learn more about the environment. 

![](Screenshot%20Train.png)
Then, the user choose how many rounds the agent will be tested on. Note that, the agent will no longer explore the environment, but rather act to the best of its knowledge. In Reinforcement Learning, this action is termed "act greedily". 
![](Screenshot%20Test.png)
## Performance

Just like a human, the AI performs better the more time it trains! Below is the AI's performance when it was trained 100 times and when it was trained 1000 times. 

***AI perform after training for 100 rounds:***

![](100%20round.gif)

***AI perform after training for 1000 rounds:***

![](1000%20round.gif)

## Improvement
There are 3 main improvements that can be made:
- The environment implemented in the game is the 'Taxi-v2' environment provided by [OpenAI](https://gym.openai.com/envs/#classic_control). In the future, we can include other environments for the AI to train on. 
- All of the hyperparameters are already tuned. We can include the options for the users to play around with different parameters, and see how they affect the learning performance. 
- The learning method implemented in the program is Q-learning. We can include other learning methods (Sarsa,...) to let the users observe how their performance stacks with each other. 



