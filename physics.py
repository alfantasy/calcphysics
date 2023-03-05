from tkinter import * 
from tkinter import ttk 
#from tkinter import messagebox 
from math import *
from tkinter.scrolledtext import ScrolledText
import time

root = Tk()
try:
    root.iconbitmap("./image/calc.ico")
except TclError:
    root.iconbitmap(None)

root.title("Калькулятор")

win = Toplevel()
win.title("Лекции")
try: 
    win.iconbitmap("./image/info.ico")
except TclError:
    root.iconbitmap(None)

win.geometry("500x600")

def get_step():
    step = Toplevel()
    step.title("Значения в степени")

    entry = StringVar()
    entry1 = StringVar()
    entry2 = StringVar()

    def math2():
        a = float(entry.get())
        b = float(entry2.get())
        c = float(entry1.get())
        var_result = a*b**c
        print(var_result)
        result = Label(step, text=str(var_result))
        result.pack(anchor=NW)
        result.after(10000,result.destroy)  
        root.clipboard_clear()
        root.clipboard_append(var_result)

    label = Label(step,text="Подпрограмма, способная возводить число в степени: 1*10⁻²³\n Первое значение: это умножаемое число. \n Второе значение: это число на которое умножают. \n Третье значение: значение степени второго числа (значения)")
    entry_en = Entry(step,textvariable=entry)
    entry_en0 = Entry(step,textvariable=entry2)
    entry_en1 = Entry(step,textvariable=entry1)
    result_button = Button(step,text="Результат",command=math2)
    label.pack()
    entry_en.pack()
    entry_en0.pack()
    entry_en1.pack()
    result_button.pack()

    step.mainloop()

def del_root():
	root.destroy()

menu_root = Menu()
menu_root.add_command(label="Закрыть", command=lambda: del_root())
menu_root.add_command(label="Значения в степени", command=lambda: get_step())
root.config(menu=menu_root) 

Lectures = ["Введение", 
            "Глава I. Механика", 
            "Глава II. Динаминка", 
            "Глава III. Импульс. Закон сохранения импульса",
            "Глава IV. Механические колебания и волны",
            "Глава V. Агрегатные состояния вещества",
            "Глава VI. Молекулярно-кинетическая теория",
            "Глава VII. Элементы термодинамики",
            "Глава VIII. Электростатика и её элементы",
            "Глава IX. Электродинамика",
            ]

Categories = [
            "Кинематика",
            "Кинематика движения по окружности",
            "Динамика",
            "Импульс",
            "Работа силы",
            "Механические колебания и волны",
            "Агрегатные состояния вещества",
            "Молекулярно-кинетическая теория",
            "Элементы термодинамики",
            "Тепловые двигатели",
            "Электростатика и её элементы",
            "Электродинамика",
]            

Formules_Dunamica = [
    "Второй закон Ньютона",
    "Плотность вещества",
    "Закон всемирного тяготения", # не выводим
    "Сила тяжести",
    "Сила упругости. Закон Гука",
    "Вес",
    "Архимедова сила",
    "Сила трения покоя",
    "Трение скольжения",
    "Жидкое трение"
]

Formules_WorkFight = [
    "Работа",
    "Работа силы упругости",
    "Работа в поле силы тяжести",
    "Мощность",
    "Кинетическая энергия",
    "Потенциальная энергия тела с высоты",
    "Потенциальная энергия тела, которое обладает деформацией",
    "Потенциальная энергия гравитационного взаимодействия"
]

Formules_MechanicCol = [
    "Период колебаний",
    "Частота колебаний",
    "Циклическая частота",
    "Длина волны",
    "Формула Гюйгенса",
    "Формула периода пружинного маятника"
]

Formules_Agregat = [
    "Относительная влажность воздуха",
    "Коэффициент поверхностного натяжения"
]

Formules_MKT = [
    "Моль (через молярную массу)",
    "Моль (через кол-во молекул)",
    "Основное уравнение МКТ",
    "Средняя кинетическая энергия",
    "Средняя квадратичная скорость",
    "Уравнение Менделеева-Клайперона"
]

Formules_TeplDvig = [
    "КПД теплового двигателя",
    "КПД идеальной тепловой машины"
]

Formules_ElekStatic = [
    "Закон Кулона",
    "Напряженность обычного заряда",
    "Напряженность точечного заряда",
    "Работа электрического поля",
    "Потенциальная энергия",
    "Потенциал",
    "Потенциал заряда в среде",
    "Напряжение",
    "Работа по перемещению заряда",
    "Заряд конденсатора",
    "Заряд конденсатора (с разностью потенциалов)",
    "Электроёмкость конденсатора",
    "Электроёмкость плоского конденсатора",
    "Энергия заряженного конденсатора",
    "Работа заряженного конденсатора (с энергией)",
    "Работа заряженного конденсатора",
]

Formules_ElekDunamic = [
    "Сила тока",
    "Объем проводника",
    "Число электронов",
    "Полный заряд",
    "Сила тока при связи с зарядом электрона",
    "Сила на заряд (при q)",
    "Сила на заряд (Второй закон Ньютона)",
    "Сила тока в металлах",
    "Сила тока в электролитах (Закон Фарадея)",
    "Зависимость сопротивления от t°",
    "Сопротивление проводника",
    "Сила тока в проводнике",
    "ЭДС"
]

Formules_ElementTermodunamic = [
    "Внутренняя энергия тела",
    "Внутренняя энергия идеального газа",
    "Работа газа в термодинамике",
    "Формула нагревания (охлаждения)",
    "Формула плавления (отвердевания)",
    "Формула парообразования (конденсанции)",
    "Формула сгорания топлива",
    "Первой закон термодинамики (с Авн)",
    "Первый закон термодинамики (с Асис)",
]

Formules_Impulus = [
    "Импульс тела",
    "Импульс силы",
    "Абсолютно упругий удар",
    "Абсолютно неупругий удар"
]

Formules_Kinematic = [
            "Уравнение движения",
            "Средняя скорость",
            "Скорость при равноускоренном движении",
            "Уравнение равноускоренного движения",
            "Проекция перемещения",
]

Formules_Kinematic_2 = [
            "Период обращения",
            "Частота",
            "Линейная скорость",
            "Угловая скорость",
            "Центростремительное ускорение",
            "Связь между линейной и угловой скоростью",
]

def widget_forget(widget):
    widget.pack_forget()

def del_f2(widget,widget1):
    widget.pack_forget()
    widget1.pack_forget()

def del_f3(widget,widget1,widget2):
    widget.pack_forget()
    widget1.pack_forget()
    widget2.pack_forget()

def del_f4(widget,widget1,widget2,widget3):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()

def wid_f(widget,widget1,widget2,widget3,widget4):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()

def wid_f6(widget,widget1,widget2,widget3,widget4,widget5):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()

def del_combobox(widget,widget1,widget2,widget3,widget4,widget5,widget6):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()
    widget6.pack_forget()    

def del_f8(widget,widget1,widget2,widget3,widget4,widget5,widget6,widget7):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()
    widget6.pack_forget()    
    widget7.pack_forget()

def wid_f9(widget,widget1,widget2,widget3,widget4,widget5,widget6,widget7,widget8):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()
    widget6.pack_forget()
    widget7.pack_forget()
    widget8.pack_forget()

def wid_f10(widget,widget1,widget2,widget3,widget4,widget5,widget6,widget7,widget8,widget9):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()
    widget6.pack_forget()
    widget7.pack_forget()
    widget8.pack_forget()
    widget9.pack_forget()

def wid_f11(widget,widget1,widget2,widget3,widget4,widget5,widget6,widget7,widget8,widget9,widget10):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()
    widget6.pack_forget()
    widget7.pack_forget()
    widget8.pack_forget()
    widget9.pack_forget()
    widget10.pack_forget()

def wid_f12(widget,widget1,widget2,widget3,widget4,widget5,widget6,widget7,widget8,widget9,widget10,widget11):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()
    widget6.pack_forget()
    widget7.pack_forget()
    widget8.pack_forget()
    widget9.pack_forget()
    widget10.pack_forget()
    widget11.pack_forget()

def wid_f13(widget,widget1,widget2,widget3,widget4,widget5,widget6,widget7,widget8,widget9,widget10,widget11,widget12):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()
    widget6.pack_forget()
    widget7.pack_forget()
    widget8.pack_forget()
    widget9.pack_forget()
    widget10.pack_forget()    
    widget11.pack_forget()
    widget12.pack_forget()

def del_f(widget,widget1,widget2,widget3,widget4,widget5,widget6,widget7,widget8,widget9,widget10,widget11,widget12,widget13,widget14,widget15,widget16,widget17):
    widget.pack_forget()
    widget2.pack_forget()
    widget1.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    widget5.pack_forget()
    widget6.pack_forget()   
    widget7.pack_forget()   
    widget8.pack_forget()    
    widget9.pack_forget()  
    widget10.pack_forget()  
    widget11.pack_forget()  
    widget12.pack_forget()  
    widget13.pack_forget()  
    widget14.pack_forget()  
    widget15.pack_forget()  
    widget16.pack_forget()  
    widget17.pack_forget()  

R = 8,314 # универсальная газовая постоянная
G = 6.67*10**-12 # гравитационная постоянная
g = 10 # ускорение свободного падения
NA = 6.022*10**23 # Число Авогадро
K = 9*10**9 # коэффициент пропорциональности
KPB = 1,38*10**-23 # постоянная Больцмана
ε = 8.85*10**-12 # диэлектрическая постоянная
e = 1.6*10**-19 # обозначение электрического заряда, значение заряда электрона в зависимости от Кл
me = 9.1*10**-31 # масса электрона, стандартного электрического заряда

messagebox = StringVar()
x_yr_en = StringVar()
x0_en = StringVar()
u_en = StringVar()
i_en = StringVar()
u0_en = StringVar()
a_en = StringVar()
t_en = StringVar()
S_en = StringVar()
S1_en = StringVar()
S2_en = StringVar()
S3_en = StringVar()
t1_en = StringVar()
t2_en = StringVar()
t3_en = StringVar()
T_en = StringVar()
N_en = StringVar()
ν_en = StringVar()
R_en = StringVar()
ω_en = StringVar()
φ_en = StringVar()
A_en = StringVar()
F_en = StringVar()
m_en = StringVar()
m1_en = StringVar()
m2_en = StringVar()
ρ_en = StringVar()
V_en = StringVar()
delx = StringVar()
k_zk = StringVar()
P_en = StringVar()
μ_en = StringVar()
k_en = StringVar()
p_en = StringVar()
p1_en = StringVar()
p11_en = StringVar()
p21_en = StringVar()
p2_en = StringVar()
v1_en = StringVar()
v11_en = StringVar()
v2_en = StringVar()
x_en = StringVar()
x1_en = StringVar()
h1_en = StringVar()
h2_en = StringVar()
q1_en = StringVar()
q2_en = StringVar()
E_en = StringVar()
l_en = StringVar()
λ_en = StringVar()
d_en = StringVar()
ε0_en = StringVar()
S_no = IntVar()
x_no = IntVar()
x0_no = IntVar()
u_no = IntVar()
t_no = IntVar()
T_no = IntVar()
N_no = IntVar()
ν_no = IntVar()
R_no = IntVar()
ω_no = IntVar()
φ_no = IntVar()
a_no = IntVar()
u0_no = IntVar()
A_no = IntVar()
F_no = IntVar()
m_no = IntVar()
ρ_no = IntVar()
V_no = IntVar()
delx_no = IntVar()
k_zk_no = IntVar()
P_no = IntVar()
μ_no = IntVar()
k_no = IntVar()
p_no = IntVar()
x1_no = IntVar()
h2_no = IntVar()
w_upn = IntVar()
w_dn = IntVar()
per = IntVar()
per0 = IntVar()
per1 = IntVar()
per2 = IntVar()
per3 = IntVar()

def rabota_pol():
  q = q1_en.get()
  e = E_en.get()
  d1 = p1_en.get()
  d2 = p2_en.get()
  var_result = float(q)*float(e)*(float(d1)-float(d2))
  q1_en.set("")
  E_en.set("")
  p1_en.set("")
  p2_en.set("")
  result = Label(root, text= "A = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def vzaim_zar_s_pol():
  q = q1_en.get()
  e = E_en.get()
  d1 = p1_en.get()
  var_result = float(q)*float(e)*float(d1)
  q1_en.set("")
  E_en.set("")
  p1_en.set("")
  result = Label(root, text= "Wp = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)  

def vzaim_toch_zar():
  q1 = q1_en.get()
  q2 = q2_en.get()
  r = R_en.get()
  var_result = float(K)*(float(q1)*float(q2)/float(r)**2)
  q1_en.set("")
  q2_en.set("")
  R_en.set("") 
  result = Label(root, text= "Wp = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def potenc():
  wp = E_en.get()
  q = q1_en.get()
  var_result = float(wp)/float(q)
  E_en.set("")
  q1_en.set("")
  result = Label(root, text= "φ = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def potenc_zar_v_srede():
  q0 = q1_en.get()
  r = R_en.get()
  var_result = float(K)*(float(q0)/float(r))
  q1_en.set("")
  R_en.set("")
  result = Label(root, text= "φ = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def napr():
  φ1 = q1_en.get()
  φ2 = q2_en.get()
  var_result = float(φ1)-float(φ2)
  q1_en.set("")
  q2_en.set("")
  result = Label(root, text= "U = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def napr2():
  a = A_en.get()
  q = q1_en.get()
  var_result = float(a)/float(q)
  a_en.set("")
  q1_en.set("")
  result = Label(root, text= "U = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def napr3():
  e = E_en.get()
  Δd = p1_en.get()
  var_result = float(e)*float(Δd)
  E_en.set("")
  p1_en.set("")
  result = Label(root, text= "U = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def rab_po_perem_zar():
  q = q1_en.get()
  φ1 = p1_en.get()
  φ2 = p2_en.get()
  var_result = float(q)*(float(φ1)-float(φ2))
  q1_en.set("")
  p1_en.set("")
  p2_en.set("")
  result = Label(root, text= "A = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def zar_condenc():
  c = A_en.get()
  u = E_en.get()
  var_result = float(c)*float(u)
  A_en.set("")
  E_en.set("")
  result = Label(root, text= "q = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def zar_condenc2():
  c = A_en.get()
  φ1 = p1_en.get()
  φ2 = p2_en.get()
  var_result = float(c)*(float(φ1)-float(φ2))
  A_en.set("")
  p1_en.set("")
  p2_en.set("")
  result = Label(root, text= "q = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)


def electroemk():
  q = q1_en.get()
  u = E_en.get()
  var_result = float(q)/float(u)
  q1_en.set("")
  E_en.set("")
  result = Label(root, text= "C = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def electroemk_plosk():
  ε0 = ε0_en.get()
  s = S_en.get()
  d = d_en.get()
  var_result = (float(ε)*float(ε0)*float(s))/float(d)
  ε0_en.set("")
  S_en.set("")
  result = Label(root, text= "C = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def energ_zar_condenc():
  q = q1_en.get()
  e = E_en.get()
  d = d_en.get()
  var_result = (float(q)*float(e)*float(d))/2
  q1_en.set("")
  E_en.set("")
  d_en.set("")
  result = Label(root, text= "W = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def energ_zar_condenc2():
  q = q1_en.get()
  u = E_en.get()
  var_result = (float(q)*float(u))/2
  q1_en.set("")
  E_en.set("")
  result = Label(root, text= "W = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def energ_zar_condenc3():
  q = q1_en.get()
  c = A_en.get()
  var_result = float(q)/(float(c)*2)
  q1_en.set("")
  A_en.set("")
  result = Label(root, text= "W = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def energ_zar_condenc4():
  c = A_en.get()
  u = E_en.get()
  var_result = (float(c)*float(u)**2)/2
  A_en.set("")
  E_en.set("")
  result = Label(root, text= "W = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def energ_zar_condenc5():
  c = A_en.get()
  e = E_en.get()
  d = d_en.get()
  var_result = (float(c)*float(e)**2*float(d)**2)/2
  A_en.set("")
  E_en.set("")
  d_en.set("")
  result = Label(root, text= "W = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def rab_zar_condenc():
  wp1 = E_en.get()
  wp2 = A_en.get()
  var_result = float(wp2)-float(wp1)
  A_en.set("")
  E_en.set("")
  result = Label(root, text= "A = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def rab_zar_condenc2():
  q = q1_en.get()
  u1 = A_en.get()
  u2 = E_en.get()
  var_result = (q*(float(u2)-float(u1)))/2
  q1_en.set("")
  A_en.set("")
  E_en.set("")
  result = Label(root, text= "A = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def sila_toka():
  Δq = q1_en.get()
  Δt = t_en.get()
  var_result = float(Δq)/float(Δt)
  q1_en.set("")
  t_en.set("")
  result = Label(root, text= "I = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def ob_provodn():
  v = V_en.get()
  Δt = t_en.get()
  s = S_en.get()
  var_result = float(v)*float(Δt)*float(s)
  V_en.set("")
  t_en.set("")
  S_en.set("")
  result = Label(root, text= "V = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def kol_electronov():
  n = N_en.get()
  v = V_en.get()
  Δt = t_en.get()
  s = S_en.get()
  var_result = float(n)*float(v)*float(Δt)*float(s)
  N_en.det("")
  V_en.set("")
  t_en.set("")
  S_en.set("")
  result = Label(root, text= "N = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def poln_zar():
  e = E_en.get()
  n = N_en.get()
  v = V_en.get()
  Δt = t_en.get()
  s = S_en.get()
  var_result = float(e)*float(n)*float(v)*float(Δt)*float(s)
  E_en.set("")
  N_en.set("")
  V_en.set("")
  t_en.set("")
  S_en.set("")
  result = Label(root, text= "q = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def sila_toka2():
  e = E_en.get()
  n = N_en.get()
  v = V_en.get()
  s = S_en.get()
  var_result = float(e)*float(n)*float(v)*float(s)
  E_en.set("")
  N_en.set("")
  V_en.set("")
  S_en.set("")
  result = Label(root, text= "I = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def sila_na_zar():
  e = E_en.get()
  q = q1_en.get()
  var_result = float(e)*float(q)
  E_en.set("")
  q1_en.set("")
  result = Label(root, text= "F = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def sila_na_zar2():
  m = m_en.get()
  Δv = V_en.get()
  t = t_en.get()
  var_result = float(m)*(float(Δv)/float(t))
  m_en.set("")
  V_en.set("")
  t_en.set("")
  result = Label(root, text= "F = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def sila_toka_metall():
  q = q1_en.get()
  n = N_en.get()
  s = S_en.get()
  v = V_en.get()
  var_result = float(q)*float(n)*float(s)*float(v)
  q1_en.set("")
  N_en.set("")
  S_en.set("")
  V_en.set("")
  result = Label(root, text= "I = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def sila_toka_electrolit():
  m = m_en.get()
  k = k_en.get()
  Δt = t_en.get()
  var_result = float(m)*(float(k)*float(Δt))
  m_en.set("")
  k_en.set("")
  t_en.set("")
  result = Label(root, text= "I = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)
  
def sopr():
  r = R_en.get()
  a = a_en.get()
  Δt = t_en.get()
  var_result = float(r)*(1+(float(a)*float(Δt)))
  R_en.set("")
  a_en.set("")
  t_en.set("")
  result = Label(root, text= "R = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def sopr_provodnika():
  ρ = ρ_en.get()
  l = l_en.get()
  s = S_en.get()
  var_result = float(ρ)*(float(l)/float(s))
  ρ_en.set("")
  l_en.set("")
  S_en.set("")
  result = Label(root, text= "R = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def sila_toka_v_provodnike():
  u = E_en.get()
  r = R_en.get()
  var_result = float(u)/float(r)
  E_en.set("")
  R_en.set("")
  result = Label(root, text= "I = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)

def eds():
  a = A_en.get()
  q = q1_en.get()
  var_result = float(a)/float(q)
  A_en.set("")
  q1_en.set("")
  result = Label(root, text= "ε = " + str(var_result))
  result.pack(anchor=NW)
  result.after(5000,result.destroy)  

def new2_a(): # второй закон Ньютона (a)
    power = F_en.get()
    m = m_en.get()
    var_result = float(power)/float(m)
    print(var_result)
    F_en.set("")
    m_en.set("")
    result = Label(root,text = " a = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def new2_m(): # второй закон Ньютона (m)
    a = a_en.get()
    power = F_en.get()
    var_result = float(power)/float(a)
    print(var_result)
    a_en.set("")
    F_en.set("")
    result = Label(root,text = " m = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def new2_F(): # второй закон Ньютона (F)
    a = a_en.get()
    m = m_en.get()
    var_result = float(a)*float(m)
    print(var_result)
    a_en.set("")
    m_en.set("")
    result = Label(root,text = " F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)    

def plot_ro(): # плотность вещества, ро
    ob = V_en.get()
    m = m_en.get()
    var_result = float(m)/float(ob)
    print(var_result)
    V_en.set("")
    m_en.set("")
    result = Label(root,text = " ρ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)   

def plot_m(): # плотность вещества (m)
    ρ = ρ_en.get()
    ob = V_en.get()
    var_result = float(ρ)*float(ob)
    print(var_result)
    ρ_en.set("")
    V_en.set("")
    result = Label(root,text = " m = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)  

def plot_V(): # плотность вещества (V)
    ρ = ρ_en.get()
    m = m_en.get()
    var_result = float(m)/float(ρ)
    print(var_result)
    ρ_en.set("")
    m_en.set("")
    result = Label(root,text = " V = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)  

def zakon_vsetg():
    m1 = m1_en.get()
    m2 = m2_en.get()
    r = R_en.get()
    var_result = (float(G)*float(m1)*float(m2))/float(r)**2
    m1_en.set("")
    m2_en.set("")
    R_en.set("")
    result = Label(root,text = " F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_tz():
    m = m_en.get()
    var_result = float(m)*float(g)
    m_en.set("")
    result = Label(root,text = " F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def zk_gyk_F():
    k = k_zk.get()
    x = delx.get()
    var_result = float(k)*float(x)
    k_zk.set("")
    delx.set("")
    result = Label(root,text=" F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def zk_gyk_delx():
    power = F_en.get()
    k = k_zk.get()
    var_result = float(power)/float(k)
    F_en.set("")
    k_zk.set("")
    result = Label(root,text=" Δx = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def zk_gyk_k():
    power = F_en.get()
    x = delx.get()
    var_result = float(power)/float(x)
    F_en.set("")
    delx.set("")
    result = Label(root,text=" k = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def weight_up_a():
    a = a_en.get()
    m = m_en.get()
    var_result = float(m)*(float(g)+float(a))
    a_en.set("")
    m_en.set("")
    result = Label(root,text=" P=N= " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.delstroy)

def weight_up_d():
    a = a_en.get()
    m = m_en.get()
    var_result = float(m)*(float(g)-float(a))
    a_en.set("")
    m_en.set("")
    result = Label(root,text=" P=N= " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.delstroy)

def arh_power():
    ρ = ρ_en.get()
    ob = V_en.get()
    var_result = float(ρ)*float(ob)*float(g)
    ρ_en.set("")
    V_en.set("")
    result = Label(root,text=" Fa = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_tr_pF():
    μ = μ_en.get()
    power_rek_op = N_en.get()
    var_result = float(μ)*float(power_rek_op)
    μ_en.set("")
    N_en.set("")
    result = Label(root,text=" F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_tr_Pμ():
    power = F_en.get()
    power_rek_op = N_en.get()
    var_result = float(power)/float(power_rek_op)
    F_en.set("")
    N_en.set("")
    result = Label(root,text=" μ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_tr_PN():
    power = F_en.get()
    μ = μ_en.get()
    var_result = float(power)/float(μ)    
    F_en.set("")
    μ_en.set("")
    result = Label(root,text=" N = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def hd_tr_F():
    k = k_en.get()
    v = V_en.get()
    var_result = float(k)*float(v)
    k_en.set("")
    V_en.set("")
    result = Label(root,text=" F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def hd_tr_v():
    k = k_en.get()
    f = F_en.get()
    var_result = float(f)/float(k)
    k_en.set("")
    F_en.set("")
    result = Label(root,text=" V = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def hd_tr_k():
    f = F_en.get()
    v = V_en.get()
    var_result = float(f)/float(v)
    F_en.set("")
    V_en.set("")
    result = Label(root,text=" k = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def hd_tr_moreV():
    k = k_en.get()
    v = V_en.get()
    var_result = float(k)*float(v)**2
    k_en.set("")
    V_en.set("")
    result = Label(root,text=" F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_tr_sk():
    μ = μ_en.get()
    m = m_en.get()
    var_result = float(g)*float(μ)*float(m)
    μ_en.set("")
    m_en.set("")
    result = Label(root,text=" F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def im_tel():
    m = m_en.get()
    v = V_en.get()
    var_result = float(m)*float(v)
    m_en.set("")
    V_en.set("")
    result = Label(root,text=" p = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def im_tel_V():
    p = p_en.get()
    m = m_en.get()
    var_result = float(p)/float(m)
    p_en.set("")
    m_en.set("")
    result = Label(root,text=" V = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def im_tel_m():
    p = p_en.get()
    v = V_en.get()
    var_result = float(p)/float(v)
    p_en.set("")
    V_en.set("")
    result = Label(root,text=" m = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def im_power():
    f = F_en.get()
    t = t_en.get()
    var_result = float(f)*float(t)
    F_en.set("")
    t_en.set("")
    result = Label(root,text=" Δp = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def im_power_f():
    p = p_en.get()
    t = t_en.get()
    var_result = float(p)/float(t)
    p_en.set("")
    t_en.set("")
    result = Label(root,text=" F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def im_power_t():
    p = p_en.get()
    f = F_en.get()
    var_result = float(p)/float(f)
    p_en.set("")
    F_en.set("")
    result = Label(root,text=" Δt = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def rule_pul():
    p1 = p1_en.get()
    p2 = p2_en.get()
    p21 = p21_en.get()
    p11 = p11_en.get()
    if float(p1) == float (p11) and float(p2) == float(p21):
        var_result = float(p1)+float(p2)
        result = Label(root,text=" p₁+p₂=p₁|+p₂| = " + str(var_result))
        result.pack(anchor=NW)
        result.after(5000,result.destroy)
    p1_en.set("")
    p2_en.set("")
    p11_en.set("")
    p21_en.set("")

def ab_ypr():
    m1 = m1_en.get()
    m2 = m2_en.get()
    v = V_en.get()
    v1 = v1_en.get()
    v2 = v2_en.get()
    v11 = v11_en.get()
    var1 = float(m1)*float(v)+float(m2)*float(v1)
    var2 = float(m1)*float(v2)+float(m2)*float(v11)
    if var1 == var2: 
        var_result = var1
        result = Label(root,text=" Абсолютно упругий удар равен " + str(var_result))
        result.pack(anchor=NW)
        result.after(5000,result.destroy)
    m1_en.set("")
    m2_en.set("")
    V_en.set("")
    v1_en.set("")
    v2_en.set("")
    v11_en.set("")
    
def ab_neypr():    
    m1 = m1_en.get()
    m2 = m2_en.get()
    v = V_en.get()
    v1 = v1_en.get()
    v2 = v2_en.get()
    var1 = float(m1)*float(v)+float(m2)*float(v1)
    var2 = (float(m1)+float(m2))*float(v2)
    if var1 == var2: 
        var_result = var1
        result = Label(root,text=" Абсолютно неупругий удар равен " + str(var_result))
        result.pack(anchor=NW)
        result.after(5000,result.destroy)
    m1_en.set("")
    m2_en.set("")
    V_en.set("")
    v1_en.set("")    
    v2_en.set("")

def work():
    f = F_en.get()
    s = S_en.get()
    cosa = a_en.get()
    var_result = float(f)*float(s)*float(cosa)   
    F_en.set("")
    S_en.set("")
    a_en.set("")
    result = Label(root,text=" A = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def work_power_ypr():
    k = k_en.get()
    x = x_en.get()
    x1 = x1_en.get()
    var_result = ((float(k)*float(x)**2)/2)-((float(k)*float(x1)**2)/2)
    k_en.set("")
    x_en.set("")
    x1_en.set("")
    result = Label(root,text=" A₁₂ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def work_power_ypr1():
    k = k_en.get()
    x = x_en.get()
    var_result = (float(k)*float(x)**2)/2
    k_en.set("")
    x_en.set("")
    result = Label(root,text=" A₁ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def work_power_tg():
    m = m_en.get()
    h1 = h1_en.get()
    h2 = h2_en.get()
    var_result = float(m)*float(g)*float(h1)-float(m)*float(g)*float(h2)
    m_en.set("")
    h1_en.set("")    
    h2_en.set("")
    result = Label(root,text=" A₁₂ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def work_power_tg1():
    m = m_en.get()
    h1 = h1_en.get()
    var_result = float(m)*float(g)*float(h1)
    m_en.set("")
    h1_en.set("")    
    result = Label(root,text=" A₁ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_N1():
    a = A_en.get()
    t = t_en.get()
    var_result = float(a)/float(t)
    A_en.set("")
    t_en.set("")
    result = Label(root,text=" N = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_N1_A():
    n = N_en.get()
    t = t_en.get()
    var_result = float(n)*float(t)
    N_en.set("")
    t_en.set("")
    result = Label(root,text=" A = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_N1_t():
    n = N_en.get()
    a = A_en.get()
    var_result = float(n)/float(a)
    N_en.set("")
    A_en.set("")
    result = Label(root,text=" t = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def power_N2():
    f = F_en.get()
    v = V_en.get()
    cosa = a_en.get()
    var_result = float(f)*float(v)*float(cosa)
    F_en.set("")
    V_en.set("")
    a_en.set("")
    result = Label(root,text=" N = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)    

def kunetic():
    m = m_en.get()
    v = V_en.get()
    var_result = float(m)*float(v)**2/2
    m_en.set("")
    V_en.set("")
    result = Label(root,text=" E = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def poten_h():
    m = m_en.get()
    h = h1_en.get()
    var_result = float(m)*float(g)*float(h)
    m_en.set("")
    h1_en.set("")
    result = Label(root,text=" E = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def poten_delx():
    k = k_en.get()
    x = x_en.get()
    var_result = float(k)*float(x)**2/2
    k_en.set("")
    x_en.set("")
    result = Label(root,text=" E = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def poten_grav():
    m = m_en.get()
    m1 = m1_en.get()
    r = R_en.get()
    var_result = float(G)*float(m)*float(m1)/float(r)
    result = Label(root,text=" E = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def mex_cylc():
    t = T_en.get()
    var_result = 2*pi/float(t)
    T_en.set()
    result = Label(root,text=" ω = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def mex_cylc_nu():
    ν = ν_en.get()
    var_result = 2*pi*float(ν)
    T_en.set()
    result = Label(root,text=" ω = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def formula_gei():
    l = l_en.get()
    var_result = 2*pi*sqrt((float(l)/float(g)))
    l_en.set("")
    result = Label(root,text=" T = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def volna():
    v = V_en.get()
    t = T_en.get()
    var_result = float(v)*float(t)
    V_en.set("")
    T_en.set("")
    result = Label(root,text=" λ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def matmain_ni():
    l = l_en.get()
    var_result = sqrt(float(g)/float(l))
    l_en.set("")
    result = Label(root,text=" ω = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def math_per():
    l = l_en.get()
    var_result = 2*pi*sqrt(float(g)/float(l))
    l_en.set("")
    result = Label(root,text=" T = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def matmain_omega():
    l = l_en.get()
    var_result = 1/2*pi*sqrt(float(g)/float(l))
    l_en.set("")
    result = Label(root,text=" ν = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def pryz_per():
    m = m_en.get()
    k = k_en.get()
    var_result = 2*pi*sqrt(float(m)/float(k))
    m_en.set("")
    k_en.set("")
    result = Label(root,text=" T = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def pryz_ni():
    m = m_en.get()
    k = k_en.get()
    var_result = 1/2*pi*sqrt(float(k)/float(m))
    m_en.set("")
    k_en.set("")
    result = Label(root,text=" ν = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def pryz_omega():
    m = m_en.get()
    k = k_en.get()
    var_result = sqrt(float(k)/float(m))
    m_en.set("")
    k_en.set("")
    result = Label(root,text=" ω = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def formula_powerfnaz():
    m = m_en.get()
    n = N_en.get()
    d = d_en.get()
    var_result = (float(m)*float(g))/(float(n)*pi*float(d))
    m_en.set("")
    N_en.set("")
    d_en.set("")
    result = Label(root,text=" ς = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def otnos_vozdyh():
    ρ = ρ_en.get()
    r = R_en.get()
    var_result = float(ρ)/float(r)*100
    ρ_en.set("")
    R_en.set("")
    result = Label(root,text=" φ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def kol_vo_1():
    m = m_en.get()
    m1 = m1_en.get()
    var_result = float(m)/float(m1)
    m_en.set("")
    m1_en.set("")
    result = Label(root,text=" ν = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def kol_vo_2():
    n = N_en.get()
    var_result = float(n)/float(NA)
    N_en.set("")
    result = Label(root,text=" ν = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def mkt_1():
    n = N_en.get()
    t = T_en.get()
    var_result = float(n)*float(KPB)*float(t)
    N_en.set("")
    T_en.set("")
    result = Label(root,text=" p = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def mkt_2():
    n = N_en.get()
    enn = E_en.get()
    var_result = 2/3*float(n)*float(enn)
    N_en.set("")
    E_en.set("")
    result = Label(root,text=" p = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def mkt_3():
    n = N_en.get()
    m = m_en.get()
    v = V_en.get()
    var_result = 1/3*(float(n)*float(m)*float(v))
    N_en.set("")
    m_en.set("")
    V_en.set("")
    result = Label(root,text=" p = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def sr_ek():
    t = T_en.get()
    var_result = 3/2*(float(KPB)*float(t))
    T_en.set("")
    result = Label(root,text=" Eк = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def sr1_v():
    r = R_en.get()
    t = T_en.get()
    m = m_en.get()
    var_result = sqrt((3*float(r)*float(t))/float(m))
    R_en.set("")
    T_en.set("")
    m_en.set("")
    result = Label(root,text=" Vкср = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def men_klap():
    ν = ν_en.get()
    r = R_en.get()
    t = T_en.get()
    var_result = float(ν)*float(r)*float(t)
    ν_en.set("")
    R_en.set("")
    T_en.set("")
    result = Label(root,text=" p*V = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000,result.destroy)

def yr_go_1():
    x0 = x0_en.get()
    u = u_en.get()
    t = t_en.get()
    var_result = float(x0)+float(u)*float(t)
    print(var_result)
    x0_en.set("")
    u_en.set("")
    t_en.set("")
    result = Label(root, text = " X = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def yr_go_x0():
    x = x_yr_en.get()
    u = u_en.get() 
    t = t_en.get()  
    var_result = float(x)-float(u)*float(t)
    print(var_result)
    x_yr_en.set("")
    u_en.set("")
    t_en.set("")
    result = Label(root, text = " X₀ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def xry_x():
    u0 = u0_en.get()
    t = t_en.get()
    a = a_en.get()
    x0 = x0_en.get()
    var_result = float(x0)+float(u0)*float(t)+(float(a)*(float(t)**2))/2
    print(var_result)
    u0_en.set("")
    x0_en.set("")
    t_en.set("")
    a_en.set("")
    result = Label(root, text = " X = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def xry_x0():
    u0 = u0_en.get()
    t = t_en.get()
    a = a_en.get()
    x = x_yr_en.get()
    var_result = float(x)-float(u0)*-float(t)-(float(a)*(float(t)**2))/2
    print(var_result)
    u0_en.set("")
    x_yr_en.set("")
    t_en.set("")
    a_en.set("")
    result = Label(root, text = " X = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)    

def xry_a():
    u0 = u0_en.get()
    t = t_en.get()
    x0 = x0_en.get()
    x = x_yr_en.get()
    var_result = -(float(x0)*2+2*float(t)*float(u0)-2*float(x))/(float(t)**2)
    print(var_result)
    u0_en.set("")
    x_yr_en.set("")
    t_en.set("")
    x0_en.set("")
    result = Label(root, text = " X = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)  

def xry_t():
    u0 = u0_en.get()
    a = a_en.get()
    x0 = x0_en.get()
    x = x_yr_en.get()
    var_result = (-float(u0)+sqrt(float(u0)**2+2*float(a)*float(x)-2*float(x0)*float(a)))/float(a)
    u0_en.set("")
    x_yr_en.set("")
    a_en.set("")
    x0_en.set("")
    print(var_result)
    result = Label(root, text = " t = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)  

def xry_u0():
    a = a_en.get()
    x0 = x0_en.get()
    x = x_yr_en.get()
    t = t_en.get()
    var_result = -(float(x0)*2+float(a)*float(t)**2-2*float(x))/(2*float(t))
    print(var_result)
    t_en.set("")
    x_yr_en.set("")
    a_en.set("")
    x0_en.set("")
    result = Label(root, text = " u₀ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)  

def fif_ux():
    u0 = u0_en.get()
    t = t_en.get()
    a = a_en.get()
    var_result = float(u0)+float(a)*float(t)
    print(var_result)
    t_en.set("")
    a_en.set("")
    u0_en.set("")
    result = Label(root, text = " Uₓ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def fif_a():
    u = u_en.get()
    t = t_en.get()
    u0 = u0_en.get()
    var_result = (float(u)-float(u0))/float(t) 
    print(var_result)
    u0_en.set("")
    u_en.set("")
    t_en.set("")
    result = Label(root,text=" a = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def fif_t():
    u = u_en.get()
    a = a_en.get()
    u0 = u0_en.get()
    var_result = (float(u)-float(u0))/float(a)
    print(var_result)
    x0_en.set("")
    u_en.set("")
    a_en.set("")
    result = Label(root,text=" t = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def fif_u0():
    u = u_en.get()
    a = a_en.get()
    t = t_en.get()
    var_result = float(u) - float(a)*float(t)
    print(var_result)
    a_en.set("")
    u_en.set("")
    t_en.set("")
    result = Label(root,text=" U₀ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)       

def yr_go_Xu():
    x = x_yr_en.get()
    t = t_en.get()
    x0 = x0_en.get()
    var_result=(float(x)-float(x0))/float(t)
    print(var_result)
    x_yr_en.set("")
    x0_en.set("")
    t_en.set("")
    result = Label(root,text=" U = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def sry_S():
    u0 = u0_en.get()
    t = t_en.get()
    a = a_en.get()
    var_result = float(u0)+float(a)*float(t)
    print(var_result)
    t_en.set("")
    a_en.set("")
    u0_en.set("")
    result = Label(root, text = " Sₓ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def sry_a():
    s = S_en.get()
    t = t_en.get()
    u0 = u0_en.get()
    var_result = (float(s)-float(u0))/float(t) 
    print(var_result)
    u0_en.set("")
    S_en.set("")
    t_en.set("")
    result = Label(root,text=" a = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def sry_t():
    s = S_en.get()
    a = a_en.get()
    u0 = u0_en.get()
    var_result = (float(s)-float(u0))/float(a)
    print(var_result)
    x0_en.set("")
    S_en.set("")
    a_en.set("")
    result = Label(root,text=" t = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def sry_u0():
    s = S_en.get()
    a = a_en.get()
    t = t_en.get()
    var_result = float(s) - float(a)*float(t)
    print(var_result)
    a_en.set("")
    S_en.set("")
    t_en.set("")
    result = Label(root,text=" U₀ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)          

def k_obr_T():
    t = t_en.get()
    n = N_en.get()
    var_result = float(t)/float(n)
    print(var_result)
    t_en.set("")
    N_en.set("")
    result = Label(root,text=" T = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)    

def k_obr_t():
    per = T_en.get()
    n = N_en.get()
    var_result = float(per)*float(n)
    print(var_result)
    T_en.set("")
    N_en.set("")
    result = Label(root,text=" t = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)        

def k_obr_N():
    per = T_en.get()
    t = t_en.get()
    var_result = float(t)/float(per)
    print(var_result)
    T_en.set("")
    t_en.set("")
    result = Label(root,text=" N = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)          

def chas_ν():
    t = t_en.get()
    obrn = N_en.get()
    var_result = float(obrn)/float(t)
    print(var_result)
    t_en.set("")
    N_en.set("")
    result = Label(root,text=" ν = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)  

def chas_t():
    ν = ν_en.get()
    obrn = N_en.get()
    var_result = float(obrn)/float(ν)
    print(var_result)
    ν_en.set("")
    N_en.set("")
    result = Label(root,text=" t = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)  

def chas_N():
    ν = ν_en.get()
    t = t_en.get()
    var_result = float(t)*float(ν)
    print(var_result)
    ν_en.set("")
    t_en.set("")
    result = Label(root,text=" N = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)      

def ygl_u():
    φ = φ_en.get()
    t = t_en.get()
    var_result = float(φ)/float(t)
    print(var_result)
    φ_en.set("")
    t_en.set("")
    result = Label(root,text=" ω = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)  

def ygl_t():
    ω = ω_en.get()
    φ = φ_en.get()
    var_result = float(φ)/float(ω)
    print(var_result)
    φ_en.set("")
    ω_en.set("")
    result = Label(root,text=" ▲t = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)         

def ygl_f():
    ω = ω_en.get()
    t = t_en.get()
    var_result = float(t)*float(ω)
    print(var_result)
    ω_en.set("")
    t_en.set("")
    result = Label(root,text=" ▲φ = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)            

def fif_u():
    t = t_en.get()
    if t: 
        t = float(t)
    else: 
        t = 0 
    t1 = t1_en.get()
    if t1: 
        t1 = float(t1)
    else: 
        t1 = 0 
    t2 = t2_en.get()
    if t2: 
        t2 = float(t2)
    else: 
        t2 = 0 
    t3 = t3_en.get()
    if t3: 
        t3 = float(t3)
    else: 
        t3 = 0 
    s = S_en.get()
    if s: 
        s = float(s)
    else: 
        s = 0 
    s1 = S1_en.get()
    if s1: 
        s1 = float(s1)
    else: 
        s1 = 0 
    s2 = S2_en.get()
    if s2: 
        s2 = float(s2)
    else: 
        s2 = 0 
    s3 = S3_en.get()
    if s3: 
        s3 = float(s3)
    else: 
        s3 = 0 
    var_result = (s1+s2+s3+s)/(t+t1+t2+t3)
    print(var_result)
    result = Label(root,text=" Uср = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def liu_u():
    r = R_en.get()
    per = T_en.get()
    var_result = (float(r)*2*pi)/float(per)
    print(var_result)
    R_en.set("")
    T_en.set("")
    result = Label(root,text=" U = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def liu_T():
    r = R_en.get()
    u = u_en.get()
    var_result = (float(r)*2*pi)/float(u)
    print(var_result)
    R_en.set("")
    u_en.set("")
    result = Label(root,text=" T = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)    

def liu_R():
    per = T_en.get()
    u = u_en.get()
    var_result = (float(u)*float(per))/2*pi
    print(var_result)
    T_en.set("")
    u_en.set("")
    result = Label(root,text=" R = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)        

def asr_a():
    u = u_en.get()
    r = R_en.get()
    var_result = float(u)**2/float(r)
    u_en.set("")
    R_en.set("")
    result = Label(root,text=" a-цр = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)   

def asr_u():
    a = a_en.get()
    r = R_en.get()
    var_result = sqrt(float(r)*float(a))
    a_en.set("")
    R_en.set("")
    result = Label(root,text=" U = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)      

def asr_r():
    u = u_en.get()
    a = a_en.get()
    var_result = float(u)**2/float(a)
    u_en.set("")
    a_en.set("")
    result = Label(root,text=" R = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def sv_lr_u():
    r = R_en.get()
    ω = ω_en.get()
    var_result = float(ω)*float(r)
    print(var_result)
    R_en.set("")
    ω_en.set("")
    result = Label(root,text=" U = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def sv_lr_ω():
    r = R_en.get()
    u = u_en.get()
    var_result = float(u)/float(r)
    print(var_result)
    u_en.set("")
    R_en.set("")
    result = Label(root,text=" ω = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)    

def sv_lr_r():
    u = u_en.get()
    ω = ω_en.get()
    var_result = float(u)/float(ω)
    print(var_result)
    ω_en.set("")
    u_en.set("")
    result = Label(root,text=" U = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)    

def inside_energy():
    u = u_en.get()
    a = A_en.get()
    var_result = float(u)+float(a)
    u_en.set("")
    A_en.set("")
    result = Label(root,text=" U = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def in_energy_gaz():
    i = i_en.get()
    ν = ν_en.get()
    r = R_en.get()
    t = T_en.get()
    var_result = float(i)*float(ν)*float(r)*float(t)/2
    i_en.set("")
    ν_en.set("")
    R_en.set("")
    T_en.set("")
    result = Label(root,text=" U = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)
    
def work_gaz():
    p = p_en.get()
    v = V_en.get()
    var_result = float(p)*float(v)
    p_en.set("")
    V_en.set("")
    result = Label(root,text=" A = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def kpd_1():
    a = A_en.get()
    qn = u_en.get()
    var_result = float(a)/float(qn)*100
    A_en.set("")
    u_en.set("")
    result = Label(root,text=" η = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def kpd_2():
    tx = T_en.get()
    tn = t_en.get()
    var_result = (float(tn)-float(tx))/float(tn)*100
    T_en.set("")
    t_en.set("")
    result = Label(root,text=" η = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def formula_nagrev():
    c = a_en.get()
    m = m_en.get()
    t = t_en.get()
    var_result = float(c)*float(m)*float(t)
    a_en.set("")
    m_en.set("")
    t_en.set("")
    result = Label(root,text=" Q = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def formula_obplav():
    l = l_en.get()
    m = m_en.get()
    var_result = float(m)*float(l)
    l_en.set("")
    m_en.set("")
    result = Label(root,text=" Q = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def formula_sgor():
    q1 = q1_en.get()
    m = m_en.get()
    var_result = float(m)*float(q1)
    q1_en.set("")
    m_en.set("")
    result = Label(root,text=" Q = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def per_zk_termo():
    q = q1_en.get()
    a = A_en.get()
    var_result = float(q)+float(a)
    q1_en.set("")
    A_en.set("")
    result = Label(root,text=" U = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def per_zk_termo1():
    u = u_en.get()
    a = A_en.get()
    var_result = float(u)+float(a)
    u_en.set("")
    A_en.set("")
    result = Label(root,text=" Q = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def zk_kylon():
    q1 = q1_en.get()
    q2 = q2_en.get()
    r = R_en.get()
    var_result = (float(K)*float(q1)*float(q2))/(float(r)**2)
    q1_en.set("")
    q2_en.set("")
    R_en.set("")
    result = Label(root,text=" F = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def naprizob():
    f = F_en.get()
    q1 = q1_en.get()
    var_result = float(f)/float(q1)
    F_en.set("")
    q1_en.set("")
    result = Label(root,text=" E = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def napriztz():
    r = R_en.get()
    q1 = q1_en.get()
    var_result = float(K)*float(q1)/(float(r)**2)
    R_en.set("")
    q1_en.set("")
    result = Label(root,text=" E = " + str(var_result))
    result.pack(anchor=NW)
    result.after(5000, result.destroy)

def selectedbox_cat(event):
    selection = combobox_cat.get()
    if selection == "Кинематика":
        def selected_box_kinematic(event):
            selection2 = combobox_kinematic.get()
            if selection2 == "Уравнение движения":
                def checkbutton_yr():
                    if x_no.get() == 1 and u_no.get() == 0 and t_no.get() == 0 and x0_no.get() == 0:
                        var1_label = Label(root,text="Начальная координата (X₀):")
                        var1_label.pack(anchor=NW)
                        var1_entry = Entry(root,textvariable=x0_en)
                        var1_entry.pack(anchor=NW)
                        var2_label = Label(root,text="Скорость (U):")
                        var2_label.pack(anchor=NW)
                        var2_entry = Entry(root,textvariable=u_en)
                        var2_entry.pack(anchor=NW)
                        var3_label = Label(root,text="Время (t):")
                        var3_label.pack(anchor=NW)
                        var3_entry = Entry(root,textvariable=t_en)
                        var3_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=yr_go_1)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,var1_entry,var1_label,var2_entry,var2_label,var3_label,var3_entry))
                        root.config(menu=main_menu)
                    if x_no.get() == 0 and u_no.get() == 0 and t_no.get() == 0 and x0_no.get() == 1:
                        x_yr_en_label = Label(root,text="Координата движения (X):")
                        x_yr_en_label.pack(anchor=NW)
                        x_yr_en_entry = Entry(root,textvariable=x_yr_en)
                        x_yr_en_entry.pack(anchor=NW)
                        var2_label = Label(root,text="Скорость (U):")
                        var2_label.pack(anchor=NW)
                        var2_entry = Entry(root,textvariable=u_en)
                        var2_entry.pack(anchor=NW)
                        var3_label = Label(root,text="Время (t):")
                        var3_label.pack(anchor=NW)
                        var3_entry = Entry(root,textvariable=t_en)
                        var3_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=yr_go_x0)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,x_yr_en_entry,x_yr_en_label,var2_entry,var2_label,var3_label,var3_entry))
                        root.config(menu=main_menu)
                    if x_no.get() == 0 and u_no.get() == 1 and t_no.get() == 0 and x0_no.get() == 0:
                        x_yr_en_label = Label(root,text="Координата движения (X):")
                        x_yr_en_label.pack(anchor=NW)
                        x_yr_en_entry = Entry(root,textvariable=x_yr_en)
                        x_yr_en_entry.pack(anchor=NW)
                        var1_label = Label(root,text="Начальная координата (X₀):")
                        var1_label.pack(anchor=NW)
                        var1_entry = Entry(root,textvariable=x0_en)
                        var1_entry.pack(anchor=NW)
                        var3_label = Label(root,text="Время (t):")
                        var3_label.pack(anchor=NW)
                        var3_entry = Entry(root,textvariable=t_en)
                        var3_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=yr_go_Xu)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,x_yr_en_entry,x_yr_en_label,var1_entry,var1_label,var3_label,var3_entry))
                        root.config(menu=main_menu)
                    if x_no.get() == 0 and x0_no.get() == 0 and t_no.get() == 0 and u_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: wid_f(combobox_kinematic,x_check,x0_check,u_check,t_check))
                        root.config(menu=main_menu)
                x_check = ttk.Checkbutton(text="Координата неизвестна",variable=x_no,command=checkbutton_yr)
                x_check.pack(anchor=NW)
                x0_check = ttk.Checkbutton(text="Начальная координата неизвестна",variable=x0_no,command=checkbutton_yr)
                x0_check.pack(anchor=NW)
                u_check = ttk.Checkbutton(text="Скорость неизвестна",variable=u_no,command=checkbutton_yr)
                u_check.pack(anchor=NW)
                t_check = ttk.Checkbutton(text="Время неизвестно", variable=t_no,command=checkbutton_yr)
                t_check.pack(anchor=NW)
                print("x=x0+U*t")
            if selection2 == "Средняя скорость":
                print("Usr=(S1+S2+S3+SN)/t1+t2+t3+tN)")   
                S_label = Label(root,text="Первое перемещение (S₁):")
                S_label.pack(anchor=NW)
                S_entry = Entry(root,textvariable=S_en)
                S_entry.pack(anchor=NW)
                S1_label = Label(root,text="Второе перемещение (S₂):")
                S1_label.pack(anchor=NW)
                S1_entry = Entry(root,textvariable=S1_en)
                S1_entry.pack(anchor=NW)
                S2_label = Label(root,text="Третье перемещение (S₃):")
                S2_label.pack(anchor=NW)
                S2_entry = Entry(root,textvariable=S2_en)
                S2_entry.pack(anchor=NW)
                S3_label = Label(root,text="Четвертое перемещение (S₄):")
                S3_label.pack(anchor=NW)
                S3_entry = Entry(root,textvariable=S3_en)
                S3_entry.pack(anchor=NW)
                t_label = Label(root,text="Первое время (t₁):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                t1_label = Label(root,text="Второе время (t₂):")
                t1_label.pack(anchor=NW)
                t1_entry = Entry(root,textvariable=t1_en)
                t1_entry.pack(anchor=NW)
                t2_label = Label(root,text="Третье время (t₃):")
                t2_label.pack(anchor=NW)
                t2_entry = Entry(root,textvariable=t2_en)
                t2_entry.pack(anchor=NW)
                t3_label = Label(root,text="Четвертое время (t₄):")
                t3_label.pack(anchor=NW)
                t3_entry = Entry(root,textvariable=t3_en)
                t3_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=fif_u)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формул", command=lambda: del_f(combobox_kinematic,t1_label,t2_label,t3_label,S_label,S1_label,S2_label,t_label,S3_label,t1_entry,t2_entry,t3_entry,S_entry,S1_entry,S2_entry,t_entry,S3_entry,result_button))
                root.config(menu=main_menu)
            if selection2 == "Скорость при равноускоренном движении":
                print("Ux=U0x+ax*t")
                def checkbutton_Ury():
                    if u_no.get() == 1 and u0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 0:
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=fif_ux)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,u0_label,u0_entry,t_label,t_entry,a_entry,a_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 0 and u0_no.get() == 1 and t_no.get() == 0 and a_no.get() == 0:
                        ux_label = Label(root,text="Скорость (Uₓ):")
                        ux_label.pack(anchor=NW)
                        ux_entry = Entry(root,textvariable=u_en)
                        ux_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=fif_u0)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,ux_label,ux_entry,t_label,t_entry,a_entry,a_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 0 and u0_no.get() == 0 and t_no.get() == 1 and a_no.get() == 0:
                        ux_label = Label(root,text="Скорость (Uₓ):")
                        ux_label.pack(anchor=NW)
                        ux_entry = Entry(root,textvariable=u_en)
                        ux_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=fif_t)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,u0_label,u0_entry,ux_label,ux_entry,a_entry,a_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 0 and u0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 1:
                        ux_label = Label(root,text="Скорость (Uₓ):")
                        ux_label.pack(anchor=NW)
                        ux_entry = Entry(root,textvariable=u_en)
                        ux_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=fif_a)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,u0_label,u0_entry,t_label,t_entry,ux_entry,ux_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 0 and u0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: wid_f(combobox_kinematic,a_check,u0_check,u_check,t_check))
                        root.config(menu=main_menu)
                u_check = ttk.Checkbutton(text="Скорость неизвестна",variable=u_no,command=checkbutton_Ury)
                u_check.pack(anchor=NW)
                t_check = ttk.Checkbutton(text="Время неизвестно", variable=t_no,command=checkbutton_Ury)
                t_check.pack(anchor=NW)
                a_check = ttk.Checkbutton(text="Ускорение неизвестно", variable=a_no,command=checkbutton_Ury)
                a_check.pack(anchor=NW)
                u0_check = ttk.Checkbutton(text="Начальная скорость неизвестна", variable=u0_no,command=checkbutton_Ury)
                u0_check.pack(anchor=NW)
            if selection2 == "Уравнение равноускоренного движения":
                print("X=X0+U0x*t+(axt^2)/2")
                def checkbutton_Xry():
                    if x_no.get() == 1 and x0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 0 and u0_no.get() == 0:
                        var1_label = Label(root,text="Начальная координата (X₀):")
                        var1_label.pack(anchor=NW)
                        var1_entry = Entry(root,textvariable=x0_en)
                        var1_entry.pack(anchor=NW)
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=xry_x)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f9(result_button,u0_label,u0_entry,t_label,t_entry,a_entry,a_label,var1_entry,var1_label))
                        root.config(menu=main_menu)
                    if x_no.get() == 0 and x0_no.get() == 1 and t_no.get() == 0 and a_no.get() == 0 and u0_no.get() == 0:
                        x_yr_label = Label(root,text="Координата движения (X):")
                        x_yr_label.pack(anchor=NW)
                        x_yr_entry = Entry(root,textvariable=x_yr_en)
                        x_yr_entry.pack(anchor=NW)
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=xry_x0)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f9(result_button,u0_label,u0_entry,t_label,t_entry,a_entry,a_label,x_yr_entry,x_yr_label))
                        root.config(menu=main_menu)
                    if x_no.get() == 0 and x0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 1 and u0_no.get() == 0:
                        x_yr_label = Label(root,text="Координата движения (X):")
                        x_yr_label.pack(anchor=NW)
                        x_yr_entry = Entry(root,textvariable=x_yr_en)
                        x_yr_entry.pack(anchor=NW)
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        var1_label = Label(root,text="Начальная координата (X₀):")
                        var1_label.pack(anchor=NW)
                        var1_entry = Entry(root,textvariable=x0_en)
                        var1_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=xry_a)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f9(result_button,u0_label,u0_entry,t_label,t_entry,var1_entry,var1_label,x_yr_entry,x_yr_label))
                        root.config(menu=main_menu)
                    if x_no.get() == 0 and x0_no.get() == 0 and t_no.get() == 1 and a_no.get() == 0 and u0_no.get() == 0:
                        x_yr_label = Label(root,text="Координата движения (X):")
                        x_yr_label.pack(anchor=NW)
                        x_yr_entry = Entry(root,textvariable=x_yr_en)
                        x_yr_entry.pack(anchor=NW)
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        var1_label = Label(root,text="Начальная координата (X₀):")
                        var1_label.pack(anchor=NW)
                        var1_entry = Entry(root,textvariable=x0_en)
                        var1_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=xry_t)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f9(result_button,u0_label,u0_entry,a_label,a_entry,var1_entry,var1_label,x_yr_entry,x_yr_label))
                        root.config(menu=main_menu)
                    if x_no.get() == 0 and x0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 0 and u0_no.get() == 1:
                        x_yr_label = Label(root,text="Координата движения (X):")
                        x_yr_label.pack(anchor=NW)
                        x_yr_entry = Entry(root,textvariable=x_yr_en)
                        x_yr_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        var1_label = Label(root,text="Начальная координата (X₀):")
                        var1_label.pack(anchor=NW)
                        var1_entry = Entry(root,textvariable=x0_en)
                        var1_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=xry_u0)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f9(result_button,t_label,t_entry,a_label,a_entry,var1_entry,var1_label,x_yr_entry,x_yr_label))
                        root.config(menu=main_menu)                        
                    if x_no.get() == 0 and x0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 0 and u0_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: wid_f6(combobox_kinematic,x_check,u0_check,a_check,t_check,x0_check))
                        root.config(menu=main_menu)
                x_check = ttk.Checkbutton(text="Координата неизвестна",variable=x_no,command=checkbutton_Xry)
                x_check.pack(anchor=NW)
                x0_check = ttk.Checkbutton(text="Начальная координата неизвестна",variable=x0_no,command=checkbutton_Xry)
                x0_check.pack(anchor=NW)
                t_check = ttk.Checkbutton(text="Время неизвестно", variable=t_no,command=checkbutton_Xry)
                t_check.pack(anchor=NW)
                a_check = ttk.Checkbutton(text="Ускорение неизвестно", variable=a_no,command=checkbutton_Xry)
                a_check.pack(anchor=NW)
                u0_check = ttk.Checkbutton(text="Начальная скорость неизвестна", variable=u0_no,command=checkbutton_Xry)
                u0_check.pack(anchor=NW)
            if selection2 == "Проекция перемещения":
                print("Sx=U0x+ax*t")
                def checkbutton_Sry():
                    if S_no.get() == 1 and u0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 0:
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=sry_S)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,u0_label,u0_entry,t_label,t_entry,a_entry,a_label))
                        root.config(menu=main_menu)
                    if S_no.get() == 0 and u0_no.get() == 1 and t_no.get() == 0 and a_no.get() == 0:
                        s_label = Label(root,text="Проекция перемещения (Uₓ):")
                        s_label.pack(anchor=NW)
                        s_entry = Entry(root,textvariable=u_en)
                        s_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=sry_u0)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,s_label,s_entry,t_label,t_entry,a_entry,a_label))
                        root.config(menu=main_menu)
                    if S_no.get() == 0 and u0_no.get() == 0 and t_no.get() == 1 and a_no.get() == 0:
                        s_label = Label(root,text="Проекция перемещения (Uₓ):")
                        s_label.pack(anchor=NW)
                        s_entry = Entry(root,textvariable=u_en)
                        s_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=sry_t)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,u0_label,u0_entry,s_label,s_entry,a_entry,a_label))
                        root.config(menu=main_menu)
                    if S_no.get() == 0 and u0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 1:
                        s_label = Label(root,text="Проекция перемещения (Uₓ):")
                        s_label.pack(anchor=NW)
                        s_entry = Entry(root,textvariable=u_en)
                        s_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        u0_label = Label(root,text="Начальная скорость (U₀):")
                        u0_label.pack(anchor=NW)
                        u0_entry = Entry(root,textvariable=u0_en)
                        u0_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=sry_a)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,u0_label,u0_entry,t_label,t_entry,s_entry,s_label))
                        root.config(menu=main_menu)
                    if S_no.get() == 0 and u0_no.get() == 0 and t_no.get() == 0 and a_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: wid_f(combobox_kinematic,a_check,u0_check,s_check,t_check))
                        root.config(menu=main_menu)
                s_check = ttk.Checkbutton(text="Проекция перемещения неизвестна",variable=S_no,command=checkbutton_Sry)
                s_check.pack(anchor=NW)
                t_check = ttk.Checkbutton(text="Время неизвестно", variable=t_no,command=checkbutton_Sry)
                t_check.pack(anchor=NW)
                a_check = ttk.Checkbutton(text="Ускорение неизвестно", variable=a_no,command=checkbutton_Sry)
                a_check.pack(anchor=NW)
                u0_check = ttk.Checkbutton(text="Начальная скорость неизвестна", variable=u0_no,command=checkbutton_Sry)
                u0_check.pack(anchor=NW)                
        combobox_kinematic = ttk.Combobox(root, values=Formules_Kinematic, state="readonly",width="45")
        combobox_kinematic.pack(anchor=NW)
        combobox_kinematic.bind("<<ComboboxSelected>>", selected_box_kinematic)
    if selection == "Кинематика движения по окружности":
        def selected_box_kinematic_2(event):
            selection3 = combobox_kinematic_2.get()
            if selection3 == "Период обращения":
                print("T=t/N")
                def checkbutton_tobr():
                    if T_no.get() == 1 and t_no.get() == 0 and N_no.get() == 0:
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        N_label = Label(root,text="Число совершенных оборотов (N):")
                        N_label.pack(anchor=NW)
                        N_entry = Entry(root,textvariable=N_en)
                        N_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=k_obr_T)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,t_label,t_entry,N_entry,N_label))
                        root.config(menu=main_menu)
                    if T_no.get() == 0 and t_no.get() == 1 and N_no.get() == 0:
                        T_label = Label(root,text="Период обращения (T):")
                        T_label.pack(anchor=NW)
                        T_entry = Entry(root,textvariable=T_en)
                        T_entry.pack(anchor=NW)
                        N_label = Label(root,text="Число совершенных оборотов (N):")
                        N_label.pack(anchor=NW)
                        N_entry = Entry(root,textvariable=N_en)
                        N_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=k_obr_t)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,T_label,T_entry,N_entry,N_label))
                        root.config(menu=main_menu)
                    if T_no.get() == 0 and t_no.get() == 0 and N_no.get() == 1:
                        T_label = Label(root,text="Период обращения (T):")
                        T_label.pack(anchor=NW)
                        T_entry = Entry(root,textvariable=T_en)
                        T_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=k_obr_N)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,T_label,T_entry,t_entry,t_label))
                        root.config(menu=main_menu)
                    if T_no.get() == 0 and t_no.get() == 0 and N_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_kinematic_2,T_check,N_check,t_check))
                        root.config(menu=main_menu)
                T_check = ttk.Checkbutton(text="Период неизвестен", variable=T_no,command=checkbutton_tobr)
                T_check.pack(anchor=NW)
                t_check = ttk.Checkbutton(text="Время неизвестно", variable=t_no,command=checkbutton_tobr)
                t_check.pack(anchor=NW)
                N_check = ttk.Checkbutton(text="Число совершенных оборотов", variable=N_no,command=checkbutton_tobr)
                N_check.pack(anchor=NW)
            if selection3 == "Частота":
                print("ν=N/t")
                def checkbutton_chas():
                    if ν_no.get() == 1 and t_no.get() == 0 and N_no.get() == 0: 
                        N_label = Label(root,text="Число совершенных оборотов (N):")
                        N_label.pack(anchor=NW)
                        N_entry = Entry(root,textvariable=N_en)
                        N_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=chas_ν)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,N_label,N_entry,t_entry,t_label))
                        root.config(menu=main_menu)
                    if ν_no.get() == 0 and t_no.get() == 1 and N_no.get() == 0: 
                        N_label = Label(root,text="Число совершенных оборотов (N):")
                        N_label.pack(anchor=NW)
                        N_entry = Entry(root,textvariable=N_en)
                        N_entry.pack(anchor=NW)
                        ν_label = Label(root,text="Частота (ν):")
                        ν_label.pack(anchor=NW)
                        ν_entry = Entry(root,textvariable=ν_en)
                        ν_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=chas_t)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,N_label,N_entry,ν_entry,ν_label))
                        root.config(menu=main_menu)
                    if ν_no.get() == 0 and t_no.get() == 0 and N_no.get() == 1: 
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        ν_label = Label(root,text="Частота (ν):")
                        ν_label.pack(anchor=NW)
                        ν_entry = Entry(root,textvariable=ν_en)
                        ν_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=chas_N)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,t_label,t_entry,ν_entry,ν_label))
                        root.config(menu=main_menu)
                    if ν_no.get() == 0 and t_no.get() == 0 and N_no.get() == 0: 
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_kinematic_2,t_check,N_check,ν_check))
                        root.config(menu=main_menu)
                ν_check = ttk.Checkbutton(text="Частота неизвестна", variable=ν_no,command=checkbutton_chas)
                ν_check.pack(anchor=NW)
                t_check = ttk.Checkbutton(text="Время неизвестно", variable=t_no,command=checkbutton_chas)
                t_check.pack(anchor=NW)
                N_check = ttk.Checkbutton(text="Число совершенных оборотов", variable=N_no,command=checkbutton_chas)
                N_check.pack(anchor=NW)
            if selection3 == "Линейная скорость":
                print("U=(2πR)/T или U=2πRν")
                def checkbutton_liu():
                    if u_no.get() == 1 and R_no.get() == 0 and T_no.get() == 0:
                        r_label = Label(root,text="Радиус (r):")
                        r_label.pack(anchor=NW)
                        r_entry = Entry(root,textvariable=R_en)
                        r_entry.pack(anchor=NW)
                        T_label = Label(root,text="Период обращения (T):")
                        T_label.pack(anchor=NW)
                        T_entry = Entry(root,textvariable=T_en)
                        T_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=liu_u)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,T_label,T_entry,r_entry,r_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 0 and R_no.get() == 1 and T_no.get() == 0:
                        ux_label = Label(root,text="Линейная скорость (U):")
                        ux_label.pack(anchor=NW)
                        ux_entry = Entry(root,textvariable=u_en)
                        ux_entry.pack(anchor=NW)
                        T_label = Label(root,text="Период обращения (T):")
                        T_label.pack(anchor=NW)
                        T_entry = Entry(root,textvariable=T_en)
                        T_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=liu_R)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,T_label,T_entry,ux_entry,ux_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 0 and R_no.get() == 0 and T_no.get() == 1:
                        ux_label = Label(root,text="Линейная скорость (U):")
                        ux_label.pack(anchor=NW)
                        ux_entry = Entry(root,textvariable=u_en)
                        ux_entry.pack(anchor=NW)
                        r_label = Label(root,text="Радиус (r):")
                        r_label.pack(anchor=NW)
                        r_entry = Entry(root,textvariable=R_en)
                        r_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=liu_T)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,r_label,r_entry,ux_entry,ux_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 0 and R_no.get() == 0 and T_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_kinematic_2,u_check,r_check,T_check))
                        root.config(menu=main_menu)
                u_check = ttk.Checkbutton(text="Линейная скорость неизвестна",variable=u_no,command=checkbutton_liu)
                u_check.pack(anchor=NW)
                r_check = ttk.Checkbutton(text="Радиус неизвестен",variable=R_no,command=checkbutton_liu)
                r_check.pack(anchor=NW)
                T_check = ttk.Checkbutton(text="Период неизвестен",variable=T_no,command=checkbutton_liu)
                T_check.pack(anchor=NW)
            if selection3 == "Угловая скорость":
                print("ω=δφ/δt")
                def checkbutton_uω(): 
                    if ω_no.get() == 1 and φ_no.get() == 0 and t_no.get() == 0:
                        φ_label = Label(root,text="Угол поворота радиус-вектора (▲φ):")
                        φ_label.pack(anchor=NW)
                        φ_entry = Entry(root,textvariable=φ_en)
                        φ_entry.pack(anchor=NW)
                        t_label = Label(root,text="Промежуток времени (▲t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=ygl_u)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,t_label,t_entry,φ_entry,φ_label))
                        root.config(menu=main_menu)
                    if ω_no.get() == 0 and φ_no.get() == 1 and t_no.get() == 0:
                        ω_label = Label(root,text="Угловая скорость (ω):")
                        ω_label.pack(anchor=NW)
                        ω_entry = Entry(root,textvariable=ω_en)
                        ω_entry.pack(anchor=NW)
                        t_label = Label(root,text="Промежуток времени (▲t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=ygl_f)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,ω_label,ω_entry,t_entry,t_label))
                        root.config(menu=main_menu)
                    if ω_no.get() == 0 and φ_no.get() == 0 and t_no.get() == 1:
                        ω_label = Label(root,text="Угловая скорость (ω):")
                        ω_label.pack(anchor=NW)
                        ω_entry = Entry(root,textvariable=ω_en)
                        ω_entry.pack(anchor=NW)
                        φ_label = Label(root,text="Угол поворота радиус-вектора (▲φ):")
                        φ_label.pack(anchor=NW)
                        φ_entry = Entry(root,textvariable=φ_en)
                        φ_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=ygl_t)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,ω_label,ω_entry,φ_entry,φ_label))
                        root.config(menu=main_menu)
                    if ω_no.get() == 0 and φ_no.get() == 0 and t_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_kinematic_2,ω_check,δφ_check,δt_check))
                        root.config(menu=main_menu)
                ω_check = ttk.Checkbutton(text="Угловая скорость неизвестна",variable=ω_no,command=checkbutton_uω)
                ω_check.pack(anchor=NW)
                δφ_check = ttk.Checkbutton(text="Угол поворота радиус-вектора неизвестен",variable=φ_no,command=checkbutton_uω)
                δφ_check.pack(anchor=NW)
                δt_check = ttk.Checkbutton(text="Промежуток времени неизвестен",variable=t_no,command=checkbutton_uω)
                δt_check.pack(anchor=NW)
            if selection3 == "Центростремительное ускорение":
                print("а-цр = U^2/R")
                def checkbutton_asr():
                    if u_no.get() == 0 and R_no.get() == 0 and a_no.get() == 1: 
                        r_label = Label(root,text="Радиус (R):")
                        r_label.pack(anchor=NW)
                        r_entry = Entry(root,textvariable=R_en)
                        r_entry.pack(anchor=NW)
                        u_label = Label(root,text="Скорость (U):")
                        u_label.pack(anchor=NW)
                        u_entry = Entry(root,textvariable=u_en)
                        u_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=asr_a)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,u_label,u_entry,r_entry,r_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 0 and R_no.get() == 1 and a_no.get() == 0: 
                        a_label = Label(root,text="Центростремительное ускорение (a-цр):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        u_label = Label(root,text="Скорость (U):")
                        u_label.pack(anchor=NW)
                        u_entry = Entry(root,textvariable=u_en)
                        u_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=asr_r)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,a_label,a_entry,u_entry,u_label))
                        root.config(menu=main_menu)
                    if u_no.get() == 1 and R_no.get() == 0 and a_no.get() == 0: 
                        a_label = Label(root,text="Центростремительное ускорение (a-цр):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        r_label = Label(root,text="Радиус (R):")
                        r_label.pack(anchor=NW)
                        r_entry = Entry(root,textvariable=R_en)
                        r_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=asr_u)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,a_label,a_entry,r_entry,r_label))
                        root.config(menu=main_menu)                        
                    if u_no.get() == 0 and R_no.get() == 0 and a_no.get() == 0: 
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_kinematic_2,u_check,r_check,a_check))
                        root.config(menu=main_menu)
                u_check = ttk.Checkbutton(text="Скорость неизвестна",variable=u_no,command=checkbutton_asr)
                u_check.pack(anchor=NW)
                r_check = ttk.Checkbutton(text="Радиус неизвестен",variable=R_no,command=checkbutton_asr)
                r_check.pack(anchor=NW)
                a_check = ttk.Checkbutton(text="Центростремительное ускорение неизвестно", variable=a_no,command=checkbutton_asr)
                a_check.pack(anchor=NW)
            if selection3 == "Связь между линейной и угловой скоростью":
                print("U=ω*R")
                def checkbutton_sv_l_r():
                    if ω_no.get() == 1 and u_no.get() == 0 and R_no.get() == 0:
                        u_label = Label(root,text="Линейная скорость (U):")
                        u_label.pack(anchor=NW)
                        u_entry = Entry(root,textvariable=u_en)
                        u_entry.pack(anchor=NW)
                        r_label = Label(root,text="Радиус (R):")
                        r_label.pack(anchor=NW)
                        r_entry = Entry(root,textvariable=R_en)
                        r_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=sv_lr_ω)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,u_label,u_entry,r_entry,r_label))
                        root.config(menu=main_menu)     
                    if ω_no.get() == 0 and u_no.get() == 1 and R_no.get() == 0:
                        ω_label = Label(root,text="Угловая скорость (ω):")
                        ω_label.pack(anchor=NW)
                        ω_entry = Entry(root,textvariable=ω_en)
                        ω_entry.pack(anchor=NW)
                        r_label = Label(root,text="Радиус (R):")
                        r_label.pack(anchor=NW)
                        r_entry = Entry(root,textvariable=R_en)
                        r_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=sv_lr_u)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,ω_label,ω_entry,r_entry,r_label))
                        root.config(menu=main_menu)     
                    if ω_no.get() == 0 and u_no.get() == 0 and R_no.get() == 1:
                        u_label = Label(root,text="Линейная скорость (U):")
                        u_label.pack(anchor=NW)
                        u_entry = Entry(root,textvariable=u_en)
                        u_entry.pack(anchor=NW)
                        ω_label = Label(root,text="Угловая скорость (ω):")
                        ω_label.pack(anchor=NW)
                        ω_entry = Entry(root,textvariable=ω_en)
                        ω_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=sv_lr_r)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,u_label,u_entry,ω_entry,ω_label))
                        root.config(menu=main_menu)   
                    if ω_no.get() == 0 and u_no.get() == 0 and R_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_kinematic_2,u_check,r_check,ω_check))
                        root.config(menu=main_menu)
                ω_check = ttk.Checkbutton(text="Угловая скорость неизвестна",variable=ω_no,command=checkbutton_sv_l_r)
                ω_check.pack(anchor=NW)
                u_check = ttk.Checkbutton(text="Линейная скорость неизвестна (обозначает связь)",variable=u_no,command=checkbutton_sv_l_r)
                u_check.pack(anchor=NW)
                r_check = ttk.Checkbutton(text="Радиус неизвестен",variable=R_no,command=checkbutton_sv_l_r)
                r_check.pack(anchor=NW)
        combobox_kinematic_2 = ttk.Combobox(root, values=Formules_Kinematic_2, state="readonly",width="45")
        combobox_kinematic_2.pack(anchor=NW)
        combobox_kinematic_2.bind("<<ComboboxSelected>>", selected_box_kinematic_2)
    if selection == "Динамика":
        def selected_box_dunamica(event):
            selection4 = combobox_dunamica.get()
            if selection4 == "Второй закон Ньютона":
                def checkbutton_new2():
                    if F_no.get() == 1 and a_no.get() == 0 and m_no.get() == 0:
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=new2_F)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,a_label,a_entry,m_entry,m_label))
                        root.config(menu=main_menu)   
                    if F_no.get() == 0 and a_no.get() == 1 and m_no.get() == 0:
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        f_label = Label(root,text="Сила (F):")
                        f_label.pack(anchor=NW)
                        f_entry = Entry(root,textvariable=F_en)
                        f_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=new2_a)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,f_label,f_entry,m_entry,m_label))
                        root.config(menu=main_menu) 
                    if F_no.get() == 0 and a_no.get() == 0 and m_no.get() == 1:
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        f_label = Label(root,text="Сила (F):")
                        f_label.pack(anchor=NW)
                        f_entry = Entry(root,textvariable=F_en)
                        f_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=new2_m)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,f_label,f_entry,a_entry,a_label))
                        root.config(menu=main_menu) 
                    if F_no.get() == 0 and a_no.get() == 0 and m_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_dunamica,m_check,a_check,F_check))
                        root.config(menu=main_menu)
                m_check = ttk.Checkbutton(text="Масса неизвестна",variable=m_no,command=checkbutton_new2)
                m_check.pack(anchor=NW)
                F_check = ttk.Checkbutton(text="Сила неизвестна",variable=F_no,command=checkbutton_new2)
                F_check.pack(anchor=NW)
                a_check = ttk.Checkbutton(text="Ускорение неизвестно",variable=a_no,command=checkbutton_new2)
                a_check.pack(anchor=NW)
            if selection4 == "Плотность вещества":
                def checkbutton_ro():
                    if ρ_no.get() == 1 and V_no.get() == 0 and m_no.get() == 0:
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        V_label = Label(root,text="Объем (V):")
                        V_label.pack(anchor=NW)
                        V_entry = Entry(root,textvariable=V_en)
                        V_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=plot_ro)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,V_label,V_entry,m_entry,m_label))
                        root.config(menu=main_menu)      
                    if ρ_no.get() == 0 and V_no.get() == 1 and m_no.get() == 0: 
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        ρ_label = Label(root,text="Плотность вещества (ρ):")
                        ρ_label.pack(anchor=NW)
                        ρ_entry = Entry(root,textvariable=ρ_en)
                        ρ_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=plot_V)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,ρ_label,ρ_entry,m_entry,m_label))
                        root.config(menu=main_menu)      
                    if ρ_no.get() == 0 and V_no.get() == 0 and m_no.get() == 1:
                        ρ_label = Label(root,text="Плотность вещества (ρ):")
                        ρ_label.pack(anchor=NW)
                        ρ_entry = Entry(root,textvariable=ρ_en)
                        ρ_entry.pack(anchor=NW)
                        V_label = Label(root,text="Объем (V):")
                        V_label.pack(anchor=NW)
                        V_entry = Entry(root,textvariable=V_en)
                        V_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=plot_m)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,V_label,V_entry,ρ_entry,ρ_label))
                        root.config(menu=main_menu)      
                    if ρ_no.get() == 0 and V_no.get() == 0 and m_no.get() == 0: 
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_dunamica,ro_check,m_check,V_check))
                        root.config(menu=main_menu)
                ro_check = ttk.Checkbutton(text="Плотность вещества неизвестна",variable=ρ_no,command=checkbutton_ro)
                ro_check.pack(anchor=NW) 
                m_check = ttk.Checkbutton(text="Масса неизвестна",variable=m_no,command=checkbutton_ro)
                m_check.pack(anchor=NW)
                V_check = ttk.Checkbutton(text="Объем неизвестен",variable=V_no,command=checkbutton_ro)    
                V_check.pack(anchor=NW)        
            if selection4 == "Закон всемирного тяготения":    
                m1_label = Label(root,text="Масса тела (m):")
                m1_label.pack(anchor=NW)
                m1_entry = Entry(root,textvariable=m1_en)
                m1_entry.pack(anchor=NW)
                m2_label = Label(root,text="Масса планеты (M):")
                m2_label.pack(anchor=NW)
                m2_entry = Entry(root,textvariable=m2_en)
                m2_entry.pack(anchor=NW)
                r_label = Label(root,text="Радиус (R):")
                r_label.pack(anchor=NW)
                r_entry = Entry(root,textvariable=t_en)
                r_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=zakon_vsetg)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,m1_label,m1_entry,m2_label,m2_entry,r_entry,r_label,combobox_dunamica))
                root.config(menu=main_menu)
            if selection4 == "Сила тяжести":
                m_label = Label(root,text="Масса (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=power_tz)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f4(result_button,m_label,m_entry,combobox_dunamica))
                root.config(menu=main_menu)
            if selection4 == "Сила упругости. Закон Гука":
                def checkbutton_rulezk():
                    if x_no.get() == 1 and k_no.get() == 0 and F_no.get() == 0:
                        k_label = Label(root,text="Коэффициент жесткости (k):")
                        k_label.pack(anchor=NW)
                        k_entry = Entry(root,textvariable=k_en)
                        k_entry.pack(anchor=NW)
                        F_label = Label(root,text="Сила (F):")
                        F_label.pack(anchor=NW)
                        F_entry = Entry(root,textvariable=F_en)
                        F_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=zk_gyk_delx)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,F_label,F_entry,k_entry,k_label))
                        root.config(menu=main_menu)     
                    if x_no.get() == 0 and k_no.get() == 1 and F_no.get() == 0:
                        x_label = Label(root,text="Деформация пружины (Δx):")
                        x_label.pack(anchor=NW)
                        x_entry = Entry(root,textvariable=x_en)
                        x_entry.pack(anchor=NW)
                        F_label = Label(root,text="Сила (F):")
                        F_label.pack(anchor=NW)
                        F_entry = Entry(root,textvariable=F_en)
                        F_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=zk_gyk_k)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,F_label,F_entry,x_entry,x_label))
                        root.config(menu=main_menu)   
                    if x_no.get() == 0 and k_no.get() == 0 and F_no.get() == 1: 
                        x_label = Label(root,text="Деформация пружины (Δx):")
                        x_label.pack(anchor=NW)
                        x_entry = Entry(root,textvariable=x_en)
                        x_entry.pack(anchor=NW)
                        k_label = Label(root,text="Коэффициент жесткости (k):")
                        k_label.pack(anchor=NW)
                        k_entry = Entry(root,textvariable=k_en)
                        k_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=zk_gyk_F)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,k_label,k_entry,x_entry,x_label))
                        root.config(menu=main_menu)        
                    if x_no.get() == 0 and k_no.get() == 0 and F_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_dunamica,f_check,k_check,delx_check))
                        root.config(menu=main_menu)
                delx_check = ttk.Checkbutton(text="Деформация пружины неизвестна",variable=x_no,command=checkbutton_rulezk)
                delx_check.pack(anchor=NW)
                k_check = ttk.Checkbutton(text="Коэффициент жесткости неизвестен",variable=k_no,command=checkbutton_rulezk) 
                k_check.pack(anchor=NW)
                f_check = ttk.Checkbutton(text="Сила неизвестна",variable=F_no,command=checkbutton_rulezk)
                f_check.pack(anchor=NW)
            if selection4 == "Вес":  
                def weight_up():
                    if w_upn.get() == 1 and w_dn.get() == 0:
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=weight_up_a)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,a_label,a_entry,m_entry,m_label))
                        root.config(menu=main_menu)  
                    if w_upn.get() == 0 and w_dn.get() == 1:
                        a_label = Label(root,text="Ускорение (a):")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=weight_up_d)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,a_label,a_entry,m_entry,m_label))
                        root.config(menu=main_menu)  
                    if w_upn.get() == 0 and w_dn.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f3(combobox_dunamica,w_up,w_do))
                        root.config(menu=main_menu)
                w_up = ttk.Checkbutton(text="Вес тела, опускающегося с ускорением и поднимающегося с замедлением",variable=w_upn,command=weight_up)
                w_up.pack(anchor=NW)
                w_do = ttk.Checkbutton(text="Вес тела, опускающегося с замедлением и поднимающегося с ускорением",variable=w_dn,command=weight_up)
                w_do.pack(anchor=NW)
            if selection4 == "Архимедова сила":
                ro_label = Label(root,text="Плотность (ρ):")
                ro_label.pack(anchor=NW)
                ro_entry = Entry(root,textvariable=ρ_en)
                ro_entry.pack(anchor=NW)
                V_label = Label(root,text="Объем (V):")
                V_label.pack(anchor=NW)
                V_entry = Entry(root,textvariable=V_en)
                V_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=arh_power)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(combobox_dunamica,result_button,ro_label,ro_entry,V_entry,V_label))
                root.config(menu=main_menu)  
            if selection4 == "Сила трения покоя":
                def tr_p():
                    if μ_no.get() == 1 and F_no.get() == 0 and N_no.get() == 0: 
                        f_label = Label(root,text="Сила трения (Fтр):")
                        f_label.pack(anchor=NW)
                        f_entry = Entry(root,textvariable=F_en)
                        f_entry.pack(anchor=NW)
                        n_label = Label(root,text="Сила реакции опоры (N):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=N_en)
                        n_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат",command=power_tr_Pμ)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(combobox_dunamica,result_button,f_label,f_entry,n_entry,n_label))
                        root.config(menu=main_menu)  
                    if μ_no.get() == 0 and F_no.get() == 1 and N_no.get() == 0: 
                        μ_label = Label(root,text="Коэффициент трения (μ):")
                        μ_label.pack(anchor=NW)
                        μ_entry = Entry(root,textvariable=μ_en)
                        μ_entry.pack(anchor=NW)
                        n_label = Label(root,text="Сила реакции опоры (N):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=N_en)
                        n_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат",command=power_tr_pF)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(combobox_dunamica,result_button,μ_label,μ_entry,n_entry,n_label))
                        root.config(menu=main_menu)  
                    if μ_no.get() == 0 and F_no.get() == 0 and N_no.get() == 1: 
                        μ_label = Label(root,text="Коэффициент трения (μ):")
                        μ_label.pack(anchor=NW)
                        μ_entry = Entry(root,textvariable=μ_en)
                        μ_entry.pack(anchor=NW)
                        f_label = Label(root,text="Сила трения (Fтр):")
                        f_label.pack(anchor=NW)
                        f_entry = Entry(root,textvariable=F_en)
                        f_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат",command=power_tr_PN)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(combobox_dunamica,result_button,μ_label,μ_entry,f_entry,f_label))
                        root.config(menu=main_menu)      
                    if μ_no.get() == 0 and F_no.get() == 0 and N_no.get() == 0: 
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_dunamica,nu_check,f_check,n_check))
                        root.config(menu=main_menu)
                nu_check = ttk.Checkbutton(text="Коэффициент трения неизвестен",variable=μ_no,command=tr_p)
                nu_check.pack(anchor=NW)
                f_check = ttk.Checkbutton(text="Сила трения неизвестна",variable=F_no,command=tr_p)
                f_check.pack(anchor=NW)
                n_check = ttk.Checkbutton(text="Сила реакции опоры неизвестна",variable=N_no,command=tr_p)
                n_check.pack(anchor=NW)
            if selection4 == "Трение скольжения":  
                μ_label = Label(root,text="Коэффициент трения (μ):")
                μ_label.pack(anchor=NW)
                μ_entry = Entry(root,textvariable=μ_en)
                μ_entry.pack(anchor=NW)
                m_label = Label(root,text="Масса (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=power_tr_sk)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(combobox_dunamica,result_button,μ_label,μ_entry,m_entry,m_label))
                root.config(menu=main_menu)  
            if selection4 == "Жидкое трение":
                def hd_tr():
                    if k_no.get() == 1 and V_no.get() == 0 and F_no.get() == 0 and N_no.get() == 0:
                        V_label = Label(root,text="Объем (V):")
                        V_label.pack(anchor=NW)
                        V_entry = Entry(root,textvariable=V_en)
                        V_entry.pack(anchor=NW)
                        F_label = Label(root,text="Сила жидкого трения (F):")
                        F_label.pack(anchor=NW)
                        F_entry = Entry(root,textvariable=F_en)
                        F_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=hd_tr_k)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,V_label,V_entry,F_entry,F_label))
                        root.config(menu=main_menu)  
                    if k_no.get() == 0 and V_no.get() == 1 and F_no.get() == 0 and N_no.get() == 0: 
                        k_label = Label(root,text="Коэффициент сопротивления (k):")
                        k_label.pack(anchor=NW)
                        k_entry = Entry(root,textvariable=k_en)
                        k_entry.pack(anchor=NW)
                        F_label = Label(root,text="Сила жидкого трения (F):")
                        F_label.pack(anchor=NW)
                        F_entry = Entry(root,textvariable=F_en)
                        F_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=hd_tr_v)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,k_label,k_entry,F_entry,F_label))
                        root.config(menu=main_menu)  
                    if k_no.get() == 0 and V_no.get() == 0 and F_no.get() == 1 and N_no.get() == 0: 
                        k_label = Label(root,text="Коэффициент сопротивления (k):")
                        k_label.pack(anchor=NW)
                        k_entry = Entry(root,textvariable=k_en)
                        k_entry.pack(anchor=NW)
                        V_label = Label(root,text="Объем (V):")
                        V_label.pack(anchor=NW)
                        V_entry = Entry(root,textvariable=V_en)
                        V_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=hd_tr_F)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,k_label,k_entry,V_entry,V_label))
                        root.config(menu=main_menu)  
                    if k_no.get() == 0 and V_no.get() == 0 and F_no.get() == 0 and N_no.get() == 1: 
                        k_label = Label(root,text="Коэффициент сопротивления (k):")
                        k_label.pack(anchor=NW)
                        k_entry = Entry(root,textvariable=k_en)
                        k_entry.pack(anchor=NW)
                        V_label = Label(root,text="Объем (V):")
                        V_label.pack(anchor=NW)
                        V_entry = Entry(root,textvariable=V_en)
                        V_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=hd_tr_moreV)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                    if k_no.get() == 0 and V_no.get() == 0 and F_no.get() == 0 and N_no.get() == 0: 
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(combobox_dunamica,k_check,V_check,F_check,V2_check))
                        root.config(menu=main_menu)  
                k_check = ttk.Checkbutton(text="Коэффициент сопротивления",variable=k_no,command=hd_tr)
                k_check.pack(anchor=NW)
                V_check = ttk.Checkbutton(text="Объем",variable=V_no,command=hd_tr)
                V_check.pack(anchor=NW)
                F_check = ttk.Checkbutton(text="Сила жидкого трения",variable=F_no,command=hd_tr)
                F_check.pack(anchor=NW)
                V2_check = ttk.Checkbutton(text="Жидкое трение при больших скоростях",variable=N_no,command=hd_tr)
                V2_check.pack(anchor=NW)
        combobox_dunamica = ttk.Combobox(root, values=Formules_Dunamica, state="readonly",width="45")
        combobox_dunamica.pack(anchor=NW)
        combobox_dunamica.bind("<<ComboboxSelected>>", selected_box_dunamica)
    if selection == "Импульс":
        def selected_box_impulus(event):
            selection5 = combobox_impulus.get()
            if selection5 == "Импульс тела":
                print("p=mV")            
                def checkbutton_imtel():
                    if m_no.get() == 1 and V_no.get() == 0 and p_no.get() == 0:
                        v_label = Label(root,text="Скорость (V):")
                        v_label.pack(anchor=NW)
                        v_entry = Entry(root,textvariable=V_en)
                        v_entry.pack(anchor=NW)
                        p_label = Label(root,text="Давление (p):")
                        p_label.pack(anchor=NW)
                        p_entry = Entry(root,textvariable=p_en)
                        p_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=im_tel_m)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,v_label,v_entry,p_entry,p_label))
                        root.config(menu=main_menu) 
                    if m_no.get() == 0 and V_no.get() == 1 and p_no.get() == 0:   
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        p_label = Label(root,text="Давление (p):")
                        p_label.pack(anchor=NW)
                        p_entry = Entry(root,textvariable=p_en)
                        p_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=im_tel_V)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,m_label,m_entry,p_entry,p_label))
                        root.config(menu=main_menu)  
                    if m_no.get() == 0 and V_no.get() == 0 and p_no.get() == 1:   
                        v_label = Label(root,text="Скорость (V):")
                        v_label.pack(anchor=NW)
                        v_entry = Entry(root,textvariable=V_en)
                        v_entry.pack(anchor=NW)
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=im_tel)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,v_label,v_entry,m_entry,m_label))
                        root.config(menu=main_menu)  
                    if m_no.get() == 0 and V_no.get() == 0 and p_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_impulus,m_check,p_check,V_check))
                        root.config(menu=main_menu)
                m_check = ttk.Checkbutton(text="Масса неизвестна",variable=m_no,command=checkbutton_imtel)
                m_check.pack(anchor=NW)
                V_check = ttk.Checkbutton(text="Скорость неизвестна",variable=V_no,command=checkbutton_imtel)
                V_check.pack(anchor=NW)
                p_check = ttk.Checkbutton(text="Импульс неизвестен",variable=p_no,command=checkbutton_imtel)
                p_check.pack(anchor=NW)
            if selection5 == "Импульс силы":
                def checkbutton_impower():
                    if F_no.get() == 1 and t_no.get() == 0 and p_no.get() == 0:
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        p_label = Label(root,text="Давление (p):")
                        p_label.pack(anchor=NW)
                        p_entry = Entry(root,textvariable=p_en)
                        p_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=im_power_f)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,t_label,t_entry,p_entry,p_label))
                        root.config(menu=main_menu) 
                    if F_no.get() == 0 and t_no.get() == 1 and p_no.get() == 0:   
                        f_label = Label(root,text="Сила (F):")
                        f_label.pack(anchor=NW)
                        f_entry = Entry(root,textvariable=F_en)
                        f_entry.pack(anchor=NW)
                        p_label = Label(root,text="Давление (p):")
                        p_label.pack(anchor=NW)
                        p_entry = Entry(root,textvariable=p_en)
                        p_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=im_power_t)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,f_label,f_entry,p_entry,p_label))
                        root.config(menu=main_menu)  
                    if F_no.get() == 0 and t_no.get() == 0 and p_no.get() == 1:   
                        f_label = Label(root,text="Сила (F):")
                        f_label.pack(anchor=NW)
                        f_entry = Entry(root,textvariable=F_en)
                        f_entry.pack(anchor=NW)
                        t_label = Label(root,text="Время (t):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=t_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=im_power)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,t_label,t_entry,f_entry,f_label))
                        root.config(menu=main_menu)  
                    if F_no.get() == 0 and t_no.get() == 0 and p_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формул", command=lambda: del_f4(combobox_impulus,f_check,p_check,t_check))
                        root.config(menu=main_menu)
                f_check = ttk.Checkbutton(text="Сила неизвестна",variable=F_no,command=checkbutton_impower)
                f_check.pack(anchor=NW)
                t_check = ttk.Checkbutton(text="Время неизвестно",variable=t_no,command=checkbutton_impower)
                t_check.pack(anchor=NW)
                p_check = ttk.Checkbutton(text="Импульс неизвестен",variable=p_no,command=checkbutton_impower)
                p_check.pack(anchor=NW)
            if selection5 == "Абсолютно упругий удар":
                m_label = Label(root,text="Масса первого тела (m₁):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                m1_label = Label(root,text="Масса второго тела (m₂):")
                m1_label.pack(anchor=NW)
                m1_entry = Entry(root,textvariable=m1_en)
                m1_entry.pack(anchor=NW)
                v_label = Label(root,text="Скорость первого тела (V₁):")
                v_label.pack(anchor=NW)
                v_entry = Entry(root,textvariable=V_en)
                v_entry.pack(anchor=NW)
                v1_label = Label(root,text="Скорость второго тела (V₂):")
                v1_label.pack(anchor=NW)
                v1_entry = Entry(root,textvariable=v1_en)
                v1_entry.pack(anchor=NW)
                v2_label = Label(root,text="Скорость первого тела после удара(V₁|):")
                v2_label.pack(anchor=NW)
                v2_entry = Entry(root,textvariable=v2_en)
                v2_entry.pack(anchor=NW)
                v11_label = Label(root,text="Скорость второго тела после удара(V₂|):")
                v11_label.pack(anchor=NW)
                v11_entry = Entry(root,textvariable=v11_en)
                v11_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=ab_neypr)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f13(result_button,m_label,m_entry,v_entry,v_label,v1_entry,v1_label,v2_label,v2_entry,v11_label,v11_entry,m1_label,m1_entry))
                root.config(menu=main_menu)  
            if selection5 == "Абсолютно неупругий удар":  
                m_label = Label(root,text="Масса первого тела (m₁):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                m1_label = Label(root,text="Масса второго тела (m₂):")
                m1_label.pack(anchor=NW)
                m1_entry = Entry(root,textvariable=m1_en)
                m1_entry.pack(anchor=NW)
                v_label = Label(root,text="Скорость первого тела (V₁):")
                v_label.pack(anchor=NW)
                v_entry = Entry(root,textvariable=V_en)
                v_entry.pack(anchor=NW)
                v1_label = Label(root,text="Скорость второго тела (V₂):")
                v1_label.pack(anchor=NW)
                v1_entry = Entry(root,textvariable=v1_en)
                v1_entry.pack(anchor=NW)
                v2_label = Label(root,text="Общая скорость(V1):")
                v2_label.pack(anchor=NW)
                v2_entry = Entry(root,textvariable=v2_en)
                v2_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=ab_ypr)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f11(result_button,m_label,m_entry,v_entry,v_label,v1_entry,v1_label,v2_label,v2_entry,m1_label,m1_entry))
                root.config(menu=main_menu)    
        combobox_impulus = ttk.Combobox(root, values=Formules_Impulus, state="readonly",width="45")
        combobox_impulus.pack(anchor=NW)
        combobox_impulus.bind("<<ComboboxSelected>>", selected_box_impulus) 
    if selection == "Работа силы":
        def selected_box_workfight(event):
            selection6 = combobox_workfight.get()
            if selection6 == "Работа":
                print("A=FS*cosa")   
                S_label = Label(root,text="Перемещение (S):")
                S_label.pack(anchor=NW)
                S_entry = Entry(root,textvariable=S_en)
                S_entry.pack(anchor=NW)
                f_label = Label(root,text="Сила (F):")
                f_label.pack(anchor=NW)
                f_entry = Entry(root,textvariable=F_en)
                f_entry.pack(anchor=NW)
                a_label = Label(root,text="cosA")
                a_label.pack(anchor=NW)
                a_entry = Entry(root,textvariable=a_en)
                a_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат",command=work)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,S_label,S_entry,a_label,a_entry,f_label,f_entry,combobox_workfight))
                root.config(menu=main_menu)  
            if selection6 == "Работа сила упругости":
                def ypr():
                    if F_no.get() == 1 and A_no.get() == 0:
                        k_label = Label(root,text="Коэффициент жесткости (k):")
                        k_label.pack(anchor=NW)
                        k_entry = Entry(root,textvariable=k_en)
                        k_entry.pack(anchor=NW)
                        x_label = Label(root,text="Деформация пружины (x):")
                        x_label.pack(anchor=NW)
                        x_entry = Entry(root,textvariable=x_en)
                        x_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=work_power_ypr1)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,x_label,x_entry,k_entry,k_label))
                        root.config(menu=main_menu)  
                    if F_no.get() == 0 and A_no.get() == 1:
                        k_label = Label(root,text="Коэффициент жесткости (k):")
                        k_label.pack(anchor=NW)
                        k_entry = Entry(root,textvariable=k_en)
                        k_entry.pack(anchor=NW)
                        x_label = Label(root,text="Деформация пружины (x):")
                        x_label.pack(anchor=NW)
                        x_entry = Entry(root,textvariable=x_en)
                        x_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=work_power_ypr)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,x_label,x_entry,k_entry,k_label))
                        root.config(menu=main_menu)  
                    if F_no.get() == 0 and A_no.get() == 0: 
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f3(combobox_workfight,yp_check,yp1_check))
                        root.config(menu=main_menu)  
                yp_check = ttk.Checkbutton(text="Сила упругости с одной деформацией",variable=F_no,command=ypr)
                yp_check.pack(anchor=NW)
                yp1_check = ttk.Checkbutton(text="Сила упругости между двумя деформациями",variable=A_no,command=ypr)    
                yp1_check.pack(anchor=NW)
            if selection6 == "Работа в поле силы тяжести":
                def tg_p():
                    if A_no.get() == 1 and F_no.get() == 0:
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        h_label = Label(root,text="Высота (h):")
                        h_label.pack(anchor=NW)
                        h_entry = Entry(root,textvariable=h1_en)
                        h_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=work_power_tg1)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,h_label,h_entry,m_entry,m_label))
                        root.config(menu=main_menu)  
                    if A_no.get() == 0 and F_no.get() == 1:
                        m_label = Label(root,text="Масса (m):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        h_label = Label(root,text="Первая высота (h₁):")
                        h_label.pack(anchor=NW)
                        h_entry = Entry(root,textvariable=h1_en)
                        h_entry.pack(anchor=NW)
                        h1_label = Label(root,text="Вторая высота (h₂):")
                        h1_label.pack(anchor=NW)
                        h1_entry = Entry(root,textvariable=h2_en)
                        h1_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=work_power_tg)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,h_label,h_entry,m_entry,m_label,h1_label,h1_entry))
                        root.config(menu=main_menu)  
                    if A_no.get() == 0 and F_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f3(combobox_workfight,tg1_check,tg_check))
                        root.config(menu=main_menu)  
                tg_check = ttk.Checkbutton(text="Работа с одной высотой",variable=A_no,command=tg_p)
                tg_check.pack(anchor=NW)
                tg1_check = ttk.Checkbutton(text="Работа с двумя высотами",variable=F_no,command=tg_p)
                tg1_check.pack(anchor=NW)
            if selection6 == "Мощность":
                def n1_run():
                    if a_no.get() == 1 and S_no.get() == 0:
                        def n1_kkrun():
                            if t_no.get() == 1 and A_no.get() == 0 and N_no.get() == 0: 
                                A_label = Label(root,text="Работа (А):")
                                A_label.pack(anchor=NW)
                                A_entry = Entry(root,textvariable=A_en)
                                A_entry.pack(anchor=NW)
                                N_label = Label(root,text="Мощность (N):")
                                N_label.pack(anchor=NW)
                                N_entry = Entry(root,textvariable=N_en)
                                N_entry.pack(anchor=NW)
                                result_button = Button(root,text="Результат", command=power_N1_t)
                                result_button.pack(anchor=NW)
                                main_menu = Menu()
                                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,N_label,N_entry,A_entry,A_label))
                                root.config(menu=main_menu)  
                            if t_no.get() == 0 and A_no.get() == 1 and N_no.get() == 0: 
                                t_label = Label(root,text="Время (t):")
                                t_label.pack(anchor=NW)
                                t_entry = Entry(root,textvariable=t_en)
                                t_entry.pack(anchor=NW)
                                N_label = Label(root,text="Мощность (N):")
                                N_label.pack(anchor=NW)
                                N_entry = Entry(root,textvariable=N_en)
                                N_entry.pack(anchor=NW)
                                result_button = Button(root,text="Результат", command=power_N1_A)
                                result_button.pack(anchor=NW)
                                main_menu = Menu()
                                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,N_label,N_entry,t_entry,t_label))
                                root.config(menu=main_menu)  
                            if t_no.get() == 0 and A_no.get() == 0 and N_no.get() == 1:      
                                A_label = Label(root,text="Работа (А):")
                                A_label.pack(anchor=NW)
                                A_entry = Entry(root,textvariable=A_en)
                                A_entry.pack(anchor=NW)
                                t_label = Label(root,text="Время (t):")
                                t_label.pack(anchor=NW)
                                t_entry = Entry(root,textvariable=t_en)
                                t_entry.pack(anchor=NW)
                                result_button = Button(root,text="Результат", command=power_N1)
                                result_button.pack(anchor=NW)
                                main_menu = Menu()
                                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(result_button,t_label,t_entry,A_entry,A_label))
                                root.config(menu=main_menu)     
                            if t_no.get() == 0 and A_no.get() == 0 and N_no.get() == 0: 
                                main_menu = Menu()
                                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f(combobox_workfight,t_check,a_check,n_check))
                                root.config(menu=main_menu)  
                        t_check = ttk.Checkbutton(text="Время неизвестно",variable=t_no,command=n1_kkrun)
                        t_check.pack(anchor=NW)
                        a_check = ttk.Checkbutton(text="Работа неизвестна",variable=A_no,command=n1_kkrun)
                        a_check.pack(anchor=NW)
                        n_check = ttk.Checkbutton(text="Мощность неизвестна",variable=N_no,command=n1_kkrun)
                        n_check.pack(anchor=NW)
                    if a_no.get() == 0 and S_no.get() == 1: 
                        f_label = Label(root,text="Сила (F):")
                        f_label.pack(anchor=NW)
                        f_entry = Entry(root,textvariable=F_en)
                        f_entry.pack(anchor=NW)
                        v_label = Label(root,text="Скорость (V):")
                        v_label.pack(anchor=NW)
                        v_entry = Entry(root,textvariable=V_en)
                        v_entry.pack(anchor=NW)
                        a_label = Label(root,text="cosA:")
                        a_label.pack(anchor=NW)
                        a_entry = Entry(root,textvariable=a_en)
                        a_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=power_N2)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f11(result_button,f_label,f_entry,v_entry,v_label,a_label,a_entry,N1_check,N2_check,combobox_workfight))
                        root.config(menu=main_menu) 
                N1_check = ttk.Checkbutton(text="Мощность с работой и временем",variable=a_no,command=n1_run)
                N1_check.pack(anchor=NW)
                N2_check = ttk.Checkbutton(text="Мощность с силой, скоростью и косинусом",variable=S_no,command=n1_run)
                N2_check.pack(anchor=NW)
            if selection6 == "Кинетическая энергия":
                m_label = Label(root,text="Масса (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                v_label = Label(root,text="Скорость (V):")
                v_label.pack(anchor=NW)
                v_entry = Entry(root,textvariable=V_en)
                v_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=kunetic)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,m_label,m_entry,v_entry,v_label,combobox_workfight))
                root.config(menu=main_menu)   
            if selection6 == "Потенциальная энергия тела с высоты":
                m_label = Label(root,text="Масса (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                h_label = Label(root,text="Высота (h):")
                h_label.pack(anchor=NW)
                h_entry = Entry(root,textvariable=h1_en)
                h_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=poten_h)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,m_label,m_entry,h_entry,h_label,combobox_workfight))
                root.config(menu=main_menu)  
            if selection6 == "Потенциальная энергия тела, которое обладает деформацией":
                k_label = Label(root,text="Коэффициент жесткости (k):")
                k_label.pack(anchor=NW)
                k_entry = Entry(root,textvariable=k_en)
                k_entry.pack(anchor=NW)
                x_label = Label(root,text="Удлинение тела (x):")
                x_label.pack(anchor=NW)
                x_entry = Entry(root,textvariable=h1_en)
                x_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=poten_delx)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,k_label,k_entry,x_entry,x_label,combobox_workfight))
                root.config(menu=main_menu)  
            if selection6 == "Потенциальная энергия гравитационного взаимодействия":
                m_label = Label(root,text="Масса тела (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                m1_label = Label(root,text="Масса планеты (M):")
                m1_label.pack(anchor=NW)
                m1_entry = Entry(root,textvariable=m1_en)
                m1_entry.pack(anchor=NW)
                r_label = Label(root,text="Радиус (R):")
                r_label.pack(anchor=NW)
                r_entry = Entry(root,textvariable=R_en)
                r_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=poten_grav)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,m_label,m_entry,m1_entry,m1_label,r_label,r_entry,combobox_workfight))
                root.config(menu=main_menu) 
        combobox_workfight = ttk.Combobox(root, values=Formules_WorkFight, state="readonly",width="45")
        combobox_workfight.pack(anchor=NW)
        combobox_workfight.bind("<<ComboboxSelected>>", selected_box_workfight)         
    if selection == "Механические колебания и волны":
        def selection_box_mexvol(event):
            selection7 = combobox_mechvol.get()
            if selection7 == "Период колебаний":    
                t_label = Label(root,text="Время (t):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                n_label = Label(root,text="Количество колебаний (N):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=N_en)
                n_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=k_obr_T)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_mechvol))
                root.config(menu=main_menu) 
            if selection7 == "Частота колебаний":
                t_label = Label(root,text="Время (t):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                n_label = Label(root,text="Количество колебаний (N):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=N_en)
                n_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=chas_ν)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_mechvol))
                root.config(menu=main_menu) 
            if selection7 == "Циклическая частота":
                def cylc():
                    if ν_no.get() == 1 and t_no.get() == 0:
                        ν_label = Label(root,text="Частота колебаний (ν):")
                        ν_label.pack(anchor=NW)
                        ν_entry = Entry(root,textvariable=ν_en)
                        ν_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=mex_cylc_nu)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f3(result_button,ν_label,ν_entry))
                        root.config(menu=main_menu) 
                    if ν_no.get() == 0 and t_no.get() == 1:
                        t_label = Label(root,text="Период (T):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=T_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=mex_cylc)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f3(result_button,t_label,t_entry))
                        root.config(menu=main_menu) 
                    if ν_no.get() == 0 and t_no.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f3(combobox_mechvol,nu_check,t_check))
                        root.config(menu=main_menu)  
                nu_check = ttk.Checkbutton(text="Циклическая частота от обычной частоты",variable=ν_no,command=cylc) 
                nu_check.pack(anchor=NW)
                t_check = ttk.Checkbutton(text="Циклическая частота от периода",variable=t_no,command=cylc)
                t_check.pack(anchor=NW)
            if selection7 == "Длина волны":
                t_label = Label(root,text="Период (T):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=T_en)
                t_entry.pack(anchor=NW)
                v_label = Label(root,text="Скорость (V):")
                v_label.pack(anchor=NW)
                v_entry = Entry(root,textvariable=V_en)
                v_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=volna)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,v_label,v_entry,combobox_mechvol))
                root.config(menu=main_menu) 
            if selection7 == "Формула Гюйгенса":
                l_label = Label(root,text="Длина нити (l):")
                l_label.pack(anchor=NW)
                l_entry = Entry(root,textvariable=l_en)
                l_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=math_per)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f4(result_button,l_label,l_entry,combobox_mechvol))
                root.config(menu=main_menu) 
            if selection7 == "Формула периода пружинного маятника":    
                m_label = Label(root,text="Масса (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                k_label = Label(root,text="Коэффициент пружины (k):")
                k_label.pack(anchor=NW)
                k_entry = Entry(root,textvariable=k_en)
                k_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=pryz_per)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,m_label,m_entry,k_label,k_entry,combobox_mechvol))
                root.config(menu=main_menu) 
        combobox_mechvol = ttk.Combobox(root,values=Formules_MechanicCol,state="readonly",width="45")
        combobox_mechvol.pack(anchor=NW)
        combobox_mechvol.bind("<<ComboboxSelected>>",selection_box_mexvol)
    if selection == "Агрегатные состояния вещества":
        def agregat():
            if a_no.get() == 1 and N_no.get() == 0:
                m_label = Label(root,text="Масса капель (M):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                m1_label = Label(root,text="Число капель (n):")
                m1_label.pack(anchor=NW)
                m1_entry = Entry(root,textvariable=N_en)
                m1_entry.pack(anchor=NW)
                r_label = Label(root,text="Внутренний диаметр пипетки (d):")
                r_label.pack(anchor=NW)
                r_entry = Entry(root,textvariable=d_en)
                r_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=formula_powerfnaz)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f9(result_button,m_label,m_entry,m1_entry,m1_label,r_label,r_entry,zozdyh,powerfnaz))
                root.config(menu=main_menu) 
            if a_no.get() == 0 and N_no.get() == 1:
                ρ_label = Label(root,text="Абсолютная влажность воздуха (ρ):")
                ρ_label.pack(anchor=NW)
                ρ_entry = Entry(root,textvariable=ρ_en)
                ρ_entry.pack(anchor=NW)
                ρ1_label = Label(root,text="Плотность насыщенного водяного пара (ρ₀):")
                ρ1_label.pack(anchor=NW)
                ρ1_entry = Entry(root,textvariable=R_en)
                ρ1_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=otnos_vozdyh)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,powerfnaz,zozdyh,ρ_label,ρ_entry,ρ1_entry,ρ1_label))
                root.config(menu=main_menu) 
            if a_no.get() == 0 and N_no.get() == 0: 
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f2(zozdyh,powerfnaz))
                root.config(menu=main_menu)  
        powerfnaz = ttk.Checkbutton(text="Коэффицинт поверхностного натяжения", variable=a_no,command=agregat)
        powerfnaz.pack(anchor=NW)
        zozdyh = ttk.Checkbutton(text="Относительная влажность воздуха",variable=N_no,command=agregat)
        zozdyh.pack(anchor=NW)
    if selection == "Молекулярно-кинетическая теория":
        def selection_box_mkt(event):
            selection8 = combobox_mkt.get()
            if selection8 == "Моль (через молярную массу)": 
                m_label = Label(root,text="Масса вещества (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                m1_label = Label(root,text="Молярная масса (Mr):")
                m1_label.pack(anchor=NW)
                m1_entry = Entry(root,textvariable=m1_en)
                m1_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=kol_vo_1)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,combobox_mkt,m_label,m_entry,m1_entry,m1_label))
                root.config(menu=main_menu) 
            if selection8 == "Моль (черел кол-во молекул)":
                n_label = Label(root,text="Количество молекул (N):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=N_en)
                n_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=kol_vo_2)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f4(result_button,combobox_mkt,n_label,n_entry))
                root.config(menu=main_menu) 
            if selection8 == "Основное уравнение МКТ":
                def mkt_res():
                    if per.get() == 1 and per0.get() == 0 and per1.get() == 0:
                        n_label = Label(root,text="Концентрация молекул (n):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=N_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Температура, Кельвины (Т):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=T_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=mkt_1)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f(result_button,t_label,t_entry,n_entry,n_label))
                        root.config(menu=main_menu) 
                    if per.get() == 0 and per0.get() == 1 and per1.get() == 0:
                        n_label = Label(root,text="Концентрация молекул (n):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=N_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Средняя кинетическая энергия (Ек):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=E_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=mkt_2)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f(result_button,t_label,t_entry,n_entry,n_label))
                        root.config(menu=main_menu) 
                    if per.get() == 0 and per0.get() == 0 and per1.get() == 1:
                        n_label = Label(root,text="Концентрация молекул (n):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=N_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Средняя квадратичная скорость (V_):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=V_en)
                        t_entry.pack(anchor=NW)
                        m_label = Label(root,text="Масса одной молекулы (m₀):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=m_en)
                        m_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=mkt_3)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry))
                        root.config(menu=main_menu) 
                    if per.get() == 0 and per0.get() == 0 and per1.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f4(mkt3,combobox_mkt,mkt2,mkt1))
                        root.config(menu=main_menu) 
                mkt1 = ttk.Checkbutton(text="Ур-е МКТ с постоянной Больцмана и температурой",variable=per,command=mkt_res)
                mkt1.pack(anchor=NW)
                mkt2 = ttk.Checkbutton(text="Ур-е МКТ с ср.кинетической энергией",variable=per0,command=mkt_res)
                mkt2.pack(anchor=NW)
                mkt3 = ttk.Checkbutton(text="Ур-е МКТ с массой одной молекулы и ср.квадрат.скоростью",variable=per1,command=mkt_res)
                mkt3.pack(anchor=NW)
            if selection8 == "Средняя кинетическая энергия":
                t_label = Label(root,text="Температура, Кельвины (T)):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=T_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sr_ek)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f4(result_button,combobox_mkt,t_label,t_entry))
                root.config(menu=main_menu) 
            if selection8 == "Средняя квадратичная скорость":
                n_label = Label(root,text="Радиус (R):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=R_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Температура, Кельвины (T):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=T_en)
                t_entry.pack(anchor=NW)
                m_label = Label(root,text="Масса (M):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sr1_v)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_mkt))
                root.config(menu=main_menu) 
            if selection8 == "Уравнение Менделеева-Клайперона":    
                n_label = Label(root,text="Моль (ν):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=ν_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Температура, Кельвины (T):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=T_en)
                t_entry.pack(anchor=NW)
                m_label = Label(root,text="Радиус (R):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=R_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=men_klap)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_mkt))
                root.config(menu=main_menu) 
        combobox_mkt = ttk.Combobox(root,values=Formules_MKT,state="readonly",width="45")  
        combobox_mkt.pack(anchor=NW)
        combobox_mkt.bind("<<ComboboxSelected>>",selection_box_mkt)      
    if selection == "Элементы термодинамики":
        def selection_box_elmtermodunamic(event):
            selection9 = combobox_elmtdc.get()
            if selection9 == "Внутренняя энергия тела":
                print("U=Eк+Еп")
                n_label = Label(root,text="Кинетическая энергия (Ек):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=N_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Потенциальная энергия (Еп):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=E_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=inside_energy)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_combobox(result_button,t_label,t_entry,n_entry,n_label,combobox_elmtdc))
                root.config(menu=main_menu) 
            if selection9 == "Внутренняя энергия идеального тела": 
                print("i*nu*RT/2")   
                m_label = Label(root,text="Число степеней свободы (i):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=i_en)
                m_entry.pack(anchor=NW)
                m1_label = Label(root,text="Количество вещества(ν):")
                m1_label.pack(anchor=NW)
                m1_entry = Entry(root,textvariable=ν_en)
                m1_entry.pack(anchor=NW)
                v_label = Label(root,text="Расстояние (К):")
                v_label.pack(anchor=NW)
                v_entry = Entry(root,textvariable=R_en)
                v_entry.pack(anchor=NW)
                v1_label = Label(root,text="Температура (T):")
                v1_label.pack(anchor=NW)
                v1_entry = Entry(root,textvariable=T_en)
                v1_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=in_energy_gaz)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f10(result_button,m_label,m_entry,v_entry,v_label,v1_entry,v1_label,m1_label,m1_entry,combobox_elmtdc))
                root.config(menu=main_menu)    
            if selection9 == "Работа газа в термодинамике":   
                print("A=pV") 
                n_label = Label(root,text="Давление (p):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=p_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Объем (V):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=V_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=work_gaz)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elmtdc))
                root.config(menu=main_menu) 
            if selection9 == "Формула нагревания (охлаждения)":    
                print("Q=cm<t>")
                n_label = Label(root,text="Удельная теплоемкость вещества (c):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=a_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Температура (T):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                m_label = Label(root,text="Масса (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=formula_nagrev)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elmtdc))
                root.config(menu=main_menu) 
            if selection9 == "Формаула плавления (отвердевания)":
                print("Q=lam*m")
                n_label = Label(root,text="Удельная теплота плавления (λ):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=l_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Масса (m):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=m_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=formula_obplav)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elmtdc))
                root.config(menu=main_menu) 
            if selection9 == "Формула парообразования (конденсанции)":
                print("Q=Lm")
                n_label = Label(root,text="Удельная теплота парообразования (L):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=l_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Масса (m):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=m_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=formula_obplav)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elmtdc))
                root.config(menu=main_menu) 
            if selection9 == "Формула сгорания топлива":
                print("Q=qm")
                n_label = Label(root,text="Удельная теплота сгорания (q):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=q1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Масса (m):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=m_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=formula_sgor)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elmtdc))
                root.config(menu=main_menu) 
            if selection9 == "Первый закон термодинамики (с Авн)":
                print("U=Q+A")
                n_label = Label(root,text="Количество теплоты (Q):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=q1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Работа (A):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=A_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=per_zk_termo)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elmtdc))
                root.config(menu=main_menu) 
            if selection9 == "Первый закон термодинамики (с Асис)":
                print("Q=U+A")
                n_label = Label(root,text="Внутрення энергия (U):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=q1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Работа (A):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=A_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=per_zk_termo1)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elmtdc))
                root.config(menu=main_menu) 
        combobox_elmtdc = ttk.Combobox(root,values=Formules_ElementTermodunamic,state="readonly",width="45")    
        combobox_elmtdc.pack(anchor=NW)
        combobox_elmtdc.bind("<<ComboboxSelected>>",selection_box_elmtermodunamic)
    if selection == "Тепловые двигатели":
        def selection_tepl_dv(event):
            selection10 = combobox_tepldv.get()
            if selection10 == "КПД теплового двигателя":
                print("ita=Ап*100%/Qн")
                n_label = Label(root,text="Полезная работа (Ап):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=A_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Количество теплоты нагревателя (Qн):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=u_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=kpd_1)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_tepldv))
                root.config(menu=main_menu) 
            if selection10 == "КПД идеальной тепловой машины":
                print("ita=|Тн-Тх|*100%/Тн")
                n_label = Label(root,text="Температура нагревателя (Tн):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=t_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Температура холодильника (Tх):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=T_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=kpd_2)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_tepldv))
                root.config(menu=main_menu) 
        combobox_tepldv = ttk.Combobox(root,values=Formules_TeplDvig,state="readonly",width="45")
        combobox_tepldv.pack(anchor=NW)
        combobox_tepldv.bind("<<ComboboxSelected>>",selection_tepl_dv)
    if selection == "Электростатика и её элементы":
        def selection_elekstatic(event):
            selection11 = combobox_elekstatic.get()
            if selection11 == "Закон Кулона":
                print("F=q1*q2/R^2")
                n_label = Label(root,text="Первый электрический заряд (q₁):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=q1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Второй электрический заряд (q₂):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=q2_en)
                t_entry.pack(anchor=NW)
                m_label = Label(root,text="Расстояние (R):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=R_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=zk_kylon)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Напряженность обычного заряда":
                print("E=F/q")
                n_label = Label(root,text="Сила (F):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=F_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Электрический заряд (q):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=q1_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=naprizob)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Напряженность точечного заряда":
                print("E=k*q/R^2")
                n_label = Label(root,text="Расстояние (R):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=F_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Электрический заряд (q):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=q1_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=napriztz)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Работа электрического поля":
                d1_label = Label(root,text="Расстояние от заряда до пластины, которое было (d₁):")
                d1_label.pack(anchor=NW)
                d1_entry = Entry(root,textvariable=p1_en)
                d1_entry.pack(anchor=NW)
                d2_label = Label(root,text="Конечное расстояние (d₂):")
                d2_label.pack(anchor=NW)
                d2_entry = Entry(root,textvariable=p2_en)
                d2_entry.pack(anchor=NW)
                q_label = Label(root,text="Электрический заряд (q):")
                q_label.pack(anchor=NW)
                q_entry = Entry(root,textvariable=q1_en)
                q_entry.pack(anchor=NW)
                e_label = Label(root,text="Напряженность (E):")
                e_label.pack(anchor=NW)
                e_entry = Entry(root,textvariable=E_en)
                e_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=rabota_pol)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f10(result_button,d1_label,d1_entry,d2_entry,d2_label,q_entry,q_label,e_label,e_entry,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Потенциальная энергия":
                def poten_power():
                    if per0.get() == 0 and per1.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f3(poten1,poten2,combobox_elekstatic))
                        root.config(menu=main_menu) 
                    if per0.get() == 1 and per1.get() == 0:
                        e_label = Label(root,text="Напряженность (E):")
                        e_label.pack(anchor=NW)
                        e_entry = Entry(root,textvariable=E_en)
                        e_entry.pack(anchor=NW)
                        q_label = Label(root,text="Электрический заряд (q):")
                        q_label.pack(anchor=NW)
                        q_entry = Entry(root,textvariable=q1_en)
                        q_entry.pack(anchor=NW)
                        d_label = Label(root,text="Расстояние (d):")
                        d_label.pack(anchor=NW)
                        d_entry = Entry(root,textvariable=p1_en)
                        d_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=vzaim_zar_s_pol)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,e_label,e_entry,q_entry,q_label,d_label,d_entry,combobox_elekstatic))
                        root.config(menu=main_menu) 
                    if per0.get() == 0 and per1.get() == 1:
                        e_label = Label(root,text="Первый электрический заряд (q₁):")
                        e_label.pack(anchor=NW)
                        e_entry = Entry(root,textvariable=q1_en)
                        e_entry.pack(anchor=NW)
                        q_label = Label(root,text="Второй электрический заряд (q₂):")
                        q_label.pack(anchor=NW)
                        q_entry = Entry(root,textvariable=q2_en)
                        q_entry.pack(anchor=NW)
                        d_label = Label(root,text="Расстояние (R):")
                        d_label.pack(anchor=NW)
                        d_entry = Entry(root,textvariable=R_en)
                        d_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=vzaim_toch_zar)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,e_label,e_entry,q_entry,q_label,d_label,d_entry,combobox_elekstatic))
                        root.config(menu=main_menu) 
                poten1 = ttk.Checkbutton(text="Взаимодействие заряда с полем",variable=per0,command=poten_power)
                poten1.pack(anchor=NW)
                poten2 = ttk.Checkbutton(text="Взаимодействие точечных зарядов",variable=per1,command=poten_power)
                poten2.pack(anchor=NW)
            if selection11 == "Потенциал":
                n_label = Label(root,text="Потенциальная энергия (Wp):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=E_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Электрический заряд (q):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=q1_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=potenc)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Потенциал заряда в среде":
                n_label = Label(root,text="Расстояние (R):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=R_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Электрический заряд (q₀):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=q1_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=potenc_zar_v_srede)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Напряжение":
                def naprr():
                    if per.get() == 0 and per0.get() == 0 and per1.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f4(nap1,nap2,nap3,combobox_elekstatic))
                        root.config(menu=main_menu) 
                    if per.get() == 1 and per0.get() == 0 and per1.get() == 0:
                        n_label = Label(root,text="Потенциал (φ₁):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=q1_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Потенциал (φ₂):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=q2_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=napr)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                        root.config(menu=main_menu) 
                    if per.get() == 0 and per0.get() == 1 and per1.get() == 0:
                        n_label = Label(root,text="Работа (A):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=A_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Электрический заряд (q):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=q1_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=napr2)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                        root.config(menu=main_menu) 
                    if per.get() == 0 and per0.get() == 0 and per1.get() == 1:
                        n_label = Label(root,text="Напряженность (E):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=E_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Расстояние между зарядов (d):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=p1_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=napr3)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                        root.config(menu=main_menu) 
                nap1 = ttk.Checkbutton(text="Разность потенциалов",variable=per,command=naprr)
                nap1.pack(anchor=NW)   
                nap2 = ttk.Checkbutton(text="Работа в поле и заряд",variable=per0,command=naprr) 
                nap2.pack(anchor=NW)
                nap3 = ttk.Checkbutton(text="Напряженность и расстояние между зарядами",variable=per1,command=naprr)
                nap3.pack(anchor=NW)
            if selection11 == "Работа по перемещению заряда":
                n_label = Label(root,text="Первый потенциал (ф₁):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=p1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Второй потенциал (ф₂):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=p2_en)
                t_entry.pack(anchor=NW)
                m_label = Label(root,text="Электрический заряд (q):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=q1_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=rab_po_perem_zar)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Заряд конденсатора":
                n_label = Label(root,text="Первый потенциал (ф₁):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=p1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Второй потенциал (ф₂):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=p2_en)
                t_entry.pack(anchor=NW)
                m_label = Label(root,text="Электрический заряд (q):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=q1_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=rab_po_perem_zar)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Заряд конденсатора (с разностью потенциалов)":
                n_label = Label(root,text="Первый потенциал (ф₁):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=p1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Второй потенциал (ф₂):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=p2_en)
                t_entry.pack(anchor=NW)
                m_label = Label(root,text="Электроёмкость конденсатора (C):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=A_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=zar_condenc2)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekstatic))
                root.config(menu=main_menu)
            if selection11 == "Электроёмкость конденсатора":
                n_label = Label(root,text="Напряжение (U):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=E_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Электрический заряд (q):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=q1_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=electroemk)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                root.config(menu=main_menu) 
            if selection11 == "Электроёмкость плоского конденсатора":
                n_label = Label(root,text="Диэлектрическая проницаемость диэлектрика (ε):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=ε0_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Площадь одной обкладки конденсатора (S):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=S_en)
                t_entry.pack(anchor=NW)
                m_label = Label(root,text="Расстояние между обкладками (d):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=d_en)
                m_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=zar_condenc2)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekstatic))
                root.config(menu=main_menu)
            if selection11 == "Энергия заряженного конденсатора": 
                def energy_zar_con():
                    if per.get() == 0 and per0.get() == 0 and per1.get() == 0 and per2.get() == 0 and per3.get() == 0:
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(energy1,energy2,energy3,energy4,energy5,combobox_elekstatic))
                        root.config(menu=main_menu)
                    if per.get() == 1 and per0.get() == 0 and per1.get() == 0 and per2.get() == 0 and per3.get() == 0:                        
                        n_label = Label(root,text="Электрический заряд (q):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=q1_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Напряженность (E):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=E_en)
                        t_entry.pack(anchor=NW)
                        m_label = Label(root,text="Расстояние между обкладками (d):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=d_en)
                        m_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=energ_zar_condenc)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekstatic))
                        root.config(menu=main_menu)
                    if per.get() == 0 and per0.get() == 1 and per1.get() == 0 and per2.get() == 0 and per3.get() == 0:        
                        n_label = Label(root,text="Напряжение (U):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=E_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Электрический заряд (q):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=q1_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=energ_zar_condenc2)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                        root.config(menu=main_menu)   
                    if per.get() == 0 and per0.get() == 0 and per1.get() == 1 and per2.get() == 0 and per3.get() == 0:                                  
                        n_label = Label(root,text="Электроёмкость конденсатора (C):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=A_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Электрический заряд (q):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=q1_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=energ_zar_condenc3)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                        root.config(menu=main_menu)   
                    if per.get() == 0 and per0.get() == 0 and per1.get() == 0 and per2.get() == 1 and per3.get() == 0:                                  
                        n_label = Label(root,text="Напряжение (U):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=E_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Электроёмкость конденсатора (C):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=A_en)
                        t_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=energ_zar_condenc4)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                        root.config(menu=main_menu)   
                    if per.get() == 0 and per0.get() == 0 and per1.get() == 0 and per2.get() == 0 and per3.get() == 1:                        
                        n_label = Label(root,text="Напряженность (E):")
                        n_label.pack(anchor=NW)
                        n_entry = Entry(root,textvariable=E_en)
                        n_entry.pack(anchor=NW)
                        t_label = Label(root,text="Электроёмкость конденсатора (C):")
                        t_label.pack(anchor=NW)
                        t_entry = Entry(root,textvariable=A_en)
                        t_entry.pack(anchor=NW)
                        m_label = Label(root,text="Расстояние между обкладками (d):")
                        m_label.pack(anchor=NW)
                        m_entry = Entry(root,textvariable=d_en)
                        m_entry.pack(anchor=NW)
                        result_button = Button(root,text="Результат", command=energ_zar_condenc5)
                        result_button.pack(anchor=NW)
                        main_menu = Menu()
                        main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekstatic))
                        root.config(menu=main_menu)                                                
                energy1 = ttk.Checkbutton(text="Напряженность, заряд и расстояние",variable=per,command=energy_zar_con)    
                energy1.pack(anchor=NW)
                energy2 = ttk.Checkbutton(text="Заряд и напряение",variable=per0,command=energy_zar_con)    
                energy2.pack(anchor=NW)
                energy3 = ttk.Checkbutton(text="Заряд и электроёмкость",variable=per1,command=energy_zar_con)    
                energy3.pack(anchor=NW)                
                energy4 = ttk.Checkbutton(text="Электроёмкость и напряжение",variable=per2,command=energy_zar_con)    
                energy4.pack(anchor=NW)
                energy5 = ttk.Checkbutton(text="Электроёмкость, напряженность и расстояние",variable=per3,command=energy_zar_con)    
                energy5.pack(anchor=NW)          
            if selection11 == "Работа заряженного конденсатора (с энергией)":
                n_label = Label(root,text="Первая энергия (Wn₁):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=E_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Вторая энергия (Wn₂):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=A_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=rab_zar_condenc)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekstatic))
                root.config(menu=main_menu)    
            if selection11 == "Работа заряженного конденсатора":
                n_label = Label(root,text="Электрический заряд (q):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=q1_en)
                n_entry.pack(anchor=NW)
                m_label = Label(root,text="Начальное напряжение (U₁):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=A_en)
                m_entry.pack(anchor=NW)
                t_label = Label(root,text="Конечное напряжение (U₂):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=E_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=rab_zar_condenc2)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekstatic))
                root.config(menu=main_menu)                       
        combobox_elekstatic = ttk.Combobox(root,values=Formules_ElekStatic,state="readonly",width="45")
        combobox_elekstatic.pack(anchor=NW)
        combobox_elekstatic.bind("<<ComboboxSelected>>",selection_elekstatic)
    if selection == "Электродинамика":
        def selection_elekdunamic(event):
            selection12 = combobox_elekdunamic.get()
            if selection12 == "Сила тока":
                n_label = Label(root,text="Электрический заряд (Δq):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=q1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Время (Δt):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sila_toka)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekdunamic))
                root.config(menu=main_menu)           
            if selection12 == "Объем проводника":
                n_label = Label(root,text="Средняя скорость упорядоченного движения электронов (V):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=V_en)
                n_entry.pack(anchor=NW)
                m_label = Label(root,text="Площадь поперечного сечения проводника (S):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=S_en)
                m_entry.pack(anchor=NW)
                t_label = Label(root,text="Время (Δt):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=ob_provodn)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekdunamic))
                root.config(menu=main_menu)      
            if selection12 == "Число электронов":
                d1_label = Label(root,text="Концентрация электронов (n):")
                d1_label.pack(anchor=NW)
                d1_entry = Entry(root,textvariable=N_en)
                d1_entry.pack(anchor=NW)
                d2_label = Label(root,text="Скорость движения электронов (V):")
                d2_label.pack(anchor=NW)
                d2_entry = Entry(root,textvariable=V_en)
                d2_entry.pack(anchor=NW)
                q_label = Label(root,text="Время (Δt):")
                q_label.pack(anchor=NW)
                q_entry = Entry(root,textvariable=t_en)
                q_entry.pack(anchor=NW)
                e_label = Label(root,text="Площадь поперечного сечения проводника  (S):")
                e_label.pack(anchor=NW)
                e_entry = Entry(root,textvariable=S_en)
                e_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=kol_electronov)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f10(result_button,d1_label,d1_entry,d2_entry,d2_label,q_entry,q_label,e_label,e_entry,combobox_elekdunamic))
                root.config(menu=main_menu)            
            if selection12 == "Полный заряд":
                d1_label = Label(root,text="Концентрация электронов (n):")
                d1_label.pack(anchor=NW)
                d1_entry = Entry(root,textvariable=N_en)
                d1_entry.pack(anchor=NW)
                d2_label = Label(root,text="Скорость движения электронов (V):")
                d2_label.pack(anchor=NW)
                d2_entry = Entry(root,textvariable=V_en)
                d2_entry.pack(anchor=NW)
                q_label = Label(root,text="Время (Δt):")
                q_label.pack(anchor=NW)
                q_entry = Entry(root,textvariable=t_en)
                q_entry.pack(anchor=NW)
                t_label = Label(root,text="Площадь поперечного сечения проводника  (S):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=S_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=poln_zar)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f10(result_button,d1_label,d1_entry,d2_entry,d2_label,q_entry,q_label,t_label,t_entry,combobox_elekdunamic))
                root.config(menu=main_menu) 
            if selection12 == "Сила тока при связи с зарядом электрона":     
                n_label = Label(root,text="Концентрация электронов (n):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=N_en)
                n_entry.pack(anchor=NW)
                m_label = Label(root,text="Скорость движения электронов (V):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=V_en)
                m_entry.pack(anchor=NW)
                t_label = Label(root,text="Площадь поперечного сечения проводника  (S):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=S_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sila_toka2)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekdunamic))
                root.config(menu=main_menu)   
            if selection12 == "Сила на заряд (при q)":
                n_label = Label(root,text="Электрический заряд (q):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=q1_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Напряженность (E):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=E_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sila_na_zar)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekdunamic))
                root.config(menu=main_menu)  
            if selection12 == "Сила на заряд (Второй закон Ньютона)":
                n_label = Label(root,text="Масса (m):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=m_en)
                n_entry.pack(anchor=NW)
                m_label = Label(root,text="Скорость движения электронов (V):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=V_en)
                m_entry.pack(anchor=NW)
                t_label = Label(root,text="Время (t):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sila_na_zar2)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekdunamic))
                root.config(menu=main_menu)                   
            if selection12 == "Сила тока в металлах":
                d1_label = Label(root,text="Концентрация электронов (n):")
                d1_label.pack(anchor=NW)
                d1_entry = Entry(root,textvariable=N_en)
                d1_entry.pack(anchor=NW)
                d2_label = Label(root,text="Скорость движения электронов (V):")
                d2_label.pack(anchor=NW)
                d2_entry = Entry(root,textvariable=V_en)
                d2_entry.pack(anchor=NW)
                q_label = Label(root,text="Электрический заряд (q):")
                q_label.pack(anchor=NW)
                q_entry = Entry(root,textvariable=q1_en)
                q_entry.pack(anchor=NW)
                e_label = Label(root,text="Площадь поперечного сечения проводника  (S):")
                e_label.pack(anchor=NW)
                e_entry = Entry(root,textvariable=S_en)
                e_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sila_toka_metall)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f10(result_button,d1_label,d1_entry,d2_entry,d2_label,q_entry,q_label,e_label,e_entry,combobox_elekdunamic))
                root.config(menu=main_menu)  
            if selection12 == "Сила тока в электролитах (Закон Фарадея)":     
                n_label = Label(root,text="Электрохимический эквивалент (k):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=k_en)
                n_entry.pack(anchor=NW)
                m_label = Label(root,text="Масса (m):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=m_en)
                m_entry.pack(anchor=NW)
                t_label = Label(root,text="Время (t):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sila_toka_electrolit)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekdunamic))
                root.config(menu=main_menu)      
            if selection12 == "Зависимость сопротивления от t°":
                n_label = Label(root,text="Сопртивление до нагрева (R₀):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=ρ_en)
                n_entry.pack(anchor=NW)
                m_label = Label(root,text="Температурный коэффициент сопротивления (α):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=a_en)
                m_entry.pack(anchor=NW)
                t_label = Label(root,text="Изменение температуры (Δt):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=t_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sopr)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekdunamic))
                root.config(menu=main_menu)   
            if selection12 == "Сопротивление проводника":
                n_label = Label(root,text="Удельное сопротивление проводника (ρ-уд):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=ρ_en)
                n_entry.pack(anchor=NW)
                m_label = Label(root,text="Длина проводника (l):")
                m_label.pack(anchor=NW)
                m_entry = Entry(root,textvariable=l_en)
                m_entry.pack(anchor=NW)
                t_label = Label(root,text="Площадь сечения (S):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=S_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sopr_provodnika)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: del_f8(result_button,t_label,t_entry,n_entry,n_label,m_label,m_entry,combobox_elekdunamic))
                root.config(menu=main_menu)   
            if selection12 == "Сила тока в проводнике":
                n_label = Label(root,text="Напряжение (U):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=E_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Сопротивление (R):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=R_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=sila_toka_v_provodnike)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekdunamic))
                root.config(menu=main_menu) 
            if selection12 == "ЭДС":         
                n_label = Label(root,text="Работа сторонних сил (Асм):")
                n_label.pack(anchor=NW)
                n_entry = Entry(root,textvariable=A_en)
                n_entry.pack(anchor=NW)
                t_label = Label(root,text="Электрический заряд (q):")
                t_label.pack(anchor=NW)
                t_entry = Entry(root,textvariable=q1_en)
                t_entry.pack(anchor=NW)
                result_button = Button(root,text="Результат", command=eds)
                result_button.pack(anchor=NW)
                main_menu = Menu()
                main_menu.add_command(label="Очистить окно формулы", command=lambda: wid_f6(result_button,t_label,t_entry,n_entry,n_label,combobox_elekdunamic))
                root.config(menu=main_menu)                   
        combobox_elekdunamic = ttk.Combobox(root,values=Formules_ElekDunamic,state="readonly",width="45")
        combobox_elekdunamic.pack(anchor=NW)
        combobox_elekdunamic.bind("<<ComboboxSelected>>",selection_elekdunamic)
def selectedbox(event):
    selection = combobox_lectures.get()
    # label["text"] = f"вы выбрали: {selection}"
    if selection == "Введение": 
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert("1.0", 
        "   | Основные понятие:\n"
        "       ❶. Физическое тело - одно из основных понятий физики, под которым понимается форма существования материи\n"
        "       ❷. Вещество - это то, из чего состоят физические тела\n"
        "       ❸. Материя - все, что реально существует в природе (планеты, растения, животные и т.д.)\n"
        "       ❹. Физические явления - это изменения, происходящие с физическими телами\n"
        "       ❺. Физические приборы - специальные устройства, которые предназначены для измерения физических величин\n"
        "\n"
        "   | Физические явления:\n"
        "       ❶. Механические явления (например, движение машин, самолетов, небесных тел, течение жидкости).\n"
        "       ❷. Электрические явления (например, электрический ток, нагревание проводников с током, электризация тел).\n"
        "       ❸. Магнитные явления (например, действие магнитов на железо, вли­яние магнитного поля Земли на стрелку компаса).\n"
        "       ❹. Оптические явления (например, отражение света от зеркал, излуче­ние световых лучей от различных источников света).\n"
        "       ❺. Тепловые явления (таяние льда, кипение воды, тепловое расширение тел).\n"
        "       ❻. Атомные явления (например, работа атомных реакторов, распад ядер, процессы, происходящие внутри звезд).\n"
        "       ❼. Акустические явления (звон колокола, музыка, гром, шум).\n"
        "\n"
        "                                                       Идея атомиза\n"
        "       ➽ Все тела состоят из атомов и молекул.\n"
        "       Э̲л̲е̲м̲е̲н̲т̲а̲р̲н̲а̲я̲ ̲ч̲а̲с̲т̲и̲ц̲а̲ - микрообъект, который невозможно разможить на составные частицы.\n"
        "       А̲т̲о̲м̲ - частица вещества микроскопических размеров и массы, наименьшая часть химического элемента.\n"
        "\n"
        "  | Фундаментальные взаимодействия:\n"
        "       • Сильное;\n"
        "       • Слабое;\n"
        "       • Электромагнитное;\n"
        "       • Гравитационное.\n"
        )
        text_block.pack(anchor=NW)
        text_block.configure(state=DISABLED)
    elif selection == "Глава I. Механика":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert("1.0", 
        " М̲е̲х̲а̲н̲и̲к̲а̲ – это наука, которая изучает механическое движение.\n"
        " М̲е̲х̲а̲н̲и̲ч̲е̲с̲к̲о̲е̲ ̲д̲в̲и̲ж̲е̲н̲и̲е̲ – это изменение положения тела в пространстве относительно других тел.\n"
        " \n"
        "   | Разделы механики: \n"
        "       ❶. Кинематика - это раздел механики, в котором исследуется геометрические свойства движения тел.\n"
        "       ❷. Динамика - это раздел механики, в котором изучаются причины возникновения механического движения.\n"
        "       ❸. Статика - это раздел механики, в которм изучаются условия равновесия материальных тел под влиянием силы.\n"
        " \n"
        "   | Виды колебательного движения: \n"
        "       • Колебательное - это движение, которое обладает той или иной степенью повторяемости во времени;\n"
        "       • Вращательное - это движение твердого тела при котором все его точки описывают окружности с центром оси вращения;\n"
        "       • Поступательное - это движение, при котором все точки одного тела движутся одинаково;\n"
        "                                                       Кинематика\n"
        " \n"
        "   | Система отсчета:\n"
        "       ❶. Тело отсчета;\n"
        "       ❷. Система координат;\n"
        "       ❸. Прибор для измерения времени.\n"
        " \n"
        " Т̲р̲а̲е̲к̲т̲о̲р̲и̲я̲ – линия, вдоль которой движется тело\n"
        " П̲у̲т̲ь̲ – длина траектории, S - путь, [м] (скалярная величина)\n"
        " П̲е̲р̲е̲м̲е̲щ̲е̲н̲и̲е̲ – это направленный отрезок, соединяющий начальное положение тела с его последующим положением, S - перемещение, [м] (векторная величина)\n"
        " М̲а̲т̲е̲р̲и̲а̲л̲ь̲н̲а̲я̲ ̲т̲о̲ч̲к̲а̲ – это тело, размерами и формами которого можно пренебречь в условиях данной задачи.\n"
        " Р̲а̲в̲н̲о̲м̲е̲р̲н̲о̲е̲-̲п̲р̲я̲м̲о̲л̲и̲н̲е̲й̲н̲о̲е̲ ̲д̲в̲и̲ж̲е̲н̲и̲е̲ – это движение, при котором тело за любые равные промежутки времени совершает равные перемещения.\n"
        " С̲к̲о̲р̲о̲с̲т̲ь̲ – это физическая величина, которая характеризует быстроту изменения координаты материальной точки, U - скорость, U=S/t, [м/с]\n"
        " Уравнение движения: x=x0+U*t. x - конечная коор-та, x0 - начальная.\n"        
        " Н̲е̲р̲а̲в̲н̲о̲м̲е̲р̲н̲о̲е̲ ̲д̲в̲и̲ж̲е̲н̲и̲е̲ – это движение, при котором тело за равные промежутки времени совершает неодинаковые перемещения. \nСредняя скорость:"
        )
        img_usr = PhotoImage(file="./image/./image/usr.png")
        text_block.image_create(END,image=img_usr)
        text_block.insert(END,
        " М̲г̲н̲о̲в̲е̲н̲н̲а̲я̲ ̲с̲к̲о̲р̲о̲с̲т̲ь̲ - это предел, к которому стремится средняя скорость за бесконечно малый промежуток времени.\n"
        "\n"
        "                                 Равноускоренное движение\n"
        "  Это движение, при котором скорость за любые равные промежутки времени изменяется одинаково (ускорение постоянно)\n"
        "  У̲с̲к̲о̲р̲е̲н̲и̲е̲ – это физические величина, численно равная отношению скорости к времени. a - ускорение [м/с²] || "
        )
        yrs1 = PhotoImage(file="./image/./image/yrs1.png")
        text_block.image_create(END,image=yrs1)
        text_block.insert(END,
        "\n Скорость при равноускоренном движении: Uₓ=U₀ₓ+aₓ*t\n"
        " Уравнение движения равноускоренного движения: "
        )
        yrdz = PhotoImage(file="./image/./image/yrdz.png")
        text_block.image_create(END,image=yrdz)
        text_block.insert(END, 
        "\n Проекция перемещения: Sₓ=U₀ₓ+aₓ*t\n"
        "                                 Свободное падение\n"
        "  Это движение тела только под влиянием притяжения к Земле. \ng = 9,8 м/с², где g - ускорение свободного падения\n"
        "                          Кинематика движения по окружности\n"
        "       ❶. Период обращения - время полного оборота. T=t/N, [с]. N - период\n"
        "       ❷. Частота - число оборотов в единицу времени. ν=N/t, [Гц]\n"
        "       ❸. Линейная скорость - отношения пройденного пути ко времени. U=2ПR/T или U=2ПRν\n"
        "       ❹. Угловая скорость - быстрота изменения угла. ω = Δφ/Δt, [рад/с]\n"
        "       ❺. Центростремительное ускорение. a-цр = U²/R\n"
        "       ❻. Связь между линейной и угловой скоростью. U=ω*R\n"
        )
        text_block.pack(anchor=NW)
        text_block.configure(state=DISABLED)
        text_block.mainloop()      
    elif selection == "Глава II. Динаминка":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert("1.0", 
        " С̲в̲о̲б̲о̲д̲н̲о̲е̲ ̲т̲е̲л̲о̲ – это тело, которое не испытывает влияние других тел, либо покоется, либо движется равномерно и прямолинейно\n"
        " И̲н̲е̲р̲ц̲и̲я̲ – это явление сохранений состояния покоя или равномерного прямолинейного движения при отсутствии \n"
        " И̲н̲е̲р̲ц̲и̲а̲л̲ь̲н̲а̲я̲ ̲с̲и̲с̲т̲е̲м̲а̲ ̲о̲т̲с̲ч̲е̲т̲а̲ ̲(̲И̲С̲О̲)̲ - это система, в которой тело покоется или движется равномерно и прямолинейно при отсутствии внешних воздействий \n"
        " Н̲е̲и̲н̲е̲р̲ц̲и̲а̲л̲ь̲н̲а̲я̲ ̲с̲и̲с̲т̲е̲м̲а̲ ̲о̲т̲с̲ч̲е̲т̲а̲ ̲(̲Н̲И̲С̲О̲)̲ - это система, в которой тело движется с ускорением \n"
        " \n"
        "   | Три закона Ньютона:\n"
        "       ❶. Инерциальная система отсчета относительно которой тело покоется или движется равномерно и прямолинейно при отсутствии внешних воздействий\n"
        "           И̲н̲е̲р̲т̲н̲о̲с̲т̲ь̲ – свойство тела сохранять состояние равномерного-прямолинейного движения или покоя, когда действующие на него силы отсутствуют или взаимно уравновешаны\n"
        "           С̲и̲л̲а̲ – это количественная характеристика действия одного тела на другое. F - сила, [Н] (векторная величина)\n"
        "           | Сила может определяться:\n"
        "               1. Модулем;\n"
        "               2. Направлением;\n"
        "               3. Точкой приложения.\n"
        "           Прибор для измерения силы - динамометр.\n"
        "       ❷. Ускорение тела прямопропорциально действующей на него силе и обратно пропорциональна его массе. \n a=F/m, F=ma\n"
        "       ❸. Тела взаимодействуют с силами, равными по величине и направленными вдоль одной прямой в противположные стороны\n F₁₂=-F₂₁\n"
        "           | Особенности третьего закона: \n"
        "               1. Выполняется для сил любой природы;\n"
        "               2. Сила действия и противодействия появляются только парами;\n"
        "               3. Силы действия и противодействия всегда одной природы;\n"
        "               4. Так как силы действия и противодействия приложены к разным телам, их нельзя складывать.\n"
        " \n"
        " Плотность вещества: ρ = m/V, [кг/м³]\n"
        " \n"
        "                              Закон всемирного тяготения\n"
        "                                      Силы в природе\n"
        "                            Принцип относительности Галилея\n"
        "  Принцип относительности Галилея состоит в том, что все механические процессы, явления протекают одинаково в инерциальных системах отсчета.\n"
        "  Закон всемирного тяготения: G=6,67*10⁻¹¹Н*м²/кг²\n"
        "                               "
        )
        zktg1 = PhotoImage(file="./image/./image/zktg1.png")
        text_block.image_create(END,image=zktg1)
        text_block.insert(END,
        " \n "
        "                                      Силы в природе\n"
        "       ❶. Сила тяжести – это сила, с которой планета притягивает тела вблизи нее.\n"
        "                               ")
        powertz = PhotoImage(file="./image/./image/powertz.png")
        text_block.image_create(END,image=powertz)
        text_block.insert(END,
        "\n           G не зависит от массы и по мере удаления уменьшается.\n"
        "           Ускорение свободного падения на полосе больше, чем на экваторе.\n"
        "               F = mg. Сила направлена к центу Земли и приложена к центру тела.\n"
        "       ❷. Сила упругости – сила, возникающая при деформации тела и противодействующая этой деформации.\n"
        "           | Закон Гука: При упругой деформации, растяжении (или сжатии), модуль силы упругости прямо пропорционален абсолютному значению изменения длины тела.\n"
        "               F = kΔx, где k - коэффициент жесткости, а Δx - деформация пружчины\n"
        "           | Виды силы упругости: \n"
        "               1. Сила реакции опоры (N) – возникает в опоре тогда, когда тело деформирует её, притягиваясь к Земле. Направлена вверх и приложена к опоре.\n"
        "               2. Вес (P) – сила, с которой тело действует на опору или подвес вследствие тяготения к Земле. Направлен вниз и приложен к опоре.\n"
        "                   P=m∙(g-a)=N – (Вес всегда равен силе реакции опоры) вес тела, опускающегося с ускорением или поднимающегося с замедлением.\n"
        "                   P=N=m∙(g+a) – вес тела, поднимающегося с ускорением или опускающегося с замедлением.\n"
        "               3. 	Сила нормального давления (Fg) – действует на наклонную плоскость со стороны тела, притягивающегося к Земле. Направлена по нормали (перпендикулярно) к поверхности и приложена к телу.\n"
        "               4. 	Сила натяжения нити (T) – возникает в нити при её растяжении под влиянием тела, тяготеющего к Земле. Приложена к телу.\n"
        "               5. 	Архимедова сила (Fa)– это сила, которая возникает в жидкости или газе при их сжатии телом, тяготеющем к Земле. Приложена к телу, и является ответной реакцией жидкости (газа) на силу нормального давления (вес тела).\n"
        "                       Fa = ρVg\n"
        "       ❸. Сила трения – сила, возникающая в месте соприкосновения тел и препятствует их относительному перемещению. Направлена противоположено направлению движения.\n"
        "           | Виды Fтр:\n"
        "               1. 	Сила трения покоя – сила, препятствующая движению одного тела по поверхности другого.\n"
        "                   Fтр=µ*N – сила реакции опоры, где µ - коэффициент трения покоя\n"
        "               2.	Трение скольжения – трение, характеризующийся относительным перемещением соприкасающихся тел.\n"
        "                   F=µ*N\n"
        "               3. Сила трения качения - действует на колеса, катки и т.д.\n"
        "               4.Жидкое трение – возникает при движении в жидкостях или газах.\n"
        "                   Fm=kV – при малых скоростях. \n "
        "                   Fm=kV^2 - при больших скоростях. \n"
        "                   k – Коэффициент сопротивления (зависит от вязкости, размеров и формы тела\n"
        )
        text_block.pack(anchor=NW)
        text_block.configure(state=DISABLED)
        text_block.mainloop()   
    elif selection == "Глава III. Импульс. Закон сохранения импульса":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert("1.0", " И̲м̲п̲у̲л̲ь̲с̲ – это физическая величина, численно равная произведению массы тела на его скорость (количество движения).\n"
        " З̲а̲м̲к̲н̲у̲т̲а̲я̲ с̲и̲с̲т̲е̲м̲а̲ - это система, в которй тела взаимодействуют только между собой и не взаимодействуют с внешними силами.\n"
        " В̲н̲у̲т̲р̲е̲н̲н̲и̲е̲ с̲и̲л̲ы̲ - это силы взаимодействие тел друг с другом.\n"
        "                               ")
        impuls = PhotoImage(file="./image/./image/impuls.png")
        text_block.image_create(END,image=impuls)
        text_block.insert(END,"\n\n                                       Закон сохранения импульса\n"
        "Суммарный импульс замкнутой системы до взаимодействия равен суммарному импульсу системы после взаимодействия.\n")
        impulszk = PhotoImage(file="./image/./image/impulszk.png")
        text_block.image_create(END,image=impulszk)
        text_block.insert(END, 
        "\n         | Виды ударов: \n"
        "               • Абсолютно упругий удар – это такой удар, при котором тела после взаимодействия движутся с разными скоростями в разные стороны.\n"
        "                               ")
        fightydarim = PhotoImage(file="./image/./image/fightydarim.png")
        text_block.image_create(END,image=fightydarim)
        text_block.insert(END, 
        "\n               • Абсолютно неупругий удар – это удар, при котором тела после взаимодействия движутся в одну и ту же сторону, с одной и той же скоростью.\n"
        "                               ")
        fightydarim1 = PhotoImage(file="./image/./image/fightydarim2.png")
        text_block.image_create(END,image=fightydarim1)
        text_block.pack(anchor=NW)
        text_block.insert(END,"\n\n                                       Рективное движение\n"
        " Реактивное движение – это такой вид механического движения, при котором одна часть системы движется за счет отделения другой ее части.\n")
        reaktiv = PhotoImage(file="./image/./image/reaktiv.png")
        text_block.image_create(END,image=reaktiv)
        text_block.insert(END, 
        "\n\n                                      Работа. Мощность. Энергия.\n"
        "   Работа – это физическая величина, численно равная произведению силы на перемещение и на косинус угла между ними. A - работа, [Дж]\n"
        " A = F*S*cosα \n"
        "       | Примеры расчетов работы: \n                          ")
        primersrabota = PhotoImage(file="./image/./image/primersrabota.png")
        text_block.image_create(END,image=primersrabota)
        text_block.insert(END,"\n   Мощность – это физическая величина, показывающая какую работу тело совершает в единицу времени (быстрота совершения работы). N - мощность, [Вт]\n")
        power1 = PhotoImage(file="./image/./image/power1.png")
        text_block.image_create(END,image=power1)
        text_block.insert(END,
        "   Энергия – это физическая величина, характеризующая способность тела совершать работу. E - энергия, [Дж]\n"
        "       1. Кинетическая энергия – это энергия, которой обладает тело вследствие своего движения. \n                      ")
        imkun = PhotoImage(file="./image/./image/imkun.png")
        text_block.image_create(END,image=imkun)
        text_block.insert(END, 
        "\n       2. Потенциальная энергия – это энергия, обусловленная взаимодействием различных тел, или частей одного тела, или тела с полем.\n")
        impoten = PhotoImage(file="./image/./image/impoten.png")
        text_block.image_create(END,image=impoten)
        text_block.insert(END, 
        "\n\n                                      Закон сохранения энергии\n"
        "   Сумма кинетической и потенциальной энергии называется полной механической энергии системы. Полная механическая энергия замкнутой системы, в которой действуют только силы упругости и тяготения, не изменяются.\n")
        zksaveen = PhotoImage(file="./image/./image/zksaveen.png")
        text_block.image_create(END,image=zksaveen)
        text_block.configure(state=DISABLED)
        text_block.mainloop()   
    elif selection == "Глава IV. Механические колебания и волны":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert("1.0", 
        "\n                                      Колебания\n"
        "   Колебания – это вид механического движения, при котором состояние системы повто-ряется точно или почти точно через определенные промежутки времени.\n"
        "       | Виды колебаний:\n"
        "           1.	Вынужденные – это колебания, происходящие под действием постоянной периоди-ческой силы.\n"
        "           2.	Свободные – это колебания, происходящие под действием внутренних сил системы и затухающие со временем.\n"
        "           3.	Автоколебания – это колебания, происходящие под действием внешнего источника энергии.\n "
        "\n                                      Основные характеристики колебаний\n"
        "   1.	Амплитуда - это максимальное отклонение от положения равновесия. A - амплитуда, [м]\n"
        "   2. 	Период – это время одного полного колебания. T = t/N, [c]\n"
        "   3.	Частота – это число колебаний за единицу времени. ν = N/t = 1/t, [Гц]\n"
        "	4. Циклическая частота – это число колебаний, совершаемых телом за 2π секунд. ω = 2π/T = 2πν. [Рад/с]\n"
        "\n                                      Гармонические колебания\n"
        "   Гармонические колебания – это колебания, которые подчиняются законом синуса или косинуса.\n"
        "   x = Acos(ωt+φ_0) |  x=Asin⁡(ωt+φ_0). φ_0 - начальная среда.\n"
        "\n                                             Волны\n"
        "   Волны – это возмущение в пространстве, распространяющиеся в упругой среде.\n"
        "       | Виды волн: \n"
        "           1)	Поперечная волна – это волна у которой характеризующая ее векторная величина лежит в плоскости перпендикулярной направлению распространению волны.\n"
        "           2)	 Продольная волна – это волна у которой характеризующая ее векторная величина совпадает с направлению распространения. \n          ")
        volna = PhotoImage(file="./image/./image/volna.png")
        text_block.image_create(END,image=volna)
        text_block.insert(END,"\n   Длина волны – это наименьшее расстояние между точками среды, которые совершают колебания в фазе.\n                     ")
        dlinavolni = PhotoImage(file="./image/./image/dlinavolni.png")
        text_block.image_create(END,image=dlinavolni)
        text_block.insert(END, 
        "\n\n                                      Виды маятников:\n"
        "   1. Математический - это тело, небольших размеров, подвешанное на тонкой, нерастяжимой нити, масссы которого можно пренебречь\n              "
        )
        formulagyge = PhotoImage(file="./image/./image/formulagyge.png")
        text_block.image_create(END,image=formulagyge)
        text_block.insert(END,
        "\n"
        "   2. Пружинный - это колебательная система, которая состоит из материальной точки и пружины\n             ")
        pryzformula = PhotoImage(file="./image/./image/pryzformula.png")
        text_block.image_create(END,image=pryzformula)
        tablmayat = PhotoImage(file="./image/./image/tablmayat.png")
        text_block.image_create(END,image=tablmayat)
        text_block.insert(END, 
        "\n\n                                      Резонанс\n"
        "   Резонанс - это явление резкого возрастания амплитуды колебаний при совпадении собственной частоты системы с частотой внешней периодической системы.\n"
        "       | Пример: 	\n"
        "           •	Солдаты на мосту;\n"
        "           •	Дребезжание стекол в окнах домов;\n"
        "           •	Вибрация деталей транспорта;\n"
        "           •	Звучание струнных и звуковых инструментов.\n"
        " Увеличение амплитуды — это лишь следствие резонанса, а причина — совпадение внешней (возбуждающей) частоты с внутренней (собственной) частотой колебательной сис-темы. При помощи явления резонанса можно выделить и/или усилить даже весьма слабые периодические колебания. Резонанс — явление, заключающееся в том, что при некоторой частоте вынуждающей силы колебательная система оказывается особенно отзывчивой на действие этой силы. Степень отзывчивости в теории колебаний описывается величиной, называемой добротность. \n"
        " Явление резонанса впервые было описано Галилео Галилеем в 1602 году в работах, посвященных исследованию маятников и музыкальных струн.\n"
        "       | Виды резонанса:\n"
        "           • механический и акустический;\n"
        "           • электрический;\n"
        "           • оптический;\n"
        "           • орбитальные колебания;\n"
        "           • атомный, частичный и молекулярный.\n"
        "\n\n                                      Звук\n"
        "   Звук - это вид продольных механических колебаний с частотами от 16 до 20000 Гц.\n"
        "   Ультразвук – звуковые волны, имеющие частоту выше воспринимаемой человеческим ухом, обычно под ультразвуком понимают частоты выше 20000 Гц.\n"
        "   Некоторые животные пользуются ультразвуковыми волнами для обнаружения препятствий, ориентировки в пространстве и общения (дельфины, летучие мыши, грызуны).\n"
        "   Инфразвук -  звуковые волны, имеющие частоту ниже,  воспринимаемой человеческим ухом. Обычно под инфразвуком понимают частоту от 0,001 Гц до 16 Гц.\n"
        "   При помощи инфразвука общаются между собой киты и слоны.\n"
        "                                      Шум\n"
        "   Децибел – логарифмическая единица уровней затуханий и усилений.\n"
        "       |Приборы для измерения шума:\n"
        "           1) Фонометр – это приборы, в которых измеряемый звук или шум сравниваются с чис-лом точно определимой частоты, возбуждаемым специальным генератором.\n"
        "           2) Шумомеры – это приборы, в которых шум воспринимается с помощью широкополосных микрофона, который преобразует звуковые колебания в электрические.\n"
        "                           Объективные и субъективные характеристики звука\n"
        "   1) Субъективные характеристики звука - характеристики, зависящие от свойств приемника:\n"
        "       - громкость. Громкость звука определяется амплитудой колебаний в звуковой волне;\n"
        "       - тон (высота тона). Определяется частотой колебаний;\n"
        "       - тембр (окраска звука);\n"
        "   2) Объективные характеристики звука - характеристики, не зависящие от свойств при-емника:\n"
        "       - интенсивность (сила звука) - энергия, проносимая звуковой волной за единицу време-ни через единицу площади, установленной перпендикулярно волне звука;\n"
        "       - частота основного тона;\n"
        "       - спектр звука - количество обертонов;\n"
        )
        text_block.configure(state=DISABLED)
        text_block.pack(anchor=NW)
        text_block.mainloop()   
    elif selection == "Глава V. Агрегатные состояния вещества":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert("1.0",
        "   В природе существуют три агрегатных состояния вещества - твердое, жидкое и газообразное.\n"
        "   Газ расширяется, пока не заполнит весь отведенный ему объем. Если увеличить или уменьшить объем сосуда, молекулы равномерно перераспределятся в новом объеме. \n"
        "   Жидкость при заданной температуре занимает фиксированный объем, однако и она принимает форму заполняемого сосуда — но только ниже уровня ее поверхности.\n"
        "   Твердое тело имеет собственную форму, не растекается по объему контейнера и не принимает его форму. \n"
        "   Имеется и четвертое состояние, которые физики склонны относить к числу агрегатных. Это плазменное состояние. Плазма характеризуется частичным или полным срывом электронов с их атомных орбит, при этом сами свободные электроны остаются внутри вещества.\n                              "
        )
        vesh1 = PhotoImage(file="./image/./image/vesh.png")
        text_block.image_create(END,image=vesh1)
        perehod = PhotoImage(file="./image/./image/perehod.png")
        text_block.image_create(END,image=perehod)
        text_block.insert(END,
        "\n\n                                      Изоморфизм и полиморфизм\n"
        "   Многие кристаллические вещества имеют одинаковые структуры. В то же время одно и то же вещество может образовывать разные кристаллические структуры. Это находит отражение в явлениях изоморфизма и полиморфизма.\n"
        "   Изоморфизм заключается в способности атомов, ионов или молекул замещать друг друга в кристаллических структурах. Изоморфизм широко распространен в природе.\n"
        "   Полиморфизм - способность твердых веществ и жидких кристаллов существовать в двух или нескольких формах с различной кристаллической структурой и свойствами при одном и том же химическом составе. \n"
        "   Переход одной полиморфной модификации в другую называется полиморфными превращениями. Эти переходы происходят при изменении температуры или давления и сопровождаются скачкообразным изменением свойств.\n"
        "\n\n                       Основные агрегатные состояния вещества\n                                      Твердое тело\n"
        "   По своим физическим свойствам и молекулярной структуре твердые тела разделяются на два класса – аморфные и кристаллические.\n"
        "   Кристаллические – это твердые тела, атомы или молекулы которых занимают упорядоченные положения в пространстве. Частицы кристаллических тел образуют в пространстве правильную кристаллическую пространственную решетку.\n"
        "       В природе существуют также:\n"
        "         а) Монокристаллы – это одиночные однородные кристаллы, имеющие форму пра-вильных многоугольников и обладающие непрерывной кристаллической решеткой\n"
        "         б) Поликристаллы – это кристаллические тела, сросшиеся из мелких, хаотически рас-положенных кристаллов.\n"
        "   Аморфные тела не имеют строгого порядка в расположении атомов и молекул (стек-ло, смола, янтарь, канифоль).\n "
        "       - у аморфных тел нет кристаллической решетки, у них обнаружен только ближний порядок в расположении молекул. \n"
        "       - аморфное тело обладает слабо выраженной текучестью. Она связана с перескоками молекул из одного положения равновесия в другое.\n"
        "       - нет определенной температуры плавления.\n"
        "       - изотропны, т.е. их физические свойства по всем направлениям одинаковы.\n"
        "       - внутренняя энергия вещества в аморфном состоянии больше, чем в кристаллическом. \n"
        "\n\n                                   Жидкость\n"
        "   Жидкостью называется физическое тело, обладающее свойством текучести, т. е. не имеющее способности самостоятельно сохранять свою форму. \n"
        "   Жидкости, делятся на два класса: сжимаемые жидкости или газы, почти несжимаемые — капельные жидкости. \n"
        "   Существуют реальные и идеальные жидкости. Идеальной называется такая жидкость, между частицами которой отсутствуют силы внутреннего трения. Вследствие этого она не сопротивляется касательным силам сдвига и силам растяжения. Идеальная жидкость совершенно не сжимается — она оказывает бесконечно большое сопротивление силам сжатия. Такой жидкости в природе не существует - это научная абстракция. Тройная точка определяется значением температуры и давления, при котором вещество может равномерно находиться в трех агрегатных состояниях вещества одновременно.\n"
        "   Критическая точка – температура при которой газ, невозможно сконденсировать ни при каком давлении.\n"
        "       | Свойства жидкостей:\n"
        "          1) Поверхностное натяжение. Силой поверхностного натяжения называют силу, которая действует вдоль поверхности жидкости перпендикулярно к линии, ограничивающей эту поверхность, и стремится сократить ее до минимума.\n"
        "          2) Вязкость - свойство жидкости оказывать сопротивление относительному движе-нию (сдвигу) частиц жидкости. Силы, возникающие в результате скольжения слоев жидко-сти, называют силами внутреннего трения или силами вязкости.\n"
        "          3) Смачивание - это поверхностное явление, которое заключается в взаимодействии поверхности твёрдого тела (другой жидкости) с жидкостью. \n"
        "          4) Капиллярность - заключается в том, что жидкость может изменять уровень в трубках, а так же узких каналах, которые имеют произвольную форму, в простых телах. Поднимается жидкость при методе смачивания каналов жидкостями.  \n"
        )
        kapular = PhotoImage(file="./image/./image/kapular.png")
        text_block.image_create(END,image=kapular)
        text_block.insert(END,
        "\n\n                                 Газы и плазма\n"
        "   Под газообразным состоянием вещества понимается такое его состояние, которое ха-рактеризуется значительной подвижностью частиц.\n"
        "   Плазма - частично или полностью ионизованный газ, который в равновесном состоянии обычно возникает при высокой температуре, от нескольких тысяч кельвинов и выше. В земных условиях плазма образуется в газовых разрядах. \n"
        "\n\n                         Насыщенный и ненасыщенный пар\n"
        "   Пар, находящийся в состоянии динамического равновесия со своей жидкостью, называется насыщенным паром. \n  Пар, который не находится в состоянии динамического равновесия со своей жидкостью, называется ненасыщенным."
        "\n      | Свойства насыщенных паров:\n"
        "       1. Плотность и давление насыщенного пара при данной температуре — это максимальные плотность и давление, которые может иметь пар при данной температуре;\n"
        "       2. Плотность и давление насыщенного пара зависят от рода вещества. Чем меньше удельная теплота парообразования жидкости, тем быстрее она испаряется и тем больше давление и плотность ее паров;\n"
        "       3. Давление и плотность насыщенного пара однозначно определяются его температурой (не зависят от того, каким образом пар достиг этой температуры: при нагревании или при охлаждении);\n"
        "       4. Давление и плотность пара быстро возрастают с увеличением температуры; \n"
        "       5. При постоянной температуре давление и плотность насыщенного пара не зависят от объема. \n"
        "   Насыщенный пар – это пар, который находится в термодинамическом равновесии со своей жидкостью (число молекул, покинувших  жидкость,  равна числу молекул, возвратившихся в жидкость).\n"
        "   Точка росы – температура, при которой пар, находившийся в воздухе, становится насыщенным.\n"
        "   Абсолютная влажность воздуха (ρ) показывает плотность водяного пара.\n"
        "   Относительной влажностью воздуха (φ) называют отношение абсолютной влажности (ρ) к плотности ρ_0 насыщенного водяного пара при той же температуре, выраженной в процентах.\n"
        )
        otnosvl = PhotoImage(file="./image/otnosvl.png")
        text_block.image_create(END,image=otnosvl)
        text_block.insert(END, 
        "\n   Психрометр - это измерительный прибор, применяемый для определения температуры и влажности воздуха.\n"
        "                               Виды психрометров\n"
        "   • Станционарный - психрометр Августа, либо классический психрометр. Состоит из двух термометров, резервуар одного из них обвязан кусочком ткани, конец которого помещен в стаканчик c водой, для обеспечения поступления воды к резервуару; \n"
        "   • Аспирационный психрометр - психрометр Асмана, сложно сконструированный прибор;\n"
        "   • Дистанционный - промышленный тип, где используются термопары и термисторы.\n"
        " Коэффициент поверхностного натяжения – это физическая величина, характеризующая данную жидкость и численно равна отношению поверхностной энергии к площади свободной поверхности жидкости. \n                     σ = W\S, \n                       где σ - коэффициент поверхностного натяжения [Дж/м²], \n                       W - поверхностная энергия жидкости [Дж], \n                       S - площадь свободной поверхности [м²]\n"
        "   Коэффициент поверхностного натяжения зависит от:\n"
        "    • природы жидкости;\n"
        "    • температуры жидкости;\n"
        "    • свойств газа, который граничит с данной жидкостью;\n"
        "    • наличия поверхностно-активных веществ (мыло или стиральный порошок), уменьшающие поверхностное натяжение\n"
        "\n\n                       Микроскоп. Его виды, части и методы работы с ним.\n"
        "  Основными частями микроскопа являются окуляр, тубус, винты, штатив, зеркало, предметный столик и объетив. \n"
        "  Существуют четыре метода работы с микроскопом: \n"
        """   
            1. Метод светлого поля в проходящем свете подходит для изучения прозрачных объектов с неоднородными включениями;
            2. Метод светлого поля светлого поля в отражении свете используется для изучения непрозрачных объектов;
            3 и 4. Метод косого освещения и метод темного поля - это методы для исследования образцов с очень низким контрастом, например, практически прозрачных живых клеток.
        """
        """
                                Виды современных микроскопов
            • Оптический микроскоп - часто встречается в классах и дома.
            • Электронный микроскоп - используетяся для изучение ультраструктуры разных органических объектов и биологических образцов. 
            • Зондовый микроскоп - используется в клеточной и молекулярной биологии и физики твердого тела.
            • Рентгеновский микроскоп - используется для анализа структуры тканей и образцов биопсии.

        Окуляр - элемент оптический системы, обращенный к глазу наблюдателя, чтобы рассмотреть изображение формируемого объективом.
        Объектив - оптическая система, являющаяся частью оптического прибора, обращённая к объекту наблюдения или съёмки и формирующая его действительное или мнимое изображение.                        
        """

        )
        text_block.configure(state=DISABLED)
        text_block.pack(anchor=NW)
        text_block.mainloop()   
    elif selection == "Глава VI. Молекулярно-кинетическая теория":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert("1.0",
        """
          МКТ – учение о строении и свойствах вещества на основе представлении о существо-вании атомов и молекул, как наименьших частиц химического вещества.
                                            Основные сведение о веществе
          Атом – это частица вещества микроскопических размеров и массы, наименьшая часть химического элемента, являющаяся носителем его свойств.
          Ион – одноатомная или многоатомная электрически заряженная частица вещества, образующаяся в результате потери или присоединения атомов в составе молекулы одного или нескольких электронов.
          Молекула – это микрочастица, образованная из двух или более атомов и способная к самостоятельному существованию.
             | Доказательства дискретности вещества:
                1.	Диффузия – это явление взаимного проникновения молекул одного вещества между молекулами другого (происходит во всех агрегатных состояниях). 
                2.	Броуновское движение – это движение малых частиц в жидкости или газе под ударами его молекул.
             | Основные положения МКТ:
                1.	Все вещества состоят из молекул и атомов.
                2.	Молекулы и атомы всех веществ находятся в постоянном хаотическом движе-нии.
                3.	Между молекулами и атомами существуют силы притяжения и отталкивания.
          Идеальный газ – это макроскопическая система, которая состоит из огромного числа микрочастиц и удовлетворяет следующим условиям:
                1.	Взаимодействие между молекулами пренебрежительно мало;
                2.	Молекулы – абсолютно твердые шарики, сталкивающиеся абсолютно упруго;
                3.	Время свободного пробега молекул во много раз превосходит время их соударений;
          Важнейшими понятиями МКТ идеальных газов являются температура, давление и объем;
          Относительная молекулярная масса (Mr) - это отношение массы одной молекулы к 1/12 массы молекулы углерода.
          Моль – количества вещества, в котором содержится столько же сколько в 12г углерода.
            ν - кол-во вещества, [моль]
        """
        )
        mol = PhotoImage(file="./image/mol.png")
        text_block.image_create(END,image=mol)
        text_block.insert(END,
        """
                            Основное уравнение МКТ.
                        Уравнение Мендеелева-Клайперона
        """)
        yrmkt = PhotoImage(file="./image/mktyr.png")
        text_block.image_create(END,image=yrmkt)
        text_block.insert(END, 
        """
                                Изопроцессы
          Изопроцессы – это равновесные процессы, в которых один из основных параметров сохраняется (температура, давление или объем).
          1) Изотермический процесс. T = const, m = const. Закон Бойля-Мариотта: p₁V₁=p₂V₂
          2) Изобарный процесс. p = const, m = const. Закон Гей-Люссака: V₁/T₁=V₂/T₂
          3) Изохорный процесс. V = const, m = const. Закон Шарля: p₁/T₁=p₂/T₂
        """
        )
        izoproc = PhotoImage(file="./image/izoproc.png")
        text_block.image_create(END,image=izoproc)
        text_block.insert(END,
        "\n  4) Адиабатический процесс – это процесс, который происходит без теплообмена с окружающей средой.\n"
        "  5) Политропический процесс – это процесс, при котором теплоёмкость газа остается постоянной."
        )
        text_block.configure(state=DISABLED)
        text_block.pack(anchor=NW)
        text_block.mainloop()   
    if selection == "Глава VII. Элементы термодинамики":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert(END, 
        """
          Термодинамика – теория тепловых процессов, в которой не учитывается молекулярное строение тел. В её основе лежит понятие "внутренняя энергия".
          Внутрення энергия тела – это сумма кинетических энергий всех молекул и потенциальных энергий взаимодействия молекул друг с другом.
                U = ΣЕк + ΣЕр = const, [U] - внутренняя энергия, [Дж]
          Число степеней свободы (i) – число возможных назвисимых направлений движения молекул. Если молекула содержит два или более атома, то помимо поступального движения, молекула также может совершать вращательные и колебательные движения.
          i=3 - одноатомный газ (He), i=5 - двухатомный газ (O₂,H₂), i=6 - трехатомный газ (CO₂)
        """)
        energyigit = PhotoImage(file="./image/energyidit.png")
        text_block.image_create(END,image=energyigit)
        text_block.insert(END,
        """
            Существуют два способа изменения работы:
             1) совершение работы: если работа совершается над телом, его U увеличивается. Если работу совершает само тело, его U уменьшается.
             2) Теплообмен. Процесс передачи энергии от одного тела к другому без совершения работы.
                                Работа газа в термодинамике.
                Газ, расширяясь, может совершать работу. 
                Работа газа: A = pSΔh = pS(h₂-h₁) или A = pΔV = νRΔT           
                    S - площадь поршня, Δh - перемещение.
                Работа в термодинамике – это процесс изменения энергии системы, связанный с перемещением её частей относительно друг друга.
                    A = pΔV - работа газа, Авн = -А - работа над газом (внешних сил).         
        """
        )
        rabotatermdunamic = PhotoImage(file="./image/rabotatermdunamic.png")
        text_block.image_create(END,image=rabotatermdunamic)
        text_block.insert(END,
        """

                                    Количество теплоты
            Количество теплоты (Q) – количественная мера изменения внутренней энергии при теплообмене.
            Если внутренняя энергия тела увеличивается, то говорят, что тело получило некоторое количество теплоты Q. Если внутренняя энергия уменьшается, то говорят, что тело отдает некоторое количество теплоты.
            Формула количества теплоты: Q = cm∆T - нагревание (охлаждение), где c - удельная теплоемкость вещества [Дж/кг*К]
            Уравнение теплового баланса: c₁m₁∆T₁+c₂m₂∆T₂+c₃m₃+∆T₃ + ... = 0
            Q = λm - плавление (отвердевание), где λ - удельная теплота плавления, [Дж/кг]
            Q = Lm - парообразование (конденсация), где L - удельная теплота парообразования [Дж/кг]
            Q = qm - сгорание топлива, где q - удельная теплота сгорания, [Дж/кг]
                                    
                                    Первый закон термодинамики
            Изменение внутренней энергии системы при переходе ее из одного состояния в другое равно сумме работы внешних сил и количеству теплоты, переданного системе.
                ΔU = Q + Авн
                 ∆U - Изменение внутренней энергии
                 Aвн – Работа внешних сил
                 Q – Количество теплоты, переданного газом
             Если работу совершает система, а не внешние силы: Q = ΔU + А. 
        """)
        zakonterm1 = PhotoImage(file="./image/1zakonterm.png")
        text_block.image_create(END,image=zakonterm1)
        text_block.insert(END, 
        """
        \n Закон термодинамики утверждает, что нельзя построить вечный двигатель первого рода, т.е. такую периодически действующую машину, которая совершала бы работу без потребления энергии извне.

                                    Второй закон термодинамики
            (!) Невозможно передать тепло от холодного тела к горячему без изменения в них или в окружающих телах.
            Обратимыми процессами называют процессы перехода системы из одного состояния в другое, которые можно провести в обратном направлении.
            Необратимыми называют процессы, которые могут протекать только в одном направлении. 
            (!) Невозможно создать двигатель, который полностью превращал бы теплоту в механическую работу.

                                    Тепловой двигатель
            Тепловой двигатель – это устройство, которое совершает механическую работу за счет внутренней энергии.                                                       
        """
        )
        tepldvig = PhotoImage(file="./image/tepldvig.png")
        text_block.image_create(END,image=tepldvig)
        text_block.insert(END, 
        "\n Коэффициент полезного действия (КПД) -  характеристика эффективности системы (устройства, машины) в отношении преобразования или передачи энергии. "
        )
        kpd = PhotoImage(file="./image/kpd.png")
        text_block.image_create(END,image=kpd)
        text_block.insert(END,"\n Цикл Карно - цикл двигателя, состоящий из двух изотерм и двух адиабат \n")
        cyclekarno = PhotoImage(file="./image/cyclekarno.png")
        text_block.image_create(END,image=cyclekarno)
        text_block.configure(state=DISABLED)
        text_block.pack(anchor=NW)
        text_block.mainloop()   
    if selection == "Глава VIII. Электростатика и её элементы":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert("1.0",
        """
          Электростатика – наука о неподвижных зарядах и связанных с ними неизменяющихся электрических полях.
          Электрический заряд – физическая величина, определяющая электромагнитное взаимодействие. q - заряд, [Кл]
          Элементарный заряд - это минимальный значение электрического заряда, которое определяется величиной заряда электрона.
            e - элементарный заряд. e = 1.6*10⁻¹⁹ Кл, mₑ= 9,1*10⁻³¹ кг
          Точечный заряд – это заряженное тело, размерами которого можно пренебречь по сравнению c расстояниями от него до других тел.
            Виды зарядов: положительные (протоны и ионы) и отрицательные (электроны)
                Заряды с одинаковыми знаками - отталкиваются, а с разными - притягиваются.
        """
        )
        vzaimelzar = PhotoImage(file="./image/vzaimelzar.png")
        text_block.image_create(END,image=vzaimelzar)
        text_block.insert(END,
        """\n
          Электролизация - процесс перераспределия зарядов, при котором электроны от одного тела переходят к другому и электрически нейтральные тела становятся заряженными.
           Виды электролизации: 1) Трение; 2) Контакт; 3) Влияние.
          Закон электростатики: q₁+q₂+...+qₙ = const
          | Закон Кулона: 
            Два неподвижных точечных заряда отталкивают или притягивают друг друга с силой, пропорциональной произведению модулей зарядов и обратно пропорционально квадрату расстояния между ними и направленной вдоль приямой, соединяющей эти заряды.
        """
        )
        zkkylon = PhotoImage(file="./image/zkkylon.png")
        text_block.image_create(END,image=zkkylon)
        text_block.insert(END,
        """\n
                                                    Электрическое поле - 
            это особый вид материи, который не фиксируется человеческими органами чувств, су-ществующий вокруг любого электрического заряда и проявляющий себя в действии на дру-гие заряды.
            | Свойства:
                •	Создается электрическими зарядами;
                •	Действует на электрические заряды.
          Электростатическое поле – электрическое поле неподвижных зарядов. Оно не меняется со временем. Оно существует в пространстве и неразрывно с ним связанно.
          Напряженность – это силовая характеристика электрического поля. E - напряженность, [Н/Кл] или [В/м]
            | Напряженность обычного заряда: E = F/q
            | Напряженность точечного заряда: E = k*q₀/R². q₀ - точечный заряд. R - расстояние от точечного заряда до точки, в которой определяется напряженность
          На положительный заряд, внесенный в поле, действует сила, направленная в ту же сторону, что и напряженность поля. Значит, напряженность поля создаваемая положительным зарядом, направлена от него, отрицательным зарядом к нему.

                                Силовые линии
          – это непрерывные линии, касательные к которым в каждой точке, через которую они проходят, совпадают с напряженностью.
            | Свойства: 1) Силовые линии не замкнуты; 2) Силовые линии не пересекаются.\n
        """)
        silline = PhotoImage(file="./image/silline.png")
        text_block.image_create(END,image=silline)
        text_block.insert(END,
        """\n
                            Работа. Энергия. Потенциал. Напряжение               
          На любой заряд действует электрическое поле, созданное другими зарядами. При перемещении заряда, действующее на него со стороны, сила, совершает работу (работа поля)
          Работа поля: A = qE(d₁-d₂). d₁ - расстояние от заряда до пластины было; d₂ - расстояние от заряда до пластины стало.         
            A = -(Wp₁-Wp₂) = -ΔWp \n
                            Потенциальная энергия
            •  Взаимодействие заряда с полем: Wp = qEd
            •  Взаимодействие точечных зарядов: Wp = k*q₁-q₂/R\n
                                Потенциал
          – скалярная характеристика электрического поля, характеризующая потенциальную энергию, которой обладает единичный положительный пробный заряд, помещенный в данную точку поля.
              φ - потенциал, [В]. φ = Wp/q
              Потенциал заряда в среде: φ = k*q₀/R\n
                                Напряжение
          – величина, численно равная работе по перемещению единицы электрического заряда между двумя произвольными точками электрической цепи. Напряжение также разность потенциалов. 
            U - напряжение, [В]. U = φ₁-φ₂. U = A/q. U = EΔd       
            Работа по перемещению заряда: A = q(φ₁-φ₂) = qU
          Эквипотенциальные поверхности - совокупность точек, которые имеют одинаковый потенциал.\n
                        Электрическая ёмкость. Конденсатор
          Конденсатор – устройство, предназначенное для накопления заряда и энергии электрического поля.                                                                  
        """)
        ystrplcon = PhotoImage(file="./image/ystrplcon.png")
        text_block.image_create(END,image=ystrplcon)
        text_block.insert(END,"\n\n Под зарядом конденсатора понимают модуль заряда из одной его обкладки: q = C*U\n\n")
        naprmezd = PhotoImage(file="./image/naprmezd.png")
        text_block.image_create(END,image=naprmezd)
        text_block.insert(END, 
        """\n
            Электроёмкостью конденсатора называют физическую величину, равную отношению заряда к разности потенциалов между его обкладками. 
                C = q/U, [Ф]. q = C*(φ₁-φ₂), q - заряд конденсатора. 1 Фарад (Ф) = 1Кл/1В
          Ёмкость конденсатора тем больше, чем больше площадь его обкладок и чем ближе друг к другу они расположены. 
          Электроёмкость плоского конденсатора: C = ε*ε₀*S/d. 
            ε - диэлектрическая проницаемость диэлектрика, 
            ε₀ - электрическая постоянная
            S - площадь одной обкладки конденсатора
            d - расстояние между обкладками

            Соединения конденсаторов бывают параллельными, последовательными и смешанными.
        """)
        posledsoed = PhotoImage(file="./image/posledsoed.png")
        paralsoed = PhotoImage(file="./image/paralsoed.png")
        text_block.image_create(END,image=paralsoed)
        text_block.image_create(END,image=posledsoed)
        text_block.insert(END,
        """
                            Энергия заряженного конденсатора
        Напряженность поля, созданного зарядом одной из пластин: E/2
        Заряд одной пластины: q
        Потенциальная заряда в однородном поле: W = q*E*d/2 = q*U/2 = q²/(2*C) = C*U²/2 = C*E²*d²/2
            A = Wₙ₂-Wₙ₁= q*(U₂-U₁)/2                            
        """)
        text_block.configure(state=DISABLED)
        text_block.pack(anchor=NW)
        text_block.mainloop()   
    if selection == "Глава IX. Электродинамика":
        text.config(text="")
        text_block.configure(state=NORMAL)
        text_block.delete("1.0",END)
        text_block.insert(END,
        """
          Электродинамика - это наука о свойствах и закономерностях поведения особого вида материи - электромагнитного поля, осуществляющего взаимодействие между электрически заряженными телами и частицами.
          Электрическим током называют упорядоченное движение заряженных частиц.
            За направление тока принимают направление движения "+" заряженных частиц. 
          Наличие электрического тока:
            1) Нагревание проводников, т.е. тепловое действие;
            2) Возникновение вокруг проводника с током магнитного поля, т.е. магнитные действие;
            3) Разделение некоторых проводников на их химические составляющие, т.е. химическое действие. 
        \n                      Источники электрического тока
          Источник тока – это устройство, в котором происходит преобразование какого-либо вида энергии в электрическую энергию. 
           • Механический (генератор);
           • Тепловой;
           • Световой (солнечная батарея);
           • Химический.
         Сила тока – это заряд, проходящий через заданное сечение проводника за единицу времени.
            I = Δq/Δt, [A]. I - Сила тока.
          Если сила тока со временем не меняется, то ток называют постоянным. 
          Сила тока в проводника зависит от количества свободных зарядов, т.е. от их концентрации и от скорости их движения.
            Связь силы тока с зарядом электрона.
        """)
        svyassilitoka = PhotoImage(file="./image/svyassilitoka.png")
        text_block.image_create(END,image=svyassilitoka)
        text_block.insert(END, 
        """
            S - площадь поперечного сечения проводника
            V = vΔtS, V - объем проводника
                v - средняя скорость упоряденного движения электронов
            N = nvΔtS, n - концентрация электронов, N - число электронов
            q = envΔtS, q - полный заряд. 
            I = envS, I - Сила тока
            Сила, действующая на заряд со стороны электрического поля: F = Eq. F = ma = mΔv/t
            Средняя скорость упорядоченного движения электронов прямо пропорциональна напряженности поля.
            Сила тока в металлическом проводнике прямо пропорциональна напряжению на его концах.
            Условия существования тока таковы: наличие свободных электронов и электрического поля.
        """
        )
        eltokvsredax = PhotoImage(file="./image/eltokvsredax.png")
        text_block.image_create(END,image=eltokvsredax)
        text_block.insert(END,
        """\n
            k - электрохимический эквивалент, [мг/Кл (10⁻⁶кг/Кл)]
            Дырки - квазичастица, носители положительного заряда, равного элементарному заряду в полупроводнике.
        \n
                                                Сопротивление
            – это физическая величина, которая характеризует способность проводника препятствовать прохождению электрического тока. R - сопротивление, [Ом]
            
            Зависимость сопротивления от температуры: R = R₀*(1+αΔt). 
                R₀ - сопротивление до нагрева.
                α - температурный коэффициент сопротивления.
                Δt - изменение температуры.
        \n
                                            Сверхпроводимость
            – это явление отсутствия сопротивления электрического тока при низких температурах.
            Сверхпроводимостью обладают металлы и их сплавы, проводники.
            Сопртивление проводника зависит от материала, из которого изготовлены проводники, его длины и сечения:
                R = ρ-уд*l/S
                ρ-уд - удельное сопротивление проводника.
                l - длина проводника, [м]
                S - площадь сечения, [м²]         
            Удельное сопротивление – это физическая величина, которая показывает каким сопротивлением обладает сделанный из этого вещества проводник единичной длины и площади.
            Электрическая проводимость – это способность веществ пропускать электрический ток под действием электрического напряжения.
            Резистор – проводник с постоянным сопротивлением.
            \n
                                    Закон Ома для участка цепи.
            Сила тока в проводнике прямопропорциональна напряжению и обратно пропорциональна сопротивлению.
                I = U/R
            Сторонние силы - это любые силы не электрического происхождения, которые действуют на электрически заряженные частицы и способны совершать работу по их переносу
            ЭДС (электродвижущая сила) является основной характеристикой источника тока.
                ε - ЭДС, [В]. ε=Асм/q. Aсм - работа сторонних сил.
            \n
                                    Полупроводники. Диэлектрики.
            Полупроводники – вещества, способные, как проводить электрический ток, так и препятствовать его прохождению.
            Используют Кремний (Si) и Германий (Ge).          
               | Свойства полупроводников:        
                Электропроводность проводников сильно зависит от окружающей температуры.
                При очень низкой температуре, близкой к абсолютному нулю (-273°С), полупроводники не проводят электрический ток, а с повышением температуры, их сопротивляемость току уменьшается.   
                Если на полупроводник навести свет, то его электропроводность начинает увеличиваться. Используя это свойство полупроводников, были созданы фотоэлектрические приборы. Также полупроводники способны преобразовывать энергию света в электрический ток, например, солнечные батареи. А при введении в полупроводники примесей определенных веществ, их электропроводность резко увеличивается
               | Свойства атомов полупроводников: 
                Германий и кремний являются основными материалами многих полупроводниковых приборов и имеют во внешних слоях своих оболочек по четыре валентных электрона.
                Атом германия состоит из 32 электронов, а атом кремния из 14. Но только 28 электронов атома: германия и 10 электронов атома кремния, находящиеся во внутренних слоях своих оболочек, прочно удерживаются ядрами и никогда не отрываются от них. Лишь только 4 валентных электрона атомов этих проводников могут стать свободными, да и то не всегда. А если атом полупроводника потеряет хотя бы один электрон, то он становится положительным ионом.     
                В полупроводнике атомы расположены в строгом порядке: каждый атом окружен 4-мя такими же атомами. Причем они расположены так близко друг к другу, что их валентные электроны образуют единые орбиты, проходящие вокруг соседних атомов, тем самым связывая атомы в единое целое вещество.
                Представим взаимосвязь атомов в кристалле полупроводника в виде плоской схемы.\n
        """)
        vzaimporovdnikov = PhotoImage(file="./image/vzaimporovdnikov.png")
        text_block.image_create(END,image=vzaimporovdnikov)
        text_block.insert(END,
        """
        На схеме шарики с плюсом, условно, обозначают ядра атомов (положительные ионы), а маленькие шарики - это валентные электроны.
        Здесь видно, что вокруг каждого атома расположены 4 точно таких же атома, а каждый из этих четырех имеет связь еще с четырьмя другими атомами и т.д. Любой из атомов связан с каждым соседним двухвалентными электронами, причем один электрон свой, а другой заимствован у соседнего атома. Такая связь называется двухэлектронной или ковалентной.
        В свою очередь, внешний слой электронной оболочки каждого атома содержит 8 электронов: 4 своих, и по одному, заимствованных от четырех соседних атомов. Здесь уже не различишь, какой из валентных электронов в атоме «свой», а какой «чужой», так как они сделались общими. При такой связи атомов во всей массе кристалла германия или кремния можно считать, что кристалл полупроводника представляет собой одну большую молекулу.\n
                                    Электропроводность полупроводника
        Рассмотрим упрощенный рисунок кристалла полупроводника, где атомы обозначаются красным шариком с плюсом, а межатомные связи показаны двумя линиями, символизирующими валентные электроны.                                                        

        """)
        elekprov = PhotoImage(file="./image/elekprov.png")
        text_block.image_create(END,image=elekprov)
        text_block.insert(END, 
        """
        При температуре, близкой к абсолютному нулю полупроводник не проводит ток, так как в нем нет свободных электронов. Но с повышением температуры связь валентных электронов с ядрами атомов ослабевает и некоторые из электронов, вследствие теплового движения, могут покидать свои атомы. Вырвавшийся из межатомной связи электрон становится «свободным», а там где он находился до этого, образуется пустое место, которое условно называют дыркой.
        Чем выше температура полупроводника, тем больше в нем становится свободных электронов и дырок. В итоге получается, что образование «дырки» связано с уходом из оболочки атома валентного электрона, а сама дырка становится положительным электрическим зарядом равным отрицательному заряду электрона.\n
                        Явление возникновения тока в полупроводнике
        Если приложить некоторое напряжение к полупроводнику, контакты «+» и «-», то в нем возникнет ток. Вследствие тепловых явлений, в кристалле полупроводника из межатомных связей начнет освобождаться некоторое количество электронов (синие шарики со стрелками).                  
        """)
        yavvoztoka = PhotoImage(file="./image/yavvoztoka.png")
        text_block.image_create(END,image=yavvoztoka)
        text_block.insert(END,
        """
        Электроны, притягиваясь положительным полюсом источника напряжения, будут перемещаться в его сторону, оставляя после себя дырки, которые будут заполняться другими освободившимися электронами. Т.е, под действием внешнего электрического поля носители заряда приобретают некоторую скорость направленного движения и тем самым создают электрический ток.
        Вывод: электроны движутся от отрицательного полюса источника напряжения к положительному, а дырки перемещаются от положительного полюса к отрицательному.\n
            По проводимости полупроводники подразделяют на n-тип и p-тип\n     
        """)
        pryamvkl = PhotoImage(file="./image/pryamvkl.png")
        text_block.image_create(END,image=pryamvkl)
        text_block.insert(END,"""
        Полупроводник п-типа имеет примесную природу и проводит электрический ток подобно металлам. Примесные элементы, которые добавляют в полупроводники для получения полупроводников п-типа, называются донорными. Термин «п-тип» происходит от слова «negative». обозначающего отрицательный заряд, переносимый свободным электроном.\n
        """)
        obrvkl = PhotoImage(file="./image/obrvkl.png")
        text_block.image_create(END,image=obrvkl)
        text_block.insert(END,
        """
        Полупроводник р-типа, кроме примесной основы, характеризуется дырочной природой проводимости. Примеси, которые добавляют в этом случае, называются акцепторными. «p-тип» происходит от слова «positive», обозначающего положительный заряд основных носителей.\n
                                Диэлетрики
        Определение 1: Диэлектрик - вещество, не обладающее способностью проводить электрический ток.
        Определение 2: Если диэлектрик поместить в электрическое поле, то, как диэлектрик, так и само поле значительно изменятся. В диэлектриках, в которых до контакта с полем не было заряда, возникают электрические заряды. Это явление объясняется процессом поляризации вещества, другими словами, в поле диэлектрик обретает электрические полюсы. Возникающие при этом заряды называются поляризационными.
        Определение 3: В процессе поляризации заряды каждой отдельной молекулы диэлектрика смещаются в противоположные ее стороны. Соответственно, одна часть молекулы становиться положительно заряженной, а другой - отрицательно, что, в общем, дает возможность заявить: молекула превращается в электрический диполь.                   
        Определение 4: Существуют такие диэлектрики, в которых в условиях отсутствующего электрического поля молекулы имеют дипольный момент (полярные молекулы).\n
        Пример 1: Если представить плоский конденсатор, который заполнен диэлектриком так, как это проиллюстрировано на рисунке, то на принадлежащей ему левой обкладке расположен положительный заряд, а на правой - отрицательный. По причине того факта, что разноименные заряды притягиваются друг к другу, у положительной обкладки на поверхности диэлектрика появится отрицательный заряд, а у правой, то есть отрицательной - положительный заряд диэлектрика. Выходит, что поле, формирующееся поляризационными зарядами, имеет противоположное направлению поля направление, которое создают обкладки, соответственно, диэлектрик ослабляет поле.
        """)
        primer1duel = PhotoImage(file="./image/primer1duel.png")
        text_block.image_create(END,image=primer1duel)
        text_block.insert(END,"\n+q, - q - представляют собой заряды на обкладках конденсатора. \n E - является напряженностью поля, которое формируется обкладками конденсатора. \n -q', +q' - это заряды диэлектрика. \n E'- напряженность поля, которое создается как результат поляризации диэлектрика. \n Явление влияния вещества на магнитное и электрическое поля было эмпирическим путем открыто Фарадеем. Именно этим ученым было в науку были введены такие термины, как диэлектрик и диэлектрическая постоянная.\n"
        "В случае если однородный изотропный диэлектрик полностью заполняет собой объем, ограниченный эквипотенциальными поверхностями поля сторонних зарядов, то напряженность поля внутри него в Е раз меньше напряженности поля сторонних зарядов.\n")
        duelteor0 = PhotoImage(file="./image/duelteor0.png")
        text_block.image_create(END,image=duelteor0)
        text_block.insert(END,"\nНапряженность поля точечного заряда, который расположен в диэлектрике с некоторой диэлектрической проницаемостью е, может быть выражена в виде следующего выражения:\n                                             ")
        duelteor1 = PhotoImage(file="./image/duelteor1.png")
        text_block.image_create(END,image=duelteor1)
        text_block.insert(END,"\nЗакон Кулона для зарядов, находящихся в жидком и газообразном диэлектрике принимает такой вид:\n                                         ")
        duelteor2 = PhotoImage(file="./image/duelteor2.png")
        text_block.image_create(END,image=duelteor2)
        text_block.configure(state=DISABLED)
        text_block.pack(anchor=NW)
        text_block.mainloop()                   
combobox_lectures = ttk.Combobox(win, values=Lectures, state="readonly",width="45")
combobox_lectures.pack(anchor=N,fill=X)
combobox_lectures.bind("<<ComboboxSelected>>", selectedbox)
text = ttk.Label(win, text="Выберите главу лекции", font=("Times New Roman", 12))
text.pack()

p1 = Text(win,wrap="word",font=("ArialBold", 16))
text_block = ScrolledText(win,wrap="word",font=("Times New Roman", 12),width="60",height="40")

combobox_cat = ttk.Combobox(root, values=Categories, state="readonly",width="45")
combobox_cat.pack(anchor=NW)
combobox_cat.bind("<<ComboboxSelected>>", selectedbox_cat)

root.mainloop()
win.mainloop()