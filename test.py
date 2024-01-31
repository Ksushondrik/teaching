# from colorama import Fore, Back, Style

# print(Fore.RED + 'Це червоний текст')
# print(Back.GREEN + 'Це текст на зеленому фоні')
# print(Style.RESET_ALL)
# print('Це звичайний текст після скидання стилю')

def is_palindrome(s: str) -> bool :
    new_s = ""
    for char in s :
        if char.isalnum() :
            new_s += char.lower()
        
    s = new_s
    # length = len(s)
    # for i in range(length//2) :
    #     if s[i] != s[length - i - 1] :
    #         return False
    # return True
    return s == s[::-1]

# Використання функції
print(is_palindrome("Козак з казок"))