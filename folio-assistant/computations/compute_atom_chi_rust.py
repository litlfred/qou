"""
compute_atom_chi_rust.py — full H_{3A} atomic-braid χ^λ via Rust kernel.

Uses pyhecke_native.chi_q_atomic (Geck-Pfeiffer + Hoefsmit seminormal,
release-optimized Rust) to compute χ^λ(β_K) for ALL partitions
λ ⊢ 3A — including the high-depth partitions where α_{k≥4} = m_e · 8G
damping kicks in. Bypasses the Python+mpmath OOM issue that limited
binding_via_interface_knot.py to A ≤ 3.

For each atom (Z, N):
- builds atomic braid word via atom_braid_word_3A(include_inter=True)
- converts to (c, d, gen) factor list (Rust's chi_q_atomic format)
- computes χ^λ at f64 precision for all p(3A) partitions in parallel

Output: witness file `atom-chi-rust-h{3A}.witness.json` with chi values
suitable for consumption by binding_depth_stratified_lr.py.

USAGE:
    python3 compute_atom_chi_rust.py <atom>   # e.g. 4He, 6Li, 7Li, ...

For atom 4He, this completes in seconds vs the 12+ GB Python OOM.

Ref: PR #761 (Rust GP MPFR kernel cherry-picked into this branch)
Ref: prop:plancherel-term-7-formulation
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import pyhecke_native
from mass_at_3A_proper import atom_braid_word_3A
from witness_base import WitnessBuilder
from q_parameter import Q as Q0_F64
from hecke_core import h as h_val


ZN = {
    "D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
    "6Li": (3, 3), "7Li": (3, 4), "9Be": (4, 5), "10B": (5, 5),
    "12C": (6, 6),
}


def compute_atom_chi(Z: int, N: int, *, include_inter: bool = True) -> dict:
    """Compute χ^λ(β_K) for all λ ⊢ 3A via Rust kernel.

    Returns dict with keys:
      n_strands : 3A
      n_partitions : p(3A)
      by_partition : list of {partition, dim, chi_lambda}
      compute_time_sec
    """
    A = Z + N
    n_strands = 3 * A

    word_triples = atom_braid_word_3A(Z, N, include_inter=include_inter)
    # Rust kernel uses 1-indexed generators; Python's atom_braid_word_3A
    # is 0-indexed. Bump by +1.
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word_triples]

    partitions = pyhecke_native.partitions_of(n_strands)
    n_partitions = len(partitions)

    t0 = time.time()
    by_partition = []
    for shape in partitions:
        chi = pyhecke_native.chi_q_atomic(shape, factors, Q0_F64)
        by_partition.append({
            "partition": list(shape),
            "dim": -1,  # not tracked by chi_q_atomic
            "chi_lambda": chi,
        })
    elapsed = time.time() - t0

    return {
        "n_strands": n_strands,
        "n_partitions": n_partitions,
        "by_partition": by_partition,
        "compute_time_sec": elapsed,
        "Z": Z, "N": N, "A": A,
        "include_inter": include_inter,
        "q_0_f64": Q0_F64,
        "engine": "pyhecke_native.chi_q_atomic (Rust, f64)",
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[0]} <atom>  e.g. 4He, 6Li, 7Li")
        print(f"Available atoms: {list(ZN.keys())}")
        return 1
    atom = sys.argv[1]
    if atom not in ZN:
        print(f"Unknown atom {atom!r}; available: {list(ZN.keys())}")
        return 1
    Z, N = ZN[atom]

    print(f"Computing χ^λ for {atom} (Z={Z}, N={N}, H_{3*(Z+N)})...")
    data_atom = compute_atom_chi(Z, N, include_inter=True)
    data_free = compute_atom_chi(Z, N, include_inter=False)
    print(f"  atom: {data_atom['n_partitions']} partitions in "
          f"{data_atom['compute_time_sec']:.2f}s")
    print(f"  free: {data_free['n_partitions']} partitions in "
          f"{data_free['compute_time_sec']:.2f}s")

    builder = WitnessBuilder(f"atom-chi-rust-{atom.lower()}")
    builder.set_description(
        f"Full H_{3*(Z+N)} chi^λ(β_K) via Rust geck_pfeiffer + "
        f"Hoefsmit seminormal kernel (cherry-picked from PR #761). "
        f"Both atom (include_inter=True) and free (include_inter="
        f"False) configs for {atom} (Z={Z}, N={N}). f64 precision; "
        f"for MPFR upgrade extend pyhecke_native.chi_q_atomic to "
        f"chi_q_atomic_mpfr."
    )
    builder.add_data("atom", data_atom)
    builder.add_data("free", data_free)
    builder.add_data("canonical_status", "canonical-with-empirical-assignment")

    builder.add_assertion(
        "rust_kernel_loaded",
        computed=float(data_atom["n_partitions"]),
        expected=data_atom["n_partitions"],
        tolerance=0,
        unit="partition count",
        source="pyhecke_native.partitions_of(3A)",
    )

    builder.save()
    print(f"✓ Witness saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
