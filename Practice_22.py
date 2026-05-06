# Vowel Program
a = "-------------------------"
print(a)
print(">>>>> Vowel Program <<<<<")
print(a)
vowel = 0
print()
print()
# Input
word = input("Enter Any Word:").lower()
vowels = "aeiou"
# For loop
for i in word:
    if i in vowels:
        vowel += 1
# If/Else
if vowel == 1:
    print(f"\nThe word {word} has {vowel} Vowel")
elif vowel > 1:
    print(f"\nThe word {word} has {vowel} Vowels")
else:
    print("\nWord has no vowels")
print()
print()
# Thank You
print(a)
print(">> Thank You For Using <<")
print(a)
print()
print()
# Press Enter
input("{Press Enter}: To Exit")
