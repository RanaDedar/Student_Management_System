from student_manager import Student_manager

def main_menu():
    manager = Student_manager()
    while True:
        print("\n--- 🎓 Student Management System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Update Student Info")
        print("5. List All Students")
        print("6. View Class Statistics")
        print("7. View Top Performers")
        print("8. Exit")
        choice = input("\nSelect an option (1-8): ")
        if choice == '1':
            s_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            email = input("Enter Email: ")
            manager.add_student(s_id, name, age, email)
        elif choice == '2':
            query = input("Search by Name or ID: ")
            manager.search_student(query)
        elif choice == '3':
            s_id = input("Enter ID of student to remove: ")
            manager.remove_student(s_id)
        elif choice == '4':
            s_id = input("Enter Student ID to update: ")
            attr = input("What do you want to update? (name/age/email): ")
            val = input(f"Enter new value for {attr}: ")
            manager.update_student(s_id, **{attr: val})
        elif choice == '5':
            print("\n--- 📋 All Students ---")
            manager.list_all_students()
        elif choice == '6':
            manager.get_stats()
        elif choice == '7':
            count = int(input("How many top students to view?: "))
            manager.get_top_students(count)
        elif choice == '8':
            print("👋 Goodbye! Data has been saved.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()