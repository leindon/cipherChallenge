ciphered = input().lower().replace(" ","")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
frequencies = []
def algor(i):
    return i[1]
def otherAlgor(i):
    return i[0]
for letter in ciphered:
    if letter not in [l[0] for l in frequencies]:
        frequencies.append([letter, ciphered.count(letter)])
frequencies.sort(key=algor)
print(frequencies)
frequencies.sort(key=otherAlgor)
print(frequencies)
