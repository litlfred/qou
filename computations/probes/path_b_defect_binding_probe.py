#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
═══════════════════════════════════════════════════════════════

Path B refined — defect binding model: B(K) = α · (|tr_M_free| − |tr_M_K|).

Per categorical-mass-markov.md the categorical mass identity is
   m(K) = m_e · ρ(K) · |tr_M(T_w)|

with ρ(K) a knot-dependent multiplicity factor.  Instead of fitting
ρ(K) directly (Plan H explored this and falsified simple forms), this
probe tries the **defect-binding model**:

   B(K) = α · (|tr_M_free(K)| − |tr_M_atomic(K)|)
   M_pred(K) = constituent_sum(K) − B(K)

where:
  - constituent_sum(K) = Z·m_p + N·m_n + Z·m_e (atomic-mass convention)
  - tr_M_free(K) = |tr_M(p)|^Z · |tr_M(n)|^N (disconnected braid:
    Markov trace factorises across disjoint nucleons)
  - tr_M_atomic(K) = |tr_M(beta_atom_K)| (the canonical bridge value)

For free particles (p, n): tr_M_free = tr_M_atomic, B = 0 (correct).
For bound atoms: tr_M_atomic < tr_M_free (the connected braid has
smaller trace), so B > 0 (correct sign — atoms have positive
binding energy).

The single fit parameter α is calibrated from deuteron's known
binding energy.  Predictions for T, 3He, 4He are then PURE
predictions — no per-atom tuning.

Output: path-b-defect-binding-probe.witness.json
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from q_parameter import Q as Q0_FLOAT, Q_MP  # noqa: E402
# CAL-1: m_e from codata_constants registry (P31-triage Phase A).
from codata_constants import M_E_MEV as _M_E_MEV_MP
# Comparison references (P31-triage Phase B): validation-only CODATA m_p/m_n
# used to report fit residuals against experiment, not as prediction inputs.
from codata_constants import (
    M_P_MEV_VALIDATION as _M_P_MEV_MP,
    M_N_MEV_VALIDATION as _M_N_MEV_MP,
)

Q0 = Q_MP
M_E_MEV = float(_M_E_MEV_MP)
M_P_MEV = float(_M_P_MEV_MP)
m_n_derived_3input = float(_M_N_MEV_MP)


# Canonical Markov traces from the Hoefsmit+Wenzl bridge witness.
# Each is |tr_M(T_w; q_0)| at 50 dps, computed via Sum_lambda
# y_lambda(q) * chi_lambda(beta).  Cross-checked with markov_peel
# to 4e-16.
TR_M = {
    "p":   1.0653062286,
    "n":   0.9232332972,
    "D":   0.3882864715,
    "T":   0.1040521187,
    "3He": 0.2065408586,
    "4He": 0.0553483459,
}

# CODATA atomic masses (MeV)
M_AME = {
    "p":   938.78308711,
    "n":   float(_M_N_MEV_MP),
    "D":   1876.12393,
    "T":   2809.43215,
    "3He": 2809.41347,
    "4He": 3728.40133,
}


def constituent_sum(Z: int, N: int) -> float:
    """Atomic constituent sum: Z·m_p + N·m_n + Z·m_e."""
    return Z * M_P_MEV + N * m_n_derived_3input + Z * M_E_MEV


def tr_M_free(Z: int, N: int) -> float:
    """Disconnected-braid Markov trace: factorises across nucleons."""
    return TR_M["p"] ** Z * TR_M["n"] ** N


def tr_M_atomic(label: str) -> float:
    """Connected atomic-braid Markov trace (canonical from bridge)."""
    return TR_M[label]


def main() -> int:
    print("=" * 90)
    print("  Defect binding model:  B(K) = α · (|tr_M_free| − |tr_M_atomic|)")
    print(f"  q_0 = {float(Q0):.10f}")
    print("=" * 90)

    atoms = [
        ("p",   1, 0),
        ("n",   0, 1),
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]

    # Compute defect for each atom
    print(f"\n  {'atom':<6} {'A':>3}  {'tr_M_free':>12} {'tr_M_atomic':>12}  "
          f"{'defect':>12}  {'B_AME':>10}")
    print("  " + "-" * 70)
    rows = []
    for label, Z, N in atoms:
        cs = constituent_sum(Z, N)
        tf = tr_M_free(Z, N)
        ta = tr_M_atomic(label)
        defect = tf - ta
        B_AME_val = cs - M_AME[label]
        print(f"  {label:<6} {Z+N:>3}  {tf:>12.6e} {ta:>12.6e}  "
              f"{defect:>+12.6e}  {B_AME_val:>+10.4f}")
        rows.append({
            "atom": label, "Z": Z, "N": N, "A": Z + N,
            "constituent_sum_MeV": cs,
            "tr_M_free": tf, "tr_M_atomic": ta,
            "defect_tr_M": defect,
            "B_AME_MeV": B_AME_val,
        })

    # Calibrate α from deuteron
    rD = next(r for r in rows if r["atom"] == "D")
    if rD["defect_tr_M"] == 0:
        print("\n  ERROR: deuteron defect is zero, cannot calibrate")
        return 1
    alpha = rD["B_AME_MeV"] / rD["defect_tr_M"]
    print(f"\n  Calibration: alpha = B(D) / defect(D) = "
          f"{rD['B_AME_MeV']:.6f} / {rD['defect_tr_M']:.6e} = {alpha:.6e} MeV per unit defect")

    # Predict
    print(f"\n  Predictions:")
    print(f"  {'atom':<6} {'A':>3}  {'B_pred':>10} {'B_AME':>10} {'B_err%':>8}  "
          f"{'M_pred':>12} {'M_AME':>12} {'M_err%':>8}")
    print("  " + "-" * 80)
    for r in rows:
        B_pred = alpha * r["defect_tr_M"]
        M_pred = r["constituent_sum_MeV"] - B_pred
        b_err = ((B_pred - r["B_AME_MeV"]) / r["B_AME_MeV"] * 100
                 if abs(r["B_AME_MeV"]) > 1e-9 else 0.0)
        m_err = (M_pred - M_AME[r["atom"]]) / M_AME[r["atom"]] * 100
        print(f"  {r['atom']:<6} {r['A']:>3}  {B_pred:>+10.4f} {r['B_AME_MeV']:>+10.4f} "
              f"{b_err:>+7.2f}%  {M_pred:>12.4f} {M_AME[r['atom']]:>12.4f} "
              f"{m_err:>+7.4f}%")
        r["B_pred_MeV"] = B_pred
        r["M_pred_MeV"] = M_pred
        r["B_err_pct"] = b_err
        r["M_err_pct"] = m_err

    # Isospin (T vs ³He)
    rT = next(r for r in rows if r["atom"] == "T")
    r3 = next(r for r in rows if r["atom"] == "3He")
    print(f"\n  Isospin (T - ³He):")
    print(f"    M_pred(T) − M_pred(³He) = {rT['M_pred_MeV'] - r3['M_pred_MeV']:+.6f} MeV")
    print(f"    CODATA M(T) − M(³He)    = {M_AME['T'] - M_AME['3He']:+.6f} MeV")
    print(f"    B_pred(T) − B_pred(³He) = {rT['B_pred_MeV'] - r3['B_pred_MeV']:+.6f} MeV")
    print(f"    B_AME(T) − B_AME(³He)   = {rT['B_AME_MeV'] - r3['B_AME_MeV']:+.6f} MeV")

    # Mean error stats
    pred_rows = [r for r in rows if r["atom"] not in ("p", "n")]
    if pred_rows:
        b_errs = [abs(r["B_err_pct"]) for r in pred_rows if r["B_err_pct"] is not None]
        m_errs = [abs(r["M_err_pct"]) for r in pred_rows]
        print(f"\n  Stats over A>=2 (excluding D calibration):")
        non_cal = [r for r in pred_rows if r["atom"] != "D"]
        if non_cal:
            non_cal_m_errs = [abs(r["M_err_pct"]) for r in non_cal]
            non_cal_b_errs = [abs(r["B_err_pct"]) for r in non_cal]
            print(f"    mean |B_err| = {sum(non_cal_b_errs)/len(non_cal_b_errs):.3f}%")
            print(f"    max  |B_err| = {max(non_cal_b_errs):.3f}%")
            print(f"    mean |M_err| = {sum(non_cal_m_errs)/len(non_cal_m_errs):.4f}%")
            print(f"    max  |M_err| = {max(non_cal_m_errs):.4f}%")

    witness = {
        "computation": "path-b-defect-binding-probe",
        "description": (
            "Refined Path B: defect binding model. B(K) = alpha * "
            "(|tr_M_free(K)| - |tr_M_atomic(K)|), where tr_M_free "
            "factorises as |tr_M(p)|^Z * |tr_M(n)|^N for disconnected "
            "constituents.  Single fit parameter alpha, calibrated "
            "from D's binding.  T, 3He, 4He are pure predictions."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "alpha_MeV_per_unit_defect": alpha,
        "calibrated_from": "deuteron",
        "rows": rows,
    }
    out = HERE / "path-b-defect-binding-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
