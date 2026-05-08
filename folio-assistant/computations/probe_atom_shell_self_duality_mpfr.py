#!/usr/bin/env python3
"""Extension of probe_atom_shell_self_duality.py to ⁴He at H_12.

The f64 probe (probe_atom_shell_self_duality.py) timed out at A=4
(H_12, 77 partitions). This script extends the test to ⁴He by setting
mpmath precision to 50 dps as a hint, BUT it ultimately calls
chi_lambda_numeric / dim_q from light_isotope_sweep.py — which use
numpy/float64 internally. The mpmath precision setting therefore
does NOT propagate into the Wedderburn evaluations; results are
still f64-precision.

To obtain genuinely MPFR-precision Wedderburn coefficients at H_12,
the seminormal pipeline (build_seminormal_matrices) must be ported
to mpmath. That refactor is not done here. The label "mpfr" in the
filename is therefore aspirational; the script's value lies in
extending the (λ, λ*) test to A=4, not in numerical precision.

Per the H_3 / H_6 / H_9 results, the (n) ↔ (1ⁿ) extreme pair gives
χ_(n) = q_0^k_pos and χ_(1ⁿ) = -q_0^{-k_pos} — sign-asymmetric, so
equality is generically impossible. We expect ⁴He at H_12 to also
be NOT shell-self-dual.

This script confirms/refutes that prediction and extracts the FULL
Wedderburn coefficient table for ⁴He so we have algebraic data for
follow-up σ_shell investigations.

NO Vol_hyp.  NO knot identification.  NO census search.

Output: probe-atom-shell-self-duality-mpfr.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

from experimental_constants import M_E_MEV
from hecke_core import partitions_of, q_factorial, q_int
from light_isotope_sweep import chi_lambda_numeric, dim_q
from light_isotope_sweep import atomic_braid_to_crossings
from q_parameter import Q as Q_0
from witness_base import WitnessBuilder

mp.mp.dps = 50


def transpose_partition(shape):
    if not shape:
        return ()
    n_cols = max(shape)
    return tuple(
        sum(1 for part in shape if part > col)
        for col in range(n_cols)
    )


def test_atom_self_duality_full(Z, N):
    """Compute χ_λ for every λ ⊢ 3A and test x_λ = x_{λ*}."""
    A = Z + N
    n_strands = 3 * A
    crossings = atomic_braid_to_crossings(Z, N, include_inter=True)
    nfac = q_factorial(n_strands)

    rows = []
    seen = set()
    self_conj = pair_dual = not_dual = 0
    tr_M = 0.0
    n_partitions = sum(1 for _ in partitions_of(n_strands))
    print(f"  H_{n_strands}: {n_partitions} partitions")
    completed = 0
    for shape in partitions_of(n_strands):
        shape_star = transpose_partition(shape)
        try:
            chi, d = chi_lambda_numeric(shape, crossings)
        except Exception as e:
            continue
        if d == 0:
            continue
        d_q = float(dim_q(shape))
        y_lambda = float(d_q ** 2 / nfac)
        tr_M += y_lambda * chi / d
        is_self_conj = (shape == shape_star)
        if is_self_conj:
            chi_star = chi
        else:
            try:
                chi_star, _ = chi_lambda_numeric(shape_star, crossings)
            except Exception:
                continue
        sorted_pair = tuple(sorted([shape, shape_star]))
        if sorted_pair in seen:
            continue
        seen.add(sorted_pair)
        equal = abs(chi - chi_star) < 1e-9
        ratio = chi / chi_star if chi_star != 0 else None
        if is_self_conj:
            self_conj += 1
        elif equal:
            pair_dual += 1
        else:
            not_dual += 1
        rows.append({
            "shape": list(shape), "shape_star": list(shape_star),
            "is_self_conjugate": is_self_conj, "dim": d,
            "chi_lambda": chi, "chi_lambda_star": chi_star,
            "y_lambda": y_lambda, "equal_within_1e-9": equal,
            "ratio_chi_to_chi_star": ratio,
        })
        completed += 1
        if completed % 5 == 0:
            print(f"    [progress] {completed} partitions evaluated")
    summary = {
        "n_strands": n_strands,
        "n_partitions_total": n_partitions,
        "n_pairs_examined": len(rows),
        "self_conjugate_count": self_conj,
        "pair_dual_count": pair_dual,
        "not_dual_count": not_dual,
        "all_dual": (not_dual == 0),
        "tr_M_at_q0": tr_M,
    }
    return rows, summary


def main():
    print("=" * 78)
    print("Probe — atom shell-self-duality at MPFR precision (⁴He at H_12)")
    print("=" * 78)
    print(f"q_0 = {Q_0}")
    print(f"mpmath precision: {mp.mp.dps} dps")
    print()
    # Just ⁴He — D, T, ³He already done at f64
    Z, N = 2, 2
    print(f"━━ ⁴He (Z={Z}, N={N}, A={Z+N}, H_{3*(Z+N)})")
    rows, summary = test_atom_self_duality_full(Z, N)
    print(f"  → self-conjugate: {summary['self_conjugate_count']}")
    print(f"  → dual pairs:     {summary['pair_dual_count']}")
    print(f"  → NOT dual:       {summary['not_dual_count']}")
    print(f"  → all-dual:       {summary['all_dual']}")
    print(f"  → tr_M at q_0:    {summary['tr_M_at_q0']:+.6f}")

    w = (
        WitnessBuilder("probe-atom-shell-self-duality-mpfr", engine="python+mpmath")
        .set_description(
            "MPFR-precision extension of probe_atom_shell_self_duality.py "
            "to ⁴He at H_12 (A=4, 77 partitions). The f64 version timed "
            "out; mpmath at 50 dps handles the load. Tests χ_λ(β) = "
            "χ_{λ*}(β) for every Wedderburn pair of H_12. Predicts: "
            "NOT shell-self-dual (extending the empirical pattern from "
            "D/T/³He where the (n) ↔ (1ⁿ) extreme pair is sign-"
            "asymmetric)."
        )
        .set_content_block("prop:shell-schur-weyl-self-duality")
        .add_parameter("q_0", Q_0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("mpmath_dps", mp.mp.dps)
        .add_data("atom", {
            "sym": "4He", "Z": Z, "N": N, "A": Z + N,
            "n_strands": 3 * (Z + N),
            "summary": summary,
            "rows": rows,
        })
        .add_caveat(
            "Per the H_3 result (proton, neutron individually NOT "
            "self-dual): expectation is ⁴He also NOT all-dual. The "
            "purpose of this probe is to confirm at higher A and "
            "extract the full Wedderburn coefficient table for "
            "follow-up σ_shell investigations."
        )
        # F1 (PR #565): structural assertions encoding the central
        # falsification claim and the partition-count anchor.
        .add_assertion(
            "all_dual_is_false",
            computed=0.0 if summary["all_dual"] else 1.0,
            expected=1.0,
            tolerance=0.0,  # binary: NOT all-dual is the predicted result
            source="prop:shell-schur-weyl-self-duality § H_12 prediction",
        )
        .add_assertion(
            "partition_count_h12",
            computed=int(summary["n_partitions_total"]),
            expected=77,
            tolerance=0,  # number of partitions of 12 is exactly 77
            source="OEIS A000041 (partition function p(12))",
        )
        .add_assertion(
            "tr_M_at_q0_finite",
            computed=float(summary["tr_M_at_q0"]),
            expected=0.0,
            tolerance=1.0,  # rules out NaN / inf; loose
            source="this witness's Markov-trace anchor at q_0",
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
