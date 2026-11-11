
"""
Student Manager — DevOps Lab 5
Developer: Dev B
"""

from student import Student


def main():
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    print("\nDANH SACH SINH VIEN:")

    for student in students:
        print(student)

    print(f"\nTong so sinh vien: {len(students)}")


if __name__ == "__main__":
    main()
