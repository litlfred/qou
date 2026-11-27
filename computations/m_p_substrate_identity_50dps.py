#!/usr/bin/env python3
"""
m_p_substrate_identity_50dps.py — production-grade substrate-categorical
prediction of m_p and m_n from (m_e, m_μ, q_0) at MPFR 50 dps.

## The substrate identity

   m_p = 2 · m_μ · |tr_M(β_Bor, q_0)| · [3]_q! / q_0^3  −  12 · m_e

   m_n = m_p + Q_β + m_e   with Q_β the SCORED owner-ruled D1 = A cell
                           |ε_flavour(V³)|·E₀ (derived_masses.q_beta_scored_mev;
                           −486 ppm on m_n, conditional on conjectures C1–C3).
                           Switched 2026-11-21 (owner decision, issue #8769) from
                           the retired z = 1 mixed base q_beta_kashiwara_n2_mev
                           (+501 ppb), which is kept below as a labelled diagnostic.
                           The flavor-split X = (q-1)²(1 - q^{-4})/3 is retained
                           as a SECONDARY diagnostic ratio (−1.76 ppm), not the route.

Both Lean-proved closed forms underlie the formula:

   |tr_M(β_Bor, q)| = (4 + h² - 3h⁴ - h⁶) / (h² + 4)
                                       ← BorromeanMarkovTrace.lean

   [3]_q! = (q² + 1 + q⁻²)(q + q⁻¹)
                                       ← YLambdaQSchur.lean (this PR)

   X = (q-1)²(1 - q^{-4})/3 = ℏ_q² · h · [2]_q / 3
                                       ← prop:flavor-split-substrate
                                         (canonical Hecke-skein derivation)

## Calibration content

INPUTS: m_e (CAL-1), m_μ (CAL-2 via m_μ/m_e), q_0 (substrate)

(NB: m_μ/m_e and q_0 are EQUIVALENT for calibration purposes — they
satisfy the muon-anchor identity m_μ/m_e = Vol(4_1)/ℏ_q²(q_0). The
QOU 3-calibration discipline lists them as CAL-2 interchangeably.)

CAL-3 (Q_β) is NOT used for nucleon masses. Q_β = m_n - m_p - m_e
is now a DERIVED quantity from this substrate identity, not a
calibration input.

## Structural identifications

- "2"  = dim V_{(2,1)} — classical dimension of the standard irrep
        of S_3 (trace-dominant per Wedderburn diagnostic at 49% of T1).
        Lean-proved via hook-length formula in DimStandardRepS3.lean.
- "12" = dim V_{(2,1)} · 3! = 2 · 6. Formula factors as:
          m_p = dim V_{(2,1)} · (m_μ · F_Bor − |S_3| · m_e)
        where |S_3| = 3! = 6 = P_3(q²)|_{q=1} (Poincaré classical limit
        of [3]_q!). Both factors are categorical invariants of H_3(q).
- "F_Bor(q)" = |tr_M(β_Bor, q)| · [3]_q! / q^3 — the natural
        categorical observable combining the Borromean Markov trace
        with the q-factorial normalisation, shifted by content q^3.

## Empirical performance

At q_0 = 1.1099785955573347... (50 dps, m_p-pinned re-pin #1422):
  m_p_pred  = 938.27209 MeV   vs CODATA 938.27209  →  0.0004 ppb  (ANCHOR
                                          round-trip, not a prediction)
  m_μ_pred  = 105.65840 MeV   vs CODATA 105.65838  →  +0.21 ppm   (9.5σ
                                          PREDICTION — the μ-p tension)
  m_n_pred  = 939.10852 MeV   vs CODATA 939.56542  →  −486 ppm   (n→p+e+ν̄  # noqa: P31 — docstring; prediction-vs-CODATA table
                                          chain; scored D1 = A Q_β, C1–C3 conditional)
  Q_β_pred  = 0.32543 MeV     vs CODATA 0.78233    →  −58.4 % on Q_β  # noqa: P31 — docstring; prediction-vs-CODATA table
                                          (retired mixed base gave 0.78280 MeV,
                                          +602 ppm; kept as a diagnostic only)

Class-A acknowledged-anchor banner (per Workplan-0b): m_e, m_μ are
CAL-1/CAL-2 anchors (CODATA inputs). q_0 is the substrate parameter
(currently calibrated, derivation re-opened per PR #1249). The
predicted m_p, m_n, Q_β are DERIVED outputs.

## Status

Substrate identity at 0.24 ppm. Structural status:
1. "2" = dim V_(2,1) — Lean-proved (DimStandardRepS3.lean)
2. "12" = dim V_(2,1) · 3! = 2·6 — identified (formula factors cleanly)
3. F_Bor identification as natural categorical observable — open

Refs:
- BorromeanMarkovTrace.lean (|tr_M| closed form)
- YLambdaQSchur.lean (this PR — [3]_q! and y_λ closed forms)
- prop:flavor-split-substrate (canonical Hecke-skein flavor split)
- 2026-05-04-ocneanu-cancellation-numerical-verification.md (the −1/12)
- 2026-05-25-proton-mass-identity-12-me-ocneanu.md (this audit)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

COMPUTE_DIR = Path(__file__).resolve().parent

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
    M_MU_MEV_VALIDATION,
)
from derived_masses import q_beta_kashiwara_n2_mev, q_beta_scored_mev  # noqa: E402


def q_int(q, n):
    """Balanced q-integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def qfact_three(q):
    """[3]_q! = [3]_q · [2]_q · [1]_q (Lean-proved closed form)."""
    return q_int(q, 3) * q_int(q, 2) * q_int(q, 1)


def trM_borromean(q):
    """|tr_M(β_Bor, q)| from BorromeanMarkovTrace.lean closed form:

        tr_M(β_Bor, q) = (4 + h² - 3h⁴ - h⁶) / (h² + 4)

    where h = q - q⁻¹ (Lean-proved: BorromeanMarkovTrace.lean). Trace
    CONVENTION: this is the SU(2)/Temperley-Lieb (Jones) decomposition
    — convention D in the trace-convention registry — NOT the Wenzl
    z-trace (convention C differs exactly; gap 1.955e-4 at q0; see
    docs/audits/2026-06-09-binding-trace-convention-split.md addendum,
    probe_convention_d_vs_c_borromean.py (the D != C proof), and
    probe_trace_convention_production_impact.py (production impact).

    WHY D AND NOT C — the forcing argument, and its unmet premise
    (bean qou-3qrv; docs/audits/2026-08-08-borromean-trace-convention-
    forcing.md). This function previously asserted the convention with
    no justification for the selection. The justification has two links;
    the first is proved, the second is NOT.

    FORCED, GIVEN TEMPERLEY-LIEB. A normalised Markov trace on H_3(q) is
    determined by (tr 1, tr s0, tr s0s1) = (1, z, z^2), so its Wedderburn
    weights are a 3x3 linear solve in the Ocneanu parameter z. The TL
    condition y_(1^3)(z) = 0 has exactly two roots: z = q, which is
    degenerate (weights (1,0,0) — it annihilates the 2-row block too, so
    it is not faithful on TL_3), and z = q^3/(q^2+1), whose weight vector
    is exactly ([4]_q/[2]_q^3, 1/[2]_q^2, 0) = convention D. So D is the
    UNIQUE Markov trace that factors through TL_3 and is faithful on it —
    no residual freedom, and no experimental input anywhere in the chain.
    Sorry-free in QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean
    (markovWeights_eq_jones_of_threeRow_eq_zero); computed in
    computations/probe3qrv_zpin.py.

    PREMISE ESTABLISHED 2026-08-08 — THIS NOTE WAS STALE ON BOTH COUNTS.
    It read "PREMISE NOT ESTABLISHED", on two claims that have each since
    been settled in the opposite direction:

      1. "conditional on the mass fibre functor landing in Rep(SU_q(2))
         ~ TL". That link is now PROVED, sorry-free, in
         QOU/BraidsAndKnots/FibreDimensionForcesTL.lean: the mass fibre
         is 2-dimensional, which fixes the Ocneanu parameter and forces
         y_(1^3) = 0. Bean qou-n1dj. With the uniqueness theorem above
         (TL => D), the chain is complete and D is DERIVED.
      2. "currently CONTRADICTED in the corpus ... states that the mass
         and binding computations use ... convention C". That scope note
         has itself been corrected: mass-theory/h3-markov-wenzl-weights-
         context.md now records convention D for BOTH channels, since the
         owner ruling of 2026-08-09 excised convention C, and flags its
         own earlier version as wrong.

    This is the THIRD instance of one staleness pattern — a "what this
    does NOT establish" note outliving the file that establishes it. The
    same note was corrected in MarkovTraceTLUniqueness.lean (PR #6144);
    this copy was missed there and is corrected here.

    WHAT IS *NOT* WEAKENED. Do not "resolve" a convention question by
    observing which value matches CODATA — deciding by match is the
    failure mode bean qou-3qrv was opened to test for, and that
    discipline is independent of the premise being settled.

    🛑 THIS FUNCTION CANNOT BE USED TO *MEASURE* THE CAP. The closed form
    below is in h alone and carries NO z parameter: convention D was
    substituted before it was written down, so y_(1^3) = 0 is baked in
    rather than passed in. Any joint solve that tries to recover y_(1^3)
    from (Q_beta, m_p) via F_Bor -> canonical_mass therefore measures its
    own assumption. The cap IS jointly observable in principle — the mass
    channel sees y_3 + y_(1^3) where decay sees y_3 - y_(1^3), and the
    two together have nonzero determinant — but that cross-check needs a
    mass pairing that does not already presuppose the convention, and
    this route is not one. Bean qou-cds1.
    """
    h = q - 1 / q
    return abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))


def F_Bor(q):
    """The natural categorical observable F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q^3."""
    return trM_borromean(q) * qfact_three(q) / q ** 3


#: Habiro 4-loop coefficient — FIT-TIER, RETAINED-BUT-NOT-APPLIED
#  (owner ruling 2026-07-03 "drop" + PR #3280 option 1; bean `2i8g`
#  reconcile CLOSED as drop): the exact c₄ needed is linear in the q₀
#  pin offset (c₄ ≈ 46 is the muon-calibration convention, the μ–p
#  tension reparametrized), `4143` has no derivation trail in the corpus,
#  and the fitted tower was STRIPPED from the pin (`q_at`) — the raw
#  proton pin is canonical. This constant + `habiro_ratio_s5bb` are kept
#  as the documented record of the fitted dressing, but are NO LONGER
#  applied to production m_p (they over-added +242 ppb at the proton
#  pin). See docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md.
with mp.workdps(70):
    C4_S5BB = +(mpf("4143") / mpf("90"))


def habiro_ratio_s5bb(q, c4=None):
    """Habiro 4-loop dressing (1 + c₄u⁴)(1 + 4u⁵)(1 − 29u⁶) with
    u = b·ℏ_q², b = √((q⁴+q²+1)/(q²+1)²). FIT-TIER (see C4_S5BB note):
    NOT part of the raw proton pin and NO LONGER applied to production m_p
    (owner ruling drop, #3280). Kept as the documented record of the
    fitted dressing; callers must not multiply it into a production mass."""
    c4 = C4_S5BB if c4 is None else c4
    hbar_q_sq = ((q - 1) / q) ** 2
    b_val = ((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2) ** mpf("0.5")
    u = b_val * hbar_q_sq
    return (1 + c4 * u ** 4) * (1 + 4 * u ** 5) * (1 - 29 * u ** 6)


def flavor_split_X(q):
    """Δm/M_N substrate prediction from prop:flavor-split-substrate:

        X = (q-1)² (1 - q^-4) / 3 = ℏ_q² · h · [2]_q / 3

    Canonically derived (not fit) — see content/observations/
    flavor-split-substrate.md for the derivation via Hecke skein
    relation on u↔d 2-strand sub-braid.
    """
    return (q - 1) ** 2 * (1 - q ** (-4)) / 3


def borromean_v3_connected_qed_traces(q: mpf) -> dict[str, mpf]:
    """Exact 3-strand weight-space Borromean V³ = (σ₁σ₂⁻¹)³ traces and connected
    4th-order QED self-energy / isospin-splitting traces at substrate parameter q.

    Backed by sorry-free Lean 4 theorems in
    `QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean` (Sections 6 & 7):
      - `trace_borromeanV3A` / `trace_borromeanV3B`:
          tr(V³) = -(q¹² - 3q¹⁰ + 3q⁸ - 5q⁶ + 3q⁴ - 3q² + 1) / q⁶
      - `trace_e3p_borromeanV3` / `trace_e3n_borromeanV3`:
          tr(e_{(3)} V³) = 1
      - `trace_e21p_borromeanV3` / `trace_e21n_borromeanV3`:
          tr(e_{(2,1)} V³) = -(q⁴ - q² + 1)(q⁸ - 2q⁶ - 2q² + 1) / q⁶ = tr(V³) - 1
      - `trace_QAdjp_borromeanV3` (per-strand connected, /3):
          tr_bar_conn(p, V³) = -2(q² - 1)⁴(q⁴ + q² + 1) / (27 q⁶)
      - `trace_QAdjn_borromeanV3_connected` (per-strand connected, /3):
          tr_bar_conn(n, V³) = +(q² - 1)⁴(2q⁴ - q² + 2) / (27 q⁶)
      - `trace_QAdj_connected_diff_borromeanV3` (per-strand connected difference, /3):
          Δtr_bar_conn(V³) = +(q² - 1)⁴(4q⁴ + q² + 4) / (27 q⁶)
      - `trace_e21p_QAdjp_borromeanV3`:
          tr(e_{(2,1)}^p (Q₁₂^(p) + Q₂₃^(p)) V_p³) = -2(q² - 1)²(q¹² - q⁶ + 1) / (9 q⁶ (q⁴ + q² + 1))
      - `trace_e21n_QAdjn_borromeanV3`:
          tr(e_{(2,1)}^n (Q₁₂^(n) + Q₂₃^(n)) V_n³) = (4q¹⁶ - 11q¹⁴ + 13q¹² - 22q¹⁰ + 20q⁸ - 22q⁶ + 13q⁴ - 11q² + 4) / (9 q⁶ (q⁴ + q² + 1))
      - `trace_e21_QAdj_diff_borromeanV3`:
          Δtr_{e_{(2,1)}}(Q_adj V³) = (2q¹⁶ - 5q¹⁴ + 5q¹² - 8q¹⁰ + 8q⁸ - 8q⁶ + 5q⁴ - 5q² + 2) / (3 q⁶ (q⁴ + q² + 1))
    """
    q2 = q ** 2
    q6 = q2 ** 3
    q4_q2_1 = q2 ** 2 + q2 + 1

    tr_V3 = -(q2 ** 6 - 3 * (q2 ** 5) + 3 * (q2 ** 4) - 5 * (q2 ** 3) + 3 * (q2 ** 2) - 3 * q2 + 1) / q6
    tr_e3_V3 = mpf(1)
    tr_e21_V3 = -(q2 ** 2 - q2 + 1) * (q2 ** 4 - 2 * (q2 ** 3) - 2 * q2 + 1) / q6

    q2m1_4 = (q2 - 1) ** 4
    tr_conn_p = -2 * q2m1_4 * q4_q2_1 / (27 * q6)
    tr_conn_n = q2m1_4 * (2 * (q2 ** 2) - q2 + 2) / (27 * q6)
    tr_conn_diff = q2m1_4 * (4 * (q2 ** 2) + q2 + 4) / (27 * q6)

    denom_e21 = q6 * q4_q2_1
    tr_e21_QAdjp = -2 * ((q2 - 1) ** 2) * (q2 ** 6 - q2 ** 3 + 1) / (9 * denom_e21)
    tr_e21_QAdjn = (
        4 * (q2 ** 8) - 11 * (q2 ** 7) + 13 * (q2 ** 6) - 22 * (q2 ** 5)
        + 20 * (q2 ** 4) - 22 * (q2 ** 3) + 13 * (q2 ** 2) - 11 * q2 + 4
    ) / (9 * denom_e21)
    tr_e21_QAdj_diff = (
        2 * (q2 ** 8) - 5 * (q2 ** 7) + 5 * (q2 ** 6) - 8 * (q2 ** 5)
        + 8 * (q2 ** 4) - 8 * (q2 ** 3) + 5 * (q2 ** 2) - 5 * q2 + 2
    ) / (3 * denom_e21)

    return {
        "tr_V3": tr_V3,
        "tr_e3_V3": tr_e3_V3,
        "tr_e21_V3": tr_e21_V3,
        "tr_conn_p": tr_conn_p,
        "tr_conn_n": tr_conn_n,
        "tr_conn_diff": tr_conn_diff,
        "tr_e21_QAdjp": tr_e21_QAdjp,
        "tr_e21_QAdjn": tr_e21_QAdjn,
        "tr_e21_QAdj_diff": tr_e21_QAdj_diff,
    }


def main():
    set_compute_dps()

    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf(M_E_MEV)
    # q₀ is pinned from m_p/m_e (2026-05-29), so m_p must be a PURE-q
    # function: substitute the muon-anchor formula m_μ = m_e·Vol(4₁)/ℏ_q²
    # for m_μ here (instead of the measured value). At the m_p-pinned q₀
    # this matches m_p to CODATA to the 50-digit-q₀ precision (≈0.0004 ppb
    # residual — a calibration match, NOT math-exact); the measured m_μ is
    # now a PREDICTION (≈9.5σ, the μ-p tension).
    # See observations/substrate-anchor-alternatives.md.
    from q_parameter import vol_4_1_at  # noqa: E402
    hbar_q_sq = ((q - 1) / q) ** 2
    m_mu = m_e * vol_4_1_at(50) / hbar_q_sq          # muon FORMULA (pure-q)
    m_mu_measured = mpf(M_MU_MEV_VALIDATION)         # CODATA — 9.5σ cross-check (registry)
    m_mu_over_m_e = m_mu / m_e

    # ── PREDICTIONS ────────────────────────────────────────────────
    F = F_Bor(q)
    # m_p = 2·m_μ·F_Bor − 12·m_e — the exact N=0 substrate formula.
    #
    # The fitted Habiro precision tower (`habiro_ratio_s5bb`, module-level
    # FIT-TIER helper) is DEFINED but NO LONGER APPLIED here (owner ruling
    # "drop", PR #3280 option 1; bean 2i8g reconcile). It closed the
    # −242 ppb formula→CODATA residual to sub-ppb, but at the current raw
    # proton pin the base already lands m_p at +1.35 ppb, so applying the
    # muon-era tower over-added +242 ppb (m_p → +243.8 ppb — a live
    # regression). The u⁴ coefficient is affine in the q₀ pin (≈0 at the
    # proton pin, 46 at the muon pin, slope 3.99/ppb): it measures the
    # muon↔proton calibration gap, not a derived constant; the old
    # `4143/90` "s5bb colour Reeb index" provenance cited a refuted route
    # (2026-06-16-s5so3-reeb-resonance-probe-negative). F_Bor is already the
    # exact Borromean Markov-trace (Habiro) evaluation, so no a_m tail is
    # added. Consistent with the 2026-07-03 owner ruling that stripped the
    # same tower from the q₀ solver + the 2026-05-28 floor audit rec #1.
    # Full analysis: docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md.
    m_p_pred = 2 * m_mu * F - 12 * m_e
    # Canonical neutron: n → p + e⁻ + ν̄, with Q_β the SCORED owner-ruled
    # D1 = A cell |ε_flavour(V³)|·E₀ (tower E₀, same q₀), derived_masses.
    # q_beta_scored_mev. Owner decision 2026-11-21 (issue #8769): the facade
    # follows the scorecard. NOT chosen by residual: it misses CODATA Q_β by
    # −58.4 % (m_n −486 ppm), further than the retired value below.
    # CONDITIONAL on conjectures C1–C3 (QOU.QBeta.DecayConjectures).
    Q_beta_pred = q_beta_scored_mev(q, m_e)
    # RETIRED MIXED BASE (owner label 2026-11-16): z = 1 Form A with a
    # convention-D phase. Its +501 ppb on m_n is not a convention-D result.
    # Kept only as a labelled diagnostic so the old figure stays reproducible.
    Q_beta_retired_mixed_base = q_beta_kashiwara_n2_mev()
    m_n_retired_mixed_base = m_p_pred + Q_beta_retired_mixed_base + m_e
    Delta_m_pred = Q_beta_pred + m_e                   # = m_n − m_p, computed directly
    m_n_pred = m_p_pred + Delta_m_pred                 # avoids large-number subtraction
    M_N_pred = (m_p_pred + m_n_pred) / 2
    # SECONDARY diagnostic — the canonical flavor-split RATIO
    # X = ℏ_q²·h·[2]_q/3 (prop:flavor-split-substrate); a derived u↔d
    # split (−1.76 ppm on m_n), NOT the production neutron route.
    X = flavor_split_X(q)
    m_n_flavor_split = m_p_pred * (1 + X / (1 - X / 2))
    Delta_m_flavor_split = m_n_flavor_split - m_p_pred

    # ── ROUND-TRIP CHECK (transparency — NOT a prediction) ────────
    # Feeding the EXPERIMENTAL Q_β (Q_AME = m_n−m_p−m_e from CODATA)
    # back through m_n = m_p + Q_AME + m_e recovers CODATA m_n BY
    # CONSTRUCTION — a circular consistency check, NOT a prediction
    # (reporting it as a prediction would violate the 3-input
    # over-count discipline). The canonical neutron above instead uses
    # the parameter-free Kashiwara b² Q_β.
    Q_beta_ame = None
    m_n_roundtrip = None
    try:
        qb_witness = record_upstream(COMPUTE_DIR / "q-beta-operator-valued-N3.witness.json", _UPSTREAM_RECORDS)
        qb_val = qb_witness.get("data", {}).get("Q_AME")
        if qb_val is not None:
            Q_beta_ame = mpf(str(qb_val))
            m_n_roundtrip = m_p_pred + Q_beta_ame + m_e
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        pass

    # ── CODATA TARGETS ─────────────────────────────────────────────
    m_p_codata = mpf(M_P_MEV_VALIDATION)
    m_n_codata = mpf(M_N_MEV_VALIDATION)
    M_N_codata = (m_p_codata + m_n_codata) / 2
    Q_beta_codata = m_n_codata - m_p_codata - m_e

    # ── RESIDUALS ──────────────────────────────────────────────────
    # m_μ is now a PREDICTION (q₀ pinned from m_p): m_μ_pred = m_e·Vol/ℏ_q²
    # vs CODATA m_mu_measured — the 9.5σ μ-p tension residual.
    res_m_mu_ppm = (m_mu - m_mu_measured) / m_mu_measured * mpf("1e6")
    res_m_p_ppm = (m_p_pred - m_p_codata) / m_p_codata * mpf("1e6")
    res_m_n_ppm = (m_n_pred - m_n_codata) / m_n_codata * mpf("1e6")
    res_M_N_ppm = (M_N_pred - M_N_codata) / M_N_codata * mpf("1e6")
    res_Q_beta_ppm = (Q_beta_pred - Q_beta_codata) / Q_beta_codata * mpf("1e6")

    # ── TWO-TERM BORROMEAN V³ QED DIAGNOSTICS (Tier A additive, qou-7ph7) ──
    # Backed by QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean (Sections 6 & 7).
    from q_parameter import (  # noqa: E402
        MASS_RATIO_MU_E_STR,
        MASS_RATIO_MU_E_ERR,
        q_muon_at,
        q_two_term_borromean_at,
    )
    bor_traces = borromean_v3_connected_qed_traces(q)
    tr_V3 = bor_traces["tr_V3"]
    tr_e3_V3 = bor_traces["tr_e3_V3"]
    tr_e21_V3 = bor_traces["tr_e21_V3"]
    tr_conn_p = bor_traces["tr_conn_p"]
    tr_conn_n = bor_traces["tr_conn_n"]
    tr_conn_diff = bor_traces["tr_conn_diff"]
    tr_e21_QAdjp = bor_traces["tr_e21_QAdjp"]
    tr_e21_QAdjn = bor_traces["tr_e21_QAdjn"]
    tr_e21_QAdj_diff = bor_traces["tr_e21_QAdj_diff"]

    # Weighting: DERIVED quantum trace Tr(K^{⊗3}·)/[2]_q³ (bean qou-99qc). The 1/3-normalised
    # entries below ('plain', 'Kp', 'KnKp') are kept as labelled historical comparisons.
    from two_term_qtrace_weighting import m_p_qed_conn_mev, delta_m_qed_conn_mev
    # Scored: covariant all-pairs (owner 2026-11-20 16:44) -> 0 on V³. Adjacent = option 1, labelled.
    M_p_QED_conn_scored_MeV = m_p_qed_conn_mev(q, m_e)
    Delta_m_QED_conn_scored_MeV = delta_m_qed_conn_mev(q, m_e)
    M_p_QED_conn_derived_MeV = m_p_qed_conn_mev(q, m_e, "derived", "adjacent")
    Delta_m_QED_conn_derived_MeV = delta_m_qed_conn_mev(q, m_e, "derived", "adjacent")
    M_p_QED_conn_MeV = m_e * abs(tr_conn_p)
    M_p_QED_conn_Kp_MeV = m_e * q * abs(tr_conn_p)
    Delta_m_QED_conn_MeV = -m_e * tr_conn_diff
    Delta_m_QED_conn_KnKp_MeV = -m_e * (tr_conn_n / q - q * tr_conn_p)
    Q_beta_two_term_plain_MeV = Q_beta_pred + Delta_m_QED_conn_MeV
    Q_beta_two_term_MeV = Q_beta_pred + Delta_m_QED_conn_scored_MeV
    Q_beta_two_term_derived_adjacent_MeV = Q_beta_pred + Delta_m_QED_conn_derived_MeV
    m_n_two_term_MeV = m_p_pred + Q_beta_two_term_MeV + m_e
    res_Q_beta_two_term_ppm = (Q_beta_two_term_MeV - Q_beta_codata) / Q_beta_codata * mpf("1e6")
    res_m_n_two_term_ppb = (m_n_two_term_MeV - m_n_codata) / m_n_codata * mpf("1e9")

    # Two-term proton pin & μ–p tension diagnostics
    vol50 = vol_4_1_at(50)
    q_muon_50 = q_muon_at(50)
    q_two_term_scored = q_two_term_borromean_at(50)
    q_two_term_derived = q_two_term_borromean_at(50, weighting="derived", insertion="adjacent")
    q_two_term_plain = q_two_term_borromean_at(50, weighting="plain")
    q_two_term_kwt = q_two_term_borromean_at(50, weighting="Kp")
    mmu_me_two_term_derived = vol_4_1_at(50) / (((q_two_term_derived - 1) / q_two_term_derived) ** 2)
    mmu_me_codata = mpf(MASS_RATIO_MU_E_STR)
    mmu_me_err = mpf(str(MASS_RATIO_MU_E_ERR))
    mmu_me_two_term_plain = vol50 / (((q_two_term_plain - 1) / q_two_term_plain) ** 2)
    mmu_me_two_term_kwt = vol50 / (((q_two_term_kwt - 1) / q_two_term_kwt) ** 2)
    mup_tension_two_term_plain_ppb = (mmu_me_two_term_plain - mmu_me_codata) / mmu_me_codata * mpf("1e9")
    mup_tension_two_term_plain_sigma = (mmu_me_two_term_plain - mmu_me_codata) / mmu_me_err
    mup_tension_two_term_kwt_ppb = (mmu_me_two_term_kwt - mmu_me_codata) / mmu_me_codata * mpf("1e9")
    mup_tension_two_term_kwt_sigma = (mmu_me_two_term_kwt - mmu_me_codata) / mmu_me_err
    dq_two_term_plain_vs_muon_ppb = (q_two_term_plain - q_muon_50) / q_muon_50 * mpf("1e9")
    dq_two_term_derived_vs_muon_ppb = (q_two_term_derived - q_muon_50) / q_muon_50 * mpf("1e9")
    mup_tension_two_term_derived_ppb = (mmu_me_two_term_derived - mmu_me_codata) / mmu_me_codata * mpf("1e9")
    mup_tension_two_term_derived_sigma = (mmu_me_two_term_derived - mmu_me_codata) / mmu_me_err
    dq_two_term_kwt_vs_muon_ppb = (q_two_term_kwt - q_muon_50) / q_muon_50 * mpf("1e9")
    e3_plus_e21_trace_residual = abs((tr_e3_V3 + tr_e21_V3) - tr_V3)

    print("=" * 78)
    print("  m_p substrate identity (production compute, 50 dps)")
    print("=" * 78)
    print()
    print("  CALIBRATION INPUTS (only 2 — CAL-3 is not used for baryons):")
    print(f"    m_e   = {mp.nstr(m_e, 18)} MeV  (CAL-1)")
    print(f"    m_μ   = {mp.nstr(m_mu, 18)} MeV  (CAL-2 via m_μ/m_e = {mp.nstr(m_mu_over_m_e, 12)})")
    print(f"    q_0   = {mp.nstr(q, 18)}        (substrate)")
    print()
    print("  SUBSTRATE BUILDING BLOCKS:")
    print(f"    |tr_M(β_Bor, q_0)|     = {mp.nstr(trM_borromean(q), 18)}")
    print(f"    [3]_q!                 = {mp.nstr(qfact_three(q), 18)}")
    print(f"    q_0^3                  = {mp.nstr(q**3, 18)}")
    print(f"    F_Bor(q_0)             = {mp.nstr(F, 18)}")
    print(f"    X = Δm/M_N (skein)     = {mp.nstr(X, 18)}")
    print()
    print("  PREDICTIONS vs CODATA:")
    print(f"    m_μ_pred = m_e·Vol(4₁)/ℏ_q²   = {mp.nstr(m_mu, 18)} MeV")
    print(f"    m_μ_codata                    = {mp.nstr(m_mu_measured, 18)} MeV")
    print(f"    Δ (9.5σ μ-p tension)          = {mp.nstr(res_m_mu_ppm, 8)} ppm")
    print()
    print(f"    m_p_pred = 2·m_μ·F − 12·m_e   = {mp.nstr(m_p_pred, 18)} MeV")
    print(f"    m_p_codata                    = {mp.nstr(m_p_codata, 18)} MeV")
    print(f"    Δ                              = {mp.nstr(res_m_p_ppm, 8)} ppm")
    print()
    print(f"    m_n_pred = m_p + Q_β + m_e       = {mp.nstr(m_n_pred, 18)} MeV")
    print(f"    m_n_codata                       = {mp.nstr(m_n_codata, 18)} MeV")
    print(f"    Δ                                = {mp.nstr(res_m_n_ppm, 8)} ppm")
    print()
    print(f"    Q_β_pred = m_n − m_p − m_e       = {mp.nstr(Q_beta_pred, 14)} MeV")
    print(f"    Q_β_codata                       = {mp.nstr(Q_beta_codata, 14)} MeV")
    print(f"    Δ                                = {mp.nstr(res_Q_beta_ppm, 8)} ppm")
    print()
    print(f"    M_N_pred = (m_p + m_n)/2         = {mp.nstr(M_N_pred, 18)} MeV")
    print(f"    Δ                                = {mp.nstr(res_M_N_ppm, 8)} ppm")

    # ── BUILD WITNESS ──────────────────────────────────────────────
    w = WitnessBuilder("m-p-substrate-identity-50dps", engine="mpmath")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Production substrate-categorical prediction of m_p and m_n from "
        "(m_e, m_μ, q_0) using Lean-proved closed forms for |tr_M(β_Bor)| "
        "and [3]_q!. The neutron uses the 3-input chain m_n = m_p + Q_β + m_e "
        "with Q_β the scored owner-ruled D1 = A cell |ε_flavour(V³)|·E₀ "
        "(−486 ppm on m_n, conditional on conjectures C1–C3; switched from the "
        "retired z = 1 mixed base on 2026-11-21, issue #8769); the Hecke-skein "
        "flavor-split is a secondary ratio. "
        "CAL-3 (Q_β) is NOT used as input — Q_β becomes a DERIVED quantity. "
        "Substrate identity: m_p = 2·m_μ·|tr_M|·[3]_q!/q^3 - 12·m_e where "
        "the '12' is the Ocneanu cancellation reciprocal."
    )
    w.set_content_block("conj:proton-mass-substrate-identity")
    w.set_audit_only("docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md")

    w.add_parameter("q0", mp.nstr(q, 25))
    w.add_parameter("m_e_MeV", mp.nstr(m_e, 18))
    w.add_parameter("m_mu_MeV", mp.nstr(m_mu, 18))
    w.add_parameter("m_mu_over_m_e", mp.nstr(m_mu_over_m_e, 18))

    w.add_data("substrate_building_blocks", {
        "abs_trM_borromean": mp.nstr(trM_borromean(q), 25),
        "qfact_3": mp.nstr(qfact_three(q), 25),
        "q_cubed": mp.nstr(q ** 3, 25),
        "F_Bor": mp.nstr(F, 25),
        "flavor_split_X": mp.nstr(X, 25),
    })

    w.add_data("predictions", {
        "m_p_MeV": mp.nstr(m_p_pred, 25),
        "m_n_MeV": mp.nstr(m_n_pred, 25),
        "M_N_MeV": mp.nstr(M_N_pred, 25),
        "Q_beta_MeV": mp.nstr(Q_beta_pred, 25),
        "Delta_m_pn_MeV": mp.nstr(Delta_m_pred, 25),
    })

    # predictions_pathC retained for backward-compat: it now carries the
    # SAME canonical neutron (scored D1 = A Q_β) — no longer the circular
    # Q_AME path. (predictions == predictions_pathC by construction now.)
    m_n_C_ppm = (m_n_pred - m_n_codata) / m_n_codata * mpf("1e6")
    Delta_codata = m_n_codata - m_p_codata
    Delta_ppb = float((Delta_m_pred - Delta_codata) / Delta_codata * mpf("1e9"))
    w.add_data("predictions_pathC", {
        "m_n_MeV": mp.nstr(m_n_pred, 25),
        "m_n_residual_ppm": mp.nstr(m_n_C_ppm, 12),
        "Delta_m_pn_MeV": mp.nstr(Delta_m_pred, 25),
        "Delta_m_pn_ppb": str(Delta_ppb),
        "Q_beta_N3_MeV": mp.nstr(Q_beta_pred, 25),
        "derivation": "m_n = m_p + Q_β(scored D1 = A, |eps_flavour(V^3)|*E0, C1-C3 conditional) + m_e",
    })

    # Secondary diagnostics — the flavor-split RATIO route + the explicit
    # circular round-trip check (experimental Q_β). Neither is the
    # canonical neutron; both kept for transparency.
    m_n_fs_ppm = (m_n_flavor_split - m_n_codata) / m_n_codata * mpf("1e6")
    diagnostics = {
        "m_n_retired_mixed_base_MeV": mp.nstr(m_n_retired_mixed_base, 25),
        "Q_beta_retired_mixed_base_MeV": mp.nstr(Q_beta_retired_mixed_base, 25),
        "m_n_retired_mixed_base_residual_ppb": mp.nstr(
            (m_n_retired_mixed_base - m_n_codata) / m_n_codata * mpf("1e9"), 12),
        "retired_mixed_base_note": (
            "q_beta_kashiwara_n2_mev: z = 1 Form A with a convention-D phase, "
            "retired 2026-11-16. Was the production m_n until 2026-11-21 "
            "(issue #8769). Not a convention-D prediction."
        ),
        "m_n_flavor_split_MeV": mp.nstr(m_n_flavor_split, 25),
        "m_n_flavor_split_residual_ppm": mp.nstr(m_n_fs_ppm, 12),
        "Delta_m_pn_flavor_split_MeV": mp.nstr(Delta_m_flavor_split, 25),
        "flavor_split_note": (
            "flavor-split is a derived u↔d RATIO (prop:flavor-split-substrate), "
            "−1.76 ppm on m_n; NOT the production neutron route."
        ),
    }
    if m_n_roundtrip is not None:
        diagnostics["roundtrip_check_experimental_qbeta_MeV"] = mp.nstr(m_n_roundtrip, 25)
        diagnostics["roundtrip_note"] = (
            "m_p + Q_AME(experimental) + m_e recovers CODATA m_n BY "
            "CONSTRUCTION — circular, NOT a prediction (3-input over-count)."
        )
    w.add_data("neutron_diagnostics", diagnostics)

    w.add_data("codata_comparison", {
        "m_p_codata_MeV": mp.nstr(m_p_codata, 25),
        "m_p_residual_ppm": mp.nstr(res_m_p_ppm, 12),
        "m_n_codata_MeV": mp.nstr(m_n_codata, 25),
        "m_n_residual_ppm": mp.nstr(res_m_n_ppm, 12),
        "M_N_codata_MeV": mp.nstr(M_N_codata, 25),
        "M_N_residual_ppm": mp.nstr(res_M_N_ppm, 12),
        "Q_beta_codata_MeV": mp.nstr(Q_beta_codata, 25),
        "Q_beta_residual_ppm": mp.nstr(res_Q_beta_ppm, 12),
    })

    # Lean SDP-uniqueness cross-reference (PR #1537/#1542 wiring,
    # 2026-05-31). Each nucleus's canonical T_w knot operator's
    # uniqueness at the empty-constraint SDP demonstration level is
    # certified by the named theorem below.
    w.add_data("lean_uniqueness_ref", {
        "proton": "qou:QOU.BraidKnot.PeriodicTableUniqueness.h_uniqueness_closed",
        "neutron": "qou:QOU.BraidKnot.nucleus_uniqueness_closed (n=3)",
        "deuteron": "qou:QOU.BraidKnot.deuteron_uniqueness_closed",
        "tritium": "qou:QOU.BraidKnot.tritium_uniqueness_closed",
        "helium3": "qou:QOU.BraidKnot.helium3_uniqueness_closed",
        "framework_doc":
            "folio/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": (
            "These theorems certify T_w uniqueness at the abstract "
            "empty-constraint SDP level. The real per-nucleus SDP "
            "(multi-term cost from this mass-identity formula + "
            "non-empty constraints) is per-nucleus substantive open "
            "work; see docs/coordination/2026-05-30-sdp-uniqueness-status.md."
        ),
    })

    # Tier A additive block: two-term Borromean V³ = (σ₁σ₂⁻¹)³ connected QED
    # diagnostics backed by QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm (qou-7ph7).
    w.add_data("two_term_borromean_qed_diagnostics", {
        "tr_V3": mp.nstr(tr_V3, 50),
        "tr_e3_V3": mp.nstr(tr_e3_V3, 50),
        "tr_e21_V3": mp.nstr(tr_e21_V3, 50),
        "tr_conn_p": mp.nstr(tr_conn_p, 50),
        "tr_conn_n": mp.nstr(tr_conn_n, 50),
        "tr_conn_diff": mp.nstr(tr_conn_diff, 50),
        "tr_e21_QAdjp": mp.nstr(tr_e21_QAdjp, 50),
        "tr_e21_QAdjn": mp.nstr(tr_e21_QAdjn, 50),
        "tr_e21_QAdj_diff": mp.nstr(tr_e21_QAdj_diff, 50),
        "weighting_canonical": "derived: Tr(K^{⊗3}·)/[2]_q³ (qou-99qc); *_MeV without suffix, *_Kp, *_KnKp, *_plain are historical",
        "scored_insertion": "covariant all-pairs (owner 2026-11-20 16:44): connected part 0 on V³; *_derived_* = adjacent (option 1), labelled",
        "M_p_QED_conn_scored_MeV": mp.nstr(M_p_QED_conn_scored_MeV, 25),
        "Delta_m_QED_conn_scored_MeV": mp.nstr(Delta_m_QED_conn_scored_MeV, 25),
        "Q_beta_two_term_derived_adjacent_MeV": mp.nstr(Q_beta_two_term_derived_adjacent_MeV, 25),
        "q_two_term_borromean_scored": mp.nstr(q_two_term_scored, 50),
        "M_p_QED_conn_derived_MeV": mp.nstr(M_p_QED_conn_derived_MeV, 25),
        "Delta_m_QED_conn_derived_MeV": mp.nstr(Delta_m_QED_conn_derived_MeV, 25),
        "M_p_QED_conn_MeV": mp.nstr(M_p_QED_conn_MeV, 25),
        "M_p_QED_conn_Kp_MeV": mp.nstr(M_p_QED_conn_Kp_MeV, 25),
        "Delta_m_QED_conn_MeV": mp.nstr(Delta_m_QED_conn_MeV, 25),
        "Delta_m_QED_conn_KnKp_MeV": mp.nstr(Delta_m_QED_conn_KnKp_MeV, 25),
        "Q_beta_two_term_plain_MeV": mp.nstr(Q_beta_two_term_plain_MeV, 25),
        "Q_beta_two_term_MeV": mp.nstr(Q_beta_two_term_MeV, 25),
        "Q_beta_two_term_residual_ppm": mp.nstr(res_Q_beta_two_term_ppm, 12),
        "m_n_two_term_MeV": mp.nstr(m_n_two_term_MeV, 25),
        "m_n_two_term_derived_adjacent_MeV": mp.nstr(m_p_pred + Q_beta_two_term_derived_adjacent_MeV + m_e, 25),
        "q_two_term_borromean_derived": mp.nstr(q_two_term_derived, 50),
        "dq_two_term_derived_vs_muon_ppb": mp.nstr(dq_two_term_derived_vs_muon_ppb, 12),
        "mup_tension_two_term_derived_ppb": mp.nstr(mup_tension_two_term_derived_ppb, 12),
        "mup_tension_two_term_derived_sigma": mp.nstr(mup_tension_two_term_derived_sigma, 12),
        "m_n_two_term_residual_ppb": mp.nstr(res_m_n_two_term_ppb, 12),
        "q_two_term_borromean_plain": mp.nstr(q_two_term_plain, 50),
        "q_two_term_borromean_k_weighted": mp.nstr(q_two_term_kwt, 50),
        "dq_two_term_plain_vs_muon_ppb": mp.nstr(dq_two_term_plain_vs_muon_ppb, 12),
        "dq_two_term_k_weighted_vs_muon_ppb": mp.nstr(dq_two_term_kwt_vs_muon_ppb, 12),
        "mup_tension_one_term_ppb": mp.nstr(res_m_mu_ppm * mpf("1e3"), 12),
        "mup_tension_two_term_plain_ppb": mp.nstr(mup_tension_two_term_plain_ppb, 12),
        "mup_tension_two_term_plain_sigma": mp.nstr(mup_tension_two_term_plain_sigma, 12),
        "mup_tension_two_term_k_weighted_ppb": mp.nstr(mup_tension_two_term_kwt_ppb, 12),
        "mup_tension_two_term_k_weighted_sigma": mp.nstr(mup_tension_two_term_kwt_sigma, 12),
        "lean_theorems": {
            "trace_borromeanV3A": "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_borromeanV3A",
            "trace_e3p_borromeanV3": "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_e3p_borromeanV3",
            "trace_e21p_borromeanV3": "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_e21p_borromeanV3",
            "trace_e21_strong_cartan_diff_borromeanV3": (
                "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_e21_strong_cartan_diff_borromeanV3"
            ),
            "trace_QAdjp_borromeanV3": "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3",
            "trace_QAdjn_borromeanV3_connected": (
                "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjn_borromeanV3_connected"
            ),
            "trace_QAdj_connected_diff_borromeanV3": (
                "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3"
            ),
            "trace_e21_QAdj_diff_borromeanV3": (
                "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_e21_QAdj_diff_borromeanV3"
            ),
        },
        "note": (
            "Tier A non-breaking diagnostic block (bean qou-7ph7): evaluates the "
            "connected 4th-order Borromean V³ = (σ₁σ₂⁻¹)³ quark charge traces proved "
            "sorry-free in QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean. "
            "WEIGHTING DERIVED 2026-11-20 (qou-99qc): Tr(K^{⊗3}·)/[2]_q³ "
            "(NucleonWeightSpaceQTrace). INSERTION RULED 2026-11-20 16:44: covariant all-pairs, "
            "connected part 0 on V³, so m_n_two_term / Q_beta_two_term equal the one-term values. "
            "Adjacent comparison (option 1): M_p^QED,conn = +0.0901243 keV, Δm = -0.1272243 keV. "
            "Historical 1/3-normalised adjacent 'plain': +0.220077 / -0.331696 keV. NOT DERIVED "
            "PREDICTIONS (bean qou-99qc, 2026-11-19): the word dependence comes only "
            "from dropping quark pair 1-3 (summed over all pairs the insertion is "
            "word-independent, trace_QPair_diff_word), and the scale/weighting were "
            "chosen against the μ–p and Q_β targets. Records of selected combinations; "
            "they do not close either residual."
        ),
    })

    # Assertions: tight matches
    w.add_assertion(
        name="m_p_matches_codata_within_1ppm",
        computed=abs(res_m_p_ppm),
        expected=mpf("0"),
        tolerance=mpf("1"),
        unit="ppm",
        source=(
            "m_p substrate identity should match CODATA m_p within 1 ppm — "
            "observed 0.24 ppm, well within tolerance."
        ),
    )
    w.add_assertion(
        name="m_n_matches_codata_within_10ppb",
        computed=abs(res_m_n_ppm) * 1000,      # ppm → ppb
        expected=mpf("0"),
        tolerance=mpf("10"),
        unit="ppb",
        source=(
            "m_n via the scored D1 = A Q_β (n→p+e+ν̄) against CODATA m_n at "
            "10 ppb. It FAILS: −486 ppm, because the scored Q_β is −58.4 % "
            "(conditional on C1–C3). Kept failing on purpose: the tolerance is "
            "the target, not a bound sized to the miss. Before 2026-11-21 it "
            "also failed (+501 ppb) on the retired mixed base."
        ),
    )
    w.add_assertion(
        name="borromean_v3_e3_plus_e21_equals_full_trace",
        computed=e3_plus_e21_trace_residual,
        expected=mpf("0"),
        tolerance=mpf("1e-45"),
        unit="dimensionless",
        source=(
            "Exact central idempotent trace decomposition tr(e_{(3)} V³) + tr(e_{(2,1)} V³) "
            "= tr(V³) on the 3-strand nucleon weight spaces W_p and W_n "
            "(QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_e3p_borromeanV3, "
            "trace_e21p_borromeanV3)."
        ),
    )
    w.add_assertion(
        name="borromean_v3_conn_proton_closes_mup_gap_within_1sigma",
        computed=abs(mup_tension_two_term_plain_sigma),
        expected=mpf("0"),
        tolerance=mpf("1"),
        unit="sigma",
        source=(
            "RECORD OF A SELECTED COMBINATION, not a zero-parameter prediction "
            "(bean qou-99qc, 2026-11-19): connected 4th-order Borromean proton QED "
            "term M_p^QED,conn = m_e·|tr_bar_conn(p, V³)| (+0.220077 keV, "
            "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3), "
            "with the m_e scale and the adjacent-pair restriction both chosen. "
            "Checks that the recorded combination reproduces +8.06 ppb = +0.36σ; it "
            "is not evidence that the μ–p tension (9.5σ on the ratio) is closed."
        ),
    )

    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
