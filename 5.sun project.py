"""Project 1️⃣ Student Marks Analyzer
Problem

Write a program to manage student marks.

Requirements

Ask user to enter 5 student marks.

Store marks in a list.

Using loops:

Print all marks

Find highest mark

Find lowest mark

Find average mark

Print students who passed (marks ≥ 35).

Print students who failed (marks < 35).

Example Input
Enter marks: 45
Enter marks: 78
Enter marks: 20
Enter marks: 90
Enter marks: 60
Example Output
Marks list: [45, 78, 20, 90, 60]
Highest mark: 90
Lowest mark: 20
Average: 58.6
Passed: 45 78 90 60
Failed: 20



"""

m=list(map(int ,input("enter marks:").split()))

#highest marks  
highest = m[0]
for x in m:
    if   x > highest:
        highest = x
print("highest marks:",highest)

#lowest marks
lowest =m[0]
for y in m:
    if y< lowest:
        lowest = y
print("Lowest marks:",lowest)

#average marks
total=0
for i in m:
    total = total + i
avg = total / len(m)
print("average marks:",avg)


#pass fail marks
print("passed:",end=" ")
for n in m:
    if n  >= 35 :
        print(n,end=" ")
print()

print("fail:",end=" ")
for n in m:
    if n  <= 35 :
        print(n,end=" ")
print()
    

"""output:
enter marks:16 80 23 36 78 89
highest marks: 89
Lowest marks: 16
average marks: 53.666666666666664
passed: 80 36 78 89 
fail: 16 23 


"""

    







    


