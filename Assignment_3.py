def load_students(students_txt):
    student_dict = {}
    with open(students_txt, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                studentId, lastName, firstName, major, gpa = line.split(",")
                student_dict[studentId] = {
                    "lastName": lastName,
                    "firstName": firstName,
                    "major": major,
                    "gpa": float(gpa)
                }
    return student_dict

def search_name(student_dict):
    results = []
    searched_name = input("Enter the last name to search: ")
    for studentId, info in student_dict.items():
        if info["lastName"].lower() == searched_name.lower():
            results.append((studentId, info))
    if results:
        for studentId, info in results:
            print(f"ID: {studentId}, Name: {info['firstName']} {info['lastName']}, Major: {info['major']}, GPA: {info['gpa']}")
    else:
        print("No students found with that last name.")
    return results

def search_major(student_dict):
    results = []
    searched_major = input("Enter the major to search: ")
    for studentId, info in student_dict.items():
        if info["major"].lower() == searched_major.lower():
            results.append((studentId, info))
    if results:
        for studentId, info in results:
            print(f"ID: {studentId}, Name: {info['firstName']} {info['lastName']}, Major: {info['major']}, GPA: {info['gpa']}")
    else:
        print("No students found with that major.")
    return results


def main():
    load_students("students.txt")
    student_dict = load_students("students.txt")
    print("Welcome to the Student Database!")
    while True:
        print("Choose an option:")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Exit")
        search_with = input("Enter in how you would like to search: ")
        if search_with == "1":
            search_name(student_dict)
        elif search_with == "2":
            search_major(student_dict)
        elif search_with == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")
            
main()