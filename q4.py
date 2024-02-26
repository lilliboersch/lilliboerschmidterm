def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

option_a= "2704702208931031198668911301398022074072"
option_b= "4257304920394478392772938744930294037524"
option_c= "0974101607733149676776769413377061014790"
option_d= "7798338247658278460338648728567428338977"

print("Option A is a palindrome:", palindrome(option_a))
print("Option B is a palindrome:", palindrome(option_b))
print("Option C is a palindrome:", palindrome(option_c))
print("Option D is a palindrome:", palindrome(option_d))