# inputfile = [[y.strip() for y in x.split(',')] for x in open('demoinput.txt')]
inputfile = [[y.strip() for y in x.split(',')] for x in open('input.txt')]

def one():
    total = 0
    for i in inputfile:
        first = i[0].split('-')
        second = i[1].split('-')
        firstset = set()
        secondset = set()
        for number in range(int(first[0]), int(first[1])+1):
            firstset.add(number)
        for number in range(int(second[0]), int(second[1])+1):
            secondset.add(number)
        if firstset.intersection(secondset) == firstset or firstset.intersection(secondset) == secondset:
            total+=1
    print(total)

def two():
    total = 0
    for i in inputfile:
        first = i[0].split('-')
        second = i[1].split('-')
        firstset = set()
        secondset = set()
        for number in range(int(first[0]), int(first[1])+1):
            firstset.add(number)
        for number in range(int(second[0]), int(second[1])+1):
            secondset.add(number)
        if firstset.intersection(secondset):
            total+=1
    print(total)

if __name__ == "__main__":
    print("First:\n")
    one()
    print("\n\nSecond:\n")
    two()