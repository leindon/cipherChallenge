# so heres my attempt at a better vigenere solver that works with an extended alphabet
# i might redesign other solvers that i made cause my code was/is geniunely abysmal
caseSensitive = True
maxKeyLength = 30

# stuff to do:
# ioc for keyword length
# chi squared for deciphering

resultantAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet = []
keyLength = 0

cipherText = input().replace(" ","")

def patternDetector(text):
    # improve this later by making it not repeat for smaller versions of the same pattern
    # ill improve this soonish trust
    patterns = {}
    for i in range(10,2,-1):
        for j in range(len(text)-i):
            pattern = text[j:j+i]
            occurences = []
            search = 0
            while True:
                search = text.find(pattern, search)
                if search == -1:
                    break
                occurences.append(search)
                search += len(pattern)
            counts = len(occurences)

            if counts > 1:
                patterns[pattern] = occurences
    return patterns

def patternDifferences(patterns):
    # i mean ig [0, 100, 200] would only return [100, 100] not [100, 100, 200] tho idk if thats necessary
    distances = []
    for pattern in patterns.values():
        for i in range(1,len(pattern)):
            distances.append(pattern[i] - pattern[i-1])
    return distances

def factorise(distances):
    print(distances)
    # if the factor list has a number multiple times it factors it multiple times which seems like an inefficiency
    factors = {i:0 for i in range(3,maxKeyLength+1)}
    for i in distances:
        for factor in factors:
            if i % factor == 0:
                factors[factor] += 1
    sortedList = {k: v for k, v in sorted(factors.items(), key=lambda item: item[1], reverse = True)} #magic code that i found online
    return sortedList

def Iocer(lst):
    Ioc = 0
    length = 0
    freq = {}
    for i in lst:
        if i not in freq:
            freq[i] = lst.count(i)
        length += 1
    for i in freq.values():
        Ioc+=(i*(i-1))
    Ioc /= length*(length-1)
    return Ioc

def keywordIocer(ciphertext):
    return {k: v for k, v in sorted({length:sum([Iocer("".join([ciphertext[x] for x in range(i, len(ciphertext), length)])) for i in range(length)])/length for length in range(3,maxKeyLength+1)}.items(), key=lambda item: item[1], reverse = True)} # i love code golf

def chiSquaredTest(comparison):
    destinationFrequency = [] # finish this
    

print(factorise(patternDifferences(patternDetector(cipherText))))
print(keywordIocer(cipherText))


