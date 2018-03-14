# Caesar cipher - Implement a Caesar cipher, both encoding and decoding. The key is an integer
# from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces
# each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts
# "HI" to "JK", but key 20 encrypts "HI" to "BC". This simple "monoalphabetic substitution cipher"
# provides almost no security, because an attacker who has the encoded message can either use frequency
# analysis to guess the key, or just try all 25 keys.
import string
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.INFO) #turn off logging
# logging.debug(string.ascii_lowercase)
logging.debug(string.ascii_uppercase)

class coding():

    def __init__(self,password,code,flag, alphabet=(string.ascii_uppercase)):
        self.password = password.upper()
        self.code = code
        self.flag = flag
        self.alphabet = alphabet


# If flag == 0 then encoding else decoding
    def cod(self):

        result = ''
        # encoding
        if self.flag == 0:

            for i in self.password:
                position = self.alphabet.index(i) + self.code

                if position >len(self.alphabet) - 1:
                    position = position - len(self.alphabet)
                result= result + (self.alphabet[position])

            return result
        # decoding
        else:
            for i in self.password:
                position = self.alphabet.index(i) - self.code

                if position < 0:
                    position = len(self.alphabet) + position
                result= result + (self.alphabet[position])

            return result

print ('--encoding--')
encoding = coding('KONRAD',5,0)
print(encoding.password)
print(encoding.cod())

print ('--decoding--')
decoding = coding('PTSWFI',5,1)
print(decoding.password)
print(decoding.cod())










