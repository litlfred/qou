#!/usr/bin/env python3
"""Does the Magnus Ω₂ sign conclusion depend on WHICH partition-weight family
is used to aggregate it?  Measured: no, on all three atoms.

WHY THIS EXISTS (bean qou-za3q)
-------------------------------
`{deuteron,triton}_magnus_omega2_sign_probe.py` and
`he4_magnus_omega2_sign_sparse_probe.py` aggregate

    P_total = Σ_λ  w(λ) · tr(ρ_λ Ω₂)

with `w = d_q(λ)² / [n]_q!`, the **quantum Plancherel** measure. Their
docstrings used to call that `y_λ`, which is the conflation AGENTS.md forbids:
the three families y_λ / w_λ / w̃_λ are distinct at q ≠ 1. The name is fixed in
those files now; this probe settles the question the name-fix does not, namely
whether the aggregate conclusion was ever sensitive to the choice.

It matters because the two measures are not a rescaling of one another. The
production Wenzl weight carries a row cap (level r = 2, bean `qou-fq0f`) that
annihilates every shape with ≥3 rows — which is exactly where the Plancherel
measure puts most of its mass. At A = 4 only **7 of 77** partitions of 12
survive the cap.

WHY THE ANSWER IS NOT AUTOMATIC
-------------------------------
Both weight families are strictly positive, so if every `tr(ρ_λ Ω₂)` shared a
sign the answer would be trivial. They do not:

    atom      tr(ρΩ₂) > 0    < 0
    deuteron        4         5
    triton         13        15
    ⁴He            26        49

The sum is a genuine cancellation, and re-weighting redistributes mass across
terms of both signs while zeroing most of them. The sign was free to flip.

METHOD
------
No re-derivation: each sign probe already records its own per-partition
`tr_rho_Omega2`, so this re-weights **that committed data** with
`y_lambda_wenzl_bridge_numeric` and compares signs. That keeps the comparison
exact (the traces are shared, not recomputed) and cheap.

NOT CLAIMED: that either measure is the right pairing for a Magnus Ω₂ sign
question. Only that the published sign does not distinguish them.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

mp.mp.dps = 50

WITNESSES = [
    ("deuteron", "deuteron-magnus-omega2-sign.witness.json"),
    ("triton", "triton-magnus-omega2-sign.witness.json"),
    ("helium-4", "he4-magnus-omega2-sign.witness.json"),
]


def main() -> int:
    q = Q_MP
    wb = WitnessBuilder("magnus-omega2-weight-family-robustness", engine="mpmath")
    wb.set_description(
        "Re-weights each Magnus Omega2 sign probe's own committed "
        "per-partition tr(rho.Omega2) with the production Wenzl bridge weight "
        "instead of the quantum Plancherel measure those probes aggregate "
        "with, and compares the sign of P_total. The traces are shared rather "
        "than recomputed, so the comparison isolates the weight family. Bean "
        "qou-za3q."
    )

    rows = []
    all_robust = True
    for atom, fname in WITNESSES:
        p = HERE / fname
        if not p.exists():
            print(f"  {atom}: MISSING {fname}")
            all_robust = False
            continue
        per = json.loads(p.read_text()).get("results", {}).get("per_partition") or []
        p_planch = mp.mpf(0)
        p_wenzl = mp.mpf(0)
        nonzero = 0
        pos = neg = 0
        for r in per:
            shape = tuple(r["lambda"])
            tr = mp.mpf(str(r["tr_rho_Omega2"]))
            if tr > 0:
                pos += 1
            elif tr < 0:
                neg += 1
            p_planch += mp.mpf(str(r["y_lambda"])) * tr
            yw = y_lambda_wenzl_bridge_numeric(shape, q, dps=50)
            if yw != 0:
                nonzero += 1
            p_wenzl += yw * tr

        def sgn(x):
            return 0 if x == 0 else (1 if x > 0 else -1)

        robust = sgn(p_planch) == sgn(p_wenzl)
        all_robust = all_robust and robust
        rows.append({
            "atom": atom,
            "partitions": len(per),
            "wenzl_nonzero_partitions": nonzero,
            "trace_sign_split": {"positive": pos, "negative": neg,
                                 "zero": len(per) - pos - neg},
            "P_total_plancherel": mp.nstr(p_planch, 20),
            "P_total_wenzl": mp.nstr(p_wenzl, 20),
            "sign_plancherel": sgn(p_planch),
            "sign_wenzl": sgn(p_wenzl),
            "sign_robust": robust,
        })
        print(f"  {atom:10s} partitions {len(per):3d}  Wenzl-nonzero {nonzero:3d}  "
              f"traces +{pos}/-{neg}")
        print(f"             P_planch {mp.nstr(p_planch, 10):>16} ({sgn(p_planch):+d})   "
              f"P_wenzl {mp.nstr(p_wenzl, 10):>16} ({sgn(p_wenzl):+d})   "
              f"robust={robust}")

    wb.add_data("per_atom", rows)
    wb.add_data("weight_families", {
        "plancherel": "d_q(lambda)^2 / [n]_q!  — what the sign probes aggregate with",
        "wenzl": "y_lambda_wenzl_bridge_numeric — the production Markov weight, "
                 "row-capped at level r = 2 so every shape with >=3 rows is exactly 0",
    })
    wb.add_caveat(
        "Establishes only that the published SIGN does not distinguish the two "
        "measures. It does NOT establish that either is the correct pairing for "
        "a Magnus Omega2 question, and the MAGNITUDES differ substantially — so "
        "any conclusion drawn from |P_total| rather than its sign is still "
        "weight-family dependent."
    )
    wb.add_assertion(
        name="sign_robust_to_weight_family",
        computed=str(int(all_robust)),
        expected="1",
    )
    print(f"\n  sign robust on all atoms: {all_robust}")
    print(f"  Witness: {wb.save()}")
    return 0 if all_robust else 1


if __name__ == "__main__":
    raise SystemExit(main())
