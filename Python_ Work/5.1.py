cars = ['aodi', 'benchi', 'baoma', 'biyadi', 'dazhong', 'yema', 'xuefulan']
for car in cars:
    if car == 'yema':
        print('恭喜你开上了奥迪')
    print('垃圾小轿车')


one_number = '9'
two_number = '9'
if one_number >= '10' and two_number >= '10':
    print('恭喜你')
if one_number != '9' and two_number != '9':
    print('抱歉')

alien = 'yellow'
if alien == 'yellow':
    print('\n\n恭喜你失败')
elif alien == 'green':
    print('测试通过')
        
alien = 'green'
if alien == 'yellow':
    print('\n\n恭喜你失败')
elif alien == 'blue':
    print('测试通过')
else:
    alien == 'white'

users = ['admin', 'li ming', 'liu ming', 'li hua', 'janny']
for user in users:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status repore?')
    if user == '':
        print('We need to find some users!')
    else:
        print(f'Hello {user}, thank you for logging in again.')



current_users = ['admin', 'liming', 'liu ming', 'li hua', 'janny']
new_user = ['admin', 'LIMING', 'xiaoming', 'xiao hua', 'xiaomie']
for new_user in new_user:
    if new_user.lower() in current_users:
        print('用户名已被占用')
    else:
        print('可以使用')

third_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9','']
for number in third_number:
    print(number)
    if number == ['1', '2', '3']:
        print(f'{number}th')
    elif number == ['4', '5', '6']:
        print(f'{number}th')
    else:
        print(f'{number}th')
        
