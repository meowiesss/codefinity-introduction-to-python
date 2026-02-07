meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]

deli_dept = [meat, cheese]
if meat[2] < 100:
    meat[2] = 100

deli_dept.sort()
print("Initial Deli List:", deli_dept)
print("Updated Deli List:", deli_dept)

