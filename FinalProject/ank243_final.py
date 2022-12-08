import pymysql.cursors
import uuid
import json
from flask import Flask
'''
Class List:
credit_card
customer_credit_card
customer_drinks
customer_order
customer_order_preference
customer_pizzas
customers
drinks
pizzas
sizes
toppings
'''

#configure the database
class Config:
    def __init__(self):
        self.db_conn = pymysql.connect(host="67.205.163.33", user="ank243", password="InfSci1500_4426782", db="ank243",charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor)

#create the customers class
class Customers:
    def __init__(self, customer_id = "", cust_name="", cust_address="", cust_phone=""):
        self.__custname = cust_name
        self.__custaddress = cust_address
        self.__custphone = cust_phone
        if customer_id == "":
            self.__custid = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO customers (pk_customers_id, customer_name, customer_address, customer_phone)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__custid, self.__custname, self.__custaddress, self.__custphone))
                    con.commit()
            finally:
                con.close()
        else:
            self.__custid = customer_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM customers WHERE pk_customers_id = '" + customer_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows=cur.fetchall()
                    for row in rows:
                        self.__custid = row["pk_customers_id"]
                        self.__custname = row["customer_name"]
                        self.__custaddress = row["customer_address"]
                        self.__custphone = row["customer_phone"]
            finally:
                con.close()
        
    def get_custid(self):
        return self.__custid
    def get_custname(self):
        return self.__custname
    def get_custaddress(self):
        return self.__custaddress
    def get_custphone(self):
        return self.__custphone
    
    def set_custname(self, name):
        self.__custname = name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE customers SET customer_name = %s WHERE pk_customers_id = %s;'
                print(qry)
                cur.execute(qry, (self.__custname, self.__custid))
                con.commit()
        finally:
            con.close()

    def set_custaddress(self, address):
        self.__custaddress = address
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE customers SET customer_address = %s WHERE pk_customers_id = %s;'
                print(qry)
                cur.execute(qry, (self.__custaddress, self.__custid))
                con.commit()
        finally:
            con.close()

    def set_custphone(self, phone):
        self.__custphone = phone
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE customers SET customer_phone = %s WHERE pk_customers_id = %s;'
                print(qry)
                cur.execute(qry, (self.__custphone, self.__custid))
                con.commit()
        finally:
            con.close()
    
    def del_customer(self, custid):
        self.__custid = custid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM customers WHERE pk_customers_id = %s'
                cur.execute(qry, (self.__custid))
                con.commit()
        finally:
            con.close()
    
    def sel_customer(self, custid):
        self.__custid = custid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM customers WHERE pk_customers_id = %s'
                cur.execute(qry, (self.__custid))
                con.commit()
        finally:
            con.close()

    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM customers'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    

    def to_json(self):
        return json.dumps(self.__dict__)

class Credit_Card:
    def __init__(self, credit_id="", credit_name="", credit_num="", credit_date=""):
        self.__creditname = credit_name
        self.__creditnumber = credit_num
        self.__creditdate = credit_date
        if credit_id == "":
            self.__creditid = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO credit_card (pk_creditcard_id, credit_name, credit_number, credit_expiration)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__creditid, self.__creditname, self.__creditnumber, self.__creditdate))
                    con.commit()
            finally:
                con.close()
        else:
            self.__creditid = credit_id
            try:
                config=Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM credit_card WHERE pk_creditcard_id = '" + credit_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__creditid = row["pk_creditcard_id"]
                        self.__creditname = row["credit_name"]
                        self.__creditnumber = row["credit_number"]
                        self.__creditdate = row["credit_expiration"]
            finally:
                con.close()

    def get_creditid(self):
        return self.__creditid
    def get_creditname(self):
        return self.__creditname
    def get_creditnumber(self):
        return self.__creditnumber
    def get_creditdate(self):
        return self.__creditdate

    def set_creditname(self, name):
        self.__creditname = name
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE credit_card SET credit_name = %s WHERE pk_creditcard_id = %s;'
                print(qry)
                cur.execute(qry, (self.__creditname, self.__creditid))
                con.commit()
        finally:
            con.close()
    
    def set_creditnumber(self, number):
        self.__creditnumber = number
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE credit_card SET credit_number = %s WHERE pk_creditcard_id = %s;'
                print(qry)
                cur.execute(qry, (self.__creditnumber, self.__creditid))
                con.commit()
        finally:
            con.close()
    
    def set_creditdate(self, date):
        self.__creditdate = date
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE credit_card SET credit_expiration = %s WHERE pk_creditcard_id = %s;'
                print(qry)
                cur.execute(qry, (self.__creditdate, self.__creditid))
                con.commit()
        finally:
            con.close()
    
    def del_credit(self, creditid):
        self.__creditid = creditid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM credit_card WHERE pk_creditcard_id = %s'
                cur.execute(qry, (self.__creditid))
                con.commit()
        finally:
            con.close()
    
    def sel_credit(self, creditid):
        self.__creditid = creditid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM credit_card WHERE pk_creditcard_id = %s'
                print(qry)
                cur.execute(qry, (self.__creditid))
                con.commit()
        finally:
            con.close()
    
    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM credit_card'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    
    def to_json(self):
        return json.dumps(self.__dict__)

class Drinks:
    def __init__(self, drink_id = "", drink_name = "", drink_price=""):
        self.__drinkname = drink_name
        self.__drinkprice = drink_price
        if drink_id == "":
            self.__drinkid = str(uuid.uuid4())
            try:
                config=Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO drinks (pk_drinks_id, drink_name, drink_price)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__drinkid, self.__drinkname, self.__drinkprice))
                    con.commit()
            finally:
                con.close()
        else:
            self.__drinkid = drink_id
            try:
                config=Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM drinks WHERE pk_drinks_id = '" + drink_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__drinkid = row["pk_drinks_id"]
                        self.__drinkname = row["drink_name"]
                        self.__drinkprice = row["drink_price"]
            finally:
                con.close()
    
    def get_drinkname(self):
        return self.__drinkname
    def get_drinkprice(self):
        return self.__drinkprice

    def set_drinkname(self, dname):
        self.__drinkname = dname
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE drinks SET drink_name = %s WHERE pk_drinks_id = %s;'
                print(qry)
                cur.execute(qry, (self.__drinkname, self.__drinkid))
                con.commit()
        finally:
            con.close()

    def set_drinkprice(self, dprice):
        self.__drinkprice = dprice
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE drinks SET drink_price = %s WHERE pk_drinks_id = %s;'
                print(qry)
                cur.execute(qry, (self.__drinkprice, self.__drinkid))
                con.commit()
        finally:
            con.close()

    def del_drink(self, drinkid):
        self.__drinkid = drinkid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM drinks WHERE pk_drinks_id = %s'
                cur.execute(qry, (self.__drinkid))
                con.commit()
        finally:
            con.close()
    
    def sel_doctor(self, drinkid):
        self.__drinkid = drinkid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM drinks WHERE pk_drinks_id = %s'
                cur.execute(qry, (self.__drinkid))
                con.commit()
        finally:
            con.close()

    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM drinks'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    
    def to_json(self):
        return json.dumps(self.__dict__)

class Sizes:
    def __init__(self, sizeid = "", sizename = "", sizeprice = ""):
        self.__sizename = sizename
        self.__sizeprice = sizeprice
        if sizeid == "":
            self.__sizeid = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO sizes (pk_sizes_id, sizes_name, sizes_price)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__sizeid, self.__sizename, self.__sizeprice))
                    con.commit()
            finally:
                con.close()
        else:
            self.__sizeid = sizeid
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM sizes WHERE pk_sizes_id = '" + sizeid + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__sizeid = row["pk_sizes_id"]
                        self.__sizename = row["sizes_name"]
                        self.__sizeprice = row["sizes_price"]
            finally:
                con.close()
    def get_sizename(self):
        return self.__sizename
    def get_sizeprice(self):
        return self.__sizeprice

    def set_sizename(self, name):
        self.__sizename = name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE sizes SET sizes_name = %s WHERE pk_sizes_id = %s;'
                print(qry)
                cur.execute(qry, (self.__sizename, self.__sizeid))
                con.commit()
        finally:
            con.close()

    def set_sizeprice(self, price):
        self.__sizeprice = price
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE sizes SET sizes_price = %s WHERE pk_sizes_id = %s;'
                print(qry)
                cur.execute(qry, (self.__sizeprice, self.__sizeid))
                con.commit()
        finally:
            con.close()
    
    def del_size(self, sizeid):
        self.__sizeid = sizeid
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM sizes WHERE pk_sizes_id = %s'
                cur.execute(qry, (self.__sizeid))
                con.commit()
        finally:
            con.close()
    
    def sel_size(self, sizeid):
        self.__sizeid = sizeid
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM sizes WHERE pk_sizes_id = %s'
                cur.execute(qry, (self.__sizeid))
                con.commit()
        finally:
            con.close()

    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM sizes'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()

    def to_json(self):
        return json.dumps(self.__dict__)

class Toppings:
    def __init__(self, topid = "", topname = ""):
        self.__toppingname = topname
        if topid == "":
            self.__toppingid = str(uuid.uuid4())
            try:
                config=Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO toppings (pk_toppings_id, topping_name)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__toppingid, self.__toppingname))
                    con.commit()
            finally:
                con.close()
        else:
            self.__toppingid = topid
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM toppings WHERE pk_toppings_id = '" + topid + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__toppingid = row ["pk_toppings_id"]
                        self.__toppingname = row ["topping_name"]
            finally:
                con.close()

    def get_topid(self):
        return self.__toppingid
    def get_topname(self):
        return self.__toppingname

    def set_topname(self, topname):
        self.__toppingname = topname
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE toppings SET topping_name = %s WHERE pk_toppings_id = %s;'
                print(qry)
                cur.execute(qry, (self.__toppingname, self.__toppingid))
                con.commit()
        finally:
            con.close()
    
    def del_topping(self, topid):
        self.__toppingid = topid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM toppings WHERE pk_toppings_id = %s'
                cur.execute(qry, (self.__toppingid))
                con.commit()
        finally:
            con.close()
    
    def sel_topping(self, topid):
        self.__toppingid = topid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM toppings WHERE pk_toppings_id = %s'
                cur.execute(qry, (self.__toppingid))
                con.commit()
        finally:
            con.close()

    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM toppings'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()

    def to_json(self):
        return json.dumps(self.__dict__)

class Customer_Credit_Card:
    def __init__(self, fk_customer = "", fk_credit = ""):
        self.__fk_customer_id = fk_customer
        self.__fk_creditcard_id = fk_credit

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'INSERT INTO customer_credit_card (fk_customer_id, fk_creditcard_id)'
                qry = qry + 'VALUES(%s, %s)'
                print(qry)
                cur.execute(qry, (self.__fk_customer_id, self.__fk_creditcard_id))
                con.commit()
        finally:
            con.close()


    def get_customerfk(self):
        return self.__fk_customer_id
    def get_creditfk(self):
        return self.__fk_creditcard_id
    
    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM customer_credit_card'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    
    def to_json(self):
        return json.dumps(self.__dict__)

class Customer_Order_Preference:
    def __init__(self, fkcustomer = "", fkorder = ""):
        self.__fk_customer = fkcustomer
        self.__fk_order = fkorder

        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'INSERT INTO customer_order_preference (fk_customer_id, fk_customer_order_id)'
                qry = qry + 'VALUES(%s, %s)'
                print(qry)
                cur.execute(qry, (self.__fk_customer, self.__fk_order))
                con.commit()
        finally:
            con.close()
    
    def get_customerfk(self):
        return self.__fk_customer
    def get_orderfk(self):
        return self.__fk_order

    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM customer_order_preference'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    
    def to_json(self):
        return json.dumps(self.__dict__)

class Customer_Drinks:
    def __init__(self, fkorder = "", fkdrink = ""):
        self.__fk_order = fkorder
        self.__fk_drink = fkdrink

        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'INSERT INTO customer_drinks (fk_customer_order_id, fk_drink_id)'
                qry = qry + 'VALUES(%s, %s)'
                print(qry)
                cur.execute(qry, (self.__fk_order, self.__fk_drink))
                con.commit()
        finally:
            con.close()
    
    def get_orderfk(self):
        return self.__fk_order
    def get_drinkfk(self):
        return self.__fk_drink
    
    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM customer_drinks'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    
    def to_json(self):
        return json.dumps(self.__dict__)

class Customer_Pizzas:
    def __init__(self, fkorder = "", fkpizza = ""):
        self.__fk_order = fkorder
        self.__fk_pizza = fkpizza

        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'INSERT INTO customer_pizzas (fk_customer_order_id, fk_pizza_id)'
                qry = qry + 'VALUES(%s, %s)'
                print(qry)
                cur.execute(qry, (self.__fk_order, self.__fk_pizza))
                con.commit()
        finally:
            con.close()
    
    def get_orderfk(self):
        return self.__fk_order
    def get_pizzafk(self):
        return self.__fk_pizza
    
    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM customer_pizzas'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    
    def to_json(self):
        return json.dumps(self.__dict__)

    
class Customer_Order:
    def __init__(self, custorder_id = "", price = "", fk_customer = "", fk_credit = ""):
        self.__orderprice = price
        self.__fk_customer = fk_customer
        self.__fk_creditcard = fk_credit

        if custorder_id == "":
            self.__orderid = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO customer_order (pk_cusomerorder_id, total_price, fk_customer_id, fk_creditcard_id)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__orderid, self.__orderprice, self.__fk_customer, self.__fk_creditcard))
                    con.commit()
            finally:
                con.close()
        else:
            self.__orderid = custorder_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM customer_order WHERE pk_cusomerorder_id = '" + custorder_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__orderid = row["pk_cusomerorder_id"]
                        self.__orderprice = row["total_price"]
                        self.__fk_customer = row["fk_customer_id"]
                        self.__fk_creditcard = row["fk_creditcard_id"]
            finally:
                con.close()
    
    def get_orderid(self):
        return self.__orderid
    def get_price(self):
        return self.__orderprice
    def get_fkcustomerid(self):
        return self.__fk_customer
    def get_fkcreditid(self):
        return self.__fk_creditcard
    
    def set_price(self, price):
        self.__orderprice = price
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE customer_order SET total_price = %s WHERE pk_cusomerorder_id = %s;'
                print(qry)
                cur.execute(qry, (self.__orderprice, self.__orderid))
                con.commit()
        finally:
            con.close()
    
    def del_order(self, orderid):
        self.__orderid = orderid
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM customer_order WHERE pk_cusomerorder_id = %s'
                cur.execute(qry, (self.__orderid))
                con.commit()
        finally:
            con.close()
    
    def sel_order(self, orderid):
        self.__orderid = orderid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM customer_order WHERE pk_cusomerorder_id = %s'
                cur.execute(qry, (self.__orderid))
                con.commit()
        finally:
            con.close()

    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM customer_order'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    
    def to_json(self):
        return json.dumps(self.__dict__)

class Pizzas:
    def __init__(self, pizzaid = "", fkpizzasize = "", fktopping1 = "", fktopping2 = "", pizzaname=""):
        self.__fk_psize = fkpizzasize
        self.__fk_topping1 = fktopping1
        self.__fk_topping2 = fktopping2
        self.__pizzaname = pizzaname
        if pizzaid == "":
            self.__pizza_id = str(uuid.uuid4())
            try:
                config=Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO pizzas (pk_pizzas_id, fk_pizzas_size, fk_pizzas_topping1, fk_pizzas_topping2, pizzas_name)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__pizza_id, self.__fk_psize, self.__fk_topping1, self.__fk_topping2, self.__pizzaname))
                    con.commit()
            finally:
                con.close()
        else:
            self.__pizza_id = pizzaid
            try:
                config=Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM pizzas WHERE pk_pizzas_id = '" + pizzaid + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__pizza_id = row["pk_pizzas_id"]
                        self.__fk_psize = row["fk_pizzas_size"]
                        self.__fk_topping1 = row["fk_pizzas_topping1"]
                        self.__fk_topping2 = row["fk_pizzas_topping2"]
                        self.__pizzaname = row["pizzas_name"]
            finally:
                con.close()
    
    def get_pizzaid(self):
        return self.__pizza_id
    def get_fksize(self):
        return self.__fk_psize
    def get_fktopping1(self):
        return self.__fk_topping1
    def get_fktopping2(self):
        return self.__fk_topping2
    def get_pizzaname(self):
        return self.__pizzaname

    def set_pizzaname(self, pname):
        self.__pizzaname = pname
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE pizzas SET pizzas_name = %s WHERE pk_pizzas_id = %s;'
                print(qry)
                cur.execute(qry, (self.__pizzaname, self.__pizza_id))
                con.commit()
        finally:
            con.close()
    
    def del_pizza(self, pizzaid):
        self.__pizza_id = pizzaid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM pizzas WHERE pk_pizzas_id = %s'
                cur.execute(qry, (self.__pizza_id))
                con.commit()
        finally:
            con.close()
    
    def sel_pizza(self, pizzaid):
        self.__pizza_id = pizzaid
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM pizzas WHERE pk_pizzas_id = %s'
                cur.execute(qry, (self.__pizza_id))
                con.commit()
        finally:
            con.close()
    
    def show_table(self):
        try:
            config=Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM pizzas'
                print(qry)
                cur.execute(qry)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")
        finally:
            con.close()
    
    def to_json(self):
        return json.dumps(self.__dict__)




test3 = Customers("", "Stranger", "24 Elm Street", "612-888-8888")
test4 = Credit_Card("", "Stranger", "8888777766663333", "09/24")
test5 = Toppings("", "Olives")

test3.sel_customer("09867495-502d-4bcb-85b4-7e6efe423905")
test4.sel_credit("4eb91903-c287-4ce8-99e6-cf9af0653fe9")
test5.sel_topping("5d5ff9ba-8e0e-4498-a6d5-973ac5fee225")

test3.del_customer("55072c89-b128-4136-b384-d828a922f494")
test4.del_credit("4eb91903-c287-4ce8-99e6-cf9af0653fe9")
test5.del_topping("5707c6c1-b83e-4884-a4a5-832fb7460b6a")


print(test3.to_json())
print(test4.to_json())
print(test5.to_json())