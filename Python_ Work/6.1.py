# 使用一个字典来存储一个人的信息，包括名、姓 、年龄和居住的城市。该字典应包含
# 键 first_name last_name、age和city。 将存储在该字典中的每项信息都打印出来

message = {'First_name':'LI','Last_name':'Hua','age':'twenty', 'city':'Beijing',
           }
print(message['First_name'] + message['Last_name'])
print(message['age'])
print(message['city'])
print(message)

# 喜欢的数 1 ,使用一个字典来存储一些人喜欢的数.请想出 5 个人的名字,并将这些名字用作字典
# 中的键.再想出每个人喜欢的一个数,并将这些数作为值存储在字典中.打印每个人的名字和喜欢
# 的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。、
number = {
    'liming':'',
    'lihua':'',
    'janny':'',
    'liujialiang':'',
    'lihaotian':'',
    }
number['liming'] = 'zero'
number['lihua'] = 25
number['janny'] = 28
number['liujialiang'] = 30
number['lihaotian'] = 20
print(number)
numbers = number['liming'].title()
print(f'liming loves {numbers}!')
numbers = number['lihua']
print(f'lihua loves {numbers}!')
numbers = number['janny']
print(f'janny loves {numbers}!')
numbers = number['liujialiang']
print(f'liujialiang loves {numbers}!')
numbers = number['lihaotian']
print(f'lihaotian loves {numbers}!')




# 词汇表 Python ，字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表
# 相处你在前面学过的 5 个编程术语，将他们用作词汇表中的键，并将它们的含义作为值存储在
# 词汇表中。
# 以整洁的方式打印每个术语及其含义。为此，既可以先打印术语，在他后面加上一个冒号，再
# 打印其含义；也可以先在一行里打印术语，再使用换行符(\n)插入一个空行，然后在下一行里
# 以缩进的方式打印其含义

glossary = {
    'print':'',
    'glossary':'',
    'int':'',
    'float':'',
    'constant':'',
    'list':'', 
    }
glossary['constant'] = '常量'
glossary['float'] = '浮点数'
glossary['glossary'] = '词汇表'
glossary['int'] = '整数'
glossary['list'] = '列表'
glossary['print'] = '输出'
print(glossary)
print("constant:\n\t" + glossary['constant'])
print("float:\n\t" + glossary['float'])
print("list:\n\t" + glossary['list'])
print("print:\n\t" + glossary['print'])
print("int:\n\t" + glossary['int'])
print("glossary:\n\t" + glossary['glossary'])

# 词汇表 2 现在你知道了如何遍历字典,请整理你为练习 6.3 词汇表 1 编写的代码,将其中的
# 一系列函数调用 print() 替换为一个遍历字典中键和值的循环。确保该循环正确无误后，再
# 在词汇表中添加 5 个Python 词汇术语。当你再次运行这个程序时, 这些新术语及其含义自动
# 包含在输出中
glossary = {
    'print':'',
    'glossary':'',
    'int':'',
    'float':'',
    'constant':'',
    'list':'', 
    }
glossary['constant'] = '常量'
glossary['float'] = '浮点数'
glossary['glossary'] = '词汇表'
glossary['int'] = '整数'
glossary['list'] = '列表'
glossary['print'] = '输出'
print(glossary)
for k , v in glossary.items():
    print(f'\nk: {k}')
    print(f'v: {v}')
glossary['key'] = '键'
glossary['value'] = '值'
glossary['if'] = '如果'
glossary['elif'] = '否则'
glossary['else'] = '否则'
print(glossary)

    

#  河流 创建一个字典, 在其中存储三条河流及其流经的国家。例如，一个键值对可能是
#  'nile' : 'egypt'。
#     使用循环为每条河流打印一条消息，如下所示。
#         THe Nile runs through Egypt.
#     使用循环将该字典中的每条河流打印出来。
#     使用循环将该字典中包含的每个国家的名字打印出来。


rivers = {
    'Amazon River': 'Usa',
    'changjiang': 'china',
    'Mae Nam': 'Thailand',
    }
for river , country in rivers.items():
    print(f'\nTHe {river} rus through {country}. ')
for river in rivers:
    print(river)
for country in rivers:
    print(country)

# 不同的做法
    print('测试测试')
    print('The ' + river + 'run through ' + country + '!')
    print(river)
    print(country)
### 分歧 虽然不同的做法 这个版本 简单易懂 但面临 单词较长时,会出现以下情况,
### The changjiangrun through china!
### 虽然用f字符串写的比较复杂 难懂,但是可以保持单词的独立完整性!

#  调查 在6.3.1 节编写的程序 favorite_lanuguages.py 中执行以下操作。
#     创建一个应该会接受调查的人的名单，其中有些人已在字典中，而其他人不在字典中。
#     遍历这个名单。 对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，
#     打印一条邀请参加调查的消息。
favorite_number = {
    'liming':'',
    'lihua':'',
    'janny':'',
    'liujialiang':'',
    'lihaotian':'',
    }
favorite_number['liming'] = 'zero'
favorite_number['lihua'] = 25
favorite_number['janny'] = 28
favorite_number['liujialiang'] = 30
favorite_number['lihaotian'] = 20
print(favorite_number)
list = {'liming', 'lihua', 'janny', 'wutianyi', 'tongjiaqi', 'datou', 'xiaotou'
    }
for name in  favorite_number:
    print(name.title())
    if name in list: 
        print(f'Many thanks to {name.title()} for participating in the survey!'
              )
    if name not in list:
        print(f"{name.title()},please cooperate with the investigation!")
          
# 人们 在为练习6.1编写的程序中,再创建两个表示人的字典,然后将这三个字典都存储在一个名为
# people 的列表中。遍历这个列表, 将其中每个人的所有信息都打印出来。
message = {'First_name':'LI','Last_name':'Hua','age':'twenty', 'city':'Beijing',
           }
print(message['First_name'] + message['Last_name'])
print(message['age'])
print(message['city'])
first_message = {
    'FIrst_name':'hu',
    'last_name':'pang',
    'age':'thirty',
    'city':'shanghai',
    }
last_message = {
    'FIrst_name':'shu',
    'last_name':'gong',
    'age':'twenty_eight',
    'city':'chengdu',
    }
peoples = [message, first_message, last_message,]
for people in peoples :
    print(people)

# 宠物 创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。将这些字典存储
# 在一个名为 pets 的列表中，再遍历该列表，并将有关每个宠物的所有信息都打印出来。

dictionary = {
    "pet_type":"dog",
    "THe_owner's_name":"chenglong"
    }
pig  = {
    "pet_type":"pig",
    "THe_owner's_name":"lixiaolong"
    } 
pets = [pig, dictionary]
for animal in pets:
    print(animal)

# 喜欢的地方 创建一个名为 favorite_places 的字典。在这个字典中，将三个人的名字用作键
# ，并存储每个人喜欢的 1 ~ 3 个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方
# 打印出来。
favorite_places = {
    'liming': ['chang jiang', 'huang ghe', 'gu gong'],
    'lihua': ['chang bai shan', 'gou er', 'chong er'],
    'liuxiang': ['shi zi', 'tiger', 'dog'],
    }
#for limings in favorite_places['liming']: 
    #print(f'{limings}')
 #   for river , country in rivers.items():
 #    print('The ' + river + 'run through ' + country + '!')
for namess , loves in favorite_places.items():
    print(f'\n{namess.title()}:')
    for love in loves:
        print(f'\t{love.title()}')



# 喜欢的数 2 修改为练习6.2编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字
# 及其喜欢的数打印出来。
number = {
    'liming': ['1', '2', '3', '4'],
    'lihua': ['23', '25', '33', '34'],
    'janny': ['12', '24','56', '36'],
    'liujialiang': ['64', '26', '27', '27'],
    'lihaotian': ['17', '32', '27', '27'],
    }
for name, numbers in number.items():
    print(f'\n{name.title()}:')
    for number in numbers:
        print(number)






# 城市 创建一个名为 cities 的字典，将三个城市名用作键。对于每座城市，都创建一个字典，并
# 在其中包含城市所属的国家、人口约数以及一个有关城市的事实。表示每座城市的的字典都应 
# 包含 counrty、pouplation和fact等键。将每座城市的名字以及相关信息都打印出来。

cites = {
    'chengdu':{'country':'china','人数': '30w', 'story': '成都非常美丽'},
    'beijing':{'country':'china','人数': '50w', 'story': '北京非常美丽'},
    'shanghai':{'country':'china','人数': '90w', 'story': '上海非常美丽'},
    'xinjiang':{'country':'china','人数': '10w', 'story': '新疆非常美丽'},
}
for city, messages in cites.items():
    print(f'\n{city.title()}:')
    for key, value in messages.items():
        print(f'{key.title()}: {value}')
      #  print(value)
        


# 扩展 本章的示例足够复杂，能以很多方式进行扩展。请对本章的示例进行扩展：添加键和值，
# 调整程序要解决的问题，或改进输出的格式.




