import sqlite3
conn = sqlite3.connect("contact_book.db")
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS contacts(
    name TEXT,
    mobile TEXT
)""")

conn.commit()

while True:
    print("\n==== CONTACT BOOK ====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Friend's Name: ")
        mobile = input("Enter Mobile Number: ")

        cursor.execute(
            "INSERT INTO contacts (name, mobile) VALUES (?, ?)",
            (name, mobile)
        )
        conn.commit()

        print("Contact Saved Successfully!")

    elif choice == "2":
        search_name = input("Enter Name to Search: ")

        cursor.execute(
            "SELECT * FROM contacts WHERE name = ?",
            (search_name,)
        )

        result = cursor.fetchone()

        if result:
            print("\nContact Found")
            print("Name :", result[0])
            print("Mobile :", result[1])
        else:
            print("Contact Not Found")

    elif choice == "3":
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()

        if contacts:
            print("\n--- All Contacts ---")
            for contact in contacts:
                print("Name:", contact[0], "| Mobile:", contact[1])
        else:
            print("No Contacts Saved Yet.")

    elif choice == "4":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Try Again.")

# Close database connection
conn.close()