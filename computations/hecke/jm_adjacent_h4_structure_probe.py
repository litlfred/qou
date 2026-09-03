"""Which property of N makes the JM adjacent normal forms agree?  Two leads, both REFUTED.

Setting: `HeckeJucysMurphyAdjacentNormalForm.lean` proves

    L_{k+1} L_{k+2} = (uv) N (uv) N (uv)        u = sigma_k, v = sigma_{k+1}, N = L_k
    L_{k+2} L_{k+1} = (uvu) N (uv) N u

and adjacent commutativity at k is exactly the assertion that they agree.  Bean qou-u9o1
recorded TWO candidate structures for what N=L_k has that a generic element lacks:
palindromicity with a square centre, and the recursion.  This measures them.

Method: the REGULAR representation of H_4(q) (24-dimensional, hence FAITHFUL -- unlike an
irrep, it cannot hide a difference), built from the Hecke rule
T_w T_s = T_{ws} if l(ws) > l(w) else (q - q^-1) T_w + T_{ws}.  Exact fractions.Fraction
at q = 2; no float64 anywhere, per the repo precision rules.  k = 1, so u = s_1, v = s_2
and the true JM element is N = L_1 = s_0^2 -- all inside H_4.

CONTROL: N = s_0^2 is the REAL JM element and adjacent commutativity at k=1 is a THEOREM,
so that line MUST be True.  It is.  Keep the control: an earlier version of this script
built the left form uncancelled and the right form cancelled, and reported False for every
case including the theorem.  That is the second time the same mixing bug appeared in this
session; without a known-answer line it looks like a discovery.

RESULTS (q=2, k=1):
  N = s_0^2 (the JM element)          True   <- control, as required
  N = 1                               True
  N = s_2^2                           True
  N = s_0 s_2                         True
  N = s_0                             False
  N = s_2                             False
  N = s_1, s_1^2                      False
  N = (s_0 s_2)^2, s_0^3, s_0^4       False

WHAT THIS REFUTES:
  * "commutes with v" -- s_0 and s_2 both commute with v = s_2 and both FAIL.  This
    independently confirms the H_3 2-dim-irrep refutation in
    jm_adjacent_generic_N_counterexample.py, by a different computation in a different
    algebra.
  * "palindrome with a square centre" (lead 1) -- s_1^2 is one and FAILS.
  * "is a square" -- (s_0 s_2)^2 and s_0^4 are squares and FAIL.

So BOTH leads recorded in qou-u9o1 are wrong.  The distinguishing property of L_k remains
unidentified.

DELIBERATELY NOT CLAIMED: the True set here is {1, s_0^2, s_2^2, s_0 s_2}, which is small
and suggestive.  Twelve data points at one q in one algebra is not a characterisation, and
fitting one would be exactly the numerology this repo forbids.  Anyone extending this
should widen q and n first.

Emits no witness: this refutes readings, it does not measure a quantity.
"""
from fractions import Fraction as F
q = F(2); h = q - F(1,2); N_ = 4
def inv(w): return sum(1 for i in range(N_) for j in range(i+1,N_) if w[i]>w[j])
def act(w,i):
    l=list(w); l[i],l[i+1]=l[i+1],l[i]; return tuple(l)
ID=tuple(range(N_))
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

U,V = 1,2                      # k=1: u=s_1, v=s_2
uv=[U,V]; uvu=[U,V,U]

def shapes(Nw):
    L  = uv + Nw + uv + Nw + uv          # (uv)N(uv)N(uv)
    R  = uvu + Nw + uv + Nw + [U]        # (uvu)N(uv)N u
    Lc = Nw + uv + Nw + uv               # N(uv)N(uv)
    Rc = [U] + Nw + uv + Nw + [U]        # u N(uv)N u
    return word(L),word(R),word(Lc),word(Rc)

def test(name,Nw):
    L,R,Lc,Rc = shapes(Nw)
    cons = (word(uv+ (Nw+uv+Nw+uv)) == L)   # cancellation consistency
    print(f"  {name:32s} uncancelled:{L==R!s:5s} cancelled:{Lc==Rc!s:5s} consistent:{cons}")

print("CONTROL -- N = L_1 = s_0^2 is the REAL JM element; adjacent commutativity")
print("at k=1 is a THEOREM, so this MUST be True or the harness is wrong.")
test("N = s_0^2   (JM element)", [0,0])
print()
print("DISCRIMINATORS")
test("N = 1", [])
test("N = s_1^2   (palindrome, sq centre)", [1,1])
test("N = s_2^2   (palindrome, sq centre)", [2,2])
test("N = s_0     (single letter)", [0])
test("N = s_0s_1s_0 (palindrome, no sq)", [0,1,0])

print()
print("PATTERN PROBE -- 'commutes with v' vs 'is a square'")
def commutes_with_v(Nw):
    a=word(Nw); return word(Nw+[V])==word([V]+Nw)
for name,Nw in [("1",[]),("s_0",[0]),("s_0^2",[0,0]),("s_2",[2]),("s_2^2",[2,2]),
                ("s_1",[1]),("s_1^2",[1,1]),("s_0s_2",[0,2]),("(s_0s_2)^2",[0,2,0,2]),
                ("s_0^3",[0,0,0]),("s_0^4",[0,0,0,0]),("s_0s_2s_0s_2",[0,2,0,2])]:
    L,R,Lc,Rc = shapes(Nw)
    print(f"  {name:14s} commutes_v={str(commutes_with_v(Nw)):5s}  identity={str(L==R):5s}")
