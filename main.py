# Elliot C, Isaac B
# 12/10/24
# Validating String Input (Tiered Assignment)

# Are you and your partner working on Level 1, Level 2 or Level 3 today?
# Working on Level...3

works = 1
works1 = 1
string = input("Type a word[6-10 letters long]")
if string != string.isalpha():
    print("That is not a word")
    works = 2

length = len(string)
if length < 6 and length > 10:
    print("Your word is to long or to short.")
    works1 = 2

if works == 2 and works1 == 2:
    print("Your word works")
if works == 1 and works1 == 1:
    print("Your word doesn't work")