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

from itertools import count
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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #Hacemos el algoritmo DFS basado en el BFS que proporciona el libro
    starNode = problem.getStartState() #Inicialiasamos la primera posicion
    pilita = util.Stack() #Hacemos la pila
    nodosVis = [] #La lista de nodos ya visitados
    pilita.push((starNode,[])) #Primer push
    while not pilita.isEmpty(): 
        nodoAct, actions = pilita.pop() #Hacemos un pop 
        if nodoAct not in nodosVis: #Si el nodo actual aun no fue visitado
            nodosVis.append(nodoAct) #Añadimos el nodo a los que ya fueron visitados
            if problem.isGoalState(nodoAct): #Si el nodo es la meta
                return actions #Regresamos las acciones que debe cumplir el agente para llegar a el
            for nNode, action, cost in problem.expand(nodoAct): #Si no es la meta expandimos el nodo al siguiente nodo
                nAction = actions + [action]  #suma las acciones que se deben de realizar para llegar al nuevo nodo
                pilita.push((nNode, nAction))  #Hacemos push a la pila con la posicion el nodo nuevo y sus acciones

    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Practicamente es lo mismo que DFS pero cambiamos a una pila a una cola
    starNode = problem.getStartState() #Primer estado del agente
    pilita = util.Queue() #Creamos la cola
    nodosVis = [] #creamos la llista de los nodo ya viditados
    pilita.push((starNode,[])) #Hacemos push de los primero elementos en la cola
    while not pilita.isEmpty(): #mientras la pila no este vacia
        nodoAct, actions = pilita.pop() #Hacemos pop de los elementos de la cola
        if problem.isGoalState(nodoAct): #Preguntamos si es la meta el nodo actual(posicion)
            return actions #regresamos las acciones que nos permiten llegar ahi
        if not nodoAct  in nodosVis: #Si no la posicion actual esta en la l
            nodosVis.append(nodoAct) #Guardamos el nodo en los que ya estan visitados
            for nNode, action, cost in problem.expand(nodoAct): #Expandimos el nodo
                nAction = actions + [action] #suma las acciones que se deben de realizar para llegar al nuevo nodo
                pilita.push((nNode, nAction))  #Hacemos push a la cola con la posicion el nodo nuevo y sus acciones

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #Este funcion a diferencia de las anteriores utiliza la heuristica

    pilita = util.PriorityQueue() #Creamos la cola
    cont = util.Counter() #Creamos un contador
    node = (problem.getStartState(), []) #Primer nodo
    cont[str(node[0])] += heuristic(node[0],problem) #Sumamos en el contador
    pilita.push(node,cont[str(cont[0])]) #Hacemos push en la cola
    nodosVis = [] #Creamos la lista de visitados


    while not pilita.isEmpty():#Mientras la cola no este vacia
        nodeAux, actions = pilita.pop() #Hcemos el pop
        if problem.isGoalState(nodeAux): #La posicion actual es la meta
            return actions #Regresamos las acciones que el agente debe llevar para llegar esa posicion
        if not nodeAux in nodosVis: #SI no esta en visitados
            nodosVis.append(nodeAux) #Agregar el nodo en visitados
            for nNode, action, cost in problem.expand(nodeAux): #Expandimos el nodo
                nAction = actions + [action] #Sumamaos las acciones para el nuevo nodo
                cont[str(nNode)] = problem.getCostOfActionSequence(nAction) #Creamos en el contador los costos para ese nodo
                cont[str(nNode)] += heuristic(nNode, problem) #Le sumamos la euristica para el costo de el nuevo nodo
                pilita.push((nNode, nAction), cont[str(nNode)]) #Hacemos push en la cola


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
