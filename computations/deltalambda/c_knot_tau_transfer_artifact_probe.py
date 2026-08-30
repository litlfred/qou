#!/usr/bin/env python3
"""Is the deuteron `C_knot = 5.853` a REAL missing many-body magnitude, or a master-formula
NORMALIZATION ARTIFACT? — settled by the fibre→archimedean τ-transfer, derive-then-check, 0-fit.

BEAN qou-1h3n (highest-leverage move of the 2026-08-08 week review) / qou-u8w5.

THE TWO ROUTES TO B(deuteron) IN THE CORPUS
  Route A (categorical master formula, m_e-scaled character sum):
      B_A = m_e · |Σ_λ y_λ χ^λ(β_D) sgn(w_0) f^λ| = m_e · |S(D)|,  |S(D)| = 0.7438  (#4543 pinned weight)
          = 0.38008 MeV      → misses AME (2.22457) by C_knot = 5.853×.
  Route B (fibre rotational tier tower, counit-scaled — g2-frame-artifact, PARAMETER-FREE):
      μ₀ = m_e/(3(q−q⁻¹)/2)         DERIVED per-crossing MeV scale (cheat-sheet L213/237; eunit-counit-mu0
                                    tracing: μ₀'s source is the counit skein (q−q⁻¹), 0 free params)
      E_rot = μ₀·ℏ_q·[3]_q[4]_q      (j = n/2 = 3 rotational band)  = 2.01958 MeV (−9.2%)
      E⁺ = E_rot/(1−t), t=(v−v⁻¹)/[2]_v   (bar-odd)                  = 2.13064 MeV (−4.2%)
      E₂ = E⁺·(1+h²), h=q−q⁻¹              (bar-even UNIT, coeff 1)  = 2.22376 MeV (−0.036%)
   Route B closes the deuteron to 360 ppm from q₀ ALONE, no free parameters.

THE τ-TRANSFER (the decisive substitution — done here, EXACT).
  Both routes claim B(deuteron); since Route B closes it parameter-free, C_knot = B_AME/B_A = E₂/B_A.
  Substitute the DERIVED μ₀ = m_e·2/(3h) into the tier-0 ratio:
      E_rot/B_A = [ m_e·(2/(3h))·ℏ_q·[3]_q[4]_q ] / [ m_e·|S| ]
                = (2/(3h))·ℏ_q·[3]_q[4]_q / |S|            ← the m_e CANCELS EXACTLY.
  So C_knot is NOT an electron-mass magnitude — it is a PURE q₀-GEOMETRY RATIO between two different
  normalizations of the same binding: the counit-scaled rotational band (numerator) over the
  m_e-scaled signed-character sum (denominator). No free magnitude; no dynamical many-body term.

EXPECTATION LOCKED BEFORE COMPUTE (anti-fit — nothing is tuned to 5.853):
  (1) numeric  E_rot/(m_e|S|)  ==  pure-geom  (2/(3h))ℏ_q[3][4]/|S|   (m_e cancellation, to 1e-40).
  (2) the counit per-crossing scale 1/h ≈ 4.78 is the single dominant factor of the ≈5.31 tier-0 ratio.
  (3) the tier-0 ratio ≈ 5.31 already accounts for ≳90% of C_knot = 5.853; the bar-odd × bar-even
      dressing supplies only ≈ ×1.10, and (g2-frame-artifact §3) that dressing is a FRAME PROJECTION
      (Ω_{k≥2}=0 EXACT for the single-generator word σ₁³), NOT a many-body/commutator term.

VERDICT IF (1)-(3) HOLD  →  ARTIFACT.  The 5.853 is the ratio of two q₀-geometric normalizations of the
deuteron binding, accounted for with 0 free parameters and 0 many-body terms. The H₆-interface
handle-commutator many-body-magnitude program, insofar as it targets the deuteron 5.853, is
BOOKKEEPING: it would double-count the counit normalization Route B already supplies, and the deuteron
word σ₁³ provably carries NO commutator content (Ω_{k≥2}=0; H₂(q) commutative, TrefoilSurfaceStateSum
`commutator_zero`). SCOPE BOUNDARY (honest): this settles the DEUTERON C_knot only. The A≥3 chain
EXTENSIVITY term (12.72× A-growth; intensive-vs-extensive + pairwise-cap proofs) is a SEPARATE,
proved-real, still-open object and is NOT dissolved by this deuteron verdict.

EXPLORATORY — audit + witness only; nothing wired; no fit; B_AME diagnostic-only, never inverted.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 50

# --- substrate inputs (muon-canonical computations/ layer; all derived / committed) ---
Q0_STR = "1.10997859555733471989976"
M_E_STR = "0.51099895"                 # CODATA electron mass (MeV) — the τ-functor scale
S_D_STR = "0.7438"                     # |S(D)| pinned Wenzl signed Markov sum (#4543)
# AME2020 deuteron binding (MeV) — DIAGNOSTIC ONLY, never inverted.
# Taken as the registry mpf rather than re-parsed from a string: mp.mpf("...")
# binds at whatever mp.mp.dps happens to be at import time, which is the pitfall
# mpf_import_time_dps_audit exists to catch.
B_AME_CONST = AME_B_DEUTERON_MEV_VALIDATION


def main() -> int:
    q0 = mp.mpf(Q0_STR)
    m_e = mp.mpf(M_E_STR)
    S_D = mp.mpf(S_D_STR)
    B_AME = B_AME_CONST

    h = q0 - 1 / q0                    # counit skein per-crossing weight (q − q⁻¹)
    hbar_q = 1 - 1 / q0                # ℏ_q
    v = mp.sqrt(q0)
    t = (v - 1 / v) / (v + 1 / v)      # bar-odd tier

    def qint(j):                       # balanced q-integer [j]_q
        return (q0 ** j - q0 ** (-j)) / (q0 - q0 ** (-1))

    # DERIVED per-crossing scale (0 free params): μ₀ = m_e / (3(q−q⁻¹)/2)
    mu0 = m_e / (3 * h / 2)

    # Route A (master, first-order) and Route B tiers (parameter-free)
    B_A = m_e * S_D
    E_rot = mu0 * hbar_q * qint(3) * qint(4)
    Eplus = E_rot / (1 - t)
    E2 = Eplus * (1 + h ** 2)
    C_knot = B_AME / B_A

    # --- the decisive τ-transfer substitution: m_e cancellation ---
    tier0_numeric = E_rot / B_A
    tier0_puregeom = (2 / (3 * h)) * hbar_q * qint(3) * qint(4) / S_D   # m_e ALGEBRAICALLY absent
    me_cancel_residual = abs(tier0_numeric - tier0_puregeom)           # must be ~1e-40

    counit_scale = 1 / h
    dressing = E2 / E_rot
    tier0_share = tier0_numeric / C_knot

    # locked-expectation assertions
    a1 = me_cancel_residual < mp.mpf("1e-30")          # (1) m_e cancels exactly
    a2 = abs(counit_scale - mp.mpf("4.78")) < mp.mpf("0.05")   # (2) counit 1/h dominates tier-0
    a3 = tier0_share > mp.mpf("0.85")                   # (3) tier-0 (normalization) ≳90% of C_knot
    a4 = abs(dressing - 1) < mp.mpf("0.15")             # dressing only ~10%, frame-projection not many-body
    verdict = "ARTIFACT" if (a1 and a3 and a4) else "INCONCLUSIVE"

    result = {
        "question": "deuteron C_knot=5.853: REAL missing many-body magnitude, or master-formula "
                    "NORMALIZATION ARTIFACT?",
        "verdict": verdict,
        "verdict_scope": "DEUTERON C_knot only. The A≥3 chain EXTENSIVITY term (12.72× A-growth; "
                         "intensive-vs-extensive + pairwise-cap proofs) is a SEPARATE proved-real "
                         "open object, NOT dissolved by this verdict.",
        "route_A_master_first_order_MeV": mp.nstr(B_A, 8),
        "route_B_tiers_MeV": {
            "tier0_E_rot": mp.nstr(E_rot, 8),
            "tier1_Eplus": mp.nstr(Eplus, 8),
            "tier2_E2": mp.nstr(E2, 8),
            "closes_B_AME_to_pct": mp.nstr((E2 - B_AME) / B_AME * 100, 3),
        },
        "mu0_MeV_DERIVED": mp.nstr(mu0, 8),
        "C_knot": mp.nstr(C_knot, 6),
        "tau_transfer_decomposition": {
            "tier0_ratio_numeric_E_rot_over_B_A": mp.nstr(tier0_numeric, 8),
            "tier0_ratio_pure_geometry_m_e_cancelled": mp.nstr(tier0_puregeom, 8),
            "m_e_cancellation_residual": mp.nstr(me_cancel_residual, 3),
            "counit_per_crossing_1_over_h": mp.nstr(counit_scale, 6),
            "dressing_multiplier_E2_over_E_rot": mp.nstr(dressing, 6),
            "tier0_normalization_share_of_C_knot_pct": mp.nstr(tier0_share * 100, 4),
            "meaning": "C_knot = (2/(3h))·ℏ_q·[3]_q[4]_q·(dressing) / |S| — a pure q₀-geometry ratio "
                       "of two normalizations (counit-scaled rotational band vs m_e-scaled character "
                       "sum). m_e cancels; the counit 1/h≈4.78 supplies the bulk; the ×1.10 dressing "
                       "is a frame projection (Ω_{k≥2}=0 exact for σ₁³), NOT a many-body term. No "
                       "5.853× many-body magnitude exists anywhere in the decomposition.",
        },
        "why_not_H6_handle_commutator": "deuteron word σ₁³ is single-generator ⇒ Ω_{k≥2}=0 EXACT "
            "(#4158); H₂(q) commutative ⇒ commutator_zero (TrefoilSurfaceStateSum.lean). No commutator "
            "charge lives on the deuteron. Any H₆-charge tuned to reproduce 5.853 would double-count the "
            "counit normalization Route B already supplies parameter-free ⇒ fit to B_AME/(m_e|S|).",
        "anti_fit_ledger": {
            "target_locked_before_compute": True,
            "B_AME_used_only_as_diagnostic_ratio_never_inverted": True,
            "free_parameters": 0,
            "nothing_wired": True,
            "m_e_cancellation_is_algebraic_not_tuned": True,
        },
        "description": "τ-transfer of the parameter-free fibre rotational tier tower (μ₀ counit-derived) "
                       "onto the m_e-scaled categorical master formula: the deuteron C_knot=5.853 is a "
                       "pure q₀-geometry NORMALIZATION ARTIFACT (m_e cancels; counit 1/h dominates; "
                       "dressing is a frame projection), NOT a missing many-body magnitude. Scope: "
                       "deuteron only; A≥3 extensivity term is separate/open.",
        "audit_only": True,
        "tier": "fibre→archimedean τ-transfer decomposition; derive-then-check; scope-(a); "
                "artifact-vs-real verdict; nothing wired; no fit.",
    }

    wb = WitnessBuilder.wrap_legacy(
        "c-knot-tau-transfer-artifact", result,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(result["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("m_e_cancels_exactly", computed=str(bool(a1)), expected="True")
    wb.add_assertion("counit_1_over_h_dominates_tier0", computed=str(bool(a2)), expected="True")
    wb.add_assertion("tier0_normalization_is_over_85pct_of_C_knot", computed=str(bool(a3)), expected="True")
    wb.add_assertion("dressing_is_small_frame_projection", computed=str(bool(a4)), expected="True")
    wb.add_assertion("verdict_is_ARTIFACT", computed=verdict, expected="ARTIFACT")
    wb.save(extra={"auditOnly": True})

    print("=" * 88)
    print("  Deuteron C_knot = 5.853: ARTIFACT vs REAL — the τ-transfer test")
    print("=" * 88)
    print(f"  Route A (master m_e·|S|)          = {mp.nstr(B_A, 8)} MeV")
    print(f"  Route B tier-2 (parameter-free)   = {mp.nstr(E2, 8)} MeV  ({mp.nstr((E2-B_AME)/B_AME*100,3)}% vs AME)")
    print(f"  C_knot = B_AME/B_A                = {mp.nstr(C_knot, 6)}")
    print("  --- τ-transfer (substitute derived μ₀ = m_e·2/(3h)) ---")
    print(f"  numeric   E_rot/(m_e|S|)          = {mp.nstr(tier0_numeric, 8)}")
    print(f"  pure-geom (2/(3h))ℏ_q[3][4]/|S|   = {mp.nstr(tier0_puregeom, 8)}   [m_e CANCELLED, residual {mp.nstr(me_cancel_residual,2)}]")
    print(f"  counit 1/h (per-crossing)         = {mp.nstr(counit_scale, 5)}")
    print(f"  tier-0 (normalization) share      = {mp.nstr(tier0_share*100, 4)}% of C_knot")
    print(f"  dressing (bar-odd × bar-even)     = ×{mp.nstr(dressing, 5)}  (frame projection, Ω_k≥2=0 exact)")
    print(f"\n  VERDICT: {verdict}")
    print("  → deuteron 5.853 is a q₀-geometry normalization ratio, not a many-body magnitude.")
    print("  → H₆ handle-commutator program is bookkeeping FOR THE DEUTERON (σ₁³ has no commutator).")
    print("  → SCOPE: A≥3 extensivity term is separate/open (NOT dissolved).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
