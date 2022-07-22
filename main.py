
from tabulate import  tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="root",database="nathiya")



def insert(name,age,city):
    res=con.cursor()
    sql="insert into user(name,age,city) values(%s,%s,%s)"
    users=(name,age,city)
    res.execute(sql,users)
    con.commit()    #save the data
    print("data insert success")

def update(name,age,city,id):
    res = con.cursor()
    sql = "update  user set name=%s,age=%s,city=%s  where id =%s"
    users = (name, age, city,id)
    res.execute(sql, users)
    con.commit()  # save the data
    print("data update success")


def select():
    res=con.cursor()
    sql="select  ID,NAME,AGE,CITY from user"
    res.execute(sql)
    #result=res.fetchone()
    #result=res.fetchmany(2)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

def delete(id):
    res = con.cursor()
    sql = "delete  from user   where id =%s"
    users = (id,)
    res.execute(sql, users)
    con.commit()  # save the data
    print("data delete success")


while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        name=input("enter the name: ")
        age=input("enter the age: ")
        city=input("enter the city: ")
        insert(name,age,city)
    elif choice==2:
        id=input("enter the id: ")
        name = input("enter the name: ")
        age = input("enter the age: ")
        city = input("enter the city: ")
        update(name, age, city,id)
    elif choice==3:
        select()
    elif choice==4:
        id=input("enter the id to delete:")
        delete(id)
    elif choice==5:
        quit()
    else:
        print("invalid selection")

