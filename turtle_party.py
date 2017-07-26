day = input('weekday or weekend?')
fruit = int(input('how many strawberries?'))
if day=='weekend':
    if fruit>39:
        print('fun')
    else:
        print('not fun')
else:
    if 61>fruit>39:
        print('fun')
    else:
        print('not fun')
        
