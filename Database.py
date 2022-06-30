import tkinter.ttk as ttk

try:
    import tkinter as tk
except:
    import tkinter as tk
    
import pymysql

conn=pymysql.connect(host="localhost",user="root",password="cnu_root_3401",db="hospital",charset="utf8")
curs=conn.cursor()
class Patient_DB(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame=None
        self.switch_frame(SelectPage)

    def switch_frame(self,frame_class):
        new_frame=frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame=new_frame
        self._frame.pack()

class SelectPage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)

        tk.Button(self,text="신규 환자",command=lambda:master.switch_frame(New_Patient)).pack()
        tk.Button(self,text="내원 이력",command=lambda:master.switch_frame(Diagnosis)).pack()
        tk.Button(self,text="의사 정보",command=lambda:master.switch_frame(Doctor_Info)).pack()
        tk.Button(self,text="관리 질병",command=lambda:master.switch_frame(Diease_Info)).pack()

class New_Patient(tk.Frame):    #신규관리 환자 기입
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        tk.Label(self,text="신규 환자",font=("bold")).pack(fill="x")
        tk.Label(self,text="이름 ",font=("bold")).pack(fill="x")
        a=tk.Entry(self)
        a.pack()
        tk.Label(self,text="등록번호",font=("bold")).pack(fill="x")
        b=tk.Entry(self)
        b.pack()
        tk.Label(self,text="주소",font=("bold")).pack(fill="x")
        c=tk.Entry(self)
        c.pack()
        tk.Button(self,text="신규등록",command=lambda:[save_patient(),master.switch_frame(SelectPage)]).pack()
        def save_patient():
            pat_name=a.get()
            pat_age=int((b.get()))
            pat_add=c.get()
            sql="""insert into Patient_Info(Patient_name,registration_num,address)
            values(%s, %s, %s)"""
            curs.execute(sql,(pat_name,pat_age,pat_add))
            conn.commit()
        #tk.Button(self,text="초기화면",command=lambda:master.switch_frame(SelectPage)).pack()
      
class Diagnosis(tk.Frame):  #진단 테이블에 추가하는것
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        tk.Label(self,text="환자 정보",font=("bold")).pack(side="top",fill='x',pady=5)
        
 
        combobox_1=ttk.Combobox(self)
        combobox_1.set("환자이름")
        combobox_2=ttk.Combobox(self)
        combobox_2.set("등록번호")
        
        combobox_3=ttk.Combobox(self)
        combobox_3.set("의사이름")
        combobox_4=ttk.Combobox(self)
        combobox_4.set("진단명")

        sql_1="select * from Patient_Info"
        sql_2="select * from Patient_Info"
        sql_3="select * from Doctor_Info"
        sql_4="select * from Diease"


        curs.execute(sql_1)
        row_1=list(curs.fetchall())
        show_row_1=[]
        for i in row_1:
            show_row_1.append(i[0])
        combobox_1.config(values=show_row_1)
        combobox_1.pack()

        curs.execute(sql_2)
        row_2=list(curs.fetchall())
        show_row_2=[]
        for i in row_2:
            show_row_2.append(i[1])
        combobox_2.config(values=show_row_2)
        combobox_2.pack()
        
        
        # curs.execute(sql_3)
        # row_3=list(curs.fetchall())
        # show_row_3=[]
        # for i in row_3:
        #     show_row_3.append(i[0])
        # combobox_3.config(values=show_row_3)
        # combobox_3.pack()




        curs.execute(sql_4)
        row_4=list(curs.fetchall())
        show_row_4=[]
        for i in row_4:
            show_row_4.append(i[0])
        combobox_4.config(values=show_row_4)
        combobox_4.pack()


        def make_list():
            pat_list=combobox_1.get()
            reg_list=combobox_2.get()
            doc_list=combobox_3.get()
            dis_list=combobox_4.get()

            if pat_list !=None and doc_list !=None and dis_list!=None:
                sql="""insert into Diagnosis(Patient_name,registration_num,Doctor_name,Diease_name,Diagnosis_date)
                values (%s, %s, %s,%s,now())"""
                curs.execute(sql,(pat_list,reg_list,doc_list,dis_list))
                conn.commit()
            
        
        def do_list():
            name=combobox_4.get()

            sql5="select * from Doctor_info where Diease_name=%s" 
            curs.execute(sql5,name)
            row_3=list(curs.fetchall())
            show_row_3=[]
            for i in row_3:
                show_row_3.append(i[0])
            combobox_3.config(values=show_row_3)
            combobox_3.pack()   
            tk.Button(self,text="접수",command=lambda:[make_list(),master.switch_frame(SelectPage)]).pack()
            tk.Button(self,text="초기화면",command=lambda: master.switch_frame(SelectPage)).pack()



        tk.Button(self,text="의사 검색",command=lambda:do_list()).pack()
       


class Doctor_Info(tk.Frame):    #의사의 정보
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        tk.Label(self,text="의사이름",font=("bold")).pack(side="top",fill='x',pady=5)
        listbox=tk.Listbox(self)
        listbox.insert(0,"Anni")
        listbox.insert(1,"Han")
        listbox.insert(2,"Kevin")
        listbox.insert(3,"Harry")
        listbox.insert(4,"Jule")
        listbox.insert(5,"Kary")
        listbox.insert(6,"Lee")
        listbox.insert(7,"Kim")
        listbox.insert(8,"Park")
        listbox.insert(9,"Porter")
        
        listbox.pack()
        tk.Button(self,text="의사정보",command=lambda:look_doctor()).pack()
        tk.Button(self,text="초기화면",command=lambda:master.switch_frame(SelectPage)).pack()

        def look_doctor():
            text=listbox.curselection()[0]
            if text==0:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Anni")
            elif text==1:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Han")
            elif text==2:      
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Kevin")
            elif text==3:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Harry")
            elif text==4:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Jule")
            elif text==5:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Kary")
            elif text==6:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Lee")
            elif text==7:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Kim")
            elif text==8:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Park")
            elif text==9:
                text_message=tk.Label(self)
                sql="select * from doctor_info where Doctor_name=%s"
                curs.execute(sql,"Porter")
            rows=curs.fetchall()
            show_doctor=tk.Label(self)
            show_doctor.after(5000,lambda:show_doctor.destroy())
            text_message.after(5000,lambda:text_message.destroy())
            text_message.config(text="이름 진료유형 경력")
            show_doctor.config(text=rows[0])
            text_message.pack()
            show_doctor.pack()     
            


class Diease_Info(tk.Frame):    #질병에 대한 정보
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        tk.Label(self,text="질병이름",font=("bold")).pack(side="top",fill='x',pady=5)
        listbox=tk.Listbox(self)
        listbox.insert(0,"감기")
        listbox.insert(1,"골절")
        listbox.insert(2,"근육통")
        listbox.insert(3,"당뇨")
        listbox.insert(4,"암")
        listbox.insert(5,"장염")
        listbox.insert(6,"코로나")
        listbox.pack()
        tk.Button(self,text="보기",command=lambda:look_diease()).pack()
        tk.Button(self,text="초기화면",command=lambda:master.switch_frame(SelectPage)).pack()
        def look_diease():
            text=listbox.curselection()[0]
            if text==0:
                text_message=tk.Label(self)
                sql="select * from diease where diease_name=%s"
                curs.execute(sql,"감기")
            elif text==1:
                text_message=tk.Label(self)
                sql="select * from diease where diease_name=%s"
                curs.execute(sql,"골절")
            elif text==2:
                text_message=tk.Label(self)
                sql="select * from diease where diease_name=%s"
                curs.execute(sql,"근육통")
            elif text==3:
                text_message=tk.Label(self)
                sql="select * from diease where diease_name=%s"
                curs.execute(sql,"당뇨")
            elif text==4:
                text_message=tk.Label(self)
                sql="select * from diease where diease_name=%s"
                curs.execute(sql,"암")
            elif text==5:
                text_message=tk.Label(self)
                sql="select * from diease where diease_name=%s"
                curs.execute(sql,"장염")
            elif text==6:
                text_message=tk.Label(self)
                sql="select * from diease where diease_name=%s"
                curs.execute(sql,"코로나")            

            rows=curs.fetchall()
            show_doctor=tk.Label(self)
            show_doctor.after(5000,lambda:show_doctor.destroy())
            text_message.after(5000,lambda:text_message.destroy())
            text_message.config(text="질병이름  약   치료기간")
            show_doctor.config(text=rows[0])
            text_message.pack()
            show_doctor.pack() 
if __name__=="__main__":
    app=Patient_DB()
    app.title("병원 DB")
    app.mainloop()