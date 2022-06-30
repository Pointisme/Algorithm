from tkinter import *
import pymysql

# def python():
#     sql="select * from Doctor_Info"
#     curs.execute(sql)
#     rows=curs.fetchall()
#     print(type(rows[0][0]))
#     print(len(rows))
    
# conn=pymysql.connect(host="localhost",user="root",password="cnu_root_3401",db="hospital",charset="utf8")
# curs=conn.cursor()

# c=python()

# def no():
#     sql="""insert into Diagnosis(Patient_name,Doctor_name,Diease_name,Diagnosis_date)
#     values (%s, %s, %s,now())"""
#     curs.execute(sql,('돼지','김정훈','복통'))
    
# p=no()
# conn.commit()
# conn.close()

win=Tk()

ent=Entry(win)
btn=Button(win,command=px)
def px():
    a=ent.get()
    []
btn.pack()
print(a)
ent.pack()

win.mainloop()