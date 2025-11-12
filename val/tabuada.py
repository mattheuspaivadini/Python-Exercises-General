while True:
    num = int(input(':'))
    if num % 2 == 0:
        for i in range(1, (num + 1)):
            tab = num * i
            print(f'{num} X {i} = {tab}')
    else:
        for i in range(1, (num +1)):
            print(i)
    if num == 0:
        break
