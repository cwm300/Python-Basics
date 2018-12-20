def is_pal(number):
    return True if reverse(number) == str(number) else False
        
def make_positive(number):
    return abs(int(number))

def reverse(number):
    return str(number)[::-1]

def reverse_add(low, high):
    
    if low == high:
        if is_pal(low):
            print('Is already PAL')
            return
        else:
            for num in range(low, high + 1):
                result = num
                count = 0
                while not is_pal(result):
                    orig_result = result
                    result = int(reverse(result)) + result
                    if count >= 100:
                        print('NOT PAL (' + str(count) + ' steps)')
                        break
                    count += 1
                    print(str(count) + '. ' + str(orig_result) + ' + ' + reverse(str(orig_result)) + ' = ' + str(result))
    else:
        for num in range(low, high + 1):
            result = num
            count = 0
            while not is_pal(result):
                result = int(reverse(result)) + result
                if count >= 100:
                    break
                count += 1
            if count >= 100:
                print(str(num) + ': NOT PAL (' + str(count) + ' steps)')
            else:
                print(str(num) + ': PAL (' + str(count) + ' steps)')
            

    ''' Executes the reverse and add algorithm for integers
        in the range low to high. For example, if low is 10 and
        high is 50, then the function would run the reverse and add
        procedure on the numbers 10, 11, .., 49, 50. Or, the user could be interested in a single number such as 89.  In 
        this case, low and high are both 89.
    '''
#1 - take positive integer
#2 - check if the int is pal.
#3 - is pal. stop
#4 - else: reverse digits
#5 - add reverse to x
#6 check if pal: stop if it is
#7 - otherwise, 4 - 6 with result
    
    
    
def main():
    ''' The program driver. '''

    # set cmd to anything except quit()
    cmd = ''
    
    # process the user commands
    cmd = input('> ')
    while  cmd != 'quit':
        i = 0
        while i < len(cmd) and cmd[i] != ' ':
            i += 1
        if ' ' in cmd: 
            low = int(cmd[:i+1])
            high = int(cmd[i+1:])         
        else:
            low = int(cmd)
            high = low
        reverse_add(low, high)
        cmd = input('> ')

main()