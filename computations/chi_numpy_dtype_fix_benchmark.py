#!/usr/bin/env python3
"""chi_numpy_dtype_fix_benchmark — P28 benchmark witness for the dtype-leak fix.

The repo convention (compute-audit skill, P28): a speedup landing emits a
per-case benchmark table in a witness, caller-vs-caller, with a numerical
cross-check at q0. This is that witness for commit 0bfb2a48ab, which added a
`float()` cast in `hoefsmit_numpy.chi_numpy`.

WHAT WAS WRONG
--------------
`d_for_ctype` returns a plain `float` for 'sigma' / 'sigma_inv' / 'averaged'
and an mpmath `mpf` for 'averaged_weighted'. In the accumulating product

    cross = sigma + d_val * eye
    M = M @ cross

one `mpf` promotes `cross` to dtype=object; `M` is reassigned from it, so M
stays dtype=object for every remaining crossing and the loop leaves BLAS for
pure-Python matmul permanently. Silent, correct, and sticky.

WHAT THIS MEASURES
------------------
For each partition: the fixed `chi_numpy` (float64/BLAS), a faithful
reconstruction of the pre-fix behaviour (identical code with the cast
removed), and the mpmath reference `chi_numeric`. Reports the speedup and the
relative difference against the reference.

The pre-fix path is reconstructed here rather than measured from git history
so the comparison is same-process, same-machine, same-inputs — a caller-vs-
caller measurement, per P28, not a comparison of two different runs.

Run:
    python3 -u computations/chi_numpy_dtype_fix_benchmark.py 2>&1 | tee /tmp/chi_bench.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401,E402

import numpy as np  # noqa: E402
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from canonical_braid_crossings import (  # noqa: E402
    atom_canonical_crossings, d_for_ctype,
)
from hoefsmit_numpy import chi_numpy, hoefsmit_matrices_numpy  # noqa: E402
from rho_k_h3a_refinement import chi_numeric  # noqa: E402

# Tritium: n=9, 35 crossings, the atom the regression was measured on. Its
# first 'averaged_weighted' crossing is at index 11 of 35.
ATOM = (1, 2, "tritium")
PARTITIONS = [(5, 2, 2), (3, 3, 3), (4, 3, 2)]


def chi_numpy_prefix(shape, crossings, q_value):
    """chi_numpy exactly as it was BEFORE 0bfb2a48ab — no float() cast.

    Kept byte-for-byte parallel to the fixed version so the only difference
    measured is the cast itself.
    """
    matrices, dim = hoefsmit_matrices_numpy(shape, q_value)
    if dim == 0:
        return mp.mpf(0)
    q = float(q_value)
    h = q - 1.0 / q
    eye = np.eye(dim, dtype=np.float64)
    M = np.eye(dim, dtype=np.float64)
    for gen_idx, ctype in crossings:
        sigma = matrices[gen_idx]
        d_val = d_for_ctype(ctype, h)      # <- the leak: mpf for averaged_weighted
        # noqa: P35 — this line is SUPPOSED to leak. It is the pre-fix code
        # under measurement; casting here would delete the thing being timed.
        cross = sigma + d_val * eye  # noqa: P35
        M = M @ cross
    return mp.mpf(float(np.trace(M)))


def main() -> int:
    mp.mp.dps = 50
    q_mp = mp.mpf(Q_50_DIGIT_STR)
    q_f64 = float(q_mp)
    crossings = atom_canonical_crossings(ATOM[0], ATOM[1])

    w = WitnessBuilder("chi-numpy-dtype-fix-benchmark", engine="python")
    print("=" * 78)
    print(f"P28 benchmark — chi_numpy dtype-leak fix (0bfb2a48ab), "
          f"{ATOM[2]} n=9, {len(crossings)} crossings")
    print("=" * 78)

    # Where does the dtype actually flip? Report it rather than assert it.
    matrices, dim = hoefsmit_matrices_numpy(PARTITIONS[0], q_f64)
    h = q_f64 - 1.0 / q_f64
    flip_at = next((i for i, (_, ct) in enumerate(crossings)
                    if not isinstance(d_for_ctype(ct, h), float)), None)
    print(f"  dim={dim}, first non-float crossing at index {flip_at} "
          f"of {len(crossings)}")

    rows, all_ok = [], True
    for lam in PARTITIONS:
        t = time.time(); fast = chi_numpy(lam, crossings, q_f64); t_fast = time.time() - t
        t = time.time(); slow = chi_numpy_prefix(lam, crossings, q_f64); t_slow = time.time() - t
        t = time.time(); ref = chi_numeric(lam, crossings, q_mp); t_ref = time.time() - t

        rel = abs(fast - ref) / abs(ref) if ref != 0 else abs(fast - ref)
        agree = abs(fast - slow) / abs(slow) if slow != 0 else abs(fast - slow)
        ok = rel < mp.mpf("1e-14")
        all_ok &= bool(ok)

        speedup = t_slow / t_fast if t_fast > 0 else float("inf")
        print(f"  λ={str(lam):<10} fixed {t_fast:7.3f}s   pre-fix {t_slow:8.3f}s   "
              f"speedup {speedup:8.1f}x   rel_diff_vs_mpmath {mp.nstr(rel, 3)}")
        rows.append({
            "partition": str(lam),
            "t_fixed_sec": fmt(t_fast),
            "t_prefix_sec": fmt(t_slow),
            # float64-intentional: a wall-clock ratio. The timings ARE
            # doubles; there is no exact route to a benchmark measurement.
            "speedup": fmt(speedup),
            "t_mpmath_reference_sec": fmt(t_ref),
            "rel_diff_vs_mpmath": mp.nstr(rel, 6),
            "rel_diff_fixed_vs_prefix": mp.nstr(agree, 6),
            "within_1e-14": bool(ok),
        })

    w.add_data("atom", ATOM[2])
    w.add_data("n_crossings", len(crossings))
    w.add_data("first_non_float_crossing_index", flip_at)
    w.add_data("per_partition", rows)
    w.add_data("commit_fixed", "0bfb2a48ab")
    w.add_data("tier", "benchmark")

    w.add_assertion(
        "the fixed float64 path agrees with the mpmath reference to better "
        "than 1e-14 on every partition — the cast changes speed, not value",
        computed=all_ok, expected=True,
        source="chi_numpy vs rho_k_h3a_refinement.chi_numeric at substrate q0; "
               "1e-14 is the tolerance hoefsmit_numpy's own docstring documents",
    )
    w.add_assertion(
        "the pre-fix path is strictly slower on every partition — the leak "
        "cost real time rather than being a theoretical concern",
        computed=all(float(r["t_prefix_sec"]) > float(r["t_fixed_sec"])
                     for r in rows),
        expected=True,
        source="same process, same machine, same inputs; the only difference "
               "between the two callers is the float() cast",
    )
    w.set_description(
        "P28 benchmark witness for the chi_numpy dtype-leak fix (0bfb2a48ab). "
        "d_for_ctype returns mpf for 'averaged_weighted' and float otherwise; "
        "one mpf promotes the accumulating numpy product to dtype=object, which "
        "drops the remaining matmuls out of BLAS into pure Python permanently. "
        "Measures fixed vs pre-fix vs mpmath reference on tritium partitions, "
        "caller-vs-caller in one process. Value is unchanged; only speed moves."
    )
    # q0 anchor: this benchmark DOES read q₀ — `Q_50_DIGIT_STR` comes straight
    # from `q_parameter` in this file. The pin is the experimental/proton one:
    # `q_parameter` is not unconditionally muon, it is manifest-driven
    # (`QOU_Q0_ANCHOR` override, else the producer's stem under `ideal_muon`,
    # else proton), and this stem is absent from
    # `computations/q0_anchor_manifest.json`, so it takes the standing proton
    # default of the 2026-08-07 owner directive. Confirmed via
    # `resolve_q0_anchor`, not inferred from the layer (bean qou-kx04).
    w.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"\n  cross-check within 1e-14 on all partitions: {all_ok}")
    print("Saved witness: chi-numpy-dtype-fix-benchmark.witness.json")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
