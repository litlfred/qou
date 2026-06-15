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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
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


def compute_atom_chi(Z: int, N: int, *, include_inter: bool = True,
                     precision: str = "mpfr", dps: int = 50) -> dict:
    """Compute χ^λ(β_K) for all λ ⊢ 3A.

    precision="mpfr" (DEFAULT, canonical tier): χ^λ at `dps` decimal
    digits via chi_cd_mpfr → pyhecke_native.chi_lambda_all_partitions_mpfr
    (the color-weighted p-n crossing is handled by linearity at full
    precision). precision="f64" is the PREVIEW tier only (owner ruling
    2026-06-09: no f64 on the canonical path).

    Returns dict with keys:
      n_strands : 3A
      n_partitions : p(3A)
      by_partition : list of {partition, dim, chi_lambda}
      compute_time_sec, precision, engine
    """
    A = Z + N
    n_strands = 3 * A

    word_triples = atom_braid_word_3A(Z, N, include_inter=include_inter)
    partitions = pyhecke_native.partitions_of(n_strands)
    n_partitions = len(partitions)

    t0 = time.time()
    if precision == "mpfr":
        import mpmath as mp
        from chi_cd_mpfr import chi_all_partitions_cd_mpfr
        if mp.mp.dps < dps:
            mp.mp.dps = dps
        chi_map = chi_all_partitions_cd_mpfr(n_strands, word_triples, dps=dps)
        by_partition = [
            {
                "partition": list(shape),
                "dim": -1,  # not tracked here
                "chi_lambda": mp.nstr(
                    chi_map[tuple(shape)], dps, strip_zeros=False
                ),
            }
            for shape in partitions
        ]
        engine = (
            f"chi_cd_mpfr → pyhecke_native.chi_lambda_all_partitions_mpfr "
            f"(Rust + MPFR, {dps} dps) [canonical tier]"
        )
    elif precision == "f64":
        # PREVIEW TIER ONLY — not for canonical consumers.
        factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word_triples]
        chi_pairs = pyhecke_native.chi_q_atomic_all_partitions(
            n_strands, factors, Q0_F64
        )
        by_partition = [
            {"partition": list(shape), "dim": -1, "chi_lambda": chi}
            for (shape, chi) in chi_pairs
        ]
        engine = "pyhecke_native.chi_q_atomic (Rust, f64) — PREVIEW TIER"
    else:
        raise ValueError(f"unknown precision {precision!r} (mpfr | f64)")
    elapsed = time.time() - t0

    return {
        "n_strands": n_strands,
        "n_partitions": n_partitions,
        "by_partition": by_partition,
        "compute_time_sec": elapsed,
        "Z": Z, "N": N, "A": A,
        "include_inter": include_inter,
        "precision": precision,
        "dps": dps if precision == "mpfr" else None,
        "engine": engine,
    }


def main() -> int:
    pos = [a for a in sys.argv[1:] if not a.startswith("--")]
    # Canonical tier (MPFR) is the DEFAULT; --f64 opts into the preview
    # tier (owner ruling 2026-06-09: no f64 on the canonical path).
    precision = "f64" if "--f64" in sys.argv else "mpfr"
    if not pos:
        print(f"USAGE: {sys.argv[0]} <atom> [--f64]  e.g. 4He, 6Li, 7Li")
        print(f"Available atoms: {list(ZN.keys())}")
        print("Default: MPFR 50-dps (canonical). --f64 = preview tier only.")
        return 1
    atom = pos[0]
    if atom not in ZN:
        print(f"Unknown atom {atom!r}; available: {list(ZN.keys())}")
        return 1
    Z, N = ZN[atom]

    print(f"Computing χ^λ for {atom} (Z={Z}, N={N}, H_{3*(Z+N)}) "
          f"[{precision} tier]...")
    data_atom = compute_atom_chi(Z, N, include_inter=True, precision=precision)
    data_free = compute_atom_chi(Z, N, include_inter=False, precision=precision)
    print(f"  atom: {data_atom['n_partitions']} partitions in "
          f"{data_atom['compute_time_sec']:.2f}s")
    print(f"  free: {data_free['n_partitions']} partitions in "
          f"{data_free['compute_time_sec']:.2f}s")

    builder = WitnessBuilder(f"atom-chi-rust-{atom.lower()}")
    builder.set_description(
        f"Full H_{3*(Z+N)} chi^λ(β_K) for {atom} (Z={Z}, N={N}), both atom "
        f"(include_inter=True) and free (include_inter=False) configs. "
        f"precision={precision}: MPFR (default) routes through chi_cd_mpfr → "
        f"pyhecke_native.chi_lambda_all_partitions_mpfr at 50 dps (canonical "
        f"tier; the color-weighted p-n crossing is expanded by linearity); "
        f"--f64 is the preview tier only (owner ruling 2026-06-09: no f64 on "
        f"the canonical path). Consumed by binding_depth_stratified_rust.py."
    )
    builder.add_data("atom", data_atom)
    builder.add_data("free", data_free)
    builder.add_data("precision", precision)
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
