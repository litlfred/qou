"""PRE-REGISTERED (2026-11-15 18:25Z, before running).  Attack option 2.
Question: is the traced_volume product P_o = prod_i prod_{j>i} (g_{i+1} + d(o_i,o_j))  (H_3, A=3)
the image of a STRAND-TRACKED labelled braid word?  Crossing element for a crossing of strands a,b
is g_s + d(o_a,o_b) with d(u,u)=0, d(d,d)=-h, d(u,d)=-h/2 (same table as the product uses).
Search space (fixed in advance): every positive word in {g1,g2} of length 1..6, every placement of
the flavours on the strands (all distinct permutations of the multiset), proton {u,u,d}, neutron {u,d,d}.
Tests: (E) exact element equality in H_3 over Q(q) (generic q, no numbers);
       (T) trace equality at z_D = q^3/(q^2+1) as rational functions of q.
Report: for each nucleon, the list of (word, placement) passing E, and passing T.
Scalars are NOT allowed (exact equality), since a scalar on a crossing is not part of the table.
No number from CODATA enters.  No outcome selects anything; a 'no word' result is scope (a):
'P is not the strand-tracked image of any positive word of length <= 6 with this crossing table'."""
import sympy as sp, itertools, sys

q,z=sp.symbols('q z',positive=True); h=q-1/q
perms=list(itertools.permutations(range(3)))
def comp(a,b): return tuple(a[b[i]] for i in range(3))
def length(p): return sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j])
S={1:(1,0,2),2:(0,2,1)}
def lmul_s(s,x):
    out={}
    for w,c in x.items():
        sw=comp(S[s],w)
        if length(sw)>length(w): out[sw]=out.get(sw,0)+c
        else: out[w]=out.get(w,0)+h*c; out[sw]=out.get(sw,0)+c
    return out
red={(0,1,2):[],S[1]:[1],S[2]:[2],comp(S[1],S[2]):[1,2],comp(S[2],S[1]):[2,1],comp(comp(S[1],S[2]),S[1]):[1,2,1]}
def mul(x,y):
    out={}
    for w,c in x.items():
        t=dict(y)
        for s in reversed(red[w]): t=lmul_s(s,t)
        for k,v in t.items(): out[k]=out.get(k,0)+c*v
    return {k:sp.simplify(v) for k,v in out.items()}
e={(0,1,2):sp.Integer(1)}
def gen(s,d): return {S[s]:sp.Integer(1),(0,1,2):d}
trb={(0,1,2):1,S[1]:z,S[2]:z,comp(S[1],S[2]):z**2,comp(S[2],S[1]):z**2,comp(comp(S[1],S[2]),S[1]):z*(h*z+1)}
zD=q**3/(q**2+1)
def tr(x): return sp.simplify(sum(c*trb[w] for w,c in x.items()).subs(z,zD))
dval={(1,1):0,(0,0):-h,(1,0):-h/2,(0,1):-h/2}
def word(o,gens):
    pos=[0,1,2]; x=dict(e)
    for s in gens:
        a,b=pos[s-1],pos[s]; x=mul(x,gen(s,dval[(o[a],o[b])])); pos[s-1],pos[s]=b,a
    return x
def product(o):
    x=dict(e)
    for i in range(3):
        for j in range(i+1,3):
            if i<2: x=mul(x,gen(i+1,dval[(o[i],o[j])]))
    return x
def eq(x,y): return all(sp.simplify(x.get(k,0)-y.get(k,0))==0 for k in perms)
for name,o in (('proton uud',(1,1,0)),('neutron udd',(1,0,0))):
    P=product(o); tP=tr(P)
    print('==',name,' product P =',{k:sp.factor(v) for k,v in P.items() if v!=0})
    E=[];T=[]
    for L in range(1,7):
        for gens in itertools.product([1,2],repeat=L):
            for pl in sorted(set(itertools.permutations(o))):
                W=word(pl,gens)
                if eq(W,P): E.append((gens,pl))
                if sp.simplify(tr(W)-tP)==0: T.append((gens,pl))
    print('  exact element matches:',E if E else 'NONE')
    print('  trace matches at z_D :',T if T else 'NONE')
