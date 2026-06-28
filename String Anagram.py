def is_anagram(s1, s2):
    if len(s1) != len(s2):
        print(s1, "&", s2, "is not anagram")
        return
    elif sorted(s1) == sorted(s2):
        print(s1, "&", s2, "is anagram")
    else:
        print(s1, "&", s2, "is not anagram")

s1 = input("Enter Your First Word : ")
s2 = input("Enter Your Second Word : ")
is_anagram(s1, s2)