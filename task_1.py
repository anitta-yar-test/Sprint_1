str='1h 45m,360s,25m,30m 120s,2h 60s'
normalized_str=str.replace(" ",',').split(',')
sum=0
for i in normalized_str:
    if 'h' in i:
        sum+=int(i.replace('h',''))*60
    elif 'm' in i:
        sum+=int(i.replace('m',''))
    elif 's' in i:
        sum+=int(int(i.replace('s',''))/60)
print(sum)