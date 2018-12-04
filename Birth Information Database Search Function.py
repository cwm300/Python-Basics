import csv

def menu():
    print('Menu')
    print('Enter one of the options:')
    print('1 to search by year/Location')
    print('2 to search by name')
    print('3 to quit')
   
def main():
    with open('names-state2017.csv') as csvfile:
        file_data = csv.reader(csvfile, delimiter = ',')
        
        all_names = {}
        boys = {}
        girls = {}
        
        menu() 
        option = str(input('Option: '))
        
        
        while option != '3':
            if option == '1':
                state_var = input('> Enter the State Abbreviation or just press enter: ').lower()
                start_year = int(input('> Enter the starting year: '))
                end_year = int(input('> Enter the ending year: '))
                
                for row in file_data:
                    state = row[0]
                    gender = row[1]
                    year = int(row[2])
                    name = row[3]
                    frequency = int(row[4])
                    
                    if state_var == state.lower():
                        if(start_year <= year <= end_year):
                            if(gender == 'M' or gender == 'F'):
                                if name not in all_names.keys():
                                    all_names[name] = frequency
                                else:
                                    all_names[name] += frequency
                                    
                            if(gender == 'M'):
                                if name not in boys.keys():
                                    boys[name] = frequency
                                else:
                                    boys[name] += frequency
                            if(gender == 'F'):
                                if name not in girls.keys():
                                    girls[name] = frequency
                                else:
                                    girls[name] += frequency
                                
                    if state_var == '':
                        if(start_year <= year <= end_year): 
                            if(gender == 'M' or gender == 'F'):
                                if name not in all_names.keys():
                                    all_names[name] = frequency
                                else:
                                    all_names[name] += frequency
                                    
                            if(gender == 'M'):
                                if name not in boys.keys():
                                    boys[name] = frequency
                                else:
                                    boys[name] += frequency
                            if(gender == 'F'):
                                if name not in girls.keys():
                                    girls[name] = frequency
                                else:
                                    girls[name] += frequency                        
                        
                
                top5_names = sorted(all_names, key=all_names.get, reverse=True)[:5]
                top5_girls = sorted(girls, key=girls.get, reverse=True)[:5]
                top5_boys = sorted(boys, key=boys.get, reverse=True)[:5]            
                
                print('Top 5 names \n')
                for i in range(len(top5_names)):
                    print('%d: %s (%d)'%(i+1, top5_names[i], all_names[top5_names[i]]))
                print()
                
                print('Top 5 names for Boys \n')
                for i in range(len(top5_boys)):
                    print('%d: %s (%d)'%(i+1, top5_boys[i], boys[top5_boys[i]]))
                print()
                
                print('Top 5 names for Girls \n')
                for i in range(len(top5_girls)):
                    print('%d: %s (%d)'%(i+1, top5_girls[i], girls[top5_girls[i]]))
                print()
                
            
                menu()
                option = str(input('Option: '))
               
                
            if option == '2':
                name_var = input('Enter the name: ').lower()
                startYear = int(input('> Enter the starting year: '))
                endYear = int(input('> Enter the ending year: '))
                state_var2 = input('> Enter the State Abbreviation or just press enter: ').lower()
                
                for row in file_data:
                    state = row[0]
                    gender = row[1]
                    year = int(row[2])
                    name = row[3]
                    frequency = int(row[4])
                    
                    
                    if state_var2 == state.lower():
                        if(startYear <= year <= endYear):
                            if(gender == 'M' or gender == 'F'):
                                if name not in all_names.keys():
                                    all_names[name] = frequency
                                else:
                                    all_names[name] += frequency
                                    
                            if(gender == 'M'):
                                if name not in boys.keys():
                                    boys[name] = frequency
                                else:
                                    boys[name] += frequency
                            if(gender == 'F'):
                                if name not in girls.keys():
                                    girls[name] = frequency
                                else:
                                    girls[name] += frequency
                        
                        if state_var2 == '':
                            if(startYear <= year <= endYear): 
                                if(gender == 'M' or gender == 'F'):
                                    if name not in all_names.keys():
                                        all_names[name] = frequency
                                    else:
                                        all_names[name] += frequency
                                        
                                if(gender == 'M'):
                                    if name not in boys.keys():
                                        boys[name] = frequency
                                    else:
                                        boys[name] += frequency
                                if(gender == 'F'):
                                    if name not in girls.keys():
                                        girls[name] = frequency
                                    else:
                                        girls[name] += frequency   
                            
                    nameranks = sorted(all_names, key=all_names.get, reverse=True)[:-1] 
                    for i in range(len(nameranks)):
                        if name == name_var:
                            print('%d: %s (%d)'%(i+1, nameranks[i], all_names[nameranks[i]]))                        
            
            
                print()
                
                menu()
                option = str(input('Option: '))

main()
        

        
        
        
        
        