from itertools import permutations
import math

def letterval(letter):
    return ord(letter.lower()) - 96

def scrabble_scores():
    return {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
           "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
           "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
           "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
           "x": 8, "z": 10}

allElements = {"h":1,"he":2,"li":3,"be":4,"b":5,"c":6,"n":7,"o":8,"f":9,"ne":10,"na":11,"mg":12,"al":13,"si":14,"p":15,"s":16,"cl":17,"ar":18,"k":19,"ca":20,"sc":21,"ti":22,"v":23,"cr":24,"mn":25,"fe":26,"co":27,"ni":28,"cu":29,"zn":30,"ga":31,"ge":32,"as":33,"se":34,"br":35,"kr":36,"rb":37,"sr":38,"y":39,"zr":40,"nb":41,"mo":42,"tc":43,"ru":44,"rh":45,"pd":46,"ag":47,"cd":48,"in":49,"sn":50,"sb":51,"te":52,"i":53,"xe":54,"cs":55,"ba":56,"la":57,"ce":58,"pr":59,"nd":60,"pm":61,"sm":62,"eu":63,"gd":64,"tb":65,"dy":66,"ho":67,"er":68,"tm":69,"yb":70,"lu":71,"hf":72,"ta":73,"w":74,"re":75,"os":76,"ir":77,"pt":78,"au":79,"hg":80,"tl":81,"pb":82,"bi":83,"po":84,"at":85,"rn":86,"fr":87,"ra":88,"ac":89,"th":90,"pa":91,"u":92,"np":93,"pu":94,"am":95,"cm":96,"bk":97,"cf":98,"es":99,"fm":100,"md":101,"no":102,"lr":103,"rf":104,"db":105,"sg":106,"bh":107,"hs":108,"mt":109}

def elements(word):
    total = 0
    word = word.lower()
    length = len(word)
    for i in xrange(0,length):
        if word[i] in allElements:
            total += allElements[word[i]]
        if i < len(word) - 1 and word[i:i+2] in allElements:
            total += allElements[word[i:i+2]]
    return total

def elements(word):
    total = 0
    word = word.lower()
    length = len(word)
    for i in xrange(0,length):
        if word[i] in allElements:
            total += allElements[word[i]]
        if i < len(word) - 1 and word[i:i+2] in allElements:
            total += allElements[word[i:i+2]]
    return total

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

def index(word):
    index = 1
    remainingLetters = len(word) - 1
    frequencies = {}
    splitString = list(word)
    sortedStringLetters = sorted(splitString)

    for val in sortedStringLetters:
        if (val not in frequencies):
            frequencies[val] = 1
        else:
            frequencies[val] += 1

    def factorial(coefficient):
        return math.factorial(coefficient)

    def getSubPermutations(sorted, currentLetter):
        if currentLetter in sorted:
            sorted[currentLetter] -= 1

        denominator = 1
        for key in sorted:
            subPermutations = factorial(sorted[key])
            if subPermutations != 0:
                denominator *= subPermutations

        if currentLetter in sorted:
            sorted[currentLetter] += 1

        return denominator

    splitStringIndex = 0
    while len(sortedStringLetters) > 0:
        for i in range(len(sortedStringLetters)):
            if (sortedStringLetters[i] != splitString[splitStringIndex]):
                if (sortedStringLetters[i] != sortedStringLetters[i+1]):
                    permutations = factorial(remainingLetters)
                    index += permutations / getSubPermutations(frequencies, sortedStringLetters[i])
                else:
                    continue
            else:
                splitStringIndex += 1
                if sortedStringLetters[i] in frequencies:
                    frequencies[sortedStringLetters[i]] -= 1
                del sortedStringLetters[i]
                remainingLetters -= 1
                break

    return index

def news(word):
    position = [0, 0]
    for i in word.lower():
        if i == 'n':
            position[0] += 1
        elif i == 'e':
            position[1] += 1
        elif i == 'w':
            position[1] -= 1
        elif i == 's':
            position[0] -= 1
    return round(math.sqrt(position[0]**2 + position[1]**2), 3)

def scrabble(word):
    score = scrabble_scores()
    return sum([score[i] for i in word.lower()])

def units(word):
    return len(word)

def typewriter(word):
    upper = 'qwertyuiop'
    return sum([1 if i in upper else 0 for i in word.lower()])

def midpoint(word):
    total = sum([letterval(i) for i in word])
    midpoint = float(total)/2.0
    count = 0
    result = None
    for (idx, letter) in enumerate(word):
        if count + letterval(letter) == midpoint:
            result = float(idx + 1)
            break
        elif count + letterval(letter) > midpoint:
            target = midpoint - count
            fraction = target / float(letterval(letter))
            result = idx + fraction
            break
        else:
            count = count + letterval(letter)
    return round(result, 3)

def generateScores(word):
    elementsScore = str(elements(word))
    indexScore = str(index(word))
    midpointScore = str(midpoint(word))
    newsScore = str(news(word))
    scrabbleScore = str(scrabble(word))
    typewriterScore = str(typewriter(word))
    unitsScore = str(units(word))

    return word + " " + elementsScore + " " + indexScore + " " + midpointScore + " " + newsScore + " " + scrabbleScore + " " + typewriterScore + " " + unitsScore + "\n"

def main():
    count = 0
    with open("puzzle-e5d3f3d5ae/words.txt", "r") as dictionaryFile:
        with open("word-with-scores.txt", "w") as outputFile:
            for line in dictionaryFile:
                count += 1
                print(count)
                outputFile.write(generateScores(line.strip()))

main()
