import mysql.connector
from admin import *
from staff import *
from customer import *
from package import *
from booking import *
from payment import *
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="san2410",
    database="travel"
)
cursor = conn.cursor()

def admin():
    while True:
        print("\n--- Admin Details ---")
        print("1. Add Admin \n2. Remove Admin \n3. Update Admin \n4. View Admins\n5. Exit ")
        choice = int(input("Enter Choice : "))
        if choice == 1:
            add_admin(cursor, conn)
        elif choice == 2:
            remove_admin(cursor, conn)
        elif choice == 3:
            update_admin(cursor, conn)
        elif choice == 4:
            view_admins(cursor)
        elif choice == 5:
            print("Thank you ")
            break
        else:
            print("Invalid Choice")

def staff():
    while True:
        print("\n--- Staff Details ---")
        print("1. Add Staff \n2. Remove Staff \n3. Update Staff \n4. View Staff\n5. Exit ")
        choice = int(input("Enter Choice : "))
        if choice == 1:
            add_staff(cursor, conn)
        elif choice == 2:
            remove_staff(cursor, conn)
        elif choice == 3:
            update_staff(cursor, conn)
        elif choice == 4:
            view_staff(cursor)
        elif choice == 5:
            print("Thank you ")
            break
        else:
            print("Invalid Choice")


def customer():
    while True:
        print("\n--- Customer Details ---")
        print("1. Add Customer \n2. Remove Customer \n3. Update Customer \n4. View Customer\n5. Exit ")
        choice = int(input("Enter Choice : "))
        if choice == 1:
            add_customer(cursor, conn)
        elif choice == 2:
            remove_customer(cursor, conn)
        elif choice == 3:
            update_customer(cursor, conn)
        elif choice == 4:
            view_customer(cursor)
        elif choice == 5:
            print("Thank you ")
            break
        else:
            print("Invalid Choice")


def package():
    while True:
        print("\n--- Packages Details ---")
        print("1. Add Package \n2. Delete Package \n3. Update Package Price \n4. View Packages \n5. Exit")
        choice = int(input("Enter Choice : "))
        if choice == 1:
            add_package(cursor, conn)
        elif choice == 2:
            delete_package(cursor, conn)
        elif choice == 3:
            update_package_price(cursor, conn)
        elif choice == 4:
            view_packages(cursor)
        elif choice == 5:
            print("Thank you ")
            break
        else:
            print("Invalid Choice")

def booking():
    while True:
        print("\n--- Admin Booking Menu ---")
        print("1. Add Booking\n2. Delete Booking (by Customer ID)\n3. Update Customer Phone\n4. View All Bookings \n5.View Customer\n6. Exit")
        choice = input("Enter Choice: ")

        if choice == "1":
            customer_id = int(input("Enter Customer ID for booking: "))
            add_booking(cursor, conn, customer_id)
        elif choice == "2":
            delete_booking_by_customer(cursor, conn)
        elif choice == "3":
            update_customer_phone(cursor, conn)
        elif choice == "4":
            view_bookings(cursor)
        elif choice == "5":
            view_customer(cursor)
        elif choice == "6":
            print("Exiting Booking Menu.")
            break
        else:
            print("Invalid choice!")

def payment():
    while True:
        print("\n--- Admin Payment Menu ---")
        print("1. View Payments")
        print("2. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            view_payments(cursor)
        elif choice == "2":
            print("Thank you")
            break
        else:
            print("Invalid Choice")

def admin_panal():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Admin Details \n2. Staff Details \n3. Customer Details \n4. Packages Details \n5. Booking Details \n6. Payment \n7. Exit")
        choice = int(input("Enter Choice : "))
        if choice == 1:
            admin()
        elif choice == 2:
            staff()
        elif choice == 3:
            customer()
        elif choice == 4:
            package()
        elif choice == 5:
            booking()
        elif choice == 6:
            payment()
        elif choice == 7:
            print("Thank you ")
            break
        else:
            print("Invalid Choice")

def staff_panel():
    while True:
        print("\n--- Staff Panel ---")
        print("1. View Packages\n2. Add Booking\n3. View Bookings\n4. Exit")
        choice = int(input("Enter Choice : "))
        if choice == 1:
            view_packages(cursor)
        elif choice == 2:
            try:
                customer_id = int(input("Enter Customer ID to book for: "))
                add_booking(cursor, conn, customer_id)
            except ValueError:
                print("Invalid Customer ID!")
        elif choice == 3:
            view_bookings(cursor)
        elif choice == 4:
            print("Thank You ")
            break
        else:
            print("Invalid choice!")

def customer_panel(customer_id, customer_name):
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Packages")
        print("2. Book Package")
        print("3. View My Bookings")
        print("4. Logout")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            cursor.execute("SELECT id, package_name, price FROM packages")
            packages = cursor.fetchall()
            print("\n--- Available Packages ---")
            for p in packages:
                print(f"ID:{p[0]}, Name:{p[1]}, Price:₹{p[2]}")
        elif choice == 2:
            add_booking(cursor, conn, customer_id, customer_name)
        elif choice == 3:
            view_my_bookings(cursor, customer_id)
        elif choice == 4:
            print("Logging out...")
            break
        else:
            print("Invalid choice")

while True:
    print("\n--- Login ---")
    print("1. Admin\n2. Staff\n3. Customer\n4. Exit")
    choice=input("Choice: ")

    if choice=='1':
        username=input("USERNAME : ")
        password=input("PASSWORD : ")
        cursor.execute("select id from admin where username=%s and password=%s",(username,password))
        if cursor.fetchone(): 
            admin_panal()
        else: 
            print("Invalid Admin ")
    elif choice=='2':
        username=input("Username: ")
        password=input("Password: ")
        cursor.execute("select id from staff where username=%s and password=%s",(username,password))
        if cursor.fetchone(): 
            staff_panel()
        else:
            print("Invalid Staff ")
    elif choice == '3':
        while True:
            print("\n1. Register Customer")
            print("2. Login Customer")
            print("3. Exit")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                add_customer(cursor, conn)

            elif choice == 2:
                username = input("Username : ")
                password = input("Password : ")

                cursor.execute(
                    "SELECT id, username FROM customer WHERE username=%s AND password=%s",
                    (username, password)
                )
                user = cursor.fetchone()

                if user:
                    customer_id = user[0]
                    customer_name = user[1]
                    print(f"Welcome {customer_name}!")
                    customer_panel(customer_id, customer_name)
                else:
                    print("Invalid Customer ID or Password")

            elif choice == 3:
                print("Exiting Customer Menu")
                break

            else:
                print("Invalid Choice")
    elif choice=='4':
        print("Thank you...")
        break
    else: print("Invalid choice!")
