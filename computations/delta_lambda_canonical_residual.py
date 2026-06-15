#!/usr/bin/env python3
"""Canonical-binding residual Δ_λ(K) — tabulation + q₀-exponent structure.

EXPLORATORY / NEAR-MATCH TIER (per the c_k tiering discipline: this is an
observation of structure in the canonical residual, NOT a wired closure and
NOT a fit ansatz — nothing here feeds production).

Per the trace-convention reconciliation (docs/audits/
2026-06-09-binding-trace-convention-split.md, PR #2082): the trace-canonical
binding path is `binding_canonical.py`

    B_pred(Z,N) = E_0 · ( tr_M(W_free) − tr_M(W_atom) )

on the Jones–Markov trace `markov/markov_trace_canonical.tr_M_element`
(`prop:categorical-mass-markov`, markov-axioms-primitive). This probe reads
its witness and tabulates the per-nucleus residual

    Δ_λ(K) = B_AME / B_pred(K)

and its q₀-logarithm. FINDING: the exponent is a near-integer family

    log_{q₀} Δ_λ(K) ≈ 10·A − 5          (= 5(2A−1))

      D    14.99   vs 15   (δ = −0.01 — essentially exact)
      T    24.93   vs 25   (δ = −0.07)
      ³He  23.60   vs 25   (δ = −1.40 — Z-dependent deviation)
      ⁴He  35.27   vs 35   (δ = +0.27)

i.e. B_AME ≈ B_canonical · q₀^(10A−5+δ), |δ| ≤ 1.4 with δ ≈ 0 on the
N≥Z isotopes. The per-nucleon increment is exactly 10 in q₀-exponent
units. Whether 10A−5 has a categorical derivation (crossing-count /
jet-order / tower-depth bookkeeping of W_free vs W_atom) is the open
question this probe sharpens — that derivation, if it exists, IS the
canonical Δ_λ(K).

Output: delta-lambda-canonical-residual.witness.json
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

SRC = HERE / "binding-canonical.witness.json"


def main() -> int:
    t0 = time.monotonic()
    q0 = float(q_at(30))
    lnq = math.log(q0)
    rows_in = json.loads(SRC.read_text())["data"]["results"]

    rows = []
    for r in rows_in:
        B_pred = float(r["B_MeV"])
        B_ame = float(r["B_AME_MeV"])
        A = int(r["A"])
        delta = B_ame / B_pred
        x = math.log(delta) / lnq
        law = 10 * A - 5
        rows.append({
            "atom": r["atom"], "Z": r["Z"], "N": r["N"], "A": A,
            "B_AME_MeV": B_ame,
            "B_pred_canonical_MeV": B_pred,
            "Delta_lambda": round(delta, 4),
            "log_q0_Delta": round(x, 3),
            "law_10A_minus_5": law,
            "deviation_from_law": round(x - law, 3),
        })

    devs = [abs(r["deviation_from_law"]) for r in rows]
    n_ge_z = [r for r in rows if r["N"] >= r["Z"]]
    devs_ngez = [abs(r["deviation_from_law"]) for r in n_ge_z]

    w = WitnessBuilder("delta-lambda-canonical-residual", engine="python",
                       start_time=t0)
    w.set_description(
        "Canonical-binding residual Δ_λ(K)=B_AME/B_pred on the Jones–Markov "
        "trace-canonical path (binding_canonical.py, per the trace-convention "
        "reconciliation). NEAR-MATCH TIER observation: log_q0 Δ_λ ≈ 10A−5 "
        "(D exact to 0.01; T −0.07; ⁴He +0.27; ³He −1.40 Z-dependent). NOT "
        "wired; the open question is a categorical derivation of 10A−5."
    )
    w.add_data("q0", q0)
    w.add_data("trace_convention",
               "Jones–Markov (markov/markov_trace_canonical.tr_M_element; "
               "prop:categorical-mass-markov)")
    w.add_data("binding_path",
               "B_pred = E_0 · (tr_M(W_free) − tr_M(W_atom)) — binding_canonical.py")
    w.add_data("rows", rows)
    w.add_data("law", {
        "candidate": "Delta_lambda(K) ≈ q0^(10A−5)",
        "equivalently": "B_AME ≈ B_canonical · q0^(5(2A−1))",
        "tier": "near-match (c_k tiering discipline) — observation, NOT wired",
        "max_abs_deviation_all": max(devs),
        "max_abs_deviation_N_ge_Z": max(devs_ngez),
        "z_dependence_note": (
            "³He (Z>N) deviates −1.40; the N≥Z isotopes (D, T, ⁴He) sit "
            "within 0.27 of the integer law."
        ),
    })
    w.add_assertion(
        name="deuteron_exponent_matches_15",
        computed=abs([r for r in rows if r["atom"] == "D"][0]["log_q0_Delta"] - 15),
        expected=0.0, tolerance=0.05,
        source="log_q0(B_AME/B_pred) for the deuteron vs 10·2−5 = 15",
    )
    w.add_assertion(
        name="N_ge_Z_family_within_half_unit",
        computed=max(devs_ngez), expected=0.0, tolerance=0.5,
        source="max |log_q0 Δ_λ − (10A−5)| over D, T, ⁴He",
    )

    out = w.save()
    print(f"{'atom':>5} {'A':>2} {'Δ_λ':>9} {'log_q0':>8} {'10A−5':>6} {'dev':>6}")
    for r in rows:
        print(f"{r['atom']:>5} {r['A']:>2} {r['Delta_lambda']:>9.3f} "
              f"{r['log_q0_Delta']:>8.2f} {r['law_10A_minus_5']:>6} "
              f"{r['deviation_from_law']:>+6.2f}")
    print("NEAR-MATCH: Δ_λ(K) ≈ q0^(10A−5) — observation tier, not wired.")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
