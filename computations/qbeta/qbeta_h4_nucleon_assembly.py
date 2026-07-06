#!/usr/bin/env python3
"""
H4 nucleon Markov-assembly — shared machinery for the route-A c4^even build (bean 8we6).

Formalize-first status
----------------------
Route B (re-decompose the unchanged H3 element at lambda|-4) is PRUNED and
machine-checked (`QOU/QBeta/H4RouteBBranchingPrune.lean`, PR #3273): the five
lambda|-4 readings of an H3 element are fixed sums of its three lambda|-3
readings, carrying no independent N=4 DOF.  Route A is the surviving path: a
genuine c4^even rung needs an H4 object with sigma_2-support (a word touching a
4th strand).

What this module does
---------------------
A HEADLESS, print-free, n-agnostic port of the Groebner-Shirshov reducer +
crossing algebra from `computations/free-neutron-decay.py`.  The nucleon "net"
functional the Q_beta ladder consumes is the AUGMENTATION (counit) of the
normal form:  net_side(q) = sum_w coeff_w(q)  over the reduced NF words (each
basis word -> 1).  `Delta(net) = net_neutron - net_proton`.  This reproduces the
committed `free-neutron-decay.witness.json` for the 3-quark (H3) object, then
extends the quark/strand list to 4 for the route-A build.

The confinement braid is the Borromean B3 = (sigma_0 sigma_1^{-1})^3 (gens 0,1);
the nucleon is B3 . prod_{i<j} crossing(type_i, type_j; gen=i).  Extending the
type list to 4 elements adds pairs (i,3) at gens {0,1,2} -> genuine sigma_2
support.  Removing the 4th strand's crossings recovers the H3 words exactly, so
the H3 ladder rungs c_2, c_3 are the g->0 limit (stability gate).

Base ring / precision: exact `sympy.Rational` coefficients in the formal
variable q (CLAUDE.md compute-author: exact arithmetic for Markov/NF identities;
no float in the algebra).  q0 evaluation is done only for reporting.

`-- Ref:` free-neutron-decay.py (H3 producer); audit
docs/audits/2026-07-03-8we6-h4-route-b-structural-prune.md (route-A requirements).
"""
from __future__ import annotations

import sympy as sp

q = sp.Symbol("q", positive=True)
HA = q - 1 / q  # Hecke constant  sigma_i - sigma_i^{-1} = q - q^{-1}

Term = dict  # { word_tuple(int,...) : sympy_coeff }


# ── element algebra ───────────────────────────────────────────
def mul(a: Term, b: Term) -> Term:
    """Concatenate-and-multiply two Hecke elements (pre-reduction)."""
    out: Term = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            w = wa + wb
            out[w] = sp.expand(out.get(w, sp.Integer(0)) + sp.expand(ca * cb))
    return {w: c for w, c in out.items() if c != 0}


def reduce_nf(terms: Term, max_iter: int = 100000) -> Term:
    """Groebner-Shirshov normal form (headless port of free-neutron-decay.reduce_verbose).

    Orienting rules (identical to the H3 producer):
      R1 Hecke        sigma_i^2 -> HA*sigma_i + 1
      R2 far-commute  sigma_i sigma_j -> sigma_j sigma_i  (|i-j|>=2, i>j: sort ascending)
      R3 Yang-Baxter  sigma_i sigma_{i+1} sigma_i -> sigma_{i+1} sigma_i sigma_{i+1}
                       (only when the RHS triple is lexicographically smaller)
    n-agnostic: generators are integer indices; nothing is special-cased to n=3.
    """
    terms = {w: c for w, c in terms.items() if c != 0}
    changed = True
    it = 0
    while changed and it < max_iter:
        changed = False
        new: Term = {}
        for word, coeff in terms.items():
            if coeff == 0:
                continue
            did = False
            # R1 Hecke
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1] and word[pos] >= 0:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    w1, w2 = pre + (i,) + suf, pre + suf
                    new[w1] = sp.expand(new.get(w1, sp.Integer(0)) + sp.expand(coeff * HA))
                    new[w2] = sp.expand(new.get(w2, sp.Integer(0)) + coeff)
                    did = changed = True
                    break
            if did:
                continue
            # R2 far-commutation (sort ascending)
            for pos in range(len(word) - 1):
                i_gen, j_gen = word[pos], word[pos + 1]
                if abs(i_gen - j_gen) >= 2 and i_gen > j_gen and i_gen >= 0 and j_gen >= 0:
                    nw = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                    new[nw] = sp.expand(new.get(nw, sp.Integer(0)) + coeff)
                    did = changed = True
                    break
            if did:
                continue
            # R3 Yang-Baxter
            for pos in range(len(word) - 2):
                a, b, c2 = word[pos], word[pos + 1], word[pos + 2]
                if a == c2 and a >= 0 and b >= 0 and abs(a - b) == 1:
                    old_trip, new_trip = (a, b, a), (b, a, b)
                    if new_trip < old_trip:
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new[nw] = sp.expand(new.get(nw, sp.Integer(0)) + coeff)
                        did = changed = True
                        break
            if not did:
                new[word] = sp.expand(new.get(word, sp.Integer(0)) + coeff)
        terms = {w: c for w, c in new.items() if c != 0}
        it += 1
    return terms


# ── crossing constructors (verbatim algebra from free-neutron-decay.crossing) ──
def crossing(type_i: str, type_j: str, gen: int) -> Term:
    """Pairwise crossing element for two strand types at generator `gen`.

    u-u -> sigma_gen                       (positive)
    d-d -> sigma_gen - (q-q^{-1})          (Skein-mixed, same-flavour down)
    u-d -> sigma_gen - (q-q^{-1})/2        (averaged mixed)

    4th-strand tags (route A):
    e (lepton)     -> sigma_gen - (q-q^{-1})/2   (weak u-d-like averaged coupling)
    b (brane-tower)-> sigma_gen                  (bare Hopf; the `else`-branch)
    """
    pair = {type_i, type_j}
    if type_i == type_j == "u":
        return {(gen,): sp.Integer(1)}
    if type_i == type_j == "d":
        return {(gen,): sp.Integer(1), (): -HA}
    if pair == {"u", "d"}:
        return {(gen,): sp.Integer(1), (): -HA / 2}
    # route-A 4th strand: lepton couples weakly (averaged, u-d-like)
    if "e" in pair:
        return {(gen,): sp.Integer(1), (): -HA / 2}
    # route-A 4th strand: brane-tower bare Hopf coupling (else-branch)
    return {(gen,): sp.Integer(1)}


# ── confinement braid B3 = (sigma_0 sigma_1^{-1})^3 ───────────
def confinement_b3() -> Term:
    sig0 = {(0,): sp.Integer(1)}
    sig1_inv = {(1,): sp.Integer(1), (): -HA}
    unit = mul(sig0, sig1_inv)
    unit2 = reduce_nf(mul(unit, unit))
    return reduce_nf(mul(unit2, unit))


# ── nucleon normal form  B3 . prod crossings(types) ───────────
def nucleon_nf(types: list[str], lepton_couples_as: str | None = None) -> Term:
    """Reduced NF of  B3 . prod_{i<j} crossing(type_i,type_j; gen=i).

    `types` lists the strand flavours (u/d) plus any 4th-strand tag.  Any pair
    whose flavours are not both in {u,d} uses the crossing() else-branch (bare
    sigma), UNLESS `lepton_couples_as` names a flavour to treat the 4th-strand
    tag as (e.g. a lepton strand coupling as an averaged 'u-d' crossing).
    """
    elem = confinement_b3()
    A = len(types)
    for i in range(A):
        for j in range(i + 1, A):
            ti, tj = types[i], types[j]
            # optional remap: a non-(u/d) 4th-strand tag coupling as a chosen flavour pair
            if lepton_couples_as is not None:
                if ti not in ("u", "d"):
                    ti = lepton_couples_as
                if tj not in ("u", "d"):
                    tj = lepton_couples_as
            elem = reduce_nf(mul(elem, crossing(ti, tj, i)))
    return elem


def nucleon_nf_coupled(types: list[str], g) -> Term:
    """Coupling-parametrised NF: each 4th-strand crossing (a pair touching a
    non-(u/d) tag) is interpolated  C(g) = (1-g)*I + g*P  between the identity
    `I = {():1}` (g=0 -> 4th strand unlinked -> exactly the H3 object) and the
    physical crossing `P` (g=1).  Lets the stability gate be read as the g->0
    limit and the c_k^even response measured to linear order in g.  Quark-quark
    crossings (both in {u,d}) are unchanged (always physical)."""
    elem = confinement_b3()
    A = len(types)
    ident = {(): sp.Integer(1)}
    for i in range(A):
        for j in range(i + 1, A):
            ti, tj = types[i], types[j]
            P = crossing(ti, tj, i)
            if ti in ("u", "d") and tj in ("u", "d"):
                cx = P  # physical quark-quark crossing, no coupling knob
            else:
                # interpolate the 4th-strand crossing between identity and P
                cx = {}
                for w, c in ident.items():
                    cx[w] = cx.get(w, sp.Integer(0)) + (1 - g) * c
                for w, c in P.items():
                    cx[w] = sp.expand(cx.get(w, sp.Integer(0)) + g * c)
                cx = {w: c for w, c in cx.items() if c != 0}
            elem = reduce_nf(mul(elem, cx))
    return elem


def augmentation(elem: Term) -> sp.Expr:
    """net = sum_w coeff_w(q)  (counit; the functional the Q_beta ladder reads)."""
    return sp.simplify(sum(elem.values()))


def max_word_len(elem: Term) -> int:
    return max((len(w) for w in elem), default=0)


# ── self-test: reproduce the committed H3 Delta(net) ──────────
def _selftest_h3() -> None:
    import json
    import os

    net_n = augmentation(nucleon_nf(["u", "d", "d"]))
    net_p = augmentation(nucleon_nf(["u", "u", "d"]))
    dnet = sp.simplify(net_n - net_p)

    here = os.path.dirname(os.path.abspath(__file__))
    wit = json.load(open(os.path.join(here, "..", "free-neutron-decay.witness.json")))
    ref_n = sp.simplify(
        sum(sp.sympify(t["coefficient_symbolic"], locals={"q": q}) for t in wit["neutron"]["nf_terms"])
    )
    ref_p = sp.simplify(
        sum(sp.sympify(t["coefficient_symbolic"], locals={"q": q}) for t in wit["proton"]["nf_terms"])
    )
    ref_dnet = sp.simplify(ref_n - ref_p)

    ok_n = sp.simplify(net_n - ref_n) == 0
    ok_p = sp.simplify(net_p - ref_p) == 0
    ok_d = sp.simplify(dnet - ref_dnet) == 0
    print("H3 self-test vs free-neutron-decay.witness.json")
    print("  net_neutron matches:", ok_n)
    print("  net_proton  matches:", ok_p)
    print("  Delta(net)  matches:", ok_d)
    print("  Delta(net)(q) =", dnet)
    q0 = sp.Rational(110998, 100000)
    print("  delta_net @ q0~1.10998 =", float(dnet.subs(q, q0)), " (witness -0.18829062)")
    assert ok_n and ok_p and ok_d, "H3 reproduction FAILED — headless port drifted"
    print("  PASS — headless assembly reproduces the H3 augmentation exactly.")


if __name__ == "__main__":
    _selftest_h3()
