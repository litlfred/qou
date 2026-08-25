#!/usr/bin/env python3
# polynomial_q_not_applicable: exact-integer knot invariant; no substrate q read.
"""Braid index from Morton-Franks-Williams — derived, not recalled (qou-dr8m).

`qou-xpgq` flagged `braid index(6_1) = 4` as a literature-recalled,
unverified, load-bearing value. This producer derives it.

That bean is on the unmerged branch of PR #5294, so `beans show qou-xpgq`
returns nothing until it lands; the PR body states the flag verbatim
("`6_1`'s braid index is **not** verified against any in-repo source").

## What is derived here

For each knot: the exact two-variable HOMFLY of a braid closure
(`homfly_skein_braid`, integer Laurent arithmetic, no floats), its
`v`-degree spread, and the MFW lower bound `spread/2 + 1` on the braid
index. For 6_1 the bound is then **met** by an explicit 4-strand braid
found by search and confirmed by SnapPy identification, so the braid
index is pinned exactly rather than bounded.

## Why a new HOMFLY was needed (measured 2026-08-21)

Neither existing corpus source can supply a `v`-degree:

- `homflypt_engine.homflypt_from_braid` is symbolic only for
  `n_strands == 2`. Its `n >= 3` branch evaluates numerically at the
  substrate q_0 and stores the resulting float in `terms[(0, 0)]`, so a
  degree read returns spread **0** with no error. For MFW that is worse
  than a crash: it yields the vacuous bound `>= 1`, which is consistent
  with every hypothesis. Recorded as a defect, not fixed here.
- The corpus Markov trace is specialised to SU(2)/Temperley-Lieb
  (convention D, `z = q^3/(q^2+1)`). That specialisation *is* the
  collapse of the `v` direction, and `v`-degree is the entire content of
  MFW. So the C-vs-D convention question does not gate this work.

## Validation gates (all must pass)

1. Textbook HOMFLY reproduced exactly for the unknot, Hopf link, 3_1,
   4_1, 5_1.
2. Conway specialisation `P(v=1, z) = grad(z)` for all seven knots --
   an independent invariant, not a restatement of the computation.
3. MFW bound equals the tabulated braid index for the six knots whose
   braid index is not in question (3_1, 4_1, 5_1, 5_2, 6_2, 6_3). These
   are the machinery gate; note every one of them has braid index 2 or 3,
   so they do NOT by themselves test 3-vs-4 discrimination.
4. The torus family T(2,3), T(2,5), T(3,4), T(3,5), T(4,5), whose braid
   index is min(p, q) by a THEOREM (MFW is sharp on torus knots) rather
   than by a table. T(4,5) is pinned at 4, which supplies the 3-vs-4
   discrimination gate 3 lacks, on a knot that is not 6_1.

Scope: this derives the braid index. It does **not** prove MFW; the two
inequalities are carried as hypotheses in
`QOU.Knot.MortonFranksWilliams`, and proving them is tracked separately.
Nothing here is wired to production.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from homfly_skein_braid import homfly, mfw_data, traverse  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Textbook HOMFLY, Lickorish (v, z): v^-1 P(L+) - v P(L-) = z P(L0).
TEXTBOOK = {
    "unknot": ((), 1, {(0, 0): 1}),
    "hopf+": ((1, 1), 2, {(1, -1): 1, (1, 1): 1, (3, -1): -1}),
    "3_1": ((1, 1, 1), 2, {(2, 0): 2, (2, 2): 1, (4, 0): -1}),
    "4_1": ((1, -2, 1, -2), 3, {(-2, 0): 1, (0, 0): -1, (0, 2): -1, (2, 0): 1}),
    "5_1": ((1, 1, 1, 1, 1), 2,
            {(4, 0): 3, (6, 0): -2, (4, 2): 4, (6, 2): -1, (4, 4): 1}),
}

# Conway polynomial as {z-exponent: coeff}; P(v=1, z) must equal it.
CONWAY = {
    "3_1": {0: 1, 2: 1}, "4_1": {0: 1, 2: -1}, "5_1": {0: 1, 2: 3, 4: 1},
    "5_2": {0: 1, 2: 2}, "6_1": {0: 1, 2: -2},
    "6_2": {0: 1, 2: -1, 4: -1}, "6_3": {0: 1, 2: 1, 4: 1},
}

# Tabulated braid indices. 6_1 is the value under test and is EXCLUDED
# from the machinery gate -- it is derived below, then compared.
TABULATED = {"3_1": 2, "4_1": 3, "5_1": 2, "5_2": 3, "6_2": 3, "6_3": 3}

# Torus knots T(p, q), as the closure of (sigma_1 ... sigma_{p-1})^q on p
# strands. Their braid index is min(p, q) by a THEOREM (MFW is sharp on
# torus knots -- Franks-Williams, Murasugi), not by a table, so this is an
# independent check of the machinery rather than a lookup. With p < q the
# word is already on min(p,q) strands, so each one is PINNED, not bounded.
#
# This is the gate that 3_1/4_1/5_1/5_2/6_2/6_3 could not supply: every one
# of those has braid index 2 or 3, so none of them tests whether the bound
# can separate 4 from 3. T(4,5) does, and it is not 6_1.
TORUS = {(2, 3): 2, (2, 5): 2, (3, 4): 3, (3, 5): 3, (4, 5): 4}


# The 4-strand representative of 6_1 found by exhaustive search over
# writhe-1 words on three generators (MFW forces writhe exactly 1 when
# the spread is 6 and n is 4), confirmed by SnapPy identify -> 6_1/m032.
SIX_ONE_4BRAID = [1, 1, 2, -1, -3, 2, -3]


def _conway(P):
    out = {}
    for (_, j), c in P.t.items():
        out[j] = out.get(j, 0) + c
    return {j: c for j, c in out.items() if c}


def main() -> int:
    print("=" * 78)
    print(" Braid index via Morton-Franks-Williams — exact HOMFLY, no floats")
    print("=" * 78)

    import snappy

    wb = WitnessBuilder("homfly-braid-index-mfw", engine="skein-recursion-exact")
    wb.set_description(
        "Derives braid indices from the exact two-variable HOMFLY of braid "
        "closures (descending-diagram skein recursion, integer Laurent "
        "arithmetic) via the Morton-Franks-Williams bound spread/2+1. "
        "Settles braid index(6_1) = 4: lower bound from spread 6, upper "
        "bound from the explicit 4-strand word [1,1,2,-1,-3,2,-3] "
        "(SnapPy-identified as 6_1/m032), replacing the literature-recalled "
        "value flagged by qou-xpgq. Gated on textbook HOMFLY for 5 links, "
        "the Conway specialisation P(v=1,z) for 7 knots, and agreement "
        "with the tabulated braid index for the 6 knots not under test, and "
        "the torus family T(2,3)..T(4,5) against the theorem braid index = "
        "min(p,q) -- T(4,5) pins 4 on a knot that is not 6_1, supplying the "
        "3-vs-4 discrimination the tabulated set cannot. "
        "Scope-(a); nothing wired. Bean qou-dr8m."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    ok = True

    print("\n[1] textbook HOMFLY")
    for name, (word, n, expect) in TEXTBOOK.items():
        got = homfly(word, n).t
        match = got == expect
        ok = ok and match
        print(f"    {name:8s} {'OK' if match else 'MISMATCH'}")

    print("\n[2] Conway specialisation P(v=1, z)")
    knots, spreads = {}, {}
    for k in CONWAY:
        w = snappy.Link(k).braid_word()
        n = max(abs(x) for x in w) + 1
        d = mfw_data(w, n)
        cw = _conway(homfly(w, n))
        match = cw == CONWAY[k]
        ok = ok and match
        knots[k] = {**d, "conway": {str(j): c for j, c in sorted(cw.items())},
                    "conway_matches": match}
        spreads[k] = d["v_spread"]
        print(f"    {k:5s} spread {d['v_spread']}  MFW >= "
              f"{d['braid_index_lower_bound']}  Conway "
              f"{'OK' if match else 'MISMATCH'}")

    print("\n[3] MFW bound vs tabulated braid index (6_1 excluded — under test)")
    for k, bi in TABULATED.items():
        got = knots[k]["braid_index_lower_bound"]
        match = got == bi
        ok = ok and match
        print(f"    {k:5s} MFW {got} vs tabulated {bi}  "
              f"{'OK' if match else 'MISMATCH'}")

    print("\n[4] 6_1 — the derivation")
    lower = knots["6_1"]["braid_index_lower_bound"]
    w4 = tuple(SIX_ONE_4BRAID)
    _, comps = traverse(w4, 4)
    same_homfly = homfly(w4, 4) == homfly(
        snappy.Link("6_1").braid_word(),
        max(abs(x) for x in snappy.Link("6_1").braid_word()) + 1)
    ident = [str(m) for m in
             snappy.Manifold(snappy.Link(braid_closure=SIX_ONE_4BRAID)
                             .exterior()).identify()]
    is_61 = any("6_1" in s for s in ident)
    upper_ok = comps == 1 and same_homfly and is_61
    ok = ok and upper_ok and lower == 4
    print(f"    lower bound (MFW, spread {knots['6_1']['v_spread']}): {lower}")
    print(f"    upper bound: closure of {SIX_ONE_4BRAID} on 4 strands")
    print(f"      one component: {comps == 1}; HOMFLY equal: {same_homfly}; "
          f"SnapPy identify: {ident}")
    print(f"    => braid index(6_1) = {lower if upper_ok and lower == 4 else '?'}")
    print("    NOTE SnapPy's own braid_word() for 6_1 uses 5 strands — a "
          "second instance of the non-minimality already recorded for 5_2.")

    print("\n[5] torus family — braid index min(p,q) by theorem, not by table")
    torus = {}
    for (pp, qq), expect in TORUS.items():
        word = tuple(g for _ in range(qq) for g in range(1, pp))
        d = mfw_data(word, pp)
        got = d["braid_index_lower_bound"]
        # p < q throughout, so the word itself realises min(p,q) strands:
        # the lower bound is MET and the braid index is pinned exactly.
        match = got == expect and pp == expect
        ok = ok and match
        torus[f"T({pp},{qq})"] = {**d, "expected_min_p_q": expect,
                                  "pinned": match}
        print(f"    T({pp},{qq})  {len(word):2d} crossings on {pp} strands  "
              f"spread {d['v_spread']:2d}  MFW >= {got}  = min(p,q) = "
              f"{expect}  {'PINNED' if match else 'MISMATCH'}")
    print("    T(4,5) pins braid index 4 on a knot that is NOT 6_1 — the "
          "3-vs-4 discrimination the tabulated set could not test.")

    wb.add_data("torus_family", torus)
    wb.add_data("knots", knots)
    wb.add_data("six_one", {
        "mfw_lower_bound": lower,
        "four_strand_word": SIX_ONE_4BRAID,
        "four_strand_writhe": sum(1 if x > 0 else -1 for x in SIX_ONE_4BRAID),
        "snappy_identify": ident,
        "braid_index": 4 if upper_ok and lower == 4 else None,
        "lean_witness": {"n": 4, "e": 1,
                         "dmin": knots["6_1"]["v_min"],
                         "dmax": knots["6_1"]["v_max"]},
        "snappy_braid_word_strands": knots["6_1"]["n_strands"],
    })
    wb.add_data("method", {
        "convention": "Lickorish (v, z): v^-1 P(L+) - v P(L-) = z P(L0)",
        "arithmetic": "exact integer Laurent; no float anywhere",
        "why_not_homflypt_engine": "its n>=3 branch returns a numerical "
                                   "constant at terms[(0,0)], so any degree "
                                   "read gives spread 0 silently",
        "why_not_markov_trace": "SU(2)/TL specialisation (convention D) "
                                "collapses the v direction MFW measures",
    })
    wb.add_assertion("textbook_homfly_all",
                     computed=str(all(homfly(w, n).t == e
                                      for (w, n, e) in TEXTBOOK.values())),
                     expected="True", tolerance="exact",
                     source="unknot, Hopf, 3_1, 4_1, 5_1")
    wb.add_assertion("conway_specialisation_all",
                     computed=str(all(knots[k]["conway_matches"] for k in CONWAY)),
                     expected="True", tolerance="exact",
                     source="P(v=1,z) vs tabulated Conway polynomial")
    wb.add_assertion("mfw_matches_tabulated_braid_index",
                     computed=str([knots[k]["braid_index_lower_bound"]
                                   for k in TABULATED]),
                     expected=str([TABULATED[k] for k in TABULATED]),
                     tolerance="exact", source="knot table, 6_1 excluded")
    wb.add_assertion("mfw_pins_torus_braid_index_min_p_q",
                     computed=str([torus[f"T({a},{b})"]
                                   ["braid_index_lower_bound"]
                                   for (a, b) in TORUS]),
                     expected=str([TORUS[k] for k in TORUS]),
                     tolerance="exact",
                     source="theorem: MFW sharp on torus knots, "
                            "braid index = min(p,q); T(4,5) gives 4")
    wb.add_assertion("braid_index_six_one",
                     computed=str(4 if upper_ok and lower == 4 else None),
                     expected="4", tolerance="exact",
                     source="MFW lower bound 4 + explicit 4-strand closure")
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no q0, on either layer. HOMFLY is computed by skein "
            "recursion in exact integer Laurent arithmetic over Z[v,z]; the "
            "substrate modulus would only appear under a specialisation, and "
            "none is taken. This is deliberate: the SU(2)/Temperley-Lieb "
            "specialisation the corpus Markov trace uses is precisely what "
            "collapses the v direction that MFW reads."),
    })

    print(f"\n  RESULT: {'DERIVED' if ok else 'FAILURE — see above'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
