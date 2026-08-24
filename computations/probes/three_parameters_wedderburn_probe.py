#!/usr/bin/env python3
"""Probe: three-parameters-wedderburn
(`prop:three-parameters-wedderburn`).

The proposition asserts that the Iwahori-Hecke algebra H_3(R, q)
decomposes via the Wedderburn-Artin theorem as

    H_3(R, q)  ≅  M_1(k) ⊕ M_2(k) ⊕ M_1(k)

with one simple matrix block per partition λ ⊢ 3 ∈ {(3), (2,1), (1^3)},
giving dim H_3 = 1² + 2² + 1² = 6.  The three blocks correspond to
the three physical sectors (shape / scale / interaction) and to the
three calibration inputs in QOU's mass-formula closure.

This probe verifies:

  (1) dim_q-independent dimension count: |SYT(λ)| = (1, 2, 1) for
      λ ∈ ((3), (2,1), (1^3)) with Σ dim² = 6 = dim H_3.
  (2) Eigenvalue structure of σ_i in each block: trivial block ↦ +q,
      sign block ↦ −q⁻¹, standard block has eigenvalues {+q, −q⁻¹}.
  (3) Hecke quadratic σ² = (q−q⁻¹)σ + 𝟙 holds in each block via the
      canonical Hoefsmit-seminormal construction.

Emits `three-parameters-wedderburn-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from probe_staircase_ew_k3_categorical import build_hoefsmit_mpfr  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from hecke_character_symbolic import standard_young_tableaux  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _matrix_max_abs(M, dim: int) -> "mp.mpf":
    return max(mp.fabs(M[i, j]) for i in range(dim) for j in range(dim))


def _eigenvalues_2x2(M):
    """Return characteristic-poly roots of 2x2 mpmath matrix."""
    tr = M[0, 0] + M[1, 1]
    det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    disc = tr * tr - 4 * det
    sqrt_disc = mp.sqrt(disc)
    return ((tr + sqrt_disc) / 2, (tr - sqrt_disc) / 2)


def main() -> int:
    builder = WitnessBuilder(
        "three-parameters-wedderburn-probe",
        engine="mpmath",
    )
    set_compute_dps()

    q = Q_MP
    h = q - 1 / q

    SHAPES = [(3,), (2, 1), (1, 1, 1)]
    EXPECTED_DIM = [1, 2, 1]
    PHYSICAL_SECTOR = [
        "shape (symmetric / deformation)",
        "scale (standard / mass ruler)",
        "interaction (sign / hadronic)",
    ]
    EIGENVALUE_DESC = [
        "+q (trivial)",
        "{+q, −q⁻¹} mixed (standard)",
        "−q⁻¹ (sign)",
    ]

    per_block = []
    total_dim = 0
    sum_squared_dims = 0
    max_hecke_residue = mp.mpf(0)
    max_eigenvalue_residue = mp.mpf(0)

    for shape, expected_dim, sector, eig_desc in zip(
            SHAPES, EXPECTED_DIM, PHYSICAL_SECTOR, EIGENVALUE_DESC):
        sigmas, dim = build_hoefsmit_mpfr(shape, q)
        syts, _, _ = standard_young_tableaux(shape)
        dim_syt = len(syts)
        assert dim == dim_syt == expected_dim, (
            f"Dim mismatch for {shape}: got {dim} from Hoefsmit, "
            f"{dim_syt} from SYT, expected {expected_dim}"
        )

        # Hecke quadratic check (already covered by Hoefsmit probe;
        # repeated here for self-containment).
        I = mp.eye(dim)
        s1 = sigmas[0]
        hecke_resid = float(_matrix_max_abs(s1 * s1 - h * s1 - I, dim))
        max_hecke_residue = max(max_hecke_residue,
                                 mp.mpf(hecke_resid))

        # Eigenvalue structure check.
        if dim == 1:
            # σ_i in 1-d block is a scalar.
            scalar = s1[0, 0]
            # Trivial block: scalar should be +q.
            # Sign block: scalar should be −q⁻¹.
            if shape == (3,):
                expected_eig = q
            else:  # (1,1,1)
                expected_eig = -1 / q
            eig_resid = float(mp.fabs(scalar - expected_eig))
            eigenvalues_found = [float(scalar)]
        else:
            # Standard block (2,1) — σ_1 has eigenvalues {+q, −q⁻¹}.
            e1, e2 = _eigenvalues_2x2(s1)
            # Pair them up to the expected set, allowing either order.
            expected_set = {float(q), float(-1 / q)}
            got_set = sorted([float(e1), float(e2)])
            exp_sorted = sorted(expected_set)
            eig_resid = max(
                abs(got_set[0] - exp_sorted[0]),
                abs(got_set[1] - exp_sorted[1]),
            )
            eigenvalues_found = got_set
        max_eigenvalue_residue = max(max_eigenvalue_residue,
                                       mp.mpf(eig_resid))

        total_dim += dim
        sum_squared_dims += dim * dim

        per_block.append({
            "shape": str(shape),
            "physical_sector": sector,
            "dim_V_lambda": dim,
            "dim_squared_contribution": dim * dim,
            "eigenvalue_description": eig_desc,
            "eigenvalues_found": eigenvalues_found,
            "eigenvalue_residue": eig_resid,
            "hecke_quadratic_residue": hecke_resid,
        })

    expected_dim_h3 = 6  # = |S_3| = 3!
    dim_h3_check = sum_squared_dims == expected_dim_h3

    (
        builder
        .set_description(
            "I1 probe for prop:three-parameters-wedderburn.  "
            "Verifies the Wedderburn-Artin decomposition "
            "H_3(R, q) ≅ M_1(k) ⊕ M_2(k) ⊕ M_1(k) with three blocks "
            "indexed by λ ⊢ 3 ∈ {(3), (2,1), (1^3)}: dim sum 1+4+1=6 "
            "= dim H_3 (and = |S_3|); eigenvalue structure +q on "
            "trivial, {+q, −q⁻¹} on standard, −q⁻¹ on sign; Hecke "
            "quadratic σ² = (q−q⁻¹)σ + 𝟙 verified in each block.  "
            "The three blocks are the three QOU calibration sectors "
            "(shape / scale / interaction)."
        )
        .set_content_block("prop:three-parameters-wedderburn")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("sum_squared_dims", sum_squared_dims)
        .add_parameter("expected_dim_h3", expected_dim_h3)
        .add_parameter("dim_h3_matches", dim_h3_check)
        .add_parameter("max_eigenvalue_residue",
                       float(max_eigenvalue_residue))
        .add_parameter("max_hecke_quadratic_residue",
                       float(max_hecke_residue))
        .add_data("per_block_structure", per_block)
        .add_assertion(
            name="dim_h3_equals_sum_of_squared_block_dims",
            computed=float(abs(sum_squared_dims - expected_dim_h3)),
            expected=0.0, tolerance=0.0,
            unit="|Σ dim²(V_λ) − dim H_3(q)|  (= |1+4+1 − 6|)",
            source="Wedderburn-Artin dimension count.",
        )
        .add_assertion(
            name="eigenvalue_structure_per_block",
            computed=float(max_eigenvalue_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over λ ∈ {(3), (2,1), (1^3)} of |σ_1 eigenvalues "
                "− expected {+q, −q⁻¹}|"
            ),
            source=(
                "Hecke quadratic factorisation "
                "(σ − q)(σ + q⁻¹) = 0 determines eigenvalues; "
                "decomposition into the three blocks is by which "
                "eigenvalue(s) appear."
            ),
        )
        .add_assertion(
            name="hecke_quadratic_per_block",
            computed=float(max_hecke_residue),
            expected=0.0, tolerance=1e-40,
            unit="max over the 3 blocks of |σ² − hσ − 𝟙|_∞",
            source="Defining relation of H_3(q).",
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"H_3(R, q) Wedderburn decomposition:")
    print(f"{'shape':<13} {'sector':<35} {'dim':<5} {'dim²':<6} {'eigenvalues':<35} {'eig_res':<10}")
    for p in per_block:
        eig_str = (f"[{p['eigenvalues_found'][0]:.4f}, "
                   f"{p['eigenvalues_found'][1]:.4f}]"
                   if len(p['eigenvalues_found']) == 2
                   else f"{p['eigenvalues_found'][0]:.4f}")
        print(f"  {p['shape']:<11} {p['physical_sector']:<35} "
              f"{p['dim_V_lambda']:<5} "
              f"{p['dim_squared_contribution']:<6} "
              f"{eig_str:<35} {p['eigenvalue_residue']:.2e}")
    print()
    print(f"  Σ dim²   = {sum_squared_dims}  (expected dim H_3 = "
          f"{expected_dim_h3}: {'✓' if dim_h3_check else '✗'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
