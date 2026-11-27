import sympy as sp
q=sp.symbols('q',positive=True); h=q-1/q
p0,p1,p01,r0,r1,r01,x,y=sp.symbols('p0 p1 p01 r0 r1 r01 x y')
R=sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]); Ri=R.inv()
I=sp.eye(2); kp=sp.kronecker_product
s0=kp(R,I); s1=kp(I,R); s1i=kp(I,Ri)
g=lambda a,b,c: sp.eye(8)+a*s0+b*s1+c*s0*s1i   # the ruled photon, letters sigma_0, sigma_1
piv=kp(kp(sp.diag(q,1/q),sp.diag(q,1/q)),sp.diag(q,1/q))
wt=lambda i: sum(1 if ((i>>k)&1)==0 else -1 for k in range(3))
Pp=sp.diag(*[1 if wt(i)==1 else 0 for i in range(8)]); Pn=sp.diag(*[1 if wt(i)==-1 else 0 for i in range(8)])
for strand,Kb in [(1,sp.Matrix([[x+y,1],[-x*y,0]])),(3,sp.Matrix([[0,1],[-x*y,x+y]]))]:
    T=kp(Kb,sp.eye(4)) if strand==1 else kp(sp.eye(4),Kb)
    G1=g(p0,p1,p01); G2=g(r0,r1,r01)
    out=[]
    for name,W in [("T.g.g",T*G1*G2),("g.T.g",G1*T*G2),("g.g.T",G1*G2*T)]:
        tp=sp.expand((piv*Pp*W).trace()); tn=sp.expand((piv*Pn*W).trace())
        out.append((name,tp,tn))
    same=all(sp.simplify(o[1]-out[0][1])==0 and sp.simplify(o[2]-out[0][2])==0 for o in out)
    tp,tn=out[0][1],out[0][2]
    r1q=sp.simplify((tp/tn).subs(q,1))
    print(f"strand {strand}: placement-independent: {same}")
    print("  Tp/Tn at q=1 (general photons):", sp.factor(r1q))
    print("  Tp at q=1:", sp.factor(tp.subs(q,1)), "  Tn at q=1:", sp.factor(tn.subs(q,1)))
    v3=sp.factor(sp.simplify((tp/tn).subs({p0:0,p1:0,p01:q*h,r0:0,r1:0,r01:-h/q})))
    print("  V3 specialisation:", v3)
