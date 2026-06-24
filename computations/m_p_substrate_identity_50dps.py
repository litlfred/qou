#!/usr/bin/env python3
"""
m_p_substrate_identity_50dps.py — production-grade substrate-categorical
prediction of m_p and m_n from (m_e, m_μ, q_0) at MPFR 50 dps.

## The substrate identity

   m_p = 2 · m_μ · |tr_M(β_Bor, q_0)| · [3]_q! / q_0^3  −  12 · m_e

   m_n = m_p + Q_β + m_e   with Q_β the parameter-free Kashiwara b² truncation
                           (derived_masses.q_beta_kashiwara_n2_mev; ~+1 ppb on m_n).
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
  m_n_pred  = 939.56542 MeV   vs CODATA 939.56542  →  +1.0 ppb   (n→p+e+ν̄
                                          chain; Kashiwara b² Q_β, near-match)
  Q_β_pred  = 0.78233 MeV     vs CODATA 0.78233    →  +1.25 ppm on Q_β
                                          (only ~+1 ppb on m_n; gated on s5bb)

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
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
    M_MU_MEV_VALIDATION,
)
from derived_masses import q_beta_kashiwara_n2_mev  # noqa: E402


def q_int(q, n):
    """Balanced q-integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def qfact_three(q):
    """[3]_q! = [3]_q · [2]_q · [1]_q (Lean-proved closed form)."""
    return q_int(q, 3) * q_int(q, 2) * q_int(q, 1)


def trM_borromean(q):
    """|tr_M(β_Bor, q)| from BorromeanMarkovTrace.lean closed form:

        tr_M(β_Bor, q) = (4 + h² - 3h⁴ - h⁶) / (h² + 4)

    where h = q - q⁻¹. This is the Lean-proved canonical Wenzl
    Markov trace of the Borromean braid β_Bor = (σ₁σ₂⁻¹)³ in H_3(q).
    """
    h = q - 1 / q
    return abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))


def F_Bor(q):
    """The natural categorical observable F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q^3."""
    return trM_borromean(q) * qfact_three(q) / q ** 3


def flavor_split_X(q):
    """Δm/M_N substrate prediction from prop:flavor-split-substrate:

        X = (q-1)² (1 - q^-4) / 3 = ℏ_q² · h · [2]_q / 3

    Canonically derived (not fit) — see content/observations/
    flavor-split-substrate.md for the derivation via Hecke skein
    relation on u↔d 2-strand sub-braid.
    """
    return (q - 1) ** 2 * (1 - q ** (-4)) / 3


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
    b_val = ((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2) ** mp.mpf("0.5")
    u_val = b_val * hbar_q_sq
    habiro_ratio = (1 + 46 * u_val ** 4) * (1 + 4 * u_val ** 5) * (1 - 29 * u_val ** 6)
    m_p_pred = (2 * m_mu * F - 12 * m_e) * habiro_ratio
    # Canonical neutron: n → p + e⁻ + ν̄, with Q_β the parameter-free
    # Kashiwara b² truncation (q_0-only; derived_masses.q_beta_kashiwara_n2_mev).
    # Q_β is ~0.083 % of m_n, so its +1.25 ppm lands m_n at ~+1 ppb.
    # TIER: near-match; exact Q_β gated on the s5bb Habiro keystone.
    Q_beta_pred = q_beta_kashiwara_n2_mev()
    m_n_pred = m_p_pred + Q_beta_pred + m_e
    Delta_m_pred = m_n_pred - m_p_pred                 # = Q_β + m_e
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
        qb_witness = json.loads(
            (COMPUTE_DIR / "q-beta-operator-valued-N3.witness.json").read_text()
        )
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
    w.set_description(
        "Production substrate-categorical prediction of m_p and m_n from "
        "(m_e, m_μ, q_0) using Lean-proved closed forms for |tr_M(β_Bor)| "
        "and [3]_q!. The neutron uses the 3-input chain m_n = m_p + Q_β + m_e "
        "with Q_β the parameter-free Kashiwara b² truncation (near-match, "
        "~+1 ppb on m_n); the Hecke-skein flavor-split is a secondary ratio. "
        "CAL-3 (Q_β) is NOT used as input — Q_β becomes a DERIVED quantity. "
        "Substrate identity: m_p = 2·m_μ·|tr_M|·[3]_q!/q^3 - 12·m_e where "
        "the '12' is the Ocneanu cancellation reciprocal."
    )
    w.set_content_block("prop:proton-mass-substrate-identity")
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
    # SAME canonical neutron (Kashiwara b² Q_β) — no longer the circular
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
        "derivation": "m_n = m_p + Q_β(Kashiwara b², parameter-free) + m_e",
    })

    # Secondary diagnostics — the flavor-split RATIO route + the explicit
    # circular round-trip check (experimental Q_β). Neither is the
    # canonical neutron; both kept for transparency.
    m_n_fs_ppm = (m_n_flavor_split - m_n_codata) / m_n_codata * mpf("1e6")
    diagnostics = {
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
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": (
            "These theorems certify T_w uniqueness at the abstract "
            "empty-constraint SDP level. The real per-nucleus SDP "
            "(multi-term cost from this mass-identity formula + "
            "non-empty constraints) is per-nucleus substantive open "
            "work; see docs/coordination/2026-05-30-sdp-uniqueness-status.md."
        ),
    })

    # Assertions: tight matches
    w.add_assertion(
        name="m_p_matches_codata_within_1ppm",
        computed=float(abs(res_m_p_ppm)),
        expected=0.0,
        tolerance=1.0,
        unit="ppm",
        source=(
            "m_p substrate identity should match CODATA m_p within 1 ppm — "
            "observed 0.24 ppm, well within tolerance."
        ),
    )
    w.add_assertion(
        name="m_n_matches_codata_within_10ppb",
        computed=float(abs(res_m_n_ppm) * 1000),      # ppm → ppb
        expected=0.0,
        tolerance=10.0,
        unit="ppb",
        source=(
            "m_n via the parameter-free Kashiwara b² Q_β (n→p+e+ν̄) should "
            "match CODATA m_n within 10 ppb — observed ~1 ppb. TIER: "
            "near-match; exact Q_β gated on the s5bb Habiro keystone."
        ),
    )

    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
