student = {
    "name": "Maria Garcia",
    "age": 28,
    "city": "Denver",
    "is_enrolled": True
}


print(student["name"])
print(student["age"])


# using .get() is safter because it returns NONE instead of crashing if key doesn't work.
print(student.get("email"))     #none (no crash)
print(student.get("email", "N/A"))  # custom default

#Direct access crashes if key is missing
print(student["email"])     # keyError: 'email'



# MODIFYING DICTIONARIES
# Add a new key-value pair
student["email"] = "maria@example.com"

# update an existing value
student["age"] = 29

# Remove a key-value pair
del student["is_enrolled"]

# Remove and get the value
city = student.pop("city")  #city = "Denver," key removed

print(student)
# {"name": "Maria Garcia", "age": 29, "email": "maria@example.com"}