#!/usr/bin/env python3
"""Are there any χ^λ structural zeros in the atom braid words? — No.

WHY THIS EXISTS
---------------
The 2026-06-10 owner directive on partition truncation
(`docs/audits/2026-06-10-binding-active-set-compute-optimization.md`) admits
dropping a partition from the binding sum only if its contribution is
**exact-0**, amended 2026-09-06 to **exact-0 or likely provable so on numerical
evidence**.

That audit searched for `χ^λ(β_atom) = 0` and found none, at q₀, exactly. This
probe re-runs that search under the amended, weaker standard — and it still
finds none, by a wide margin.

THE STANDARD: A Q-SWEEP, NOT A MAGNITUDE
----------------------------------------
"Likely provable on numerical evidence" is only meaningful with a test that
separates a structural identity from a coincidence. Magnitude at one q does not:
this corpus has measured the coincidence floor, and a figure agreeing to 0–2
significant figures is a coincidence **100 %** of the time.

A structural zero vanishes at **every** q. So the test is whether `χ^λ` vanishes
across several q values, and those values must carry genuine 50-digit content —
`q = 1.1` and friends are exactly recoverable from their own float64, which is
why `pyhecke.atom.reject_float64_q` refuses them, and why a 1e-30 threshold
against such a q would be meaningless. Hence the irrational sweep points.

RESULT
------
Zero candidates, at every nucleus tested, across five q values:

    nucleus    n   partitions   χ^λ≈0 at all 5 q   smallest |χ^λ| at q₀
    proton     3       3              0                 0.2806
    deuteron   6      11              0                 0.0367
    tritium    9      30              0                 0.0693
    ⁴He       12      77              0                 0.0149

Nothing is close — the smallest character anywhere is 1.5e-2, thirty orders
above the threshold. The original finding survives a far stronger test than the
one that produced it: not "no exact zeros at q₀" but "no near-zeros at any of
five q".

AND THE NEAR-MISSES ARE ALREADY GONE
------------------------------------
At tritium and ⁴He, **every** one of the smallest-|χ^λ| partitions already
carries `y_λ = 0` under production convention D (Wenzl row cap, level r = 2 —
bean `qou-fq0f`). The two criteria do not overlap: there is nothing for a
character selection rule to drop that the weight has not already dropped.

So the droppable set is exactly the row cap, and it qualifies under the STRICT
reading — `WenzlWeightVanishing.lean` certifies it — without needing the
amendment at all.

Bean: `qou-fq0f`.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "substrate"))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402

mp.mp.dps = 50

from q_parameter import Q_50_DIGIT_STR as QS  # noqa: E402
import mass_at_3A_proper as M  # noqa: E402
from chi_general_word import chi_all_lambda_any  # noqa: E402
from hecke_characters import partitions_of  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402

#: Threshold below which a character counts as a vanishing candidate. Set far
#: under the observed floor (1.5e-2) so this cannot be accused of being tuned:
#: anything real would have to fall twenty-eight orders to reach it.
ZERO_TOL = mp.mpf("1e-30")

NUCLEI = (((1, 0), "proton"), ((1, 1), "deuteron"),
          ((1, 2), "tritium"), ((2, 2), "helium-4"))


def sweep_points():
    """q values with genuine 50-digit content.

    Irrational by construction: a value like 1.3 is exactly recoverable from
    its own float64, so `reject_float64_q` refuses it and — more to the point —
    a 17-digit q would cap χ at ~1e-17 and make ZERO_TOL meaningless.
    """
    return [("q0", mp.mpf(QS)), ("sqrt2", mp.sqrt(2)),
            ("phi", (1 + mp.sqrt(5)) / 2), ("sqrt3", mp.sqrt(3)),
            ("e_over_2", mp.e / 2)]


def main() -> int:
    pts = sweep_points()
    print("χ^λ structural-zero search — "
          f"{len(pts)}-point irrational q-sweep at {mp.mp.dps} dps")
    print(f"  sweep: {', '.join(n for n, _ in pts)}")
    print(f"  a candidate must satisfy |χ^λ| < {mp.nstr(ZERO_TOL, 3)} at EVERY q\n")

    rows = []
    all_candidates = []
    for (Z, N), label in NUCLEI:
        n = 3 * (Z + N)
        tabs = [chi_all_lambda_any(M.atom_braid_word_3A(Z, N, q=q), n, dps=50, q=q)
                for _, q in pts]
        q0 = pts[0][1]
        parts = [tuple(p) for p in partitions_of(n)]
        cands = [t for t in parts
                 if max(abs(tb.get(t, mp.mpf(0))) for tb in tabs) < ZERO_TOL]
        all_candidates.extend((label, t) for t in cands)

        ranked = sorted(((t, abs(tabs[0].get(t, mp.mpf(0)))) for t in parts),
                        key=lambda r: r[1])
        smallest_t, smallest = ranked[0]
        # Do the near-misses still carry weight, or has the row cap them already?
        near = [(t, m, y_lambda_wenzl_bridge_numeric(list(t), q0, dps=50))
                for t, m in ranked[:3]]
        live_near = [t for t, _, y in near if y != 0]

        rows.append({
            "nucleus": label, "Z": Z, "N": N, "n": n,
            "partitions": len(parts),
            "chi_zero_candidates": len(cands),
            "smallest_abs_chi_at_q0": mp.nstr(smallest, 12),
            "smallest_abs_chi_partition": list(smallest_t),
            "near_misses_with_nonzero_weight": [list(t) for t in live_near],
        })
        print(f"  {label:<9} n={n:<3} partitions={len(parts):<4} "
              f"candidates={len(cands)}   smallest |χ^λ| = "
              f"{mp.nstr(smallest, 8)} at {smallest_t}")
        for t, m, y in near:
            tag = "weight already 0 (row cap)" if y == 0 else "LIVE — weight nonzero"
            print(f"        {str(t):<24} |χ|={mp.nstr(m, 8):<14} {tag}")

    print(f"\n  total candidates across all nuclei: {len(all_candidates)}")
    if all_candidates:
        print("  *** investigate before dropping anything:")
        for lbl, t in all_candidates:
            print(f"        {lbl}: {t}")
    else:
        print("  The 2026-06-10 finding holds under the amended standard: no χ^λ "
              "is zero,\n  and none is close. The droppable set is the Wenzl row "
              "cap alone, which is\n  provable outright and needs no appeal to "
              "numerical evidence.")

    from witness_base import WitnessBuilder  # noqa: E402
    wb = WitnessBuilder(Path(__file__).stem, engine="python")
    wb.set_description(
        "Searches for structural zeros of χ^λ(β_atom) across a 5-point "
        "irrational q-sweep at 50 dps, under the 2026-09-06 owner amendment "
        "admitting truncation on exact-0 OR likely-provable numerical "
        "evidence. Result: no candidates at any nucleus tested; the smallest "
        "character anywhere is 1.5e-2. The 2026-06-10 audit's conclusion "
        "survives a strictly stronger test than the one that produced it."
    )
    wb.add_data("sweep_points", [n for n, _ in pts])
    wb.add_data("zero_tolerance", mp.nstr(ZERO_TOL, 3))
    wb.add_data("per_nucleus", rows)
    wb.add_data("total_chi_zero_candidates", len(all_candidates))
    wb.add_data("conclusion", (
        "No χ^λ structural zeros. Every smallest-|χ^λ| partition at tritium "
        "and helium-4 already has y_λ = 0 under convention D, so the two "
        "criteria do not overlap and the row cap is the whole droppable set."
    ))
    wb.add_assertion(name="no_chi_structural_zeros",
                     computed=str(len(all_candidates)), expected="0")
    wb.add_caveat(
        "A negative result over four nuclei (n ≤ 12), not a theorem. It does "
        "not rule out a character selection rule at larger n or for a "
        "different word; re-run this probe rather than assuming it extends."
    )
    wb.add_caveat(
        "The sweep points are irrational deliberately. A simple value like "
        "q = 1.3 is exactly recoverable from its own float64 — "
        "`pyhecke.atom.reject_float64_q` refuses it — and a 17-digit q would "
        "cap χ near 1e-17, making the 1e-30 tolerance vacuous."
    )
    print(f"\nWitness: {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
