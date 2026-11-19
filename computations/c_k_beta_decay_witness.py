#!/usr/bin/env python3
# polynomial_q_not_applicable: structural / substrate-derived
# closed-form computation; no symbolic-q output.
"""Substrate-derived dampening rate `c(K)` for the β-decay sector.

Verifies `prop:archimedean-remainder-exponential-decay` for the
free-neutron operator class `K`: the per-braid-mass-tower bound

    |R_N|  ≤  ℏ_q^{2(N+1)} / (1 - ℏ_q²)

equals

    |R_N|  ≤  C(K) · e^{-c(K) · N}

with closed-form rate constants derived from CAL-2 q_0 only:

    ℏ_q  =  (q_0 - 1) / q_0
    c(K)  =  -2 ln ℏ_q
    C(K)  =  ℏ_q² / (1 - ℏ_q²)

The witness:
  1. Loads CAL-2 q_0 (50 dps).
  2. Computes ℏ_q, c(K), C(K) symbolically.
  3. Tabulates the bound at depths N = 0, 1, 2, 3, 4.
  4. Compares the N=0 bound to the *observed* +1.31 keV residual on
     the single-wrap Q_β prediction (depth-0 truncation residual).
  5. Asserts the observed N=0 residual sits INSIDE the bound (the
     conjecture's structural ceiling).
  6. Emits a witness JSON via WitnessBuilder.

Note: the bound is a *ceiling* — the true c(K) for the operator
class may be larger (faster decay). The observation R_0 ≈ 0.168%
vs bound R_0 ≤ 0.991% says the actual fall-off is at least a factor
of ~6 faster than the worst-case bound at N=0. Pinning the *actual*
rate (vs the ceiling) is the open lift-formula part of the
brane-tower conjecture.

**Three-calibration discipline** (per
`docs/audits/2026-05-11-three-calibration-discipline-violations.md`
on PR #640): this script is **Class C (diagnostic / probe)**.
Inputs:

  * CAL-1 `m_e` — prediction input (via Form A = `prop:neutron-qvalue-symbolic`)
  * CAL-2 `q_0` — prediction input (via canonical pinning witness)
  * `Q_BETA_MEV` — **comparator only**, used to compute the
    OBSERVED residual `Q_β^pred - Q_β^CODATA` for the
    `N0_observed_residual_within_per_braid_bound` assertion. NOT
    a calibration input to the prediction or the bound.

The substrate-only prediction `Q_β^pred = Form A · E_0` consumes
only CAL-1 + CAL-2. CAL-3 (`Q_BETA_MEV`) enters only as the
empirical anchor for the ceiling-vs-observation comparison.

Output: `c-k-beta-decay-bound.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

# Set 50 dps BEFORE importing codata_constants — its mp.mpf
# constants are built at import time and otherwise inherit the
# default 15 dps (per Copilot review on PR #639).
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

Q_PINNING = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)

# Observed N=0 residual: single-wrap symbolic Q_β prediction
# Q_β = 0.7836 MeV vs CODATA Q_β = 0.7823 MeV.
# Residual = (0.7836 - 0.7823) / 0.7823 ≈ +0.168%.
N_DEPTHS = (0, 1, 2, 3, 4)


def _load_q_0() -> mp.mpf:
    with Q_PINNING.open() as fh:
        # 🛑 PROTON PIN (migrated 2026-08-29, bean `qou-cds3`). AGENTS.md
        # §"q₀ anchor convention": the experimental (proton) anchor is the default
        # for all production compute, and the owner authorisation recorded there
        # covers this sweep ("we want proton unless for an explicit reason ... fix
        # all, even if not visible").
        #
        # This read `q-pinning-50-digit.witness.json` -> `derived_50_digit.q`, the
        # MUON value, which NO manifest entry and NO `QOU_Q0_ANCHOR` could reach: a
        # direct read of the anchor-defining witness computes at muon whatever the
        # configuration says. The two pins differ by 11.54 ppb, the μ–p substrate
        # tension itself.
        #
        # The upstream record is KEPT — that witness remains the canonical 3-CAL
        # (muon) pin document, it is simply no longer the source of this
        # computation's q₀. Idiom copied from `alpha/alpha_k_jones_markov_h12.py`.
        from q_parameter import Q_50_DIGIT_STR as _Q50_PROTON
        return mp.mpf(_Q50_PROTON)


def main() -> int:
    # dps already set at module import (see top of file).
    w = WitnessBuilder("c-k-beta-decay-bound", engine="mpmath")

    q_0 = _load_q_0()
    m_e = M_E_MEV
    q_codata = mp.mpf(str(Q_BETA_MEV))

    # ── ℏ_q, c(K), C(K) — closed-form from substrate ─────────────
    hbar_q = (q_0 - 1) / q_0
    hbar_q_sq = hbar_q * hbar_q
    c_K = -2 * mp.log(hbar_q)
    C_K = hbar_q_sq / (1 - hbar_q_sq)

    # ── Per-depth bound table ────────────────────────────────────
    # Bound: |R_N| ≤ ℏ_q^{2(N+1)} / (1 - ℏ_q²) = C(K) · exp(-c(K)·N)
    bound_rows = []
    for N in N_DEPTHS:
        bound_via_geometric = hbar_q ** (2 * (N + 1)) / (1 - hbar_q_sq)
        bound_via_exponential = C_K * mp.exp(-c_K * N)
        bound_ratio = bound_via_geometric / bound_via_exponential
        bound_rows.append({
            "N": N,
            "bound_geometric": fmt(bound_via_geometric),
            "bound_exponential": fmt(bound_via_exponential),
            "ratio_geom_over_exp": fmt(bound_ratio),
            "bound_pct": fmt(bound_via_geometric * mp.mpf(100)),
            "bound_ppm": fmt(bound_via_geometric * (mp.mpf(10) ** 6)),
            "bound_ppb": fmt(bound_via_geometric * (mp.mpf(10) ** 9)),
        })

    # ── Observed N=0 residual via the single-wrap symbolic form ──
    # Form A: Q_β = m_e · |q² - 2q - 1| · (q + 1) / (2 q³)
    q_beta_form_a = (
        m_e
        * abs(q_0 * q_0 - 2 * q_0 - 1)
        * (q_0 + 1)
        / (2 * q_0 ** 3)
    )
    r_0_observed_rel = abs(q_beta_form_a - q_codata) / q_codata
    r_0_observed_kev = abs(q_beta_form_a - q_codata) * 1000

    # Bound at N=0 (worst-case)
    bound_n0 = bound_rows[0]
    bound_n0_rel = mp.mpf(bound_n0["bound_geometric"])

    # Margin: observation / bound (should be ≤ 1)
    margin = r_0_observed_rel / bound_n0_rel
    # Faster-than-bound factor: bound / observation (should be ≥ 1)
    speedup = bound_n0_rel / r_0_observed_rel

    print("=" * 78)
    print("c(K) DAMPENING RATE FOR β-DECAY SECTOR (substrate-derived)")
    print("=" * 78)
    print(f"  q_0 (50 dps)          = {mp.nstr(q_0, 16)}")
    print(f"  ℏ_q = (q - 1)/q       = {mp.nstr(hbar_q, 16)}")
    print(f"  ℏ_q²                  = {mp.nstr(hbar_q_sq, 16)}")
    print(f"  c(K) = -2 ln ℏ_q      = {mp.nstr(c_K, 12)}")
    print(f"  C(K) = ℏ_q²/(1-ℏ_q²)  = {mp.nstr(C_K, 12)}")
    print()
    print("  Per-depth bound |R_N| ≤ ℏ_q^(2(N+1))/(1-ℏ_q²)")
    print("  ─────────────────────────────────────────────────────────────")
    print("    N |       bound (%) |       bound (ppm) |       bound (ppb)")
    print("  ─────────────────────────────────────────────────────────────")
    for r in bound_rows:
        print(
            f"    {r['N']} | {mp.nstr(mp.mpf(r['bound_pct']), 8):>15s} | "
            f"{mp.nstr(mp.mpf(r['bound_ppm']), 8):>17s} | {mp.nstr(mp.mpf(r['bound_ppb']), 8):>17s}"
        )
    print()
    print("  Observed N=0 residual (single-wrap Q_β vs CODATA):")
    print(f"    |Q_β^A - Q_β^CODATA|/Q_β^CODATA = {mp.nstr(r_0_observed_rel, 8)}  ({mp.nstr(r_0_observed_rel * mp.mpf(100), 5)}%)")
    print(f"    |Q_β^A - Q_β^CODATA|            = {mp.nstr(r_0_observed_kev, 8)} keV")
    print()
    print(f"  Bound at N=0                     = {mp.nstr(bound_n0_rel, 8)}  ({mp.nstr(bound_n0_rel * mp.mpf(100), 5)}%)")
    print(f"  margin = observed/bound          = {mp.nstr(margin, 6)}  (≤ 1 → inside bound ✓)")
    print(f"  speedup = bound/observed         = {mp.nstr(speedup, 6)}× (actual fall-off faster than ceiling)")

    w.set_content_block("prop:archimedean-remainder-exponential-decay")
    w.set_description(
        "Substrate-derived dampening rate c(K) for the β-decay "
        "operator class. From the per-braid-mass-tower bound "
        "|R_N| ≤ ℏ_q^(2(N+1))/(1-ℏ_q²) and the substrate identity "
        "ℏ_q = (q_0-1)/q_0, the bound reads exactly C(K)·exp(-c(K)·N) "
        "with c(K) = -2 ln ℏ_q ≈ 4.624 and C(K) = ℏ_q²/(1-ℏ_q²) ≈ "
        "0.00991. The observed N=0 residual (+0.168%, +1.31 keV) "
        "sits INSIDE the structural ceiling 0.991%, with a ~5.9× "
        "headroom. The actual c(K) for the operator may be larger "
        "than this ceiling rate — pinning it is the open lift-"
        "formula part of brane-tower-z-habiro. Witness CAL-1 + CAL-2 "
        "only; no CAL-3 (Q_β) input — N=0 prediction comes from "
        "prop:neutron-qvalue-symbolic."
    )
    w.add_parameter("q_0_50dps", fmt(q_0))
    w.add_parameter("m_e_MeV", fmt(m_e))
    w.add_parameter("Q_beta_codata_MeV", fmt(q_codata))
    w.add_data("hbar_q", fmt(hbar_q))
    w.add_data("hbar_q_sq", fmt(hbar_q_sq))
    w.add_data("c_K", fmt(c_K))
    w.add_data("C_K", fmt(C_K))
    w.add_data("bound_table", bound_rows)
    w.add_data("Q_beta_form_a_MeV", fmt(q_beta_form_a))
    w.add_data("R_0_observed_relative", fmt(r_0_observed_rel))
    w.add_data("R_0_observed_keV", fmt(r_0_observed_kev))
    w.add_data("R_0_bound_relative", fmt(bound_n0_rel))
    w.add_data("margin_observed_over_bound", fmt(margin))
    w.add_data("speedup_bound_over_observed", fmt(speedup))

    # Geometric and exponential forms must agree (sanity check on
    # the closed-form derivation of c(K)).
    max_ge_ratio_dev = max(
        abs(mp.mpf(r["ratio_geom_over_exp"]) - mp.mpf(1)) for r in bound_rows
    )
    w.add_assertion(
        "geometric_form_equals_exponential_form_to_50dps",
        computed=fmt(max_ge_ratio_dev),
        expected="0",
        tolerance="1e-40",
    )

    # The observation must sit inside the bound (margin ≤ 1).
    w.add_assertion(
        "N0_observed_residual_within_per_braid_bound",
        computed=fmt(margin),
        expected="0",
        tolerance="1",
    )
    out = w.save()
    print(f"\nWrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
