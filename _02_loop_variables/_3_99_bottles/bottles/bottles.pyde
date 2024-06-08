for i in range(100):
    i = 99-i
    if i > 1 & i < 99:
        print(' ')
        print(str(i) + ' bottles of beer on the wall')
        print(str(i) + ' bottles of beer')
        print('Take one down, pass it around')
        print(str(i-1) + ' bottles of beer on the wall!')
    elif i == 1:
        print('1' + ' bottle of beer on the wall')
        print('1' + ' bottle of beer')
        print('Take one down, pass it around')
        print('no more bottles of beer on the wall!')
        print(' ')
        print('no more bottles of beer on the wall!')
        print('no more bottles of beer')
        print('go to the store, buy some more')
        print('99 bottles of beer on the wall!')
