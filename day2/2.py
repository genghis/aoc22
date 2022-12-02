def one():
    results = {
        'X': {
           'score': 1,
           'A': 3,
           'B': 0,
           'C': 6 
        },
        'Y': {
            'score': 2,
            'A': 6,
            'B': 3,
            'C': 0
        },
        'Z': {
            'score': 3,
            'A': 0,
            'B': 6,
            'C': 3
        }
    }
    games = [x.strip().split(' ') for x in open('input.txt')]
    total_score = 0
    for game in games:
        theirs,mine = game[0], game[1]
        round = results[mine]['score']+results[mine][theirs]
        total_score += round
    print(total_score)

def two():
    results = {
        'X': {
           'score': 0,
           'A': 3,
           'B': 1,
           'C': 2 
        },
        'Y': {
            'score': 3,
            'A': 1,
            'B': 2,
            'C': 3
        },
        'Z': {
            'score': 6,
            'A': 2,
            'B': 3,
            'C': 1
        }
    }
    games = [x.strip().split(' ') for x in open('input.txt')]
    total_score = 0
    for game in games:
        theirs,mine = game[0], game[1]
        round = results[mine]['score']+results[mine][theirs]
        total_score += round
    print(total_score)

if __name__ == "__main__":
    print("First:\n")
    one()
    print("\n\nSecond:\n")
    two()