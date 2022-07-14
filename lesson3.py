'''
name = input('Your name: ')
age = input('Your age: ')
job = input('Your job: ')
while True:
    if name == '':
        name = input('Your name: ')
    if age == '':
        age = input('Your age: ')
    if job == '':
        job = input('Your job: ')
    if name != '' and age != '' and job != '':
        break
'''aaaafaffaaaaaa
ffffaaaafff
'''
# Problem 1
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
lang1 = 'Rust'
if lang1 in languages:
    print('this languages is in list')

# Problem 2
for i in languages:
    if i == 'php':
        break

# Problem 3
number = 7
for i in range(5):
    number *= number
    print(number)

# Problem 4
count = 0
for i in languages:
    print(f'{count} {i}')
    count += 1

# Problem 5
i = 1
while i < 11:
    print(i, end=' ')
    i += 1
for j in range(9, 0, -1):
    print(j, end=' ')

print()
# Problem 6
names = (
'Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат',
'Аслан',)
for k in range(0, len(names), 2):
    print(names[k])

# Problem 7
names = (
'Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек', 'Дастан', 'Бекмамат',
'Аслан',)
for l in range(1, len(names), 2):
    print(names[l])

# Problem 8
num = int(input("Your number: "))
if num in range(100, 1000):
    print(num)
if num > 0 and num % 2 == 0:
    print(num)
if num % 31 == 0:
    print(num)
if num > 100 and num % 17 == 0 or num > 150 and num == 13 ** 2:
    print(num)
    
# Problem 9
seven = -100
count_one = 0
count_two = 0
for i in range(-100, 101):
    if i % 13 == 0 and i % 2 == 0:
        print(i ** 2)
        count_one += 1
    if i == seven:
        if i % 2 == 1:
            print(i)
        seven += 7
        count_two += 1
print(f'first if == {count_one} \nsecond if == {count_two}')


numbers = '1 2 3 4 5 6 7 8 9 10'
result = numbers + numbers[17::-1]
print(result)
for i in result:
    print(i, end='')
'''

'''
num = int(input('Enter number: '))
palin = []
for i in range(1, num + 1):
    palin.append(i)
for j in range(num - 1, 0, -1):
    palin.append(j)
print(palin)
'''
'''
num = int(input('Enter number: ')) # if num == 12
l1 = []
l2 = []
for i in range(1, num + 1):
    l1.append(i)
    l2.append(num-i)
print(l1 + l2[:-1])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''

num = int(input('Enter number: '))  # if num == 12
right = ''
left = ''
for i in range(1, num + 1):
    right += str(i) + ','
    left += str(num - i) + ','
print(right + left[:-3])
# 1,2,3,4,5,6,7,8,9,10,11,12,11,10,9,8,7,6,5,4,3,2,1



