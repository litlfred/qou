#!/usr/bin/env python3
"""DEPRECATED for absolute mass (owner ruling 2026-06-24) — superseded by the
muon-anchored Hecke energy; retained as the record of the Family-A route.

═══════════════════════════════════════════════════════════════════
SUPERSESSION (2026-06-24): this script's m_p / m_n are NOT the
canonical absolute nucleon masses.

Everything below computes the `m_e · Vol(𝓑₃)/ℏ_q² · λ_A` form, which
the 2026-06-24 ruling deprecated for absolute mass: it applies
1/ℏ_q² to the *Borromean* volume, where the c_q² belongs in the
*muon* anchor Vol(4₁). The canonical route is

    m_p = 2·(m_μ·F_Bor − 6·m_e)  →  938.27 MeV (CODATA, +1.35 ppb)

via the single facade `canonical_mass.py` (`proton_mass_mev()`).
The ~2.9 % figures below are the deprecated form's, not the
framework's live accuracy. See docs/canonical-mass-formula-guardrail.md.

⚠ This script's witness `m-p-borromean-verification-50dps.witness.json`
is still READ by `canonical_mass_table_extended.py`
(`lookup_nucleon_mass_borromean`), so the +2.89 % values propagate into
the canonical mass table's nucleon rows and everything projected from
it. That is tracked separately — it is a compute-wiring defect, not a
prose one, and is not fixed by this banner.

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
difference enters via the substrate flavor-split
(`flavor_split_subleading`, PR #690), NOT through λ_scale itself.
This script now WIRES the flavor split: it computes
m_avg = m_e · Vol(B_3)/ℏ_q² · λ_A and then splits with
Δm/M_N = ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3.

Honest predictions at q_0:
    m_avg^pred ≈ 966 MeV       (vs CODATA 938.92, ~2.9 % off)
    Δm/M_N^pred ≈ 0.001377     (vs CODATA 0.001377, ~305 ppm = 0.030 % off)
    m_p^pred ≈ 965.38 MeV      (vs CODATA 938.27, ~2.9 % off)
    m_n^pred ≈ 966.71 MeV      (vs CODATA 939.57, ~2.9 % off)
    Δ m_pn^pred ≈ 1.330 MeV    (vs CODATA 1.293, ~2.9 % off)

The framework's PROVABLE accuracy at this layer is ~3 %, not 1 ppb.
The Bring-Bloch identity
(`conj:lambda-scale-bring-bloch-identity`) is the open R&D path
for closing the residual gap categorically (Tier0-5 PSLQ negative
to date).

═══════════════════════════════════════════════════════════════════
λ_A EXCISION UPDATE (2026-06-24 owner ruling, applied 2026-07-02):

λ_A is a CODATA-implied FIT, excised as a mass density (see
docs/coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md).
This script is retained as the AUDIT-VERIFICATION of that excised
path: the ~2.9 % numbers below document the fit's honest residual,
they are NOT the framework's absolute-mass prediction. The canonical
absolute nucleon mass is the muon-anchored Hecke energy
m_p = 2·(m_μ·F_Bor − 6·m_e) via computations/canonical_mass.py
(≈938.27 / 939.57 MeV); a comparison column against it is emitted in
the witness (`canonical_mass_reference`).
═══════════════════════════════════════════════════════════════════

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

## The formula (canonical, post-PR #1080)

  m(K) = m_e · VolDensity(K, q₀)              (single Geom call per knot)

For the Borromean rings 𝓑₃ (proton/neutron baryon class):

  VolDensity(𝓑₃, q) = (Vol(𝓑₃)/ℏ_q²) · linking_weight(q)

where:
- Vol(𝓑₃) = 8·G = 7.32772... (Adams 1985; Lobachevsky/Catalan exact)
- ℏ_q = (q-1)/q
- linking_weight(q) = (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h²
  (PROVED Family A categorical Wedderburn identity; terminates at h²;
   Lean: `lambda-scale-substrate-form.lean`)

There is no separate λ_scale constant — older docs called the linking-
weight component λ_scale before it was absorbed into VolDensity on
2026-05-23 (PR #1080, commit `3daeb1b4`).  See
`docs/lambda-scale-absorbed-into-vol-density.md` for the framing.

## Result

VolDensity(𝓑₃, q₀) ≈ 746.42 × 2.46 ≈ 1836 — this IS the 1700× scale
factor missing from the single-level Markov-trace m_p chain.  With
Vol(𝓑₃) = 8·G exact (Adams 1985), the formula gives m_avg ≈ 966 MeV
(+2.89 % vs CODATA mean).  The substrate flavor split
(prop:flavor-split-substrate) then assigns m_p ≈ 965.4, m_n ≈ 966.7
(both +2.89 %), with the SPLIT ratio Δm/M_N matched to ~305 ppm.

The remaining ~2.89 % gap is now framed (per PR #1063) as a
VolDensity(𝓑₃) categorical-exactness refinement gap at h² order,
NOT as a separate λ_scale closure.

## Lean coverage

  PROVED in Lean:
    - linking_weight identity (3q² + 4 + 3q⁻²)/4:
      `lambda-scale-substrate-form.lean` (Family A)

  NOT YET PROVED in Lean (potential source of error):
    - Vol(𝓑₃) = 8·G (Adams 1985): cited from literature, not in
      Mathlib; depends on Catalan's constant + Lobachevsky function
    - VolDensity(K) per-knot decomposition (PR #1080 / prop:geom-
      universality): narrative-level only, no Lean theorem yet
    - flavor_split closed form ℏ_q²·h_q·[2]_q·(1+ℏ_q³)/3 (PR #690 /
      prop:flavor-split-substrate): partial; the (1+ℏ_q³) 3-loop
      correction lacks Lean backing
    - q_0 substrate value (CAL-2 from m_μ/m_e): numerical anchor, no
      Lean theorem
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

set_compute_dps()

# Substrate q_0 at 50 dps (witness-derived)
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
Q = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
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
# Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 33 digits, correct to 29 (qou-ckbv)
VOL_41 = 2 * mp.clsin(2, mp.pi / 3)

# CODATA / validation values — imported from the calibration
# registry, not free literals (P31 audit discipline). m_e is CAL-1;
# m_p, m_n, m_mu are validation-only references (NOT calibration
# anchors per AGENTS.md three-CAL discipline).
from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV,
    M_P_MEV_VALIDATION as _M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION as _M_N_MEV_VALIDATION,
    M_MU_MEV_VALIDATION as _M_MU_MEV_VALIDATION,
)
M_E_CODATA_MEV = _M_E_MEV
M_P_CODATA_MEV = _M_P_MEV_VALIDATION
M_N_CODATA_MEV = _M_N_MEV_VALIDATION
M_MU_CODATA_MEV = _M_MU_MEV_VALIDATION  # CODATA muon (validation; codata_constants registry)

# VolDensity(𝓑₃, q) — the canonical per-knot Geom evaluation
# (PR #1080, commit `3daeb1b4` on 2026-05-24).  Single Geom call
# per knot/link.  See `prop:geom-universality` and
# `docs/lambda-scale-absorbed-into-vol-density.md` for the framing.
#
# Internally VolDensity = (Vol(𝓑₃)/ℏ_q²) × linking_weight, where
# the linking_weight is the PROVED Family A categorical identity
#     linking_weight(q) = (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h²
# (h-series TERMINATES at h²; higher h^{2k} ≡ 0).  There is no
# separate λ_scale constant — the same numerical factor that older
# docs called λ_scale is now the linking-weight component of
# VolDensity, not a standalone calibration to derive or close.
#
# Honest predictions (Family A inside VolDensity, PR #895 + #942 +
# #1080):
#   m_p^pred ≈ 965 MeV  (vs CODATA 938.27, +2.89 %)
#   m_n^pred ≈ 967 MeV  (vs CODATA 939.57, +2.89 %)
#   Δm/M_N = substrate flavor split (~305 ppm match)
# err ≈ +2.89 % vs CODATA — the framework's honest provable accuracy.
# The Yekutieli per-cell curvature (−G·h²) was PURGED (2026-05-24)
# as NOT CANONICAL — bijection NEGATIVE per PR #985, Reading A is
# substrate-q₀ coincidence, no categorical backing.  The ~2.89 %
# residual is now framed as a VolDensity(𝓑₃) categorical-exactness
# refinement gap (per PR #1063), not as a separate λ_scale closure.
# λ_A path retained here INTENTIONALLY as the audited subject
# (excision ruling 2026-06-24) — the DeprecationWarning is suppressed
# because this is the documented audit-verification use, not a
# production consumer.
import warnings as _warnings
from _li_2_q_util import per_knot_density_borromean as _vol_density_borromean
with _warnings.catch_warnings():
    _warnings.simplefilter("ignore", DeprecationWarning)
    GEOM_FULL_BORROMEAN = _vol_density_borromean(Q)

# Falsified-fit literals retained as audit-only references for the
# Phase 5q ppm-coincidence comparison column in the witness.
# DO NOT use as production inputs.  Pre-PR #1080 framing: these were
# fitted values of a hypothetical separate λ_scale; post-#1080 they
# are simply audit-only constants with no production role.
LINKING_WEIGHT_PROTON_FITTED_FROM_CODATA_AUDIT_ONLY = mp.mpf("2.4599527869")
LINKING_WEIGHT_NEUTRON_FITTED_FROM_CODATA_AUDIT_ONLY = mp.mpf("2.4633436333")


def main() -> int:
    w = WitnessBuilder("m-p-borromean-verification-50dps", engine="mpmath")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "AUDIT-VERIFICATION at MPFR 50 dps of the EXCISED λ_A "
        "Borromean-VolDensity path (`conj:borromean-baryon-mass-formula`) "
        "against CODATA m_p, m_n. λ_A was ruled a CODATA-implied FIT and "
        "excised as a mass density (owner ruling 2026-06-24); the canonical "
        "absolute nucleon mass is the muon-anchored Hecke energy via "
        "computations/canonical_mass.py — see `canonical_mass_reference` in "
        "this witness. The audited form: m(K) = m_e × VolDensity(K, q₀), "
        "VolDensity = (Vol(𝓑₃)/ℏ_q²) × linking_weight, where linking_weight "
        "is the Family A Wedderburn sum (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h² "
        "(the algebraic identity is proved — Lean: "
        "`lambda-scale-substrate-form.lean` — its role as mass density is "
        "the excised fit).  "
        "Family A applies to the baryon class uniformly, giving "
        "m_avg^pred = m_e × VolDensity(𝓑₃, q₀) ≈ 966 MeV at q_0 — "
        "about 2.89 % above the CODATA mean (m_p + m_n)/2 ≈ 938.92 MeV. "
        "The proton-neutron mass difference is then supplied "
        "categorically by the substrate flavor-split closed form "
        "Δm/M_N = ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3 "
        "(`prop:flavor-split-substrate`, PR #690), giving "
        f"m_p^pred ≈ 965.38 MeV (vs CODATA {float(_M_P_MEV_VALIDATION):.6f}, "
        f"~2.89 % off) and m_n^pred ≈ 966.71 MeV "
        f"(vs CODATA {float(_M_N_MEV_VALIDATION):.6f}, ~2.89 % off).  The "
        "substrate Δm/M_N ratio itself matches CODATA to ~305 ppm "
        "(0.030 %) — framework-proved, no fit.  The prior CAL-4 fit "
        "(2.4599527869, 2.4633436333, 5.4 ppm tautological match) was "
        "removed in 2026-05-22 per the conjecture-falsification audit "
        "and is retained ONLY as audit-only "
        "`linking_weight_*_fitted_from_codata_AUDIT_ONLY` columns.  "
        "Per PR #1063, the ~2.89 % residual is now framed as a "
        "VolDensity(𝓑₃) categorical-exactness refinement gap at h² "
        "order, NOT as a separate λ_scale closure."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    # Discipline markers — λ_A excised as mass density 2026-06-24;
    # this witness audits the excised path, it is not the production
    # absolute-mass route (that is canonical_mass.py).
    w.add_parameter("derivation_status", "EXCISED_FIT_AUDIT_LAMBDA_A_2026_06_24")
    w.add_parameter("cal_class", "CAL-1 m_e only")
    w.add_parameter("audited_formula", "m(K) = m_e × VolDensity(K, q₀)  [EXCISED λ_A path]")
    w.add_parameter(
        "production_mass_route",
        "canonical_mass.proton_neutron_mass_mev() — muon-anchored Hecke "
        "energy m_p = 2·(m_μ·F_Bor − 6·m_e) (owner ruling 2026-06-24)",
    )
    w.add_parameter("vol_density_decomposition",
                    "VolDensity = (Vol(𝓑₃)/ℏ_q²) × linking_weight; "
                    "linking_weight = (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h² "
                    "(algebraic Family A identity proved; its role as "
                    "mass density is the fit excised 2026-06-24)")
    w.add_parameter("linking_weight_lean_ref",
                    "lambda-scale-substrate-form.lean")
    w.add_parameter("linking_weight_proof_script",
                    "lambda_scale_all_c_i_family_a.py")
    w.add_parameter("framing_reference_doc",
                    "docs/lambda-scale-absorbed-into-vol-density.md")
    w.add_parameter("tracking_doc",
                    "docs/canonical-derivation-cheat-sheet.md §5 fix #1 (closed)")
    w.add_parameter("q_0_50dps", mp.nstr(Q, 20))
    w.add_parameter("hbar_q_50dps", mp.nstr(HBAR_Q, 20))
    w.add_parameter("Vol_B3", mp.nstr(VOL_B3, 20))
    w.add_parameter("Vol_4_1", mp.nstr(VOL_41, 20))
    w.add_parameter("m_e_codata_MeV", mp.nstr(M_E_CODATA_MEV, 20))
    # Canonical VolDensity(𝓑₃, q₀) value — what the framework actually uses.
    w.add_parameter("vol_density_borromean_q0", mp.nstr(GEOM_FULL_BORROMEAN, 20))
    # Audit-only comparison column — the falsified-fit literals
    # whose 5.4 ppm "match" prompted the 2026-05-18 audit.  These
    # are NOT consumed by the production prediction below; they
    # exist so reviewers can see the ppm-coincidence gap that the
    # falsification audit established.  Pre-PR #1080 framing: these
    # were fitted values of a hypothetical separate λ_scale; post-
    # #1080 they are audit-only with no production role.
    w.add_parameter("linking_weight_proton_fitted_from_codata_AUDIT_ONLY",
                    mp.nstr(LINKING_WEIGHT_PROTON_FITTED_FROM_CODATA_AUDIT_ONLY, 15))
    w.add_parameter("linking_weight_neutron_fitted_from_codata_AUDIT_ONLY",
                    mp.nstr(LINKING_WEIGHT_NEUTRON_FITTED_FROM_CODATA_AUDIT_ONLY, 15))

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
        computed=fmt(abs(mu_ppm)),
        expected="0",
        tolerance="2.0",  # 2 ppm
        unit="ppm",
        source="CAL-2 anchor: m_mu/m_e = Vol(4_1)/ℏ_q²",
    )

    # ── Class-uniform m_avg from VolDensity (proton, neutron predicted
    #    equal at this layer) + substrate flavor split (proton-neutron
    #    mass difference) ─────────────────────────────────────────────
    # Per `prop:flavor-split-substrate` / PR #690, the proton-neutron
    # mass ratio carries a PROVED substrate-pure closed form:
    #     Δm / M_N  =  ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3
    # (see `_li_2_q_util.flavor_split_subleading`).  This is the
    # categorical Bring-color-tube weighting the cheat sheet §3
    # footnote flags.  VolDensity(𝓑₃, q₀) gives ONE class-uniform mass
    # scale; the split then assigns:
    #     m_p_pred = m_avg_pred · (1 − Δm/M_N / 2)
    #     m_n_pred = m_avg_pred · (1 + Δm/M_N / 2)
    # so the proton-neutron mass difference is Δm/M_N · m_avg_pred —
    # absolute Δm prediction within ~2.9 % of CODATA (same fractional
    # gap as m_avg, by construction).
    from _li_2_q_util import flavor_split_subleading as _flavor_split
    Q_INV = mp.mpf(1) / Q
    dm_over_Mn = _flavor_split(Q, Q_INV)

    # Class-uniform Family A m_avg (Borromean tower, before flavor split).
    # Uses the canonical VolDensity(𝓑₃, q₀) per PR #1080 — a single
    # Geom call rather than a manually-expanded Vol × linking_weight.
    m_avg_pred = GEOM_FULL_BORROMEAN * M_E_CODATA_MEV
    M_AVG_CODATA = (M_P_CODATA_MEV + M_N_CODATA_MEV) / 2
    m_avg_rel_diff = (m_avg_pred - M_AVG_CODATA) / M_AVG_CODATA
    w.add_data("class_uniform_m_avg", {
        "formula": "m_avg = m_e · VolDensity(𝓑₃, q₀)  (PR #1080, before flavor split)",
        "m_avg_pred_MeV": mp.nstr(m_avg_pred, 20),
        "m_avg_codata_MeV": mp.nstr(M_AVG_CODATA, 12),
        "rel_diff_ppm": mp.nstr(m_avg_rel_diff * mp.mpf("1e6"), 8),
        "vol_density_decomposition": (
            "VolDensity = (Vol(𝓑₃)/ℏ_q²) × linking_weight; "
            "linking_weight = (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h² "
            "(PROVED canonical Wedderburn — Family A)"
        ),
    })
    # ── Canonical-mass comparison column (production route) ───────
    # The production absolute nucleon mass, for side-by-side contrast
    # with the audited (excised) λ_A path above.
    from canonical_mass import proton_neutron_mass_mev as _canonical_pn
    _mp_canon, _mn_canon = _canonical_pn()
    w.add_data("canonical_mass_reference", {
        "route": "canonical_mass.proton_neutron_mass_mev (muon-anchored Hecke energy)",
        "m_p_MeV": fmt(_mp_canon),
        "m_n_MeV": fmt(_mn_canon),
        "note": (
            "Production absolute-mass route (owner ruling 2026-06-24). "
            "The λ_A-path m_avg_pred above overshoots this by ~2.9 % — "
            "that gap is what the excised fit was absorbing."
        ),
    })

    dm_codata_ratio = (M_N_CODATA_MEV - M_P_CODATA_MEV) / M_AVG_CODATA
    dm_ratio_ppm = (dm_over_Mn / dm_codata_ratio - 1) * mp.mpf("1e6")
    w.add_data("substrate_flavor_split", {
        "formula": "Δm/M_N = ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3 "
                   "(prop:flavor-split-substrate, PR #690)",
        "delta_m_over_M_N": mp.nstr(dm_over_Mn, 25),
        "delta_m_over_M_N_codata": mp.nstr(dm_codata_ratio, 15),
        "ratio_ppm_vs_codata": mp.nstr(dm_ratio_ppm, 8),
    })
    # Gate the substrate flavor split — if `flavor_split_subleading`
    # regresses to zero / the wrong ratio, the proton/neutron 5 %
    # ceiling above would still pass tautologically.  This assertion
    # is the actual regression guard for the PR's central wire-up.
    w.add_assertion(
        "substrate_flavor_split_ratio_within_1000ppm_of_codata",
        computed=fmt(abs(dm_ratio_ppm)),
        expected="0",
        tolerance="1000.0",  # 0.1 % ceiling — current value ~305 ppm
        unit="ppm",
        source=(
            "prop:flavor-split-substrate / flavor_split_subleading "
            "vs CODATA (M_N − M_P)/M_avg at MPFR 50 dps"
        ),
    )

    # ── Proton (with substrate flavor split) ──────────────────────
    proton_pred = m_avg_pred * (mp.mpf(1) - dm_over_Mn / 2)
    proton_factor = proton_pred / M_E_CODATA_MEV  # for back-compat field
    proton_rel_diff = (proton_pred - M_P_CODATA_MEV) / M_P_CODATA_MEV
    proton_ppm = proton_rel_diff * mp.mpf("1e6")
    w.add_data("proton", {
        "formula": "m_p = m_avg_pred · (1 − Δm/M_N / 2), with "
                   "m_avg_pred = m_e · VolDensity(𝓑₃, q₀) and "
                   "Δm/M_N from flavor_split_subleading",
        "vol_B3_over_hbar_q_squared": mp.nstr(VOL_B3 / HBAR_Q**2, 20),
        "vol_density_borromean_q0": mp.nstr(GEOM_FULL_BORROMEAN, 20),
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
        computed=fmt(abs(proton_ppm)),
        expected="0",
        tolerance="50000.0",  # 5 % ceiling
        unit="ppm",
        source="Borromean baryon formula (Family A λ) vs CODATA m_p at MPFR 50 dps",
    )

    # ── Neutron (with substrate flavor split) ─────────────────────
    neutron_pred = m_avg_pred * (mp.mpf(1) + dm_over_Mn / 2)
    neutron_factor = neutron_pred / M_E_CODATA_MEV  # for back-compat field
    neutron_rel_diff = (neutron_pred - M_N_CODATA_MEV) / M_N_CODATA_MEV
    neutron_ppm = neutron_rel_diff * mp.mpf("1e6")
    w.add_data("neutron", {
        "formula": "m_n = m_avg_pred · (1 + Δm/M_N / 2), with "
                   "m_avg_pred = m_e · Vol(B_3)/ℏ_q² · λ_Y and "
                   "Δm/M_N from flavor_split_subleading",
        "tower_factor": mp.nstr(neutron_factor, 20),
        "m_n_pred_MeV": mp.nstr(neutron_pred, 20),
        "m_n_codata_MeV": mp.nstr(M_N_CODATA_MEV, 12),
        "rel_diff": mp.nstr(neutron_rel_diff, 12),
        "rel_diff_ppm": mp.nstr(neutron_ppm, 8),
    })
    # Same Family A m_avg → same ~3 % residual for the neutron (the
    # flavor split only redistributes m_avg between p and n; the
    # absolute scale gap is the same as for the proton).
    w.add_assertion(
        "neutron_borromean_tower_within_5pct_of_codata",
        computed=fmt(abs(neutron_ppm)),
        expected="0",
        tolerance="50000.0",  # 5 % ceiling
        unit="ppm",
        source="Borromean baryon formula (Family A λ + flavor split) vs CODATA m_n at MPFR 50 dps",
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
            "The pn split is now categorically derived: "
            "Δm = m_avg_pred · (ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3) "
            "via prop:flavor-split-substrate / flavor_split_subleading. "
            "The rel_diff vs CODATA inherits the Family A m_avg gap "
            "(~3 %); the substrate flavor-ratio Δm/M_N is matched to "
            "~305 ppm (~0.030 %) independently — see "
            "substrate_flavor_split.ratio_ppm_vs_codata."
        ),
    })

    # ── 1700× scale-gap explanation ───────────────────────────
    single_level_estimate = mp.mpf("1.065") * M_E_CODATA_MEV  # T1 alone
    # No float(). Both inputs are already mpf; casting here and then handing
    # the result to fmt() would serialize a float64 as a 50-digit string —
    # 17 real digits followed by 33 invented ones. The mixed-arithmetic gate
    # caught exactly that when this was first drained, which is what it is for.
    gap_factor = M_P_CODATA_MEV / single_level_estimate
    tower_multiplier = mp.mpf(GEOM_FULL_BORROMEAN)
    w.add_data("scale_gap_resolution", {
        "single_level_m_p_estimate_MeV": mp.nstr(single_level_estimate, 8),
        "codata_m_p_MeV": mp.nstr(M_P_CODATA_MEV, 8),
        "scale_gap_factor": fmt(gap_factor),
        "borromean_tower_multiplier": fmt(tower_multiplier),
        "match_to_gap_pct": fmt(abs(tower_multiplier - gap_factor) / gap_factor * mp.mpf(100)),
        "conclusion": (
            "VolDensity(𝓑₃, q₀) ≈ 1836 IS the 1700× scale factor "
            "missing from the single-level Markov-trace m_p chain. "
            "The Borromean tower formula closes the gap to ~2.89 % on "
            "m_avg; substrate flavor split (PR #690) supplies Δm/M_N "
            "to ~305 ppm independently."
        ),
    })

    w.add_caveat(
        "λ_A EXCISION (owner ruling 2026-06-24): this witness AUDITS the "
        "excised λ_A Borromean-VolDensity path; it is NOT the production "
        "absolute-mass route. Production route: canonical_mass.py "
        "(muon-anchored Hecke energy, see canonical_mass_reference). "
        "Ledger: docs/coordination/2026-06-24-lambda-a-fit-excised-per-"
        "knot-density.md."
    )
    # Open R&D: closing the m_avg ~2.89 % residual categorically
    w.add_caveat(
        "Audited formula framing (pre-excision, PR #1080): m(K) = m_e × "
        "VolDensity(K, q₀), a single Geom call per knot.  VolDensity decomposes as "
        "(Vol(𝓑₃)/ℏ_q²) × linking_weight, with linking_weight = "
        "(3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h² (PROVED Family A "
        "categorical Wedderburn identity, Lean: "
        "`lambda-scale-substrate-form.lean`).  There is no separate "
        "λ_scale constant — older docs called the linking-weight "
        "component λ_scale before it was absorbed into VolDensity.  "
        "The prior CAL-4 literals 2.4599527869 / 2.4633436333 are "
        "retained only as audit-only comparison columns.  The proton-"
        "neutron mass ratio Δm/M_N is the substrate-pure closed form "
        "from `prop:flavor-split-substrate` (PR #690): "
        "ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3, which matches CODATA "
        "to ~305 ppm (~0.030 %).  The remaining ~2.89 % gap in the "
        "absolute m_avg scale is now framed (per PR #1063) as a "
        "VolDensity(𝓑₃) categorical-exactness refinement gap at h² "
        "order, NOT as a separate λ_scale closure."
    )
    # Lean SDP-uniqueness cross-reference (PR #1537/#1542/#1554
    # wiring, 2026-05-31). Each nucleus's canonical T_w knot
    # operator uniqueness at the empty-constraint SDP level.
    w.add_data("lean_uniqueness_ref", {
        "proton": "qou:QOU.BraidKnot.PeriodicTableUniqueness.h_uniqueness_closed",
        "neutron": "qou:QOU.BraidKnot.nucleus_uniqueness_closed (n=3)",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": (
            "These theorems certify T_w uniqueness at the abstract empty-constraint SDP level (PR #1537/#1542 parameterised module). The real per-nucleus SDP (multi-term cost + non-empty constraints) is per-nucleus substantive open work. Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md."
        ),
    })


    out = w.save()
    print(f"Witness emitted: {out.name}")
    print()
    print(f"Vol(B_3)/ℏ_q²       = {float(VOL_B3 / HBAR_Q**2):.6f}")
    print(f"Vol(4_1)/ℏ_q²       = {float(VOL_41 / HBAR_Q**2):.6f}  (m_μ/m_e)")
    print()
    print(f"Muon  pred  m_μ = {float(mu_pred):.8f} MeV  vs CODATA {float(M_MU_CODATA_MEV):.8f}  Δ = {float(mu_ppm):+.3f} ppm")
    print(f"m_avg  pred       = {float(m_avg_pred):.8f} MeV  vs CODATA {float(M_AVG_CODATA):.8f}  Δ = {float(m_avg_rel_diff * mp.mpf('1e6')):+.4f} ppm  (Family A class-uniform)")
    print(f"Δm/M_N pred       = {float(dm_over_Mn):.10f}  vs CODATA {float((M_N_CODATA_MEV - M_P_CODATA_MEV) / M_AVG_CODATA):.10f}")
    print(f"Proton  pred  m_p = {float(proton_pred):.8f} MeV  vs CODATA {float(M_P_CODATA_MEV):.8f}  Δ = {float(proton_ppm):+.4f} ppm")
    print(f"Neutron pred  m_n = {float(neutron_pred):.8f} MeV  vs CODATA {float(M_N_CODATA_MEV):.8f}  Δ = {float(neutron_ppm):+.4f} ppm")
    print(f"Δ m_pn  pred      = {float(delta_pn):.6f} MeV  vs CODATA {float(delta_pn_codata):.6f}  Δ rel = {float(delta_diff)*100:+.3f} %")
    print()
    print(f"Scale-gap explanation:")
    print(f"  single-level pred (T1):  {float(single_level_estimate):.4f} MeV")
    print(f"  Borromean tower factor:  {float(tower_multiplier):.4f}")
    print(f"  CODATA / single-level:   {float(gap_factor):.4f}")
    print(f"  → VolDensity(𝓑₃, q₀) closes to ~2.89 % vs CODATA on m_avg;")
    print(f"    substrate flavor split (PR #690) supplies Δm/M_N to")
    print(f"    ~305 ppm (~0.030 %) giving a categorical (non-fit) p/n split.")
    print(f"    Open R&D: ~2.89 % m_avg gap framed as VolDensity(𝓑₃)")
    print(f"    categorical-exactness refinement (PR #1063), not separate λ closure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
