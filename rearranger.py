ciphered = input("what is the cipher text ").upper()
cipheredList = ciphered.split()
cipheredLetters = []
for letter in ciphered:
    cipheredLetters.append(letter)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
blocked = []
spaces = []
key = [[],[]]
length = int(input("what is the length you want it to be split into "))
adder = ""
for letter in ciphered:
    if letter == " ":
        spaces.append(letter)
    else:
        adder = adder + letter
        if len(adder) == length:
            blocked.append(adder)
            adder = ""
if adder != "":
    blocked.append(adder)
print(blocked)
freq = []
for block in blocked:
    if block not in [i[0] for i in freq]:
        freq.append([block,blocked.count(block)])
        print(block+": "+str(blocked.count(block)))

deciphered = ""
rearrangement = input("what should each block be rearranged by. Type the numbers with spaces between").split()
for i in range(len(rearrangement)):
    rearrangement[i] = int(rearrangement[i])
    rearrangement[i] -= 1
for block in blocked:
    if len(block) < len(rearrangement):
        print("what do we do with this bro")
        print(block)
        print("type what you want it to be rearranged into.")
        deciphered+= input()
    else:
        for i in rearrangement:
            deciphered+= block[i]
        deciphered+= " "
print(deciphered)