# inputfile = open('demoinput.txt').read().split('\n')
inputfile = open('input.txt').read().split('\n')

def solve(window):
    for code in inputfile:
        for i,v in enumerate(code):
            chunk = code[i:i+window]
            if len(set(chunk)) == window:
                print(i+window)
                break

def one():
    window = 4
    solve(window)
    
def two():
    window = 14
    solve(window)

if __name__ == "__main__":
    print("First:\n")
    one()
    print("\n\nSecond:\n")
    two()