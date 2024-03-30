from fastapi import FastAPI
from data_models import (
    NewEmployee,
    UpdateEmployee
)

app = FastAPI(
    title="CRUD API",
    description="This API will implement CRUD operations"
)

employees = {
    1: {
        "name": "Michael",
        "age": 45,
        "pos": "Manager"
    }
}


@app.get("/")
def index():
    return "Welcome to API for CRUD operations"


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):
    if emp_id not in employees:
        return f"No employee found with ID = {emp_id}"
    return employees[emp_id]


@app.post("/add-employee")
def add_employee(new_emp: NewEmployee):
    if not employees:
        new_id = 1
    else:
        new_id = max(employees.keys()) + 1

    employees[new_id] = new_emp.model_dump()
    return employees[new_id]


@app.put("/update-employee/{emp_id}")
def update_employee(emp_id: int, emp: UpdateEmployee):
    if emp_id not in employees:
        return f"No employee found with ID = {emp_id}"
    
    if emp.name is not None:
        employees[emp_id]["name"] = emp.name
    
    if emp.age is not None:
        employees[emp_id]["age"] = emp.age
    
    if emp.pos is not None:
        employees[emp_id]["pos"] = emp.pos
    
    return employees[emp_id]


@app.delete("/delete-employee/{emp_id}")
def delete_employee(emp_id: int):
    if emp_id not in employees:
        return f"No employee found with ID = {emp_id}"
    del employees[emp_id]
    return employees