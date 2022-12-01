input = open("input.txt","r").read()

def one():
    elves_raw = [i for i in input.split("\n")]
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
    elves_raw = [i for i in input.split("\n")]
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