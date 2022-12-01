demo = 0

if demo == True:
    input = 'demoinput.txt'
else:
    input = 'input.txt'

def one():
    elves_raw = [x.strip() for x in open(input)]
    elves = []
    temp = 0
    for i in elves_raw:
        if i == "":
            elves.append(temp)
            temp = 0
        else:
            temp+=int(i)
    print(max(elves))

def two():
    elves_raw = [x.strip() for x in open(input)]
    elves = []
    temp = 0
    for i in elves_raw:
        if i == "":
            elves.append(temp)
            temp = 0
        else:   
            temp+=int(i)
    elves.append(temp)
    elves.sort(reverse = True)
    print(sum(elves[0:3]))

if __name__ == "__main__":
    print("First:\n")
    one()
    print("\n\nSecond:\n")
    two()