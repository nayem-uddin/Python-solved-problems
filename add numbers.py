n=input('Enter the numbers you want to sum with spaces and press Enter if finished: ').split()
sum=0
for i in n:
    sum+=int(i)
print('The sum of your numbers is: ',sum)