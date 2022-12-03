letters = '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def one():
    total_priority = 0
    inputfile = open('demoinput.txt')
    for i in inputfile:
        halfway = int(len(i.strip())/2)
        first = set(i[:halfway])
        second = set(i[halfway:])
        repeat = first.intersection(second)
        for letter in repeat:
            points = letters.index(letter)
            total_priority += points
    print(total_priority)

def two():
    total_priority = 0
    inputfile = open('input.txt').readlines()
    trios = [[set(y.strip()) for y in inputfile[x:x+3]] for x in range(0,len(inputfile),3)]
    for trio in trios:
        repeat = trio[0].intersection(trio[1], trio[2])
        for letter in repeat:
            points = letters.index(letter)
            total_priority += points
    print(total_priority)

if __name__ == "__main__":
    print("First:\n")
    one()
    print("\n\nSecond:\n")
    two()