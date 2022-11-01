import uuid
import pymysql.cursors
import json
import pylint
import unittest
from flask import Flask

app = Flask(__name__)

'''
Class List:
Doctor
Patient
Visit
Diagnosis
Procedure
'''



#configure the database
class Config:
    def __init__(self):
        self.db_conn = pymysql.connect(host="67.205.163.33", user="ank243", password="InfSci1500_4426782",db="ank243", charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor)

#create the doctor class
class Doctor:
    def __init__(self, duser_id = "", fname = "", lname=""):
        """Constructor for Doctor Class"""
        self.__docfname = fname
        self.__doclname = lname
        if duser_id == "":
            self.__duser_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO doctor (doctor_id, dfname, dlname)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__duser_id, self.__docfname, self.__doclname))
                    con.commit()
            finally:
                con.close()
        else:
            self.__duser_id = duser_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM doctor WHERE doctor_id = '" + duser_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__duser_id = row["doctor_id"]
                        self.__docfname = row["dfname"]
                        self.__doclname = row["dlname"]
            finally:
                con.close()
    def get_fname(self):
        """Get Doctor First Name"""
        return self.__docfname
    def get_lname(self):
        """Get Doctor Last Name"""
        return self.__doclname
    def get_duser_id(self):
        """Get Doctor ID"""
        return self.__duser_id

    def set_fname(self, fname):
        """Set Doctor First Name"""
        self.__docfname = fname
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET dfname = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__docfname, self.__duser_id))
                con.commit()
        finally:
            con.close()

    def set_lname(self, lname):
        """Set Doctor Last Name"""
        self.__doclname = lname
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET dlname = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__doclname, self.__duser_id))
                con.commit()
        finally:
            con.close()

    def del_doctor(self, duser_id):
        """Delete Doctor Entry"""
        self.__duser_id = duser_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM doctor WHERE doctor_id = %s'
                cur.execute(qry, (self.__duser_id))
                con.commit()
        finally:
            con.close()
    
    def sel_doctor(self, duser_id):
        """Select Doctor Entry"""
        self.__duser_id = duser_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'SELECT * FROM doctor WHERE doctor_id = %s'
                cur.execute(qry, (self.__duser_id))
                con.commit()
        finally:
            con.close()

    def to_json(self):
        """Doctor To JSON"""
        return json.dumps(self.__dict__)


class TestDoctorClass(unittest.TestCase):
    def test_update_doctor(self):
        doc1 = Doctor("34fd6a54-c25d-4b86-ac27-6e87d2a449b4", "Kenny", "Pickett")
        doc1.set_lname("Heisman")
        self.assertEqual(doc1.get_lname(), "Heisman", "incorrect Last Name")

    def test_create_doctor(self):
        doc3 = Doctor("fd889ea8-d8a2-47ce-9fd0-d931132cb6d8", "Big", "Ben")
        self.assertEqual(doc3.get_duser_id(), "fd889ea8-d8a2-47ce-9fd0-d931132cb6d8", "Doctor was not created")

    def test_delete_doctor(self):
        doc4 = Doctor("866faf0a-314a-46fc-a6c6-6f0b6a129e94", "Roger", "Federer")
        doc4.del_doctor("866faf0a-314a-46fc-a6c6-6f0b6a129e94")
        self.assertFalse(doc4.sel_doctor("866faf0a-314a-46fc-a6c6-6f0b6a129e94"), "Doctor was not Deleted")




class Patient:
    def __init__(self, puser_id = "", fname = "", lname = "", phone = "", addy = ""):
        """Constructor for Patient Class"""
        self.__patfname = fname
        self.__patlname = lname
        self.__phone_number = phone
        self.__address = addy
        if puser_id == "":
            self.__puser_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO patient (patient_id, pfname, plname, phone_number, address)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__puser_id, self.__patfname, self.__patlname, 
                    self.__phone_number, self.__address))
                    con.commit()
            finally:
                con.close()
        else:
            self.__puser_id = puser_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient WHERE patient_id = '" + puser_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__puser_id = row["patient_id"]
                        self.__patfname = row["pfname"]
                        self.__patlname = row["plname"]
                        self.__phone_number = row["phone_number"]
                        self.__address = row["address"]
            finally:
                con.close()
    def get_fname(self):
        """Get Patient First Name"""
        return self.__patfname
    def get_lname(self):
        """Get Patient Last Name"""
        return self.__patlname
    def get_phone_number(self):
        """Get Patient Phone Number"""
        return self.__phone_number
    def get_address(self):
        """Get Patient Address"""
        return self.__address
    def get_puser_id(self):
        """Get Patient ID"""
        return self.__puser_id

    def set_fname(self, fname):
        """Set Patient First Name"""
        self.__patfname = fname
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET pfname = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__patfname, self.__puser_id))
                con.commit()
        finally:
            con.close()

    def set_lname(self, lname):
        """Set Patient Last Name"""
        self.__patlname = lname
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET plname = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__patlname, self.__puser_id))
                con.commit()
        finally:
            con.close()

    def set_phone_number(self, phone):
        """Set Patient Phone Number"""
        self.__phone_number = phone
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET phone_number = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__phone_number, self.__puser_id))
                con.commit()
        finally:
            con.close()

    def set_address(self, addy):
        """Set Patient Address"""
        self.__address = addy
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET address = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__address, self.__puser_id))
                con.commit()
        finally:
            con.close()

    def to_json(self):
        """Patient Class TO JSON"""
        return json.dumps(self.__dict__)

class Visit:
    def __init__(self, visit_id = "", visit_location = "", visit_date = "", reason = "", fk_doctor_id = "", fk_patient_id = ""):
        """Constructor for Visit Class"""
        self.__vlocation = visit_location
        self.__vdate = visit_date
        self.__vreason = reason
        self.__doctor = fk_doctor_id
        self.__patient = fk_patient_id
        self.__diagnosis = []
        self.__procedure = []
        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO visit (visit_id, location, visit_date, visit_reason, address, fk_doctor_id, fk_patient_id)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__visit_id, self.__vlocation, self.__vdate, self.__vreason, self.__doctor, self.__patient))
                    con.commit()
            finally:
                con.close()
        else:
            self.__visit_id = visit_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM visit WHERE visit_id = '" + visit_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__visit_id = row["visit_id"]
                        self.__vlocation = row["location"]
                        self.__vdate = row["visit_date"]
                        self.__vreason = row["visit_reason"]
                        self.__doctor = row["fk_doctor_id"]
                        self.__patient = row["fk_patient_id"]
            finally:
                con.close()

    def get_location(self):
        """Get Visit Location"""
        return self.__vlocation
    def get_date(self):
        """Get Visit Date"""
        return self.__vdate
    def get_reason(self):
        """Get Visit Reason"""
        return self.__vreason
    def get_doctor_id(self):
        """Get Doctor ID"""
        return self.__doctor
    def get_patient_id(self):
        """Get Patient ID"""
        return self.__patient

    def add_diagnosis(self, diagnosis_id):
        """Add Diagnosis to Visit"""
        self.__diagnosis.append(diagnosis_id)
    def add_procedure(self, procedure_id):
        """Add Procedure to Visit"""
        self.__procedure.append(procedure_id)

    def to_json(self):
        """Visit Class To JSON"""
        return json.dumps(self.__dict__)


class Diagnosis:
    def __init__(self, diag_id = "", diag_name = ""):
        """Constructor for Diagnosis Class"""
        self.__diagnosis = diag_name
        if diag_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO diagnosis (diag_id, diag_name)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__diagnosis_id, self.__diagnosis))
                    con.commit()
            finally:
                con.close()
        else:
            self.__diagnosis_id = diag_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM diagnosis WHERE diag_id = '" + diag_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__diagnosis_id = row["diag_id"]
                        self.__diagnosis = row["diag_name"]
            finally:
                con.close()

    def get_diagnosis_id(self):
        """Get Diagnosis ID"""
        return self.__diagnosis_id
    def get_diagnosis(self):
        """Get Diagnosis"""
        return self.__diagnosis
    
    def set_diagnosis(self, diag_name):
        """Set Diagnosis"""
        self.__diagnosis = diag_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diag_name = %s WHERE diag_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis, self.__diagnosis_id))
                con.commit()
        finally:
            con.close()
    
    def to_json(self):
        """Diagnosis Class to JSON"""
        return json.dumps(self.__dict__)


class Procedure:
    def __init__(self, proc_id = "", proc_name = ""):
        """Constructor for Procedure Class"""
        self.__procname = proc_name
        if proc_id == "":
            self.__procedure_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO procedure (proc_id, proc_name)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__procedure_id, self.__procname))
                    con.commit()
            finally:
                con.close()
        else:
            self.__procedure_id = proc_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM procedure WHERE proc_id = '" + proc_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__procedure_id = row["proc_id"]
                        self.__procname = row["proc_name"]
                        
            finally:
                con.close()


    def get_procedure(self):
        """Get Procedure"""
        return self.__procname
    def get_procedure_id(self):
        """Get Procedure ID"""
        return self.__procedure_id

    def to_json(self):
        """Procedure Class TO JSON"""
        return json.dumps(self.__dict__)


#doc = Doctor("ce4d2071-9934-44fe-a22a-d73feca1e95c", "Larry", "Doe")
#doc.set_lname("Johnson")
#doc1 = Doctor("34fd6a54-c25d-4b86-ac27-6e87d2a449b4", "Kenny", "Pickett")
#doc2 = Doctor("b8961126-2f2e-442d-bca8-8213c9c7793e", "TJ", "Watt")

#NOT SURE IF I LEAVE THIS COMMENTED OR NOT FOR RUNNING THE FLASK APP
#unittest.main()


@app.route('/')
def index():
    pat1 = Patient("24026261-977a-46d9-af69-ac526dc4b9b8", "Andrew", "Kistner", "724-777-7777", "724 Window Lane")
    doctor1 = Doctor("cfdf6a75-732f-4a53-9d0d-c56d1a2b8989", "Jim", "Timmy")
    visit1 = Visit("212bb090-64c0-4a74-b239-d3b50d963aff", "Oakland", "11/12/2021", "sore throat", "cfdf6a75-732f-4a53-9d0d-c56d1a2b8989", "24026261-977a-46d9-af69-ac526dc4b9b8")
    visit2 = Visit("43b66098-2ade-4fc0-b329-9c713f728945", "Oakland", "11/15/2021", "headache", "cfdf6a75-732f-4a53-9d0d-c56d1a2b8989", "24026261-977a-46d9-af69-ac526dc4b9b8")
    return visit1.to_json(), visit2.to_json()



        