words_by_elements = {}
words_by_index = {}
words_by_midpoint = {}
words_by_news = {}
words_by_scrabble = {}
words_by_typewriter = {}
words_by_units = {}
word_lists = (words_by_elements, words_by_index, words_by_midpoint, words_by_news, words_by_scrabble, words_by_typewriter, words_by_units)
score_letters = ('e','i','m','n','s','t','u')

# parse the wordfile

def log_word(word, scores):
    for i in range(len(word_lists)):
        word_list = word_lists[i]
        score = scores[i]
        if (score == None):
            continue
        if (score not in word_list):
            word_list[score] = []
        word_list[score].append(word)

for line in open('./word-with-scores.txt', 'r'):
    (word, e, i, m, n, s, t, u) = line.strip().split(' ')
    log_word(word, (e,i,m,n,s,t,u))

# parse each puzzle

def get_possibilities(word, scores):
    possibleWords = -1
    for i in range(len(word_lists)):
        # if (i == 1):
        #     continue
        word_list = word_lists[i]
        score = scores[i]
        if (score is None):
            continue
        if score in word_list:
            if (possibleWords == -1):
                possibleWords = set(word_list[score])
            else:
                possibleWords = possibleWords.intersection(set(word_list[score]))
        else:
            return set()
    return possibleWords

def puzzle_file_path(n):
    n = str(n)
    while len(n) < 4:
        n = '0' + n
    return './puzzle-e5d3f3d5ae/puzzles/puzzle'+n+'.txt'

histogram = {}
total = 0
with open("puzzle-answers.txt", "w") as outputFile:
    for i in range(10000):
        scores = [None, None, None, None, None, None, None]
        quit = False
        for line in open(puzzle_file_path(i)):
            if line[0:7] == 'special':
                continue
            score_letter = line[0]
            score = line.strip().split(' ')[2]
            scores[score_letters.index(score_letter)] = score
        if quit:
            continue
        res = get_possibilities(word, scores)
        #if res != None:
        #   print('Answer to puzzle #' + str(i) + ' is ' + str(res))

        if len(res) == 1:
            outputFile.write('Puzzle #' + str(i) + ': ' + str(next(iter(res))))
        if len(res) > 1:
            outputFile.write('Puzzle #' + str(i) + ': ' + str(list(res)))
        if len(res) < 1:
            outputFile.write('Puzzle #' + str(i) + ': ' + "NO_ANSWER")
        outputFile.write("\n")
        # if len(res) > 1:
        #     print('\t' + str(res))
        # if len(res) in histogram:
        #     histogram[len(res)] += 1
        # else:
        #     histogram[len(res)] = 1
        # total += 1
