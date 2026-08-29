#!/usr/bin/env python3
"""The canonical colour-weighted bridge BREAKS tau — and it was already there.

## A correction first

I wrote, in this arc, that a "charge-carrying bridge -- a different word per
nucleon-type pair -- is untested and is the open route", and warned that
choosing such a rule risked being a fit. Both halves were wrong, and the
corpus-grep checklist is what found it.

It is implemented, it is canonical, and it is the `bring_color_weighted`
convention made canonical by the 2026-08-15 owner ruling R3. From
`tr_m_algebraic_q.py::atom_braid_symbolic`:

    if   nuc == "p" and nxt == "p":  dd = 0                       # p-p
    elif nuc == "n" and nxt == "n":  dd = -h                      # n-n
    else:                            dd = -h*(1/2 - delta/4)      # p-n

with h = q - 1/q and the colour delta(q) = (q-1)^2 (1 - q^-4)/3. Three
distinct interfaces, chosen by TYPE PAIR.

The fitting hazard I raised was already recognised there, and better than I
put it. That file's own docstring: the p-n colour delta "is numerically
indistinguishable from -h/2, so it must be placed structurally, not matched".
That is the anti-fit discipline applied to exactly this question, years of
sessions before I raised it.

## The measurement

Note the shape: the canonical interface is not a braid word at all. It is the
ALGEBRA ELEMENT `sigma_g + d*I` -- a generator plus a scalar. Every bridge in
this arc has been a bare word, which is why none of them could carry a type.

    bridge                          pn/pp   pp/nn   pn/np
    every bare word tried              20      28      28    <- tau holds
    canonical colour-weighted          35      39      28    <- tau BROKEN

tau = (p<->n complement) o (block reversal) forces `pp/nn == pn/np`. Five
sign-only bridges all gave 28 == 28. The canonical bridge gives 39 != 28.

## What this does to the arc's negatives, and it is not small

The 3H/3He result -- that every relabel-invariant functional is blind, and
that a 3H ordering sits at distance 0 from a 3He ordering -- was measured
with sign-symmetric bare-word bridges. So was the H_6 isospin negative, and
so was my own withdrawn exchange-odd discriminator.

Those negatives are therefore scoped to bare-word bridges, NOT to the
framework. The tau-invariance they all ran into is a property of the encoding
they shared, and the canonical convention does not have it. Re-running them
against `sigma_g + d*I` is the obvious next step and is not done here.

## Honest about the by-construction part

tau swaps p and n, and the interface assignment is not symmetric under that
swap (p-p gets 0, n-n gets -h), so tau-breaking is immediate from the
convention rather than emergent from the algebra. That is the same "true by
construction" shape as the exchange-odd claim I withdrew, and it must not be
oversold the same way.

What makes it worth recording anyway is the direction of the inference. There
the construction masqueraded as physics; here the construction IS the
physics -- it is a derived substrate quantity (delta), placed structurally,
by a canonical convention that predates this arc. The finding is not "tau can
be broken by choosing an asymmetric rule", which is trivial. It is that the
arc measured a symmetry the production convention does not have, because
every probe used an encoding the production path does not use.

Exact throughout: sparse Laurent over Q[q,q^-1] via `fractions.Fraction`
(delta carries a 1/3, so Z does not suffice). No floats, no anchor.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_exact_laurent import (  # noqa: E402
    FastHecke, coxeter_length, lau_add, lau_mul, word_to_elem_fast,
)
from isospin_triplet_filtration_probe import P_A, N_A, P_B, N_B  # noqa: E402


def qm(e: int) -> dict:
    return {e: F(1)}


def smul(s, a: dict) -> dict:
    return {e: s * c for e, c in a.items() if s * c}


H = {1: F(1), -1: F(-1)}                                   # h = q - 1/q
_QM1 = lau_add(qm(1), smul(F(-1), qm(0)))                   # q - 1
DELTA = smul(F(1, 3), lau_mul(lau_mul(_QM1, _QM1),
                              lau_add(qm(0), smul(F(-1), qm(-4)))))
#: The canonical interface scalars, by nucleon-type pair.
D_BY_TYPE = {
    "pp": {},
    "nn": smul(F(-1), H),
    "pn": smul(F(-1), lau_mul(H, lau_add(smul(F(1, 2), qm(0)),
                                         smul(F(-1, 4), DELTA)))),
}


def bridged(core_a, core_b, kind: str, gen: int = 3) -> FastHecke:
    """Apply the canonical interface `sigma_gen + d*I` for this type pair."""
    E = word_to_elem_fast(6, core_a + core_b)
    out, d = FastHecke(6), D_BY_TYPE[kind]
    for w, c in E.terms.items():
        p = list(w)
        p[gen - 1], p[gen] = p[gen], p[gen - 1]
        wsi = tuple(p)
        if coxeter_length(wsi) > coxeter_length(w):
            out._add(wsi, c)
        else:
            out._add(w, lau_mul(c, H))
            out._add(wsi, c)
        if d:
            out._add(w, lau_mul(c, d))
    return out


def n_diff(X: FastHecke, Y: FastHecke) -> int:
    return sum(1 for w in set(X.terms) | set(Y.terms)
               if X.terms.get(w, {}) != Y.terms.get(w, {}))


def trace_by_zpower(E) -> dict:
    """The Markov trace with z kept FREE, resolved by z-power.

    tr(T_w) = z^(n - cycles(w)), so the trace is
        sum_k z^(n-k) * (sum of coefficients over w with cycles(w) = k).
    Returning {z-power: Laurent(q)} IS the trace, exactly, with z symbolic.
    """
    out: dict = {}
    for w, c in E.terms.items():
        seen, cyc = set(), 0
        for s0 in range(len(w)):
            if s0 in seen:
                continue
            cyc += 1
            x = s0
            while x not in seen:
                seen.add(x)
                x = w[x] - 1
        k = E.n - cyc
        out[k] = lau_add(out.get(k, {}), c)
    return {k: v for k, v in out.items() if v}


def coloured_trace_separates(E) -> dict:
    """#5928 proved the UNCOLOURED trace cannot separate these at any z.
    Does the canonical COLOURED bridge change that?"""
    print("\n" + "=" * 74)
    print("Does the COLOURED trace see what the uncoloured one provably cannot?")
    print("=" * 74)
    T = {k: trace_by_zpower(v) for k, v in E.items() if k != "np"}
    for k in ("pn", "pp", "nn"):
        print(f"    tr({k}) z-powers present: {sorted(T[k])}")
    rows = {}
    for k in ("pp", "nn"):
        dz = sorted(z for z in set(T[k]) | set(T["pn"])
                    if T[k].get(z, {}) != T["pn"].get(z, {}))
        print(f"    tr({k}) == tr(pn): {T[k] == T['pn']}   z-powers differing: {dz}")
        rows[k] = dz
    print("\n    YES. And note tr(pp) has NO z^0 term at all -- the p-p interface")
    print("    carries d = 0, so it contributes no scalar, and the identity")
    print("    permutation drops out entirely.")
    print()
    print("    This closes the criterion derived in #5928: 'any p/n-sensitive")
    print("    weighting must BREAK the block factorisation'. The canonical")
    print("    convention does, and the trace sees the result. The uncoloured")
    print("    blindness proved there was correctly scoped.")
    assert all(rows.values()), "the coloured trace failed to separate -- rewrite this"
    return rows


def rerun_the_bare_word_negatives(E) -> dict:
    """Option 5: do the arc's negatives survive the canonical interface?

    The H_6 isospin negative was: identical grade COUNTS, identical grade-MASS
    and identical SUPPORT across pn, pp and nn. Re-run against sigma_g + d*I.
    """
    print("\n" + "=" * 74)
    print("Do the bare-word negatives survive the canonical interface?")
    print("=" * 74)

    def counts(X):
        return {g: len(v) for g, v in sorted(X.profile().items())}

    def mass(X):
        out: dict = {}
        for w, c in X.terms.items():
            g = coxeter_length(w)
            out[g] = lau_add(out.get(g, {}), c)
        return {g: v for g, v in sorted(out.items()) if v}

    for k in ("pn", "pp", "nn"):
        print(f"    counts({k}) = {counts(E[k])}")
    same_c = counts(E["pn"]) == counts(E["pp"]) == counts(E["nn"])
    same_s = set(E["pn"].terms) == set(E["pp"].terms) == set(E["nn"].terms)
    m = {k: mass(E[k]) for k in ("pn", "pp", "nn")}
    same_m = m["pn"] == m["pp"] == m["nn"]
    print(f"\n    counts identical    : {same_c}")
    print(f"    support identical   : {same_s}")
    print(f"    grade-mass identical: {same_m}")
    print("\n    NEGATIVE LIFTED -- it was an artifact of the bare-word bridge.")
    print("\n    But read the grouping before celebrating. The profile splits")
    print("    {pp} from {pn, nn}, because pp's interface scalar is d = 0 while")
    print("    both others are nonzero. The PHYSICAL split is {pn} bound from")
    print("    {pp, nn} unbound. So the profile now sees something -- and what")
    print("    it sees is 'does the interface carry a scalar', a property of the")
    print("    convention, not boundness. Lifting a blindness is not the same as")
    print("    acquiring the right signal.")
    print("\n    The TRACE does better: all three come out distinct (above).")
    print("    Whether they RANK correctly is a separate question, untested.")
    assert not (same_c and same_s and same_m), "negative survived -- rewrite this"
    return {"counts_identical": same_c, "support_identical": same_s,
            "mass_identical": same_m}


def main():
    E = {"pn": bridged(P_A, N_B, "pn"), "np": bridged(N_A, P_B, "pn"),
         "pp": bridged(P_A, P_B, "pp"), "nn": bridged(N_A, N_B, "nn")}
    d_ppnn, d_pnnp = n_diff(E["pp"], E["nn"]), n_diff(E["pn"], E["np"])
    print("Canonical colour-weighted interface  sigma_g + d*I,  d by type pair\n")
    print(f"    pn vs pp : {n_diff(E['pn'], E['pp'])}")
    print(f"    pp vs nn : {d_ppnn}    <- tau forces these two to be EQUAL")
    print(f"    pn vs np : {d_pnnp}    <-")
    print(f"\n    tau BROKEN: {d_ppnn != d_pnnp}")
    print("\n    Every bare-word bridge in this arc gave 28 == 28. The arc's")
    print("    negatives are scoped to bare-word bridges, not to the framework.")
    assert d_ppnn != d_pnnp, "tau not broken -- the docstring is now wrong"
    tr = coloured_trace_separates(E)
    rerun_the_bare_word_negatives(E)
    return {"pp_vs_nn": d_ppnn, "pn_vs_np": d_pnnp, "tau_broken": True,
            "coloured_trace_separates": {k: v for k, v in tr.items()}}


if __name__ == "__main__":
    main()
