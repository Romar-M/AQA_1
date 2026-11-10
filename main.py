users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30, "email": "charlie@example.com"},
    {"name": "David", "email": "david@example.com"},
]

names = [user["name"] for user in users if user.get("age", 0) >= 18 and user.get("email")]

if __name__ == "__main__":
    print(names)
