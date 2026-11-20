#!/usr/bin/env python3
"""Exploratory exact-sympy probe (Q3c of PREREGISTRATION.md, run before it was written):
replace every lepton crossing of the 4-strand passage by the left-line weak vertex
W_L = q^-1 J, J = (2 sigma - h)/[2]; print the beta blocks. Exact arithmetic, no floats.
"""
import sympy as sp
q=sp.symbols('q',positive=True); h=q-1/q; b2=q+1/q
S1=sp.Matrix([[q,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,1,0,h,0,0],[0,0,1,0,h,0],[0,0,0,0,0,q]])
S2=sp.Matrix([[0,1,0,0,0,0],[1,h,0,0,0,0],[0,0,q,0,0,0],[0,0,0,q,0,0],[0,0,0,0,0,1],[0,0,0,0,1,h]])
S3=sp.Matrix([[q,0,0,0,0,0],[0,0,1,0,0,0],[0,1,h,0,0,0],[0,0,0,0,1,0],[0,0,0,1,h,0],[0,0,0,0,0,q]])
I=sp.eye(6)
J=lambda S:(2*S-h*I)/b2
WL=lambda S:J(S)/q
inNnu=[2,4,5]; outEp=[5,4,3]; inPe=[3,1,0]; inNuN=[0,1,2]
Eu=sp.Matrix([[0,1,q],[1,0,1],[1/q,1,0]])
def blk(M,r,c): return sp.Matrix(3,3,lambda i,j:sp.simplify(M[r[i],c[j]]))
L=WL(S1)*WL(S2)*WL(S3); R=WL(S3)*WL(S2)*WL(S1)
for name,M,r,c in [("W-left n nu->e p",L,outEp,inNnu),("W-right nu n->p e",R,inPe,inNuN),("W-left reverse p e->nu n",L,inNuN,inPe),("W-right reverse",R,outEp,inNnu)]:
    B=blk(M,r,c); print(name); sp.pprint(sp.simplify(B))
    # ratio to Eu
    try: print(' ratio/Eu:', sp.simplify(B[0,1]/Eu[0,1]), [sp.simplify(B[i,j]-B[0,1]*Eu[i,j]) for i in range(3) for j in range(3)])
    except Exception as e: print(e)
print("== right positive sigma3 sigma2 sigma1: nu n -> p e")
B=blk(S3*S2*S1,inPe,inNuN); sp.pprint(B)
print("== P.W_L single vertex")
Rc=sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]); P=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
Jm=(2*Rc-h*sp.eye(4))/b2
print(sp.simplify(P*Jm/q)[1,2], sp.simplify(P*Jm/q)[2,1], sp.simplify(P*Jm*q)[1,2])
