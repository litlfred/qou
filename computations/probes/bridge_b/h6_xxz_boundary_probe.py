import sympy as sp
q=sp.symbols('q',positive=True); h=q-1/q
R=sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]); I=sp.eye(2); kp=sp.kronecker_product
e=q*sp.eye(4)-R                     # TL generator (kills the q-eigenspace), up to normalisation
E1=kp(e,I); E2=kp(I,e); H=-2*(E1+E2)
F=sp.Matrix([[0,0],[1,0]]); Ki=sp.diag(1/q,q)
F3=kp(kp(F,I),I)+kp(kp(Ki,F),I)+kp(kp(Ki,Ki),F)
print("sum e_i commutes with F3:", sp.simplify(H*F3-F3*H)==sp.zeros(8))
sz=sp.diag(1,-1); Bd=-(h/2)*(kp(kp(sz,I),I)-kp(kp(I,I),sz))
print("boundary term alone commutes with F3:", sp.simplify(Bd*F3-F3*Bd)==sp.zeros(8))
piv=kp(kp(sp.diag(q,1/q),sp.diag(q,1/q)),sp.diag(q,1/q))
wt=lambda i: sum(1 if ((i>>k)&1)==0 else -1 for k in range(3))
Pp=sp.diag(*[1 if wt(i)==1 else 0 for i in range(8)]); Pn=sp.diag(*[1 if wt(i)==-1 else 0 for i in range(8)])
print("boundary term restricted traces p, n:", sp.simplify((piv*Pp*Bd).trace()), sp.simplify((piv*Pn*Bd).trace()))
