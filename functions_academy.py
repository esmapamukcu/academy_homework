import pymysql

db=pymysql.connect(host='127.0.0.1',
                   user='root',
                   password='****',
                   db='academy',
                   charset='utf8mb4',
                   cursorclass=pymysql.cursors.DictCursor)

conn=db.cursor()

def add_data_students():
    ListTblStudents()
    counter = 1
    usersize = int(input("Kaç tane veri girilecek? :"))
    while counter <= usersize:
        #midterm = 0
        #final = 0
        #average = 0
        #lettergrade = 'XX'
        stdNo = int(input('Eklenmek istenen öğrenci numarası :'))
        name = input('Eklenmek istenen isim :')
        surname = input('Eklenmek istenen soyisim :')
        phone = input('Eklenmek istenen telefon numarası :')
        mail = input('Eklenmek istenen email adresi :')
        print("Kayıt eklenmiştir.")
        counter = counter + 1
        conn.execute("INSERT INTO tbl_students (std_no,std_name, std_surname, std_phone, std_mail) VALUES (%s,%s, %s, %s, %s)",(stdNo,name, surname, phone, mail))
        #conn.execute("INSERT INTO tbl_grades_math (StdNo,midterm,final,average,letterGrade) VALUES (%s,%s,%s,%s,%s)",(stdNo,midterm,final,average,lettergrade))
        db.commit()

def delete_students():
    ListTblStudents()
    id = input('Lütfen silinecek kaydın numarasını(ID) yazınız :')
    mail = input('Silinecek kaydın email adresi :')
    print("Öğrenci kaydı silinmiştir.")
    conn.execute(f"DELETE FROM tbl_students where ID='{id}' and std_mail='{mail}'")
    db.commit()
    db.close()


def update_isim():
    ListTblStudents()
    id = input('Lütfen adını güncellemek istediğiniz kişinin numarasını(ID) yazınız :')
    name = input('Lütfen yeni adı giriniz :')
    print("Kayıt güncellenmiştir.")
    conn.execute(f"Update tbl_students set std_name='{name}' where ID='{id}'")
    db.commit()
    db.close()


def update_soyisim():
    ListTblStudents()
    id = input('Lütfen soyadını güncellemek istediğiniz kişinin numarasını(ID) yazınız :')
    surname = input('Lütfen yeni soyadı giriniz :')
    print("Kayıt güncellenmiştir.")
    conn.execute(f"Update tbl_students set std_surname='{surname}' where ID='{id}'")
    db.commit()
    db.close()


def update_tel():
    ListTblStudents()
    id = input('Lütfen telefonunu güncellemek istediğiniz kişinin numarasını(ID) yazınız :')
    phone = input('Lütfen yeni numarayı giriniz :')
    print("Kayıt güncellenmiştir.")
    conn.execute(f"Update tbl_students set std_phone='{phone}' where ID='{id}'")
    db.commit()
    db.close()


def update_email():
    ListTblStudents()
    id = input('Lütfen mail adresini güncellemek istediğiniz kişinin numarasını(ID) yazınız :')
    mail = input('Lütfen yeni mail adresini giriniz :')
    print("Kayıt güncellenmiştir.")
    conn.execute(f"Update tbl_students set std_mail='{mail}' where ID='{id}'")
    db.commit()
    db.close()

###########################

def add_data_grades():
    ListTblGradesMath()
    counter = 1
    gradesize = int(input("Kaç tane veri girilecek? :"))
    while counter <= gradesize:
        stdNo = int(input("Lütfen öğrenci numarası giriniz :"))
        midterm = float(input('Lütfen vize notu giriniz :'))
        final=float(input('Lütfen final notu giriniz :'))
        average = float((midterm * 0.4) + (final * 0.6))
        lettergrade = getGrade(average)
        print("Kayıt eklenmiştir.")
        counter = counter + 1
        conn.execute("INSERT INTO tbl_grades_math (StdNo,midterm,final,average,letterGrade) VALUES (%s,%s,%s,%s,%s)",(stdNo, midterm, final, average, lettergrade))
        db.commit()


def getGrade(average):
    lettergrade = ""

    if average >= 90:
        lettergrade = "AA"
    elif average >= 85:
        lettergrade = "BA"
    elif average >= 75:
        lettergrade = "BB"
    elif average >= 55:
        lettergrade = "CC"
    else:
        lettergrade = "FF"

    return lettergrade


def delete_grades():
    ListTblGradesMath()
    id = int(input('Lütfen silinecek kaydın numarasını(ID) yazınız :'))
    print("Not kaydı silinmiştir.")
    conn.execute(f"DELETE FROM tbl_grades_math where ID='{id}'")
    db.commit()
    db.close()

def update_exams():
    ListTblGradesMath()
    counter = 1
    gradesize = int(input("Kaç tane veri güncellenecek? :"))
    while counter <= gradesize:
        id = int(input('Lütfen güncelleme yapacağınız öğrencinin numarasını(ID) yazınız :'))
        midterm = float(input('Lütfen yeni vize notu giriniz :'))
        final = float(input('Lütfen yeni final notu giriniz :'))
        average = float((midterm * 0.4) + (final * 0.6))
        lettergrade = getGrade(average)
        print("Kayıt güncellenmiştir.")
        counter = counter + 1
        conn.execute(f"Update tbl_grades_math set midterm={midterm}, final={final}, average={average}, letterGrade='{lettergrade}' where ID='{id}'")
        db.commit()

##############################

def ListTblStudents():
    print("*********Veritabanındaki güncel veriler aşağıda listelenmiştir.*********")
    print("ID, öğrenciNo, İsim, Soyisim, telefonNumarası, mailAdresi ")
    conn.execute("SELECT * FROM tbl_students")
    db.commit()
    data = conn.fetchall()
    for i in data:
        print(i["ID"],"--- ", i["std_no"],"--- ",i["std_name"],"--- ",i["std_surname"],"--- ",i["std_phone"],"--- ",i["std_mail"])

def ListTblGradesMath():
    print("*********Veritabanındaki güncel veriler aşağıda listelenmiştir.*********")
    print("ID, öğrenciNo, vizeNotu, finalNotu, ortalama, harfNotu ")
    conn.execute("SELECT * FROM tbl_grades_math")
    db.commit()
    data = conn.fetchall()
    for i in data:
        print(i["ID"],"--- ",i["StdNo"], "--- ", i["midterm"], "--- ", i["final"], "--- ", i["average"], "--- ", i["letterGrade"])


def ListGradesandStudents():
    conn.execute("SELECT * FROM tbl_students INNER JOIN tbl_grades_math on tbl_students.std_no=tbl_grades_math.StdNo")
    db.commit()
    data = conn.fetchall()
    for i in data:
        print(i["ID"], "--- ", i["std_no"], "--- ", i["std_name"], "--- ", i["std_surname"], "--- ", i["std_phone"],
              "--- ", i["std_mail"], i["ID"], "--- ", i["StdNo"], "--- ", i["midterm"], "--- ", i["final"], "--- ",
              i["average"], "--- ", i["letterGrade"])


def list_std():
    ListTblStudents()
    id = input('Görüntülemek istediğiniz kaydın numarasını(ID) yazınız :')
    conn.execute(f"SELECT * FROM tbl_students WHERE ID='{id}'")
    db.commit()


def list_grade():
    ListTblGradesMath()
    id = input('Görüntülemek istediğiniz kaydın numarasını(ID) yazınız :')
    conn.execute(f"SELECT * FROM std_grades_math WHERE ID='{id}'")
    db.commit()

