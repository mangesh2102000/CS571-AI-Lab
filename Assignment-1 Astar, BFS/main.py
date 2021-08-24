# Driver Code

# Import Required Functionalities 
from Utils import *
from puzzle import Puzzle, heuristicFuncList
from BFS import BFS
from Astar import Astar
from time import time
import sys

# Input
START_STATE = inputFromFile('StartState')
GOAL_STATE  = inputFromFile('GoalState')

# Check for Valid Input
if not Puzzle.legitPuzzle(START_STATE) or not Puzzle.legitPuzzle(GOAL_STATE):
    print("Error: Puzzle Tiles configuration is invalid")
    print("\nStart State :")
    print(convertToInputFormat(START_STATE))

    print("Goal State :")
    print(convertToInputFormat(Puzzle.GOAL_STATE))
    sys.exit()

if GOAL_STATE: 
    Puzzle.GOAL_STATE = GOAL_STATE

start_puzzle = Puzzle(START_STATE)

# Run Algos one by one
#BFS
def RunBFS():
    processes = []
    for heuristic, heuristicFunc in heuristicFuncList.items():
        processes.append(BFS(heuristic,heuristicFunc,start_puzzle))

    exec_info = [bfs.run() for bfs in processes]

    for idx, value in enumerate(exec_info):
        exec_time, path = value
        print(processes[idx].heuristic,"heuristics")
        
        path.reverse()
        if not path:
            print("\nNo path available")

            print("\nStart State :")
            print(convertToInputFormat(START_STATE))

            print("Goal State :")
            print(convertToInputFormat(Puzzle.GOAL_STATE))

            print("Total number of states explored before termination :",processes[idx].exploredStates)
            print("-----------------------------------------------------")
        else:
            print("\nPath exists")
        
            print("\nStart State :")
            print(convertToInputFormat(START_STATE))

            print("Goal State :")
            print(convertToInputFormat(Puzzle.GOAL_STATE))

            print("Total number of states explored :",processes[idx].exploredStates)
            
            print("\nTotal number of states to optimal path : ", len(path))
            
            print("\nOptimal Path :")
            for step in path:
                print(convertToInputFormat(step.puzzleConfig))

            print("\nOptimal Path Cost :", len(path)-1)

            print("\nTime Taken For Execution :", exec_time, "seconds")
            print("-----------------------------------------------------")

#Astar
def RunAstar():
    processes = []
    for heuristic, heuristicFunc in heuristicFuncList.items():
        processes.append(Astar(heuristic,heuristicFunc,start_puzzle))

    exec_info = [astar.run() for astar in processes]

    for idx, value in enumerate(exec_info):
        exec_time, path = value
        print(processes[idx].heuristic,"heuristics")
        
        path.reverse()
        if not path:
            print("\nNo path available")

            print("\nStart State :")
            print(convertToInputFormat(START_STATE))

            print("Goal State :")
            print(convertToInputFormat(Puzzle.GOAL_STATE))

            print("Total number of states explored before termination :",processes[idx].exploredStates)
            print("-----------------------------------------------------")
        else:
            print("\nPath exists")
        
            print("\nStart State :")
            print(convertToInputFormat(START_STATE))

            print("Goal State :")
            print(convertToInputFormat(Puzzle.GOAL_STATE))

            print("Total number of states explored :",processes[idx].exploredStates)
            
            print("\nTotal number of states to optimal path : ", len(path))
            
            print("\nOptimal Path :")
            for step in path:
                print(convertToInputFormat(step.puzzleConfig))

            print("\nOptimal Path Cost :", len(path)-1)

            print("\nTime Taken For Execution :", exec_time, "seconds")
            print("-----------------------------------------------------")

if __name__ == '__main__':
    print("Running BFS on the puzzle tile configuration\n")
    RunBFS()
    print("Running Astar on the puzzle tile configuration\n")
    RunAstar()
