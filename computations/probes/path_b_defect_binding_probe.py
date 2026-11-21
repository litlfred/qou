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
    M_H1_MEV_VALIDATION as _M_H1_MEV_MP,
)
from codata_constants import M_D_ATOMIC_MEV_VALIDATION, M_HE3_ATOMIC_MEV_VALIDATION, M_HE4_ATOMIC_MEV_VALIDATION, M_T_ATOMIC_MEV_VALIDATION  # noqa: E402  (AME registry)

Q0 = Q_MP
M_E_MEV = _M_E_MEV_MP   # mpf; float() cast removed 2026-08-31 (qou-46ab)
M_P_MEV = _M_P_MEV_MP   # mpf; float() cast removed 2026-08-31 (qou-46ab)
m_n_derived_3input = _M_N_MEV_MP   # mpf; float() cast removed 2026-08-31 (qou-46ab)


# Canonical Markov traces |tr_M(T_w; q_0)|, read from the committed
# proton-anchored producer witness
# computations/canonical-tr-m-via-chi-cache.witness.json (q0Anchor: proton),
# which agrees with computations/markov/markov-peel-atomic-tr-m.witness.json
# to <= 3.8e-50.
#
# CONVENTION + PRECISION FIX (2026-08-31, bean qou-46ab). This block held
# SIX convention-C values, as bare float64 literals, under a comment calling
# them "Canonical":
#
#     p 1.0653062286   n 0.9232332972   D  0.3882864715
#     T 0.1040521187   3He 0.2065408586  4He 0.0553483459
#
# Two defects at once. (i) Convention: those are convention-C values at the
# muon pin -- n 0.9232332972 and D 0.3882864715 are exactly the values the
# n- and D-tr-M-q0 derivation chains reported before their 2026-08-31
# migration -- while convention D at the proton pin has been canonical since
# the owner rulings of 2026-08-09 and 2026-08-15 (R1/R2). Nothing in this
# file declared a frame, so they read as canonical D. (ii) Precision: bare
# float literals violate the NO-FLOAT64 discipline; TR_M feeds _geom(), a
# live computation, so the truncation propagates into the emitted witness.
# Both are fixed here by carrying mpmath.mpf at full witness precision.
#
# ══════════════════════════════════════════════════════════════════════════
# ⚠ (iii) A THIRD DEFECT, 2026-09-13 — AND IT IS THE SAME SHAPE AS (i).
#
# The fix for (i) moved these to "convention D at the proton pin", canonical
# when it landed on 2026-08-31. The 2026-09-05 owner ruling (bean `qou-hu1f`)
# then made the borromean intra-nucleon word canonical, and this table did not
# follow. So the entries below are GROUPED-era.
#
# MEASURED, not inferred (bean `qou-4383`): every entry reproduces to 50
# significant digits under `atom_braid_word_3A(..., intra_order="grouped")`.
# The canonical (borromean) values at the same pin are
#
#   p    0.62932840220292191816534574677848592760021940063436
#   n    0.47513351715568221250609023267500579955840763470875
#   D    0.15196833920423160759266569775106614127124096465526
#   T    0.029144042360972065357254218791869844065838803564741
#   3He  0.058596253654436380218956715452130256830877107284187
#   4He  0.011237417659767421564199549374410607269662696081262
#
# NOT FLIPPED HERE, and the reason differs from the twelve-consumer argument
# that pins `derivation_chain.TR_M_AT_Q0`. This table is self-contained —
# nothing imports it. What stops a mechanical swap is that `alpha` is a
# CALIBRATED fit parameter (`alpha = B(D)/defect(D)`) and T / 3He / 4He are
# then pure predictions. Recomputing in the canonical frame does not correct a
# constant; it changes what the model SAYS about every atom, which is the
# owner's call on the model, not a frame repair. The emitted witness now
# declares `intra_ordering_frame: "grouped"` so no consumer has to guess.
#
# The lesson (i) and (iii) share: a hardcoded trace does not track a ruling.
# The durable fix is to read `canonical_trm_reference.tr_m_nucleon()`, which
# selects by recorded q0 and cannot serve the wrong frame silently.
# ══════════════════════════════════════════════════════════════════════════
# witness-copy-intentional: grouped-frame traces kept on purpose; the note above says why they
# are not flipped (an owner call on the model, not a frame repair).
TR_M = {
    "p":   mp.mpf("1.1457596924573008696890815957741193059437280619435"),
    "n":   mp.mpf("0.98774368811580957163402016550129498205504875906279"),
    "D":   mp.mpf("0.57517224391777187082653534398618088915249435289284"),
    "T":   mp.mpf("0.22931010210455650733209081026890887960280163645605"),
    "3He": mp.mpf("0.40376703685142817036867025333340254115508707059188"),
    "4He": mp.mpf("0.16097414544240738182587344098071685392360735413342"),
}

# CODATA atomic masses (MeV).
#
# `mp.mpf("...")`, not bare float literals. These are EXACT decimals as
# authored, and a bare literal makes each the nearest double instead — which
# then serializes at the raised dps as its full binary expansion
# (1876.123929999999973006197251379489898681640625…), i.e. fake precision the
# float64-padding ratchet counts. The `"n"` entry was already carried as mpf
# from the registry; the other five were floats, so the dict was mixed.
#
# NOT swapped for the registry's `M_D_MEV_VALIDATION` etc.: those are NUCLEAR
# masses (m_D = 1875.61294500) while these are ATOMIC (nucleus + electron), so
# the substitution would look like a tidy-up and silently change the physics.
M_AME = {
    "p":   _M_H1_MEV_MP,  # registry H-1 atomic mass; the typed 938.78308711 was 1.4e-5 MeV off
    "n":   _M_N_MEV_MP,
    "D":   M_D_ATOMIC_MEV_VALIDATION,
    "T":   M_T_ATOMIC_MEV_VALIDATION,
    "3He": M_HE3_ATOMIC_MEV_VALIDATION,
    "4He": M_HE4_ATOMIC_MEV_VALIDATION,
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
        # float() here is DISPLAY ONLY (AGENTS.md permits it inside an
        # f-string); tf / ta / defect stay mpf in every computation above.
        print(f"  {label:<6} {Z+N:>3}  {float(tf):>12.6e} {float(ta):>12.6e}  "
              f"{float(defect):>+12.6e}  {float(B_AME_val):>+10.4f}")
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
          f"{float(rD['B_AME_MeV']):.6f} / {float(rD['defect_tr_M']):.6e} = "
          f"{float(alpha):.6e} MeV per unit defect")

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
        print(f"  {r['atom']:<6} {r['A']:>3}  {float(B_pred):>+10.4f} "
              f"{float(r['B_AME_MeV']):>+10.4f} "
              f"{float(b_err):>+7.2f}%  {float(M_pred):>12.4f} "
              f"{float(M_AME[r['atom']]):>12.4f} "
              f"{float(m_err):>+7.4f}%")
        r["B_pred_MeV"] = B_pred
        r["M_pred_MeV"] = M_pred
        r["B_err_pct"] = b_err
        r["M_err_pct"] = m_err

    # Isospin (T vs ³He)
    rT = next(r for r in rows if r["atom"] == "T")
    r3 = next(r for r in rows if r["atom"] == "3He")
    print(f"\n  Isospin (T - ³He):")
    print(f"    M_pred(T) − M_pred(³He) = {float(rT['M_pred_MeV'] - r3['M_pred_MeV']):+.6f} MeV")
    print(f"    CODATA M(T) − M(³He)    = {float(M_AME['T'] - M_AME['3He']):+.6f} MeV")
    print(f"    B_pred(T) − B_pred(³He) = {float(rT['B_pred_MeV'] - r3['B_pred_MeV']):+.6f} MeV")
    print(f"    B_AME(T) − B_AME(³He)   = {float(rT['B_AME_MeV'] - r3['B_AME_MeV']):+.6f} MeV")

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
            print(f"    mean |B_err| = {float(sum(non_cal_b_errs)/len(non_cal_b_errs)):.3f}%")
            print(f"    max  |B_err| = {float(max(non_cal_b_errs)):.3f}%")
            print(f"    mean |M_err| = {float(sum(non_cal_m_errs)/len(non_cal_m_errs)):.4f}%")
            print(f"    max  |M_err| = {float(max(non_cal_m_errs)):.4f}%")

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
        # WHICH FRAME THE NUMBERS ABOVE ARE IN (bean qou-4383, 2026-09-13).
        # Machine-readable, because a consumer reading `rows` has no other way
        # to tell, and the same omission is what let the grouped values sit
        # here unnoticed. Same pattern as `weight_family` in the Magnus Omega2
        # witnesses (qou-za3q): declaring the frame costs nothing and removes
        # the ambiguity without re-meaning any existing field.
        "intra_ordering_frame": "grouped",
        "intra_ordering_frame_note": (
            "SUPERSEDED. The TR_M table this probe computes from is grouped-era: "
            "every entry reproduces to 50 significant digits under "
            "atom_braid_word_3A(..., intra_order='grouped'), measured 2026-09-13. "
            "The canonical word has been borromean since the 2026-09-05 owner "
            "ruling (bean qou-hu1f). So alpha and every prediction in `rows` are "
            "computed in a retired frame. Not silently re-framed here: alpha is a "
            "calibrated fit parameter (from B(D)), so recomputing in the canonical "
            "frame changes what the MODEL says, which is an owner call rather than "
            "a mechanical constant fix. Canonical values are recorded above the "
            "TR_M table in this file."
        ),
        "alpha_MeV_per_unit_defect": alpha,
        "calibrated_from": "deuteron",
        "rows": rows,
    }
    out = HERE / "path-b-defect-binding-probe.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
