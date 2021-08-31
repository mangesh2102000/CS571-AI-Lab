# Driver Code

# Import Required Functionalities 
from Utils import *
from puzzle import Puzzle, heuristicFuncList, heuristics
from SimulatedAnnealing import SimulatedAnnealing
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

coolingFuncList = [
    "1. maxTemperature*(0.9**iteration)",
    "2. maxTemperature/iteration"
]

# Run Algos one by one
#SimulatedAnnealing
def RunSimulatedAnnealing():
    
    print("\nEnter choice for heuristic")
    choice = int(input("0. Displced tiles Heuristic.\n1. Manhattan distance Heuristic.\n2. Displaced tile heuristic with blank tile cost included\n3. Manhattan distance heuristic with blank tile cost included\n4. Manhattan and displaced tile combined heuristic\n: "))

    if choice >= 5 or choice < 0:
        print("Invalid choice")
        sys.exit()

    maxTemperature = float(input("\nEnter the max temperature : "))
    cooling_function = int(input("\nEnter Cooling Function Choice\n1. maxTemperature*(0.9**iteration)\n2. maxTemperature/iteration\n: "))

    processes = []
    processes.append(SimulatedAnnealing(heuristics[choice],heuristicFuncList[choice],start_puzzle,maxTemperature,cooling_function))

    exec_info = [SimulatedAnnealing.run() for SimulatedAnnealing in processes]

    orig_stdout = sys.stdout
    file = open("output.txt", 'w')
    sys.stdout = file
    for idx, value in enumerate(exec_info):
        exec_time, path = value
        print(heuristics[choice],"heuristics")
        
        path.reverse()
        if not path:
            print("\nNo path available")

            print("\nStart State :")
            print(convertToInputFormat(START_STATE))

            print("Goal State :")
            print(convertToInputFormat(Puzzle.GOAL_STATE))

            print("Max temperature :", maxTemperature)

            print("\nCooling Function :", coolingFuncList[cooling_function-1])

            print("\nTotal number of states explored before termination :",processes[idx].exploredStates)
            print("-----------------------------------------------------")
        else:
            print("\nPath exists")
        
            print("\nStart State :")
            print(convertToInputFormat(START_STATE))

            print("Goal State :")
            print(convertToInputFormat(Puzzle.GOAL_STATE))

            print("Max temperature :", maxTemperature)

            print("\nCooling Function :", coolingFuncList[cooling_function-1])

            print("\nTotal number of states explored :",processes[idx].exploredStates)
            
            print("\nTotal number of states to optimal path : ", len(path))
            
            #print("\nOptimal Path :")
            # for step in path:
            #     print(convertToInputFormat(step.puzzleConfig))

            print("\nOptimal Path Cost :", len(path)-1)

            print("\nTime Taken For Execution :", exec_time, "seconds")
            print("-----------------------------------------------------")
    sys.stdout = orig_stdout
    file.close()

if __name__ == '__main__':
    print("\nRunning SimulatedAnnealing on the puzzle tile configuration")
    RunSimulatedAnnealing()
