testing = input("what is the ciphered text")
tempTesting = testing.replace(" ","")
patterns = {}
distances = []
keyLengths = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
deciphered = ""
def sortAlgor(i):
    return i[1]
def factorise(number,max):
  factors = []
  for i in range(2,max+1):
    if number%i == 0:
      factors.append(i)
  return factors
def indexOfCoincidence(text):
  freq = [0 for _ in range(26)]
  length = 0
  for letter in text:
      if letter.lower() in alphabet:
          freq[alphabet.index(letter.lower())]+=1
          length += 1
  Ioc = 0
  for i in freq:
      Ioc+=(i*(i-1))
  Ioc /= length*(length-1)
  return Ioc
def chiSquared(text, minimum):
    #englishFrequency = [0.08551690673195275, 0.016047959168228293, 0.03164435380900101, 0.03871183735737418, 0.1209652247516903, 0.021815103969122528, 0.020863354250923158, 0.04955707280570641, 0.0732511860723129, 0.002197788956104563, 0.008086975227142329, 0.04206464329306453, 0.025263217360184446, 0.07172184876283856, 0.07467265410810447, 0.020661660788966266, 0.0010402453014323196, 0.0633271013284023, 0.06728203117491646, 0.08938126949659495, 0.026815809362304373, 0.01059346274662571, 0.018253618950416498, 0.0019135048594134572, 0.017213606152473405, 0.001137563214703838]
    englishFrequency = [0.0815, 0.0144, 0.0276, 0.0379, 0.1311, 0.0292, 0.0199, 0.0526, 0.0635, 0.0013, 0.0042, 0.0339, 0.0254, 0.071, 0.08, 0.019799999999999998, 0.0012, 0.0683, 0.061, 0.1047, 0.0246, 0.0092, 0.0154, 0.0017000000000000001, 0.019799999999999998, 0.0008]
    freq = [0 for _ in range(26)]
    for letter in text:
        if letter.lower() in alphabet:
            freq[alphabet.index(letter.lower())]+=1
    total = sum(freq)
    for i in range(26):
        freq[i]/=total
    chis = []
    for z in range(26):
        chi = 0
        for i in range(26):
            chi += ((freq[(i)%26]-englishFrequency[(i-z)%26])**2)/(englishFrequency[(i-z)%26])
        chis.append(chi)
    if minimum == True:
      return chis.index(min(chis))
    else:
      return chis

for i in range(3,11):
  for x in range(i-1,len(tempTesting)):
    test = ""
    for z in range(x+1-i,x+1):
      test = test + tempTesting[z]
    if tempTesting.count(test) > 1:
      if test in patterns:
        patterns[test].append(x+1-i)
      else:
        patterns[test] = [x+1-i]
deleteName = []
tdeleteName = []
tdeletePos = []
for pat in patterns:
    if tdeletePos == []:
        tdeletePos.append(patterns[pat][0])
        tdeleteName.append(pat)
    elif tdeletePos[-1]==patterns[pat][0]-1:
        tdeletePos.append(patterns[pat][0])
        tdeleteName.append(pat)
    elif len(tdeletePos) == 1:
        tdeletePos = []
        tdeleteName = []
        tdeletePos.append(patterns[pat][0])
        tdeleteName.append(pat)
    else:
        deleteName = deleteName + tdeleteName
        tdeleteName = []
        tdeletePos = []
        tdeletePos.append(patterns[pat][0])
        tdeleteName.append(pat)
for name in deleteName:
    patterns.pop(name)
for pat in patterns:
  print(pat+str(patterns[pat]))
  for i in range(len(patterns[pat])-1):
    distances.append(patterns[pat][i+1]-patterns[pat][i])
distances.sort()
for distance in distances:
  keyLengths = keyLengths + factorise(distance,20)
sortedKeyLengths = []
for key in keyLengths:
    if key not in [i[0] for i in sortedKeyLengths]:
        sortedKeyLengths.append([key,keyLengths.count(key)])
sortedKeyLengths.sort(key=sortAlgor, reverse=True)
print(sortedKeyLengths)

sets = [["" for _ in range(i+1)] for i in range(30)]
for x in range(0,30):
  for i in range(len(tempTesting)):
    sets[x][i%(x+1)] += tempTesting[i]
indexOfCoincidences = []
for s in sets:
  temp = 0
  for i in s:
    temp+=indexOfCoincidence(i)
  indexOfCoincidences.append([len(s),round(temp/len(s),5)])
indexOfCoincidences.sort(key=sortAlgor, reverse=True)
print(indexOfCoincidences)
keyLength = 0
key = ""
while True:
  keyLength = int(input("What is the key length"))
  key = ""
  possibleLetters = []
  for coset in sets[keyLength-1]:
    t= chiSquared(coset,minimum=False)
    possibleLetters.append(t)
    key += alphabet[t.index(min(t))]
  print(key)
  joke = 1
  while input("is this good yes or no").lower() == "no":
    joke+=1
    if joke == 2:
      print(str(joke) + "nd times the charm")
    elif joke > 2:
      print(str(joke) + "rd times the charm")
    if joke > 10:
      print("maybe the key length is just wrong, you can change it by saying yes when i as is this good yes or no.")
    letterNumber = int(input("what letter do you want to change (start counting from 0)"))
    options = [[alphabet[i],round(possibleLetters[letterNumber][i],3)] for i in range(26)]
    print("Your options are:")
    options.sort(key=sortAlgor)
    print(options)
    print("The lower the better btw")
    change = input("What letter should it be now?")
    tkey = ""
    for i in range(len(key)):
      if i == letterNumber:
        tkey+=change
      else:
        tkey += key[i]
    key=tkey
    print(key)
  deciphered = ""
  pos = 0
  for letter in testing:
    if letter.lower() in alphabet:
      deciphered += alphabet[alphabet.index(letter.lower())-alphabet.index(key[pos%len(key)])%26]
      pos += 1
    else:
      deciphered += letter
  print(deciphered)
  if input("are you satisfied with this decoding? type yes for yes").lower() == "yes":
    if joke == 1:
      print("lets go it only took "+ str(joke)+" try")
    else:
      print("lets go it only took "+ str(joke)+" tries")
    print("heres the key and the deciphered text")
    break
print(key)
print(deciphered)

# it outputs results in a list of the form [key length, likelihood]
# the first list is using kasiski's examination and the second is using the index of coincidence.
# once you get the key length there are ways of getting the key which I will code later.
# also if you get the error division by zero why are you entering in a text shorter than 20 characters. (i will fix this eventually)
# vigenereSolverLAlphabet.py is an updated version