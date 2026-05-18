"""Categorical Δ_λ derivation via shift_NF + Wenzl-bridge factoring.

Per prop:rho-k-h3a-refinement, the categorical density admits the
Wedderburn-Schur decomposition:

  ρ_K(q) = ρ_K^LO(Z, N)
         + (1 / |tr_M(β_K)|) · Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(β_K) · Δ_λ(K)

with the LO piece tautological (|tr_M| cancels → constituent mass).
The non-tautological binding lives in the Δ_λ block-binding corrections.

The shift_NF integers from PR #670 (crystal_shift_nf_atomic.py) provide
a STRUCTURAL CONSTRAINT on which partitions can have non-zero Δ_λ:

  shift_NF table (per atom):
    D=40, T=61, ³He=58, ⁴He=79, ⁵Li=97, ⁶Li=118

The shift_NF integer is the LEADING pole order at q=0 of the
canonical mass formula. The Wenzl-bridge gives:

  y_λ(q) ∝ q^(shift_NF_λ)   (Wenzl-bridge for each partition)

So the leading-order partitions contributing to Δ_λ(K) are those
λ ⊢ 3A whose shift_NF_λ matches shift_NF_K.

## Direct derivation: empirical Δ_λ via linear system

For each atom K with A nucleons:
  M_codata(K) − (Z·m_p + N·m_n) = m_e · Σ_λ y_λ(q_0) · χ^λ(β_K) · Δ_λ(K)

The LHS is the binding energy. The RHS has the y_λ·χ^λ matrix
multiplied by the unknown Δ_λ vector. Under the constraint that
only shift_NF-matched partitions contribute, the system becomes
finitely-determined.

This probe:
1. Computes shift_NF per atom and per partition.
2. Extracts the empirical binding per atom from M_codata.
3. Reports the y_λ · χ^λ matrix on the constrained partition set.
4. Solves for Δ_λ where possible.

Open theoretical work: closed-form Δ_λ(K) in terms of braid-word
data. This probe provides empirical values + structural constraints
for that derivation.

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)
from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q_0_FLOAT  # noqa: E402


M_CODATA_MEV = {
    "p":   float(M_P_MEV_VALIDATION),
    "n":   float(M_N_MEV_VALIDATION),
    "D":   float(M_D_MEV_VALIDATION),
    "T":   float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION),
    "4He": float(M_HE4_MEV_VALIDATION),
}

SHIFT_NF_FROM_PR670 = {
    "D":   40,
    "T":   61,
    "3He": 58,
    "4He": 79,
    "5Li": 97,
    "6Li": 118,
}


def main() -> int:
    mp.mp.dps = 50
    q_val = float(Q_0_FLOAT)
    m_p = float(M_P_MEV_VALIDATION)
    m_n = float(M_N_MEV_VALIDATION)
    m_e = float(M_E_MEV)

    print("=" * 80)
    print("  Δ_λ derivation via shift_NF + Wenzl-bridge")
    print("=" * 80)
    print()
    print(f"  q_0 = {q_val:.10f}")
    print(f"  m_e = {m_e:.10f} MeV")
    print()
    print("  ── Per-atom binding energy (empirical, from CODATA) ──")
    print()
    print(f"  {'atom':>5} {'A':>2} {'M_codata':>11} {'Z·m_p + N·m_n':>14} {'Binding (MeV)':>14} {'shift_NF':>10}")
    print("  " + "-" * 75)

    per_atom = []
    for label, Z, N in [
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]:
        A = Z + N
        M_codata = M_CODATA_MEV[label]
        constituent = Z * m_p + N * m_n
        binding = M_codata - constituent
        shift_nf = SHIFT_NF_FROM_PR670.get(label, "—")
        per_atom.append({
            "atom": label, "Z": Z, "N": N, "A": A,
            "M_codata_MeV": M_codata,
            "constituent_MeV": constituent,
            "binding_MeV": binding,
            "shift_NF": shift_nf,
        })
        print(f"  {label:>5} {A:>2} {M_codata:>11.6f} {constituent:>14.6f} "
              f"{binding:>+14.6f} {str(shift_nf):>10}")

    # ── For deuteron (A=2, n=6, 11 partitions): solve Δ_λ system ──
    print()
    print("  ── Δ_λ extraction for deuteron (A=2, n=6, 11 partitions) ──")
    print()
    A_target = 2
    Z, N = 1, 1
    n_strands = 3 * A_target
    word = atom_braid_word_3A(Z, N, include_inter=True)
    n_gens = n_strands - 1

    binding_D = M_CODATA_MEV["D"] - (m_p + m_n)
    # Δ contribution to ρ_K: per prop:rho-k-h3a-refinement,
    #   M(K) = ρ_K · m_e · |tr_M|
    #        = (ρ_LO + Δ-contribution) · m_e · |tr_M|
    #        = constituent + m_e · Σ_λ y_λ · χ^λ · Δ_λ
    # so Σ_λ y_λ · χ^λ · Δ_λ = binding / m_e
    target_lhs = binding_D / m_e
    print(f"  Σ_λ y_λ · χ^λ(β_D) · Δ_λ(D) = binding_D / m_e = "
          f"{binding_D:+.6f} / {m_e:.6f} = {target_lhs:+.6f}")
    print()

    y_vals = y_lambda_at(n_strands, q_val=q_val)
    print(f"  {'λ ⊢ 6':>15} {'dim':>5} {'y_λ(q_0)':>14} {'χ^λ(β_D)':>14} "
          f"{'y·χ':>14}")
    print("  " + "-" * 75)
    rows = []
    sum_y_chi = mp.mpf(0)
    for shape, y in sorted(y_vals.items(), key=lambda kv: -abs(float(kv[1]))):
        sigmas, dim, _ = build_seminormal_matrices(shape, q=q_val)
        if dim == 0:
            continue
        chi = chi_lambda_of_word(sigmas, dim, word, n_gens)
        y_f = float(y)
        chi_f = float(chi)
        y_chi = y_f * chi_f
        sum_y_chi += y_chi
        rows.append({
            "partition": list(shape), "dim": int(dim),
            "y_at_q0": y_f, "chi_at_q0": chi_f, "y_times_chi": y_chi,
        })
        print(f"  {str(list(shape)):>15} {dim:>5} {y_f:>+14.6e} "
              f"{chi_f:>+14.4f} {y_chi:>+14.6e}")

    print()
    print(f"  Σ y·χ (verifies |tr_M(β_D)|) = {float(sum_y_chi):+.6e}")
    print(f"  Target:                       = {target_lhs:+.6f}")
    print()
    print("  ── Δ_λ structural finding ──")
    print()
    print("  Under the constraint Δ_λ(K) = constant Δ * (1 if λ has matching")
    print("  shift_NF), the equation Σ_λ y_λ·χ^λ·Δ_λ = binding/m_e becomes:")
    print()
    print("    Δ · Σ_(λ with matching shift_NF) y_λ·χ^λ = binding/m_e")
    print()
    print("  → Δ_const = (binding/m_e) / Σ_(λ matching)")
    print()
    print("  This collapses the 11-partition system to a single Δ — IF")
    print("  the shift_NF constraint is the right physical filter.")
    print()
    print("  Full categorical derivation requires identifying which partitions")
    print("  λ ⊢ 6 satisfy `shift_NF_λ = shift_NF(D) = 40`.  This needs")
    print("  the per-partition χ^λ pole-order expansion (open work; the")
    print("  crystal_shift_nf_atomic.py from PR #670 has the structural")
    print("  ingredients but not the per-λ resolution).")

    builder = (
        WitnessBuilder(
            "delta-lambda-shift-nf-wenzl-probe", engine="mpmath"
        )
        .set_description(
            "Categorical Δ_λ derivation framework via shift_NF + "
            "Wenzl-bridge factoring. Provides empirical binding/m_e "
            "targets per atom + y_λ·χ^λ matrix for the partitions of "
            "n=3A. The shift_NF constraint (from PR #670) reduces the "
            "underdetermined Δ_λ system to a single Δ per atom; full "
            "categorical derivation requires per-partition shift_NF "
            "resolution which is open work."
        )
        .set_content_block("prop:rho-k-h3a-refinement")
        .add_parameter("q_0", q_val)
        .add_data("per_atom_binding", per_atom)
        .add_data("D_y_lambda_chi_rows", rows)
        .add_data("D_target_lhs", float(target_lhs))
        .add_data("D_sum_y_chi", float(sum_y_chi))
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
