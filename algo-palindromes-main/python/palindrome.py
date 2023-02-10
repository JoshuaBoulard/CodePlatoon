def palindrome(string):
    string = str(string)
    string = string.lower()
    new_string = ''
    for char in string:
        if char.isalnum():
            new_string += char
        
    reverse_string = new_string[::-1]
   
    if reverse_string == new_string:
        return True
    else:
        return False

print(palindrome('A man, a plan, a canal -- Panama'))
