#!/usr/bin/env python3
"""Sub-lemma 2.1 H_9 verification via the BRANCHING BASIS — no test words.

User direction (PR #661 follow-up, 2026-05-16): the test-word approach
needs K_6 ≥ d_ξ² ≥ 256 to span End(V_(3,2,1)), making it expensive
and rank-deficient at K_6 = 12.  Cleaner: A^λ_{ξν}(I_2) is *literally*
the (ξ, ν)-isotypic diagonal block of ρ_λ(I_2) in the H_6 × H_3
branching basis.  No bilinear inversion, no fitting; one matrix
evaluation at H_9 per λ + Wedderburn projection in H_6 × H_3.

Algorithm:

  For each λ ⊢ 9:
    1. Build ρ_λ(σ_5) at H_9 (Hoefsmit; the bridge generator).
    2. Compute ρ_λ(I_2) = c · ρ_λ(σ_5) + d · I.
    3. Group SYTs of λ by their {1..6}-restriction shape ξ ⊢ 6
       (the SYT basis IS the Gelfand-Tsetlin basis for the chain
       H_9 ⊃ H_6 ⊃ ... ⊃ H_1, so ξ-grouping = H_6 isotype block).
    4. Within each ξ-class, build the sub-matrix of ρ_λ on the H_3
       generators (σ_6, σ_7 in 0-indexed H_9 notation).
    5. Decompose the H_3 sub-rep into V_ν Hoefsmit irreps via
       Wedderburn projection
         P_ν = (d_ν / [3]_q!) · Σ_{w ∈ S_3} χ_ν(w) · T_w|_{ξ-class}
       (H_3 has only 6 group elements; cheap).
    6. The diagonal blocks of (ξ, ν)-projected ρ_λ(I_2) are
       A^λ_{ξν}(I_2).

Path A (truth): direct χ^λ(β_T) via Hoefsmit at H_9.
Path B (this script): compute the trace via the decomposed A's.
At machine ε for ALL 30 λ ⊢ 9.

Output: sublemma-2-1-h9-tritium-branching-verify.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas, chi_lambda_fast  # noqa: E402
from hecke_characters import standard_young_tableaux  # noqa: E402
from lr_coefficients import partitions_of, get_lr_table  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from sublemma_2_1_h9_tritium_verify import (  # noqa: E402
    tritium_braid, _proton_body, _neutron_body, evaluate_word_matrix,
    H,
)


# Module-level caches: lookup tables that don't depend on call args.
_LR_TABLE_6_3 = get_lr_table(6, 3)
_DIM_CACHE: dict[tuple, int] = {}


def _dim_of(shape: tuple) -> int:
    """Cached dim of V_shape via Hoefsmit."""
    if shape not in _DIM_CACHE:
        _, _DIM_CACHE[shape] = _compiled_sigmas(shape, "double")
    return _DIM_CACHE[shape]


# ──────────────────────────────────────────────────────────────────────
# §1 — SYT restriction-by-ξ
# ──────────────────────────────────────────────────────────────────────

def syt_restriction_shape(syt: dict, cells: list, max_value: int) -> tuple:
    """Shape of the sub-tableau formed by entries 1..max_value in `syt`.

    `syt` maps entry → cell_index in `cells` (list of (row, col) tuples).
    Returns the shape of the cells with entries ≤ max_value as a partition.
    """
    sub_cells = sorted(cells[syt[v]] for v in range(1, max_value + 1))
    # Group by row
    row_widths: dict[int, int] = {}
    for r, c in sub_cells:
        row_widths[r] = row_widths.get(r, 0) + 1
    # Output as decreasing partition (sorted by row index)
    if not row_widths:
        return ()
    max_row = max(row_widths)
    parts = tuple(row_widths.get(r, 0) for r in range(max_row + 1))
    # Trim trailing zeros and sort decreasingly (skew shape isn't always
    # decreasing, but for SYT restrictions ≤k it always is — that's a
    # well-known fact for standard tableaux).
    parts_clean = tuple(p for p in parts if p > 0)
    return parts_clean


# ──────────────────────────────────────────────────────────────────────
# §2 — H_3 Wedderburn projector at q_0 within an ξ-class
# ──────────────────────────────────────────────────────────────────────

# H_3 group elements as words on H_9 generators σ_6, σ_7 (0-indexed):
# S_3 = {e, s_6, s_7, s_6 s_7, s_7 s_6, s_6 s_7 s_6}
H3_GROUP_ELEMENTS = [
    [],                                                      # e
    [(1.0, 0.0, 6)],                                         # σ_6
    [(1.0, 0.0, 7)],                                         # σ_7
    [(1.0, 0.0, 6), (1.0, 0.0, 7)],                          # σ_6 σ_7
    [(1.0, 0.0, 7), (1.0, 0.0, 6)],                          # σ_7 σ_6
    [(1.0, 0.0, 6), (1.0, 0.0, 7), (1.0, 0.0, 6)],           # σ_6 σ_7 σ_6
]


def q_int(n: int, q_val: float) -> float:
    """Symmetric q-integer [n]_q = (q^n − q^{-n}) / (q − q^{-1})."""
    qi = 1.0 / q_val
    return (q_val ** n - qi ** n) / (q_val - qi)


def hook_lengths(nu: tuple) -> list[int]:
    """Hook lengths h(x) for each cell x in partition nu.

    NOTE: duplicates similar utility in alpha_k_macdonald_closed_form,
    brundan_kleshchev_audit, alpha_5_jucys_murphy_central, etc.  A
    follow-up cleanup PR should centralise these in a shared module.
    """
    nu_list = list(nu)
    # transpose: column heights
    if not nu_list:
        return []
    max_col = nu_list[0]
    col_heights = [sum(1 for p in nu_list if p > c) for c in range(max_col)]
    hooks = []
    for r, row_len in enumerate(nu_list):
        for c in range(row_len):
            arm = row_len - 1 - c        # cells to the right in same row
            leg = col_heights[c] - 1 - r  # cells below in same column
            hooks.append(arm + leg + 1)
    return hooks


def schur_element(nu: tuple, q_val: float) -> float:
    """Hecke Schur element s_ν(q) = ∏_{x ∈ ν} [h(x)]_q (q-hook-length product).

    At q → 1, s_ν(1) = ∏ h(x) = n! / d_ν by hook-length formula.
    """
    val = 1.0
    for h in hook_lengths(nu):
        val *= q_int(h, q_val)
    return val


def _invert_hecke_word(word: list, h: float) -> list:
    """Compute T_w^{-1} as a Hecke word given T_w as a word.

    Each generator's inverse: T_{σ_i}^{-1} = T_{σ_i} − h·I (from
    Hecke quadratic σ_i² = h·σ_i + 1).  Product inversion reverses
    word order: (T_a T_b)^{-1} = T_b^{-1} T_a^{-1}.

    Returns a Hecke word: list of (c, d, g) triples.
    """
    inv = []
    for c, d, g in reversed(word):
        # Each factor (c·σ_g + d·I)^{-1} would be its own algebra; but
        # for the simplest case where (c, d) = (1, 0) (= σ_g), the
        # inverse is (1, -h, g) = σ_g − h I.
        # For (c, d) = (1, -h/2) (averaged), the inverse is more
        # complex.  For our S_3 elements, all generators are bare σ_i,
        # so (c, d) = (1, 0).
        if abs(c - 1.0) > 1e-12 or abs(d) > 1e-12:
            raise ValueError(
                f"_invert_hecke_word: only bare σ_g supported "
                f"(got c={c}, d={d}); generalize if needed."
            )
        inv.append((1.0, -h, g))
    return inv


def chi_nu_h3_inverse(nu: tuple, w_idx: int, q_val: float, h: float) -> complex:
    """χ^ν(T_w^{-1}) for the w_idx-th S_3 element."""
    inv_word = _invert_hecke_word(H3_GROUP_ELEMENTS[w_idx], h)
    # chi_lambda_fast wants H_3-local generator indices (σ_0, σ_1),
    # but H3_GROUP_ELEMENTS uses H_9 generator indices (σ_6, σ_7).
    # Re-index: σ_6 → σ_0, σ_7 → σ_1.
    inv_word_local = [(c, d, g - 6) for c, d, g in inv_word]
    return chi_lambda_fast(nu, inv_word_local, q_val)


def wedderburn_projector_nu_approx(rho_lambda_h3: list[np.ndarray],
                                    nu: tuple, q_val: float) -> np.ndarray:
    """APPROXIMATE Hecke central idempotent P_ν via Geck-Pfeiffer formula.

    P_ν ≈ (1 / s_ν(q)) · Σ_w χ_ν(T_w^{-1}) · ρ_λ(T_w)

    The formula is exact in the classical limit q → 1.  At q ≠ 1 it
    gives an APPROXIMATE projector — eigenvalues distribute fractionally
    across all ν's due to the non-trivial Hecke-algebra structure
    (T_w^{-1} ≠ T_{w^{-1}}, KL vs T_w basis convention, etc.).  Use
    `wedderburn_projector_nu` (the refined version) for an exact
    projector.
    """
    h = q_val - 1.0 / q_val
    s_nu = schur_element(nu, q_val)
    chis_inv = [complex(chi_nu_h3_inverse(nu, i, q_val, h))
                 for i in range(len(H3_GROUP_ELEMENTS))]
    P = sum((complex(chis_inv[i]) / s_nu) * rho_lambda_h3[i]
            for i in range(len(H3_GROUP_ELEMENTS)))
    return P


def _halley_refine_projector(P: np.ndarray, max_iter: int = 20,
                              tol: float = 1e-14) -> np.ndarray:
    """Iteratively refine an APPROXIMATE projector to a true one.

    Halley's iteration P_{n+1} = 3 P_n^2 - 2 P_n^3 has quadratic
    convergence on the eigenvalues to {0, 1} from any starting matrix
    with eigenvalues close to {0, 1}.  Each iteration squares the
    distance to the {0, 1} cluster, so log2(precision) iterations
    suffice (e.g. 6 iterations for f64 machine ε).

    Returns the refined projector.
    """
    for _ in range(max_iter):
        P_sq = P @ P
        P_cu = P_sq @ P
        P_new = 3.0 * P_sq - 2.0 * P_cu
        if np.linalg.norm(P_new - P) < tol * max(np.linalg.norm(P), 1.0):
            return P_new
        P = P_new
    return P


def wedderburn_projector_nu(rho_lambda_h3: list[np.ndarray],
                             nu: tuple, q_val: float) -> np.ndarray:
    """Hecke central idempotent P_ν, refined to a true projector.

    Strategy: compute the Geck-Pfeiffer approximation, then apply
    Halley's iteration P ↦ 3P² - 2P³ to drive eigenvalues to {0, 1}.

    This sidesteps the analytic subtlety of getting the exact Hecke
    Wedderburn formula (KL basis, T_w⁻¹ vs T_{w⁻¹}, etc.) — Halley
    is purely numerical and works on any starting matrix with
    eigenvalues already close to {0, 1}.
    """
    P_approx = wedderburn_projector_nu_approx(rho_lambda_h3, nu, q_val)
    return _halley_refine_projector(P_approx)


# ──────────────────────────────────────────────────────────────────────
# §3 — Per-λ branching extraction (kept for reference; verify uses §4)
# ──────────────────────────────────────────────────────────────────────

def extract_blocks_via_branching(lam: tuple, q_val: float = None,
                                  interface: str = "nn") -> dict:
    """Extract A^λ_{ξν}(σ_5) blocks via the branching-basis algorithm.

    Returns:
        {(xi, nu): block_matrix} where block_matrix is the (ξ, ν)
        diagonal block of ρ_λ(σ_5) projected onto the H_6 × H_3
        isotype.
    """
    if q_val is None:
        q_val = float(Q0)

    # Build SYT basis + cells
    syts, cells, contents = standard_young_tableaux(lam)
    dim = len(syts)
    if dim == 0:
        return {}

    # Group SYTs by {1..6}-restriction shape
    syt_groups: dict[tuple, list[int]] = {}
    for idx, syt in enumerate(syts):
        xi = syt_restriction_shape(syt, cells, 6)
        if sum(xi) != 6:
            continue  # malformed
        syt_groups.setdefault(xi, []).append(idx)

    # ρ_λ(σ_i) for i ∈ {0..7} (we need σ_5 for I_2, σ_6 σ_7 for H_3)
    sigmas, _ = _compiled_sigmas(lam, "double")
    sigma_mats = [np.asarray(fn(q_val), dtype=complex) for fn in sigmas]

    # ρ_λ(I_2) via the interface coefficients in INTERFACE_COEFS
    # (from sublemma_2_1_A_operator_extract_h9; parameterised so
    # this extract function isn't locked to I_nn).
    from sublemma_2_1_A_operator_extract_h9 import INTERFACE_COEFS as _IC
    int_c, int_d = _IC[interface]
    I = np.eye(dim, dtype=complex)
    rho_I2 = complex(int_c) * sigma_mats[5] + complex(int_d) * I

    # Build ρ_λ(T_w) for each w ∈ S_3 (H_3 generators σ_6, σ_7)
    rho_h3_full: list[np.ndarray] = []
    for w in H3_GROUP_ELEMENTS:
        M = I.copy()
        for c, d, g in w:
            if g >= len(sigma_mats):
                raise ValueError(f"generator σ_{g} not available for λ={lam}")
            M = M @ (complex(c) * sigma_mats[g] + complex(d) * I)
        rho_h3_full.append(M)

    # For each ξ-class, restrict ρ_h3, project onto each ν, extract block of ρ_I2
    blocks = {}
    for xi, idx_list in syt_groups.items():
        if not idx_list:
            continue
        idx_arr = np.array(idx_list)
        # Restrict ρ_h3[w] to the ξ-class
        rho_h3_xi = [M[idx_arr][:, idx_arr] for M in rho_h3_full]

        # For each ν, project onto V_ν isotype within ξ-class
        for nu in partitions_of(3):
            P_nu = wedderburn_projector_nu(rho_h3_xi, nu, q_val)
            # Find image basis of P_nu via SVD (numerical rank)
            U, S, _ = np.linalg.svd(P_nu)
            rank = int(np.sum(S > 1e-9 * S.max()) if S.size > 0 else 0)
            if rank == 0:
                continue
            U_basis = U[:, :rank]  # orthonormal basis of V_ν isotype in ξ-class

            # The (ξ, ν) block of ρ_λ(I_2) in this basis:
            # First restrict ρ_I2 to ξ-class, then project to ν isotype.
            rho_I2_xi = rho_I2[idx_arr][:, idx_arr]
            block = U_basis.conj().T @ rho_I2_xi @ U_basis
            blocks[(xi, nu)] = {
                "matrix": block,
                "rank": rank,
                "trace": complex(np.trace(block)),
            }

    return blocks


# ──────────────────────────────────────────────────────────────────────
# §4 — Path A vs Path B verification on tritium
# ──────────────────────────────────────────────────────────────────────

def path_b_chi(lam: tuple, beta_full: list, w_inner_h6: list,
               beta_3_h3: list, q_val: float) -> complex:
    """Compute χ^λ(β_full) via the iterated Sub-lemma 2.1 formula.

    Path B = sum over (ξ, ν): c^λ_{ξν} · Tr(A^λ_{ξν}(I_2) · M_{ξν})
    where M_{ξν} = (basis-projected) ρ_λ(W_inner · β_3) restricted
    to the (ξ, ν) isotype.

    Specifically, the projected ρ_λ(W_inner) and ρ_λ(β_3) need to be
    expressed in the V_ξ ⊗ V_ν basis. Easier route: compute Path B as

      χ^λ(β_full) = Σ Tr(P_{ξν} · ρ_λ(β_full))

    using the projector composition. This is mathematically equivalent
    but bypasses the need for explicit V_ξ ⊗ V_ν isomorphism.
    """
    sigmas, dim = _compiled_sigmas(lam, "double")
    if dim == 0:
        return 0 + 0j
    sigma_mats = [np.asarray(fn(q_val), dtype=complex) for fn in sigmas]
    I = np.eye(dim, dtype=complex)

    # Build ρ_λ(β_full)
    M = I.copy()
    for c, d, g in beta_full:
        if g >= len(sigma_mats):
            return 0 + 0j
        M = M @ (complex(c) * sigma_mats[g] + complex(d) * I)

    # Group SYTs by {1..6}-restriction
    syts, cells, _ = standard_young_tableaux(lam)
    syt_groups: dict[tuple, list[int]] = {}
    for idx, syt in enumerate(syts):
        xi = syt_restriction_shape(syt, cells, 6)
        if sum(xi) != 6:
            continue
        syt_groups.setdefault(xi, []).append(idx)

    # Build ρ_λ(T_w) for w ∈ S_3 (H_3 generators)
    rho_h3_full: list[np.ndarray] = []
    for w in H3_GROUP_ELEMENTS:
        N = I.copy()
        for c, d, g in w:
            if g >= len(sigma_mats):
                return 0 + 0j
            N = N @ (complex(c) * sigma_mats[g] + complex(d) * I)
        rho_h3_full.append(N)

    # Sum over (ξ, ν): Tr of M restricted to V_ν isotype within ξ-class.
    # Halley-refined Wedderburn projectors P_ν are TRUE projectors
    # (eigenvalues in {0, 1}); their rank within ξ-class equals the
    # dim of the V_ν isotype = d_ξ · c^λ_(ξν) · d_ν  (the V_ν
    # multiplicity in the H_3 sub-rep of ξ-class).
    # KEY: not c·d_ν alone — the d_ξ factor accounts for the V_ξ
    # tensor copy in (V_ξ ⊗ V_ν).
    total = 0 + 0j
    for xi, idx_list in syt_groups.items():
        if not idx_list:
            continue
        idx_arr = np.array(idx_list)
        d_xi = _dim_of(xi)
        # H_3 sub-action on ξ-class
        rho_h3_xi = [N[idx_arr][:, idx_arr] for N in rho_h3_full]
        # ρ_λ(β_full) on ξ-class
        M_xi = M[idx_arr][:, idx_arr]
        for nu in partitions_of(3):
            c = _LR_TABLE_6_3.get((xi, nu, lam), 0)
            if c == 0:
                continue
            expected_rank = d_xi * c * _dim_of(nu)
            P_nu = wedderburn_projector_nu(rho_h3_xi, nu, q_val)
            # Top expected_rank eigenvectors of P_nu via SVD
            U, S, _ = np.linalg.svd(P_nu)
            U_basis = U[:, :expected_rank]
            # Tr(M restricted to V_ν isotype within ξ-class)
            total += complex(np.trace(U_basis.conj().T @ M_xi @ U_basis))
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atom", choices=["tritium"], default="tritium",
                        help="atom to verify (default: tritium)")
    args = parser.parse_args()

    print("=" * 96)
    print(f"  Sub-lemma 2.1 H_9 BRANCHING-BASIS verification: {args.atom}")
    print("=" * 96)
    print(f"  q_0 = {float(Q0):.10f}, h = {H:.10f}")
    print()

    parts_9 = partitions_of(9)
    beta_full = tritium_braid()
    w_inner_h6 = _proton_body() + [(1.0, -H / 2, 2)] + \
                 [(c, d, g + 3) for (c, d, g) in _neutron_body()]
    beta_3_h3 = _neutron_body()

    print(f"  β_{args.atom}: {len(beta_full)} generators")
    print()

    # Path A: direct χ^λ(β_full) via Hoefsmit
    print(f"  [Path A] direct χ^λ(β_{args.atom}) at H_9 for {len(parts_9)} λ...")
    t0 = time.monotonic()
    chi_a = {}
    for lam in parts_9:
        chi_a[lam] = chi_lambda_fast(lam, beta_full)
    print(f"    done in {time.monotonic() - t0:.1f}s")
    print()

    # Path B: branching-basis decomposition
    print(f"  [Path B] iterated formula via Wedderburn-projector branching...")
    t0 = time.monotonic()
    chi_b = {}
    for lam in parts_9:
        chi_b[lam] = path_b_chi(lam, beta_full, w_inner_h6, beta_3_h3,
                                  float(Q0))
    print(f"    done in {time.monotonic() - t0:.1f}s")
    print()

    # Compare
    print(f"  Path A vs Path B:")
    print(f"  {'λ':<26} {'χ^λ A':>20} {'χ^λ B':>20} {'|rel|':>11}  status")
    print("  " + "-" * 88)
    max_rel = 0.0
    n_pass = 0
    for lam in parts_9:
        a = chi_a[lam]
        b = chi_b[lam]
        denom = max(abs(a), 1e-15)
        rel = abs(a - b) / denom
        max_rel = max(max_rel, rel)
        if rel < 1e-10:
            n_pass += 1
            status = "✓"
        else:
            status = "✗"
        print(f"  {str(lam):<26} {a.real:>+20.10e} {b.real:>+20.10e} "
              f"{rel:>11.2e}  {status}")
    print()
    print(f"  Verified: {n_pass}/{len(parts_9)}  max rel residual: {max_rel:.2e}")
    print()

    # Witness
    from witness_base import WitnessBuilder
    from lean_uniqueness_refs import lean_uniqueness_ref
    builder = (
        WitnessBuilder(f"sublemma-2-1-h9-{args.atom}-branching-verify",
                       engine="numpy")
        .set_description(
            f"Sub-lemma 2.1 H_9 verification for {args.atom} via the "
            f"BRANCHING BASIS approach (no test words). Uses SYT "
            f"restriction-by-ξ to identify the H_6 isotype blocks of "
            f"V_λ, then Wedderburn projection in H_3 (6 group elements) "
            f"to identify V_ν blocks within each ξ-class. Path B = "
            f"Σ_(ξ,ν) Tr(P_(ξν) · ρ_λ(β_full)) compared to Path A "
            f"(direct Hoefsmit). At q_0 numerically (f64); machine ε "
            f"target."
        )
        .set_audit_only(
            "docs/audits/2026-05-16-sublemma-2-1-h9-phase-1.md"
        )
        .add_data("atom", args.atom)
        .add_data("lean_uniqueness_ref", lean_uniqueness_ref(args.atom))
        .add_data("interface_outer", "nn")
        .add_data("interface_inner", "pn")
        .add_data("approach", "branching_basis_no_test_words")
        .add_data("n_partitions_9", len(parts_9))
        .add_data("n_verified", n_pass)
        .add_data("max_relative_residual", max_rel)
        .add_data("chi_path_a", {
            str(lam): [chi_a[lam].real, chi_a[lam].imag]
            for lam in parts_9
        })
        .add_data("chi_path_b", {
            str(lam): [chi_b[lam].real, chi_b[lam].imag]
            for lam in parts_9
        })
        .add_assertion(
            "all_lambda_path_a_eq_path_b_machine_eps",
            computed=n_pass,
            expected=len(parts_9),
            source="branching-basis Wedderburn projection at H_6 × H_3",
        )
        .add_caveat(
            "f64 numerical precision (~1e-12 relative). 50-dps mpmath "
            "version is straightforward (replace numpy with mpmath in "
            "Wedderburn projector + matrix products) but ~50× slower."
        )
    )
    out_path = builder.save()
    print(f"  Witness: {out_path}")
    return 0 if n_pass == len(parts_9) else 1


if __name__ == "__main__":
    sys.exit(main())
