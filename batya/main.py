# coding: utf8
# Python 2.7.13
import config
import download
import mysql.connector
import io


def upload_to_database(file_name, cnt):
    with io.open(file_name, "r", encoding="cp1251") as f:
        upload_cr = cnt.cursor()
        f.next()
        for line in f:
            if line != "\n":
                buf = line[:-1].encode("utf-8").split("\t;\t")
                #command = "call insert_new_record({},{},{},'{}','{}');".format(buf[0], buf[1], buf[2], buf[4], buf[5])
                upload_cr.callproc("insert_new_record", (buf[0], buf[1], buf[2], buf[4], buf[5]))
                #commands.append(command)

        cnt.commit()
    # upload_cr = cnt.cursor()
    # upload_cr.execute("\n".join(commands), multi=True)
    # upload_cr.executemany("call insert_new_record(%d,%d,%d,'%s','%s')", commands)


download.downloadAll()
try:
    main_connect = mysql.connector.connect(**config.dbconnet)
    cur = main_connect.cursor()
    # cur.execute("select * from operators; ")
    upload_to_database("downloads/Kody_ABC-3kh.csv",  main_connect)
    upload_to_database("downloads/Kody_ABC-4kh.csv", main_connect)
    upload_to_database("downloads/Kody_ABC-8kh.csv", main_connect)
    upload_to_database("downloads/Kody_ABC-9kh.csv", main_connect)
except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Wrong userName or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)

else:
    main_connect.close()
