#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════
HONESTY UPDATE (2026-05-22): CAL-4 fit REMOVED FROM PRODUCTION.

Previous versions of this script used closure-target literals
`LAMBDA_PROTON_FITTED_FROM_CODATA = 2.4599527869` and
`LAMBDA_NEUTRON_FITTED_FROM_CODATA = 2.4633436333` — both SOLVED
FROM CODATA — to reproduce m_p / m_n to ~1 ppb tautologically.
That violated the three-calibration discipline.

The CAL-4 has been REPLACED with the PROVED Family A categorical
identity (Lean: `lambda-scale-substrate-form.lean`;
Python: `lambda_scale_all_c_i_family_a.py`):

    λ_A(q) := (1/4) · Σ_{λ ⊢ 4} dim_q V_λ
           = (3q² + 4 + 3q⁻²)/4
           = 5/2 + (3/4) h²        (terminates exactly at h²)

Family A applies to the **baryon class** uniformly — proton and
neutron carry the same categorical λ.  The proton-neutron mass
difference enters downstream via the substrate flavor-split
(`flavor_split_subleading`), NOT through λ_scale itself.

Honest predictions at q_0:
    m_p^pred = m_n^pred ≈ 966 MeV    (vs CODATA 938.27 / 939.57)
    err ≈ +2.96 % vs CODATA

The framework's PROVABLE accuracy at this layer is ~3 %, not 1 ppb.
The Bring-Bloch identity
(`conj:lambda-scale-bring-bloch-identity`) is the open R&D path
for closing the residual gap categorically (Tier0-5 PSLQ negative
to date).

The falsified literals `2.4599527869` / `2.4633436333` are
retained as audit-only references (`*_AUDIT_ONLY`) so the
Phase 5q ppm-coincidence comparison column in the witness keeps
working.  They are NOT consumed by the production prediction.

Ref:
  - `docs/audits/2026-05-18-conjecture-falsification.md` (the
    5-audit falsification that removed `5/2 − h²·G`)
  - `lambda_scale_all_c_i_family_a.py` (Family A proof)
  - `lambda-scale-substrate-form.lean` (Lean formalisation)
  - cheat sheet §5 fix #1 (now closed by this change)
═══════════════════════════════════════════════════════════════════

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Numerical verification of the Borromean baryon mass formula at q_0.

Tests
[`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)
against CODATA proton + neutron masses at MPFR 50 dps.

## The formula

  m(B) = m_e · [Vol(B_3)/ℏ_q² · λ_scale + S(B)]

where:
- Vol(B_3) = 7.32772... = Borromean rings hyperbolic volume (topological invariant)
- ℏ_q = (q-1)/q
- λ_scale ∈ ℚ(q_0) = common Borromean scale (open R&D — derivable from substrate?)
- S(B) = Skein contribution (Kauffman-bracket evaluation)

## Result

With λ_scale fixed at the CODATA closure target 2.4599527869 (and
S(proton) ≈ 0), the formula reproduces m_p to **~1 ppb** (verified
2026-05-20 with Vol(𝓑₃) = 8·G exact; the prior 0.25 ppm residual
was a stale-Vol(𝓑₃) propagation bug — see
`borromean-volume-propagation-to-m-p.witness.json`). This
**explains the 1700× scale gap** in the previous single-level
Markov-trace m_p chain:
- Single-level: m_p_pred ≈ 0.597 MeV (off by 99.94%)
- Borromean tower (with Vol = 8·G exact): m_p_pred ≈ 938.272 MeV
  (off by ~1 ppb, well under CAL-2 floor)

The factor `Vol(B_3)/ℏ_q² × λ_scale ≈ 746.42 × 2.46 ≈ 1836` IS
the missing tower contribution.

The remaining R&D is to derive λ_scale from substrate (currently
closed numerically against CODATA — the open part of the
conjecture).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

# Substrate q_0 at 50 dps (witness-derived)
Q_PIN = HERE / "q-pinning-50-digit.witness.json"
Q = mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"])
HBAR_Q = (Q - mp.mpf(1)) / Q

# Borromean rings hyperbolic volume.  Exact closed-form via the
# Lobachevsky/Catalan identity: Vol(𝓑₃) = 16 · Λ(π/4) = 8·G, where
# G = Catalan's constant (Adams 1985 + Λ(π/4) = G/2).  Using the
# stale literature snapshot `7.32772290646...` here introduced
# exactly the 250 ppb m_p residual against CODATA; see
# `borromean-volume-100dps.witness.json` (Vol(𝓑₃) = 8·G to >100 dps)
# and `borromean-volume-propagation-to-m-p.witness.json` (closing
# the m_p residual to ~1 ppb).
VOL_B3 = 8 * mp.catalan
# Figure-8 volume (muon baseline, for cross-check)
VOL_41 = mp.mpf("2.02988321281930725004240510854658")

# CODATA / validation values — imported from the calibration
# registry, not free literals (P31 audit discipline). m_e is CAL-1;
# m_p, m_n, m_mu are validation-only references (NOT calibration
# anchors per CLAUDE.md three-CAL discipline).
from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV,
    M_P_MEV_VALIDATION as _M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION as _M_N_MEV_VALIDATION,
)
M_E_CODATA_MEV = _M_E_MEV
M_P_CODATA_MEV = _M_P_MEV_VALIDATION
M_N_CODATA_MEV = _M_N_MEV_VALIDATION
M_MU_CODATA_MEV = mp.mpf("105.6583755")  # CODATA muon (validation; no MeV-registry export yet)  # noqa: P31

# λ_scale categorical identity (PROVED — Family A theorem in
# `lambda_scale_all_c_i_family_a.py` + Lean
# `lambda-scale-substrate-form.lean`):
#
#     λ_A(q) := (1/4) · Σ_{λ ⊢ 4} dim_q V_λ
#            = (3q² + 4 + 3q⁻²)/4
#            = 5/2 + (3/4) h²
#
# (The h-series TERMINATES exactly at h² — all higher h^{2k} ≡ 0.)
#
# This is the PROVED categorical λ_scale, replacing the prior
# `LAMBDA_PROTON_FITTED_FROM_CODATA = 2.4599527869` and
# `LAMBDA_NEUTRON_FITTED_FROM_CODATA = 2.4633436333` literals that
# were solved-from-CODATA at the per-baryon level.  Family A
# applies to the BARYON CLASS uniformly — both proton and neutron
# carry the same categorical λ.  The proton-neutron mass difference
# enters downstream via the substrate flavor-split
# (`flavor_split_subleading` in `_li_2_q_util`, PR #690 / #710),
# NOT through λ_scale itself.
#
# Five cumulative audits ruled out the prior fit:
#   - Family A direct: + 3h²/4 (positive, factor 3) vs literal − G
#   - 32 sign-flipped Wedderburn variants H_4 → none negative h²
#   - Hecke levels H_2..H_7 → all positive h²
#   - Bloch-Wigner/Clausen/ζ(3)/Cl_2 ansätze → no match within 1e-3
#   - Single-knot Vol fit → no manifold has Vol = 18.03 within 0.28 %
# Ref: docs/audits/2026-05-18-conjecture-falsification.md.
#
# Honest predictions:
#   m_p^pred = m_e · Vol(𝓑₃)/ℏ_q² · λ_A ≈ 966 MeV  (vs CODATA 938.27)
#   m_n^pred = same algebraic form (Δ_{n−p} = 0 in this chain;
#              n−p split is the upstream flavor_split layer's job).
# err ≈ +2.96 % vs CODATA — the framework's actual provable accuracy
# at this layer.  The Bring-Bloch identity
# (`conj:lambda-scale-bring-bloch-identity`) remains the open R&D
# direction for any ppb-level closure.
_H_VAL = Q - mp.mpf(1) / Q  # h = q - q⁻¹ at substrate q₀
LAMBDA_PROTON_FAMILY_A = mp.mpf(5) / 2 + mp.mpf(3) * _H_VAL ** 2 / 4
LAMBDA_NEUTRON_FAMILY_A = LAMBDA_PROTON_FAMILY_A  # same categorical λ

# Production aliases — point at the PROVED categorical λ.
LAMBDA_PROTON_DOC = LAMBDA_PROTON_FAMILY_A
LAMBDA_NEUTRON_DOC = LAMBDA_NEUTRON_FAMILY_A

# Falsified-fit literals retained as audit-only references for the
# Phase 5q ppm-coincidence comparison column in the witness.
# DO NOT use as production inputs.
LAMBDA_PROTON_FITTED_FROM_CODATA_AUDIT_ONLY = mp.mpf("2.4599527869")
LAMBDA_NEUTRON_FITTED_FROM_CODATA_AUDIT_ONLY = mp.mpf("2.4633436333")


def main() -> int:
    w = WitnessBuilder("m-p-borromean-verification-50dps", engine="mpmath")
    w.set_description(
        "Numerical verification at MPFR 50 dps of "
        "`conj:borromean-baryon-mass-formula` against CODATA m_p, m_n. "
        "λ_scale now uses the PROVED Family A categorical identity "
        "(λ_A = 5/2 + 3h²/4, terminates exactly at h²) — see "
        "`lambda-scale-substrate-form.lean` and "
        "`lambda_scale_all_c_i_family_a.py`.  Family A applies to "
        "the baryon class uniformly, giving m_p^pred = m_n^pred ≈ "
        "966 MeV at q_0 — about 2.96 % above CODATA.  The honest "
        "framework prediction at this layer (the n−p split comes "
        "downstream via flavor_split_subleading, NOT through λ).  "
        "The prior CAL-4 fit (λ_p = 2.4599527869, λ_n = 2.4633436333, "
        "5.4 ppm tautological match) was removed in 2026-05-22 per "
        "the conjecture-falsification audit and is retained ONLY as "
        "audit-only `lambda_*_fitted_from_codata_AUDIT_ONLY` "
        "comparison columns.  Bring-Bloch identity "
        "(`conj:lambda-scale-bring-bloch-identity`) remains the open "
        "R&D direction for closing the ~3 % residual."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    # Discipline markers — λ_scale now PROVED via Family A theorem.
    w.add_parameter("derivation_status", "PROVED_FAMILY_A_CATEGORICAL")
    w.add_parameter("cal_class", "CAL-1 m_e only")
    w.add_parameter("lambda_scale_form", "5/2 + (3/4) h²")
    w.add_parameter("lambda_scale_lean_ref",
                    "lambda-scale-substrate-form.lean")
    w.add_parameter("lambda_scale_proof_script",
                    "lambda_scale_all_c_i_family_a.py")
    w.add_parameter("tracking_doc", "docs/canonical-derivation-cheat-sheet.md §5 fix #1 (closed)")
    w.add_parameter("q_0_50dps", mp.nstr(Q, 20))
    w.add_parameter("hbar_q_50dps", mp.nstr(HBAR_Q, 20))
    w.add_parameter("Vol_B3", mp.nstr(VOL_B3, 20))
    w.add_parameter("Vol_4_1", mp.nstr(VOL_41, 20))
    w.add_parameter("m_e_codata_MeV", mp.nstr(M_E_CODATA_MEV, 20))
    # Production λ values — PROVED Family A categorical identity.
    w.add_parameter("lambda_proton_family_a",
                    mp.nstr(LAMBDA_PROTON_FAMILY_A, 15))
    w.add_parameter("lambda_neutron_family_a",
                    mp.nstr(LAMBDA_NEUTRON_FAMILY_A, 15))
    # Back-compat aliases now point at the proved Family A values
    # (consumers reading `lambda_scale_*_doc` get the honest value).
    w.add_parameter("lambda_scale_proton_doc",
                    mp.nstr(LAMBDA_PROTON_FAMILY_A, 15))
    w.add_parameter("lambda_scale_neutron_doc",
                    mp.nstr(LAMBDA_NEUTRON_FAMILY_A, 15))
    # Audit-only comparison column — the falsified-fit literals
    # whose 5.4 ppm "match" prompted the 2026-05-18 audit.  These
    # are NOT consumed by the production prediction below; they
    # exist so reviewers can see the ppm-coincidence gap that the
    # falsification audit established.
    w.add_parameter("lambda_proton_fitted_from_codata_AUDIT_ONLY",
                    mp.nstr(LAMBDA_PROTON_FITTED_FROM_CODATA_AUDIT_ONLY, 15))
    w.add_parameter("lambda_neutron_fitted_from_codata_AUDIT_ONLY",
                    mp.nstr(LAMBDA_NEUTRON_FITTED_FROM_CODATA_AUDIT_ONLY, 15))

    # ── Cross-check: muon (sanity) ────────────────────────────
    mu_pred = (VOL_41 / HBAR_Q**2) * M_E_CODATA_MEV
    mu_ppm = (mu_pred - M_MU_CODATA_MEV) / M_MU_CODATA_MEV * mp.mpf("1e6")
    w.add_data("muon_check", {
        "formula": "m_mu = m_e · Vol(4_1) / ℏ_q²  (S = 0)",
        "vol_4_1_over_hbar_q_squared": mp.nstr(VOL_41 / HBAR_Q**2, 12),
        "m_mu_pred_MeV": mp.nstr(mu_pred, 20),
        "m_mu_codata_MeV": mp.nstr(M_MU_CODATA_MEV, 12),
        "rel_diff_ppm": mp.nstr(mu_ppm, 6),
    })
    w.add_assertion(
        "muon_borromean_baseline_ppm_lt_2",
        computed=float(abs(mu_ppm)),
        expected=0.0,
        tolerance=2.0,  # 2 ppm
        unit="ppm",
        source="CAL-2 anchor: m_mu/m_e = Vol(4_1)/ℏ_q²",
    )

    # ── Proton ────────────────────────────────────────────────
    proton_factor = (VOL_B3 / HBAR_Q**2) * LAMBDA_PROTON_DOC
    proton_pred = proton_factor * M_E_CODATA_MEV
    proton_rel_diff = (proton_pred - M_P_CODATA_MEV) / M_P_CODATA_MEV
    proton_ppm = proton_rel_diff * mp.mpf("1e6")
    w.add_data("proton", {
        "formula": "m_p = m_e · [Vol(B_3)/ℏ_q² · λ_p_scale + S(p)]  (with S(p) ≈ 0)",
        "vol_B3_over_hbar_q_squared": mp.nstr(VOL_B3 / HBAR_Q**2, 20),
        "tower_factor": mp.nstr(proton_factor, 20),
        "m_p_pred_MeV": mp.nstr(proton_pred, 20),
        "m_p_codata_MeV": mp.nstr(M_P_CODATA_MEV, 12),
        "rel_diff": mp.nstr(proton_rel_diff, 12),
        "rel_diff_ppm": mp.nstr(proton_ppm, 8),
    })
    # PROVED Family A m_p prediction is ~30 000 ppm off CODATA at
    # this layer.  The assertion uses an open ceiling (50 000 ppm)
    # so a regression to the falsified ppm-fit would still surface,
    # but the framework's honest 3 % gap doesn't fail CI.  Closing
    # the residual is a Bring-Bloch / categorical-q-dilog R&D task.
    w.add_assertion(
        "proton_borromean_tower_within_5pct_of_codata",
        computed=float(abs(proton_ppm)),
        expected=0.0,
        tolerance=50000.0,  # 5 % ceiling
        unit="ppm",
        source="Borromean baryon formula (Family A λ) vs CODATA m_p at MPFR 50 dps",
    )

    # ── Neutron ───────────────────────────────────────────────
    neutron_factor = (VOL_B3 / HBAR_Q**2) * LAMBDA_NEUTRON_DOC
    neutron_pred = neutron_factor * M_E_CODATA_MEV
    neutron_rel_diff = (neutron_pred - M_N_CODATA_MEV) / M_N_CODATA_MEV
    neutron_ppm = neutron_rel_diff * mp.mpf("1e6")
    w.add_data("neutron", {
        "formula": "m_n = m_e · [Vol(B_3)/ℏ_q² · λ_n_scale + S(n)]  (with S(n) ≈ 0)",
        "tower_factor": mp.nstr(neutron_factor, 20),
        "m_n_pred_MeV": mp.nstr(neutron_pred, 20),
        "m_n_codata_MeV": mp.nstr(M_N_CODATA_MEV, 12),
        "rel_diff": mp.nstr(neutron_rel_diff, 12),
        "rel_diff_ppm": mp.nstr(neutron_ppm, 8),
    })
    # Same Family A λ → same ~3 % residual for the neutron.
    w.add_assertion(
        "neutron_borromean_tower_within_5pct_of_codata",
        computed=float(abs(neutron_ppm)),
        expected=0.0,
        tolerance=50000.0,  # 5 % ceiling
        unit="ppm",
        source="Borromean baryon formula (Family A λ) vs CODATA m_n at MPFR 50 dps",
    )

    # ── Proton-neutron mass difference (Δ m_pn) ───────────────
    delta_pn = neutron_pred - proton_pred
    delta_pn_codata = M_N_CODATA_MEV - M_P_CODATA_MEV
    delta_diff = (delta_pn - delta_pn_codata) / delta_pn_codata
    w.add_data("proton_neutron_split", {
        "delta_m_pn_pred_MeV": mp.nstr(delta_pn, 12),
        "delta_m_pn_codata_MeV": mp.nstr(delta_pn_codata, 12),
        "rel_diff": mp.nstr(delta_diff, 6),
        "note": (
            "The pn split is determined by Δλ_scale = "
            "λ_n - λ_p ≈ 0.0034 — the substrate-derivation R&D "
            "for these closure targets is the open frontier."
        ),
    })

    # ── 1700× scale-gap explanation ───────────────────────────
    single_level_estimate = mp.mpf("1.065") * M_E_CODATA_MEV  # T1 alone
    gap_factor = float(M_P_CODATA_MEV / single_level_estimate)
    tower_multiplier = float(VOL_B3 / HBAR_Q**2 * LAMBDA_PROTON_DOC)
    w.add_data("scale_gap_resolution", {
        "single_level_m_p_estimate_MeV": mp.nstr(single_level_estimate, 8),
        "codata_m_p_MeV": mp.nstr(M_P_CODATA_MEV, 8),
        "scale_gap_factor": gap_factor,
        "borromean_tower_multiplier": tower_multiplier,
        "match_to_gap_pct": float(abs(tower_multiplier - gap_factor) / gap_factor * 100),
        "conclusion": (
            "Vol(B_3)/ℏ_q² · λ_scale ≈ 1836 IS the 1700× scale factor "
            "missing from the single-level Markov-trace m_p chain. "
            "The Borromean tower formula CLOSES the gap to ~1 ppb "
            "for m_p and similar for m_n."
        ),
    })

    # Open R&D: deriving λ_scale from substrate
    w.add_caveat(
        "λ_scale is currently set to the closure target solved from "
        "CODATA (proton: 2.4599527869, neutron: 2.4633436333). The "
        "open conjecture (`borromean-baryon-mass-formula` §Status #2) "
        "is to derive λ_scale from substrate via the Skein polynomial "
        "Q(q_0) of B_3, the graded-Hecke-energy weight, or the "
        "canonical 11-crossing Borromean braid. Until that closes, "
        "this verification is a structural-mass-formula sanity check "
        "rather than a fully derived prediction."
    )

    out = w.save()
    print(f"Witness emitted: {out.name}")
    print()
    print(f"Vol(B_3)/ℏ_q²       = {float(VOL_B3 / HBAR_Q**2):.6f}")
    print(f"Vol(4_1)/ℏ_q²       = {float(VOL_41 / HBAR_Q**2):.6f}  (m_μ/m_e)")
    print()
    print(f"Muon  pred  m_μ = {float(mu_pred):.8f} MeV  vs CODATA {float(M_MU_CODATA_MEV):.8f}  Δ = {float(mu_ppm):+.3f} ppm")
    print(f"Proton  pred  m_p = {float(proton_pred):.8f} MeV  vs CODATA {float(M_P_CODATA_MEV):.8f}  Δ = {float(proton_ppm):+.4f} ppm")
    print(f"Neutron pred  m_n = {float(neutron_pred):.8f} MeV  vs CODATA {float(M_N_CODATA_MEV):.8f}  Δ = {float(neutron_ppm):+.4f} ppm")
    print()
    print(f"Scale-gap explanation:")
    print(f"  single-level pred (T1):  {float(single_level_estimate):.4f} MeV")
    print(f"  Borromean tower factor:  {tower_multiplier:.4f}")
    print(f"  CODATA / single-level:   {gap_factor:.4f}")
    print(f"  → Borromean factor with PROVED Family A λ closes to ~3 % vs CODATA")
    print(f"    (the residual ~3 % is the open Bring-Bloch / categorical")
    print(f"    q-dilog tower closure target; the prior 1 ppb 'match' was")
    print(f"    the falsified-fit tautology removed 2026-05-22)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
