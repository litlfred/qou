"""Widen q and n on the JM adjacent-commutator identity, as qou-u9o1 required.

The H_4 probe found a True/False pattern over N but explicitly refused to characterise
it -- twelve points at one q in one algebra. This widens both axes before any claim.

Method: regular representation of H_n(q) (FAITHFUL), exact fractions.Fraction, no
float64. Tested at q = 2, 3, 5/2; at (n,k) = (4,1) and (5,2). The JM element is built
from the recursion L_0 = 1, L_{j+1} = s_j L_j s_j, so at k=2 it is s_1 s_0 s_0 s_1.

CONTROL: N = L_k must give True at every q and k -- adjacent commutativity is a
theorem. It does, INCLUDING at k = 2, which the H_4 harness could not reach. That is
a genuinely new verified case: Lean has only the k = 0 shape.

FINDINGS

1. q-INDEPENDENT. Identical results at q = 2, 3, 5/2. The pattern is structural, not
   arithmetic.

2. k-DEPENDENT -- and this kills any fixed "True set" reading of the H_4 data:

       N = s_0     : FALSE at k=1,  TRUE at k=2
       N = s_0 s_3 : TRUE  at k=1 (as s_0 s_2), FALSE at k=2

   So the earlier True set {1, s_0^2, s_2^2, s_0 s_2} is an artifact of k=1 and must
   not be read as a characterisation. Good thing it was not claimed as one.

3. The k-dependence has a PROVED explanation, now in Lean as
   `jmRaw_adjacent_of_comm`: if N commutes with BOTH u = s_k and v = s_{k+1}, both
   normal forms collapse to N^2 (uvu)^2 and the identity follows from the half-twist
   identity `braid_cube_eq`. At k=2, s_0 commutes with s_2 and s_3; at k=1 it does not
   commute with s_1. That is exactly the flip.

   SUFFICIENT, NOT NECESSARY -- measured: at k=2, N = s_3^2 satisfies the identity
   while NOT commuting with u = s_2 (adjacent). So this cannot be the characterisation
   either, and it does NOT apply to N = L_k, which never commutes with s_k (the hook
   word ends in s_{k-1}, adjacent to s_k). That is precisely why the real case is hard.

Emits no witness: this measures which readings survive, not a physical quantity.
"""
from fractions import Fraction as F
def build(n, q):
    h = q - 1/q
    def inv(w): return sum(1 for i in range(n) for j in range(i+1,n) if w[i]>w[j])
    def act(w,i):
        l=list(w); l[i],l[i+1]=l[i+1],l[i]; return tuple(l)
    ID=tuple(range(n))
    def add(a,b):
        r=dict(a)
        for k,v in b.items():
            r[k]=r.get(k,F(0))+v
            if r[k]==0: del r[k]
        return r
    def mul_gen(a,i):
        r={}
        for w,c in a.items():
            ws=act(w,i)
            if inv(ws)>inv(w): r=add(r,{ws:c})
            else: r=add(r,add({w:h*c},{ws:c}))
        return r
    def word(seq):
        r={ID:F(1)}
        for i in seq: r=mul_gen(r,i)
        return r
    return word

def run(n, q, k, cases):
    word = build(n,q)
    u,v = k, k+1
    uv=[u,v]; uvu=[u,v,u]
    out={}
    for name,Nw in cases:
        L = word(uv + Nw + uv + Nw + uv)
        R = word(uvu + Nw + uv + Nw + [u])
        out[name] = (L==R)
    return out

# JM element L_k as a generator word: L_0 = 1, L_{j+1} = s_j L_j s_j
def jm(k):
    w=[]
    for j in range(k): w = [j] + w + [j]
    return w

print("jm words:", {k: jm(k) for k in range(4)})
for (n,k) in [(4,1),(5,2)]:
    cases = [("JM L_k (CONTROL)", jm(k)), ("1", []),
             ("s_0", [0]), ("s_0^2", [0,0]), ("s_%d^2"%(k+1), [k+1,k+1]),
             ("s_%d^2"%k, [k,k]), ("s_0 s_%d"%(k+1), [0,k+1])]
    for q in [F(2), F(3), F(5,2)]:
        r = run(n,q,k,cases)
        ctrl = r["JM L_k (CONTROL)"]
        flag = "OK " if ctrl else "*** CONTROL FAILED ***"
        print(f"n={n} k={k} q={q}  {flag}  " + "  ".join(f"{nm}={str(val)[0]}" for nm,val in r.items()))
