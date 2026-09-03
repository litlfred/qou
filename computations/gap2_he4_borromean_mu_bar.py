#!/usr/bin/env python3
"""gap2_he4_borromean_mu_bar.py — GAP-2, the OPEN step (bean qou-klgu / qou-ooqh):
run the validated Milnor mu-bar tower on the ⁴He link, count the Milnor-IRREDUCIBLE
(Borromean, mu-bar_ijk != 0 with WELL-DEFINED value) triples M3(⁴He), and test
whether the per-order 3-body energy e3*M3(⁴He) reproduces (part of) the 14.95 MeV
⁴He "magic surplus" over the C(4,2)=6 pairwise backbone.

Follows gap2_borromean_triple_count.py (which REFUTED the 3-clique reading: it
overshoots A>=5 by +13..24%) and binding_mn_milnor_linking.py (the validated
mu-bar machinery: Hopf lk=1, Borromean mu-bar_123=+-1, chain mu-bar=0).

## The crux: mu-bar INDETERMINACY (the honest subtlety)

Milnor's mu-bar(ijk) is only a well-defined integer invariant modulo the gcd of
the lower-order invariants (the pairwise linking numbers lk among {i,j,k}). For
the Borromean rings lk_ij=0, so mu-bar_123 is a genuine invariant (=+-1). For a
cluster where every bonded pair has lk=1 (Hopf pairs -- the nuclear contact
graph), mu-bar_ijk is defined only mod gcd(lk)=1, i.e. mu-bar_ijk = 0 in Z. So a
mutually-bonded (3-clique) triple is Milnor-REDUCIBLE: its triple-linking carries
no invariant content beyond the pairwise bonds. THIS is why the 3-clique count
over-counts. The irreducible M3 counts only triples whose pairwise lk vanish.

We compute mu-bar for several ⁴He link models AND report the pairwise-lk
indeterminacy for each triple, so the WELL-DEFINED irreducible count is explicit.

## Model / anti-fit

Per-order energies pinned per-ORDER on the minimal nucleus of each order
(D 2-body, T 3-body, ⁴He 4-body) -- NOT per-isotope fitting. The per-order-3
energy e3 = m_e*a_D^(3)*w3 is FIXED by the triton (the lightest 3-body nucleus),
then the ⁴He 3-body content is a PREDICTION from its link's irreducible triple
count. Anti-fit: e3 is NOT solved from the ⁴He residual.

EXPLORATORY, scope-(a). No production wiring, no fitted constant.

-- Ref: computations/binding_mn_milnor_linking.py (validated mu-bar tower)
-- Ref: computations/gap2_borromean_triple_count.py (3-clique refutation)
-- Ref: docs/audits/2026-07-11-gap2-borromean-triple-count.md
-- Ref: docs/workplans/2026-07-11-mnk-derivation-gaps.md (GAP-2)
"""
from __future__ import annotations

import sys
from itertools import combinations
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp  # noqa: E402
import _path_bridge  # noqa: F401,E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

D = 4  # Magnus truncation degree (enough for triple + quadruple linking)


def mul(p, r):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in r.items():
            m = m1 + m2
            if len(m) <= D:
                out[m] = out.get(m, 0) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def magnus_gen(i, sign):
    p = {(): 1}
    if sign > 0:
        p[(i,)] = 1
    else:
        for d in range(1, D + 1):
            p[tuple([i] * d)] = (-1) ** d
    return p


def magnus_word(word):
    p = {(): 1}
    for g, e in word:
        p = mul(p, magnus_gen(g, e))
    return p


def comm(a, b):
    return [(a, 1), (b, 1), (a, -1), (b, -1)]


def mu(longitudes, seq):
    """mu-bar(i_1..i_k) = coeff of X_{i_1}..X_{i_{k-1}} in Magnus image of l_{i_k}."""
    *pre, last = seq
    return magnus_word(longitudes[last]).get(tuple(pre), 0)


def lk(longitudes, i, j):
    """pairwise linking number lk_ij = coeff of X_i in Magnus(l_j)."""
    return magnus_word(longitudes[j]).get((i,), 0)


# ---- ⁴He link models (4 components = 4 nucleons) ----
# (A) all-Hopf tetrahedron K_4: each nucleon Hopf-links the other three.
#     longitude l_i = product of meridians of the 3 neighbours.
HE4_HOPF_K4 = {i: [(j, 1) for j in (1, 2, 3, 4) if j != i] for i in (1, 2, 3, 4)}

# (B) Borromean triple on {1,2,3} + a 4th component Hopf-linked to all
#     (a "Borromean core + apex" model: the 3-body core is genuinely irreducible).
HE4_BOR_CORE = {
    1: comm(2, 3) + [(4, 1)],
    2: comm(3, 1) + [(4, 1)],
    3: comm(1, 2) + [(4, 1)],
    4: [(1, 1), (2, 1), (3, 1)],
}

# (C) pure 4-component Brunnian (Borromean-4): every proper sublink is trivial;
#     the irreducible content is the single 4-body invariant. Longitudes as
#     nested commutators (standard Milnor Brunnian presentation, degree-3 core).
HE4_BRUNNIAN = {
    1: comm(2, 3),
    2: comm(3, 4),
    3: comm(4, 1),
    4: comm(1, 2),
}


def analyse(name, L):
    print(f"\n### {name}")
    comps = sorted(L)
    # pairwise linking
    lks = {}
    for i, j in combinations(comps, 2):
        lks[(i, j)] = lk(L, i, j)
    print("  pairwise lk:", {f"{i}{j}": v for (i, j), v in lks.items()})
    # triples: mu-bar and its indeterminacy (gcd of pairwise lk in the triple)
    m3_welldef = 0
    triples = []
    for tr in combinations(comps, 3):
        a, b, c = tr
        val = mu(L, (a, b, c))
        # indeterminacy modulus = gcd of the three pairwise lk within the triple
        g = 0
        for i, j in combinations(tr, 2):
            g = gcd(g, abs(lks[(i, j)]))
        welldef = (g == 0)          # invariant well-defined iff pairwise lk all 0
        irr = welldef and (val != 0)
        m3_welldef += 1 if irr else 0
        triples.append((tr, val, g, welldef, irr))
        print(f"  triple {tr}: mu-bar={val:+d}  indet.mod={g}  "
              f"{'WELL-DEF' if welldef else 'reducible (mod '+str(g)+')'}"
              f"{'  -> IRREDUCIBLE' if irr else ''}")
    # 4-body (only well-defined if all lower invariants vanish); needs >=4 comps
    if len(comps) >= 4:
        m4 = mu(L, (1, 2, 3, 4))
        all_lk_zero = all(v == 0 for v in lks.values())
        m4_welldef = all_lk_zero and (m4 != 0)
        print(f"  4-body mu-bar_1234 = {m4:+d}   "
              f"({'WELL-DEF (all lk=0)' if all_lk_zero else 'indeterminate (some lk!=0)'})")
    else:
        m4, m4_welldef = 0, False
    print(f"  => M3_irreducible = {m3_welldef},  M4 = {1 if m4_welldef else 0}")
    return m3_welldef, (1 if m4_welldef else 0)


def main() -> int:
    from codata_constants import (
        AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
        AME_B_HE4_MEV_VALIDATION,
    )
    BD = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    BT = mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION))
    BHe = mp.mpf(str(AME_B_HE4_MEV_VALIDATION))

    print("=== GAP-2: ⁴He Milnor-irreducible triple count + energy test ===")

    # --- validate the machinery on the reference links first ---
    HOPF = {1: [(2, 1)], 2: [(1, 1)]}
    BOR = {1: comm(2, 3), 2: comm(3, 1), 3: comm(1, 2)}
    assert lk(HOPF, 1, 2) == 1, "Hopf lk"
    assert mu(BOR, (1, 2, 3)) in (1, -1) and lk(BOR, 1, 2) == 0, "Borromean"
    print("machinery validated: Hopf lk=1; Borromean mu-bar_123=+-1, pairwise lk=0.")

    # --- per-order energies, pinned per-ORDER on D / T (clique M3(T)=1) ---
    # e2 from D (M2=1); e3 from T (M2=3, M3=1 -- the single triton triple).
    e2 = BD / 1
    # triton: is its single triple irreducible? compute for the natural triton link.
    m3T, _ = analyse("triton T (Borromean 3-core)", BOR)   # natural 3-body model
    e3 = (BT - e2 * 3) / max(m3T, 1)
    print(f"\n  e2 = {float(e2):.4f} MeV (deuteron bond)")
    print(f"  e3 = {float(e3):.4f} MeV (triton 3-body, per-order pin; M3(T)={m3T})")

    # --- ⁴He surplus over the pairwise backbone ---
    surplus = BHe - e2 * 6
    print(f"\n  ⁴He magic surplus over C(4,2)=6 pairwise backbone: "
          f"B(⁴He) - 6*e2 = {float(BHe):.3f} - {float(6*e2):.3f} = {float(surplus):.4f} MeV")

    # --- ⁴He link models: M3_irreducible + M4 ---
    results = {}
    for nm, L in [("⁴He (A) all-Hopf K4", HE4_HOPF_K4),
                  ("⁴He (B) Borromean-core + apex", HE4_BOR_CORE),
                  ("⁴He (C) Brunnian 4-body", HE4_BRUNNIAN)]:
        results[nm] = analyse(nm, L)

    # --- energy test: does e3*M3(⁴He) reproduce the surplus (3-body attribution)? ---
    print("\n=== energy test: is the ⁴He surplus a 3-body (e3*M3) term? ===")
    print(f"  target surplus = {float(surplus):.4f} MeV;  e3 = {float(e3):.4f} MeV")
    for nm, (m3, m4) in results.items():
        e3pred = e3 * m3
        print(f"  {nm:>34}: M3_irr={m3} M4={m4}  e3*M3 = {float(e3pred):.4f} MeV "
              f"({'MATCH' if abs(e3pred-surplus) < 1 else f'off by {float(e3pred-surplus):+.2f}'})")

    print("\nHONEST READING: report which model (if any) gives M3_irr with e3*M3 ~ surplus,")
    print("and whether the surplus is 3-body (M3) or forced to 4-body (M4) by the mu-bar")
    print("indeterminacy (all-bonded clusters have pairwise lk!=0 -> M3_irr=0).")

    # witness
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("gap2-he4-borromean-mu-bar", engine="python-magnus")
        wb.set_description(
            "GAP-2 open step (bean qou-klgu): Milnor mu-bar tower on ⁴He link models, "
            "counting the WELL-DEFINED irreducible triple count M3 (mu-bar_ijk != 0 with "
            "vanishing pairwise lk indeterminacy) and the 4-body M4. Tests whether the "
            "per-order 3-body energy e3*M3(⁴He) reproduces the 14.95 MeV magic surplus. "
            "e3 pinned per-order on the triton (anti-fit). EXPLORATORY, no wiring.")
        from _precision import fmt
        wb.add_data("per_order_energy_MeV", {"e2": fmt(e2), "e3": fmt(e3)})
        wb.add_data("he4_surplus_MeV", fmt(surplus))
        wb.add_data("models", {nm: {"M3_irr": m3, "M4": m4} for nm, (m3, m4) in results.items()})
        wb.add_data("free_parameters", 0)
        # q0Anchor DECLARED, not defaulted. `resolve_q0_anchor` returns "proton" for
        # any stem absent from the manifest -- the runtime DEFAULT, not evidence -- so
        # an undeclared witness goes out asserting a pin it never used, and
        # `q0_anchor_ratchet --strict` counts it as unstamped. Declared 2026-08-29,
        # bean `qou-6u53`, on an import-cone trace plus the absence of any q_0 value
        # in the payload.
        out = wb.save({
            "q0Anchor": "independent",
            "q0AnchorReason": (
                "q0-independent: this producer never references q_0 at all. Its only "
                "path to `qou_substrate.constants` is the CODATA mass table reached via "
                "`codata_2022_source`, and importing a table is not computing at a pin."
            ),
        })
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
