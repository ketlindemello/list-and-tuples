def main():

    print('Chapter 7 Exercises')
    print('-----------------------------')
    print('1) Charge Account Validation')
    print('-----------------------------')

    read_file()
    account_number = account_input()
    list_of_accounts = read_file()
    account_search(account_number, list_of_accounts)

    print('-----------------------------')
    wait = input("Press Enter to continue...")
    print('-----------------------------')
    print('2) Name Search')
    print('-----------------------------')   
    
    
    boy_name, girl_name = get_names()

    girls_name_list, boy_name_list = read_names()

    search_for_names(girl_name, girls_name_list, boy_name, boy_name_list)
    
    print('-----------------------------')
    wait = input("Press Enter to continue...")
    print('-----------------------------')
    print('3) Population Data')
    print('-----------------------------')

    population()



def read_file():
    
    try:
        lines_list = [line.rstrip('\n') for line in open('charge_accounts.txt', 'r')]
        
        return lines_list

    except FileNotFoundError:
        print('An error ocurred trying to read the file', 'charge_accounts.txt')

def account_input():
    while True:
        account = str(input('Enter account number: '))
        if len(account) == 7 and account.isalpha() == False:
            return account
        else:
            print('Accounts are composed of 7 numerical digits.')

def account_search(account, list_of_accounts):
    number = account
    accounts = list_of_accounts

    if number in accounts:
        print(number, ' is a valid charge account!')
    else:
        print(number, ' is an invalid charge account')

def read_names():
    try:
        girls_list = [line.rstrip('\n').lower() for line in open('GirlNames.txt', 'r')]
        boy_list = [line.rstrip('\n').lower() for line in open('BoyNames.txt', 'r')]
           
        
        return girls_list, boy_list
    
    
    except FileNotFoundError:
        print('An error ocurred trying to read the file')



def get_boy_name():
    while True:
        boy_name = str(input('Enter boy name: '))
        if boy_name.isalpha() == True:
            return boy_name
        else:
            print("Please enter only alphabetical letters, A–Z or a–z...")

def search_for_names(girl_name, girls_name_list, boy_name, boy_name_list):
    
    name_girl = girl_name
    name_list_girl = girls_name_list
    name_boy = boy_name
    name_list_boy = boy_name_list


    if name_girl.isalpha() == True:
        if name_girl.lower() in name_list_girl:
            print(name_girl, ' is a popular girl name.')

        else:
            print(name_girl, ' is not a popular girl name.')
    else:
        print('Girl name provided is not a valid name.')
        
    if name_boy.isalpha() == True:
        if name_boy.lower() in name_list_boy:
            print(name_boy, ' is a popular boy name.')

        else:
            print(name_boy, ' is not a popular boy name.')
    else:
        print('Boy name provided is not a valid name.')
        
def get_names():
    girl_name = str(input('Enter girl name: '))
    boy_name = str(input('Enter boy name: '))
    
    
    return boy_name, girl_name;


def population():
    
  counter = 0
  increase_year = 0
  max_year = 0
  max_year_position = 0
  min_year = 0
  min_year_position = 0
  average_period = 0

  list_numbers = []
  list_number_verage =[]
  list_years = [i for i in range(1950,1991)]

  try:
    file_read = open("USPopulation.txt", "r")

    
    for i in file_read:
      counter = counter + 1

    for j in range(counter):
      list_numbers.append(0)

    file_read.seek(0)
    
    for k in range(counter):
      list_numbers[k] = int(file_read.readline())
      min_year = list_numbers[0]

    for l in range(0,counter,+1):
      
      if (l+1) == counter:
        break
      
      
      increase_year = (list_numbers[l+1] - list_numbers[l])/2
      
      
      if increase_year > max_year:
        max_year = increase_year
        max_year_position = l+1

      
      if min_year > increase_year:
        min_year = increase_year
        min_year_position = l+1
    
    
    average_period = (list_numbers[counter-1] - list_numbers[0])/(counter-1)

    
    print('The average annual change in population during the time period is', '{0:,.2f}'.format(average_period, '.2f'))
    
    print('The year with the greatest increase in population during the time period was', list_years[max_year_position])
    
    print('The year with the smallest increase in population during the time period was', list_years[min_year_position])

    file_read.close()

  
  except FileNotFoundError:
    print('File does not exist')

  
  except IndexError as error:
    print('Index Invalid')

  
  except Exception as exception:
    print('Something went wrong!')

                    

if __name__ == '__main__':
    main()
