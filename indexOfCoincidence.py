ciphered = input("what is the ciphered text").replace(" ","")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
def blocker(text, length, offset):
    blocked = []
    adder = ""
    a = offset
    for letter in text:
        if a > 0:
            a -= 1
        else:
            if letter.lower() in alphabet:
                adder += letter.lower()
            if len(adder) == length:
                blocked.append(adder)
                adder = ""
    print(blocked)
    return blocked
def Iocer(list):
    Ioc = 0
    length = 0
    freq = [[],[]]
    for i in list:
        if i not in freq[1]:
            freq[1].append(i)
            freq[0].append(list.count(i))
        length += 1
    for i in freq[0]:
        Ioc+=(i*(i-1))
    Ioc /= length*(length-1)
    return Ioc
magicNumbers = [0.06505393453880672, 0.006954068888965075, 0.0011645100416382257, 0.0002072884387305877, 5.796101442862997e-05]
nGramProbabilites = [False for _ in range(len(magicNumbers))]
IndexOfCoincidences = []
for i,j in enumerate(magicNumbers):
    IndexOfCoincidence = Iocer(blocker(ciphered,i+1,0))
    if j*0.9< IndexOfCoincidence and IndexOfCoincidence <j*1.1:
        print("probably a "+str(i+1)+"gram cipher")
        nGramProbabilites[i] = True
    IndexOfCoincidences.append(IndexOfCoincidence)
print(IndexOfCoincidences)
print(nGramProbabilites)
# for this code you input the text and it uses the index of coincidence to predict whether it is a monogram cipher or not. I'll probably add detection for bigrams and higher but that takes a lot of frequency analysis so I'll do that later.