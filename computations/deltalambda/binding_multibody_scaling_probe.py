#!/usr/bin/env python3
# polynomial_q_not_applicable: exact AME data + integer combinatorics; no q, no fit.
"""
Multi-body SCALING test for the missing extensive binding term (bean qou-uclw /
qou-0c19).  ZERO-fit: no coefficients are fitted.  For each light nucleus read the
AME binding B(A) and ask which combinatorial count B tracks with a *constant ratio*
(a constant ratio ⇒ that count is the dominant scaling):

    per-nucleon        B / A            (liquid-drop volume term ∝ A)
    per-pair           B / C(A,2)       (pairwise / 2-body)
    per-triple         B / C(A,3)       (3-body, super-pairwise)
    cap ratio          B(A) / B(2)  vs  C(A,2)   (the proved pairwise cap ρ_A ≤ C(A,2))

A constant column identifies the scaling with no free parameter.  This is the
disciplined complement to the pairwise-cap proof
(QOU.MassTheory.exchangeDet_pow_two_le_four): the cap says the term is
super-pairwise; this says *which* super-pairwise scaling the data actually follow.

Read-only AME input; no AME inversion (we compare scalings, we do not solve for a
weight).  Output: binding-multibody-scaling.witness.json.
"""
from __future__ import annotations

import json
import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
_COMP = HERE.parent
for p in (str(_COMP), str(_COMP / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

AME = _COMP / "ame-2020-binding-energies.witness.json"

# isotope key in the AME witness -> (Z, N)
ISO = {
    "B_deuteron_MeV": ("2H", 1, 1),
    "B_tritium_MeV": ("3H", 1, 2),
    "B_he3_MeV": ("3He", 2, 1),
    "B_he4_MeV": ("4He", 2, 2),
    "B_li6_MeV": ("6Li", 3, 3),
    "B_li7_MeV": ("7Li", 3, 4),
    "B_be9_MeV": ("9Be", 4, 5),
    "B_c12_MeV": ("12C", 6, 6),
    "B_o16_MeV": ("16O", 8, 8),
}


def main() -> int:
    ame = record_upstream(AME, _UPSTREAM_RECORDS)
    data = ame.get("data", ame)

    def getB(key: str) -> float | None:
        v = data.get(key)
        if v is None:
            v = ame.get(key)
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    B2 = getB("B_deuteron_MeV")
    rows = []
    for key, (name, Z, N) in ISO.items():
        B = getB(key)
        if B is None:
            continue
        A = Z + N
        row = {
            "iso": name, "A": A, "B_MeV": B,
            "B_per_A": B / A,
            "B_per_pair": B / comb(A, 2) if A >= 2 else None,
            "B_per_triple": (B / comb(A, 3)) if A >= 3 else None,
            "cap_ratio_B_over_B2": B / B2,
            "pairwise_cap_C_A_2": comb(A, 2),
            "exceeds_pairwise_cap": (B / B2) > comb(A, 2),
        }
        rows.append(row)

    # constancy diagnostic: coefficient of variation (std/mean) of each ratio
    # across A ≥ 4 (the saturation regime) — the smallest CV is the best scaling.
    def cv(vals):
        vals = [v for v in vals if v is not None]
        if len(vals) < 2:
            return None
        m = sum(vals) / len(vals)
        var = sum((x - m) ** 2 for x in vals) / len(vals)
        return (var ** 0.5) / m if m else None

    sat = [r for r in rows if r["A"] >= 4]
    cv_perA = cv([r["B_per_A"] for r in sat])
    cv_perpair = cv([r["B_per_pair"] for r in sat])
    cv_pertriple = cv([r["B_per_triple"] for r in sat])

    w = WitnessBuilder("binding-multibody-scaling", engine="exact")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "0-fit multi-body scaling test for the missing extensive binding term. "
        "Which combinatorial count (A, C(A,2), C(A,3)) does AME B(A) track with a "
        "constant ratio? Complements the proved pairwise cap ρ_A ≤ C(A,2)."
    )
    w.set_content_block("alg:delta-lambda-closure")
    w.add_parameter("no_fit", True)
    w.add_parameter("cv_B_per_A_satregime", cv_perA)
    w.add_parameter("cv_B_per_pair_satregime", cv_perpair)
    w.add_parameter("cv_B_per_triple_satregime", cv_pertriple)
    best = min(
        [("per_A", cv_perA), ("per_pair", cv_perpair), ("per_triple", cv_pertriple)],
        key=lambda kv: (kv[1] if kv[1] is not None else 9e9),
    )
    w.add_parameter("most_constant_scaling_A_ge_4", best[0])
    w.add_data("rows", rows)
    built = w.build()
    (HERE / "binding-multibody-scaling.witness.json").write_text(
        json.dumps(built, indent=2, sort_keys=True) + "\n")

    print(f"{'iso':<5}{'A':>3}{'B(MeV)':>10}{'B/A':>8}{'B/C(A,2)':>10}"
          f"{'B/C(A,3)':>10}{'B/B2':>8}{'C(A,2)':>8}  cap?")
    for r in rows:
        pp = f"{r['B_per_pair']:.2f}" if r['B_per_pair'] is not None else "—"
        pt = f"{r['B_per_triple']:.2f}" if r['B_per_triple'] is not None else "—"
        print(f"{r['iso']:<5}{r['A']:>3}{r['B_MeV']:>10.3f}{r['B_per_A']:>8.2f}"
              f"{pp:>10}{pt:>10}{r['cap_ratio_B_over_B2']:>8.2f}"
              f"{r['pairwise_cap_C_A_2']:>8}  {'EXCEEDS' if r['exceeds_pairwise_cap'] else 'within'}")
    print()
    print(f"  CV (A≥4, smaller=more constant): B/A={cv_perA:.3f}  "
          f"B/C(A,2)={cv_perpair:.3f}  B/C(A,3)={cv_pertriple:.3f}")
    print(f"  most-constant scaling (A≥4): {best[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
