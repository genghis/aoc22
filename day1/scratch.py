def one():
    print(max([sum(int(y) for y in x.split('\n')) for x in open('input.txt').read().split('\n\n')]))
    
def two():
    print(sum(sorted([sum(int(y) for y in x.split('\n')) for x in open('input.txt').read().split('\n\n')])[-3:]))

if __name__ == "__main__":
    print("\nFirst:")
    one()
    print("\nSecond:")
    two()