testing = input("what is the ciphered text").replace(" ","")
patterns = {}
countedPatterns = []
distances = []
patLengths = []
def sortAlgor(i):
    return i[1]
def weirdAlgor(i):
  return len(i[0][0])
def factorise(number,max):
  factors = []
  for i in range(2,max+1):
    if number%i == 0:
      factors.append(i)
  return factors
for i in range(3,11):
  for x in range(i-1,len(testing)):
    test = ""
    for z in range(x+1-i,x+1):
      test = test + testing[z]
    if testing.count(test) > 1:
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
  if len(pat) not in patLengths:
    patLengths.append(len(pat))
    countedPatterns.append([])
  countedPatterns[patLengths.index(len(pat))].append([pat,len(patterns[pat])])
for i in range(len(countedPatterns)):
  countedPatterns[i].sort(key=sortAlgor)
print(countedPatterns)
countedPatterns.sort(key=weirdAlgor)
for i in countedPatterns:
  for z in i:
    print(z[0] + ": " + str(z[1]))