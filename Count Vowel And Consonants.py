def count_vowels_consonants(s):
    vowel_count = 0
    consonant_count = 0

    for ch in s:
        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            vowel_count += 1
        elif ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
            consonant_count += 1
    
    return vowel_count, consonant_count

s = input("Enter any string : ")
v, c = count_vowels_consonants(s)
print("Vowel = ", v)
print("Consonant = ", c)