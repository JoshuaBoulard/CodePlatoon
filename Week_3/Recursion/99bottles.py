def bottles(num, count=0):
    if num == 2:
        print(f'{num} bottles of beer on the wall, {num} bottles of beer.  Take one down pass it around {num - 1} bottle of beer on the wall')
        count += 1
        return bottles(num-1, count) 
    elif num == 1:
        print(f'{num} bottle of beer on the wall, {num} bottle of beer.  Take one down pass it around no more bottles of beer on the wall')
        count += 1
        return bottles(num-1, count) 
    elif num == 0:
        print(f'No more bottles of beer on the wall, no more bottles of beer.  Go to the store buy some more, {count} bottles of beer on the wall.')
        return
    else:
        print(f'{num} bottles of beer on the wall, {num} bottles of beer.  Take one down pass it around {num - 1} bottles of beer on the wall')
        count += 1
        return bottles(num - 1, count) 

bottles(87)