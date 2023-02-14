import csv

animal_type = input("What animal library would you like to access?\n")

try:
    data = open(f'/Users/reapingcalamity/Desktop/TangoPlatoon/Assignments/csv-reader-main/data/{animal_type}.csv')
    reader = csv.DictReader(data)

    for row in reader:
        print(f'{row["name"]} is a {row["age"]} year old {row["breed"]}.')

    data.close()

except:
    print(f'Sorry, we dont have any {animal_type} here')