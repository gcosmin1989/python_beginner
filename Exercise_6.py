palindrome = input('Input a palindrome: ').lower()

reversed_word = palindrome[len(palindrome)::-1].lower()

if palindrome == reversed_word:
    print(f'{palindrome} is a palindrome')
else:
    print(f'{palindrome} is not a palindrome {palindrome} not {reversed_word}')
