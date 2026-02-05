from connection import collection


# auxiliary function
def serialize_doc(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

# auxiliary function
def serialize_list(doc):
    return [serialize_doc(doc) for doc in doc]


def get_engineering_high_salary_employees():
    return serialize_list(collection.find({"job_role.department": "Engineering", "salary": {"$gt": 65000}}, {"_id": 0, "employee_id": 1, "name": 1, "salary": 1}))

def get_employees_by_age_and_role():
    return serialize_list(collection.find({"job_role.title": {"$in": ["Engineer", "Specialist"]}, "age": {"$gte": 30, "$lte": 45}},{}))

def get_top_seniority_employees_excluding_hr():
    return serialize_list(collection.find({"job_role.department": {"$ne": "HR"}}, {}).sort("years_at_company", -1).limit(7))

def get_employees_by_age_or_seniority():
    return serialize_list(collection.find({"$or": [{"age": {"$gt": 50}}, {"years_at_company": {"$lt": 3}}]}, {"employee_id": 1, "name": 1, "age": 1, "years_at_company": 1}))

def get_managers_excluding_departments():
    return serialize_list(collection.find({"job_role.title": "Manager", "job_role.department": {"$nin": ["Sales", "Marketing"]}}, {}))

def get_employees_by_lastname_and_age():
    return serialize_list(collection.find({"$and":[{"age": {"$lt": 35}}, {"name":{"$regex": "Nelson"}}]}, {"name": 1, "age": 1, "job_role.department": 1}))


