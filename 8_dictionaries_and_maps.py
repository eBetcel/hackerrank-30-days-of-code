# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phone_book = dict()

for i in range(n):
    input_data = input().split()
    name = input_data[0]
    number = input_data[1]
    phone_book[name] = number
    
while True:
    try:
        search = input()
        if search in phone_book:
            print(search + '=' + phone_book[search])
        else:
            print('Not found')
    except EOFError:
        break        