"""PRE-REGISTERED (2026-11-15). Blast radius of traced product P != braid.
For every 2-type ordering of A = 3, 4, 5 strands (types p/n, d: pp=0, nn=-h, pn=-h/2;
same table at quark level with u<->p, d<->n), compare
  P     = prod_i Vhat_i  (HeckeRational.traced_volume, all-pairs, readout z*M10+M11)
  braid = Ocneanu trace at z_D of the strand-tracked positive half twist Delta_A
          (reduced word s1 (s2 s1) (s3 s2 s1) ..., each pair crosses once),
in exact-ish mpmath (dps 40) at the 50-digit q0. Report log|P| - log|braid| per ordering.
Also: is the H_3 (A=3) Ocneanu trace code validated against h3.py closed forms? (check uud/udd)."""
import mpmath as mp, itertools
from qou_substrate.constants import q_at  # proton pin, derived, not a typed copy
mp.mp.dps=40
q=mp.mpf(q_at(60)); h=q-1/q; z=q**3/(q**2+1)
def swap(p,i): p=list(p); p[i],p[i+1]=p[i+1],p[i]; return tuple(p)
def inv(p):
    return sum(1 for i in range(len(p)) for j in range(i+1,len(p)) if p[i]>p[j])
def lmul(i,x):  # T_{s_i} * x ; perms act on positions: s∘w = swap values? use w as word image list
    out={}
    for w,c in x.items():
        sw=tuple(i+1 if v==i else i if v==i+1 else v for v in w)  # s_i ∘ w
        if inv(sw)>inv(w): out[sw]=out.get(sw,0)+c
        else: out[w]=out.get(w,0)+h*c; out[sw]=out.get(sw,0)+c
    return out
def rmul(x,i):  # x * T_{s_i}
    out={}
    for w,c in x.items():
        ws=swap(w,i)   # w ∘ s_i
        if inv(ws)>inv(w): out[ws]=out.get(ws,0)+c
        else: out[w]=out.get(w,0)+h*c; out[ws]=out.get(ws,0)+c
    return out
def reduced_word(w):  # right-descent: w = w' s_i
    word=[]; w=tuple(w)
    while inv(w)>0:
        for i in range(len(w)-1):
            if w[i]>w[i+1]: word.append(i); w=swap(w,i); break
    return list(reversed(word))  # w = s_{word[0]} ... s_{word[-1]}
memo={}
def trT(w):
    n=len(w)
    if n==1: return mp.mpf(1)
    if w in memo: return memo[w]
    if w[-1]==n-1: r=trT(w[:-1])
    else:
        rw=reduced_word(w)
        k=rw.index(n-2)  # exactly one s_{n-2} in a suitable reduced word? use Markov on element
        # T_w = T_a T_{n-2} T_b with a,b in H_{n-1}: tr = z tr(T_a T_b)
        a=rw[:k]; b=rw[k+1:]
        if (n-2) in a or (n-2) in b: raise Exception('need normal form')
        x={tuple(range(n-1)):mp.mpf(1)}
        for i in a+b: x=rmul(x,i)
        r=z*sum(c*trT(v) for v,c in x.items())
    memo[w]=r; return r
def jones_word(w):
    pass
def tr(x): return sum(c*trT(w) for w,c in x.items())
D={(1,1):0,(0,0):-h}
def dd(a,b): return D.get((a,b),-h/2)
def braid_trace(o):
    n=len(o); x={tuple(range(n)):mp.mpf(1)}; pos=list(range(n))
    word=[i for k in range(1,n) for i in range(k-1,-1,-1)]
    for i in word:
        a,b=pos[i],pos[i+1]; d=dd(o[a],o[b])
        y=rmul(x,i); x={k:y.get(k,0)+d*x.get(k,0) for k in set(y)|set(x)}
        pos[i],pos[i+1]=b,a
    return tr(x)
def prod_P(o):
    P=mp.mpf(1)
    for i in range(len(o)-1):
        a,b=mp.mpf(0),mp.mpf(1)
        for j in range(i+1,len(o)):
            d=dd(o[i],o[j]); a,b=a*(h+d)+b, a+b*d
        P*=z*a+b
    return P
print('check uud',mp.nstr(mp.log(abs(braid_trace((1,1,0)))),8),' udd',mp.nstr(mp.log(abs(braid_trace((1,0,0)))),8),' (h3.py: -0.614886, -0.7200703)')
for A in (3,4,5):
    tot=0; bad=0; mx=0
    for o in itertools.product((1,0),repeat=A):
        try: br=braid_trace(o)
        except Exception as e: print('skip',o,e); continue
        dl=mp.log(abs(prod_P(o)))-mp.log(abs(br)); tot+=1
        if abs(dl)>mp.mpf('1e-30'): bad+=1
        mx=max(mx,abs(dl))
        if A<=4: print(A,o,'log P - log braid =',mp.nstr(dl,6))
    print(f'A={A}: {bad}/{tot} orderings differ; max |Δlog| = {mp.nstr(mx,5)}')
# validation: tr(Delta_4) uniform type should equal z^2 * tr2(sigma^4)  (Markov + braid relation, by hand)
t4=z*(h**3+2*h)+h**2+1
print('validate A=4 uniform: braid', mp.nstr(braid_trace((1,1,1,1)),12), ' z^2 tr2(s^4)=', mp.nstr(z**2*t4,12), ' P=', mp.nstr(prod_P((1,1,1,1)),12))
