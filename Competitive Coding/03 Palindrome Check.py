def checkPalindrome(inputString):
    inputString = inputString.lower()
    rev = reversed(inputString)
    if list(inputString) == list(rev):
        print(True)
    else:
        print(False)

#tesing conditions to be passed
while 1:
	print('-'*20)
	checkPalindrome(input('Enter the string to check for palindrome - '))
	print('-'*20)
	if (int(input('Enter 0 to exit - ')) == 0):
		print('-'*20)
		break