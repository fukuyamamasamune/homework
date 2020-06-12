print('何時におきましたか？(0~24の整数で！)\n')
i=int(input())

if 4<=i<=10:
    print('おはよう\n')

elif 11<=i<=16:
    print('いいご身分ですね\n')

elif 17<=i<=24 or 0<=i<=3:
    print('おはよう？')

else:
    print('0~24の整数からえらんでね\n')