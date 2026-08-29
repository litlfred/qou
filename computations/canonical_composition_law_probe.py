#!/usr/bin/env python3
"""The canonical composition law: strong and charge channels SEPARATE.

`body_order_composition_probe` derived G_A(x) = x^(A-1) * G_1(x)^A for the
bare-word bridge, and flagged that the canonical interface is sigma_g + d*I
with d chosen by nucleon-type pair, whose scalar part it did not carry.

Carrying it is one line of algebra. Multiplying by sigma_g + d*I on a fresh
interface gives E.sigma_g + d*E, and QOU.Knot.JetGradePromotion says the
first term is a rigid +1 shift, so in generating-function terms

    G_{E.(sigma_g + d I)}(x) = x * G_E(x) + d * G_E(x) = (x + d) * G_E(x)

-- the interface factor is (x + d), not x. Hence

    G_A(x) = [ prod over bonds (x + d_bond) ] * G_1(x)^A

## The part worth the trouble

G_1 is THE SAME for a proton and a neutron -- measured, and it must be: they
are mirror words with identical grade profiles, which is exactly why the
bare-word encoding could not see p from n at all.

So every nucleon-type dependence sits in the bond factors and nowhere else.
The law separates:

    G_1(x)^A              type-BLIND, one factor per nucleon    (strong)
    prod (x + d_bond)     type-DEPENDENT, one factor per bond   (charge)

That is the channel separation stated as a factorisation rather than as a
hope, and it is why the coloured interface breaks tau while no sign-only
bridge could: tau permutes nucleon types, which moves the d_bond factors and
leaves G_1^A alone.

## Verified exactly

A=2, all three pairings: (x + d)*G_1^2 reproduces the element exactly.
A=3, two bonds with DIFFERENT d: 3H (nnp), 3He (ppn), pnp and ppp all exact.

Coefficient-by-coefficient over Q[q,q^-1], never by term count.

## Scope

Still a law about the FILTRATION generating function. Reading body-order
weights w_n off these coefficients additionally needs the SW periods
a_D^(n), which `conj:binding-manybody-eq-jet-filtration` carries as
conjectural. The factorisation says WHERE the charge dependence lives; it
does not supply a binding energy.

The d values are the canonical ones (bring_color_weighted, ruling R3), read
from tr_m_algebraic_q.py, not chosen here. Nothing is fitted.

Exact: sparse Laurent over Q[q,q^-1] via Fraction (the colour delta has 1/3).
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from canonical_color_bridge_tau_probe import D_BY_TYPE  # noqa: E402
from hecke_exact_laurent import (  # noqa: E402
    FastHecke, coxeter_length, lau_add, lau_mul, word_to_elem_fast,
)

H_LAU = {1: F(1), -1: F(-1)}


def grade_gf(E) -> dict:
    out: dict = {}
    for w, c in E.terms.items():
        g = coxeter_length(w)
        out[g] = lau_add(out.get(g, {}), c)
    return {g: v for g, v in sorted(out.items()) if v}


def proton_core(k: int) -> list:
    a, b = 3 * k + 1, 3 * k + 2
    return [a, -b, a, -b, a, -b]


def neutron_core(k: int) -> list:
    a, b = 3 * k + 1, 3 * k + 2
    return [-a, b, -a, b, -a, b]


def polymul(P: dict, Q: dict) -> dict:
    out: dict = {}
    for e1, c1 in P.items():
        for e2, c2 in Q.items():
            t = lau_mul(c1, c2)
            if t:
                out[e1 + e2] = lau_add(out.get(e1 + e2, {}), t)
    return {e: v for e, v in out.items() if v}


def apply_interface(E, gen: int, d: dict):
    """Multiply by the canonical interface `sigma_gen + d*I`."""
    out = FastHecke(E.n)
    for w, c in E.terms.items():
        p = list(w)
        p[gen - 1], p[gen] = p[gen], p[gen - 1]
        wsi = tuple(p)
        if coxeter_length(wsi) > coxeter_length(w):
            out._add(wsi, c)
        else:
            out._add(w, lau_mul(c, H_LAU))
            out._add(wsi, c)
        if d:
            out._add(w, lau_mul(c, d))
    return out


def bond_factor(kind: str) -> dict:
    """The polynomial `x + d_kind`."""
    d = D_BY_TYPE[kind]
    t = {1: {0: F(1)}}
    if d:
        t[0] = dict(d)
    return t


def _norm(P: dict) -> dict:
    return {e: {k: F(v) for k, v in c.items()} for e, c in P.items()}


def main():
    G1p = grade_gf(word_to_elem_fast(3, proton_core(0)))
    G1n = grade_gf(word_to_elem_fast(3, neutron_core(0)))
    print("Canonical composition law\n")
    print(f"    G_1(proton) == G_1(neutron): {G1p == G1n}")
    print("    -> every type dependence must sit in the BOND factors.")
    assert G1p == G1n

    print("\n  A=2, one bond:")
    for label, (c0, c1, kind) in {
        "p n": (proton_core, neutron_core, "pn"),
        "p p": (proton_core, proton_core, "pp"),
        "n n": (neutron_core, neutron_core, "nn"),
    }.items():
        E = apply_interface(word_to_elem_fast(6, c0(0) + c1(1)), 3, D_BY_TYPE[kind])
        pred = polymul(bond_factor(kind), polymul(G1p, G1p))
        ok = _norm(pred) == _norm(grade_gf(E))
        print(f"    {label}: (x + d)*G_1^2 exact: {ok}")
        assert ok, f"A=2 law failed for {label}"

    print("\n  A=3, two bonds with different d:")
    for label, (c0, c1, c2, k01, k12) in {
        "3H  n n p": (neutron_core, neutron_core, proton_core, "nn", "pn"),
        "3He p p n": (proton_core, proton_core, neutron_core, "pp", "pn"),
        "p n p    ": (proton_core, neutron_core, proton_core, "pn", "pn"),
        "p p p    ": (proton_core, proton_core, proton_core, "pp", "pp"),
    }.items():
        E = word_to_elem_fast(9, c0(0) + c1(1) + c2(2))
        E = apply_interface(E, 3, D_BY_TYPE[k01])
        E = apply_interface(E, 6, D_BY_TYPE[k12])
        # start from the multiplicative UNIT, not from x -- a factor equal to
        # the sentinel is otherwise silently dropped when d = 0 (the pp bond).
        fac = {0: {0: F(1)}}
        for k in (k01, k12):
            fac = polymul(fac, bond_factor(k))
        pred = polymul(fac, polymul(G1p, polymul(G1p, G1p)))
        ok = _norm(pred) == _norm(grade_gf(E))
        print(f"    {label}: prod(x + d_bond)*G_1^3 exact: {ok}")
        assert ok, f"A=3 law failed for {label}"

    print("\n  G_A(x) = [prod over bonds (x + d_bond)] * G_1(x)^A")
    print("    G_1^A            type-blind, per nucleon   (strong)")
    print("    prod (x+d_bond)  type-dependent, per bond  (charge)")
    return {"law": "G_A = prod(x + d_bond) * G_1^A"}


if __name__ == "__main__":
    main()
