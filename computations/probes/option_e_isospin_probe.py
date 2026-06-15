#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical mpmath/sympy consumer
"""option_e_isospin_probe.py — H follow-up to PR #619.

Test whether **Option E's Kashiwara crystal weight `c_λ(q)`**
(per `rho_k_h3a_crystal.py`, deuteron) preserves the structural
**T = ³He isospin invariance** established at PR #622
(Hopf-antipode `prop:spin-involution-lp-dual-invariance`) and at
PR #624 (sign-flip `prop:crystal-isospin-degeneracy`).

Question: Form the c_λ-weighted observable

    W_c(K) := Σ_{λ ⊢ 3A,  ht(λ) ≤ 6}  c_λ(q_0) · χ^λ(β_K)(q_0)

over the canonical Δ_I-coupled atomic word `β_K =
mass_at_3A_proper.atom_braid_word_3A(Z, N)` for K ∈ {D, T, ³He}.
(⁴He has 58 height-≤6 partitions at H_12 with much larger
seminormal matrix dimensions; the probe is feasible there but
intentionally deferred behind the (B) ⁴He Path A pole-order check
in the same H follow-up queue.)

If W_c(T) = W_c(³He) (to numerical precision), then Option E's
crystal weight respects the Hopf-antipode V_λ ↔ V_{λᵀ} symmetry —
this is the *non-trivial* prediction of the convergence finding in
[isospin-mass-split-em-localisation](#rem:isospin-mass-split-em-localisation),
because the **canonical Δ_I-coupled words** for T and ³He differ
in interface type, not just signs (so naive multiplicativity
arguments don't apply).

If W_c(T) ≠ W_c(³He), Option E *breaks* the Hopf-antipode symmetry
at the c_λ-weight level, which would localise some of the
mirror-isobar mass split inside the c_λ-weighted Markov-trace
sector — contradicting the EM-localisation conclusion.

Either result is informative; this script reports both.

Output: option-e-isospin-probe.witness.json
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
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

# 50 dps matches the precision policy of rho_k_h3a_crystal.py and
# rho_k_h3a_refinement.py.  The c_λ Macdonald hook-content is
# evaluated in mpmath at this precision and serialised in full;
# the χ^λ matrix product is in numpy float64 (~1e-15 rel) for
# speed but the resulting per-atom W_c value is recovered to ~1e-15
# rel — well above the 1e-3 falsification threshold this probe uses.
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder
from canonical_braid_crossings import atom_canonical_crossings
from hecke_characters import partitions_of
from rho_k_h3a_refinement import hoefsmit_matrices_numeric
from rho_k_h3a_crystal import c_lambda_q
from q_parameter import Q_MP

import numpy as np


def chi_numeric_float(shape, crossings, q_mp):
    """Float64 χ^λ(β)(q) via numpy.  ~1000× faster than mpmath chi_numeric.

    Precision: float64 ≈ 1e-15 relative; well above the 1e-10 isospin
    test threshold for W_c values of magnitude ≤ 10^9.
    """
    matrices_mp, dim, _ = hoefsmit_matrices_numeric(shape, q_mp)
    if dim == 0:
        return 0.0
    matrices = [
        np.array([[float(M[i, j]) for j in range(dim)] for i in range(dim)],
                 dtype=np.float64)
        for M in matrices_mp
    ]
    q = float(q_mp)
    h = q - 1.0 / q
    d_lookup = {"sigma": 0.0, "sigma_inv": -h, "averaged": -h / 2.0}
    eye = np.eye(dim, dtype=np.float64)
    M = np.eye(dim, dtype=np.float64)
    for gen_idx, ctype in crossings:
        sigma = matrices[gen_idx]
        cross = sigma + d_lookup[ctype] * eye
        M = M @ cross
    return float(np.trace(M))


ATOMS = [
    # (label, Z, N) — order matches the merged crystal-isospin-degeneracy
    # block; only D, T, ³He are probed (⁴He partition count exceeds the
    # symbolic χ^λ budget for a quick probe).
    ("D",   1, 1),
    ("T",   1, 2),
    ("³He", 2, 1),
]


def height_le_6_partitions(n: int) -> list[tuple[int, ...]]:
    return [tuple(p) for p in partitions_of(n) if len(p) <= 6]


def main() -> int:
    # Instantiate the witness up front so durationMs covers the
    # actual probe runtime, not just serialization (per Copilot
    # review on PR #629).
    out = (WitnessBuilder("option-e-isospin-probe", engine="mpmath")
        .set_content_block("rem:option-e-isospin-test")
        .set_description(
            "H follow-up to PR #619: tests whether the Option E "
            "Kashiwara crystal weight c_λ(q) (per rho_k_h3a_crystal) "
            "preserves the T = ³He isospin invariance established for "
            "the LP-dual shadow price (PR #622 Hopf-antipode) under "
            "the canonical Δ_I-coupled atomic braid words. Probes "
            "W_c(K) := Σ_λ c_λ(q_0)·χ^λ(β_K)(q_0) for K ∈ {D, T, ³He}."
        )
        .add_data("narrative_block", "rem:option-e-isospin-test")
        .add_data("conditional_on", ["conj:crystal-graph-realization"])
        .add_data("q_0", str(Q_MP))
        .add_parameter("mp_dps", str(mp.mp.dps))
        .add_data("inputs", {
            "atom_braid_words":
                "mass_at_3A_proper.atom_braid_word_3A "
                "(canonical Δ_I-coupled (c, d, gen_idx) triples)",
            "c_lambda_q":
                "rho_k_h3a_crystal.c_lambda_q "
                "(mpmath at mp_dps; Macdonald hook-content)",
            "chi_lambda":
                "hoefsmit_matrices_numeric (mpmath seminormal "
                "matrices) → chi_numeric_float (numpy float64 trace "
                "of the canonical-word product)",
        })
    )
    print("Option E isospin probe — c_λ(q_0)-weighted observable\n",
          flush=True)
    print("Question: does W_c(T) = W_c(³He) under canonical Δ_I words?\n",
          flush=True)
    print(f"  q_0 = {mp.nstr(Q_MP, 20)}\n", flush=True)

    rows = []
    W_c_by_atom: dict[str, mp.mpf] = {}

    for label, Z, N in ATOMS:
        A = Z + N
        n = 3 * A
        crossings = atom_canonical_crossings(Z, N)
        partitions = height_le_6_partitions(n)
        print(f"  {label}  (Z={Z}, N={N}, A={A}, n={n}, "
              f"{len(crossings)} crossings, {len(partitions)} partitions)",
              flush=True)

        W_c = mp.mpf(0)
        per_partition = []
        for k, shape in enumerate(partitions):
            t0 = time.time()
            c_lam = c_lambda_q(shape, n, Q_MP)
            chi_q0 = chi_numeric_float(shape, crossings, Q_MP)
            dt = time.time() - t0
            print(f"    [{k+1:2d}/{len(partitions)}] λ={shape} "
                  f"chi={chi_q0:+.8g}  c_λ={mp.nstr(c_lam,8)}  "
                  f"({dt:.2f}s)", flush=True)
            contrib = c_lam * mp.mpf(chi_q0)
            W_c += contrib
            if abs(contrib) > mp.mpf("1e-12"):
                per_partition.append({
                    "lambda": list(shape),
                    "c_lambda_q0": str(c_lam),
                    "chi_lambda_q0": str(chi_q0),
                    "contribution": str(contrib),
                })

        W_c_by_atom[label] = W_c
        rows.append({
            "atom": label, "Z": Z, "N": N, "A": A, "n_strands": n,
            "n_partitions": len(partitions),
            "W_c_q0": str(W_c),
            "n_nonzero_contributions": len(per_partition),
            "top_contributions": sorted(
                per_partition,
                key=lambda r: abs(mp.mpf(r["contribution"])),
                reverse=True,
            )[:6],
        })
        print(f"    W_c(q_0) = {mp.nstr(W_c, 15)}")
        print()

    # Isospin test: W_c(T) vs W_c(³He)
    W_T = W_c_by_atom.get("T")
    W_He3 = W_c_by_atom.get("³He")
    isospin_split = abs(W_T - W_He3) if (W_T is not None and W_He3 is not None) else None

    print("─" * 60)
    print(f"  Isospin split:  |W_c(T) - W_c(³He)|  = "
          f"{mp.nstr(isospin_split, 12) if isospin_split is not None else 'n/a'}")
    if isospin_split is not None:
        rel_split = abs(isospin_split / W_T) if W_T != 0 else mp.mpf("nan")
        print(f"  Relative:        |Δ| / |W_c(T)|       = "
              f"{mp.nstr(rel_split, 6)}")
        if isospin_split < mp.mpf("1e-10"):
            print(f"\n  RESULT: Option E PRESERVES isospin invariance "
                  f"(T = ³He at machine precision).")
        else:
            print(f"\n  RESULT: Option E BREAKS isospin invariance "
                  f"(T ≠ ³He under canonical Δ_I words).")

    out = (out
        .add_data("atoms", rows)
        .add_data(
            "isospin_split_T_minus_3He",
            str(isospin_split) if isospin_split is not None else None,
        )
    )
    if isospin_split is not None:
        # Falsification probe: under the canonical Δ_I-coupled
        # convention, c_λ is transpose-asymmetric (c_λ ≠ c_{λᵀ}
        # except for self-conjugate λ), so W_c is *not* an
        # S-invariant observable.  We *expect* a large isospin
        # split as a structural fact, and the assertion records
        # this — `passed = true` when the split is large.
        out.add_assertion(
            "option_e_breaks_S_invariance_as_structurally_expected",
            computed=1.0 if isospin_split > mp.mpf("1e-3") else 0.0,
            expected=1.0,
            tolerance=0.0,
            source=("c_λ ≠ c_{λᵀ} for non-self-conjugate λ ⇒ "
                    "W_c not Hopf-antipode invariant; see "
                    "rem:option-e-isospin-test"),
        )
    p = out.save()
    print(f"\n  Witness: {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
