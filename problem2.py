#Pattern A
number_of_rows=5
for i in range(1,number_of_rows+1):#generates the number of rows the pattern A has.
    number=2
    for j in range(1,number_of_rows+1-i):#print the  1 in the mid-side.
        print('',end = '  ')#set the space
    for k in range(i,0,-1):#print the left-side triangle.
        print(pow(3,k-1),end=' ')#set the space
    for x in range(2,i+1):#print the right-side triangle.
        print(number,end=' ')#set the space
        number=number*2
    print()

print("\n")

#Pattern B
number_of_rows = 6
for i in range(number_of_rows, 1, -1):#generates the number of rows the pattern A has.

    for j in range(1, i - 1):#print the left-side upper triangle.
      print(j, end=" ")

    for k in range(i - 1, 0, -1):#print the right-side upper triangle.
        print(k, end=" ")

    print()
