# Formal Languages - Assignment 1
## DFA Simulator 

## Name
Alejandro Restrepo Osorio

## System version and programming language used

- Windows 11 
- Python 3.13.5

## How to run the code

1. Execute the program with:
   ```
   python main.py
   ```

2. Enter a string composed of symbols 'a' and 'b' when prompted

3. The program will:
   - Display the state transitions in the console
   - Save all output to `States.txt` file in the same directory

## Explanation of the code

### What the program does:

The program simulates a **Deterministic Finite Automata (DFA)** based on the finite automaton diagram from section 3.19 of the reference book. It processes an input string symbol by symbol and determines whether the string is accepted or rejected by the automaton.

### DFA Structure:

**States:** 0137 (initial), 247, 7, 8, 58, 68

**Alphabet:** {a, b}

**Accepting States:** {8, 58, 68} 

**Transition Table:**
- From state `0137`: a → 247, b → 8
- From state `247`: a → 7, b → 58
- From state `7`: a → 7 (self-loop), b → 8
- From state `8`: b → 68
- From state `58`: b → 68
- From state `68`: b → 8

### Program Logic:

1. **Input Reading:** The program prompts the user to enter a string composed of 'a' and 'b' symbols

2. **State Processing:** For each symbol in the input string:
   - Checks if there exists a valid transition from the current state
   - If valid: moves to the next state and logs the transition
   - If invalid: stops processing and rejects the string

3. **Output:** 
   - Prints the initial state
   - Displays each state transition in the format: `current_state ---symbol---> next_state`
   - Shows the final state and acceptance status (ACCEPTED or REJECTED)

4. **File Logging:** All console output is simultaneously written to `States.txt` for record keeping

### Example Execution:

**Input:** `abb`

**Expected Output:**
```
Start state: 0137
0137 -------a-------> 247
247 -------b-------> 58
58 -------b-------> 68

Final state: 68
String ACCEPTED
```

(Since 68 is an accepting state, the string is accepted)