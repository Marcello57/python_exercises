passwd = 'ala123'  # stored password

print('Enter password:')
inpt = input()
while inpt != passwd:
    print('Wrong password, try again')
    inpt = input()

print('Correct password!')
