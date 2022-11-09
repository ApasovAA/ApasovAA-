import sympy
import math
t=[[4.703, 4.660, 4.676],
   [4.488, 4.566, 4.539],
   [2.271, 2.156, 2.154]]
t_sr=[]
S_t=[]
kfst=4.303
t_sl=[]
t_sis=0.002
t_ab=[]
t_ot=[]
h=0.4
r=0.044
r_ab=0.002
h_ab=0.0005
m=0.0583
g=9.8
j=[]
j_ot=[]
j_ab=[]
x=sympy.symbols('x')
y=sympy.symbols('y')
z=sympy.symbols('z')
f_d=0
##############################################################################
for i in range(len(t)):
    t_sr.append(sum(t[i])/len(t[i]))
for i in range(len(t_sr)):
    S_t.append(0)
    for k in t[i]:
        S_t[i]+=((t_sr[i]-k)**2)/(len(t[i])-1)
    S_t[i]=S_t[i]**0.5
for i in S_t:
    t_sl.append(kfst*i)
for i in t_sl:
    t_ab.append((i**2+t_sis**2)**0.5)
for i in range(len(t_sr)):
    t_ot.append(t_ab[i]/t_sr[i])
for i in t_sr:
    j.append(m*r**2*(g*i**2/(2*h)-1))
f = sympy.log(m*x**2*(g*y**2/(2*z)-1))
for n in range(len(t_sr)):
    j_ot.append((f.diff(x) * r_ab) ** 2 +
                (f.diff(y) * t_sr[n]) ** 2 +
                (f.diff(z) * h_ab) ** 2)
    f_d = sympy.lambdify(x, j_ot[n])
    j_ot[n]=f_d(r)
    f_d=sympy.lambdify(y, j_ot[n])
    j_ot[n]=f_d(t_sr[n])
    f_d=sympy.lambdify(z, j_ot[n])
    j_ot[n]=float(f_d(h))**0.5
print(j_ot)
#for i in range(len(t_sr)):
#    j_ot.append(((2*r_ab/r)**2+
#                (2*g*t_sr[i]*t_ab[i]/(g*t_sr[i]**2-2*h))**2+
#                (g*t_sr[i]**2*h_ab/(h*(g*t_sr[i]**2-2*h)))**2)**0.5)
for i in range(len(j)):
    j_ab.append(j_ot[i]*j[i])
    print('Момент инерции', i+1, '=', j[i], '+-', j_ab[i])
##############################################################################