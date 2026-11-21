#!/usr/bin/env python3
# polynomial_q_not_applicable: probe; mpmath numeric eval at substrate q0; no fitted inputs.
"""
flavor_split_substrate_probe.py — VERIFICATION probe for the claim in
content block `prop:flavor-split-substrate`
(folio/quantum-observable-universe/mass-theory/flavor-split-substrate.md).

THE CLAIM. The proton–neutron mass splitting is a closed form in substrate
atoms with NO calibration to the u–d mass difference:

    (m_n − m_p) / M_N  ≈  (q − 1)² · (1 − q⁻⁴) / 3  =  ℏ_q² · h_q · [2]_q / 3

where  M_N = (m_p + m_n)/2,  ℏ_q = (q−1)/q,  h_q = q − q⁻¹,  [2]_q = q + q⁻¹.
This is the PROVEN *leading* substrate split (the block's stated formula).
Neither μ_u nor μ_d appears — only q₀ and the universal nucleon scale M_N.

WHAT THIS PROBE DOES.
  1. Evaluates the canonical *leading* substrate form at the canonical
     substrate q₀ (muon-anchored 50-digit value used by the whole
     computations/ layer, imported from q_parameter.Q_50_DIGIT_STR — NOT
     hardcoded) via the shared canonical utility
     `_li_2_q_util.flavor_split_leading(q)` (the single source of the
     Δm/M_N leading closed form; also consumed by closed_form_tau_M's
     bring_color_weighted δ split). NO fitted quark masses.
  2. Compares to the CODATA target (m_n − m_p)/M_N built from the single
     validation source (codata_constants.M_{P,N}_MEV_VALIDATION), and
     asserts archimedean agreement within a stated tolerance.
  3. Cross-checks that the two algebraic forms in the block agree exactly
     (machine precision): (q−1)²(1−q⁻⁴)/3  ==  ℏ_q²·h_q·[2]_q/3.

Honest verify-or-refute: NO fit. q₀ is forced; the formula is a Laurent
polynomial in q with fixed integer structure. The *leading* form misses
CODATA by ≈ 0.13 % (the known residual the block reports as −0.10 %); the
posited subleading (1+ℏ_q³) multiplier is NOT part of this block's proven
claim (audit 2026-06-29) and is deliberately NOT used here. The tolerance
is set to 2e-3 (0.2 %) — tight enough to reject any order-of-magnitude
mismatch, loose enough to admit the leading form's honest ~0.13 % residual.
If the number does not land, the probe FAILS and the block must NOT be
wired `status:"verified"`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`) working from
# the `probes/` cluster subdirectory, and puts the parent `computations/`
# dir on sys.path so `from _li_2_q_util import …` resolves. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
)
from _li_2_q_util import flavor_split_leading  # noqa: E402


# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# Verification tolerance on the relative error vs the CODATA split. The
# leading substrate form misses by ≈ 0.13 % (the block reports −0.10 %);
# we require < 0.2 % (2e-3), an honest archimedean-agreement gate that
# admits the known leading residual but rejects any gross mismatch.
REL_ERR_TOLERANCE = mpf("2e-3")

# Exact-identity tolerance (the two algebraic forms are the same Laurent
# polynomial; they must agree to compute precision).
IDENTITY_TOLERANCE = mpf("1e-40")


def main() -> None:
    set_compute_dps()
    wb = WitnessBuilder("flavor-split-substrate-probe", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    qi = 1 / q

    # ── Canonical leading substrate form via the shared utility ─────────
    delta_pred = flavor_split_leading(q, qi)  # (q−1)²(1−q⁻⁴)/3

    # ── Independent factored form ℏ_q²·h_q·[2]_q/3 (block's 2nd form) ────
    hbar = (q - 1) / q            # ℏ_q
    h_q = q - qi                  # h_q  = q − q⁻¹
    br2 = q + qi                  # [2]_q = q + q⁻¹
    delta_factored = hbar**2 * h_q * br2 / 3

    identity_gap = abs(delta_pred - delta_factored)

    # ── CODATA target (single validation source; no fitted quark mass) ──
    m_p = mpf(M_P_MEV_VALIDATION)
    m_n = mpf(M_N_MEV_VALIDATION)
    M_N_avg = (m_p + m_n) / 2
    delta_codata = (m_n - m_p) / M_N_avg

    rel_err = abs(delta_pred - delta_codata) / delta_codata

    passed = (rel_err < REL_ERR_TOLERANCE) and (identity_gap < IDENTITY_TOLERANCE)

    # ─── Report ──────────────────────────────────────────────────────────
    print("=" * 76)
    print(" (m_n−m_p)/M_N = (q−1)²(1−q⁻⁴)/3  —  substrate-pure vs CODATA at q₀")
    print("=" * 76)
    print(f"  q₀              = {mp.nstr(q, 30)}")
    print(f"  ℏ_q             = {mp.nstr(hbar, 20)}")
    print(f"  h_q = q−q⁻¹     = {mp.nstr(h_q, 20)}")
    print(f"  [2]_q = q+q⁻¹   = {mp.nstr(br2, 20)}")
    print("-" * 76)
    print(f"  δ_pred (leading)= {mp.nstr(delta_pred, 18)}   (q−1)²(1−q⁻⁴)/3")
    print(f"  δ_factored      = {mp.nstr(delta_factored, 18)}   ℏ_q²·h_q·[2]_q/3")
    print(f"  identity gap    = {mp.nstr(identity_gap, 6)}   (must be < {mp.nstr(IDENTITY_TOLERANCE,2)})")
    print("-" * 76)
    print(f"  δ_CODATA        = {mp.nstr(delta_codata, 18)}   (m_n−m_p)/M_N")
    print(f"    m_p           = {mp.nstr(m_p, 12)} MeV")
    print(f"    m_n           = {mp.nstr(m_n, 12)} MeV")
    print(f"  rel error       = {mp.nstr(rel_err, 6)}  ({float(rel_err) * 100:.4f} %)")
    print(f"  tolerance       = {mp.nstr(REL_ERR_TOLERANCE, 3)}  (0.2 %)")
    print("-" * 76)
    print(f"  VERDICT         = {'PASS' if passed else 'FAIL'}")
    if not passed:
        print("  ✗ leading substrate split does NOT reproduce CODATA (or the two")
        print("    algebraic forms disagree) within tolerance — do NOT wire this")
        print("    block status:'verified'.")

    # ─── Witness ─────────────────────────────────────────────────────────
    wb.set_content_block("prop:flavor-split-substrate")
    wb.set_description(
        "Verify the substrate-pure proton–neutron flavor-split closed form "
        "(m_n−m_p)/M_N = (q−1)²(1−q⁻⁴)/3 = ℏ_q²·h_q·[2]_q/3 (the PROVEN leading "
        "form; the posited (1+ℏ_q³) subleading is NOT this block's claim) at the "
        "canonical muon-anchored substrate q₀, via the shared canonical utility "
        "_li_2_q_util.flavor_split_leading. No fit and no u–d mass input: only q₀ "
        "and the nucleon scale M_N enter. Compares to the CODATA split built from "
        "codata_constants.M_{P,N}_MEV_VALIDATION (single source), cross-checks the "
        "two algebraic forms agree exactly, and asserts archimedean agreement "
        "< 0.2 % (measured ≈ 0.13 %, the block's −0.10 % leading residual)."
    )
    wb.add_data("inputs", {
        "q0": mp.nstr(q, 30),
        "q0_source": "q_parameter.Q_50_DIGIT_STR (muon-anchored canonical q0)",
        "m_p_MeV": mp.nstr(m_p, 20),
        "m_n_MeV": mp.nstr(m_n, 20),
        "codata_source": "codata_constants.M_{P,N}_MEV_VALIDATION",
        "producer": "_li_2_q_util.flavor_split_leading",
    })
    wb.add_data("substrate_atoms", {
        "hbar_q": mp.nstr(hbar, 30),
        "h_q": mp.nstr(h_q, 30),
        "bracket_2_q": mp.nstr(br2, 30),
    })
    wb.add_data("result", {
        "delta_pred_leading": mp.nstr(delta_pred, 30),
        "delta_factored": mp.nstr(delta_factored, 30),
        "identity_gap": mp.nstr(identity_gap, 12),
        "delta_codata": mp.nstr(delta_codata, 30),
        "rel_error": mp.nstr(rel_err, 12),
        "rel_error_percent": float(rel_err) * 100,
        "tolerance": mp.nstr(REL_ERR_TOLERANCE, 6),
        "verdict": "PASS" if passed else "FAIL",
    })
    wb.add_assertion(
        "flavor_split_matches_codata",
        computed=mp.nstr(rel_err, 12),
        expected="0",
        tolerance=float(REL_ERR_TOLERANCE),
        source="Relative error of the leading substrate flavor split "
               "(m_n−m_p)/M_N = (q−1)²(1−q⁻⁴)/3 (via _li_2_q_util."
               "flavor_split_leading) vs the CODATA split "
               "(M_N_MEV_VALIDATION−M_P_MEV_VALIDATION)/M_N, evaluated at the "
               "canonical muon-anchored substrate q₀ (50 dps). No fitted quark "
               "mass. Passes iff rel err < 2e-3 (0.2 %); measured ≈ 1.3e-3.",
    )
    wb.add_assertion(
        "two_algebraic_forms_agree_exactly",
        computed=mp.nstr(identity_gap, 12),
        expected="0",
        tolerance=float(IDENTITY_TOLERANCE),
        source="Exact identity (q−1)²(1−q⁻⁴)/3 == ℏ_q²·h_q·[2]_q/3 checked at "
               "compute precision; both are the same Laurent polynomial in q.",
    )
    path = wb.save()
    print(f"\n  witness -> {path}")

    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
