from constants import HELL_COORDINATE_POINTS
from starways_env import create_env
from q_learning import train_q_learning, visualize_q_table,test_q_table

train = False
train_render = False
visualize_results = False
test_results = True

learning_rate = 0.01  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_min = 0.01  # Minimum exploration rate
epsilon_decay = 0.999  # Decay rate for exploration
no_episodes = 10_000  # Number of episodes

goal_coordinates = (9, 9)

hell_state_coordinates = HELL_COORDINATE_POINTS


if train:
    
    env = create_env(goal_coordinates=goal_coordinates,
               hell_state_coordinates=hell_state_coordinates)
    
    train_q_learning(env=env,
                     no_episodes=no_episodes,
                     epsilon=epsilon,
                     epsilon_min=epsilon_min,
                     epsilon_decay=epsilon_decay,
                     alpha=learning_rate,
                     gamma=gamma,
                     train_render=train_render)
    
    
if visualize_results:
    visualize_q_table(hell_state_coordinates=hell_state_coordinates,
                      goal_coordinates=goal_coordinates,
                      q_values_path="q_table.npy")
    
    
if test_results:
    
    new_env = create_env(goal_coordinates=goal_coordinates,
               hell_state_coordinates=hell_state_coordinates)
    
    test_q_table(env=new_env,
                no_episodes=no_episodes,
                epsilon=epsilon)