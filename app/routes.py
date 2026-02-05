from fastapi import APIRouter
from dal import get_engineering_high_salary_employees, get_employees_by_age_and_role, \
    get_top_seniority_employees_excluding_hr, get_employees_by_age_or_seniority, get_managers_excluding_departments, \
    get_employees_by_lastname_and_age

router = APIRouter()

@router.get("/employees/engineering/high-salary")
def high_salary():
    return get_engineering_high_salary_employees()

@router.get("/employees/by-age-and-role")
def by_age_and_role():
    return get_employees_by_age_and_role()

@router.get("/employees/top-seniority")
def top_seniority():
    return get_top_seniority_employees_excluding_hr()

@router.get("/employees/age-or-seniority")
def age_or_seniority():
    return get_employees_by_age_or_seniority()

@router.get("/employees/managers/excluding-departments")
def excluding_departments():
    return get_managers_excluding_departments()

@router.get("/employees/by-lastname-and-age")
def by_lastname_and_age():
    return get_employees_by_lastname_and_age()





