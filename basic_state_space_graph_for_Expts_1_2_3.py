class Graph:
    def __init__(self, states=[], initial_state=None, goal_states=[]):
        self.states = states
        self.initial_state = initial_state
        self.goal_states = goal_states
    
    def BFS(self):
        pass
    
    def DFID(self):
        pass
    
    def A_star(self):
        pass


class State:
    def __init__(self, name, actions=[]):
        self.name = name
        self.actions = actions


class Action:
    def __init__(self, name, dest, cost):
        self.name = name
        self.dest = dest
        self.cost = cost

if __name__ == '__main__':
    print('Demonstration of Search algorithms over state-space graphs in AI')
    try:
        N = int(input('Enter the number of states in the state-space graph: '))
        if N <= 0:
            exit('Entered number is not a valid positive integer')
    except:
        exit('Entered number is not a valid positive integer')
    
    G = Graph()
    for i in range(N):
        G.states.append(State(input(f'Enter name for state number {i+1}')))
    initial_state_name = input('Enter the name of initial state : ')
    try:
        G.initial_state = list(filter(lambda s: s.name==initial_state_name, G.states))[0]
    except:
        exit(f'No state with name {start_state_name}')
    
    goal_states_string = input('Enter the names of goal-states separated by spaces:')
    for g in goal_states_string.split():
        try:
            G.goal_states.append(list(filter(lambda s: s.name==g, G.states))[0])
        except:
            exit(f'No state with name {g}')
    # print(G.goal_states[0].name)
    
    for s in G.states:
        try:
            N = int(input(f'Enter the number of actions available in state {s.name}: '))
            if N < 0:
                exit('Entered number is not a valid non-negative integer')
        except:
            exit('Entered number is not a valid non-negative integer')
        if N > 0:
            print('Enter the action-name, destination-name and cost separated by spaces:')
            for i in range(N):
                action_name, dest_name, cost = input(f'for action number {i}: ').split()
                if len(list(filter(lambda s: s.name==dest_name, G.states))) == 0:
                    exit(f'No state with name {dest_name}')
                try:
                    cost = float(cost)
                except:
                    exit('Entered cost is not a valid number')
                s.actions.append(Action(action_name, dest_name, cost))

