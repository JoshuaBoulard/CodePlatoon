class ContactList:

    def __init__(self, identify, contacts):
        self.identify = identify
        self.contacts = contacts

    def __str__(self):
        return f'{self.identify}: {self.contacts}'

    def add_contact(self):
        new_cont = {'name':input('Name: '), 'number':input('Number: ')}
        self.contacts.append(new_cont)
        self.contacts = sorted(self.contacts, key=lambda d: d["name"])
        return f'{self.contacts}'

    def remove_contact(self):
        for i in range(len(self.contacts)):
            if self.contacts[i]['name'] == input('Name of contact to be removed: '):
                del self.contacts[i]
                break
        return f'Updated Contact List: {self.contacts}'

    def find_shared_contacts(self, compare):
        shared_contacts = []
        for i in self.contacts:
            if i in compare:
                shared_contacts.append(i)
        return shared_contacts






friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends = ContactList('Friends', friends)
my_work_buddies = ContactList("Work buddies", work_buddies)

print(ContactList.find_shared_contacts(my_friends, work_buddies))


