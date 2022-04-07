import pymysql
import functions_academy

db=pymysql.connect(host='127.0.0.1',
                   user='root',
                   password='****',
                   db='academy',
                   charset='utf8mb4',
                   cursorclass=pymysql.cursors.DictCursor)

conn=db.cursor()


while True:
    choice = input( 'Veritabanında: '
                    '\n1-Öğrencileri kaydetme,silme,güncelleme ve listeleme işlemleri için--> 1 '
                    '\n2-Öğrencilerin notlarını ekleme,silme,güncelleme ve listeleme işlemleri için--> 2 '
                    '\n3-Öğrencilerin notlarını ve bilgilerini birlikte görüntülemek için--> 3'
                    '\nBasınız :')

    try:
        choice = int(choice)
        break
    except ValueError:
        print("Lütfen bir sayı değeri giriniz!")
        continue

if choice == 1:
    mes = input('Veritabanında öğrenci: '
                '\n1-Ekleme işlemi için-->E '
                '\n2-Silme işlemi için-->S '
                '\n3-Listeleme işlemi için-->L '
                '\n4-Güncelleme işlemi için-->G '
                '\nBasınız :')

    if mes.upper() == "E":
        functions_academy.add_data_students()

    elif mes.upper() == "S":
        functions_academy.delete_students()

    elif mes.upper() == "L":
        mes_list=input("Tüm öğrenci listesini görüntelemek için--> *"
                        "\nBir öğrenci görüntülemek için--> 1"
                        "\nBasınız :")

        if mes_list == "*":
            functions_academy.ListTblStudents()
        elif mes_list == 1:
            functions_academy.list_std()

    elif mes.upper() == "G":
        mes_update=input("Öğrencinin adını güncellemek için--> A"
                        "\nÖğrencinin soyadını güncellemek için--> S"
                        "\nÖğrencinin telefonunu güncellemek için--> T"
                        "\nÖğrencinin mail adresini güncellemek için--> M"
                        "\nBasınız :")
        if mes_update.upper() == 'A':
            functions_academy.update_isim()
        elif mes_update.upper() == 'S':
            functions_academy.update_soyisim()
        elif mes_update.upper() == 'T':
            functions_academy.update_tel()
        elif mes_update.upper() == 'M':
            functions_academy.update_email()


elif choice == 2:
    mes = input('Veritabanında not: '
                '\n1-Ekleme işlemi için-->E '
                '\n2-Silme işlemi için-->S '
                '\n3-Listeleme işlemi için-->L '
                '\n4-Güncelleme işlemi için-->G '
                '\nBasınız :')

    if mes.upper() == 'E':
        functions_academy.add_data_grades()
    elif mes.upper() == 'S':
        functions_academy.delete_grades()
    elif mes.upper() == 'L':
        mes_list=input("Tüm öğrenci notlarını görüntülemek için--> *"
                        "\nBir öğrencinin notunu görüntülemek için--> 1"
                        "\nBasınız :")
        if mes_list == '*':
            functions_academy.ListTblGradesMath()
        elif mes_list == 1:
            functions_academy.list_grade()
    elif mes.upper() == 'G':
        functions_academy.update_exams()

elif choice == 3:
    functions_academy.ListGradesandStudents()



#list_std çalışmıyor

#list_grade çalışmıyor.

#elif==3 çalışmıyor.