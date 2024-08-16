# 遍历整个列表
pizzas = ['liulian', 'heixin', 'caomei', 'naiyou', 'huotui', 'menzi']
for pizza in pizzas:
    print(f'I like {pizza} pizza!')
print(f'I realy realy like pizza!')

animals = ['tiger', 'dog', 'lion', 'giraffe', 'elephant']
for animal in animals:
    print(animal.title())
    print(f"I very like {animal.title()}!\n")
print(f'This animals run fast! ')


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

for value in range(1, 21):
    print(value)
# numbers = list(range(1, 1000001))
# for number in numbers:
#     print(number)
print(f'总和')
numberss = list(range(1, 1000001))
print(min(numberss))
print(max(numberss))
print(sum(numberss))

one_numbers = list(range(1, 21, 2))
for one in one_numbers:
    print(one)

two_numbers = list(range(3, 31, 3))
for two in two_numbers:
    print(two)

three_numbers = []
for value in range(1, 11):
    three_numbers.append(value ** 2)
print(three_numbers)

three_numbers = [value ** 2 for value in range(1, 11)]
print(three_numbers)


my_mountains = ['taishan', 'wutaishan', 'qingxushan', 'baishishan', 
'changbaishan', 'mingshan', 'baoduzhai']
print(f'The first three items in the list are:')
print(my_mountains[:3])
print(f'Three items from the middle of the list are:')
print(my_mountains[2:5])
print(f'The last three items in the list are:')
print(my_mountains[-3:])

print(f'\n\n\n\n\n')
my_pizzas = ['liulian', 'heixin', 'caomei', 'naiyou', 'huotui', 'menzi']
friend_pizzas = my_pizzas[:]
print(friend_pizzas)
my_pizzas.insert(6, 'xigua')
for pizza in my_pizzas:
    print(f'My favorite pizzas are:')
    print(f'{pizza}!')
friend_pizzas.append('hongdou')
for pizza in friend_pizzas:
    print(f"\n\nMy friend's favorite pizzas are:")
    print(f'{pizza}!')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for food in my_foods:
    print("My favorite foods are:")
    print(f'{food}!')
for food in friend_foods:
    print("\nMy friend's favorite foods are:")
    print(f'{food}!')


foodsss = ('炸鸡', '啤酒', '香瓜', '饮料', '核桃', '饺子')
for food in foodsss:
    print(food)
# foodsss[-1] = '奶茶'
# print(foodsss)
foodsss = ('炸鸡', '啤酒', '西瓜', '奶茶', '香瓜', '葡挞皮')
for food in foodsss:
    print(f'\n{food}')