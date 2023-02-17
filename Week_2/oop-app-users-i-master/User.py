class User:

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

        if not hasattr(User, 'posts'):
            User.posts = []



    def __str__(self):
        return f"Name: {self.first_name + ' ' + self.last_name} Username: {self.username} Email: {self.email}"

    @staticmethod
    def make_post(self):
        post = input("Make a post:\n")
        User.posts.append(f'{self.username}: {post}')
        return f"{self.username} posted:\n{post}"

mike = User("Mike", "Williams", "DirtyMike", "mikewilliams@email.com")
will = User("Will", "Johnson", "WillyPete", "willjohnson@email.com")
john = User('John', "Hancock", "JohnnyBravo", "johnhancock@email.com")

mike_posts = User.posts
will_posts = User.posts
john_posts = User.posts

print(User.make_post(mike))
print(User.make_post(will))
print(User.make_post(john))

print(mike_posts)
print(will_posts)
print(john_posts)


