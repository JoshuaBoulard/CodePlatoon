class ContactList:

    def __init__(self, friends, work_buddies):
        self.friends = friends
        self.work_buddies = work_buddies

    def __str__(self):
        return f'Friends: {self.friends}\nWork Buddies: {self.work_buddies}'

    


friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

contacts = ContactList(friends, work_buddies)

print(contacts)
