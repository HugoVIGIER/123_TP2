import math as m

#Fonction:

def Point_Fixe(g, x0, epsilon, Nitermax):
    xold = x0
    xnew = g(xold)
    erreur = g(xold)- xold
    xnew = g(xold)
    n = 1
    while abs(erreur) > epsilon and n < Nitermax :
        n = n + 1
        xnew = g(xold)
        erreur = xnew - xold
        xold = xnew
        print(xnew,n)
    return xnew,n, abs(xnew-xold)


#Question 1:

print("="*25,"Question 1","="*25)

def g1plus(x):
    return (9-3*x)**(1/4)

print(Point_Fixe(g1plus, 3/2, 1e-6, 5e4))

print("="*20)

def g1neg(x):
    return -(9-3*x)**(1/4)

print(Point_Fixe(g1neg, -(3/2), 1e-6, 5e4))



#Question 2:

print("="*25,"Question 2","="*25)


def g2plus(x):
    return m.acos((x+2)/3)

print(Point_Fixe(g2plus, 0.4, 1e-6, 5e4))

print("="*20)

def g2neg(x):
    return m.acos((x+2)/3)*(-1)

print(Point_Fixe(g2neg, -1.4, 1e-6, 5e4))



#Question 3:

print("="*25,"Question 3","="*25)

def g3(x):
    return m.log(7/x)

print(Point_Fixe(g3, 1.4, 1e-6, 5e4))



#Question 4:

print("="*25,"Question 4","="*25)

def g4a(x):
    return m.log(10+x)

print(Point_Fixe(g4a, 2.5, 1e-6, 5e4))

print("="*20)

def g4b(x):
    return m.exp(x)-10

print(Point_Fixe(g4b, -9.5, 1e-6, 5e4))



#Question 5:

print("="*25,"Question 5","="*25)

def g5plus(x):
    return m.atan((x+5)/2)

print(Point_Fixe(g5plus, 1.3, 1e-6, 5e4))



#Question 6:

print("="*25,"Question 6","="*25)

def g6(x):
    return m.log((x**2)+3)

print(Point_Fixe(g6, 1.7, 1e-6, 5e4))



#Question 7:

print("="*25,"Question 7","="*25)

def g7(x):
    return (7+m.log(x)*(-4))/3 

print(Point_Fixe(g7, 1.7, 1e-6, 5e4))



#Question 8:

print("="*25,"Question 8","="*25)

def g8plus(x):
    return ((2*x**2)-4*x+17)**0.25

print(Point_Fixe(g8plus, 1.8, 1e-6, 5e4))

print("="*20)

def g8neg(x):
    return  -((2*x**2)-4*x+17)**0.25

print(Point_Fixe(g8neg, -2.6, 1e-6, 5e4))



#Question 9:

print("="*25,"Question 9","="*25)

def g9(x):
    return m.log(7+2*m.sin(x))

print(Point_Fixe(g9, 2.3, 1e-6, 5e4))



#Question 10:

print("="*25,"Question 10","="*25)

def g10(x):
    return m.log(10/m.log((x**2)+4))

print(Point_Fixe(g10, 1.8, 1e-6, 5e4))




