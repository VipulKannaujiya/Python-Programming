def frequency_of_character(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    for key in freq:
        print(" ", key, ":", freq[key])
    
text = input("Enter any string : ")
frequency_of_character(text)