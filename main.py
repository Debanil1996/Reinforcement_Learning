from starways_env import create_env
from q_learning import train_q_learning, visualize_q_table,test_q_table

train = True
visualize_results = True
test_results = False

learning_rate = 0.01  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_min = 0.1  # Minimum exploration rate
epsilon_decay = 0.992  # Decay rate for exploration
no_episodes = 1000  # Number of episodes

goal_coordinates = (9, 9)
# Define all hell state coordinates as a tuple within a list
hell_state_coordinates = [
    (0, 5),
    (1, 3),
    (2, 8),
    (3, 6),
    (4, 1),
    (5, 9),
    (6, 7),
    (7, 3),
    (8, 1),
    (9, 3)
]


if train:
    
    env = create_env(goal_coordinates=goal_coordinates,
               hell_state_coordinates=hell_state_coordinates)
    
    train_q_learning(env=env,
                     no_episodes=no_episodes,
                     epsilon=epsilon,
                     epsilon_min=epsilon_min,
                     epsilon_decay=epsilon_decay,
                     alpha=learning_rate,
                     gamma=gamma)
    
    
if visualize_results:
    visualize_q_table(hell_state_coordinates=hell_state_coordinates,
                      goal_coordinates=goal_coordinates,
                      q_values_path="q_table.npy")
    
    
if test_results:
    
    new_env = create_env(goal_coordinates=goal_coordinates,
               hell_state_coordinates=hell_state_coordinates)
    
    test_q_table(env=new_env,
                     no_episodes=no_episodes,
                     epsilon=epsilon,
                     epsilon_min=epsilon_min,
                     epsilon_decay=epsilon_decay,
                     alpha=learning_rate,
                     gamma=gamma)