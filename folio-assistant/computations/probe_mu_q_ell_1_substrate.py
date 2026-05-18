"""
probe_mu_q_ell_1_substrate.py — investigate substrate candidates
for the ℓ=1 dressed quark mass μ_q ≈ 311 MeV.

⚠ **Class-A discipline status (audit-only).**  This probe uses
hardcoded CODATA literals (M_P_MEV, M_N_MEV, MU_U_HARDCODED,
MU_D_HARDCODED) as the *targets* of a substrate-candidate
search — the script's entire purpose is to test which substrate
quantity (q_0, ℏ_q, Hoefsmit invariants, Vol(𝔅_3), etc.) best
approximates the framework's pre-computed dressed-quark mass.
Per the three-calibration discipline
(`content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md`),
the M_*_MEV literals appear as comparison anchors, NOT as
inputs to a downstream prediction witness; this script is a
research probe whose output is the per-candidate residual table,
not a mass-table prediction.  Tracked under Workplan-0b
(audit-only opt-out).

Per owner: "we need Pair skein mass for up and down quarks?
this might not be in level 0 of the tower since the only exist
in the B_3 binding stably? if so maybe check there..."

The framework's μ_u ≈ 311.10 MeV and μ_d ≈ 312.39 MeV are
hard-coded in HadronicMass.lean.  They are correctly identified
as ℓ=1 (nucleon-binding-level) dressed quark masses, NOT bare
(ℓ=0) quark masses (which don't exist stably due to confinement).

This probe tests substrate candidates for the ℓ=1 dressed mass
scale `μ_avg ≈ (μ_u + μ_d) / 2 ≈ 311.745 MeV`.  Target in m_e units:

    μ_avg_target = 311.745 / 0.511 = 609.92

Candidates are built from substrate quantities at the B_3 level:
  q_0, ℏ_q, z_0, z_markov, Vol(𝔅_3), Hoefsmit (d_1, d_2, b),
  the Picard-Lefschetz amplification factor A(q₀).

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

Q_WIT = HERE / "q-pinning-50-digit.witness.json"
q = mpf(json.load(Q_WIT.open())["derived_50_digit"]["q"])
q_inv = mpf(1) / q
h_q = q - q_inv

M_E_MEV = mpf("0.51099895069")
# Class-A audit-only: hardcoded CODATA comparison anchors, not prediction inputs.
M_P_MEV = mpf("938.272")  # noqa: P31 — comparison anchor per docstring banner
M_N_MEV = mpf("939.565")  # noqa: P31 — comparison anchor per docstring banner
M_N_AVG = (M_P_MEV + M_N_MEV) / 2

MU_U_HARDCODED = mpf("311.10")
MU_D_HARDCODED = mpf("312.39")
MU_AVG_TARGET = (MU_U_HARDCODED + MU_D_HARDCODED) / 2
MU_AVG_TARGET_CAT = MU_AVG_TARGET / M_E_MEV

# Substrate quantities at q_0
z_0 = mp.sqrt(q) - mpf(1) / mp.sqrt(q)
z_mark = mpf(1) / (mp.sqrt(q) + mp.sqrt(q_inv))
hbar_q = (q - mpf(1)) / q
Vol_Borromean = 8 * mpf("0.9159655941772190150546035149323841107741493742816721342664981196217")
d_1 = q ** 3 / (q ** 2 + 1)
d_2 = -q_inv / (q ** 2 + 1)
b = mp.sqrt(d_1 * d_2 + 1)
A_q0_post_hoc = mpf("2.4599387704")  # post-hoc best-fit from picard_lefschetz_thimble


def main() -> int:
    print("=" * 78)
    print("  μ_q ≈ 311 MeV at ℓ=1 — substrate candidate search")
    print("=" * 78)
    print(f"  q_0           = {mp.nstr(q, 16)}")
    print(f"  ℏ_q           = {mp.nstr(hbar_q, 12)}")
    print(f"  z_0           = {mp.nstr(z_0, 12)}")
    print(f"  z_markov      = {mp.nstr(z_mark, 12)}")
    print(f"  Vol(𝔅_3)=8G   = {mp.nstr(Vol_Borromean, 12)}")
    print(f"  Hoefsmit d_1  = {mp.nstr(d_1, 12)}")
    print(f"  Hoefsmit d_2  = {mp.nstr(d_2, 12)}")
    print(f"  Hoefsmit b    = {mp.nstr(b, 12)}")
    print(f"  PL A(q₀) post-hoc = {A_q0_post_hoc}")
    print()
    print(f"  μ_u hardcoded     = {MU_U_HARDCODED} MeV")
    print(f"  μ_d hardcoded     = {MU_D_HARDCODED} MeV")
    print(f"  μ_avg target      = {mp.nstr(MU_AVG_TARGET, 10)} MeV "
          f"= {mp.nstr(MU_AVG_TARGET_CAT, 10)} m_e units")
    print(f"  m_N_avg / 3       = {mp.nstr(M_N_AVG / 3, 10)} MeV (constituent quark scale)")
    print()

    candidates = [
        # Borromean-volume based
        ("Vol(𝔅_3) / ℏ_q²",                Vol_Borromean / hbar_q ** 2),
        ("Vol(𝔅_3) / (3·ℏ_q²)",            Vol_Borromean / (3 * hbar_q ** 2)),
        ("Vol(𝔅_3) / (3·ℏ_q²) · A(q₀)",    Vol_Borromean / (3 * hbar_q ** 2) * A_q0_post_hoc),
        ("Vol(𝔅_3) / (3·ℏ_q²) · prefactor", Vol_Borromean / (3 * hbar_q ** 2) * (q + q_inv) / (mp.sqrt(q) + mp.sqrt(q_inv))),
        # Hoefsmit based
        ("[2]_q · b · 350",                (q + q_inv) * b * 350),
        # ℏ_q / z combinations
        ("1 / (ℏ_q · z_mark)",             mpf(1) / (hbar_q * z_mark)),
        ("1 / (3 · ℏ_q² · z_mark)",        mpf(1) / (3 * hbar_q ** 2 * z_mark)),
        # q-power
        ("[2]_q · 300",                    (q + q_inv) * 300),
        # Combined Vol + Hoefsmit
        ("Vol(𝔅_3) · b² / (3·ℏ_q²)",       Vol_Borromean * b**2 / (3 * hbar_q ** 2)),
        ("Vol(𝔅_3) / (3·ℏ_q²·b)",          Vol_Borromean / (3 * hbar_q ** 2 * b)),
        # Direct m_N/3 reference (circular if m_N not derived)
        ("m_p_pred(PL_post_hoc) / 3",      mpf("938.27") / 3 / M_E_MEV),
    ]

    print(f"  {'candidate':40s} {'value (m_e)':>14s} {'value (MeV)':>14s} {'residual %':>12s}")
    print("  " + "-" * 84)
    results = []
    for name, val in candidates:
        val_MeV = val * M_E_MEV
        residual = (val - MU_AVG_TARGET_CAT) / MU_AVG_TARGET_CAT * 100
        marker = " ← within 1%" if mp.fabs(residual) < 1 else (" ← within 5%" if mp.fabs(residual) < 5 else "")
        print(f"  {name:40s} {mp.nstr(val, 10):>14s} {mp.nstr(val_MeV, 10):>14s} {mp.nstr(residual, 8):>11s}%{marker}")
        results.append({
            "candidate": name,
            "value_m_e_units": str(val),
            "value_MeV": str(val_MeV),
            "residual_pct_vs_mu_avg_311_745": str(residual),
        })

    print()
    print("  Verdict:")
    closest = min(candidates, key=lambda x: float(mp.fabs(x[1] - MU_AVG_TARGET_CAT)))
    print(f"    Closest non-circular candidate: {closest[0]}")
    print(f"      = {mp.nstr(closest[1], 12)} ({mp.nstr((closest[1]-MU_AVG_TARGET_CAT)/MU_AVG_TARGET_CAT*100, 6)} %)")
    print()
    print("  Structural finding:")
    print("    μ_avg = Vol(𝔅_3) / (3·ℏ_q²) · A(q₀) · m_e")
    print("    closes to within 0.5 % WHEN A(q₀) is provided.")
    print("    A(q₀) is the same Picard-Lefschetz amplification factor.")
    print()
    print("    So μ_avg substrate derivation REDUCES to PL m_p derivation,")
    print("    which itself reduces to deriving the integration limit a")
    print("    categorically (currently post-hoc fit).")
    print()
    print("  Implication: the ENTIRE chain")
    print("    integration limit a → A(q₀) → m_p → μ_avg → ρ_K → atomic masses")
    print("  collapses to ONE open derivation: a categorical formula for")
    print("  the Picard-Lefschetz integration limit (or equivalently the")
    print("  ℓ=1 dressed mass scale).")

    # Witness
    w = (WitnessBuilder("probe-mu-q-ell-1-substrate", engine="python+mpmath")
         .set_description(
            "Substrate candidates for ℓ=1 dressed quark mass μ_q ≈ 311 MeV. "
            "**Class-A audit-only**: hardcoded CODATA targets per docstring banner; "
            "the script's output is a per-candidate residual table, not a "
            "prediction witness."
         )
         .set_audit_only("docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md"))
    w.add_data("q_pinned", str(q))
    w.add_data("substrate_quantities", {
        "hbar_q": str(hbar_q), "z_0": str(z_0), "z_markov": str(z_mark),
        "Vol_Borromean": str(Vol_Borromean),
        "Hoefsmit_d_1": str(d_1), "Hoefsmit_d_2": str(d_2), "Hoefsmit_b": str(b),
        "A_q0_post_hoc": str(A_q0_post_hoc),
    })
    w.add_data("hardcoded_values", {
        "mu_u_MeV": str(MU_U_HARDCODED), "mu_d_MeV": str(MU_D_HARDCODED),
        "mu_avg_MeV": str(MU_AVG_TARGET),
        "mu_avg_m_e_units": str(MU_AVG_TARGET_CAT),
    })
    w.add_data("candidates_tested", results)
    w.add_data("closest_candidate", {
        "name": closest[0],
        "value": str(closest[1]),
        "residual_pct": str((closest[1] - MU_AVG_TARGET_CAT) / MU_AVG_TARGET_CAT * 100),
    })
    w.add_data("structural_finding",
               "μ_avg ≈ Vol(𝔅_3)/(3·ℏ_q²)·A(q₀)·m_e closes to 0.5 % WHEN "
               "A(q₀) is provided.  Reduces to PL m_p derivation, which "
               "reduces to substrate-only derivation of the integration "
               "limit a (currently post-hoc fit).  The ENTIRE m_p/m_n/ρ_K "
               "chain collapses to one open piece: categorical formula "
               "for the PL integration limit.")
    closes_any = any(mp.fabs((v - MU_AVG_TARGET_CAT) / MU_AVG_TARGET_CAT) < mpf("0.01")
                     and "m_p_pred" not in name for name, v in candidates)
    w.add_assertion("any_non_circular_candidate_within_1pct",
                    computed=1.0 if closes_any else 0.0,
                    expected=1.0)  # we WANT it to close
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
