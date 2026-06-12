#!/usr/bin/env python3
"""sublemma_2_1_h12_he4_branching.py — H_12 ⁴He Sub-lemma 2.1 verification.

Phase 2 of the H_12 ⁴He scaffold (`docs/audits/2026-05-16-sublemma-
2-1-h12-he4-scaffold.md`).  Extends PR #666's H_9 branching-basis
algorithm with one more level of LR nesting: H_12 ↓ H_9 × H_3.

For canonical pppnnn ⁴He at H_12:
   β_⁴He = β_p₁ · I_pp · β_p₂ · I_pn · β_n₁ · I_nn · β_n₂
   (with 3 inter-nucleon interfaces)

Outer split at σ_8 (between strand 9 and 10, 0-indexed σ_8):
   χ^λ(β_⁴He) = Σ_(η⊢9, ν⊢3) c^λ_(η,ν) · Tr_(V_η⊗V_ν)(
       A^λ_(η,ν)(I_nn) · (ρ_η(W_tritium) ⊗ ρ_ν(β_n₂)))

where W_tritium ∈ H_9 is the first three nucleons + their two interfaces.

Algorithm:
   1. SYT enumeration of λ ⊢ 12, group by {1..9}-restriction shape η ⊢ 9.
   2. Halley-refined Hecke Wedderburn projector P_ν (ν ⊢ 3) on each
      η-class via the H_3 sub-action (σ_9, σ_10 in H_12 = 0-indexed).
   3. Path A: direct χ^λ(β_⁴He) via Hoefsmit at H_12.
   4. Path B: Σ_(η,ν) Tr(P_(η,ν) · ρ_λ(β_⁴He)) using the branching
      basis (with LR-determined rank from c^λ_(η,ν) · d_η · d_ν).
   5. Verify Path A = Path B at machine ε for all λ ⊢ 12.

Output: sublemma-2-1-h12-he4-branching-verify.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas, chi_lambda_fast  # noqa: E402
from hecke_characters import standard_young_tableaux  # noqa: E402
from lr_coefficients import partitions_of, get_lr_table  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from sublemma_2_1_h9_branching_basis import (  # noqa: E402
    syt_restriction_shape, wedderburn_projector_nu,
)
from sublemma_2_1_h9_tritium_verify import (  # noqa: E402
    _proton_body, _neutron_body, H,
)


# Module-level caches
_LR_TABLE_9_3 = get_lr_table(9, 3)
_DIM_CACHE: dict[tuple, int] = {}


def _dim_of(shape: tuple) -> int:
    if shape not in _DIM_CACHE:
        _, _DIM_CACHE[shape] = _compiled_sigmas(shape, "double")
    return _DIM_CACHE[shape]


# H_3 group elements as words on H_12 generators σ_9, σ_10 (0-indexed)
# These are the bridge generators for the H_3 sub-algebra acting on
# strands {10, 11, 12} (= last nucleon n₂).
H3_GROUP_AT_H12 = [
    [],
    [(1.0, 0.0, 9)],
    [(1.0, 0.0, 10)],
    [(1.0, 0.0, 9), (1.0, 0.0, 10)],
    [(1.0, 0.0, 10), (1.0, 0.0, 9)],
    [(1.0, 0.0, 9), (1.0, 0.0, 10), (1.0, 0.0, 9)],
]


def he4_braid_canonical() -> list:
    """Canonical pppnnn ⁴He braid at H_12: p₁ · I_pp · p₂ · I_pn · n₁ · I_nn · n₂."""
    word = []
    # β_p₁ on strands 0..2
    word.extend(_proton_body())
    # I_pp at strand 2 (bridge between p₁ and p₂)
    word.append((1.0, 0.0, 2))
    # β_p₂ on strands 3..5
    word.extend([(c, d, g + 3) for (c, d, g) in _proton_body()])
    # I_pn at strand 5
    word.append((1.0, -H / 2, 5))
    # β_n₁ on strands 6..8
    word.extend([(c, d, g + 6) for (c, d, g) in _neutron_body()])
    # I_nn at strand 8
    word.append((1.0, -H, 8))
    # β_n₂ on strands 9..11
    word.extend([(c, d, g + 9) for (c, d, g) in _neutron_body()])
    return word


def path_b_chi_h12(lam: tuple, beta_full: list, q_val: float) -> complex:
    """Path B: χ^λ(β_full) at H_12 via H_9 × H_3 branching basis."""
    sigmas, dim = _compiled_sigmas(lam, "double")
    if dim == 0:
        return 0 + 0j
    sigma_mats = [np.asarray(fn(q_val), dtype=complex) for fn in sigmas]
    I = np.eye(dim, dtype=complex)

    # ρ_λ(β_full)
    M = I.copy()
    for c, d, g in beta_full:
        if g >= len(sigma_mats):
            return 0 + 0j
        M = M @ (complex(c) * sigma_mats[g] + complex(d) * I)

    # Group SYTs of λ by {1..9}-restriction shape η
    syts, cells, _ = standard_young_tableaux(lam)
    syt_groups: dict[tuple, list[int]] = {}
    for idx, syt in enumerate(syts):
        eta = syt_restriction_shape(syt, cells, 9)
        if sum(eta) != 9:
            continue
        syt_groups.setdefault(eta, []).append(idx)

    # ρ_λ(T_w) for w ∈ S_3 (H_3 sub-action acting on strands {10..12})
    rho_h3_full: list[np.ndarray] = []
    for w in H3_GROUP_AT_H12:
        N = I.copy()
        for c, d, g in w:
            if g >= len(sigma_mats):
                return 0 + 0j
            N = N @ (complex(c) * sigma_mats[g] + complex(d) * I)
        rho_h3_full.append(N)

    # Sum over (η, ν): Tr of M restricted to V_ν isotype within η-class
    total = 0 + 0j
    for eta, idx_list in syt_groups.items():
        if not idx_list:
            continue
        idx_arr = np.array(idx_list)
        d_eta = _dim_of(eta)
        rho_h3_eta = [N[idx_arr][:, idx_arr] for N in rho_h3_full]
        M_eta = M[idx_arr][:, idx_arr]
        for nu in partitions_of(3):
            c = _LR_TABLE_9_3.get((eta, nu, lam), 0)
            if c == 0:
                continue
            expected_rank = d_eta * c * _dim_of(nu)
            # Build H_3 Wedderburn projector on η-class using PR #666's
            # function — but adapted to H_12 generator indices (σ_9, σ_10).
            # The wedderburn_projector_nu function from #666 uses
            # H3_GROUP_ELEMENTS with σ_6, σ_7 (for H_9 case).  We pass
            # our pre-restricted rho_h3_eta matrices, which are correct
            # for our H_12 use.
            P_nu = wedderburn_projector_nu(rho_h3_eta, nu, q_val)
            U, S, _ = np.linalg.svd(P_nu)
            U_basis = U[:, :expected_rank]
            total += complex(np.trace(U_basis.conj().T @ M_eta @ U_basis))
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-dim", type=int, default=50,
                        help="skip λ with dim > max_dim (default 50, "
                             "tractable in reasonable time)")
    parser.add_argument("--all", action="store_true",
                        help="process all 77 λ ⊢ 12 (~15-30 min)")
    args = parser.parse_args()

    print("=" * 96)
    print("  Sub-lemma 2.1 H_12 ⁴He BRANCHING-BASIS verification")
    print("=" * 96)
    print(f"  q_0 = {float(Q0):.10f}, h = {H:.10f}")
    print()

    parts_12 = partitions_of(12)
    beta_full = he4_braid_canonical()
    print(f"  β_⁴He: {len(beta_full)} generators")
    print()

    # Filter to tractable subset
    print("  Computing per-λ dims (filter to tractable subset)...")
    t0 = time.monotonic()
    lam_dims = []
    for lam in parts_12:
        d = _dim_of(lam)
        lam_dims.append((lam, d))
    print(f"    77 dims computed in {time.monotonic()-t0:.1f}s")
    print()

    if args.all:
        targets = lam_dims
    else:
        targets = [(lam, d) for lam, d in lam_dims if d <= args.max_dim]
    print(f"  Processing {len(targets)} λ ⊢ 12 (dim ≤ {args.max_dim if not args.all else 'all'})")
    print()

    print(f"  {'λ':<28} {'dim':>5} {'χ^λ(Path A)':>15} {'χ^λ(Path B)':>15} "
          f"{'|rel|':>11}  status")
    print("  " + "-" * 92)
    max_rel = 0.0
    n_pass = 0
    n_total = 0
    chi_a_dict = {}
    chi_b_dict = {}
    t_total = 0.0
    for lam, d in targets:
        n_total += 1
        ta = time.monotonic()
        a = chi_lambda_fast(lam, beta_full)
        elapsed_a = time.monotonic() - ta
        tb = time.monotonic()
        b = path_b_chi_h12(lam, beta_full, float(Q0))
        elapsed_b = time.monotonic() - tb
        t_total += elapsed_a + elapsed_b
        chi_a_dict[lam] = a
        chi_b_dict[lam] = b
        denom = max(abs(a), 1e-15)
        rel = abs(a - b) / denom
        max_rel = max(max_rel, rel)
        status = "✓" if rel < 1e-10 else "✗"
        if rel < 1e-10:
            n_pass += 1
        print(f"  {str(lam):<28} {d:>5} {a.real:>+15.7e} {b.real:>+15.7e} "
              f"{rel:>11.2e}  {status}  (A:{elapsed_a:.1f}s B:{elapsed_b:.2f}s)")

    print()
    print(f"  Verified: {n_pass}/{n_total}  max rel residual: {max_rel:.2e}")
    print(f"  Total compute time: {t_total:.1f}s")
    print()

    from witness_base import WitnessBuilder
    from lean_uniqueness_refs import lean_uniqueness_ref
    builder = (
        WitnessBuilder("sublemma-2-1-h12-he4-branching-verify",
                       engine="numpy")
        .set_description(
            f"Sub-lemma 2.1 H_12 ⁴He multi-interface verification via "
            f"the branching-basis approach extended from PR #666 with "
            f"one more LR nesting level (H_12 ↓ H_9 × H_3).  "
            f"Path A = direct Hoefsmit at H_12; Path B = iterated "
            f"sub-lemma 2.1 with Halley-refined Wedderburn projectors "
            f"in H_3.  Verified for {n_pass}/{n_total} λ ⊢ 12 "
            f"(dim ≤ {args.max_dim if not args.all else 'all 77'}); "
            f"max relative residual {max_rel:.2e}."
        )
        .set_audit_only(
            "docs/audits/2026-05-16-sublemma-2-1-h12-he4-scaffold.md"
        )
        .add_data("atom", "4He_canonical")
        .add_data("interface_pp_outer", False)
        .add_data("interface_pn_middle", False)
        .add_data("interface_nn_outermost", True)
        .add_data("approach", "h12_branching_basis_h9_x_h3")
        .add_data("max_dim_filter", args.max_dim if not args.all else None)
        .add_data("n_partitions_processed", n_total)
        .add_data("n_partitions_verified", n_pass)
        .add_data("max_relative_residual", max_rel)
        .add_data("compute_time_seconds", t_total)
        .add_data("chi_path_a", {
            str(lam): [v.real, v.imag] for lam, v in chi_a_dict.items()
        })
        .add_data("chi_path_b", {
            str(lam): [v.real, v.imag] for lam, v in chi_b_dict.items()
        })
        .add_assertion(
            "all_processed_lambda_path_a_eq_path_b_machine_eps",
            computed=n_pass,
            expected=n_total,
            source="iterated branching-basis H_12 ↓ H_9 × H_3 "
                   "+ Halley-refined Wedderburn projectors",
        )
        .add_caveat(
            f"With --max-dim {args.max_dim}, only {n_total} of 77 "
            f"λ ⊢ 12 are processed (the rest have dim > {args.max_dim} "
            f"and Hoefsmit cold-start at H_12 takes longer per λ).  "
            f"Full coverage requires --all flag (~15-30 min compute)."
        )
    )
    builder.add_data("lean_uniqueness_ref", lean_uniqueness_ref("helium-4"))
    out = builder.save()
    print(f"  Witness: {out}")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    sys.exit(main())
