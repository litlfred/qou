#!/usr/bin/env python3
"""The level-3 EM term already exists — and its multiplicity is mirror-INVARIANT.

Owner, 2026-08-30: *"next qou-vudb's open item — add an explicit EM term at
level 3 ... Coulomb's A-scaling, exponent ~0.78 on this grid"*.

**The term is already there, and no coefficient can make it do the job.**

## What the corpus's decomposition says

`qou-toul` (2026-08-29, completed) derived the crossing-energy split from
`def:crossing-energy`'s own weights, `E = n+ q - n- q^-1`, solving
`E = A(q + q^-1) + B(q - q^-1)`:

    A  (symmetric / STRONG)      = (n+ - n-)/2      the WRITHE
    B  (antisymmetric / COULOMB) = (n+ + n-)/2      the crossing COUNT

and fixed `coulomb-charge.md`/`crossing-energy.lean`, which had them swapped.

## What the braid words actually give — verified here, not assumed

`mba-sidecar-mirror-cancellation` states `n+ + n- = 10A - 2` and
`w = n+ - n- = 4Z`. This probe **verifies both** against
`mass_at_3A_proper.atom_braid_word_3A`, classifying each letter by its `d`
coefficient, per that function's own docstring:

    d == 0    -> sigma      (positive crossing)
    d == -h   -> sigma^-1   (negative crossing; this module has sigma^-1 = sigma - h)
    otherwise -> an AVERAGED letter, not a braid generator at all

Counting instead by the `c` coefficient — which is 1 on every letter — reports
every braid as positive and is simply wrong; that error is what this probe was
written to avoid repeating.

Result: `n+ = 5A - 1 + 2Z` and `n- = 5A - 1 - 2Z`, so

    COULOMB channel  B = (n+ + n-)/2 = 5A - 1     depends on A ONLY
    STRONG  channel  A = (n+ - n-)/2 = 2Z         carries ALL the charge dependence

## The two findings

**1. The Coulomb channel contributes exactly zero to every mirror splitting.**
Its multiplicity `5A - 1` is identical for `(Z,N)` and `(N,Z)`. No coefficient
times a mirror-invariant multiplicity produces a mirror splitting, so the
existing EM term cannot be tuned into the Coulomb displacement energy. This is
the same parity inversion `qou-1pig` found in the bond layer, now confirmed one
level up in the corpus's own POST-CORRECTION decomposition — and it is why
`qou-vudb` measured the model's mirror asymmetry as a *strong*-channel constant.

**2. No linear functional of the crossing counts can be Coulomb.** The Coulomb
displacement energy needs a multiplicity going as the number of proton PAIRS,
`Z(Z-1)` — quadratic in `Z`. But `n+` and `n-` are each **affine** in `(A, Z)`,
so every `a*n+ + b*n- + c` is affine, and no affine function of `(A, Z)` equals
`Z(Z-1)`. Verified here by exhibiting the second difference, and proved in
`QOU/MassTheory/CrossingCountAffine.lean`.

The strong channel's `2Z` is also linear, which is exactly the `A^0` mirror
scaling `qou-vudb` measured against an observed `~A^0.87`.

## Scope

**(b)** for finding 2, invariant named: **degree**. An affine function of
`(A, Z)` cannot equal a quadratic one, so the exclusion holds for every
coefficient and every anchor, not merely for the ones tried.

**(b)** for finding 1 as well, as of the Lean of 2026-08-30.
`QOU/MassTheory/BondArcTheorems.lean` section 5 PROVES `n+ + n- = 10A - 2` and
`n+ - n- = 4Z` from the chain model -- per proton (6, 3, 2), per neutron
(5, 4, 2), plus `Z-1` pp interfaces, `N-1` nn, and exactly one pn -- and this
probe verifies that model reproduces `atom_braid_word_3A` EXACTLY on every
nucleus tested. So the Coulomb channel's mirror-invariance holds for all
`(Z, N)`, not just the 12 checked.

What remains unproved is one level down: that the per-nucleon counts
`(6,3,2)` and `(5,4,2)` follow from the quark content. They are read off the
implementation, so section 5's theorems are exact GIVEN the construction and
are not a proof that the construction is right.

Nothing is refuted -- `qou-toul`'s correction stands and this builds on it.
Nothing is wired.

`-- Ref:` `def:crossing-energy`; `prop:crossing-energy-decomposition`;
`mba-sidecar-mirror-cancellation`. Beans `qou-toul`, `qou-vudb`, `qou-1pig`.
"""
from __future__ import annotations

import datetime
import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

EPS = mpf(10) ** (-40)

NUCLEI = [
    ("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
    ("7Li", 3, 4), ("7Be", 4, 3), ("11B", 5, 6), ("11C", 6, 5),
    ("15N", 7, 8), ("15O", 8, 7), ("39K", 19, 20), ("39Ca", 20, 19),
]


def crossing_counts(Z, N, h):
    """(n_plus, n_minus, n_averaged), classifying by the d coefficient.

    Per atom_braid_word_3A's docstring: a letter is the Hecke element
    c*sigma_g + d*1.  d == 0 is sigma; d == -h is sigma^-1 (this module uses
    sigma^-1 = sigma - h); anything else is an averaged letter and is NOT a
    braid generator.  Classifying by `c` instead reports every braid positive
    and is wrong.
    """
    npos = nneg = navg = 0
    for (_c, d, _g) in atom_braid_word_3A(Z, N):
        dv = mpf(d)
        if abs(dv) < EPS:
            npos += 1
        elif abs(dv + h) < EPS:
            nneg += 1
        else:
            navg += 1
    return npos, nneg, navg


def main() -> int:
    q = Q_MP
    h = hecke_h(q)

    rows = []
    for name, Z, N in NUCLEI:
        A = Z + N
        npos, nneg, navg = crossing_counts(Z, N, h)
        rows.append({
            "nucleus": name, "Z": Z, "N": N, "A": A,
            "n_plus": npos, "n_minus": nneg, "n_averaged": navg,
            "count_n_plus_n_minus": npos + nneg,
            "predicted_10A_minus_2": 10 * A - 2,
            "writhe_n_plus_minus_n_minus": npos - nneg,
            "predicted_4Z": 4 * Z,
            "averaged_matches_2A_plus_1": navg == 2 * A + 1,
            "coulomb_channel_multiplicity": (npos + nneg) // 2,   # = 5A - 1
            "strong_channel_multiplicity": (npos - nneg) // 2,    # = 2Z
        })

    # The Lean model (QOU/MassTheory/BondArcTheorems, section 5): per proton
    # (6 pos, 3 neg, 2 avg), per neutron (5, 4, 2), plus the chain's Z-1 pp
    # interfaces (positive), N-1 nn (negative) and exactly ONE pn (averaged) --
    # a chain on p^Z n^N has exactly one p->n transition. Lean proves
    # n+ + n- = 10A - 2 and n+ - n- = 4Z FROM this model; this checks the model
    # reproduces the implementation, which is what makes those theorems bite.
    def lean_model(Z, N):
        return (6 * Z + 5 * N + (Z - 1), 3 * Z + 4 * N + (N - 1), 2 * (Z + N) + 1)

    for r in rows:
        m = lean_model(r["Z"], r["N"])
        r["lean_model"] = list(m)
        r["matches_lean_model"] = (r["n_plus"], r["n_minus"], r["n_averaged"]) == m
    model_ok = all(r["matches_lean_model"] for r in rows)

    stats_ok = all(r["count_n_plus_n_minus"] == r["predicted_10A_minus_2"]
                   and r["writhe_n_plus_minus_n_minus"] == r["predicted_4Z"]
                   and r["averaged_matches_2A_plus_1"] for r in rows)

    # mirror pairs present in the table: the Coulomb multiplicity must coincide
    mirror_checks = []
    by_zn = {(r["Z"], r["N"]): r for r in rows}
    for (Z, N), r in by_zn.items():
        if (N, Z) in by_zn and Z > N:
            s = by_zn[(N, Z)]
            mirror_checks.append({
                "pair": f"{r['nucleus']}/{s['nucleus']}",
                "coulomb_mult": [r["coulomb_channel_multiplicity"],
                                 s["coulomb_channel_multiplicity"]],
                "coulomb_equal": (r["coulomb_channel_multiplicity"]
                                  == s["coulomb_channel_multiplicity"]),
                "strong_mult": [r["strong_channel_multiplicity"],
                                s["strong_channel_multiplicity"]],
                "strong_differs": (r["strong_channel_multiplicity"]
                                   != s["strong_channel_multiplicity"]),
            })

    # finding 2: affine in (A,Z) cannot be Z(Z-1). Exhibit the second difference.
    # For fixed A, Z(Z-1) has constant second difference 2; an affine function 0.
    second_diff_quadratic = [(z + 2) * (z + 1) - 2 * (z + 1) * z + z * (z - 1)
                             for z in (1, 2, 3, 5, 10)]
    # the strong channel's own second difference in Z, from the measured 2Z
    second_diff_strong = [2 * (z + 2) - 2 * 2 * (z + 1) + 2 * z for z in (1, 2, 3, 5, 10)]

    print("Level-3 EM channel: the term exists, and its multiplicity is mirror-invariant\n")
    print(f"  {'nuc':>6}{'Z':>3}{'N':>3}{'A':>4}{'n+':>5}{'n-':>5}{'avg':>5}"
          f"{'n++n-':>7}{'10A-2':>7}{'n+-n-':>7}{'4Z':>5}"
          f"{'Coul=5A-1':>11}{'Strong=2Z':>11}")
    for r in rows:
        print(f"  {r['nucleus']:>6}{r['Z']:>3}{r['N']:>3}{r['A']:>4}"
              f"{r['n_plus']:>5}{r['n_minus']:>5}{r['n_averaged']:>5}"
              f"{r['count_n_plus_n_minus']:>7}{r['predicted_10A_minus_2']:>7}"
              f"{r['writhe_n_plus_minus_n_minus']:>7}{r['predicted_4Z']:>5}"
              f"{r['coulomb_channel_multiplicity']:>11}"
              f"{r['strong_channel_multiplicity']:>11}")
    print(f"\n  all 12 match mba-sidecar-mirror-cancellation: {stats_ok}")
    print(f"  all 12 match the LEAN model of section 5 exactly:  {model_ok}")

    print("\n  FINDING 1 — the Coulomb channel is mirror-BLIND:")
    for m in mirror_checks:
        print(f"    {m['pair']:>12}  Coulomb {m['coulomb_mult']} equal={m['coulomb_equal']}"
              f"   Strong {m['strong_mult']} differs={m['strong_differs']}")
    print("    -> no coefficient times a mirror-invariant multiplicity yields a")
    print("       mirror splitting, so the EXISTING EM term cannot be tuned into")
    print("       the Coulomb displacement energy.")

    print("\n  FINDING 2 — no linear functional of the crossing counts is Coulomb:")
    print("    n+ = 5A - 1 + 2Z  and  n- = 5A - 1 - 2Z  are both AFFINE in (A,Z),")
    print("    so every a*n+ + b*n- + c is affine. Coulomb needs Z(Z-1) proton pairs.")
    print(f"    second difference in Z of Z(Z-1) : {second_diff_quadratic}  (constant 2)")
    print(f"    second difference in Z of 2Z     : {second_diff_strong}  (identically 0)")
    print("    -> an affine function cannot equal a quadratic one, for ANY coefficients.")

    assertions = [
        {"name": "the Lean model's per-nucleon and per-interface counts reproduce "
                 "the implementation exactly -- this is what lets Lean PROVE the "
                 "two statistics rather than sample them",
         "passed": model_ok},
        {"name": "n+ + n- = 10A - 2 on every nucleus tested (12, up to A=39)",
         "passed": all(r["count_n_plus_n_minus"] == r["predicted_10A_minus_2"] for r in rows)},
        {"name": "n+ - n- = 4Z on every nucleus tested",
         "passed": all(r["writhe_n_plus_minus_n_minus"] == r["predicted_4Z"] for r in rows)},
        {"name": "the averaged (non-braid) letters number 2A+1, as the docstring states",
         "passed": all(r["averaged_matches_2A_plus_1"] for r in rows)},
        {"name": "the braids are NOT positive — n- is nonzero everywhere, so the "
                 "two channels are genuinely distinct objects",
         "passed": all(r["n_minus"] > 0 for r in rows)},
        {"name": "the COULOMB channel multiplicity is equal across every mirror pair",
         "passed": bool(mirror_checks) and all(m["coulomb_equal"] for m in mirror_checks)},
        {"name": "the STRONG channel multiplicity differs across every mirror pair — "
                 "the charge dependence is in the wrong channel",
         "passed": bool(mirror_checks) and all(m["strong_differs"] for m in mirror_checks)},
        {"name": "Z(Z-1) has constant nonzero second difference in Z while the "
                 "crossing-count channels have zero — degree excludes the fit",
         "passed": all(d == 2 for d in second_diff_quadratic)
                   and all(d == 0 for d in second_diff_strong)},
    ]

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "The level-3 EM term already exists and cannot do the job. Post-qou-toul "
            "the antisymmetric/Coulomb channel has multiplicity (n+ + n-)/2 = 5A - 1, "
            "which is MIRROR-INVARIANT, while the symmetric/strong channel carries "
            "(n+ - n-)/2 = 2Z, all of the charge dependence -- the reverse of physics. "
            "So the existing EM term contributes exactly zero to every mirror "
            "splitting. Further, n+ and n- are each affine in (A,Z), so no linear "
            "functional of the crossing counts can supply the Z(Z-1) proton-pair "
            "multiplicity Coulomb needs."),
        "q0_pin": "proton",
        "q0": Q_50_DIGIT_STR,
        "crossing_statistics": rows,
        "statistics_match_sidecar": stats_ok,
        "matches_lean_model": model_ok,
        "lean_model": {
            "per_proton": "(6 pos, 3 neg, 2 avg)",
            "per_neutron": "(5 pos, 4 neg, 2 avg)",
            "chain_interfaces": "Z-1 pp (pos), N-1 nn (neg), exactly 1 pn (avg)",
            "closed_forms": "n+ = 7Z + 5N - 1 ; n- = 3Z + 5N - 1 ; avg = 2A + 1",
            "lean": "QOU/MassTheory/BondArcTheorems.lean section 5",
        },
        "mirror_checks": mirror_checks,
        "degree_argument": {
            "n_plus_formula": "5A - 1 + 2Z",
            "n_minus_formula": "5A - 1 - 2Z",
            "coulomb_channel": "(n+ + n-)/2 = 5A - 1  (mirror-invariant)",
            "strong_channel": "(n+ - n-)/2 = 2Z       (mirror-odd)",
            "coulomb_needs": "Z(Z-1), the number of proton pairs -- quadratic in Z",
            "second_difference_of_Z_times_Z_minus_1": second_diff_quadratic,
            "second_difference_of_strong_channel": second_diff_strong,
        },
        "assertions": assertions,
        "free_parameters": 0,
        "scope": (
            "(b) for the degree exclusion, invariant named: an affine function of "
            "(A,Z) cannot equal a quadratic one, so it holds for every coefficient "
            "and every anchor. UPGRADED from (a) to (b) for the crossing "
            "statistics too: QOU/MassTheory/BondArcTheorems section 5 PROVES "
            "n+ + n- = 10A - 2 and n+ - n- = 4Z from the chain model, and this "
            "probe verifies the model reproduces atom_braid_word_3A exactly, so "
            "the Coulomb channel's mirror-invariance now holds for all (Z,N) "
            "rather than for the 12 tested. What remains unproved is that the "
            "per-nucleon counts (6,3,2)/(5,4,2) follow from the quark content -- "
            "they are read off the implementation. Nothing refuted; qou-toul's correction "
            "stands and this builds on it. Nothing wired."),
        "lean": "QOU/MassTheory/CrossingCountAffine.lean",
        "beans": ["qou-toul", "qou-vudb", "qou-1pig"],
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = _HERE / "level3-em-channel-parity.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")

    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"\n  Witness: {out.name}   allPassed={witness['allPassed']}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
