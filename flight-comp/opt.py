from gpkit import Model, Variable
CDA0 = Variable("CDA0",0.004,"m^2")
e = Variable("e",0.95,"-","span efficiency factor")
tau = Variable("tau",0.11,"-") #t/c
epsilon = Variable("epsilon",0.03,"-") # h/c
W_fuse = Variable("W_fuse",2.7,"N")
rho_foam = Variable("rho_foam",32,"kg/m^3")
E_foam = Variable("E_foam",19.3,"MPa")
T_max = Variable("T_max",0.7,"N")
R = Variable("R",12.5,"m^2")
c_d = Variable("c_d","-","wing profile drag coefficient")
W_pay = Variable("W_pay","N")

L = Variable("L","N")
D = Variable("D","N")
N = Variable("N","-")

constraints = [	D >= N*(W_fuse+W_wing),
				D <= T_max]

m = Model(objective,constraints)
sol = m.solve()
print sol.table()


objective = 1/W_pay