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

# ─────────────────────────────────────────────────────────────────────────────
# ✅ FIXED 2026-11-21 (bean qou-07ts): the kernel now runs at COMPUTE_DPS (70)
# and prints at 50, so the last-place wobble below sits ~20 digits under the
# output. Measured after the fix: D, T and 3He each give ONE output in 10
# consecutive runs (T gave 2 in 10 before it; 3He was stable on that day).
# The old 50-in/50-out strings were wrong in their last 1-2 digits (max rel
# 4.4e-49 vs the guarded value). History of the defect follows.
#
# 🛑 (HISTORICAL) THIS PRODUCER WAS NOT REPRODUCIBLE FOR 3He. Measured 2026-09-05, bean
# `qou-07ts`: eight consecutive runs, same container, same commit, nothing else
# running, produced FOUR DISTINCT outputs. The differences are one unit in the
# last place of the 50-dps `chi_lambda` strings, e.g. ...992028901 -> ...8900.
# The committed value is the modal one (4 of 8).
#
# `D` and `T` were stable over the same runs; `4He` costs 21 minutes and is
# simply unmeasured. It is not "MPFR is loose" — it is specific, and 3He is
# not even the largest case (T has the same n_partitions = 30).
#
# WHAT THIS COSTS YOU. Not precision: a wobble at the 50th significant digit
# is 35 orders below the 1 ppQ (1e-15) L1 target and threatens no physics
# claim. What it costs is ATTRIBUTION. The standard discipline — run the
# producer unmodified first, confirm it reproduces byte-identically, then
# attribute any remaining diff to your change — DOES NOT WORK HERE. A single
# before/after pair will show you a spurious diff. The author of this comment
# nearly attributed one to their own change twice before running the repeat
# test that showed otherwise.
#
# If you need attribution on this producer, run it several times on the
# UNMODIFIED source first and collect the set of outputs, then check whether
# your post-change output falls inside that set.
#
# `computations/witness-reproducibility-check` is the corpus's checker for
# exactly this ("drift" is its word) and does NOT cover this producer — its
# scope is 11 build_*_chain scripts.
# ─────────────────────────────────────────────────────────────────────────────

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
        # Guard digits (bean qou-07ts). The kernel used to run at exactly
        # the `dps` digits it then printed, so a last-place rounding
        # difference in the Rust MPFR accumulation surfaced as a ±1 ulp
        # wobble in the 50th printed digit (3He 2026-09-05; T 2026-11-21,
        # 2 outputs in 10 runs). Computing at COMPUTE_DPS (70, the value
        # the witness's own precisionMetadata already declares) and
        # printing at `dps` keeps that wobble ~20 digits below the output.
        from _precision import COMPUTE_DPS
        work_dps = max(dps + 20, COMPUTE_DPS)
        if mp.mp.dps < work_dps:
            mp.mp.dps = work_dps
        chi_map = chi_all_partitions_cd_mpfr(n_strands, word_triples,
                                             dps=work_dps)
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
            f"(Rust + MPFR, {work_dps} dps, printed at {dps}) [canonical tier]"
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


def _partition_count(n: int) -> int:
    """Number of integer partitions of `n`, computed here.

    Deliberately NOT read back from the kernel whose output it checks: the
    point of the assertion is that the kernel returned p(3A), and taking p
    from the same kernel would restate its answer instead of testing it.
    Standard partition DP, exact integer arithmetic, no float anywhere.
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            dp[i] += dp[i - k]
    return dp[n]


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

    # The assertion this replaces compared `float(data_atom["n_partitions"])`
    # to `data_atom["n_partitions"]` — the same subscript, one wrapped in
    # float(). The residual was identically zero and no value could fail it;
    # the `float()` is also what hid it from the raw-AST tautology census,
    # which compares the two arguments syntactically. Bean `qou-t0wm`;
    # detector `computations/audits/tolerance_from_residual_audit.py`.
    #
    # Its `source` field already named the checkable claim —
    # "pyhecke_native.partitions_of(3A)" — so assert THAT: the kernel returned
    # p(3A) partitions, with p computed here rather than taken from the kernel.
    # Verified against the four committed witnesses before wiring: d 11 = p(6),
    # t 30 = p(9), 3he 30 = p(9), 4he 77 = p(12).
    n_expected = _partition_count(3 * (Z + N))
    for _cfg, _d in (("atom", data_atom), ("free", data_free)):
        builder.add_assertion(
            f"partition_count_is_p_3A_{_cfg}",
            computed=_d["n_partitions"],
            expected=n_expected,
            tolerance=0,
            unit="partition count",
            source=f"independent p(3A) = p({3 * (Z + N)}); kernel is "
                   "pyhecke_native.partitions_of(3A)",
        )

    builder.save()
    print(f"✓ Witness saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
