from collections import defaultdict

# Jug capacities and target amount
jug1, jug2, aim = 4, 3, 2
visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2):
    # Check if we reached the target amount
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True

    # Check if this state has already been visited
    if visited[(amt1, amt2)] == False:
        visited[(amt1, amt2)] = True
        print(amt1, amt2)

        # Explore all possible actions
        return (waterJugSolver(0, amt2) or      # Empty jug1
                waterJugSolver(amt1, 0) or      # Empty jug2
                waterJugSolver(jug1, amt2) or   # Fill jug1
                waterJugSolver(amt1, jug2) or   # Fill jug2
                waterJugSolver(amt1 - min(amt1, jug2 - amt2), amt2 + min(amt1, jug2 - amt2)) or  # Pour jug1 into jug2
                waterJugSolver(amt1 + min(amt2, jug1 - amt1), amt2 - min(amt2, jug1 - amt1))     # Pour jug2 into jug1
               )

# Start the solver with both jugs empty
waterJugSolver(0, 0)
