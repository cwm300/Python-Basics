import re
password = input('Create password: ')

while password != ('quit'):    
    if (len(password)<8):
        print('Not valid. Password length must be more than 8 characters. \n')
        password = input('Try a different password: ')
        
    if (len(password)>30):
        print('Not valid. Password length must be less than 30 characters. \n')
        password = input('Try a different password: ')
        
    elif not re.search('[a-z]', password):
        print('Not valid. Password must include a lower-case letter. \n')
        password = input('Try a different password: ')
        
    elif not re.search('[A-Z]', password):
        print('Not valid. Password must include an upper-case letter. \n')
        password = input('Try a different password: ')
        
    elif not re.search('[0-9]', password):
        print('Not valid. Password must include a number. \n')
        password = input('Try a different password: ')
        
    elif not re.search('[$, #, @, !, %, &, *, ^]', password):
        print('Not valid. Password must include a special character. \n')
        password = input('Try a different password: ')
        
    else:
        print('Password accepted.')
        break
        
        
        
        