
def one():

    input = [sum(x for y in int(x.split('\n'))) for x in open('demoinput.txt').read().split("\n\n")]
    print(input)
    # elves_raw = [i for i in input.split("\n")]
    # print(elves_raw)

    # elves = []
    # temp = 0
    # for i in elves_raw:
    #     if i == "":
    #         elves.append(temp)
    #         temp = 0
    #     else:
    #         temp+=int(i)
    # print(max(elves))

if __name__ == "__main__":
    print("First:\n")
    one()