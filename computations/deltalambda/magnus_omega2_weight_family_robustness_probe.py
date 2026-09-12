#!/usr/bin/env python3
"""Does the Magnus Ω₂ sign conclusion depend on WHICH partition-weight family
is used to aggregate it?  Measured: **yes at A=3 and A=4**, no at A=2. All
three sources are now post-ruling, so nothing is excluded from the gate.

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
    triton         14        14
    ⁴He            26        49

The sum is a genuine cancellation, and re-weighting redistributes mass across
terms of both signs while zeroing most of them. The sign was free to flip — and
at A=3 it does:

    atom      source        P_plancherel   P_wenzl     agree?
    deuteron  canonical         -15.095     -6.921     yes
    triton    canonical          +2.470    -13.931     NO
    ⁴He       canonical         +34.126    -20.466     NO

Read down the sign columns rather than across the rows. Plancherel gives
-, +, + over A = 2, 3, 4 — one sign change, between the deuteron and the
triton. Wenzl gives -, -, - — no sign change anywhere. The programme's target
is a sign change in A, so the two measures do not merely disagree on a number:
they disagree on whether the target phenomenon is present.

That is a finding about the measures, NOT a reason to prefer Plancherel. It
yields the wanted sign, and picking it for that reason is fitting. Note also
that Plancherel's tr(1) is 11.139 / 184.233 / 6751.541 at n = 6, 9, 12 against
Wenzl's exact 1.0 — it is not a normalised trace and its scale drifts ~600x
from A=2 to A=4, which is precisely what makes a cross-A statement under it
hard to read.

METHOD
------
No re-derivation: each sign probe already records its own per-partition
`tr_rho_Omega2`, so this re-weights **that committed data** with
`y_lambda_wenzl_bridge_numeric` and compares signs. That keeps the comparison
exact (the traces are shared, not recomputed) and cheap.

NOT CLAIMED: that either measure is the right pairing for a Magnus Ω₂ sign
question. Only which atoms the published sign distinguishes them on.

A NOTE ON THE FIRST VERSION OF THIS FILE. It reported robustness on all three
atoms, because it re-weighted each probe's committed traces without checking
they were canonical — two of three predated the 2026-09-05 ordering ruling. The
`ORDERING_RULING` guard below exists so that cannot recur: a stale source is
excluded from the gate rather than counted as agreement.
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

#: The 2026-09-05 intra-nucleon ordering ruling (bean qou-hu1f). A source
#: witness computed BEFORE this carries grouped-era traces, and re-weighting
#: those answers a question about a superseded braid word.
#:
#: This check exists because its absence produced a wrong answer. The first run
#: of this probe reported "sign robust on all atoms: True" — but triton's source
#: witness was dated 2026-09-03, and regenerating it on the canonical word
#: flipped P_total from -108.147 to +2.470, at which point the two weight
#: families DISAGREE at A=3. Trusting an input's date is weak, but silently
#: trusting an undated one is how that claim got published.
ORDERING_RULING = "2026-09-05"

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
        _doc = json.loads(p.read_text())
        _when = (_doc.get("computedAt") or "")[:10]
        pre_ruling = bool(_when) and _when < ORDERING_RULING
        per = _doc.get("results", {}).get("per_partition") or []
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
        # A pre-ruling source cannot support a verdict either way: its traces
        # are for a superseded braid word, so both arms answer the wrong
        # question. Excluded from the gate rather than counted as agreeing.
        if not pre_ruling:
            all_robust = all_robust and robust
        rows.append({
            "atom": atom,
            "source_computed_at": _when or "unknown",
            "source_pre_ruling": pre_ruling,
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
        _flag = "  [PRE-RULING SOURCE — verdict not counted]" if pre_ruling else ""
        print(f"  {atom:10s} partitions {len(per):3d}  Wenzl-nonzero {nonzero:3d}  "
              f"traces +{pos}/-{neg}{_flag}")
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
        "A source witness computed before the 2026-09-05 ordering ruling carries "
        "grouped-era traces; re-weighting those compares two contractions of a "
        "superseded braid word, so its verdict is excluded from the gate. "
        "`source_pre_ruling` records which. This is not hypothetical: the first "
        "run of this probe reported robustness on all three atoms because "
        "triton's source was 2026-09-03, and the canonical regeneration flipped "
        "its sign."
    )
    wb.add_caveat(
        "The published SIGN DOES distinguish the two measures, at A=3 and A=4 "
        "both. Plancherel runs -,+,+ over A=2,3,4 (one sign change, between "
        "deuteron and triton); Wenzl runs -,-,- (no sign change anywhere). So "
        "the A-dependent sign change exists only under the measure the probes "
        "aggregate with, not under the production Markov weight. This caveat "
        "previously read 'the published SIGN does not distinguish the two "
        "measures' — true when only the deuteron had a canonical source, and "
        "contradicted by this witness's own per_atom rows once triton and "
        "helium-4 did."
    )
    wb.add_caveat(
        "Does NOT establish that either measure is the correct pairing for a "
        "Magnus Omega2 question — that is bean qou-za3q decision 1, still "
        "open. It establishes that the choice is no longer cosmetic: it "
        "determines whether the programme's target sign change is exhibited at "
        "all. Choosing the measure that yields the wanted sign would be "
        "fitting (AGENTS.md: selection against the target), so the honest "
        "reading is that under the production weight the sign change is NOT "
        "exhibited in A=2,3,4. Magnitudes remain weight-family dependent and "
        "non-monotone."
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
