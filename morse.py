from table import MORSE_CODE_DICT

class MorseCode:
    def __int__(self,words,morseCode):
        self.words = words
        self.morseCode = morseCode

    def encrypt(self,words):
            code = ""
            for ch in words.upper():
                if ch in MORSE_CODE_DICT:
                    code += MORSE_CODE_DICT[ch] + " "
            return code.strip()
    def decrypt(self,morseCode):

        #we can reverse the dictionary to decode it
        reverse_dict = { value:key for key,value in MORSE_CODE_DICT.items()}

        decode = ""
        for ch in morseCode.split(" "):
           if ch in reverse_dict:
               decode += reverse_dict[ch]

        return decode.title()

