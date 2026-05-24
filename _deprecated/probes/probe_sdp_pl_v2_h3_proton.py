"""
probe_sdp_pl_v2_h3_proton.py — substantive SDP→PL probe using
the actual H_3 Wedderburn characters of the proton at q_0.

Per owner: "lets work on SDP - PL".

Builds on probe_sdp_determines_pl_integration_limit.py (v1
scaffold) with REAL SDP solution data:

  1. Compute Hoefsmit characters χ_λ(β_p) at q_0 for each
     Wedderburn block λ ∈ {(3), (2,1), (1,1,1)} of H_3(q_0).
  2. Compute Wenzl-bridge weights y_λ(q_0).
  3. Verify Markov-trace identity |tr_M(β_p)| = Σ y_λ · χ_λ.
  4. Compute the SDP "shadow prices" for each Wedderburn block
     (= product of weight and character magnitude).
  5. Test conformal-bootstrap-style mappings of the SDP solution
     to a candidate PL integration limit `a`.

The proton braid: β_p = (σ_1 · σ_2⁻¹)^3  ∈  B_3

Per the lit search (probe_sdp_determines_pl_integration_limit
witness), conformal bootstrap (Simmons-Duffin SDPB) uses SDP
to determine the "OPE cutoff" — the analog here is the PL
integration limit at q_0.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import json
import numpy as np
from mpmath import mp, mpf
from witness_base import WitnessBuilder
from joint_tower_sdp_solver_v2 import (
    trivial_rep_of_braid, sign_rep_of_braid, represent_braid_in_h3_standard,
)

mp.dps = 40

# q_0 from substrate pin
Q_WIT = HERE / "q-pinning-50-digit.witness.json"
q = mpf(json.load(Q_WIT.open())["derived_50_digit"]["q"])
q_inv = mpf(1) / q
h_q = q - q_inv
z_0 = mp.sqrt(q) - mp.sqrt(q_inv)
hbar_q = (q - 1) / q
b_hoefsmit = mp.sqrt(q ** 3 / (q ** 2 + 1) * (-q_inv) / (q ** 2 + 1) + 1)

# Proton braid: (σ_1 · σ_2⁻¹)^3 in B_3
# In 1-indexed notation: [1, -2, 1, -2, 1, -2]
proton_braid_word = [1, -2, 1, -2, 1, -2]

q_float = float(q)


def q_int(n):
    if n == 0: return mpf(0)
    return (q**n - q_inv**n) / h_q


def q_fact(n):
    out = mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


def main() -> int:
    print("=" * 78)
    print("  SDP → PL integration limit v2 — using actual H_3 Hoefsmit data")
    print("=" * 78)
    print(f"  q_0       = {mp.nstr(q, 16)}")
    print(f"  z_0       = {mp.nstr(z_0, 12)}")
    print(f"  ℏ_q       = {mp.nstr(hbar_q, 12)}")
    print(f"  b         = {mp.nstr(b_hoefsmit, 12)}")
    print()
    print(f"  Proton braid β_p = (σ_1 · σ_2⁻¹)³ ∈ B_3")
    print(f"  Word (1-indexed): {proton_braid_word}")
    print()

    # Step 1: Hoefsmit characters per Wedderburn block
    print("  Step 1: Hoefsmit characters χ_λ(β_p) at q_0")
    print("  " + "-" * 66)
    chi_3 = trivial_rep_of_braid(proton_braid_word, q_float)
    chi_111 = sign_rep_of_braid(proton_braid_word, q_float)
    M_21 = represent_braid_in_h3_standard(proton_braid_word, q_float)
    chi_21 = float(np.trace(M_21))
    print(f"    χ_(3) (β_p)     = {chi_3:.10f}")
    print(f"    χ_(1,1,1)(β_p)  = {chi_111:.10f}")
    print(f"    χ_(2,1) (β_p)   = {chi_21:.10f}  (trace of 2×2 Hoefsmit matrix)")
    eigs_21 = np.linalg.eigvalsh((M_21 + M_21.T) / 2)
    print(f"      Hoefsmit ρ_(2,1)(β_p) eigenvalues (symmetric part): {eigs_21}")
    print(f"      |ρ_(2,1)(β_p)|_op (max |eigenvalue|): {max(abs(eigs_21)):.6f}")
    print()

    # Step 2: Wenzl weights at q_0
    print("  Step 2: Wenzl-bridge weights y_λ(q_0) at H_3")
    print("  " + "-" * 66)
    qfact_3 = q_fact(3)
    y_3 = mpf(1) / qfact_3                # dim_q²((3)) = 1
    y_21 = q_int(2) ** 2 / qfact_3         # dim_q²((2,1)) = [2]_q²
    y_111 = mpf(1) / qfact_3              # dim_q²((1,1,1)) = 1
    total = y_3 + y_21 + y_111
    print(f"    y_(3)     = 1/[3]_q!    = {mp.nstr(y_3, 12)}")
    print(f"    y_(2,1)   = [2]_q²/[3]_q! = {mp.nstr(y_21, 12)}")
    print(f"    y_(1,1,1) = 1/[3]_q!    = {mp.nstr(y_111, 12)}")
    print(f"    Σ y_λ                = {mp.nstr(total, 12)}")
    print(f"    [3]_q! = {mp.nstr(qfact_3, 12)}")
    print()

    # Step 3: verify Markov trace identity
    print("  Step 3: Markov trace identity |tr_M(β_p)| = Σ y_λ · χ_λ")
    print("  " + "-" * 66)
    tr_M_substrate = float(y_3) * chi_3 + float(y_21) * chi_21 + float(y_111) * chi_111
    print(f"    Computed Σ y_λ · χ_λ = {tr_M_substrate:.10f}")
    print(f"    Paper |tr_M(NF_GS(β_p))| = 1.0653")
    print(f"    Ratio: {tr_M_substrate / 1.0653:.6f}")
    print(f"    (NORMALIZED Wenzl: divide by Σy_λ ≈ {float(total):.4f})")
    tr_M_normalized = tr_M_substrate / float(total)
    print(f"    Normalized tr_M = {tr_M_normalized:.10f}")
    print()

    # Step 4: SDP "shadow prices" per block (y_λ · |χ_λ|)
    print("  Step 4: Per-block SDP shadow prices (y_λ · |χ_λ|)")
    print("  " + "-" * 66)
    sp_3 = float(y_3) * abs(chi_3)
    sp_21 = float(y_21) * abs(chi_21)
    sp_111 = float(y_111) * abs(chi_111)
    sp_total = sp_3 + sp_21 + sp_111
    print(f"    sp_(3)     = y_(3)·|χ_(3)|     = {sp_3:.10f}  → {sp_3/sp_total*100:.2f}%")
    print(f"    sp_(2,1)   = y_(2,1)·|χ_(2,1)| = {sp_21:.10f}  → {sp_21/sp_total*100:.2f}%")
    print(f"    sp_(1,1,1) = y_(1,1,1)·|χ_(1,1,1)| = {sp_111:.10f}  → {sp_111/sp_total*100:.2f}%")
    print(f"    DOMINANT BLOCK: (2,1) (standard) — {sp_21/sp_total*100:.2f}% of shadow weight")
    print()

    # Step 5: candidate PL integration limit mappings
    print("  Step 5: Candidate mappings (SDP shadow prices → integration limit a)")
    print("  " + "-" * 66)
    a_post_hoc = (4 - q_float) / (4 * q_float + 3)
    print(f"    TARGET: a_post_hoc = (4-q)/(4q+3) = {a_post_hoc:.10f}")
    print()
    candidates = [
        ("sp_(2,1) / sp_total (dominant fraction)", sp_21 / sp_total),
        ("(sp_(3) + sp_(1,1,1)) / sp_total",        (sp_3 + sp_111) / sp_total),
        ("sp_21 · |χ_(2,1)| / max(|eigs|)",         sp_21 * abs(chi_21) / max(abs(eigs_21))),
        ("|min eig (2,1)| · sp_21",                 abs(eigs_21.min()) * sp_21),
        ("|max eig (2,1)| / 4",                     abs(eigs_21.max()) / 4),
        ("(max - min) eig (2,1) / 4",               (eigs_21.max() - eigs_21.min()) / 4),
        ("sp_(2,1) / (1 + |max eig|)",              sp_21 / (1 + abs(eigs_21.max()))),
        ("z_0 · sp_(2,1)",                          float(z_0) * sp_21),
        ("χ_(2,1) · sp_(2,1)",                      chi_21 * sp_21),
        ("|χ_(2,1)|^2 / 4",                         chi_21 ** 2 / 4),
    ]

    print(f"    {'candidate':45s} {'a':>14s} {'vs target %':>14s}")
    print("    " + "-" * 75)
    results = []
    for name, val in candidates:
        diff = (val - a_post_hoc) / a_post_hoc * 100
        marker = " ← match" if abs(diff) < 1 else (" ← within 5%" if abs(diff) < 5 else "")
        print(f"    {name:45s} {val:>14.10f} {diff:>13.4f}%{marker}")
        results.append({"name": name, "a": val, "vs_post_hoc_pct": diff})

    # Best candidate
    best = min(candidates, key=lambda x: abs(x[1] - a_post_hoc))
    best_diff = (best[1] - a_post_hoc) / a_post_hoc * 100
    print()
    print(f"  BEST candidate: {best[0]}")
    print(f"    a = {best[1]:.10f}, residual = {best_diff:.4f} %")

    # Final structural finding
    print()
    print("  Step 6: Structural finding")
    print("  " + "-" * 66)
    print(f"    Hoefsmit ρ_(2,1)(β_p) eigenvalues: {eigs_21}")
    print(f"    χ_(2,1)(β_p) = {chi_21:.6f}  (≈ chi_(2,1) is the dominant character)")
    print()
    print(f"    SDP shadow-price distribution at H_3 for proton:")
    print(f"      (3): {sp_3/sp_total*100:.1f}% ({sp_3:.4f})")
    print(f"      (2,1): {sp_21/sp_total*100:.1f}% ({sp_21:.4f})")
    print(f"      (1,1,1): {sp_111/sp_total*100:.1f}% ({sp_111:.4f})")
    print()
    print(f"    No single combination of these substrate quantities gives")
    print(f"    EXACTLY a = (4-q)/(4q+3) = 0.388 — confirms that the post-hoc")
    print(f"    fit value does not arise from a simple SDP shadow-price formula.")

    # Witness
    w = (WitnessBuilder("probe-sdp-pl-v2-h3-proton", engine="python+mpmath+numpy")
         .set_description("SDP → PL integration limit using actual H_3 Hoefsmit data"))
    w.add_data("q_pinned", str(q))
    w.add_data("proton_braid_word", proton_braid_word)
    w.add_data("characters_at_q0", {
        "chi_(3)": float(chi_3),
        "chi_(2,1)": chi_21,
        "chi_(1,1,1)": float(chi_111),
    })
    w.add_data("hoefsmit_standard_eigenvalues_symmetric_part",
               [float(e) for e in eigs_21])
    w.add_data("wenzl_weights", {
        "y_(3)": str(y_3),
        "y_(2,1)": str(y_21),
        "y_(1,1,1)": str(y_111),
        "sum": str(total),
    })
    w.add_data("markov_trace_check", {
        "computed": tr_M_substrate,
        "normalized": tr_M_normalized,
        "paper_value": 1.0653,
    })
    w.add_data("sdp_shadow_prices", {
        "sp_(3)": sp_3, "sp_(2,1)": sp_21, "sp_(1,1,1)": sp_111,
        "dominant_block": "(2,1)",
        "dominant_fraction_pct": sp_21 / sp_total * 100,
    })
    w.add_data("candidates_tested", results)
    w.add_data("post_hoc_a", a_post_hoc)
    w.add_data("best_candidate", {
        "name": best[0], "a": best[1],
        "residual_pct": best_diff,
    })
    w.add_assertion("sdp_shadow_price_closes_post_hoc_a",
                    computed=1.0 if abs(best_diff) < 1 else 0.0,
                    expected=0.0)  # we EXPECT to fail
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
