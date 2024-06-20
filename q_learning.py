# Imports:
# --------
from functools import reduce
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import copy
import gymnasium as gym
import os


# Function 1: Train Q-learning agent
# -----------
def valid_size(state,env):
    return  0 < state[0] < env.grid_size and 0 < state[1] < env.grid_size

SEQ = []
def generate_random_int_without_repeat(low, high):
    random_num = np.random.randint(low, high)
    
    if len(SEQ) > 0 and SEQ[len(SEQ) - 1] == random_num:
        random_num = SEQ[len(SEQ) - 1]
        return random_num
    else:
        SEQ.append(random_num)
        return random_num



def train_q_learning(env:gym.Env,
                     no_episodes,
                     epsilon,
                     epsilon_min,
                     epsilon_decay,
                     alpha,
                     gamma,
                     q_table_save_path="q_table.npy"):

    # Initialize the Q-table:
    # -----------------------
    q_table = np.zeros((env.grid_size, env.grid_size, env.action_space.n))

    # Q-learning algorithm:
    # ---------------------
    #! Step 1: Run the algorithm for fixed number of episodes
    #! -------
    isLooped = False
    for episode in range(no_episodes):

        state, _ = env.reset()
            
       
            

        state = tuple(state)
        total_reward = 0

        #! Step 2: Take actions in the environment until "Done" flag is triggered
        #! -------
        for _ in range(1_000):
            #! Step 3: Define your Exploration vs. Exploitation
            #! -------
            env.agent_health = 100
            random_rand = np.random.rand()
            if random_rand < epsilon:
                # action = env.action_space.sample()  # Explore
                action=generate_random_int_without_repeat(0,4)
            else:
                action = np.argmax(q_table[state])  # Exploit

            next_state, reward, done, _ = env.step(action)
            #env.render()

            next_state = tuple(next_state)
            
            
                
            total_reward += reward

            #! Step 4: Update the Q-values using the Q-value update rule
            #! -------
            q_table[state][action] = q_table[state][action] + alpha * \
                (reward + gamma *
                 np.max(q_table[next_state]) - q_table[state][action])

            state = next_state

            #! Step 5: Stop the episode if the agent reaches Goal or Hell-states
            #! -------
            if done:
                break

        #! Step 6: Perform epsilon decay
        #! -------
        print(f"Current Epsilon of Episode {episode}",epsilon)
        
        epsilon = max(epsilon_min, epsilon * epsilon_decay)

        print(f"Episode {episode + 1}: Total Reward: {total_reward}")

    #! Step 7: Close the environment window
    #! -------
    env.close()
    print("Training finished.\n")

    #! Step 8: Save the trained Q-table
    #! -------
    idpath = os.path.join("npyfiles",str(id(q_table))+q_table_save_path)
    np.save(q_table_save_path, q_table)
    np.save(idpath,q_table)
    print("Q Table",q_table)
    print("Saved the Q-table.")


# Function 2: Visualize the Q-table
# -----------
def visualize_q_table(hell_state_coordinates=[(2, 1), (0, 4)],
                      goal_coordinates=(4, 4),
                      actions=["Up", "Down", "Right", "Left"],
                      q_values_path="q_table.npy"):

    # Load the Q-table:
    # -----------------
    try:
        q_table = np.load(q_values_path)

        # Create subplots for each action:
        # --------------------------------
        _, axes = plt.subplots(1, 4, figsize=(20, 5))

        for i, action in enumerate(actions):
            ax = axes[i]
            heatmap_data = q_table[:, :, i].copy()
            print('heatmap_data: ', heatmap_data)
            

            # Mask the goal state's Q-value for visualization:
            # ------------------------------------------------
            mask = np.zeros_like(heatmap_data, dtype=bool)
            mask[goal_coordinates] = True
            for indx in range(len(hell_state_coordinates)):
                mask[hell_state_coordinates[indx]] = True

            sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="viridis",
                        ax=ax, cbar=False, mask=mask, annot_kws={"size": 9})

            # Denote Goal and Hell states:
            # ----------------------------
            ax.text(goal_coordinates[1] + 0.5, goal_coordinates[0] + 0.5, 'G', color='green',
                    ha='center', va='center', weight='bold', fontsize=14)
            
            for row in range(len(hell_state_coordinates)):
                ax.text(hell_state_coordinates[row][1] + 0.5, hell_state_coordinates[row][0] + 0.5, 'H', color='red',
                        ha='center', va='center', weight='bold', fontsize=14)
            
            

            ax.set_title(f'Action: {action}')

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("No saved Q-table was found. Please train the Q-learning agent first or check your path.")
        
        
        
def test_q_table(env, no_episodes, epsilon, q_table_save_path="q_table.npy", actions=["Up", "Down", "Right", "Left"]):
    try:
        loaded_q_table = np.load(q_table_save_path)
    except FileNotFoundError:
        print("No saved Q-table found. Please train the Q-learning agent first or check your path.")
        return
    
    state, _ = env.reset(train=False)
    state = tuple(state)
    total_reward = 0
    path = [state]
    done= False
    prev_action = ""
    mappedAction = {}
    while not done:
        print(len(mappedAction))
        if len(mappedAction) == 0:
            prev_action = ""
            mappedAction = {action: 0 for action in actions}
            for indx, action in enumerate(actions):
                np_arrayed = np.array(loaded_q_table[:][:][indx])
                mappedAction[action] = reduce(lambda x, y: x + y, np_arrayed.flatten())
        
           
        max_key = max(mappedAction, key=mappedAction.get)
        while max_key == prev_action:
            mappedAction.pop(max_key)
            max_key = max(mappedAction, key=mappedAction.get)
        prev_action  = max_key
        maxActionValue = [indx for indx,val in enumerate(actions) if val == max_key ][0]
        
        action = maxActionValue if any(mappedAction) else generate_random_int_without_repeat(0,4)
        
            
        next_state, reward, done, _ = env.step(action)
        env.render()

        next_state = tuple(next_state)
        total_reward += reward
        path.append(next_state)
        state = next_state

        if done:
            break




    