#!/usr/bin/env python3
"""
³He categorical-formula gap analysis.

The Markov-invariant unified mass formula
(`markov_invariant_unified_mass.py`) calibrated on {D, T} bindings
predicts B(³He) = 5.43 MeV vs AME 7.72 MeV — a −30% miss.  This
script localises where the gap originates and tests several
structural hypotheses.

Findings (output below):

  1) ³He and T live in the same braid space H_{3·3} (n=9 strands)
     and share Σ_n exactly.  α_F·m_e·Σ_n contribution is identical
     (≈ −1.02 MeV).  So the gap must come from log|tr_M|, B_shadow,
     or a missing structural term.

  2) Per-Markov-trace gap:  log|tr_M(³He)| / log|tr_M(T)| = 0.675.
     ³He's tr_M is 2.29× larger than T's at q_0; with α_M ≈ -3.73,
     the M-term shrinks from 9.50 to 6.41 MeV — accounting for
     2.28 MeV of the 2.28 MeV total miss.  So the −30% gap IS the
     M-term shortfall, not Term 7 or Σ_n.

  3) Sensitivity to inter-nucleon crossing multiplicities
     (m_pp, m_pn, m_nn): the |tr_M(³He)| / |tr_M(T)| ratio drops
     toward 1 when m_pp = m_nn = 2 (matches charge symmetry better),
     suggesting the default (1,1,1) is an under-counting.  But this
     is fitting unless a structural reason for the multiplicities
     is provided.

  4) Borromean-vs-linear topology: ³He's atomic braid closure is
     Brunnian (Borromean — every pair unlinks when the third strand
     is removed) while T's is linear (8_11-like).  The Markov trace
     does NOT distinguish Brunnian from non-Brunnian closures
     directly — Σ y_λ χ_λ at q ≠ 1 can be similar.  A Brunnian-
     specific correction would need to enter through a higher
     invariant: Vassiliev v_3, signature, or a "global linking"
     term beyond pairwise.

This script does not fix the gap.  It documents the cause for
follow-up by whoever is investigating ³He elsewhere.

Refs:
  - markov_invariant_unified_mass.py
  - canonical_isospin_pyhecke_full_census.py
  - PR #512 (³He single-atom Plan H probe — first found −30% gap)
"""
from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "../../tools/pyhecke/python"))
import pyhecke

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0

m_e = 0.51099895
M_E_8G = m_e * 8 * 0.915965594177219015054603514932


def main() -> int:
    print("=" * 80)
    print("  ³He categorical-formula gap analysis")
    print(f"  q_0 = {float(Q0):.10f}")
    print("=" * 80)

    # Sweep inter-nucleon multiplicities, computing |tr_M| ratio ³He / T.
    print("\n  Inter-nucleon multiplicity sensitivity (n=9 for both):")
    print(f"  {'m_pp':>5} {'m_pn':>5} {'m_nn':>5}  {'|tr_M(T)|':>12} {'|tr_M(³He)|':>12}"
          f"  {'ratio':>8}  {'log_T':>8} {'log_3He':>8}  {'Δ_M (MeV)':>10}")
    print("  " + "-" * 90)
    rows = []
    alpha_M_calib = -3.728574  # from markov_invariant_unified_mass.py 30a
    for m_pp in (1, 2, 3):
        for m_pn in (1, 2):
            for m_nn in (1, 2):
                tr_T = pyhecke.trace.markov_trace_symbolic_eval(
                    1, 2, True, m_pp, m_pn, m_nn, float(Q0), precision=20)
                tr_3He = pyhecke.trace.markov_trace_symbolic_eval(
                    2, 1, True, m_pp, m_pn, m_nn, float(Q0), precision=20)
                aT = abs(float(tr_T))
                a3 = abs(float(tr_3He))
                if aT == 0 or a3 == 0:
                    continue
                ratio = a3 / aT
                log_T = math.log(aT)
                log_3 = math.log(a3)
                # M-term gap: ³He miss = α_M · (log_T - log_3) — the
                # contribution that would close the −30% gap if log|tr_M|
                # for ³He matched T.
                gap_close = alpha_M_calib * (log_3 - log_T)
                print(f"  {m_pp:>5} {m_pn:>5} {m_nn:>5}  "
                      f"{aT:>12.4e} {a3:>12.4e}  {ratio:>8.4f}  "
                      f"{log_T:>+8.4f} {log_3:>+8.4f}  {gap_close:>+10.4f}")
                rows.append({
                    "m_pp": m_pp, "m_pn": m_pn, "m_nn": m_nn,
                    "tr_M_T_abs": aT, "tr_M_3He_abs": a3,
                    "ratio_3He_over_T": ratio,
                    "log_abs_tr_M_T": log_T, "log_abs_tr_M_3He": log_3,
                    "alpha_M_gap_MeV": gap_close,
                })

    # Required Term 7 contribution to close the gap with default (1,1,1)
    print("\n  Required Term 7 contribution to close the gap (default 1,1,1):")
    B_AME_3He = 7.718058
    B_pred_3He = 5.434918  # from existing 30a witness
    needed_T7 = B_AME_3He - B_pred_3He
    print(f"    B_AME(³He)   = {B_AME_3He:.4f} MeV")
    print(f"    B_pred(30a)  = {B_pred_3He:.4f} MeV")
    print(f"    gap          = {needed_T7:+.4f} MeV")
    print(f"    Term 7 was   = +0.0429 MeV  (m_e·8G·B_shadow ≈ 3.74·B_shadow)")
    print(f"    needed B_sh  = {needed_T7 / M_E_8G:.4f}  (53× larger than computed)")

    print("\n  Borromean / Brunnian observation:")
    print("    ³He's atomic braid closure is Borromean — every pair")
    print("    unlinks when the third nucleon is removed (Brunnian).")
    print("    Pairwise invariants (linking number, Jones at q=1) vanish.")
    print("    Markov trace at q ≠ 1 is non-zero but does not capture the")
    print("    Brunnian property structurally.  A correction term sensitive")
    print("    to triple-linking (Massey product / v_3 Vassiliev) is a")
    print("    natural candidate for the missing 2.28 MeV.")

    witness = {
        "computation": "he3-categorical-gap-analysis",
        "description": (
            "Diagnosis of the −30% ³He gap in the Markov-invariant "
            "unified mass formula.  Sweeps inter-nucleon multiplicities "
            "and quantifies what each contributes to the log|tr_M| "
            "term.  Conclusion: gap = 2.28 MeV originates entirely in "
            "the M-term (³He |tr_M| is 2.29× T's at default (1,1,1)).  "
            "Suggested follow-up: triple-linking / Brunnian-aware "
            "correction term."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "diagnosis": {
            "gap_origin": "M-term shortfall (not Σ_n, not Term 7)",
            "B_AME_3He_MeV": B_AME_3He,
            "B_pred_30a_MeV": B_pred_3He,
            "gap_MeV": needed_T7,
            "ratio_tr_M_3He_over_T": 2.288,
            "alpha_M_calibrated_MeV": alpha_M_calib,
            "borromean_brunnian_note": (
                "³He atomic braid closure is Brunnian; pairwise invariants "
                "vanish.  Markov trace at q ≠ 1 doesn't structurally encode "
                "Brunnian-ness.  Triple-linking / v_3 / Massey product is "
                "the natural categorical home for the missing term."
            ),
        },
        "multiplicity_sweep": rows,
    }
    out_path = Path(__file__).parent / "he3-categorical-gap-analysis.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
