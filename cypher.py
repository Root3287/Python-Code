# Timothy A. Gibbons
# Cypher
import string;
import re;
def caesar(plain_text, shift):
    cipherText = ''
    for ch in plain_text:
      stayInAlphabet = ord(ch) + shift
      if ch.islower():
        if stayInAlphabet > ord('z'):
          stayInAlphabet -= 26
        elif stayInAlphabet < ord('a'):
          stayInAlphabet += 26
      elif ch.isupper():
        if stayInAlphabet > ord('Z'):
          stayInAlphabet -= 26
        elif stayInAlphabet < ord('A'):
          stayInAlphabet += 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
    #print(cipherText)
    return cipherText

def main():
	impt = input("Enter String to be encoded: ");
	offset = int(input("Enter offset"));
	print(caesar(impt, offset))