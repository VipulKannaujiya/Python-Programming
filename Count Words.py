def count_words(s):
    result = 1
    for ch in s:
        if(ch == " "):
            result = result + 1
    return result

text = input("Enter any string : ")
print(count_words(text))