users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]
for user in users_info:
    print(f"Name: {user[0]}, Age: {user[1]}")


users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]
for user, age in users_info:
    print(f"Name: {user}, Age: {age}")
