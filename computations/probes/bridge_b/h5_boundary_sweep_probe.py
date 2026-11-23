import sympy as sp
q=sp.symbols('q',positive=True); x,y=sp.symbols('x y')
I=sp.eye(2); kp=sp.kronecker_product
def run(qq, strand, word_spec, label):
    h=qq-1/qq
    R=sp.Matrix([[qq,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,qq]]); Ri=R.inv()
    # solve RE on the boundary strand for this R
    a,b,c,d=sp.symbols('a b c d'); Km=sp.Matrix([[a,b],[c,d]])
    Kb1=kp(Km,I) if strand==1 else kp(I,Km)
    eqs=[e for e in set(sp.expand(R*Kb1*R*Kb1-Kb1*R*Kb1*R)) if e!=0]
    sols=[s for s in sp.solve(eqs,[a,b,c,d],dict=True)]
    s1=kp(R,I); s1i=kp(Ri,I); s2=kp(I,R); s2i=kp(I,Ri)
    L={'1':s1,'1i':s1i,'2':s2,'2i':s2i}
    word=[L[t] for t in word_spec]
    piv=kp(kp(sp.diag(qq,1/qq),sp.diag(qq,1/qq)),sp.diag(qq,1/qq))
    wt=lambda i: sum(1 if ((i>>k)&1)==0 else -1 for k in range(3))
    Pp=sp.diag(*[1 if wt(i)==1 else 0 for i in range(8)]); Pn=sp.diag(*[1 if wt(i)==-1 else 0 for i in range(8)])
    print(label, "RE solutions:", sols)
    for s in sols:
        Ks=Km.subs(s)
        if Ks.free_symbols & {a,b,c,d} == set(Ks.free_symbols & {a,b,c,d}) and Ks.is_diagonal() and (Ks-Ks[0,0]*I)==sp.zeros(2): continue
        T=kp(Ks,sp.eye(4)) if strand==1 else kp(sp.eye(4),Ks)
        ratios=set()
        for j in range(len(word)+1):
            W=sp.eye(8)
            for k,Lm in enumerate(word):
                if k==j: W=W*T
                W=W*Lm
            if j==len(word): W=W*T
            tp=(piv*Pp*W).trace(); tn=(piv*Pn*W).trace()
            ratios.add(sp.factor(sp.simplify(tp/tn)))
        for r in ratios:
            print("   K=",Ks.tolist()," Tp/Tn=",r," at q=1:",sp.limit(r,q,1))
V3=['1','2i']*3; V6=['1','2i']*6
run(q,1,V3,"strand1 V3")
run(q,1,V6,"strand1 V6")
run(q,3,V3,"strand3 V3")
run(1/q,1,V3,"bar(q->1/q) strand1 V3")
