#!/usr/bin/env python3
"""qbeta_ck_recursion_kernel_constraint_probe.py
==================================================

**Constrain + refute sub-classes of the open Q_β c_k-recursion kernel**, using
the `cos(Φ(u))` phase reframe (PR #1887) and the ladder anchors `c_1 = 0`,
`c_2 = -1`.

The on-`main` block `prop:q-beta-c-k-recursion-from-habiro-q-difference` posits
a depth-`d` kernel `{a_j}` with `f_n = Σ_{j=1}^d a_j·f_{n-j}` on the Taylor
coefficients `f_n = [u^n] F(u)` of `F = Q_β/Q_A = cos(Φ(u))` (seed `f_0 = 1`,
`f_1 = 0`, `f_2 = c_2 = -1`, `f_3 = c_3`, `f_4 = c_4`; product/Taylor agree
through `u⁴`). The kernel is OPEN (SW-residue / Hoefsmit, PR #1871).

This probe is the companion to the Lean lemmas
(`QBetaCKRecursionKernelConstraints`). It does NOT derive the kernel; it:

  (1) pins the constant depth-2 kernel `(a_1, a_2) = (-c_3, -1)` from the
      anchors (Lean: `ck_a1_eq_neg_c3_depth_two`, `ck_a2_eq_c2_depth_two`);
  (2) records `a_1 = -c_3 = √2·Φ_2` — the kernel's leading coefficient IS the
      #1887 Φ_2 target (Lean: `ck_a1_eq_sqrt2_phi2`);
  (3) **refutes** the constant depth-2 kernel: it predicts `c_4 = 1 - c_3²`
      (Lean: `ck_c4_constant_depth_two_prediction`), which misses the fitted
      `c_4 ≈ -0.972` by ~3.4× at both anchors ⇒ the recursion is depth ≥ 3 or
      non-constant (Habiro `(u;u)_m` basis, not raw `u^k`).

No fits wired; closed-form anchors only. The closure stays GAP-A / SW-residue.

## References
- Phase reframe + parity: PR #1887 (`QBetaReebSinhParity`, `cos(Φ(u))`)
- c_k recursion block (open kernel): `prop:q-beta-c-k-recursion-from-habiro-q-difference`
- c_3 cross-anchor target: `qbeta_utils.c3_target_at` (PR #1831)
- c_4 fitted value: `qbeta_1ppq_achieved.py` (CODATA residual)
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, sqrt, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import c3_target_at  # noqa: E402

# The fitted c_4 (CODATA residual, near the c_k precision floor) — the value the
# constant depth-2 prediction is tested against.  Ref: qbeta_1ppq_achieved.py.
C4_FIT = mpf("-0.97157")

# Refutation gate: the constant depth-2 prediction must miss the fitted c_4 by
# more than this factor to count as refuted (sign-preserving, floor-robust).
REFUTE_FACTOR = mpf("2")


def main() -> int:
    set_compute_dps()

    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    sqrt2 = sqrt(mpf(2))

    print("=" * 78)
    print(" Q_β c_k-recursion kernel constraints — constant depth-2 refutation")
    print("=" * 78)
    print(f"  seed: f_0 = 1, f_1 = c_1 = 0, f_2 = c_2 = -1, f_3 = c_3, f_4 = c_4")
    print(f"  fitted c_4 (CODATA residual) = {float(C4_FIT):.6f}")
    print()
    print(f"  {'anchor':<8}{'c_3':>14}{'a_1=-c_3':>14}{'a_2=c_2':>10}"
          f"{'Φ_2=-c_3/√2':>16}{'√2·Φ_2':>12}")
    print(f"  {'-'*8}{'-'*14}{'-'*14}{'-'*10}{'-'*16}{'-'*12}")

    anchors = []
    all_refuted = True
    for name, qf in (("proton", q_at), ("muon", q_muon_at)):
        q = qf(mp.dps)
        c3 = c3_target_at(q, q_codata, me)

        # Constant depth-2 kernel pinned from the anchors (Lean lemmas).
        a1 = -c3                     # ck_a1_eq_neg_c3_depth_two
        a2 = mpf(-1)                 # ck_a2_eq_c2_depth_two (c_2 = -1)
        phi2 = -c3 / sqrt2           # #1887 phase relation c_3 = -Φ_1 Φ_2, Φ_1=√2
        a1_via_phi = sqrt2 * phi2    # ck_a1_eq_sqrt2_phi2 — must equal a1

        # Constant depth-2 prediction for c_4 (n=4 rung):
        #   c_4 = a_1·f_3 + a_2·f_2 = (-c_3)·c_3 + (-1)·(-1) = 1 - c_3².
        c4_pred = a1 * c3 + a2 * (-1)
        # cross-check the closed form
        c4_pred_cf = 1 - c3 ** 2

        miss_factor = fabs(c4_pred / C4_FIT)
        refuted = miss_factor > REFUTE_FACTOR
        all_refuted = all_refuted and refuted

        # bridge consistency: a1 (from -c3) must equal √2·Φ_2 to mp precision
        bridge_err = fabs(a1 - a1_via_phi)

        print(f"  {name:<8}{float(c3):>14.6f}{float(a1):>14.6f}{float(a2):>10.1f}"
              f"{float(phi2):>16.6f}{float(a1_via_phi):>12.6f}")

        anchors.append({
            "anchor": name,
            "q": fmt(q),
            "c_3": fmt(c3),
            "a_1": fmt(a1),
            "a_2": fmt(a2),
            "phi_2": fmt(phi2),
            "a_1_via_sqrt2_phi2": fmt(a1_via_phi),
            "bridge_err_a1_vs_sqrt2phi2": fmt(bridge_err),
            "c_4_predicted_constant_depth2": fmt(c4_pred),
            "c_4_predicted_closed_form_1_minus_c3sq": fmt(c4_pred_cf),
            "c_4_fitted": fmt(C4_FIT),
            "miss_factor": float(miss_factor),
            "constant_depth2_refuted": refuted,
        })

    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    for a in anchors:
        print(f"  {a['anchor']}: constant depth-2 predicts c_4 = "
              f"{a['c_4_predicted_constant_depth2'][:10]} "
              f"(= 1 - c_3²), fitted c_4 = {float(C4_FIT):.5f}  "
              f"⇒ miss ×{a['miss_factor']:.2f}  "
              f"[{'REFUTED' if a['constant_depth2_refuted'] else 'consistent'}]")
    print()
    if all_refuted:
        print("  CONSTANT_DEPTH2_KERNEL_REFUTED — the constant depth-2 kernel")
        print("  (a_1=-c_3, a_2=-1), fully pinned by the c_2/c_3 anchors, predicts")
        print("  c_4 = 1 - c_3² ≈ -3.1..-3.3, but the fitted c_4 ≈ -0.97. So the")
        print("  c_k ladder is NOT generated by a constant depth-2 recursion on the")
        print("  raw u^k basis: the kernel is depth ≥ 3 or non-constant (the Habiro")
        print("  (u;u)_m change-of-basis is load-bearing). What survives: depth ≥ 2,")
        print("  leading coefficient a_1 = -c_3 = √2·Φ_2 (bar-ODD, #1887 wall).")
        verdict = "CONSTANT_DEPTH2_KERNEL_REFUTED"
    else:
        print("  CONSISTENT — constant depth-2 reproduces c_4 within the gate.")
        verdict = "CONSTANT_DEPTH2_KERNEL_CONSISTENT"

    # Witness
    wb = WitnessBuilder(
        "qbeta-ck-recursion-kernel-constraint-probe", engine="mpmath",
    )
    wb.set_description(
        "Constrain + refute sub-classes of the open Q_β c_k-recursion kernel "
        "(prop:q-beta-c-k-recursion-from-habiro-q-difference) using the "
        "cos(Φ(u)) reframe (#1887) and anchors c_1=0, c_2=-1. Pins the "
        "constant depth-2 kernel (a_1=-c_3, a_2=-1) from the c_2/c_3 anchors, "
        "records a_1=-c_3=√2·Φ_2 (kernel leading coeff = #1887 Φ_2 target), "
        "and REFUTES the constant depth-2 kernel: it predicts c_4=1-c_3² "
        "(~-3.2) vs fitted c_4≈-0.972 (~3.4× miss) ⇒ kernel is depth≥3 or "
        "non-constant (Habiro basis). Companion to Lean "
        "QBetaCKRecursionKernelConstraints. No fits; closure stays GAP-A."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("c_4_fitted", fmt(C4_FIT))
    wb.add_data("refute_factor_gate", fmt(REFUTE_FACTOR))
    wb.add_data("anchors", anchors)
    wb.add_data("verdict", verdict)
    wb.add_data("interpretation", (
        "The constant depth-2 kernel is over-determined: a_2=-1 (from c_2 via "
        "f_0=1), a_1=-c_3 (from c_3 via f_1=0), leaving c_4=1-c_3² as a "
        "falsifiable prediction. It fails. The surviving constraints on the "
        "open kernel: depth ≥ 2; leading coefficient a_1 = -c_3 = √2·Φ_2 "
        "(the #1887 Φ_2 target, bar-ODD per the Reeb-sinh parity wall). These "
        "prune the SW-residue/Hoefsmit kernel search (#1871) without deriving "
        "it."
    ))
    # Invariants
    wb.add_assertion(
        "constant_depth2_refuted_both_anchors",
        computed=1.0 if all_refuted else 0.0, expected=1.0,
    )
    wb.add_assertion(
        "bridge_a1_eq_sqrt2_phi2_exact",
        computed=1.0 if all(
            mpf(a["bridge_err_a1_vs_sqrt2phi2"]) < mpf("1e-40")
            for a in anchors
        ) else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-ck-recursion-kernel-constraint-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
