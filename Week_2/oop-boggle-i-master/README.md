# Boggle Challenge Part 1: Basic Board Generation

## Summary

The goal of this exercise is to create a [4x4 grid of randomly generated letters](https://s-media-cache-ak0.pinimg.com/originals/f0/92/03/f09203920ca7db9c7f3e9247308a8482.jpg), according to the rules of Boggle. If you're not familiar with boggle, you can [read more on wikipedia](http://en.wikipedia.org/wiki/Boggle).


### Step 1: Basic Boggle Board


The `BoggleBoard` class has one core instance method: `shake!`

1. `shake!` should modify the board by filling each cell with a random upper-case letter `A..Z`. Also, there aren't any restrictions on the letters. They can appear multiple times, so choose at random.

2. If you've looked into Boggle, you're probably thinking about how in Boggle 'Q' is always 'Qu'. Don't worry about this, instead just use 'Q' to represent 'Qu'

#### Example

Our code should output something like this:

* When a new 'BoggleBoard' is initialized the output should look like this:

```python
   ____
   ____
   ____
   ____
```

* When `shake!` is invoked on our board, it should output something like this:

```python
   LMVQ
   DKHZ
   SUCO
   GDMV
```

* When I `shake!` it again, it should randomly generate the board again.

### Step 2: Smart Boggle board

We currently implement our board without modeling dice. We should do that next to make our board come closer to modeling a real Boggle board. Instead of choosing 16 random letters from the entire alphabet, we should choose a random letter from any of the six letters on the die, for each of the 16 dice that boggle uses. We also need to choose a random order for the dice themselves. 


We're still only going to have one core method, `shake!` on our `BoggleBoard` class. The following is a list of Boggle Dice, with 'Q' representing 'Qu':

```python
AAEEGN
ELRTTY
AOOTTW
ABBJOO
EHRTVW
CIMOTU
DISTTY
EIOSST
DELRVY
ACHOPS
HIMNQU
EEINSU
EEGHNW
AFFKPS
HLNNRZ
DEILRX
```

### Step 3: Dealing with that Pesky 'Qu'

Our Boggle board generator is nearly finished! We still have one pesky little issue with the representation of 'Qu'. Our board currently prints a 'Q' instead of a 'Qu'. How could we print a 'Qu' instead?

There are various ways to approach this, but it might be worth keeping in mind that how the board is represented in your program, doesn't have to be how it appears to a person using the program.

The alignment of your board my start to look funky once you figure this out, so you'll want to make sure you adjust your program so that it now looks something like this:

```text
P  N  O  T
S  A  F  G
S  V  L  T
L  Qu Z  F
```

## Additional Resources
* [Boggle on Wikipedia](http://en.wikipedia.org/wiki/Boggle)
* [Play Boggle online](http://www.wordplays.com/boggle)




# School Interface II

## Step 1: Menu

Let's think about our program from the user's point of view for a moment. The first thing we want them to see when the program starts is a menu that lists all the actions they can take. 

```
What would you like to do?
Options:
    1. List All Students
    2. View Individual Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
```
Let's create our menu first and then we can work down the list and implement each feature one at a time.  

We'll start by putting this logic in our runner file. We can always pull it out later if need be. 

Replace the lines that are printing out the `staff` and `student` variables with this code for the menu. 

```Python
#runner.py
print("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

```
The above code might look strange, but when we run it we'll find that our menu prints out just the way we want it to. The `\n` in the string tells Python to start a new line.  

Right now we have a program that prints a menu and then exits. That's not very useful. We want to give the user the option to select one of the menu items. We can do that using `input()`. 

```Python
#runner.py 

mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

print(mode)

```

We are going to have our user choose options by their number. If they enter `1` we'll list all students, if they enter `2` they can view a specific student's info, etc. We'll worry about error handling later. 

```Python
#runner.py 
from classes.school import School 

school = School('Ridgemont High') 

mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

if mode == '1':
    school.list_students() 
else:
    pass 

```
Right now if the user enters a `'1'` our program will run the the `list_students()` method on our school object. Any other input will return and exit the program. Run `python3 runner.py` and enter `'1'`. You'll get an error. What does it say? 

In `school.py` write a method `list_students` that prints out a numbered list of student names followed by their school_ids. Your output should look something like this: 

```
1. Lisa 13345
2. Jessie 12335
3. Slater 12645
4. kim 34456
5. dave 788908
6. doug 0809890
```

## Step 2: View Single Student 

Next let's give the user the ability to see data about a single student. First, we'll update our case statement. 

```Python
if mode == '1':
    school.list_students()
elif mode == '2':
    student_id = input('Enter student id:')
    student = school.find_student_by_id(student_id)
    print(str(student))
else:
    pass 
```
After the user chooses to view a student, they'll have to enter a student id so we have a way to look up the student. This is better than searching by name because there can be several students with the same name, but ideally each student will have a unique id. 

Again if we run this and choose `'2'` we will get an error because we haven't written the method yet. 

In `school.py` define a method `find_student_by_id()` that takes in an id and returns the student with the matching id. 

When you're done you should be able to run `python3 runner.py`, enter `'2'`, enter a student id, and have the student object print out in the terminal. It'll look ugly, but we'll handle that in the next release. 

## Step 3: The str() Method

`str()` is a `Python` method that converts an object into a string. Some objects have a `str()` method defined already. For objects we make ourselves (like our student class) we can define our own `str()` method that to control how an object gets printed out. 

Write a `str()` method (`def __str__(self):`) in the student class that prints the instance of student object in a more readable way. 

```
LISA
---------------
age: 25
id: 13345
```

## Step 4: Quit

We've implemented two of or our features. One problem we can fix before we're done for today is the fact that our program quits out after one action. We want the user to be able to view multiple students in a session. How can we use a loop to include this functionality? Add code to `runner.py` so that after showing the list of students or the data from a single student, the menu displays again and the user can input another selection. Only when the user inputs a `'5'` should the program exit. 