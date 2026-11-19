def add_customer(cursor, conn):
    name = input("Enter the Name : ")
    proff_id = int(input("Enter the Aadhar number : "))
    phone_no = int(input("Enter the Phone No : "))
    username = input("Enter customer username: ")
    password = input("Enter password: ")
    q = "insert into customer ( name,proff_id,phone_no,username, password) VALUES (%s,%s,%s,%s, %s)" 
    values = (name,proff_id,phone_no,username, password)
    c = conn.cursor()
    res=c.execute(q,values)
    conn.commit()
    if res != 0:
        print("customer added successfully")
    else:
        print("customer added Failed")



def remove_customer(cursor, conn):
    customer_id = input("Enter customer ID to remove: ")
    q = "delete from customer where id = %s"
    c = conn.cursor()
    res = c.execute(q,(customer_id,))
    conn.commit()
    if res != 0:
        print("customer removed successfully")
    else:
        print("customer removed Failed")


def update_customer(cursor, conn):
    customer_id = input("Enter customer ID : ")
    new_password = input("Enter new password: ")
    q = "update customer set password = %s where id = %s"
    c = conn.cursor()
    values = (new_password,customer_id)
    res = c.execute(q,values)
    conn.commit()
    if res != 0:
        print("customer updated successfully")
    else:
        print("customer updated Failed")


def view_customer(cursor):
    q = "select * from customer"
    cursor.execute(q)
    m = cursor.fetchall()
    print("\n--- Customer List ---")
    for i in m:
        print("ID : ", i[0] ,"| Name : ",i[1], "| PROFF_ID : ",i[2],"| Mobile : ",i[3], "| Username : ",i[4] ,"| Password : ",i[5])
    else:
        print("No customer found.")
