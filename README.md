# Q-Learning Maze Agent

This project implements a reinforcement learning agent that learns to navigate a maze using Q-learning.

The agent interacts with the maze environment, receives rewards based on its actions, and gradually improves its policy through repeated training. The project demonstrates core reinforcement learning ideas including Q-table updates, epsilon-greedy exploration, and reward-based decision making.

## Project Overview

The goal of this project is to train an agent to successfully move through a maze by learning which actions lead to better long-term rewards.

Rather than being given the correct path directly, the agent explores the environment, updates its Q-values, and improves over time through repeated episodes.

## What the Code Does

The notebook performs the following tasks:

1. Loads the maze environment
2. Initializes a Q-learning agent
3. Trains the agent over repeated episodes
4. Updates Q-values using observed rewards
5. Uses epsilon-greedy exploration to balance exploration and exploitation
6. Evaluates the learned behavior after training
7. Reports performance such as rewards, success, or learning progress

## Methods Used

- Python
- Reinforcement Learning
- Q-Learning
- Epsilon-Greedy Exploration
- Reward-Based Training

## Main Components

### `q_learning_maze_agent.ipynb`
Main notebook containing the training logic, experiments, and results.

### `maze.py`
Maze environment code used by the notebook. This file defines the maze structure and agent interaction rules.

## Learning Approach

This project uses a standard Q-learning workflow:

- The agent observes its current state
- It chooses an action
- It receives a reward from the environment
- It updates the Q-table using the Q-learning update rule
- Over many episodes, the agent improves its policy

Key reinforcement learning concepts used include:

- learning rate
- discount factor
- exploration rate
- Q-table updates
- training versus evaluation behavior

## Why This Project Matters

This project demonstrates:

- reinforcement learning fundamentals
- agent-based learning in an environment
- implementation of Q-learning from scratch or near-scratch logic
- handling exploration versus exploitation
- evaluating learned behavior over time

It is a useful portfolio project because it shows more than standard supervised learning on tabular data.

## Repository Contents

- `q_learning_maze_agent.ipynb` — main notebook
- `maze.py` — maze environment code

## Possible Improvements

Some natural next steps for this project would be:

- visualize the learned path through the maze
- plot reward over training episodes
- compare different values of alpha, gamma, and epsilon
- add more complex maze layouts
- compare Q-learning with other reinforcement learning methods
- improve reporting of convergence and success rate

## How to Run

1. Clone the repository
2. Make sure `maze.py` is in the same folder as the notebook
3. Install the required Python packages
4. Open the notebook and run all cells

If needed, install common dependencies with:

```bash
pip install numpy matplotlib
