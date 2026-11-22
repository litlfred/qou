exec(open('intw.py').read().split('# M blocks')[0].split("basis={}")[0])
P32=intertwiners(3,2)[1]; P21=intertwiners(2,1)[1]
def Mblock(z):
    d=[]
    for s_ in states(z):
        nz=sum(1 for t in (0,1,2) if s_[t]==0); w_=K(s_)
        d.append(w_ if nz==1 else (-w_/q**2 if nz==2 else 0))
    return sp.diag(*d)
Mz={z:Mblock(z) for z in (1,2,3)}
ns=sp.symbols('a0:24'); N32=sp.Matrix(4,6,ns); ms=sp.symbols('b0:24'); N21=sp.Matrix(6,4,ms)
eqs=list(P21*N21-Mz[1])+list(P32*N32-N21*P21-Mz[2])+list(-N32*P32-Mz[3])
sol=sp.solve(eqs,list(ns)+list(ms),dict=True)[0]
N32=N32.subs(sol).subs({x:0 for x in ns+ms}).applyfunc(sp.simplify)
N21=N21.subs(sol).subs({x:0 for x in ns+ms}).applyfunc(sp.simplify)
assert sp.simplify(P21*N21-Mz[1])==sp.zeros(4) and sp.simplify(P32*N32-N21*P21-Mz[2])==sp.zeros(6) and sp.simplify(-N32*P32-Mz[3])==sp.zeros(4)
P('/-! ### Intertwiners and the universal left ratio -/\n')
P(f'def P32 (q : R) : Matrix (Fin 6) (Fin 4) R :=\n  {matlean(P32)}\n')
P(f'def P21 (q : R) : Matrix (Fin 4) (Fin 6) R :=\n  {matlean(P21)}\n')
P(f'def N32 (q : R) : Matrix (Fin 4) (Fin 6) R :=\n  {matlean(N32)}\n')
P(f'def N21 (q : R) : Matrix (Fin 6) (Fin 4) R :=\n  {matlean(N21)}\n')
for z in (1,2,3):
    n=N[z]; P(f'def M{z} (q : R) : Matrix (Fin {n}) (Fin {n}) R :=\n  Matrix.diagonal ![{", ".join(lean(Mz[z][k,k]) for k in range(n))}]\n')
alld=', '.join(defs)
P('set_option hygiene false in\nmacro "matTac" : tactic => `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>\n  simp [' + alld + ', P32, P21, N32, N21, M1, M2, M3, Matrix.mul_apply, Matrix.diagonal,\n    Fin.sum_univ_four, Fin.sum_univ_six, Matrix.one_apply] <;> (try field_simp) <;> (try ring)))\n')
T=open('intw_tmpl.lean').read()
for (src,dst,Pn) in ((3,2,'P32'),(2,1,'P21')):
    for i in range(3):
        for inv in (0,1):
            sfx=f'{i}{"i" if inv else ""}'
            P(f'theorem {Pn}_g{sfx} (q : R) (hq : q ≠ 0) : {Pn} q * g{src}_{sfx} q = g{dst}_{sfx} q * {Pn} q := by matTac\n')
    P(T.split('--WORD--')[1].replace('PN',Pn).replace('SRC',str(src)).replace('DST',str(dst)))
P(T.split('--WORD--')[2])
