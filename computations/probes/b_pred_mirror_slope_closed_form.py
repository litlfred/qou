#!/usr/bin/env python3
"""b_pred_mirror_slope_closed_form.py — DERIVATION: the framework side of
the writhe coefficient κ in closed form.

RESULT. The isovector (mirror) slope of the canonical binding prediction,
b_pred = d(log_{q₀} B_pred)/dT₃ — measured A-constant ≈ +1.37 in
kappa_writhe_side_decomposition_probe.py and carrying ~78% of the
residual's bar-odd coefficient b = 4κ — has an exact closed form under
the Phase 5q identity used by binding_canonical's closed-form path:

    B_pred(Z,N) = E₀ · τ_p^Z τ_n^N · (1 − ε(Z,N)),
    ε(Z,N)      = z^{Z−1} (z − h/2) (z − h)^{N−1}          (Z,N ≥ 1)

    b_pred(A)   = log_{q₀}(τ_p/τ_n)
                  + log[(1−ε(N,Z)) / (1−ε(Z,N))] / ((N−Z)·ln q₀)

for a mirror pair (Z,N) ↔ (N,Z), and hence

    b_pred(A→∞) = log_{q₀}(τ_p / τ_n) ≈ 1.37181           (the plateau)

since ε → 0 geometrically (z ≈ 0.4994, z−h ≈ 0.2903 both < 1). The
finite-A rise 1.326 → 1.372 measured across A=6..12 is exactly the ε
correction. VERIFIED here against the measured slopes from the IMME
triplet/quartet witnesses to ≤ 1e-3 (their rounding).

CONSEQUENCES:
- The framework component of the per-writhe-unit coefficient is DERIVED:
  κ_FW = −b_pred(∞)/4 = −log_{q₀}(τ_p/τ_n)/4 ≈ −0.34295. The observable
  κ ≈ −0.437 = κ_FW + κ_AME leaves κ_AME ≈ −0.094 experimental
  (Coulomb isovector) — genuinely outside the trace.
- The earlier near-match flag log_{q₀}(z/(z−h))/4 = 1.2998 is REFUTED
  as the asymptote (scope (a)): interfaces enter only the vanishing ε
  term; the plateau is the p/n TRACE ratio, not an interface factor.
- Pipeline discriminant: the Borromean single pipeline has τ_p = τ_n
  (GAP-A-4), so its b_pred comes only from interfaces and must differ —
  measurable, and a test between the colour-weighted and Borromean
  nucleon representations.

τ_p, τ_n are computed by the same entry point binding_canonical uses
(tr_M_via_wenzl_bridge_mpfr on the canonical H_3 words, 50 dps).

Derived-tier for b_pred (algebra on the Phase 5q closed form; the
identity itself is the verified production closed form). κ overall
remains near-match: the AME-side piece is not derived. Not wired.

Ref: docs/audits/2026-06-29-delta-lambda-z-correction-writhe.md
Ref: computations/probes/kappa_writhe_side_decomposition_probe.py
Ref: computations/closed_form_tau_M.py (Phase 5q identity)
Ref: prop:alpha-k-derivation-procedure is NOT involved — trace-level only
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention: the
# bar-symmetriser of z, which averages the two flavours 50/50 and so cannot
# see the substrate flavour split. Imported, not open-coded, so there is one
# definition; the import is hard on purpose because a fallback would compute
# the blind convention while reporting success.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402

# Mirror pairs (Z, N) with Z < N, matching the IMME triplet (T₃=±1
# members) and quartet (inner ±1/2 members) witnesses.
MIRROR_PAIRS = [(2, 4), (3, 5), (4, 5), (4, 6), (5, 7)]

# Measured b_pred from kappa-writhe-side-decomposition-probe.witness.json
# (rounded to 4 decimals there).
MEASURED = {6: 1.326, 8: 1.365, 9: 1.369, 10: 1.371, 12: 1.372}


def nucleon_word(g0, g1):
    return [(c, d, 0) for c, d in g0] + [(c, d, 1) for c, d in g1]


def main() -> int:
    set_compute_dps()
    q = Q_MP; h = q - 1 / q
    z = q**3 / (q**2 + 1); lnq = mp.log(q)
    tau_p = mp.mpf(tr_M_via_wenzl_bridge_mpfr(
        nucleon_word(_PROTON_G0, _PROTON_G1), 3, Q_50_DIGIT_STR, dps=50))
    tau_n = mp.mpf(tr_M_via_wenzl_bridge_mpfr(
        nucleon_word(_NEUTRON_G0, _NEUTRON_G1), 3, Q_50_DIGIT_STR, dps=50))
    plateau = mp.log(tau_p / tau_n) / lnq
    interface_only = mp.log(z / (z - h)) / lnq / 4

    def eps(Z, N):
        return z**(Z - 1) * (z + _pn_d(h)) * (z - h)**(N - 1)

    print(f"tau_p = {mp.nstr(tau_p, 15)}")
    print(f"tau_n = {mp.nstr(tau_n, 15)}")
    print(f"plateau log_q0(tau_p/tau_n) = {mp.nstr(plateau, 10)}")

    rows = []
    max_dev = 0.0
    for Z, N in MIRROR_PAIRS:
        A = Z + N; dT = N - Z
        corr = mp.log((1 - eps(N, Z)) / (1 - eps(Z, N))) / (dT * lnq)
        bp = plateau + corr
        dev = abs(float(bp) - MEASURED[A])
        max_dev = max(max_dev, dev)
        rows.append({"A": A, "pair": f"({Z},{N})<->({N},{Z})",
                     "b_pred_closed_form": fmt(bp),
                     "eps_correction": fmt(corr),
                     "b_pred_measured": MEASURED[A],
                     "abs_dev": round(dev, 6)})
        print(f"A={A:>2}: closed {float(bp):.5f}  measured {MEASURED[A]:.3f}"
              f"  (ε-corr {float(corr):+.5f})")

    kappa_fw = -plateau / 4
    print(f"\nκ_FW = −plateau/4 = {mp.nstr(kappa_fw, 8)}")
    print(f"interface-only candidate log_q0(z/(z−h))/4 = "
          f"{mp.nstr(interface_only, 6)} → REFUTED as asymptote "
          f"(enters only the vanishing ε term)")

    b = WitnessBuilder("b-pred-mirror-slope-closed-form", output_dir=HERE)
    b.set_description(
        "DERIVATION (trace-level algebra on the Phase 5q closed form): "
        "the framework side of the writhe coefficient. b_pred(A) = "
        "log_q0(tau_p/tau_n) + geometrically-vanishing interface "
        "correction; plateau 1.37181 = the p/n trace ratio; matches the "
        "measured mirror slopes (A=6..12) to their rounding. Framework "
        "component of kappa DERIVED: kappa_FW = -log_q0(tau_p/tau_n)/4 "
        "= -0.34295; the AME-side remainder (~-0.094, Coulomb) is not "
        "framework-derivable. The interface-only candidate "
        "log_q0(z/(z-h))/4 = 1.2998 is refuted as the asymptote "
        "(scope (a)). Discriminant: the Borromean pipeline (tau_p = "
        "tau_n, GAP-A-4) must show a different b_pred (interfaces only). "
        "Not wired; kappa overall stays near-match (AME piece open).")
    b.add_parameter("tau_p", fmt(tau_p))
    b.add_parameter("tau_n", fmt(tau_n))
    b.add_parameter("plateau_log_q0_taup_over_taun", fmt(plateau))
    b.add_parameter("kappa_FW", fmt(kappa_fw))
    b.add_data("rows", rows)
    b.add_data("interface_only_candidate_log_q0_z_ratio_over_4",
               fmt(interface_only))
    b.add_data("interface_candidate_verdict",
               "REFUTED as asymptote — scope (a): appears only inside the "
               "vanishing eps correction, not the plateau")
    b.add_assertion(
        "closed_form_matches_measured_slopes",
        computed=max_dev, expected=0.0, tolerance=1e-3,
        unit="max |closed − measured| over A=6..12",
        source="kappa-writhe-side-decomposition-probe.witness.json "
               "(measured values rounded to 3-4 dp)")
    b.add_assertion(
        "plateau_equals_pn_trace_ratio",
        computed=plateau, expected=1.37181, tolerance=1e-4,
        unit="log_q0(tau_p/tau_n)",
        source="tr_M_via_wenzl_bridge_mpfr on canonical H_3 words at 50 dps")
    b.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
