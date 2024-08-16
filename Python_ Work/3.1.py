# 列表  列表的计算是从0位开始的,-1可以快速返回末位的元素!
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[2])
print(bicycles[2].title())
print(bicycles[3].upper())
print(bicycles[-1])

names = ['Li ming', 'Liu ming', 'Li hua', 'Janny', 'Taitan']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])
print(f'Heloo {names[0]}!')
print(f'Heloo {names[1]}!')
print(f'Heloo {names[2]}!')
print(f'Heloo {names[3]}!')
print(f'Heloo {names[-1]}!')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
transportation = ['car', 'bicycle', 'bus', 'airplan']
print(f'I would like to own a {transportation[0].title()}!')

# 打印今晚聚餐的人员名单,并发出邀请!
print(names)
invite = "can you have dinner with us tonight!"
print(f'{names[0]} {invite}')
print(f'{names[1]} can you have dinner with us tonight!')
print(f'{names[2]} can you have dinner with us tonight!')
print(f'{names[3]} can you have dinner with us tonight!')
print(f'{names[4]} can you have dinner with us tonight!')
print(f'{names[0]} cannot attend the dinner tonight!')

# 李明无法正常赴约今晚的聚餐,打印新的名单,并重新发出邀请!
names[0] = 'Chen yi'
print(names)
print(f'{names[0]} {invite}')
print(f'{names[1]} can you have dinner with us tonight!')
print(f'{names[2]} can you have dinner with us tonight!')
print(f'{names[3]} can you have dinner with us tonight!')
print(f'{names[4]} can you have dinner with us tonight!')
# invite 在这里用来精简代码
desk = 'I found a bigger dining table!'
print(desk)
print(names)
names.insert(0, 'Chen shu')
print(names)
names.insert(3, 'Chen qi ')
print(names)
names.append('Chen a')
print(names)
sorry = "We are very sorry that the new table could not be delivered in time, so we have reduced the number of people for tonight's dinner to two!"
print(sorry)

print(names)
print(f'{names[0]}, {sorry}')
names.pop(0)
print(f'{names[2]}, {sorry}')
names.pop(2)
print(f'{names[3]}, {sorry}')
names.pop(3)
print(f'{names[3]}, {sorry}')
names.pop(3)
print(names)
print(f'{names[-1]}, {sorry}')
names.pop(-1)
print(names)
print(f'{names[-2]}, {sorry}')
names.pop(-2)
print(names)
invites = "Congratulations on being on tonight;s guest list!"
print(f'{names[0]}, {invites}')
print(f'{names[1]}, {invites}')
del names[0]
print(names)
del names[0]
print(names)
# 3.8 放眼世界,想出至少5个你想去旅游的地方
citys = ['usa', 'japan', 'taiwan', 'u.k.', 'australia', 'iceland', 'russia']
print(f'\n\n\n\t{citys}')
print(sorted(citys))
print(citys)
print(sorted(citys, reverse = True))
print(f'\n{citys}')

citys.reverse()
print(citys)
citys.reverse()
print(citys)
citys.sort()
print(citys)
citys.sort(reverse = True)
print(citys)

names = ['Li ming', 'Liu ming', 'Li hua', 'Janny', 'Taitan']
print(f'\n{names}')
print(len(names)) 


# 练习 3.10 创建一个列表,运用以上第三章讲到的每一个函数!
print(f'练习3.10')

mountains = ['taishan', 'wutaishan', 'qingxushan', 'baishishan', 'changbaishan', 'mingshan', 'baoduzhai']
# 获取长度!

print(len(mountains))
print(mountains)
# 反向打印列表!
mountains.reverse()
print(mountains)
mountains.reverse()
print(mountains)

print(sorted(mountains))
print(sorted(mountains,reverse = True))   
mountains.sort()
print(mountains)
mountains.sort(reverse = True)
print(mountains)
print(mountains)
mountains.remove('mingshan')
print(mountains)
mountains.pop(-2)
print(mountains)
del mountains[-3]
print(mountains)
print(mountains[-1])
mountains.insert(-1, 'qingxushan')
print(mountains)
mountains.append('daoshan')
print(mountains)
mountains[-1] = 'ximalayashan'
print(mountains)