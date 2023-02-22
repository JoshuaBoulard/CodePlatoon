def palindrome(string):
    base_string = str(string).lower()
    alpha_str = ''
    for char in base_string:
        if char.isalnum():
            alpha_str += char
    
    def reverse(reverse_str):
        if len(reverse_str) == 0:
            return reverse_str
        else:
            return reverse(reverse_str[1:]) + reverse_str[0]
        
    reversed_string = reverse(alpha_str)

    if reversed_string == alpha_str:
        return True 
    else:
        return False

print(palindrome('Sore was I ere I saw Eros.'))
print(palindrome("A man, a plan, a canal -- Panama"))
print(palindrome(4664))