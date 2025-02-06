# Know your DEVIL name
import random
import string
n=input("Give your name to the Devil =")
a=n[::-1]
letters = string.ascii_letters
s=(''.join(random.choice(letters))+ a + ''.join(random.choice(letters) for i in range(4)))
print(s)