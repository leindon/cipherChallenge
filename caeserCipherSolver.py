ciphered = input("what is the ciphered text").lower()
#englishFrequency = [0.08551690673195275, 0.016047959168228293, 0.03164435380900101, 0.03871183735737418, 0.1209652247516903, 0.021815103969122528, 0.020863354250923158, 0.04955707280570641, 0.0732511860723129, 0.002197788956104563, 0.008086975227142329, 0.04206464329306453, 0.025263217360184446, 0.07172184876283856, 0.07467265410810447, 0.020661660788966266, 0.0010402453014323196, 0.0633271013284023, 0.06728203117491646, 0.08938126949659495, 0.026815809362304373, 0.01059346274662571, 0.018253618950416498, 0.0019135048594134572, 0.017213606152473405, 0.001137563214703838]
englishFrequency = [0.0815, 0.0144, 0.0276, 0.0379, 0.1311, 0.0292, 0.0199, 0.0526, 0.0635, 0.0013, 0.0042, 0.0339, 0.0254, 0.071, 0.08, 0.019799999999999998, 0.0012, 0.0683, 0.061, 0.1047, 0.0246, 0.0092, 0.0154, 0.0017000000000000001, 0.019799999999999998, 0.0008]
freq = [0 for _ in range(26)]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
for letter in ciphered:
    if letter.lower() in alphabet:
        freq[alphabet.index(letter.lower())]+=1
total = sum(freq)
for i in range(26):
   freq[i]=freq[i]/total
chis = []
for z in range(26):
    chi = 0
    for i in range(26):
        chi += ((freq[(i)%26]-englishFrequency[(i-z)%26])**2)/(englishFrequency[(i-z)%26])
    chis.append(chi)
deciphered = ""
print(chis)
print(min(chis))
print(alphabet[chis.index(min(chis))])
for letter in ciphered:
    if letter in alphabet:
        deciphered+=alphabet[(alphabet.index(letter)-chis.index(min(chis)))%26]
    else:
        deciphered += letter
print(deciphered)
# this was mostly made for the vigenere cipher solver cause caeser ciphers r so easy
# it uses the chi squared method to auto solve caeser ciphers.