#!/usr/bin/env python3
"""Plan H — ρ(Z,N) Wedderburn-multiplicity experiment for ³He.

³He has the largest mass-residual in the principled census:
  M_err = +81 ppm  vs  ²H/⁴He at <1 ppm.
Strategy on file: `census:Borromean, ρ=2m_e` (hand-picked).
α* = 1.0 (all Wedderburn blocks PSD), so the canonical T_w IS the
Borromean closure ⟨σ_1 σ_2⁻¹⟩^3 in B_3 — no SDP solve needed for the
braid.  The open question is the prefactor ρ.

This script computes, at q_0 ≈ 1.1099786 (50 dps):
  - Per-Wedderburn-block character χ_λ(β) for β = (σ_1 σ_2⁻¹)^3
  - Markov-trace coefficient y_λ(q_0) (Wenzl bridge)
  - Markov trace tr_M(β) = Σ_λ y_λ χ_λ
  - Several candidate ρ formulas from Wedderburn multiplicity data
  - For each ρ candidate, the predicted B and its M_err_ppm

Goal: identify a ρ formula that closes the +81 ppm ³He gap WITHOUT
breaking ²H (12.9 ppm), ³H (4.7 ppm), ⁴He (0 ppm).

Refs:
  - docs/plans/H-rho-from-wedderburn-multiplicity.md
  - prop:atom-knot-mass-derivation §"Mass identity"
  - folio-assistant/computations/low-isotope-mass-table.witness.json
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import numpy as np

# Module-level constants (single source of truth) per CLAUDE.md guidance
Q_0 = 1.1099785955541805     # substrate parameter at f64 precision
M_E = 0.51099895             # electron mass in MeV (CODATA)
B_AME_3HE = 7.718            # ³He AME 2020 binding energy in MeV
# 2·m_p + m_n − B + 2·m_e ≈ ³He total mass in MeV
M_AME_3HE = 2809.41336
G_CATALAN = float(mp.catalan)  # Catalan's constant — same source everywhere


def hoefsmit_h3_at_q(q: float):
    """Return (T_1, T_2, T_2_inv) in the Hoefsmit standard (2,1)
    representation of H_3(q).  Verified to satisfy Hecke quadratic
    + braid relation at f64 precision.
    Reference: Mathas Def 3.32 / Geck-Pfeiffer §5.4 with axial dist 1.
    """
    T_1 = np.array([[q, 0.0], [0.0, -1.0 / q]])
    denom = q * q + 1.0
    a = -1.0 / (q * denom)
    d = (q ** 3) / denom
    c = (q ** 4 + q * q + 1.0) / (denom * denom)
    T_2 = np.array([[a, 1.0], [c, d]])
    h = q - 1.0 / q
    T_2_inv = T_2 - h * np.eye(2)
    return T_1, T_2, T_2_inv


def chi_partitions_at_borromean(q: float):
    """Return χ_λ((σ_1 σ_2^{-1})^3) for each λ ⊢ 3 at numerical q."""
    # Trivial (3): σ_i ↦ q,  σ_i⁻¹ ↦ 1/q
    chi_3 = (q * (1.0 / q)) ** 3  # = 1.0
    # Sign (1,1,1): σ_i ↦ -1/q,  σ_i⁻¹ ↦ -q
    chi_111 = ((-1.0 / q) * (-q)) ** 3  # = 1.0
    # Standard (2,1): trace of the 2×2 matrix product
    T_1, T_2, T_2_inv = hoefsmit_h3_at_q(q)
    M = np.eye(2)
    for op in [T_1, T_2_inv, T_1, T_2_inv, T_1, T_2_inv]:
        M = M @ op
    chi_21 = np.trace(M)
    return {"(3)": chi_3, "(2,1)": chi_21, "(1,1,1)": chi_111}


def markov_y_lambda_h3_from_witness():
    """Load canonical y_λ for H_3 at q_0 from
    `y-lambda-jones-markov-witness.json` (Wenzl-bridge, verified
    Σ y_λ·d_λ = 1)."""
    import json as _json
    with open(Path(__file__).parent / "y-lambda-jones-markov-witness.json") as f:
        W = _json.load(f)
    h3 = W["tables_by_n"]["3"]
    return {
        "(3)": next(w["y_lambda"] for w in h3["weights"] if w["partition"] == [3]),
        "(2,1)": next(w["y_lambda"] for w in h3["weights"] if w["partition"] == [2, 1]),
        "(1,1,1)": next(w["y_lambda"] for w in h3["weights"] if w["partition"] == [1, 1, 1]),
    }


def markov_y_lambda_h3(q: float):
    """y_λ at H_3, q_0.  The closed-form below is provisional; defers
    to the canonical witness when q matches q_0.

      Wenzl bridge convention (Jones-Markov):

      y_(3)     ≈  1 / (1 + z + z^2)   for some normalisation
      y_(2,1)   ≈  z   ... etc.

    Concretely, for H_3 we use the Hoefsmit-traced normalisation
    that satisfies tr_M(1) = 1 and tr_M(σ_i) = z:

      tr_M(σ_w) = Σ_λ y_λ(q) · χ_λ(σ_w)/dim_λ
    where dim_λ = χ_λ(1) = d_λ (1, 2, 1 for S_3).

    z(q) = 1 / (q^{1/2} + q^{-1/2}).  With the unit normalisation
    tr_M(1) = Σ_λ y_λ · 1 = 1 and the Markov condition
    tr_M(σ_w · σ_n) = z · tr_M(σ_w):

      y_(3)   = z^2 / (1+z+z^2)       ≈ small for q_0 close to 1
      y_(2,1) = z(1-z) / (1+z+z^2)
      y_(1,1,1) = (1-z)^2 / (1+z+z^2)

    These are the Jones-Markov "y_λ at H_3" satisfying
    Σ_λ y_λ d_λ = 1 (closure normalisation).
    """
    if abs(q - Q_0) < 1e-9:
        return markov_y_lambda_h3_from_witness()
    # Provisional fallback (NOT exact); use witness when possible.
    # The split z² + z(1-z) + (1-z)² = 1 already, so dividing by
    # (1 + z + z²) would BREAK the closure Σ d_λ y_λ = 1 with d_λ = (1, 2, 1).
    z = 1.0 / (np.sqrt(q) + 1.0 / np.sqrt(q))
    return {"(3)": z * z, "(2,1)": z * (1.0 - z),
            "(1,1,1)": (1.0 - z) ** 2}


def main():
    base = Path(__file__).parent
    # Constants pulled from module-level (Q_0, M_E, B_AME_3HE, M_AME_3HE,
    # G_CATALAN — single source of truth per CLAUDE.md guidance).

    print("══════════════════════════════════════════════════════════════════════")
    print("  Plan H — ρ(Z, N) Wedderburn-multiplicity experiment for ³He")
    print(f"  q_0 = {Q_0}, m_e = {M_E} MeV, B_AME(³He) = {B_AME_3HE} MeV")
    print("══════════════════════════════════════════════════════════════════════")

    # ─── 1. Per-block characters at q_0 ──────────────────────────
    chi = chi_partitions_at_borromean(Q_0)
    print("\n──── 1. χ_λ((σ_1 σ_2^{-1})^3) at q_0 ────")
    for k, v in chi.items():
        print(f"  λ = {k:<10}  χ = {v:+.10f}")

    # ─── 2. Wenzl-bridge y_λ ──────────────────────────────────────
    y = markov_y_lambda_h3(Q_0)
    print("\n──── 2. y_λ(q_0) (Wenzl bridge) ────")
    for k, v in y.items():
        print(f"  λ = {k:<10}  y = {v:+.10f}")
    # sanity: Σ_λ y_λ · d_λ = 1
    d = {"(3)": 1, "(2,1)": 2, "(1,1,1)": 1}
    sum_y_d = sum(y[k] * d[k] for k in y)
    print(f"  closure check Σ_λ y_λ·d_λ = {sum_y_d:.10f}  (expected 1)")

    # ─── 3. Markov trace tr_M(β) ──────────────────────────────────
    tr_M = sum(y[k] * chi[k] for k in y)
    print(f"\n──── 3. tr_M((σ_1 σ_2^{{-1}})^3)|_{{q=q_0}} = {tr_M:.10f}")

    # ─── 4. Hand-pick: B = ρ · m_e · Vol_hyp(K), ρ = 2, Vol = 8G ─
    # 8G ≈ 7.327724753417...  G_CATALAN sourced from mp.catalan
    # (module level) so all G usages stay in lock-step.
    vol_hyp = 8 * G_CATALAN
    rho_handpick = 2
    B_handpick = rho_handpick * M_E * vol_hyp
    err_handpick = (B_handpick - B_AME_3HE) / B_AME_3HE * 100
    print(f"\n──── 4. Hand-pick (current strategy) ────")
    print(f"  Vol_hyp(B_3) = 8G = {vol_hyp:.6f}")
    print(f"  B = ρ·m_e·Vol_hyp = {rho_handpick}·{M_E}·{vol_hyp:.6f} = {B_handpick:.6f} MeV")
    print(f"  err = {err_handpick:+.4f}% on binding")
    M_err_ppm_handpick = (B_handpick - B_AME_3HE) / M_AME_3HE * 1e6
    print(f"  M_err = {M_err_ppm_handpick:+.2f} ppm on total mass (witness reports +81 ppm)")

    # ─── 5. Candidate ρ formulas from Wedderburn data ────────────
    print("\n──── 5. Candidate ρ formulas (Plan H) ────")
    print(f"  (a) ρ = #blocks       = {len(chi)} = 3")
    print(f"  (b) ρ = Σ_λ d_λ        = {sum(d.values())} = 4 (regular rep dim)")
    print(f"  (c) ρ = Σ_λ d_λ²/|S_3|  = {sum(v*v for v in d.values())}/6 = 1.0")
    print(f"  (d) ρ = #PSD blocks at q_0 = 3 (all 3 blocks PSD per α*=1)")
    print(f"  (e) ρ from tr_M directly: B = m_e · ρ · tr_M(β)")
    if abs(tr_M) > 1e-12:
        rho_via_tr_M = B_AME_3HE / (M_E * tr_M)
        print(f"        ⇒ implied ρ = B_AME/(m_e·tr_M) = {rho_via_tr_M:.6f}")

    # Test each candidate
    print("\n──── 6. Each candidate's prediction ────")
    print(f"  {'candidate':<30s} {'ρ':>8s} {'B_pred (MeV)':>14s} {'err %':>8s} {'M_err (ppm)':>12s}")
    candidates = [
        ("hand-pick: ρ=2", 2),
        ("ρ = #blocks (3)", 3),
        ("ρ = Σ d_λ (4)", 4),
        ("ρ = Σ d_λ² / |S_3|", 1),
        ("ρ from tr_M·m_e match B_AME", B_AME_3HE / (M_E * tr_M) if abs(tr_M) > 1e-12 else float("nan")),
    ]
    for label, rho in candidates:
        B_pred = rho * M_E * vol_hyp if "tr_M" not in label else rho * M_E * tr_M
        err_pct = (B_pred - B_AME_3HE) / B_AME_3HE * 100
        M_err_ppm = (B_pred - B_AME_3HE) / M_AME_3HE * 1e6
        print(f"  {label:<30s} {rho:>8.4f} {B_pred:>14.6f} {err_pct:>+8.3f} {M_err_ppm:>+12.2f}")

    # ─── 7. The "8G" decomposition itself (post-Archimedean naming) ──
    print("\n──── 7. Post-Archimedean naming check ────")
    print(f"  Vol_hyp(B_3) via mpmath catalan: 8G = {float(8*mp.catalan):.10f}")
    print(f"  tr_M(β)|_{{q=q_0}} numerical:     {tr_M:.10f}")
    ratio = vol_hyp / tr_M if abs(tr_M) > 1e-12 else float("nan")
    print(f"  ratio Vol_hyp / tr_M           = {ratio:.6f}")
    print(f"  (volume conjecture: only equal asymptotically at roots of unity)")

    # ─── Honest finding ───────────────────────────────────────────
    print("\n──── Finding ────")
    rho_implied = B_AME_3HE / (M_E * vol_hyp)
    delta = rho_implied - 2
    print(f"  Implied ρ for B = ρ·m_e·Vol_hyp to hit B_AME exactly: {rho_implied:.6f}")
    print(f"  Hand-pick ρ=2 has δ = {delta:+.6f} = {delta * 1000:.2f} ‰")
    print(f"  This δ ≈ 0.061 does NOT match a simple Wedderburn-multiplicity formula:")
    print(f"    Σ d_λ = 4, Σ d_λ² = 6, #blocks = 3 — none yield ρ=2.062")
    print(f"  δ ≈ 0.061 is a higher-order substrate-q correction beyond")
    print(f"  block-multiplicity counting; closing it likely needs:")
    print(f"   (a) Wenzl-bridge tower correction at q_0 (depth-2 in y_λ)")
    print(f"   (b) Volume-conjecture asymptotic deviation at non-root-of-unity q_0")
    print(f"   (c) α_λ stratum-level corrections (R5-full open item)")
    print()
    print(f"  Plan H's hypothesis as currently stated (ρ = simple Wedderburn integer)")
    print(f"  is INSUFFICIENT to close the +81 ppm ³He gap.  The structural ρ=2 is")
    print(f"  the dominant integer contribution; the +3% correction is non-trivial.")

    # ─── Emit witness ─────────────────────────────────────────────
    out_path = base / "rho-3he-wedderburn-experiment.witness.json"
    witness = {
        "computation": "rho-3he-wedderburn-experiment",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Plan H — ρ(Z,N) Wedderburn-multiplicity experiment for ³He.  "
            "Computes χ_λ, y_λ, tr_M for the Borromean braid (σ_1 σ_2^{-1})^3 "
            "and tests several candidate ρ formulas against the +81 ppm hand-pick gap."
        ),
        "q_0": Q_0,
        "m_e_MeV": M_E,
        "B_AME_MeV": B_AME_3HE,
        "characters_at_q0": {k: float(v) for k, v in chi.items()},
        "y_lambda_at_q0": {k: float(v) for k, v in y.items()},
        "markov_trace": float(tr_M),
        "vol_hyp_8G": vol_hyp,
        "hand_pick": {"rho": 2, "B_pred_MeV": B_handpick,
                      "err_pct": err_handpick, "M_err_ppm": M_err_ppm_handpick},
        "candidates": [
            {
                "label": label,
                "rho": float(rho),
                "B_pred_MeV": float(
                    rho * M_E * (tr_M if "tr_M" in label else vol_hyp)
                ),
                "err_pct": float(
                    ((rho * M_E * (tr_M if "tr_M" in label else vol_hyp))
                     - B_AME_3HE) / B_AME_3HE * 100
                ),
                "M_err_ppm": float(
                    ((rho * M_E * (tr_M if "tr_M" in label else vol_hyp))
                     - B_AME_3HE) / M_AME_3HE * 1e6
                ),
            }
            for label, rho in candidates
        ],
    }
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"\n→ wrote {out_path}")


if __name__ == "__main__":
    main()
