def convert(number_str):
    number_to_str_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    number_to_str_tens = {'10': 'ten', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'}
    
    
    final_result = ''
    if number_str == '1000':
        return 'one thousand'
    elif number_str == '0':
        return number_to_str_dict[number_str]
    elif number_str == '11':
        return 'eleven'
    elif number_str == '12':
        return 'twelve'
    elif number_str == '13':
        return 'thirteen'
    elif number_str == '14':
        return 'fourteen'
    elif number_str == '15':
        return 'fifteen'
    elif number_str == '16':
        return 'sixteen'
    elif number_str == '17':
        return 'seventeen'
    elif number_str == '18':
        return 'eighteen'
    elif number_str == '19':
        return 'ninteen'
        
        
    result = ''
    for digit in number_str:
        result += number_to_str_dict[digit]+' '
        
    changed_result = make_change(number_str)
    split_nums = changed_result.split(' ')
    for num in split_nums:
        if len(num) > 2:
            final_result += number_to_str_dict[num[0]] + ' hundred '            
            #compare hundreds
        
        elif len(num) > 1:
            final_result += number_to_str_tens[num] + ' '
            #compare tens
            
        else:
            if len(num.strip()) != 0:
                final_result += number_to_str_dict[num]
            #compare ones
 
    
    
    return final_result

def make_change(num_str):
    num = int(num_str)
    result = num
    final_str = ''
    while result > 9:
        if result > 99:
           
            result2 = result % 100
            result3 = result - result2
            final_str += str(result3) + ' '
            result = result2
        elif result > 9:
          
            result2 = result % 10
            result3 = result - result2
            final_str += str(result3) + ' '
            result = result2            
    
    if result > 0:
        final_str += str(result)
    return final_str
    
def main():
    
    user_input = input('> ')
    while  user_input != 'quit':
        print(convert(user_input))
        user_input = input('> ')


main()