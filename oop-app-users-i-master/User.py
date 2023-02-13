class User:

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def __str__(self):
        return f"Name: {self.first_name + ' ' + self.last_name} Username: {self.username} Email: {self.email}"

mike = User("Mike", "Williams", "DirtyMike", "mikewilliams@email.com")
will = User("Will", "Johnson", "WillyPete", "willjohnson@email.com")
john = User('John', "Hancock", "JohnnyBravo", "johnhancock@email.com")

print(mike)
