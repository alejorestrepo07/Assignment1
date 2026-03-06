transitions = { #Transitions of the DFA
    "0137": {"a": "247", "b": "8"},
    "247": {"a": "7", "b": "58"},
    "7": {"a": "7", "b": "8"},
    "8": {"b": "68"},
    "58": {"b": "68"},
    "68": {"b": "8"}
}

state = "0137" #Initial state of the DFA

accepting_states = {"8", "58", "68"} #Set of accepting states


string = input("Enter a string (a,b): ") #Read the input string "a or b"

with open("States.txt", "w") as file: #File to write the states and transitions during the processing of the input string
    
    def log(message):  #Function to log the messages of the console in the file as well
        print(message)
        file.write(message + "\n")
    
    log("\nStart state: " + state) #Print the initial state
    
    for symbol in string: #Loop over each symbol in the input string
        if symbol in transitions.get(state, {}): #Check if there is a transition for the current state and symbol
            next_state = transitions[state][symbol] #Get the next state from the transitions table
            log(f"{state} -------{symbol}-------> {next_state}")
            state = next_state #Update the current state to the next state
        else:
            log(f"No transition from {state} with '{symbol}'") #if there is no valid transition, print an error message
            state = None
            break
    
    if state in accepting_states: #Check if the final state is an accepting state
        log("\nFinal state: " + state) #Print the final state
        log("String ACCEPTED")
    else:
        log("\nFinal state: " + state)
        log("String REJECTED")

