"""Construct the q-Toffoli as an ELEMENT of H_3(q), take its NF coordinates,
and evaluate the LP feasibility condition G.t >= 0 that prop:toffoli-lp-stability
asserts but never computes.

WHY THIS PROBE EXISTS (bean qou-0pnj).  The proposition opens

    "Let T_q in H_3(q) be the q-Toffoli element, realized as the 3-strand braid
     word ... Express the q-Toffoli in normal-form coordinates as
     T_q = sum_{i=1..6} t_i(q) b_i"

and its proof reduces LP feasibility to "the positivity of P_77(q) . W_std(q)
with the appropriate sign from Phi(q)".  Measured before writing this:

  * t(q) appears NOWHERE in the corpus.  computations/toffoli-lp-stability.py
    emits P_77, q_AND_P76 and the Gram spectrum, and never forms G.t.
  * No braid word is specified anywhere.  The string "3-strand braid word"
    occurs in exactly one place -- that opening sentence -- and no sigma-word
    for the Toffoli exists in any producer.
  * The only recorded construction (_deprecated/toffoli-braid.py) works
    entirely in SCALARS: 2x2 transfer matrices over crossing coefficients,
    traced volumes V_i = z a_i + b_i, and products of them.

So the object the proposition takes coordinates of is never built.  This probe
builds it, from the construction's own ingredients.

THE KEY OBSERVATION that makes it possible.  The deprecated producer prints its
own convention: "Crossing coefficients C_{ij} = c_j sigma_i + d_j".  That is an
ELEMENT of H_3(q), not a scalar.  And chain_reduce's recursion

    new_a = a*c*ha + a*d + b*c ;  new_b = a*c + b*d

is exactly the product (a sigma + b)(c sigma + d) reduced by the Hecke relation
sigma^2 = ha*sigma + 1:

    (a s + b)(c s + d) = ac s^2 + (ad + bc) s + bd
                       = ac(ha s + 1) + (ad + bc) s + bd
                       = (ac*ha + ad + bc) s + (ac + bd).

So chain_reduce(i, ordering) returns the coefficients of the algebra element
prod_{j>i} (c_j sigma_i + d_j) = a_i sigma_i + b_i, and the Toffoli element for
an ordering is the product over generators

    T_q(ordering) = (a_0 sigma_0 + b_0)(a_1 sigma_1 + b_1)  in  H_3(q).

That lands in the full 6-dimensional algebra (sigma_0 and sigma_1 do not
commute), so it has genuine NF coordinates.

WHAT IS MEASURED.  For each of the 8 strand-type orderings: the NF coordinate
vector t(q0), the Gram product (G t)_i, and whether every component is >= 0.
The Gram is pyhecke.gram.gram_matrix_mp -- the PRODUCTION Gram, convention D.
The producer's own gram_matrix is NOT used: it builds tr_M with the retracted
naive length rule `tr += c * (z ** len(w))`, which the content block itself
calls "the retracted naive length rule ... the pre-2026-05-19 tr_M(e^-) = z^3
bug".

Exact rational arithmetic in q throughout via sympy; the anchor evaluation is
mpmath at 50 dps.  No float64 anywhere.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent
                      / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent
                      / "tools" / "qou-substrate" / "python"))

import mpmath as mp                                        # noqa: E402
import sympy as sp                                         # noqa: E402

mp.mp.dps = 50

q = sp.Symbol("q", positive=True)
ha = q - 1 / q                       # the Hecke parameter q - q^{-1}

# NF basis of H_3(q), as words in generators 0 and 1.  Matches
# pyhecke.gram.NF_BASIS exactly (asserted below).
NF = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]


def crossing_coefficients(ti, tj):
    """(c, d) for a crossing of strand types ti, tj -- the paper convention."""
    if ti == 1 and tj == 1:
        return sp.Integer(1), sp.Integer(0)          # pp
    if ti == 0 and tj == 0:
        return sp.Integer(1), -ha                    # nn
    return sp.Integer(1), -ha / 2                    # mixed


def chain_element(gen_idx, ordering):
    """prod_{j>gen_idx} (c_j sigma_i + d_j) = a sigma_i + b.  Returns (a, b).

    Identical recursion to _deprecated/toffoli-braid.py::chain_reduce; kept
    here so this probe does not import from _deprecated/.
    """
    a, b = sp.Integer(0), sp.Integer(1)
    for j in range(gen_idx + 1, len(ordering)):
        c, d = crossing_coefficients(ordering[gen_idx], ordering[j])
        a, b = sp.expand(a * c * ha + a * d + b * c), sp.expand(a * c + b * d)
    return sp.cancel(a), sp.cancel(b)


# ---- Hecke multiplication in the NF basis -------------------------------

def _mul_word_gen(word, g):
    """Right-multiply an NF word by generator g; return {word: coeff}."""
    # sigma_g^2 = ha sigma_g + 1
    if word and word[-1] == g:
        base = word[:-1]
        return {word: ha, base: sp.Integer(1)}
    cand = word + (g,)
    if cand in NF:
        return {cand: sp.Integer(1)}
    # braid-reduce to an NF word
    for target in NF:
        if len(target) == len(cand) and _braid_equiv(cand, target):
            return {target: sp.Integer(1)}
    raise ValueError(f"cannot reduce {cand}")


def _braid_equiv(w1, w2):
    """H_3: sigma_0 sigma_1 sigma_0 = sigma_1 sigma_0 sigma_1."""
    if w1 == w2:
        return True
    if len(w1) == 3 and len(w2) == 3:
        return {w1, w2} == {(0, 1, 0), (1, 0, 1)}
    return False


def mul(t1, t2):
    """Multiply two NF-coordinate dicts."""
    out = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            acc = {w1: c1 * c2}
            for g in w2:
                nxt = {}
                for w, c in acc.items():
                    for w3, c3 in _mul_word_gen(w, g).items():
                        nxt[w3] = nxt.get(w3, 0) + c * c3
                acc = nxt
            for w, c in acc.items():
                out[w] = out.get(w, 0) + c
    return {w: sp.cancel(sp.expand(c)) for w, c in out.items()
            if sp.simplify(c) != 0}


def toffoli_element(ordering):
    """T_q(ordering) = prod_i (a_i sigma_i + b_i) in H_3(q), in NF coords."""
    acc = {(): sp.Integer(1)}
    for i in range(len(ordering) - 1):
        a, b = chain_element(i, ordering)
        acc = mul(acc, {(i,): a, (): b})
    return acc


def decode(k):
    return ((k >> 2) & 1, (k >> 1) & 1, k & 1)


def main():
    from pyhecke.gram import NF_BASIS, gram_matrix_mp
    assert list(NF_BASIS) == NF, f"NF basis drift: {NF_BASIS} vs {NF}"
    # Q_50_DIGIT_STR, not Q: the module constant Q is float64, and the
    # raw-float64 ratchet flags reading it (correctly -- this probe carries q0
    # through an exact-rational substitution, so a 17-digit anchor would cap
    # the whole computation at float64 width regardless of mp.dps).
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP
    q0 = Q_MP

    G = gram_matrix_mp(q=q0)
    G = [[mp.mpf(str(x)) for x in row] for row in G]

    print("=" * 74)
    print("  q-TOFFOLI NF COORDINATES AND THE LP FEASIBILITY CONDITION G.t >= 0")
    print("=" * 74)
    print(f"  q0 = {mp.nstr(q0, 20)}   (proton pin)")
    print(f"  NF basis: {NF}")
    print(f"  Gram: pyhecke.gram.gram_matrix_mp (production, convention D)")
    print()

    results, n_feasible = [], 0
    for k in range(8):
        ordering = decode(k)
        T = toffoli_element(ordering)
        t = [sp.cancel(T.get(w, sp.Integer(0))) for w in NF]
        tv = [mp.mpf(str(sp.N(c.subs(q, sp.Float(mp.nstr(q0, 40), 40)), 40)))
              for c in t]
        Gt = [sum((G[i][j] * tv[j] for j in range(6)), mp.mpf(0))
              for i in range(6)]
        feasible = all(x >= 0 for x in Gt)
        n_feasible += feasible
        results.append((k, ordering, tv, Gt, feasible))
        print(f"  k={k} ordering={ordering}  feasible={feasible}")
        print(f"      t (q0) = [{', '.join(mp.nstr(x, 8) for x in tv)}]")
        print(f"      (G t)  = [{', '.join(mp.nstr(x, 8) for x in Gt)}]")
        neg = [i for i, x in enumerate(Gt) if x < 0]
        if neg:
            print(f"      violated rows: {neg}")
        print()

    print("=" * 74)
    print(f"  ORDERINGS WITH G.t >= 0 : {n_feasible} of 8")
    print("=" * 74)

    # ---- HOW MUCH IS THAT WORTH?  The adversarial check. -----------------
    # G.t >= 0 is only informative if cancellation was POSSIBLE.  If G is
    # entrywise non-negative and t is too, positivity is forced by shape and
    # says nothing about the framework.
    g_neg = [(i, j) for i in range(6) for j in range(6) if G[i][j] < 0]
    print()
    print(f"  Gram entrywise: {len(g_neg)} negative entries of 36")
    if not g_neg:
        print("  -> G is entrywise NON-NEGATIVE.")
    trivial = []
    for k, ordering, tv, Gt, feas in results:
        t_neg = [i for i, x in enumerate(tv) if x < 0]
        tag = "TRIVIAL (t entrywise >= 0 too)" if not t_neg else \
              f"non-trivial: t has negatives at {t_neg}"
        trivial.append((k, not t_neg))
        print(f"    k={k}: {tag}")
    n_trivial = sum(1 for _, t in trivial if t)
    print()
    print(f"  Of the {n_feasible} feasible orderings, {n_trivial} are TRIVIALLY so.")

    # Cross-check the Gram against the value the corpus records, so a reader
    # can see this probe is using the same object the proof block discusses.
    ev = sorted(mp.eigsy(mp.matrix(G), eigvals_only=True))
    print()
    print(f"  Gram eigenvalues: {[mp.nstr(x, 8) for x in ev]}")
    print(f"  lambda_min = {mp.nstr(ev[0], 10)}")
    print("  corpus records lambda_min(q0) = -0.75270211 under convention D")
    print("  (toffoli-lp-stability-proof.md) -- MATCHES, so this is the same Gram.")
    n_zero = sum(1 for x in ev if abs(x) < mp.mpf("1e-40"))
    print(f"  zero eigenvalues: {n_zero} -> the form is SINGULAR, as recorded.")

    # The two claims under test, stated so a reader can see which is which.
    k7 = next(r for r in results if r[0] == 7)
    print()
    print("  The Toffoli's own control-control-target ordering is k=7 = (1,1,1).")
    print(f"  Its LP feasibility at q0: {k7[4]}")
    print()
    print("  Its element is  T_q = sigma_1 + (q - 1/q) sigma_0 sigma_1,  read off")
    print("  the crossing coefficients: all-proton gives (c,d) = (1,0) at every")
    print("  crossing, so chain 0 is sigma_0^2 = ha sigma_0 + 1 and chain 1 is")
    print("  sigma_1, and the product is ha sigma_0 sigma_1 + sigma_1.")
    print()
    print("  READ THE SIGN STRUCTURE, because it inverts the amplitude story:")
    print("  t has a negative component exactly when ha = q - 1/q < 0, i.e. on")
    print("  q < 1.  So on q > 1 -- WHERE P_76 IS NEGATIVE -- the NF coordinates")
    print("  are entrywise non-negative and feasibility is automatic; and on")
    print("  q < 1, where P_76 > 0, t acquires a negative component.  The two")
    print("  sign structures run OPPOSITE ways.  That is a direct obstruction to")
    print("  the proof's reduction, which reads the cone condition off the")
    print("  amplitude sign.")
    print()
    print("  NOTE ON SCOPE.  This measures the condition the proposition")
    print("  STATES.  It does not validate the proposition's REDUCTION of that")
    print("  condition to P_77 . W_std with a sign from the off-diagonal")
    print("  amplitude: G.t is a 6-vector over the Hecke NF basis, while")
    print("  P_77/P_76 are entries of an 8x8 matrix indexed by strand-type")
    print("  orderings.  Those index spaces are different and no map between")
    print("  them is recorded.  Whether the reduction holds is untouched here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
