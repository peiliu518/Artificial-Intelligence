import sys
import math
import random
import pdb

class MDP:
	def __init__(self, ball_x=None,ball_y=None,velocity_x=None,velocity_y=None,paddle_y=None):

		self.create_state(ball_x=ball_x,ball_y=ball_y,velocity_x=velocity_x,velocity_y=velocity_y,paddle_y=paddle_y)
        
        # the agent can choose between 3 actions - stay, up or down respectively.
		self.actions = [0, 0.04, -0.04]
		self.reward = 0
		self.Q = {}
    
	def create_state(self,ball_x=None,ball_y=None,velocity_x=None,velocity_y=None,paddle_y=None):

       ########### Helper function for the initializer. Initialize member variables with provided or default values.

		self.paddle_height = 0.2
		self.ball_x = ball_x if ball_x != None else 0.5
		self.ball_y = ball_y if ball_y != None else 0.5
		self.velocity_x = velocity_x if velocity_x != None else 0.03
		self.velocity_y = velocity_y if velocity_y != None else 0.01
		self.paddle_y = paddle_y if paddle_y != None else 0.5 - self.paddle_height/2
    
	def initialize(self):
		self.paddle_height = 0.2
		self.ball_x = 0.5
		self.ball_y = 0.5
		self.velocity_x = 0.03
		self.velocity_y = 0.01
		self.paddle_y = 0.5 - self.paddle_height/2

	def simulate_one_time_step(self, action_selected):
        
        #:param action_selected - Current action to execute.
        #Perform the action on the current continuous state.
		self.reward = 0 
		paddle_x = 1

        # update ball status
		ball_x = self.ball_x + self.velocity_x
		ball_y = self.ball_y + self.velocity_y
		velocity_x = self.velocity_x
		velocity_y = self.velocity_y
        # update paddle status
		paddle_y = self.paddle_y + action_selected
        # paddle boundary check
		if paddle_y > (1 - self.paddle_height):
			paddle_y = 1 - self.paddle_height 
		if paddle_y < 0:
			paddle_y = 0
		
        # ball boundary check
		if ball_y < 0:
			ball_y = - ball_y
			velocity_y = - self.velocity_y
		if ball_x < 0:
			ball_x = - ball_x
			velocity_x = - self.velocity_x
		if ball_y > 1:
			ball_y = 2 - ball_y
			velocity_y = - self.velocity_y

        # bounce check 
		if ball_x >= 1: 
            # if paddle misses the ball
			if ball_y < paddle_y or ball_y > (paddle_y + self.paddle_height):
				self.reward = -1
            # if paddle reaches the ball
			else:
				# 2/14/2017 20:07
				# ball_x == 1
				self.reward = 1
				ball_x = 2 * paddle_x - self.ball_x
                # randomize ball velocity 
				velocity_x = - velocity_x
				if abs(velocity_x) >= 0.03:
					velocity_x += random.uniform(-0.015, 0.015)
				else:
					while velocity_x < 0.03:
						velocity_x += random.uniform(0.000, 0.015)    ## change this to 0
				velocity_y += random.uniform(-0.03, 0.03)                 
				                      
		self.ball_x = round(ball_x,3)
		self.ball_y = round(ball_y,3)
		self.velocity_x = round(velocity_x,3)
		self.velocity_y = round(velocity_y,3)
		self.paddle_y = round(paddle_y,3)

        # self.ball_x = ball_x
        # self.ball_y = ball_y
        # self.velocity_x = velocity_x
        # self.velocity_y = velocity_y
        # self.paddle_y = paddle_y

        # pdb.set_trace()


    
	def discretize_state(self):
        # discretize ball position
		if math.floor(12 * self.ball_x) >= 11:#originally math.fllor(self.ball_x)
			ball_x = 11
		else:
			ball_x = math.floor(12 * self.ball_x)
		if math.floor(12 * self.ball_y) >= 11:
			ball_y = 11
		else:
			ball_y = math.floor(12 * self.ball_y  )

        # discretize ball horitonzal movement
		if self.velocity_x >= 0:
			velocity_x = 1
		else:
			velocity_x = -1
            # discretize ball vertical movement 
		if self.velocity_y >= 0.015:
			velocity_y = 1
		elif self.velocity_y <= -0.015:
			velocity_y = -1
		else:
			velocity_y = 0    

        # discretize paddle y coord.
		if self.paddle_y >= 1 - self.paddle_height: 
			paddle_y = 11
		else:
			paddle_y = math.floor(12 * self.paddle_y / (1 - self.paddle_height))

		return (ball_x, ball_y, velocity_x, velocity_y, paddle_y)

	def get_Q(self):
		
		max_Q = -sys.maxint
		for action in self.actions:
			key =(self.discretize_state(),action)
			if key not in self.Q :
				self.Q[key]= 0
			if self.Q[key] > max_Q : 
				max_Q=self.Q[key]
		return max_Q




