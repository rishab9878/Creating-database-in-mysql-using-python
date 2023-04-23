import mysql.connector as a
con=a.connect(host="localhost",user="root",password="Rishab@2004")
c=con.cursor()
sql1="create database miniproject"
c.execute(sql1)
sql2="use miniproject"
c.execute(sql2)
sql3="create table bus(busno int(10),bustop varchar(20),distance int(10),time varchar(10),bustype varchar(10),numberofseats int(5),price int(10))"
c.execute(sql3)
sql4="create table passenger(name varchar(20),idno int(10),age int(5),date varchar(20))"
c.execute(sql4)
con.commit()

import mysql.connector as a

con = a.connect(host="localhost", user="root", password="Rishab@2004", database="miniproject")


def bus():
    bn = int(input("bus no:"))
    bs = input("bus stop:")
    ds = int(input("distance:"))
    t = input("timings:")
    bt = input("bus type:")
    ns = int(input("no of seats:"))
    p = ds * 10 * ns
    data = (bn, bs, ds, t, bt, ns, p)
    sql = 'insert into bus values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered successfully")
    c.execute('SELECT * FROM miniproject.aiport')
    for r in c:
        print(r)
    main()


def passenger():
    n = input("name:")
    idn = int(input("id no:"))
    age = int(input("age:"))
    dt = input("date:")
    data = (n, idn, age, dt)
    sql = 'insert into passenger values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered successfully")
    main()


def main():
    print("1.bus details")
    print("2.passenger details")
    c = int(input("choice:"))
    if c == 1:
        bus()
    elif c == 2:
        passenger()
    else:
        print("try again")
    main()


main()
