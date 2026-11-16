"""PRE-REGISTERED (2026-11-15 18:35Z, before running).  Attack option 1 (owner: "try coloured strands").
Algebra: two-colour Yokonuma–Hecke Y_{2,3}(q), presentation (Chlouveraki–Poulain d'Andecy):
  t_j^2 = 1, t's commute;  g_i t_j = t_{s_i(j)} g_i;  braid relations;
  g_i^2 = 1 + h e_i g_i,  e_i = (1 + t_i t_{i+1})/2,  h = q - 1/q.   Exact over Q(q, z, x), basis t^a g_w (48).
Trace: Juyumaya Markov trace, found by solving the linear system tr(1)=1, cyclicity on generators,
  tr(b g_n)=z tr(b), tr(b t_{n+1}) = x tr(b) for b in Y_{2,n} (n=1,2).  z = z_D = q^3/(q^2+1).
  x: reported SYMBOLICALLY, and at the three E-system solutions for d=2: x = 1, 0, -1.  None is selected.
Colours: u -> t-eigenvalue +1, d -> -1.  Colour projector pi_c = prod_j (1 + eps_j t_j)/2.
  tr(pi_c W) vanishes unless c is constant on the cycles of W's permutation, so the placement is FORCED:
  half twist (perm (0 2)): proton = (u,d,u), neutron = (d,u,d).  Full twist (perm id): (u,u,d), (u,d,d).
Variants (fixed in advance):
  Y0: every crossing is g_i (positive word).
  Y1: crossings between two d strands use g_i^{-1} = g_i - h e_i (chirality rule of the old table);
      uu and mixed crossings use g_i.
Phi_raw(K) = log|tr(pi_c W)|;  Phi_norm(K) = log|tr(pi_c W)/tr(pi_c)|.
Consistency check printed: all-u sector reduces to the Ocneanu H_3 trace (tr(pi_uuu W)/tr(pi_uuu) vs H_3).
Report dPhi and alpha*|dPhi| (alpha = m_e*8G); CODATA printed for comparison only.  No outcome selects anything."""
import sympy as sp, mpmath as mp, itertools
q,z,x=sp.symbols('q z x'); h=q-1/q
P3=list(itertools.permutations(range(3)))
def comp(a,b): return tuple(a[b[i]] for i in range(3))
def ln(p): return sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j])
S={1:(1,0,2),2:(0,2,1)}
red={(0,1,2):[],S[1]:[1],S[2]:[2],comp(S[1],S[2]):[1,2],comp(S[2],S[1]):[2,1],comp(comp(S[1],S[2]),S[1]):[1,2,1]}
def add(d,k,v):
    d[k]=d.get(k,0)+v
def swap(a,i): a=list(a); a[i-1],a[i]=a[i],a[i-1]; return tuple(a)
def tflip(a,js): a=list(a); [a.__setitem__(j,a[j]^1) for j in js]; return tuple(a)
def lg(i,X):  # g_i * X
    out={}
    for (a,w),c in X.items():
        b=swap(a,i); sw=comp(S[i],w)
        if ln(sw)>ln(w): add(out,(b,sw),c)
        else:
            add(out,(b,sw),c)
            add(out,(b,w),h*c/2); add(out,(tflip(b,[i-1,i]),w),h*c/2)
    return out
def lt(j,X): return {(tflip(a,[j]),w):c for (a,w),c in X.items()}
def mul(X,Y):
    out={}
    for (a,w),c in X.items():
        T=dict(Y)
        for s in reversed(red[w]): T=lg(s,T)
        for j in range(3):
            if a[j]: T=lt(j,T)
        for k,v in T.items(): add(out,k,c*v)
    return {k:sp.together(v) for k,v in out.items() if sp.simplify(v)!=0}
basis=[(a,w) for a in itertools.product((0,1),repeat=3) for w in P3]
one={((0,0,0),(0,1,2)):sp.Integer(1)}
G={i:{((0,0,0),S[i]):sp.Integer(1)} for i in (1,2)}
Tg={j:{(tuple(1 if k==j else 0 for k in range(3)),(0,1,2)):sp.Integer(1)} for j in range(3)}
E={i:{((0,0,0),(0,1,2)):sp.Rational(1,2),(tuple(1 if k in (i-1,i) else 0 for k in range(3)),(0,1,2)):sp.Rational(1,2)} for i in (1,2)}
def lin(X,Y,s=1): 
    out=dict(X); [add(out,k,s*v) for k,v in Y.items()]; return out
def scal(c,X): return {k:c*v for k,v in X.items()}
Ginv={i:lin(G[i],scal(-h,E[i])) for i in (1,2)}
U={b:sp.Symbol('T%d'%n) for n,b in enumerate(basis)}
def trs(X): return sum(c*U[k] for k,c in X.items())
eqs=[U[((0,0,0),(0,1,2))]-1]
for b in basis:
    B={b:sp.Integer(1)}
    for s in list(G.values())+list(Tg.values()):
        eqs.append(trs(mul(s,B))-trs(mul(B,s)))
def inY(b,n):
    a,w=b; return all(a[k]==0 for k in range(n,3)) and all(w[k]==k for k in range(n,3))
for b in basis:
    B={b:sp.Integer(1)}
    if inY(b,2): eqs+= [trs(mul(B,G[2]))-z*U[b], trs(mul(B,Tg[2]))-x*U[b]]
    if inY(b,1): eqs+= [trs(mul(B,G[1]))-z*U[b], trs(mul(B,Tg[1]))-x*U[b]]
sol=sp.solve(eqs,list(U.values()),dict=True)
assert len(sol)==1, sol
sol=sol[0]; print('trace solved; free symbols left:',set().union(*[sp.sympify(v).free_symbols for v in sol.values()]))
def tr(X): return sp.factor(sp.simplify(trs(X).subs(sol)))
def proj(c):
    X=dict(one)
    for j,cj in enumerate(c):
        eps=1 if cj=='u' else -1
        X=mul(X,lin(scal(sp.Rational(1,2),one),scal(sp.Rational(eps,2),Tg[j])))
    return X
def wordel(c,gens,variant):
    pos=[0,1,2]; X=dict(one)
    for s in gens:
        a,b=pos[s-1],pos[s]
        el=Ginv[s] if (variant=='Y1' and c[a]=='d' and c[b]=='d') else G[s]
        X=mul(X,el); pos[s-1],pos[s]=b,a
    return X
zD=q**3/(q**2+1)
mp.mp.dps=40
from qou_substrate.constants import q_at  # proton pin, derived, not a typed copy
q0=mp.mpf(q_at(mp.mp.dps))
al=mp.mpf('0.51099895069')*8*mp.catalan; tgt=mp.mpf('1.29333378')
# consistency: all-u sector vs Ocneanu H3 half twist tr = z(hz+1)
pu=proj('uuu'); W=wordel('uuu',[1,2,1],'Y0')
print('check all-u: tr(pi W)/tr(pi) =',sp.factor(sp.simplify(tr(mul(pu,W))/tr(pu))),' vs Ocneanu z(hz+1) at same z only if x=1')
for wname,gens,cp,cn in (('half twist',[1,2,1],'udu','dud'),('full twist',[1,2,1,1,2,1],'uud','udd')):
    for var in ('Y0','Y1'):
        Pp=proj(cp); Pn=proj(cn)
        tp=tr(mul(Pp,wordel(cp,gens,var))); tn=tr(mul(Pn,wordel(cn,gens,var)))
        np_=tr(Pp); nn=tr(Pn)
        print(f'== {wname} {var}: proton {cp}, neutron {cn}')
        print('   tr(pi_p W)=',tp); print('   tr(pi_n W)=',tn); print('   tr(pi_p)=',np_,'  tr(pi_n)=',nn)
        for xv in (1,0,-1,sp.Symbol('x')):
            for norm in ('raw','norm'):
                a=sp.simplify((tp/(np_ if norm=='norm' else 1)).subs({z:zD,x:xv})); b=sp.simplify((tn/(nn if norm=='norm' else 1)).subs({z:zD,x:xv}))
                if xv==sp.Symbol('x'):
                    print(f'   x symbolic {norm}: ratio n/p =',sp.factor(sp.simplify(b/a))); continue
                if a in (0,sp.zoo,sp.nan) or b in (0,sp.zoo,sp.nan) or a.has(sp.zoo) or b.has(sp.zoo):
                    print(f'   x={xv} {norm}: undefined (p={a}, n={b})'); continue
                r=sp.factor(sp.simplify(b/a)); d=mp.log(abs(sp.lambdify(q,r,'mpmath')(q0)))
                print(f'   x={xv} {norm}: ratio={r}  dPhi={mp.nstr(d,7)}  Dm={mp.nstr(al*abs(d),6)}  vs CODATA {mp.nstr((al*abs(d)/tgt-1)*100,4)}%')
