import sympy as sp
q=sp.symbols('q',positive=True); h=q-1/q
a,b,c,d=sp.symbols('a b c d')
R=sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]])
Km=sp.Matrix([[a,b],[c,d]]); I=sp.eye(2); kp=sp.kronecker_product
K1=kp(Km,I)
RE=sp.expand(R*K1*R*K1-K1*R*K1*R)
eqs=[e for e in set(RE) if e!=0]
print(len(eqs)); 
for e in eqs: print(sp.factor(e))
print(sp.solve(eqs,[a,b,c,d],dict=True))
