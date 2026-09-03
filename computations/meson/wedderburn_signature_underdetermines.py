#!/usr/bin/env python3
"""The braid Wedderburn signature is a NECESSARY CONDITION, not a selection principle.

RECORDED NEGATIVE. I proposed that specifying the Wedderburn image could replace
the failed operator-selection LP objective. A braid word of exponent sum `e` has
the forced signature

    chi_sym = q^e ,   det rho_std = (-1)^e ,   chi_alt = (-1/q)^e

and this is REAL: verified here on six braids including negative exponent sums
and the identity, 6 of 6. It is what powered the earlier proof that the LP's
optimum is not a braid image (`operator_selection_what_selects_b3.py`).

But it does NOT select, and the arithmetic I used to argue it nearly did was
wrong. I claimed exponent sum plus Markov trace leaves "2 free, pinned up to
conjugacy -- the right equivalence for a closed braid". The first half is
correct and the conclusion does not follow: pinning a CONJUGACY CLASS is not
pinning a POINT, and the LP's variable `x` is a point in R^6.

MEASURED, exhaustively over all words of length 1-5 in the four signed
generators: 37 of 38 distinct `(e, tr_M)` classes contain MORE THAN ONE distinct
NF vector. The cleanest witness is `(e = 1, tr_M = 0.6126880371)`, which holds
eight of them -- among these `sigma_0` and `sigma_1` themselves, the two unit
basis vectors. They are conjugate in B_3, so they share every class function,
and they are different elements of the algebra.

THE GENERAL OBSTRUCTION, which is the useful part. `chi_sym`, `chi_alt`,
`det rho_std` and `tr_M(x)` are all CLASS FUNCTIONS. No collection of them can
ever separate conjugate elements, so no set of trace-like constraints pins a
point. What does break conjugation invariance is the Frobenius family
`tr_M(b_i . x)` for fixed `b_i` -- which is precisely what `G` already supplies,
and which `NF(B_3)` satisfies with every constraint strictly slack.

So the selection cannot be bought economically from invariants: enough
constraints to pin `x` is equivalent to specifying `x`. Together with the
relative-interior result (no linear objective can select `B_3`), the LP form is
closed off from both directions -- objective and constraints.

Emits no witness: a decision probe whose output is an argument. Arithmetic is
exact (sympy over Q(q), Rational at the pin); `float` only for display.

Bean qou-v7qj.
"""
import sys, itertools, sympy as sp
sys.path.insert(0,"computations/meson"); sys.path.insert(0,"tools/qou-substrate/python")
from operator_selection_lattice_symbolic import (
    NF_BASIS,q,h,structure_constants,derive_trace,_reduce_nf)
from qou_substrate.constants import Q_50_DIGIT_STR
C=structure_constants(); t=derive_trace(C)
q0=sp.Rational(Q_50_DIGIT_STR); tn=[e.subs(q,q0) for e in t]
def rmul(y,g,inv):
    tm={}
    for i,b in enumerate(NF_BASIS):
        if y[i]==0: continue
        tm[b+(g,)]=tm.get(b+(g,),0)+y[i]
        if inv: tm[b]=tm.get(b,0)-h*y[i]
    r=_reduce_nf(tm); return [sp.simplify(r.get(b,0)) for b in NF_BASIS]
GENS=[(0,0),(0,1),(1,0),(1,1)]
groups={}
for L in range(1,6):
    for w in itertools.product(GENS, repeat=L):
        y=[sp.Integer(1)]+[sp.Integer(0)]*5
        for g,iv in w: y=rmul(y,g,iv)
        yn=tuple(sp.nsimplify(sp.N(v.subs(q,q0),22)) for v in y)
        e=sum(1 if not iv else -1 for _,iv in w)
        tm=sp.N(sum(yn[i]*tn[i] for i in range(6)),18)
        groups.setdefault((e,str(tm)),set()).add(yn)
tot=sum(len(v) for v in groups.values())
coll={k:v for k,v in groups.items() if len(v)>1}
print(f"words enumerated: lengths 1-5 over 4 signed generators")
print(f"distinct NF vectors reached : {tot}")
print(f"distinct (e, tr_M) classes  : {len(groups)}")
print(f"classes holding >1 NF vector: {len(coll)}")
if coll:
    print(f"\n=> (e, tr_M) UNDER-DETERMINES. Examples:")
    for k,v in list(coll.items())[:4]:
        print(f"   (e={k[0]}, tr_M={k[1][:12]}) -> {len(v)} distinct NF vectors, e.g.")
        for vec in list(v)[:2]:
            print("        [" + ", ".join(f"{float(z):+.5f}" for z in vec) + "]")
else:
    print("\n=> no collisions at these lengths")
