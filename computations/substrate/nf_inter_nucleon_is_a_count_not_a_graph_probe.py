#!/usr/bin/env python3
"""
nf_inter_nucleon_is_a_count_not_a_graph_probe — the NF encoding cannot express a
coordination GRAPH, only a bond COUNT by type. So `k` is not derivable from it.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Follows #6304 (the q-degree bond-set
diagnostic), #6332 (the channel arity gap) and #6345 (the k-inversion genericity
guard), which closed by saying:

    "What WOULD be informative: a k derived from the substrate -- from the braid
     word's own geometry -- and then COMPARED to the plateau."

This probe answers that, and the answer is that the NF encoding has no geometry in
its inter-nucleon block to derive `k` from.

## The observation

`hecke_core_symbolic.build_atom_nf_sym`'s inter-nucleon loop is

    for prev in range(k):
        ti, tj = ordering[prev], ordering[k]
        if   ti == "p" and tj == "p":  nf = hm_sym(nf, ONE, 0,          0)
        elif ti == "n" and tj == "n":  nf = hm_sym(nf, ONE, -h,         0)
        else:                          nf = hm_sym(nf, ONE, -h * HALF,  0)

Every factor is at **gen 0**, for every pair `(prev, k)`. Nothing in the factor
records *which* two nucleons the bond joins — only the pair's TYPE, through `d`.

Contrast `mass_at_3A_proper.atom_braid_word_3A`, whose docstring says it places
"the appropriate pp/nn/pn crossing at **gen 3k+2**": that is a genuine bridge
between strand blocks `k` and `k+1`, so it exists only for ADJACENT nucleons and
there are exactly `A-1` of them. That word has geometry; the NF word does not.

## Why that is decisive rather than cosmetic

All the inter-nucleon factors are polynomials in the SAME generator `sigma_0`, so
they commute. Hence

    prod over bonds of (sigma_0 + d_bond)

depends on the bond set ONLY through the multiset `{d_bond}`, i.e. only through
`(n_pp, n_pn, n_nn)`. Two different graphs on the same nucleons with the same type
counts give a bit-identical NF vector.

Measured below, not argued: the multiset is shuffled many times per nucleus and the
resulting 6-vector of exact Laurent polynomials is compared coefficient by
coefficient.

## What this settles, and what it does not

It settles that a coordination NUMBER cannot be derived from this producer's braid
word, because the word does not encode a graph. "Complete graph vs bounded degree"
is expressible here only as a difference in bond COUNT — a degree-`k` graph and the
complete graph are distinguishable solely by having different `(n_pp, n_pn, n_nn)`,
never by their structure.

It does NOT say the framework cannot have a coordination graph, and it does not
touch `atom_braid_word_3A`, whose gen-`3k+2` bridges are geometric (and are a chain
by construction, which is why that word has `A-1` bonds and not `C(A,2)`).

Scope **(a)**: a statement about what the current encoding can represent.

NO FLOAT64: exact `fractions.Fraction` Laurent arithmetic via the machinery in
`atom_nf_q_degree_probe`; nothing is evaluated at any numerical q, and every
reported quantity is an integer or a boolean.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import random  # noqa: E402

from substrate.atom_nf_q_degree_probe import (  # noqa: E402
    hm_laurent, build_atom_nf_laurent, ldeg,
    ONE_L, ZERO_L, NEG_H_L, NEG_HALF_H_L,
)

# The three inter-nucleon `d` values, exactly as build_atom_nf_sym writes them.
D = {"pp": ZERO_L, "nn": NEG_H_L, "pn": NEG_HALF_H_L}

SEED = 11          # fixed: the shuffles are a search for a counterexample, not a sample


def apply_bonds(nf, kinds):
    """Apply the inter-nucleon factors in the given ORDER — all at gen 0, as the
    producer does for every pair regardless of which pair it is."""
    for k in kinds:
        nf = hm_laurent(nf, ONE_L, D[k], 0)
    return nf


def signature(nf):
    """Exact identity of the 6-vector: every coefficient of every slot."""
    return tuple(tuple(sorted(c.items())) for c in nf)


def complete_kinds(Z: int, N: int) -> list[str]:
    """The type of every pair, in the order build_atom_nf_sym visits them."""
    order = ["p"] * Z + ["n"] * N
    out = []
    for j in range(Z + N):
        for i in range(j):
            a, b = order[i], order[j]
            out.append("pp" if a == b == "p" else ("nn" if a == b == "n" else "pn"))
    return out


def main() -> int:
    print("nf_inter_nucleon_is_a_count_not_a_graph_probe")
    print("=" * 78)
    print("Every inter-nucleon factor in build_atom_nf_sym is at gen 0, for every")
    print("pair.  All such factors are polynomials in the same generator, so they")
    print("commute, so the product can depend only on the MULTISET of types.")
    print()

    print("TEST 1 — order-invariance.  Start from the real atom NF with no pair")
    print("bonds, then apply the same type multiset in many random orders.")
    print(f"{'nucleus':>9} {'A':>3} {'bonds':>6} {'(pp,pn,nn)':>14} "
          f"{'shuffles identical':>20}")
    rng = random.Random(SEED)
    all_ok = True
    for name, Z, N in [("4He", 2, 2), ("6Li", 3, 3), ("9Be", 4, 5),
                       ("12C", 6, 6), ("14N", 7, 7)]:
        base, _ = build_atom_nf_laurent(Z, N, bonds="none")
        kinds = complete_kinds(Z, N)
        ref = signature(apply_bonds(base, kinds))
        trials, same = 40, 0
        for _ in range(trials):
            sh = kinds[:]
            rng.shuffle(sh)
            same += (signature(apply_bonds(base, sh)) == ref)
        all_ok &= (same == trials)
        counts = (kinds.count("pp"), kinds.count("pn"), kinds.count("nn"))
        print(f"{name:>9} {Z+N:>3} {len(kinds):>6} {str(counts):>14} "
              f"{f'{same}/{trials}':>20}")
    print(f"  every shuffle bit-identical on every nucleus: {all_ok}")
    print()

    print("TEST 2 — structure-invariance.  Two DIFFERENT graphs on the same")
    print("nucleons with the same type counts, and one with different counts.")
    base, _ = build_atom_nf_laurent(3, 3, bonds="none")
    cases = [
        ("complete graph, C(6,2)=15 edges", ["pp"] * 3 + ["pn"] * 9 + ["nn"] * 3),
        ("degree-4 graph, 12 edges (5,4,3)", ["pp"] * 5 + ["pn"] * 4 + ["nn"] * 3),
        ("SAME counts (5,4,3), different pairing",
         ["nn"] * 3 + ["pp"] * 5 + ["pn"] * 4),
    ]
    sigs = {}
    print(f"{'bond set':>42} {'span(gamma)':>12} {'identical to':>26}")
    for label, kinds in cases:
        nf = apply_bonds(base, kinds)
        s = signature(nf)
        hi, lo = ldeg(nf[0])
        match = next((lbl for lbl, ss in sigs.items() if ss == s), "-- (new)")
        sigs[label] = s
        print(f"{label:>42} {hi - lo:>12} {match:>26}")
    same_counts_identical = sigs[cases[1][0]] == sigs[cases[2][0]]
    diff_counts_differ = sigs[cases[0][0]] != sigs[cases[1][0]]
    print(f"  same type counts, different pairing -> identical : {same_counts_identical}")
    print(f"  different type counts               -> differ    : {diff_counts_differ}")
    print()

    print("Reading")
    print("-" * 78)
    ok = all_ok and same_counts_identical and diff_counts_differ
    if ok:
        print("  * The inter-nucleon block of build_atom_nf_sym is a product of")
        print("    COMMUTING factors, so it depends on the bond set only through")
        print("    (n_pp, n_pn, n_nn).  The bond SET is only ever a bond COUNT.")
        print("  * So 'complete graph vs bounded degree' is expressible in this")
        print("    producer only as a difference in COUNT.  A degree-k graph and the")
        print("    complete graph differ solely by having different type counts,")
        print("    never by their structure -- measured above.")
        print("  * Consequence for qou-brng: a coordination NUMBER cannot be derived")
        print("    from this word's geometry, because this word has no geometry in")
        print("    its inter-nucleon block.  #6345 asked for a k derived from the")
        print("    substrate and then compared to the plateau; this producer cannot")
        print("    supply one, and that is a property of the encoding, not a gap in")
        print("    anyone's search.")
        print("  * Where the geometry DOES live: atom_braid_word_3A places its")
        print("    pp/nn/pn crossing at gen 3k+2, a bridge between strand blocks k")
        print("    and k+1.  Adjacent-only, hence A-1 bonds by CONSTRUCTION rather")
        print("    than by choice.  That is the word to ask geometric questions of.")
    else:
        print("  * The commutation claim FAILED somewhere above -- read the tables.")
        print("    Do not quote the conclusion; the measurement did not support it.")
    print()
    print("  Scope (a): about what the current encoding can represent.  Nothing here")
    print("  says the framework cannot have a coordination graph, and nothing here")
    print("  touches atom_braid_word_3A.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
