#Remove pass and complete the code
def check_character(word, index):
   character = word[index]
   if character.isalpha():
       return "letter"
   elif character.isdigit():
       return "digit"
   elif character.isspace():
      return "white space"
   else:
       return "unknown"


if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))

#check