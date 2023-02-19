import json

class Employee:
    def __init__(self, name, DOB, height, city, state):
        self.name = name
        self.DOB = DOB
        self.height = height
        self.city = city
        self.state = state
    
    def __str__(self):
        return f"{self.name} ({self.DOB}) from {self.city}, {self.state} ({self.height} cm)"

with open('employee.json', 'r') as file:
    employee_data = json.load(file)

employees = []
for employee in employee_data:
    employees.append(Employee(employee['name'], employee['DOB'], employee['height'], employee['city'], employee['state']))

print("****List of Employee objects : ****")
for emp in employees:
    print(emp)

indian_states = {
    "Maharashtra": "Mumbai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "West Bengal": "Kolkata",
    "Punjab": "Chandigarh"
}

with open('indian_states.json', 'w') as f:
    json.dump(indian_states, f)

print("****Indian states and their capitals : ****")
with open('indian_states.json', 'r') as f:
    indian_states_data = json.load(f)
    for state, capital in indian_states_data.items():
        print(f"{state}: {capital}")
