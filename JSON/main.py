import json
import os

DATA_FILE = "data.json"  # Common file for storing JSON data


def write_json():
    """Writes sample data to data.json"""
    student_data = {
        "name": "Tejas",
        "age": 21,
        "course": "B.Tech CSE - AI & Data Engineering",
        "skills": ["Python", "Data Analysis", "Machine Learning"],
        "is_graduated": False,
    }
    with open(DATA_FILE, "w") as file:
        json.dump(student_data, file, indent=4)
    print("Data written to 'data.json' successfully!\n")


def read_json():
    """Reads and displays data from data.json"""
    if not os.path.exists(DATA_FILE):
        print("'data.json' not found! Please run Write option first.\n")
        return

    with open(DATA_FILE, "r") as file:
        student_data = json.load(file)

    print("Student Name:", student_data["name"])
    print("Age:", student_data["age"])
    print("Course:", student_data["course"])
    print("Skills:", ", ".join(student_data["skills"]))
    print("Graduated?:", "Yes" if student_data["is_graduated"] else "No")


def string_conversion():
    """Demonstrates JSON string conversion without files"""
    employee_data = {
        "name": "John Doe",
        "role": "Data Engineer",
        "experience_years": 3,
        "skills": ["Python", "SQL", "AWS"],
        "available": True,
    }

    json_string = json.dumps(employee_data, indent=4)
    print("\nJSON String:\n", json_string)

    python_data = json.loads(json_string)
    print("\nEmployee Name:", python_data["name"])
    print("Skills:", ", ".join(python_data["skills"]))
    print("\nType of json_string:", type(json_string))
    print("Type of python_data:", type(python_data), "\n")


# -----------------------------
# Main Menu
# -----------------------------
while True:
    print("=== JSON Operations Menu ===")
    print("1. Write JSON to file")
    print("2. Read JSON from file")
    print("3. JSON string conversion (without files)")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        write_json()
    elif choice == "2":
        read_json()
    elif choice == "3":
        string_conversion()
    elif choice == "4":
        print("👋 Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.\n")