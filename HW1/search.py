# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    fringe=util.Stack()
    closed=set()
    initial_state_name = problem.getStartState()
    initial_state=(initial_state_name , [] , 0)
    """ state STRUCT -> (state_name,state_path,state_cost) """
    fringe.push(initial_state)


    while not fringe.isEmpty():
        expanded_state= fringe.pop()
        (expanded_state_name,expanded_state_path,expanded_state_cost)=expanded_state
        if not expanded_state_name in closed:
            closed.add(expanded_state_name)
            if(problem.isGoalState(expanded_state_name)):
                return expanded_state_path
            for state_name , state_action , state_cost in problem.getSuccessors(expanded_state_name):
                if not state_name in closed:
                    new_state_name = state_name
                    new_state_path = expanded_state_path + [state_action]
                    new_state_cost = expanded_state_cost + state_cost
                    new_state=(new_state_name,new_state_path,new_state_cost)
                    fringe.push(new_state)

    return ["GOAL NOT FOUND"]


    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe=util.Queue()
    visited=set()
    """ added visited list to prevent duplication in fringe"""
    closed=set()
    initial_state_name = problem.getStartState()
    initial_state=(initial_state_name , [] , 0)
    """ state STRUCT -> (state_name,state_path,state_cost) """
    fringe.push(initial_state)
    visited.add(initial_state_name)


    while not fringe.isEmpty():
        expanded_state= fringe.pop()
        (expanded_state_name,expanded_state_path,expanded_state_cost)=expanded_state
        closed.add(expanded_state_name)
        if(problem.isGoalState(expanded_state_name)):
            return expanded_state_path
        for state_name , state_action , state_cost in problem.getSuccessors(expanded_state_name):
            if not state_name in visited:
                if not state_name in closed:
                    new_state_name = state_name
                    new_state_path = expanded_state_path + [state_action]
                    new_state_cost = expanded_state_cost + state_cost
                    new_state=(new_state_name,new_state_path,new_state_cost)
                    fringe.push(new_state)
                    visited.add(new_state_name)

    return ["GOAL NOT FOUND"]
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    fringe=util.PriorityQueue()
    visitedcost={}
    closed=set()
    initial_state_name = problem.getStartState()
    initial_state=(initial_state_name , [] , 0)
    """ state STRUCT -> (state_name,state_path,state_cost) """
    fringe.push(initial_state,0)
    visitedcost[initial_state_name]=0


    while not fringe.isEmpty():
        expanded_state= fringe.pop()
        (expanded_state_name,expanded_state_path,expanded_state_cost)=expanded_state
        if expanded_state_name in closed:
            pass
        closed.add(expanded_state_name)
        if(problem.isGoalState(expanded_state_name)):
            return expanded_state_path
        for state_name , state_action , state_cost in problem.getSuccessors(expanded_state_name):
            if not state_name in closed:
                new_state_name = state_name
                new_state_path = expanded_state_path + [state_action]
                new_state_cost = expanded_state_cost + state_cost
                new_state=(new_state_name,new_state_path,new_state_cost)
                try:
                    if visitedcost[new_state_name]>new_state_cost :
                        fringe.push(new_state,new_state_cost)
                except:
                    fringe.push(new_state,new_state_cost)
                visitedcost[new_state_name]=new_state_cost

    return ["GOAL NOT FOUND"]


    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe=util.PriorityQueue()
    visitedfn={}
    closed=set()
    initial_state_name = problem.getStartState()
    initial_state=(initial_state_name , [] , 0)
    """ state STRUCT -> (state_name,state_path,state_cost) """
    initial_state_fn=0 + heuristic(initial_state_name,problem)
    fringe.push(initial_state,initial_state_fn)
    visitedfn[initial_state_name]=initial_state_fn


    while not fringe.isEmpty():
        expanded_state= fringe.pop()
        (expanded_state_name,expanded_state_path,expanded_state_cost)=expanded_state
        closed.add(expanded_state_name)
        if(problem.isGoalState(expanded_state_name)):
            return expanded_state_path
        for state_name , state_action , state_cost in problem.getSuccessors(expanded_state_name):
            if not state_name in closed:
                new_state_name = state_name
                new_state_path = expanded_state_path + [state_action]
                new_state_cost = expanded_state_cost + state_cost
                new_state=(new_state_name,new_state_path,new_state_cost)
                new_state_fn = new_state_cost + heuristic(new_state_name,problem)
                try:
                    if visitedfn[new_state_name]>new_state_fn :
                        fringe.push(new_state,new_state_fn)
                except:
                    fringe.push(new_state,new_state_fn)
                visitedfn[new_state_name]=new_state_fn

    return ["GOAL NOT FOUND"]
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
