"""PRE-REGISTERED (2026-11-15, before running).  Route R5.
Algebra: H_3(q), generators g1,g2, g^2 = h g + 1 (h = q - 1/q), exact over Q(q,z) (sympy).
Trace: Ocneanu/Markov tr(1)=1, tr(x g2)=z tr(x) for x in H_2, tr(g1)=z; z = z_D = q^3/(q^2+1)
       (z_C printed only as the historical comparison).
Crossing elements by flavour of the two STRANDS crossing (strand-tracked through the word):
       uu -> g, dd -> g^{-1} = g - h, ud -> g - h/2  (= weak vertex W up to a scalar that cancels:
       uud and udd each have 2 ud pairs in every word below).
Words: (i) half twist Delta = g1 g2 g1 (each strand pair crosses once);
       (ii) full twist Delta^2 (each pair crosses twice).
Orderings fixed in advance: proton [1,1,0], neutron [1,0,0].  Phi(K) = log|tr(word_K)|.
Report Dm = alpha*|Phi(udd)-Phi(uud)|, alpha = m_e*8G; CODATA printed for comparison only.
Also print the H_3 channel decomposition of tr_z (w_(3), w_(21), w_(111)) to confirm w_(111)=0 at z_D.
No outcome selects anything."""
import sympy as sp, mpmath as mp, itertools
from qou_substrate.constants import q_at  # proton pin, derived, not a typed copy
q,z=sp.symbols('q z',positive=True); h=q-1/q
perms=list(itertools.permutations(range(3)))
def comp(a,b): return tuple(a[b[i]] for i in range(3))   # (a∘b)
def length(p): return sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j])
S={1:(1,0,2),2:(0,2,1)}
def lmul_s(s,x):  # T_s * x
    out={}
    for w,c in x.items():
        sw=comp(S[s],w)
        if length(sw)>length(w): out[sw]=out.get(sw,0)+c
        else:
            out[w]=out.get(w,0)+h*c; out[sw]=out.get(sw,0)+c
    return out
def mul(x,y):  # x*y, x expanded via reduced words
    red={(0,1,2):[],S[1]:[1],S[2]:[2],comp(S[1],S[2]):[1,2],comp(S[2],S[1]):[2,1],comp(comp(S[1],S[2]),S[1]):[1,2,1]}
    out={}
    for w,c in x.items():
        t=dict(y)
        for s in reversed(red[w]): t=lmul_s(s,t)
        for k,v in t.items(): out[k]=out.get(k,0)+c*v
    return out
e={(0,1,2):1}
def gen(s,d): # g_s + d
    return {S[s]:1,(0,1,2):d}
trb={(0,1,2):1,S[1]:z,S[2]:z,comp(S[1],S[2]):z**2,comp(S[2],S[1]):z**2,comp(comp(S[1],S[2]),S[1]):z*(h*z+1)}
def tr(x): return sp.simplify(sum(c*trb[w] for w,c in x.items()))
dval={(1,1):0,(0,0):-h,(1,0):-h/2,(0,1):-h/2}
def word(o,gens):
    pos=list(range(3)) # pos[k] = strand at position k
    x=dict(e)
    for s in gens:
        a,b=pos[s-1],pos[s]
        x=mul(x,gen(s,dval[(o[a],o[b])]))
        pos[s-1],pos[s]=b,a
    return x
mp.mp.dps=40
q0=mp.mpf(q_at(60))
al=mp.mpf('0.51099895069')*8*mp.catalan; tgt=mp.mpf('1.29333378')
zD=q0**3/(q0**2+1); zC=mp.sqrt(q0)/(q0+1)
for name,gens in (('half twist g1g2g1',[1,2,1]),('full twist (g1g2g1)^2',[1,2,1,1,2,1])):
    tp=tr(word([1,1,0],gens)); tn=tr(word([1,0,0],gens))
    print('==',name); print(' tr(uud)=',sp.factor(tp)); print(' tr(udd)=',sp.factor(tn))
    print(' D closed ratio tr(udd)/tr(uud)=',sp.factor(sp.simplify((tn/tp).subs(z,q**3/(q**2+1)))))
    for zn,zz in (('C',zC),('D',zD)):
        P=sp.lambdify((q,z),tp,'mpmath')(q0,zz); N=sp.lambdify((q,z),tn,'mpmath')(q0,zz)
        d=mp.log(abs(N))-mp.log(abs(P))
        print(f'  {zn}: Phi(uud)={mp.nstr(mp.log(abs(P)),7)} Phi(udd)={mp.nstr(mp.log(abs(N)),7)} dPhi={mp.nstr(d,7)} Dm={mp.nstr(al*abs(d),6)} vs CODATA {mp.nstr((al*abs(d)/tgt-1)*100,4)}%')
# channel check: w_(111) of tr_z on H_3 = coefficient s.t. tr = sum w_l chi_l ; sign rep chi(g)=-1/q
# solve w's from tr on basis 1, g1, g1g2 (class reps) using characters
chi={'3':{0:1,1:q,2:q**2},'111':{0:1,1:-1/q,2:q**-2},'21':{0:2,1:q-1/q,2:-1}}
w=sp.symbols('w3 w21 w111'); eqs=[sp.Eq(sum(wi*chi[k][n] for wi,k in zip(w,['3','21','111'])),[1,z,z**2][n]) for n in range(3)]
sol=sp.solve(eqs,w); print('w_(111) at z_D =',sp.simplify(sol[w[2]].subs(z,q**3/(q**2+1))))
