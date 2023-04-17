move=0
# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    global move
    hanoi(disks - 1, source, destination, helper)
    move = move+1
    print('move {} Disk {} moves from tower {} to tower {}.'.format(move, disks, source, destination))
    move = move+1
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))

# Actual function call
hanoi(disks, 'A', 'B', 'C')