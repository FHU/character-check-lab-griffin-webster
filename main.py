#Remove pass and complete the code
def check_character(word, index):
   character = word[index]
   if character.isalpha():
       print("letter")
   elif character.isdigit():
       print("digit")
   elif character.isspace():
       print("white space")
   else:
       print("unknown")


if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
