n=input('Write your elements with spaces and then press Enter: ').split()
m=int(input("Enter the index number of the point where you want to split the list (count from 1, you don't need to count from zero): "))
n=n[m-1:]+n[0:m-1]
print(' '.join(n))