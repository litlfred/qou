"""The naive induction step for the JM adjacent case FAILS.  Lead 2 is refuted in its
simple form.

After the H_4/H_5 work refuted "palindrome with square centre", "is a square" and
"commutes with v", the ONLY surviving lead in qou-u9o1 was the recursion
L_k = s_{k-1} L_{k-1} s_{k-1}, i.e. run an induction on k. The obvious inductive step is

    "the identity holds for N"  =>  "it holds for w N w",   w = s_{k-1}

because that is exactly what the recursion does. This measures it.

Method: regular representation of H_5(q) (FAITHFUL), exact Fractions at q = 2, k = 2,
so u = s_2, v = s_3 and w = s_1 -- adjacent to u, far from v, exactly the geometry the
recursion has. Reuses the builder from jm_adjacent_widen_q_and_n.py.

CONTROL: N = L_2 = s_1 s_0 s_0 s_1 gives True, as adjacent commutativity requires.

RESULT -- the step is FALSE:

    N = 1        works;  w N w = s_1^2          works
    N = s_0      works;  w N w = s_1 s_0 s_1    FAILS   <--
    N = s_0^2    works;  w N w = s_1 s_0^2 s_1  works   (= L_2, the control)
    N = s_3^2    works;  w N w = s_1 s_3^2 s_1  FAILS   <--

So "satisfies the identity" is NOT preserved by N |-> wNw, and an induction whose
hypothesis is just the conclusion cannot work. **The inductive invariant has to be
strengthened.**

DELIBERATELY NOT CLAIMED: among these, the step succeeded exactly for N = 1 = L_0 and
N = s_0^2 = L_1 -- both genuine JM elements -- and failed for the two non-JM inputs.
That is TWO supporting points. It hints the right invariant is "N is a JM element"
rather than "N satisfies the identity", but two points is not evidence for a
characterisation, and the repo forbids fitting one. Widen before proposing anything.

Emits no witness: this refutes a proof strategy, it does not measure a quantity.
"""
from fractions import Fraction as F
exec(open(__file__.replace('jm_adjacent_induction_step_probe','jm_adjacent_widen_q_and_n')).read().split('print("jm words')[0])

def check(n,q,k,Nw):
    word = build(n,q); u,v = k,k+1
    L = word([u,v]+Nw+[u,v]+Nw+[u,v]); R = word([u,v,u]+Nw+[u,v]+Nw+[u])
    return L==R
def jm(k):
    w=[]
    for j in range(k): w=[j]+w+[j]
    return w

n,k,q = 5,2,F(2)
w = k-1     # sigma_{k-1}: adjacent to u=s_k, far from v=s_{k+1}
print(f"n={n} k={k}: u=s_{k}, v=s_{k+1}, w=s_{w}")
print("CONTROL  N = L_k =", jm(k), "->", check(n,q,k,jm(k)))
print()
print("Does 'N works  =>  wNw works' hold?  (the naive induction step)")
for name,Nw in [("1",[]),("s_0",[0]),("s_0^2",[0,0]),("s_3^2",[3,3]),("L_1=s_0^2",jm(1))]:
    a = check(n,q,k,Nw)
    b = check(n,q,k,[w]+Nw+[w])
    tag = "" if (not a or b) else "   <-- STEP FAILS"
    print(f"  N={name:10s} works={str(a):5s}   wNw works={str(b):5s}{tag}")
