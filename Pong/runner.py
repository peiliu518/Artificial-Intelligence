
from Simulator import Simulator
from MDP import MDP

if __name__ == "__main__":
    '''
    Runner code to start the training and game play.
    '''
alpha_value = 0.1
gamma_value = 0.95
epsilon_value = 1
num_games = 100000
agent = Simulator.Simulator(num_games, alpha_value, gamma_value, epsilon_value)
obj = MDP.MDP()
obj.create_state()
agent.train_agent(obj)
agent.play_game(obj)
