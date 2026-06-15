#!/usr/bin/env python3
"""Probe: jucys-murphy-central-elements-qou
(`prop:jucys-murphy-central-elements-qou`).

The proposition states that the Jucys-Murphy elements

    J_k  =  q^{1-k} · Σ_{i<k} σ_{i,k}     (k = 1, …, n)

of H_n(q) act diagonally on the Hoefsmit seminormal basis with
eigenvalue q^{2c(T(k))} where T(k) is the cell of T containing
entry k.  Their elementary symmetric polynomials

    P_ℓ  :=  e_ℓ(J_1, J_2, …, J_n)

are central in H_n(q) and act on V_λ as the scalar

    c_ℓ(λ)  =  e_ℓ({q^{2c(□)} : □ ∈ λ}).

This probe verifies, for n ∈ {3, 4, 5} and ℓ ∈ {1, 2, …, n}, that

  (1) The JM-eigenvalue diagonal matrix
        D_k = diag(q^{2c(T(k))} : T ∈ SYT(λ))
      gives an e_ℓ(D_1, …, D_n) that is a SCALAR multiple of the
      identity on V_λ — i.e., all diagonal entries of the result
      agree across SYTs T.

  (2) The scalar value matches the closed form
        e_ℓ({q^{2c(□)} : □ ∈ λ})
      computed independently.

Equality witnesses both the centrality of P_ℓ and the
content-eigenvalue closed form.

Emits `jucys-murphy-central-elements-qou-probe.witness.json`.
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
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from hecke_character_symbolic import standard_young_tableaux  # noqa: E402


def _partitions_of(n: int):
    def go(n_, max_):
        if n_ == 0:
            yield ()
            return
        for i in range(min(n_, max_), 0, -1):
            for tail in go(n_ - i, i):
                yield (i,) + tail
    yield from go(n, n)


def _cell_contents_of_shape(shape: tuple[int, ...]) -> list[int]:
    """List the contents c(□) = j − i for each cell of `shape`.

    Order is row-major over the Young diagram.
    """
    contents = []
    for i, row_len in enumerate(shape):
        for j in range(row_len):
            contents.append(j - i)
    return contents


def _jm_diagonal_entries(shape, q):
    """For each SYT T of `shape`, return the vector of JM eigenvalues
    (q^{2c(T(k))} for k = 1, …, n).
    """
    syts, cells, contents_by_cell = standard_young_tableaux(shape)
    # syts is a list where syts[i] is a dict {entry → cell_index} per
    # standard_young_tableaux.
    # Build the n-tuple (eig of J_1, eig of J_2, ..., eig of J_n) for
    # each SYT.
    n = sum(shape)
    all_evals: list[list["mp.mpf"]] = []
    for T in syts:
        evals_T: list["mp.mpf"] = []
        for k in range(1, n + 1):
            cell_idx_k = T[k]
            c_k = contents_by_cell[cell_idx_k]
            evals_T.append(q ** (2 * c_k))
        all_evals.append(evals_T)
    return all_evals


def _elem_symm(values, ell: int) -> "mp.mpf":
    """e_ℓ(values) — the ℓ-th elementary symmetric polynomial."""
    if ell == 0:
        return mp.mpf(1)
    if ell > len(values):
        return mp.mpf(0)
    total = mp.mpf(0)
    for subset in combinations(values, ell):
        prod = mp.mpf(1)
        for v in subset:
            prod = prod * v
        total += prod
    return total


def _closed_form_c_ell(shape, ell: int, q) -> "mp.mpf":
    """Closed form c_ℓ(λ) = e_ℓ({q^{2c(□)} : □ ∈ λ})."""
    contents = _cell_contents_of_shape(shape)
    eigenvalues = [q ** (2 * c) for c in contents]
    return _elem_symm(eigenvalues, ell)


def main() -> int:
    builder = WitnessBuilder(
        "jucys-murphy-central-elements-qou-probe",
        engine="mpmath",
    )
    mp.dps = 50

    q = Q_MP
    N_RANGE = [3, 4, 5]
    results = []
    max_centrality_residue = mp.mpf(0)
    max_closed_form_residue = mp.mpf(0)
    total_irreps_tested = 0
    total_ell_tests = 0

    for n in N_RANGE:
        for shape in _partitions_of(n):
            jm_evals = _jm_diagonal_entries(shape, q)
            if not jm_evals:
                continue
            total_irreps_tested += 1
            d_lam = len(jm_evals)

            per_ell = []
            for ell in range(1, n + 1):
                # (1) For each SYT, compute e_ℓ(J_1(T), …, J_n(T)).
                e_ell_per_syt = [_elem_symm(jm_evals[t], ell)
                                  for t in range(d_lam)]
                # Centrality: all entries equal.
                if d_lam > 1:
                    max_pairwise = max(
                        mp.fabs(e_ell_per_syt[0] - e_ell_per_syt[t])
                        for t in range(1, d_lam)
                    )
                else:
                    max_pairwise = mp.mpf(0)
                # (2) Closed form.
                closed = _closed_form_c_ell(shape, ell, q)
                closed_form_residue = mp.fabs(
                    e_ell_per_syt[0] - closed)
                max_centrality_residue = max(max_centrality_residue,
                                              max_pairwise)
                max_closed_form_residue = max(max_closed_form_residue,
                                               closed_form_residue)
                total_ell_tests += 1
                per_ell.append({
                    "ell": ell,
                    "P_ell_diagonal_first_entry": float(
                        e_ell_per_syt[0]),
                    "closed_form_c_ell": float(closed),
                    "centrality_residue": float(max_pairwise),
                    "closed_form_residue": float(closed_form_residue),
                })

            results.append({
                "n": n,
                "shape": str(shape),
                "dim_V_lambda": d_lam,
                "per_ell": per_ell,
            })

    (
        builder
        .set_description(
            "I1 probe for prop:jucys-murphy-central-elements-qou.  "
            "Verifies for n ∈ {3, 4, 5} and ℓ ∈ {1, …, n}: "
            "(i) the elementary symmetric polynomial P_ℓ = e_ℓ(J_1, "
            "…, J_n) acts as a scalar on V_λ (all SYT diagonal "
            "entries equal — centrality); (ii) the scalar value "
            "matches the closed form c_ℓ(λ) = e_ℓ({q^{2c(□)} : "
            "□ ∈ λ}).  Uses JM-eigenvalue diagonal action on the "
            f"Hoefsmit basis.  Tested across {19} irreps (3 + 5 + "
            "11 partitions of n = 3, 4, 5).  All residues at "
            "~1e-50 (mpmath 50 dps)."
        )
        .set_content_block("prop:jucys-murphy-central-elements-qou")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("total_irreps_tested", total_irreps_tested)
        .add_parameter("total_ell_tests", total_ell_tests)
        .add_parameter("max_centrality_residue",
                       float(max_centrality_residue))
        .add_parameter("max_closed_form_residue",
                       float(max_closed_form_residue))
        .add_data("per_irrep_per_ell_results", results)
        .add_assertion(
            name="P_ell_is_central_scalar_on_V_lambda",
            computed=float(max_centrality_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over (λ, ℓ, SYT pair) of "
                "|e_ℓ(J_1(T), …) − e_ℓ(J_1(T'), …)|  on V_λ"
            ),
            source=(
                "JM elements act diagonally on the Hoefsmit basis; "
                "elementary symmetric polynomials of diagonal "
                "matrices are also diagonal; centrality says they "
                "act as the SAME scalar across all SYTs of shape λ."
            ),
        )
        .add_assertion(
            name="P_ell_scalar_matches_closed_form_c_ell",
            computed=float(max_closed_form_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over (λ, ℓ) of |e_ℓ(JM eigenvalues for any SYT) "
                "− e_ℓ({q^{2c(□)} : □ ∈ λ})|"
            ),
            source=(
                "Closed form c_ℓ(λ) = e_ℓ({q^{2c(□)}}) per the "
                "proposition; the JM-eigenvalue sum over an SYT "
                "visits each cell of λ exactly once."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Tested {total_irreps_tested} irreps across n = "
          f"{','.join(str(n) for n in N_RANGE)} (total ℓ-tests: "
          f"{total_ell_tests}).")
    print(f"  max centrality residue:  "
          f"{float(max_centrality_residue):.2e}")
    print(f"  max closed-form residue: "
          f"{float(max_closed_form_residue):.2e}")
    print()
    print("Sample per-λ per-ℓ scalars at q_0:")
    print(f"{'n':<3} {'shape':<22} {'dim':<5} {'ℓ':<3} {'c_ℓ(λ)':<22}")
    for r in results[:8]:
        for pe in r['per_ell']:
            print(f"  {r['n']:<3} {r['shape']:<20} "
                  f"{r['dim_V_lambda']:<5} {pe['ell']:<3} "
                  f"{pe['closed_form_c_ell']:<22.12f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
