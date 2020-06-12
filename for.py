print('整数を入力してください\n')
x=int(input()) + 1

for i in range(1,x):
    for j in range(1,x):
        pro = i*j
        print(str(pro),end='' + '\t')
    print('')
