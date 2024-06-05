from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        self.possible_actions = ['MM', 'MC', 'CC', 'M', 'C']
        super().__init__(initial, goal)

    def result(self, state, action):
        x = -1 if state[2] else 1 # Sets the direction for unit movement.
        return (state[0] + action.count('M')*x, state[1] + action.count('C')*x, not state[2])

    def actions(self, state):
        valid_actions =  ['MM', 'MC', 'CC', 'M', 'C']
        for action in self.possible_actions :
            test_state = self.result(state, action)
            # Confirm Missionaries are in range
            if test_state[0] < 0 or test_state[0] > self.M :
                valid_actions.remove(action)
            # Confirm Cannibals are in range    
            elif test_state[1] < 0 or test_state[1] > self.C : 
                valid_actions.remove(action)
            # Confirm Missionaries aren't outnumbered on left bank
            elif test_state[0] > 0 and test_state[0] < test_state[1] : 
                valid_actions.remove(action)
            # Confirm Missionaries aren't outnumbered on right bank
            elif self.M - test_state[0] > 0 and (self.M - test_state[0]) < (self.C - test_state[1]) :
                valid_actions.remove(action)
        return valid_actions
    
if __name__ == '__main__':
    mc = MissCannibals(M=4, C=4)
    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)