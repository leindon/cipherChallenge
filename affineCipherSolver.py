a = [1,3,5,7,9,11,15,17,19,21,23,25]
b = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
original = alphabet.index(input("what is the letter"))
current = alphabet.index(input("what is the letter meant to be"))
for i in a:
  b.append((original-current*i)%26)
  print("a="+str(i)+" b="+str((original-current*i)%26))

#use frequency analysis to find the most common letter, then you can input e for the first question and the most common letter for the second.
#also note this outputs the a and b for encoding, cause the cipherchallenge tools auto reverses it for u