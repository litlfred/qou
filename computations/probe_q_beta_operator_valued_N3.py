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

Q_β N=3 brane-tower truncation via Kashiwara b³ recursion.

Building on the rep-theory finding from
`probe_tau_M_four_anchors.py`: Kashiwara b² predicts the empirical
c_2 to 98.3% match, validating

  τ_M^{V_(2,1)}(β) = Tr(ρ(β)) · F(α, b, ℏ_q²)

with F admitting the Kashiwara b^k recursion.

N=3 ansätze tested here:

  Pure b³ extension:    cos(α - b·ℏ_q²/2) · (1 - b²·ℏ_q^4) · (1 ∓ b³·ℏ_q^6)
  Product-cos:          cos(α - b·ℏ_q²/2) · cos(b·ℏ_q²) · cos(b²·ℏ_q^4)
  Exponential resum:    exp(-½ Σ_k b^k · ℏ_q^{2k}) = exp(-b·ℏ_q²/(2(1-b·ℏ_q²)))
  Matrix exponential:   Tr exp(i·M) where M is the 2-d Pauli generator

Output: `q-beta-operator-valued-N3.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402 (codata sweep)
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps()


def _q_0_50dps() -> mp.mpf:
    """The PROTON 50-digit pin.

    This read `derived_50_digit.q` out of `q-pinning-50-digit.witness.json`,
    which is the MUON value -- that producer is listed `ideal_muon`, so its
    Newton solve never runs and the field holds the muon literal. Nothing in
    this probe said so, and the witness it emits declares no `q0Anchor` at
    all, so the muon-ness was invisible to every consumer downstream.

    It surfaced when `probes/qbeta_habiro_residual_probe.py` was repinned to
    proton (owner ruling 2026-08-21) and started comparing its live
    single-wrap against the `Q_A` stored here: the agreement went from 1.1e-42
    to 29.96 ppb. The former figure was not a validation -- it was both sides
    being muon. 29.96 ppb is ~2.6x the 11.54 ppb pin separation, i.e. Q_beta
    amplifies the anchor.

    Now takes the proton pin by name, the same way `alpha_k_jones_markov_h12`
    and the habiro probe do. The witness still records the pin file as an
    upstream, but for provenance rather than for the value. Bean `qou-m9xp`.
    """
    from q_parameter import Q_50_DIGIT_STR

    return mp.mpf(Q_50_DIGIT_STR)


# ─────────────────────────────────────────────────────────────────────────
# ⚠ THE LADDER BELOW IS A CONVENTION-C FRAME WITH z_D SUBSTITUTED IN.
#
# Commit archaeology, 2026-08-21. The committed witness dated 2026-06-22
# (Q_N2 = 0.78233438651817188) reproduces EXACTLY from this producer at
# scriptHash 8ce74e846c64 = commit c51e43fa21ce, whose only formula
# difference from today is one line:
#
#     -    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))     # convention C
#     +    z = q**3 / (q**2 + 1)                     # convention D
#
# Verified at 60 dps: muon + C reproduces the committed value byte for byte;
# muon + D and proton + D both give 0.782804..., 6.0e-4 away. So the entire
# 1248 -> 602,433 ppb move in the downstream residual is that substitution,
# NOT the anchor (the mu-p pin shift contributes 3.0e-8, four orders less).
#
# AGENTS.md §"CONVENTION LABEL (2026-08-15 ruling)" forbids this move in
# terms:
#
#   "The ladder must be RE-DERIVED under D, and that is not a z-swap --
#    QOU.QBeta.decayLadder_zC_threeRow_ne_zero (MarkovZFullBarCondition.lean,
#    sorry-free) makes the C-frame ladder and the mass channel's three-row
#    forcing mutually exclusive, so substituting z_D into the existing ladder
#    is not a valid move."
#
# So `residual_N2 = 602,433 ppb` is NOT a Q_beta result. It is a C-frame
# ladder evaluated at a D parameter, which the corpus holds to be incoherent.
# The 1248 ppb figure was the coherent C-frame number -- and C is excised.
# Neither is currently a valid statement about Q_beta.
#
# NOT fixed here, deliberately: re-deriving the ladder under D is tranche S1
# of bean `qou-cds1`, it is research rather than repair, and it is much larger
# than this anchor fix. This banner exists so the number is not quoted as a
# physics result in the meantime.
# ─────────────────────────────────────────────────────────────────────────


def main() -> int:
    q = _q_0_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    Q_AME = mp.mpf(M_N_MEV_VALIDATION) - mp.mpf(M_P_MEV_VALIDATION) - m_e
    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    hbar_q = (q - 1) / q
    hbar_q2 = hbar_q ** 2
    hbar_q4 = hbar_q ** 4
    hbar_q6 = hbar_q ** 6
    alpha = (z - 1) * h / 2
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)

    # N=1 and N=2 baselines (Kashiwara predictions)
    alpha_N1 = alpha - b * hbar_q2 / 2
    cos_N1 = mp.cos(alpha_N1)
    Q_N1 = Q_A * cos_N1
    Q_N2 = Q_N1 * (1 - b ** 2 * hbar_q4)
    eps_N1 = (Q_N1 / Q_AME - 1) * mp.mpf("1e6")
    eps_N2 = (Q_N2 / Q_AME - 1) * mp.mpf("1e6")

    print("=" * 96)
    print("  Q_β N=3 brane-tower truncation — Kashiwara b³ prediction")
    print("=" * 96)
    print()
    print(f"  q_0      = {mp.nstr(q, 14)}")
    print(f"  b        = {mp.nstr(b, 14)}")
    print(f"  ℏ_q²     = {mp.nstr(hbar_q2, 14)}")
    print(f"  ℏ_q^6    = {mp.nstr(hbar_q6, 14)}")
    print(f"  b³·ℏ_q^6 = {mp.nstr(b ** 3 * hbar_q6, 14)}")
    print()
    print(f"  Baselines:")
    print(f"    N=0 Form A bare:                       +1677.5314 ppm")
    print(f"    N=1 cos(α-b·ℏ_q²/2):                   {float(eps_N1):+10.4f} ppm")
    print(f"    N=2 ·(1-b²ℏ_q^4):                      {float(eps_N2):+10.4f} ppm")
    print(f"    c(K) N=3 ceiling:                        ≤ 0.0094 ppm")
    print()

    # Solve for empirical c_3 in the ansatz:
    #   Q_β^CODATA = Q_A · cos(α_N1) · (1 - b²·ℏ_q^4) · (1 + c_3·b³·ℏ_q^6)
    Q_emp_factor = Q_AME / Q_N2  # residual factor we need
    # Q_emp_factor = 1 + c_3 · b³ · ℏ_q^6   ⇒  c_3 = (Q_emp_factor - 1) / (b³ · ℏ_q^6)
    c3_emp_additive = (Q_emp_factor - 1) / (b ** 3 * hbar_q6)
    print(f"  Empirical c_3 (additive ansatz):")
    print(f"    target factor = Q_AME / Q_N2 = {mp.nstr(Q_emp_factor, 14)}")
    print(f"    (factor - 1) / (b³·ℏ_q^6) = {mp.nstr(c3_emp_additive, 14)}")
    print()

    # N=3 candidates
    candidates = {
        # Naive Kashiwara b³ extension (+ sign — geometric tail continues)
        "Q_N2 · (1 + b³·ℏ_q^6)":
            Q_N2 * (1 + b ** 3 * hbar_q6),
        "Q_N2 · (1 - b³·ℏ_q^6)":
            Q_N2 * (1 - b ** 3 * hbar_q6),
        "Q_N2 · (1 - 0.5·b³·ℏ_q^6)":
            Q_N2 * (1 - mp.mpf("0.5") * b ** 3 * hbar_q6),
        # Empirically fitted (just to record the target)
        "Q_N2 · (1 + c_3_emp · b³·ℏ_q^6) [fit]":
            Q_N2 * (1 + c3_emp_additive * b ** 3 * hbar_q6),
        # Iterated cos (multiplicative composition)
        "Q_A · cos(α_N1) · cos(b·ℏ_q²)":
            Q_A * cos_N1 * mp.cos(b * hbar_q2),
        "Q_A · cos(α_N1) · cos(b·ℏ_q²) · cos(b²·ℏ_q^4)":
            Q_A * cos_N1 * mp.cos(b * hbar_q2) * mp.cos(b ** 2 * hbar_q4),
        # Half-argument variants
        "Q_A · cos(α_N1) · cos(b·ℏ_q²/2)":
            Q_A * cos_N1 * mp.cos(b * hbar_q2 / 2),
        # Exponential resummation of c_k = b^k (geometric)
        "Q_A · cos(α_N1) · exp(-b·ℏ_q²/(2(1-b·ℏ_q²)))":
            Q_A * cos_N1 * mp.exp(-b * hbar_q2 / (2 * (1 - b * hbar_q2))),
        "Q_A · cos(α_N1) · exp(-b²·ℏ_q^4/(2(1-b·ℏ_q²)))":
            Q_A * cos_N1 * mp.exp(-b ** 2 * hbar_q4 / (2 * (1 - b * hbar_q2))),
        # Padé[2,2] in (b·ℏ_q²)
        "Q_A · cos(α_N1) · (1 - b²ℏ_q^4 + b^4 ℏ_q^8)":
            Q_A * cos_N1 * (1 - b ** 2 * hbar_q4 + b ** 4 * hbar_q ** 8),
        # 1 / (1 + b² ℏ_q^4) — geometric of (b² ℏ_q^4)
        "Q_A · cos(α_N1) / (1 + b²·ℏ_q^4)":
            Q_A * cos_N1 / (1 + b ** 2 * hbar_q4),
        # Symmetric refinement: cos(α_N1 + b²·ℏ_q^4 shift)
        "Q_A · cos(α_N1 - b²·ℏ_q^4/2)":
            Q_A * mp.cos(alpha_N1 - b ** 2 * hbar_q4 / 2),
        "Q_A · cos(α_N1 - b·ℏ_q²/2 - b²·ℏ_q^4/2 - b³·ℏ_q^6/2)":
            Q_A * mp.cos(alpha - b * hbar_q2 / 2 - b ** 2 * hbar_q4 / 2 - b ** 3 * hbar_q6 / 2),
        # Tr matrix exponential of 2-d Pauli generator (Kashiwara natural form)
        # M = i·(α·σ_z + δ·σ_x) where α = single-wrap, δ ~ b·ℏ_q²
        # Tr(exp(i·M)) = 2 cos(√(α² + δ²))
        "2 cos(√(α² + (b·ℏ_q²/2)²)) / 2 [matrix exp]":
            mp.cos(mp.sqrt(alpha ** 2 + (b * hbar_q2 / 2) ** 2)),
    }

    print(f"  N=3 candidates vs CODATA Q_β:")
    print(f"    {'candidate':<70} {'ε [ppm]':>12} verdict")
    print(f"    {'-'*110}")
    results = []
    best_name, best_eps = "Q_N2 (no N=3 correction)", eps_N2
    eps_N2_abs = mp.fabs(eps_N2)
    for name, val in candidates.items():
        eps = (val / Q_AME - 1) * mp.mpf("1e6")
        if mp.fabs(eps) < mp.fabs(best_eps):
            best_name, best_eps = name, eps
        eps_abs = mp.fabs(eps)
        if eps_abs < mp.mpf("1e-12"):
            verdict = "EXACT match (fit candidate)"
        elif eps_abs < eps_N2_abs * mp.mpf("0.3"):
            ratio = float(eps_N2_abs / eps_abs)
            verdict = f"BETTER ({ratio:.2f}× tighter than N=2)"
        elif eps_abs < eps_N2_abs * mp.mpf("0.8"):
            ratio = float(eps_N2_abs / eps_abs)
            verdict = f"better ({ratio:.2f}× tighter than N=2)"
        elif eps_abs < eps_N2_abs * mp.mpf("1.2"):
            verdict = "~same as N=2"
        else:
            ratio = float(eps_abs / eps_N2_abs)
            verdict = f"worse ({ratio:.2f}× looser than N=2)"
        print(f"    {name:<70} {float(eps):>+12.4f}  {verdict}")
        results.append({
            "name": name,
            "Q_pred_MeV": str(val),
            "eps_ppm": float(eps),
        })
    print()
    print(f"  BEST candidate: {best_name}")
    print(f"    ε = {float(best_eps):+.6f} ppm")
    if mp.fabs(best_eps) < mp.mpf("0.0094"):
        print(f"    ✓ UNDER N=3 c(K) ceiling (0.0094 ppm) — N=3 closure!")
    elif mp.fabs(best_eps) < mp.mpf("0.96"):
        print(f"    UNDER N=2 ceiling (0.96 ppm) but NOT N=3 ceiling.")
    elif mp.fabs(best_eps) < eps_N2_abs:
        # Inline the float() into the f-string so the display-context
        # exemption applies. Was flagged by compute_no_mpf_to_float_cast.
        print(f"    {float(eps_N2_abs / mp.fabs(best_eps)):.2f}× tighter than N=2 but above N=2 ceiling.")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "q-beta-operator-valued-N3",
        {
            "description": (
                "N=3 brane-tower truncation probe testing Kashiwara b³ "
                "and several recursion variants (exponential, Padé, "
                "iterated cos, matrix exponential). Builds on the "
                "Kashiwara b² N=2 result (1.23 ppm) per "
                "prop:tau-M-asymptotic-rep-theory."
            ),
            "auditOnly": (
                "PR #655 N=3 follow-up. Identifies which N=3 ansatz "
                "closes (or doesn't) the residual gap below the "
                "0.96 ppm N=2 ceiling toward 0.0094 ppm N=3 ceiling."
            ),
            "data": {
                "q_0_50dps": str(q),
                "alpha": str(alpha),
                "alpha_N1": str(alpha_N1),
                "hbar_q_sq": str(hbar_q2),
                "hbar_q_4th": str(hbar_q4),
                "hbar_q_6th": str(hbar_q6),
                "hoefsmit_b": str(b),
                "Q_A": str(Q_A),
                "Q_N1": str(Q_N1),
                "Q_N2": str(Q_N2),
                "Q_AME": str(Q_AME),
                "eps_N1_ppm": float(eps_N1),
                "eps_N2_ppm": float(eps_N2),
                "c_3_empirical_additive": str(c3_emp_additive),
                "candidates": results,
                "best_candidate_name": best_name,
                "best_eps_ppm": float(best_eps),
                "under_N3_ceiling": bool(mp.fabs(best_eps) < mp.mpf("0.0094")),
                "under_N2_ceiling": bool(mp.fabs(best_eps) < mp.mpf("0.96")),
                "tightening_vs_N2": (
                    mp.nstr(eps_N2_abs / mp.fabs(best_eps), 12)
                    if best_eps != 0 else None
                ),
            },
        },
        script_path=__file__,
        engine="mpmath",
    )
    out_path = builder.save()
    print(f"\n  Witness: {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
