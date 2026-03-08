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
for n in m:
    if n  >= 35 :
        print("pass",n)
    else:
        print("failed",n)

"""
output: enter marks:28 36 90 98 37 99 17
highest marks: 99
Lowest marks: 17
average marks: 57.857142857142854
failed 28
pass 36
pass 90
pass 98
pass 37
pass 99
failed 17


"""

    







    


