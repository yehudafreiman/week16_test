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















#
#
#
#
# @router.get("/users")
# def get_all_users():
#     return get_users_from_db()
#
# @router.get("/users/{user_id}")
# def get_user(user_id: str):
#     user = get_user_from_db(user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
#
#
#
#
#
#
#
#
#
# @router.get("/restaurants/query/{q_num}")
# def get_restaurant_query(q_num: int):
#     queries = {
#         1: res_dal.q1_all_docs,
#         2: res_dal.q2_specific_fields,
#         3: res_dal.q3_exclude_id,
#         4: res_dal.q4_with_zip,
#         5: res_dal.q5_bronx,
#         6: res_dal.q6_limit_5,
#         7: res_dal.q7_skip_5,
#         8: res_dal.q8_score_gt_90,
#         9: res_dal.q9_score_80_100,
#         10: res_dal.q10_lat_less,
#         11: res_dal.q11_complex_filter,
#         12: res_dal.q12_no_and_operator,
#         13: res_dal.q13_cuisine_sort,
#         14: res_dal.q14_name_wil,
#         15: res_dal.q15_name_ces,
#         16: res_dal.q16_name_reg,
#         17: res_dal.q17_bronx_cuisine,
#         18: res_dal.q18_multiple_boroughs,
#         19: res_dal.q19_not_boroughs,
#         20: res_dal.q20_score_le_10,
#         21: res_dal.q21_complex_name_cuisine,
#         22: res_dal.q22_grade_date,
#         23: res_dal.q23_second_element_grade,
#         24: res_dal.q24_coord_range,
#         25: res_dal.q25_sort_asc,
#         26: res_dal.q26_sort_desc,
#         27: res_dal.q27_multi_sort,
#         28: res_dal.q28_street_exists,
#         29: res_dal.q29_coord_is_double,
#         30: res_dal.q30_score_mod_7,
#         31: res_dal.q31_name_mon,
#         32: res_dal.q32_name_mad
#     }
#
#     if q_num not in queries:
#         raise HTTPException(status_code=404, detail="Query number not found (1-32)")
#
#     return queries[q_num]()