grid = []
# mapping, instructionstring = open('demoinput.txt').read().split('\n\n')
mapping, instructionstring = open('input.txt').read().split('\n\n')
instructions = instructionstring.split('\n')

def gridgen():
    grid.clear()
    crates = mapping.split('\n')
    for ind,val in enumerate(crates[-1]):
        if val != ' ':
            newrow = []
            for i in crates[:-1]:
                if i[ind] != ' ':
                    newrow.insert(0, i[ind])
            grid.append(newrow)

def move(quantity, origin, destination):
    for i in range(quantity):
        crate = grid[origin].pop()
        grid[destination].append(crate)

def movebatch(quantity, origin, destination):
    stack = grid[origin][-quantity:]
    grid[destination].extend(stack)
    del grid[origin][-quantity:]
    
def one():
    gridgen()
    for instruction in instructions:
        instruction_set = instruction.split(' ')
        move(int(instruction_set[1]), int(instruction_set[3])-1, int(instruction_set[5])-1)
    answer = ''
    for line in grid:
        answer+=line[-1]
    print(answer)

def two():
    gridgen()
    for instruction in instructions:
        instruction_set = instruction.split(' ')
        movebatch(int(instruction_set[1]), int(instruction_set[3])-1, int(instruction_set[5])-1)
    answer = ''
    for line in grid:
        if line:
            answer += line[-1]
    print(answer)

if __name__ == "__main__":
    print("First:\n")
    one()
    print("\n\nSecond:\n")
    two()