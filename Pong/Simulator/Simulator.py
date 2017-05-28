import random
import sys
import math
import pdb
from MDP import MDP

class Simulator:

	def __init__(self, num_games=0, alpha_value=0, gamma_value=0, epsilon_value=0):

		self.num_games = num_games
		self.epsilon_value = epsilon_value
		self.alpha_value = alpha_value
		self.gamma_val = gamma_value
		self.bounces = 0

        # Your Code Goes Here!
		# MDP Initialization exist

	def f_function(self,M_obj):

        #Choose action based on an epsilon greedy approach
        #return action selected


		if self.epsilon_value > random.random(): #epsilon greedy approach
			action=M_obj.actions[int(math.floor(random.uniform(0,3)))]
			return action

		#check for non-state
		action_selected = None		 #best action
		test_q_value = -sys.maxint   #check q values of each action possible in the current state
		for action in M_obj.actions:
			key = (M_obj.discretize_state(),action) #as an element for hash
			if key not in M_obj.Q:
				action_selected = action
				return action_selected
			if M_obj.Q[key] > test_q_value:
				test_q_value = M_obj.Q[key]
				action_selected = action
		return action_selected



	def train_agent(self,obj):
        #Train the agent over a certain number of games.
        # Your Code Goes Here!
		# obj = MDP.MDP()
		bounce_total = 0
		count = 0
		while count < 100000:
			if count%1000 == 0:
			 	print ("number of attempts ", count)
			 	if count != 0:
			 		print ("average bounce is ",bounce_total/1000.000)
					bounce_total = 0
			obj.initialize() #initialize
			bounce_single = 0
			while obj.reward != -1:
				action = self.f_function(obj)

				# if bounce_single >= 10:
				# 	print '!!!!!!!!!!!!!! current bounce too large: ', bounce_single
				# 	print "game #", count
				# 	print 'action:', action
				# 	print 'state:', (obj.ball_x, obj.ball_y, obj.velocity_x, obj.velocity_y, obj.paddle_y)	
				# 	print 'discretize_state: ', obj.discretize_state()

				key = (obj.discretize_state(),action)  #save information of prev state before move on to next state
				obj.simulate_one_time_step(action)
				self.Q_learning(key, obj)
				if obj.reward > 0:
					bounce_single+=1
					bounce_total +=1
				self.num_games-=1
				# single game ends
#		    	print "game #", count

#		    	if count !=  0:
#		    		print 'total bounce = ', bounce_total
#		    		print 'single game bounce = ', bounce_single
#		    		print 'avg bounce = ', float(bounce_total)/float(count)
#		    	else:
#		    		print 'avg bounce = ', bounce_total	
			count +=1
			obj.reward=0	

	def Q_learning(self, key, obj):
		 #parameter of hash for current state
		if key not in obj.Q:
			obj.Q[key] = self.alpha_value*( obj.reward+self.gamma_val*obj.get_Q() )
			pass
		obj.Q[key] = obj.Q[key] + self.alpha_value*(obj.reward + self.gamma_val * obj.get_Q()-obj.Q[key])
		pass

	def play_game(self, m_obj):

		print '==========='
		print '==========='
		print 'Play starts'
		#pdb.set_trace()
		total_bounce = 0
		for play_num in range (1,6):
			m_obj.paddle_height = 0.2
			m_obj.ball_x = 0.5
			m_obj.ball_y = 0.5
			m_obj.velocity_x = 0.03
			m_obj.velocity_y = 0.01
			m_obj.paddle_y = 0.5 - m_obj.paddle_height/2
			m_obj.reward = 0
			bounce = 0
			while m_obj.reward != -1:
				action = self.f_function(m_obj)
				key = (m_obj.discretize_state(),action)  #save information of prev state before move on to next state
				m_obj.simulate_one_time_step(action)
				if m_obj.reward > 0:
					bounce += 1
			total_bounce += bounce
			print 'Game %d bounce number: %d ' %(play_num, bounce)
		print 'Average bounce number: ', float(total_bounce)/5
		print 'Play ends'

