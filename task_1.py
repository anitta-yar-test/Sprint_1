str='1h 45m,360s,25m,30m 120s,2h 60s'
str_new=str.split(',')
print(str_new)
str_new2=[]
for i in range(0,len(str_new)):
    str_new2+=str_new[i].split(' ')
print(str_new2)
sum=0
for i in range(0,(len(str_new2))):
    if 'h' in str_new2[i]:
        sum+=int(str_new2[i].replace('h',''))*60
    elif 'm' in str_new2[i]:
        sum+=int(str_new2[i].replace('m',''))
    elif 's' in str_new2[i]:
        sum+=int(int(str_new2[i].replace('s',''))/60)
print(sum)