def remove_space(s):
    rev = ""
    for ch in s:
        if ch != " ":
            rev = rev + ch
    
    return rev

txt = input("Enter any string : ")
print(remove_space(txt))