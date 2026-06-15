#!/usr/bin/env python3
"""Probe: hoefsmit-seminormal-form (`prop:hoefsmit-seminormal-form`).

The proposition states that the Hoefsmit seminormal form gives an
explicit matrix representation ρ_λ : H_n(R, q) → M_{d_λ}(ℂ) for each
partition λ ⊢ n, where d_λ = |SYT(λ)|, and that these matrices satisfy
both:

  (i)  Hecke quadratic:  σ_i² = (q − q⁻¹) σ_i + 𝟙
  (ii) Braid relation:   σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}

This probe verifies both relations on every partition λ ⊢ n for
n = 2, …, 6, evaluated at q = q_0 via the canonical builder
`build_hoefsmit_mpfr` from `probe_staircase_ew_k3_categorical`.

A failure here would invalidate every probe that uses canonical
Hoefsmit downstream (the entire H_n cluster of PR #818 and beyond).
This probe is therefore a foundational gate for the cluster.

Emits `hoefsmit-seminormal-form-probe.witness.json`.
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


def _partitions_of(n: int):
    """Generate partitions of n (descending parts)."""
    def go(n_, max_):
        if n_ == 0:
            yield ()
            return
        for i in range(min(n_, max_), 0, -1):
            for tail in go(n_ - i, i):
                yield (i,) + tail
    yield from go(n, n)


def _matrix_max_abs(M, dim: int) -> "mp.mpf":
    return max(mp.fabs(M[i, j]) for i in range(dim) for j in range(dim))


def main() -> int:
    builder = WitnessBuilder(
        "hoefsmit-seminormal-form-probe",
        engine="mpmath",
    )
    mp.dps = 50

    q = Q_MP
    h = q - 1 / q

    results = []
    max_hecke_residue = mp.mpf(0)
    max_braid_residue = mp.mpf(0)
    total_irreps_tested = 0

    for n in range(2, 7):  # n = 2 … 6
        for shape in _partitions_of(n):
            sigmas, dim = build_hoefsmit_mpfr(shape, q)
            if dim == 0:
                continue
            total_irreps_tested += 1
            I = mp.eye(dim)

            # (i) Hecke quadratic: σ_i² − h σ_i − 𝟙 = 0 for every i.
            hecke_residues = []
            for k in range(n - 1):
                sig = sigmas[k]
                resid_mat = sig * sig - h * sig - I
                hecke_residues.append(
                    float(_matrix_max_abs(resid_mat, dim)))
            shape_hecke_max = max(hecke_residues) if hecke_residues else 0.0
            max_hecke_residue = max(max_hecke_residue,
                                     mp.mpf(shape_hecke_max))

            # (ii) Braid relation: σ_i σ_{i+1} σ_i − σ_{i+1} σ_i σ_{i+1} = 0
            # for every i ∈ {1, …, n−2}.
            braid_residues = []
            for k in range(n - 2):
                s1, s2 = sigmas[k], sigmas[k + 1]
                resid_mat = s1 * s2 * s1 - s2 * s1 * s2
                braid_residues.append(
                    float(_matrix_max_abs(resid_mat, dim)))
            shape_braid_max = (max(braid_residues)
                                if braid_residues else 0.0)
            max_braid_residue = max(max_braid_residue,
                                     mp.mpf(shape_braid_max))

            # Sanity: dim = |SYT(λ)|.
            syts, _, _ = standard_young_tableaux(shape)
            d_syt = len(syts)

            results.append({
                "n": n,
                "shape": str(shape),
                "dim_hoefsmit": dim,
                "dim_syt_count": d_syt,
                "dim_matches_syt": dim == d_syt,
                "hecke_quadratic_max_residue": shape_hecke_max,
                "braid_relation_max_residue": shape_braid_max,
            })

    (
        builder
        .set_description(
            "I1 probe for prop:hoefsmit-seminormal-form.  Verifies "
            "that for every partition λ ⊢ n with 2 ≤ n ≤ 6, the "
            "canonical Hoefsmit-seminormal matrices satisfy both "
            "(i) the Hecke quadratic σ² = (q−q⁻¹)σ + 𝟙 on every "
            "generator and (ii) the braid relation "
            "σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1} on every adjacent "
            "pair.  Also confirms dim ρ_λ = |SYT(λ)| (Hoefsmit's "
            "seminormal dimension).  This is the foundational gate "
            "for the entire H_n probe cluster of PR #818 — a failure "
            "here would invalidate downstream character checks."
        )
        .set_content_block("prop:hoefsmit-seminormal-form")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("total_irreps_tested", total_irreps_tested)
        .add_parameter("max_hecke_quadratic_residue",
                       float(max_hecke_residue))
        .add_parameter("max_braid_relation_residue",
                       float(max_braid_residue))
        .add_data("per_irrep_results", results)
        .add_assertion(
            name="hecke_quadratic_all_irreps_n_2_to_6",
            computed=float(max_hecke_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over partitions λ ⊢ n (2 ≤ n ≤ 6) and generators "
                "σ_i of |σ_i² − (q−q⁻¹) σ_i − 𝟙|_∞"
            ),
            source=(
                "Hoefsmit-seminormal axial-distance formula; the "
                "Hecke quadratic is the defining relation per "
                "rem:hecke-algebra-from-braiding."
            ),
        )
        .add_assertion(
            name="braid_relation_all_irreps_n_3_to_6",
            computed=float(max_braid_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over partitions λ ⊢ n (3 ≤ n ≤ 6) and adjacent "
                "pairs (i, i+1) of "
                "|σ_i σ_{i+1} σ_i − σ_{i+1} σ_i σ_{i+1}|_∞"
            ),
            source=(
                "Hoefsmit's construction is a faithful representation "
                "of the braid group on |SYT(λ)|-dimensional space; "
                "the braid relation is preserved by construction."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Tested {total_irreps_tested} irreducible reps "
          f"across n = 2…6.")
    print(f"  max Hecke quadratic residue:  "
          f"{float(max_hecke_residue):.2e}")
    print(f"  max braid relation residue:   "
          f"{float(max_braid_residue):.2e}")
    print()
    print(f"{'n':<3} {'shape':<22} {'dim':<5} {'hecke_res':<12} {'braid_res':<12}")
    for r in results:
        print(f"  {r['n']:<3} {r['shape']:<20} {r['dim_hoefsmit']:<5} "
              f"{r['hecke_quadratic_max_residue']:<12.2e} "
              f"{r['braid_relation_max_residue']:<12.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
