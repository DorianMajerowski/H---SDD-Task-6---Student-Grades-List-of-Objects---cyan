"""
Student Grades

A Team effort!
Daniel
Dorian

11/09/20

Reads in names and scores for students in a class and then calculates percentages and grades

Allows user to update the records after entry
"""

class Student():
    def __init__(self, record, record_id):
        self.id = record_id
        self.name = record[0]
        self.score = record[1]

def main():
    students = get_records()
    calc_percentage(students)
    calc_grade(students)
    display_records(students)

    user_choice = 0

    # Loop until user chooses 'Exit'
    while user_choice != 2:
        user_choice = int(input('\nOptions\n1 - Change an entry\n2 - Exit\n> '))

        if user_choice == 1:
            student_id = int(input(f'\nPlease enter the student you want to update (0 - {len(students) - 1})\n> '))

            # Update selected record and display again
            update_record(students, student_id)
            display_records(students)

def get_records():
    # List to store records
  
    records = []

    # For each student
    for x in range(10):
        # Get record and add to list
        records.append(Student(
          get_record_data(), x))

    return records

def get_record_data():
    # TODO: Read in details of one record
    temp_name = input('name: ')
    temp_score = int(input('score: '))
    # TODO: Return details of record
    return [temp_name, temp_score]

def calc_percentage(records):
    # TODO: Calculate percentages and store in records
    for x in records:
        x.percent = x.score / 150 * 100
        x.percent = round(x.percent, 2)
    
    pass

def calc_grade(records):
    # TODO: Calculate grades and store in records
    
    for x in records:
      if x.percent >= 85:
        x.grade = 'A'
      elif x.percent >= 70 and x.percent < 85:
        x.grade = 'B'
      elif x.percent >= 55 and x.percent < 70:
        x.grade = 'C'
      elif x.percent >= 40 and x.percent < 55:
        x.grade = 'D'
      else:
        x.grade = 'F'
      
    pass

def update_record(records, record_id):
    record = get_record_data()

    # TODO: Update percentages and grades for new data
    records[record_id ] = Student(record, record_id )
    calc_percentage(records)
    calc_grade(records)


def display_records(records):
    print()
    print(f'{"ID":7}{"Name":20}{"Score":10}{"Percentage":15}Grade')

    for record in records:
        print(f'{record.id:<7}{record.name:<20}{record.score:<10}{record.percent:<15}{record.grade}')

main()