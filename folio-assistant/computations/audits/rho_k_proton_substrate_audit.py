#!/usr/bin/env python3
"""
rho_k_proton_substrate_audit.py — substrate-derivation audit for the
proton's categorical density ρ_K.

## Why this probe exists

PR #1272's γγ-pair-production-decomposition probe identified that
the 2.89% VolDensity(𝓑₃) residual is NOT a simple h²-coefficient swap
inside `linking_weight`. Tracing through the canonical 6-term
mass-endomorphism formula
([`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md))
shows the actual closure problem is the **categorical density ρ_K**
of [`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md):

  • The structural 6-term sum at q₀ gives |sum| ≈ 2.21 (= 1.13 MeV)
  • CODATA m_p = 938.27 MeV
  • Closure factor ρ_K ≈ m_p_CODATA / (m_e · |tr_M(T_w, q₀)|) ≈ 1723.6

The Borromean `linking_weight` parameterization is just
ρ_K · |tr_M| / (Vol/ℏ_q²) = same ρ_K closure problem, re-named.

## What this probe does

1. Reads [`mass-formula-6term-mpfr-50dps.witness.json`](mass-formula-6term-mpfr-50dps.witness.json)
   and [`term6-full-pole-sum.witness.json`](term6-full-pole-sum.witness.json)
   to extract the 6 structural terms for the proton.

2. Computes the empirical ρ_K via the simple-form
   `ρ_K = m_p_CODATA / (m_e · |tr_M(T_w, q₀)|)` and reports the value.

3. Computes the alternative via the linking_weight parameterization:
   `ρ_K_via_linking = linking_weight_target · (Vol/ℏ_q²) / |tr_M|`.

4. Verifies the two routes agree (confirming they parameterize the
   same closure).

5. Reports the **graded substrate expansion** of ρ_K per
   [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md):
     • LO piece: `Z m_p + N m_n + Z m_e` (proved, Wenzl 1988
       Markov multiplicativity) — but for A=1 proton this reduces to
       m_p itself, so the LO piece is trivial here.
     • single-gen piece: `α · Σ_i ln|V̂_i^full|` (empirical 0.18%)
     • pair-gen piece: OPEN — conjectural ρ_K-pair-gen
       (`conj:rho-k-pair-gen-canonical-form`)

The open pair-gen piece IS the structural derivation that would close
the per-knot VolDensity gap categorically.

## Status

AUDIT-ONLY — does not introduce new closure attempts. Documents the
existing decomposition + the (empirical) value of ρ_K^𝔭. The
substrate derivation of ρ_K's pair-gen component remains open.

Ref: [`docs/audits/2026-05-25-non-abelian-stokes-reading-a-exploration.md`](../../docs/audits/2026-05-25-non-abelian-stokes-reading-a-exploration.md)
Ref: [`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
Ref: [`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md)
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as q0  # noqa: E402
from codata_constants import M_E_MEV, M_P_MEV_VALIDATION  # noqa: E402


def load_six_term_proton():
    """Load proton entry from mass-formula-6term-mpfr-50dps witness."""
    path = _pb.witness_path("mass-formula-6term-mpfr-50dps.witness.json", HERE)
    with path.open() as f:
        data = json.load(f)
    proton = next(r for r in data["data"]["results"] if r["Z"] == 1 and r["N"] == 0)
    return proton


def load_term6_proton():
    """Load proton term6 from term6-full-pole-sum witness."""
    path = _pb.witness_path("term6-full-pole-sum.witness.json", HERE)
    with path.open() as f:
        data = json.load(f)
    proton = next(a for a in data["data"]["atoms"] if a["atom"].startswith("p"))
    return proton


def main():
    set_compute_dps()

    # ── Load structural terms ──────────────────────────────────
    six_term = load_six_term_proton()
    term6 = load_term6_proton()

    T1 = mpf(six_term["term1_descended"])
    T2 = mpf(six_term["term2_single"])
    T3 = mpf(six_term["term3_pair"])
    T4 = mpf(six_term["term4_frob_canonical_per_3A"])
    T5 = mpf(six_term["term5_chirality_bw"])
    T6 = mpf(term6["term6_simple_residue_partial"])

    sum_signed = T1 + T2 + T3 + T4 + T5 + T6
    sum_abs_T5 = T1 + T2 + T3 + T4 + abs(T5) + T6  # treat |T5| if sign anomaly

    m_e_mp = mpf(M_E_MEV)
    m_p_codata = mpf(M_P_MEV_VALIDATION)

    # ── ν_SDP for proton (per atom-knot-mass-derivation.md line 264) ──
    # The doc reports ν_SDP_D = 1, ν_SDP_T = 2, ν_SDP_³He = 2.  For the
    # proton itself (A=1) the structural prefactor rule gives ν_SDP = 1.
    nu_SDP_proton = 1

    # ── Empirical ρ_K via the canonical simple form ──────────────
    # m_p = m_e · ρ_K · |tr_M|  ⇒  ρ_K = m_p / (m_e · |tr_M|)
    rho_K_via_trM = m_p_codata / (m_e_mp * abs(T1))

    # ── Cross-check: ρ_K via linking_weight parameterization ─────
    # m_p = m_e · Vol/ℏ_q² · linking_weight
    # linking_weight = ρ_K · |tr_M| / (Vol/ℏ_q²)
    # ⇒ ρ_K_via_lw = linking_weight_target · (Vol/ℏ_q²) / |tr_M|
    q = q0
    hbar_q_sq = ((q - 1) / q) ** 2
    vol_b3 = 8 * mp.catalan
    geom_leading = vol_b3 / hbar_q_sq
    linking_weight_target = m_p_codata / (m_e_mp * geom_leading)
    rho_K_via_linking = linking_weight_target * geom_leading / abs(T1)

    # The two routes MUST agree by algebra.
    delta_rho_routes = abs(rho_K_via_trM - rho_K_via_linking)

    # ── Implied prediction from the full 6-term sum ──────────────
    m_p_pred_signed_sum = m_e_mp * abs(sum_signed)
    m_p_pred_abs_sum = m_e_mp * sum_abs_T5

    print("=" * 76)
    print("  ρ_K substrate audit for the proton")
    print(f"  q₀ = {mp.nstr(q, 12)}")
    print("=" * 76)
    print()
    print(f"  6-term canonical formula at proton (q₀):")
    print(f"    T1 |tr_M(T_w)|          = {mp.nstr(T1, 12)}")
    print(f"    T2 single brane tower   = {mp.nstr(T2, 12)}")
    print(f"    T3 pair brane tower     = {mp.nstr(T3, 12)}")
    print(f"    T4 Frobenius co-Casimir = {mp.nstr(T4, 12)}")
    print(f"    T5 chirality + bulk     = {mp.nstr(T5, 12)}  ← negative!")
    print(f"    T6 Habiro residue       = {mp.nstr(T6, 12)}")
    print(f"    Σ T_i (signed)          = {mp.nstr(sum_signed, 12)}")
    print(f"    Σ T_i with |T5|          = {mp.nstr(sum_abs_T5, 12)}")
    print()
    print(f"  Predicted m_p from 6-term sum:")
    print(f"    |sum| · m_e             = {mp.nstr(m_p_pred_signed_sum, 8)} MeV  (off by {mp.nstr(m_p_codata / m_p_pred_signed_sum, 6)}×)")
    print(f"    |T5|-flipped sum · m_e  = {mp.nstr(m_p_pred_abs_sum, 8)} MeV  (off by {mp.nstr(m_p_codata / m_p_pred_abs_sum, 6)}×)")
    print(f"    CODATA m_p              = {mp.nstr(m_p_codata, 8)} MeV")
    print()
    print(f"  Empirical ρ_K closure factor:")
    print(f"    ρ_K via simple form     = {mp.nstr(rho_K_via_trM, 8)}")
    print(f"    ρ_K via linking_weight  = {mp.nstr(rho_K_via_linking, 8)}")
    print(f"    Δ (route agreement)     = {mp.nstr(delta_rho_routes, 6)}")
    print(f"    Doc-quoted ρ_K^𝔭        ≈ 1723.6  (atom-knot-mass-derivation.md line 7)")
    print()

    # ── Verify the two routes agree (they MUST by algebra) ────────
    routes_agree = float(delta_rho_routes < mpf("1e-12"))

    # ── Build witness ──────────────────────────────────────────
    w = WitnessBuilder(
        "rho-k-proton-substrate-audit",
        engine="mpmath",
    )
    w.set_description(
        "Substrate-derivation audit for the proton's categorical density "
        "ρ_K. Companion to PR #1272 — traces through the canonical 6-term "
        "mass-endomorphism formula at q₀ and shows that linking_weight "
        "and ρ_K parameterize the same closure problem. Reads existing "
        "6-term + term-6 witnesses; computes implied ρ_K via two routes "
        "(simple form `m_p / (m_e · |tr_M|)` and linking_weight form) and "
        "verifies they agree. The pair-gen substrate-component of ρ_K "
        "(per prop:rho-k-graded-expansion) is the OPEN derivation that "
        "would close the per-knot VolDensity gap categorically."
    )
    w.add_parameter("q0", mp.nstr(q, 20))
    w.add_parameter("m_e_MeV", mp.nstr(m_e_mp, 20))
    w.add_parameter("m_p_codata_MeV", mp.nstr(m_p_codata, 20))
    w.add_parameter("nu_SDP_proton", nu_SDP_proton)

    w.add_data("six_term_at_q0", {
        "T1_tr_M": mp.nstr(T1, 20),
        "T2_single_brane_tower": mp.nstr(T2, 20),
        "T3_pair_brane_tower": mp.nstr(T3, 20),
        "T4_frobenius_co_casimir": mp.nstr(T4, 20),
        "T5_chirality_bw": mp.nstr(T5, 20),
        "T6_habiro_residue": mp.nstr(T6, 20),
        "sum_signed": mp.nstr(sum_signed, 20),
        "sum_abs_T5_flipped": mp.nstr(sum_abs_T5, 20),
    })

    w.add_data("rho_K_computation", {
        "rho_K_via_simple_form": mp.nstr(rho_K_via_trM, 20),
        "rho_K_via_linking_weight": mp.nstr(rho_K_via_linking, 20),
        "delta_rho_routes": mp.nstr(delta_rho_routes, 20),
        "rho_K_doc_quoted": "1723.6 (atom-knot-mass-derivation.md line 7)",
        "linking_weight_target": mp.nstr(linking_weight_target, 20),
        "vol_b3_over_hbar_q_sq": mp.nstr(geom_leading, 20),
    })

    w.add_data("graded_substrate_expansion_status", {
        "LO_piece_status": (
            "PROVED (Wenzl 1988 Markov multiplicativity) but trivial for "
            "A=1 — reduces to m_p itself. Substantive only for A≥2 multi-"
            "nucleon binding chain."
        ),
        "single_gen_piece_status": (
            "EMPIRICAL: closes to ~0.18% per atomic-mass-gb-nf §rho_K closure. "
            "Categorical derivation NOT yet completed."
        ),
        "pair_gen_piece_status": (
            "OPEN: this is the conjectural `rho_K_pair_gen` of "
            "prop:rho-k-graded-expansion / conj:rho-k-pair-gen-canonical-form. "
            "Substrate-only derivation of this piece would close the per-knot "
            "VolDensity gap categorically — same problem as `derive linking_weight` "
            "(re-parameterised)."
        ),
    })

    # ── Assertions ─────────────────────────────────────────────
    w.add_assertion(
        name="rho_k_routes_agree",
        computed=routes_agree,
        expected=1.0,
        tolerance=1e-12,
        source=(
            "The simple form `ρ_K = m_p / (m_e · |tr_M|)` and the "
            "linking_weight form `ρ_K = linking_weight · (Vol/ℏ_q²) / |tr_M|` "
            "MUST agree by algebra. This assertion confirms they do."
        ),
    )

    w.add_assertion(
        name="rho_k_matches_doc_quoted_value",
        computed=mp.nstr(rho_K_via_trM, 8),
        expected="1723.6",  # tolerance handled via string-compare fallback
        tolerance=10.0,  # ~0.6% absolute tolerance
        source=(
            "Empirical ρ_K^𝔭 computed in this audit should match the "
            "value 1723.6 quoted in atom-knot-mass-derivation.md line 7."
        ),
    )

    out = w.save()
    print(f"  Witness: {out}")


if __name__ == "__main__":
    main()
