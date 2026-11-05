employees = [
    {"name": "Meet", "salary": 25000},
    {"name": "Rahul", "salary": 40000},
    {"name": "Priya", "salary": 55000},
    {"name": "Amit", "salary": 30000}
]

#extract all emp name
name = [row["name"] for row in employees]
print(name)

#extract emp who has salary greater then 30000
salary_more_than_30000 = [row["salary"] for row in employees if row["salary"] > 30000]
print(salary_more_than_30000)

#list of salaries with a 10% increment
increment_list = [row["salary"] + row["salary"]*10/100 for row in employees]
print(increment_list)

#Extract names of employees whose salary is below ₹35,000
name_below_30000 = [row["name"] for row in employees if row["salary"] < 35000]
print(name_below_30000)
