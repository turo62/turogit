
def get_input():
    gamest = []
    stats = open("/home/turoczi/Dokumentumok/python/game-statistics-python-turo62/game_stat.txt", 'r')
    for line in stats.readlines():
        gamest.append(line.strip())
    return gamest

def repl_ch(gamest):
    input_file = []
    length = len(gamest)
    i = 0
    while i <= length-1:
        item = gamest[i]
        item = item.split("\t")
        input_file.append(item)
        i += 1
    return input_file

def count_games(input_file):
    result = len(input_file)
    return result

def input_year():
        year = int(input("Enter a year: "))
        return year


def decide(input_file, year):
    result = year
    for row in input_file:
        for z in row:
            i = 0
            if input_file[i][2] != result:
                result = False
            i += 1
        else:
            result = True
    return result

def get_latest(input_file):
    result = 0
    N = len(input_file)
    for i in range(N):
        i = 0
        while i <= N - 2:
            if input_file[i][2] > input_file[i+1][2]:
                temp = input_file[i+1][2]
                input_file[i+1][2] = input_file[i][2]
                input_file[i][2] = temp
            else:
                i = i+1
    result = input_file[i][2]
    return result

def create_file(input_file):
    with open('your_file.txt', 'w') as f:
            for row in input_file:
                f.write("%s\n" % row)
            f.close

def main():
        gamest = get_input()
        input_file = repl_ch(gamest)
        result = count_games(input_file)
        print(result)
        create_file(input_file)
        year = input_year()
        result = decide(input_file,year)
        print(result)
        result = get_latest(input_file)
        print(result)


if __name__ == '__main__':
        main()
