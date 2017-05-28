import MDP
import pdb

##### test discretization
print '<Test begins> \ndiscretization & one-time-step:'
ret = {}
# pdb.set_trace()
m = MDP.MDP()	
m.create_state(0.99, 0.99, 0.02, 0.34,0.6)
print 'Original state', (m.ball_x, m.ball_y, m.velocity_x, m.velocity_y, m.paddle_y)
ret_1 = m.discretize_state()
print 'Discretized state:', ret_1

##### test one time step
#pdb.set_trace()	
m.simulate_one_time_step(-0.4)
print "One step after:", (m.ball_x, m.ball_y, m.velocity_x, m.velocity_y, m.paddle_y)
print '<Test ends>'


