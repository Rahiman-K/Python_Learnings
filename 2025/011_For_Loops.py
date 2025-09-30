a = 12
for i in range(a):
    print(i)

# above code gives output as below 

"""
0
1
2
3
4
5
6
7
8
9
10
11
"""
# range starts actually from 0 which actually can be termed as indexing

for i in range(1, 6): # so ex = 0->1, 1->2, 2->3, 3->4, 4->5, 5->6, to be simple 1, n-1 where n is your max range
    print(i)

"""
1
2
3
4
5
"""

# writing a table using for loop
table = int(input("Table you want to know : "))
for i in range(1,11):
    print(f"{table} X ", i, " = ",table*i)
