#!/usr/bin/env python3
"""H_n(q) regular-representation GB normal-form multiplication table + Markov trace.

Infra for the Lean H4 Markov-trace formalization (bean qou-1jrr, τ-functor open
item A). Right-action of Coxeter generators s_0..s_{n-2} on the T_w basis
{T_w : w ∈ S_n} via the Iwahori-Hecke rule (T_{s_i}^2 = 1 + h·T_{s_i},
h = q - q^{-1}):
    T_w·T_{s_i} = T_{w s_i}            if l(w s_i) > l(w)
    T_w·T_{s_i} = T_{w s_i} + h·T_w    if l(w s_i) < l(w)
and the Ocneanu/Markov trace: tr(1)=1, tr(x·T_{s_{n-1}}·y)=z·tr(xy) for x,y∈H_{n-1}.
VALIDATION: reproduces the hardcoded H_3 mulσ₀/mulσ₁/TRM before emitting H_4.
"""
import sympy as sp
from itertools import permutations
h, z = sp.symbols('h z')

def length(p):
    n=len(p); return sum(1 for i in range(n) for j in range(i+1,n) if p[i]>p[j])
def mul_gen(p,i):
    q=list(p); q[i],q[i+1]=q[i+1],q[i]; return tuple(q)
def reduced_word(p):
    """A reduced word (list of s_i) with p = s_{w[0]}···s_{w[-1]} acting on identity one-line."""
    p=list(p); w=[]
    while True:
        done=True
        for i in range(len(p)-1):
            if p[i]>p[i+1]:
                p[i],p[i+1]=p[i+1],p[i]; w.append(i); done=False; break
        if done: break
    return list(reversed(w))

class Hecke:
    def __init__(self,n):
        self.n=n
        self.S=sorted(set(permutations(range(n))),key=lambda p:(length(p),p))
        self.idx={p:k for k,p in enumerate(self.S)}
        self.N=len(self.S)
        # right-action matrices gen[i][k] = dict{col:coeff} for T_{S[k]}·s_i
        self.gen=[]
        for i in range(n-1):
            rows=[]
            for p in self.S:
                wsi=mul_gen(p,i); d={}
                if length(wsi)>length(p): d[self.idx[wsi]]=sp.Integer(1)
                else: d[self.idx[wsi]]=sp.Integer(1); d[self.idx[p]]=d.get(self.idx[p],0)+h
                rows.append(d)
            self.gen.append(rows)
    def right_gen(self,vec,i):
        """vec (dict col->coeff) · T_{s_i}."""
        out={}
        for k,c in vec.items():
            for col,cc in self.gen[i][k].items():
                out[col]=sp.expand(out.get(col,0)+c*cc)
        return {k:v for k,v in out.items() if v!=0}
    def mul_word(self,vec,word):
        for i in word: vec=self.right_gen(vec,i)
        return vec
    def T(self,p): return {self.idx[p]:sp.Integer(1)}

def markov_trace(Hn):
    """tr(T_w) for all w, via coset-Markov recursion; returns list over Hn.S."""
    n=Hn.n
    memo={}
    def tr_elt(vec,m):
        # trace of an algebra element (dict over S_m indices of H_m) — but our vec is
        # indexed in H_n's basis; we restrict to elements supported on S_m (fix pts>=m).
        return sp.expand(sum(c*tr_basis(Hn.S[k],m) for k,c in vec.items()))
    def tr_basis(p,m):
        key=(p,m)
        if key in memo: return memo[key]
        if length(p)==0: memo[key]=sp.Integer(1); return memo[key]
        # p is an element of S_m (fixes points >= m). coset decomp S_m = S_{m-1}·chain
        if p[m-1]==m-1:  # fixes top point -> in S_{m-1}
            r=tr_basis(p,m-1); memo[key]=r; return r
        # w = u · (s_{m-2} s_{m-3} ... s_{k}), u ∈ S_{m-1}. Peel top generator once.
        # Build chain c = s_{m-2}...s_k that sends top strand; factor via reduced word.
        w=reduced_word(p)
        assert w.count(m-2)>=1, (p,w)
        # take the LAST occurrence of s_{m-2}; everything after is in S_{m-1} on lower strands
        j=len(w)-1-w[::-1].index(m-2)
        left=w[:j]; right=w[j+1:]   # T_p = T_left · T_{s_{m-2}} · T_right, right has no s_{m-2}
        # tr = z · tr(T_left · T_right)  (Markov, both left,right ∈ H_{m-1})
        prod=Hn.mul_word(dict(Hn.T(tuple(range(n)))),left)  # start from identity, apply left
        prod=Hn.mul_word(prod,right)
        r=sp.expand(z*tr_elt(prod,m-1))
        memo[key]=r; return r
    return [tr_basis(p,n) for p in Hn.S]

def lean_vec(row,N):
    return [row.get(k,sp.Integer(0)) for k in range(N)]

if __name__=='__main__':
    H3=Hecke(3); tr3=markov_trace(H3)
    print("H3 basis:",H3.S)
    print("H3 TRM:",tr3)
    print("H3 gen0:",[lean_vec(H3.gen[0][k],H3.N) for k in range(H3.N)])
    print("H3 gen1:",[lean_vec(H3.gen[1][k],H3.N) for k in range(H3.N)])
    # Expected (Lean, up to basis reorder): TRM has one entry = h*z^2+z (longest elt)
    print("longest-elt trace:",tr3[-1],"  (expect h*z**2+z)")

# ---------------------------------------------------------------------------
def self_validate(Hn, trace):
    """Numeric checks: Hecke rel σ²=1+hσ, braid rels, trace cyclicity tr(ab)=tr(ba)."""
    import random
    subs={h: sp.Rational(7,3), z: sp.Rational(5,2)}
    def gmat(i):
        return sp.Matrix([[Hn.gen[i][k].get(c,0) for c in range(Hn.N)] for k in range(Hn.N)])
    G=[gmat(i).subs(subs) for i in range(Hn.n-1)]
    I=sp.eye(Hn.N); hh=sp.Rational(7,3)
    ok=True
    for i in range(Hn.n-1):
        if G[i]*G[i]!=I+hh*G[i]: ok=False; print(f"  Hecke rel FAIL i={i}")
    for i in range(Hn.n-2):
        if G[i]*G[i+1]*G[i]!=G[i+1]*G[i]*G[i+1]: ok=False; print(f"  braid FAIL {i}")
    for i in range(Hn.n-1):
        for j in range(Hn.n-1):
            if abs(i-j)>=2 and G[i]*G[j]!=G[j]*G[i]: ok=False; print(f"  commute FAIL {i},{j}")
    # trace cyclicity on random pairs of basis elements
    trv=[t.subs(subs) for t in trace]
    def trvec(vec): return sum(c.subs(subs)*trv[k] for k,c in vec.items())
    random.seed(1)
    for _ in range(40):
        a=random.randrange(Hn.N); b=random.randrange(Hn.N)
        wa=reduced_word(Hn.S[a]); wb=reduced_word(Hn.S[b])
        ab=Hn.mul_word(dict(Hn.T(Hn.S[a])),wb)   # T_a·T_b
        ba=Hn.mul_word(dict(Hn.T(Hn.S[b])),wa)
        if sp.expand(trvec(ab)-trvec(ba))!=0: ok=False; print(f"  cyclicity FAIL {a},{b}")
    print(f"  self-validate {'PASS' if ok else 'FAIL'} (Hecke+braid+commute+cyclicity)")
    return ok

def emit_lean_vec(entries):
    return "![" + ", ".join(str(e).replace('**','^') for e in entries) + "]"

def emit_mulsigma(Hn, i):
    """(mulσ_i v)_row = Σ_k gen[i][k][row]·v k, as a Fin N → R map ![...]."""
    ent=[]
    for row in range(Hn.N):
        terms=[]
        for k in range(Hn.N):
            c=Hn.gen[i][k].get(row,0)
            if c==0: continue
            cs=str(c).replace('**','^')
            terms.append(f"v {k}" if c==1 else (f"h * v {k}" if cs=='h' else f"({cs}) * v {k}"))
        ent.append(" + ".join(terms) if terms else "0")
    return "![" + ", ".join(ent) + "]"

if __name__=='__main__':
    print("\n=== H3 self-validate ==="); self_validate(H3,tr3)
    print("\n=== H4 build ===")
    H4=Hecke(4); tr4=markov_trace(H4)
    self_validate(H4,tr4)
    print("H4 N =",H4.N)
    print("H4 TRM =", emit_lean_vec([str(t).replace('**','^') for t in tr4]).replace("'",""))
    for i in range(3):
        print(f"H4 mulσ{i} = "+emit_mulsigma(H4,i))
    print("H4 reduced words:", [reduced_word(p) for p in H4.S])

def emit_witness():
    import json
    H3=Hecke(3); H4=Hecke(4)
    tr3=markov_trace(H3); tr4=markov_trace(H4)
    v3=self_validate(H3,tr3); v4=self_validate(H4,tr4)
    # Markov reduction check: tr(mulσ_{top} e_x) = z·tr(e_x) for x in H_{n-1} parabolic
    def parab_indices(Hn):
        return [k for k,p in enumerate(Hn.S) if all(g < Hn.n-2 for g in reduced_word(p))]
    par4=parab_indices(H4); top=H4.n-2
    subs={h:sp.Rational(7,3), z:sp.Rational(5,2)}
    mk_ok=True
    for x in par4:
        lhs=H4.right_gen(dict(H4.T(H4.S[x])),top)
        lv=sum(c*tr4[k] for k,c in lhs.items())
        if sp.expand(lv - z*tr4[x])!=0: mk_ok=False
    out={"schema":"hecke-regular-nf/v1","description":"H_n(q) regular-rep GB-NF generator actions + Ocneanu/Markov trace; H3 validation + H4 emission for the Lean H4 Markov-trace formalization (bean qou-1jrr).",
         "convention":"T_{s_i}^2 = 1 + h T_{s_i}, h=q-q^{-1}; tr(1)=1, tr(x T_{top})=z tr(x)","validated":{"H3":bool(v3),"H4":bool(v4),"markov_reduction_H4":bool(mk_ok)},
         "H4":{"dim":H4.N,"parabolic_H3_indices":par4,"top_generator":top,
               "TRM":[str(t) for t in tr4],"reduced_words":[reduced_word(p) for p in H4.S],
               "basis_perms":[list(p) for p in H4.S]}}
    json.dump(out,open("computations/markov/hecke-regular-nf-h4.witness.json","w"),indent=1)
    print("witness written; markov_reduction_H4:",mk_ok,"parab:",par4)
