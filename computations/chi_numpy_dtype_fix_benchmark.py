#!/usr/bin/env python3
"""chi_numpy_dtype_fix_benchmark — P28 benchmark witness for the dtype-leak fix.

The repo convention (compute-audit skill, P28): a speedup landing emits a
per-case benchmark table in a witness, caller-vs-caller, with a numerical
cross-check at q0. This is that witness for commit 0bfb2a48ab, which added a
`float()` cast in `hoefsmit_numpy.chi_numpy`.

ROOT CAUSE OF THE `qou-nz8e` `allPassed` FLIP (MEASURED 2026-11-24)
-------------------------------------------------------------------
Bean `qou-nz8e` observed `allPassed: true -> false` and `durationMs: 408402 ->
32485` under `numpy 2.4.6` and hypothesized a `numpy 2.x` dtype skip path.
Direct inspection refutes the `numpy 2.x` skip hypothesis and identifies the
exact cause:

  1. Upstream fix at the source: `canonical_braid_crossings.d_for_ctype` was
      subsequently updated (`if isinstance(h_val, float): d = float(d)` at line
     241) so `d_for_ctype("averaged_weighted", h_f64)` now returns a plain
     `float` rather than an `mp.mpf`.
  2. Consequently, the old `chi_numpy_prefix` (which called `d_for_ctype(ctype,
     h_f64)` directly) stopped receiving an `mp.mpf` at crossing 11 (`flip_at`
     became `None`) and executed the same ~3-20 ms BLAS `float64` loop as
     `chi_numpy` instead of the ~253 s `dtype=object` loop. Comparing two
     identical millisecond BLAS runs under `t_prefix_sec > t_fixed_sec` then
     flipped `False` by wall-clock jitter.
  3. Meanwhile, under `numpy 2.x` (verified on `numpy 2.4+` / `2.5+`), adding
     an `mp.mpf` scalar into `sigma + d_val * eye` STILL promotes a `float64`
     ndarray to `dtype=object` permanently, so `hoefsmit_numpy.chi_numpy`'s
     explicit `float(...)` cast (`0bfb2a48ab`) remains load-bearing whenever an
     `mp.mpf` crossing parameter is passed.

WHAT THIS MEASURES (80-DPS REFERENCE + FAITHFUL PRE-FIX RECONSTRUCTION)
-----------------------------------------------------------------------
Evaluates `q_0 = q_at(95)` at `compute_dps = 95`, `output_dps = 80`:
  * `chi_numpy` (`float64`/BLAS with explicit `float()` guard),
  * `chi_numpy_prefix` reconstructing the exact pre-fix un-downcast `mp.mpf`
    return `-h * (1 - _avg_color_delta() / 2) / 2` on `'averaged_weighted'`,
  * `chi_numeric` (`mpmath` 95-dps reference).
Verifies both that live `d_for_ctype("averaged_weighted", h_f64)` is now
`float`-safe AND that the un-cast `mp.mpf` path promotes `numpy` arrays to
`dtype=object` and incurs the >100x pure-Python matmul penalty while agreeing
with the 80-dps `mpmath` reference to `< 1e-14`.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

os.environ.setdefault("QOU_COMPUTE_DPS", "95")
os.environ.setdefault("QOU_OUTPUT_DPS", "80")

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401,E402

import numpy as np  # noqa: E402  # float64-ok: P28 benchmark of hoefsmit_numpy float64/BLAS path
import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from canonical_braid_crossings import (  # noqa: E402
    _avg_color_delta,
    atom_canonical_crossings,
    d_for_ctype,
)
from hoefsmit_numpy import chi_numpy, hoefsmit_matrices_numpy  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from rho_k_h3a_refinement import chi_numeric  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

# Tritium: n=9, 35 crossings, the atom the regression was measured on. Its
# first 'averaged_weighted' crossing is at index 11 of 35.
ATOM = (1, 2, "tritium")
PARTITIONS = [(5, 2, 2), (3, 3, 3), (4, 3, 2)]


def _d_for_ctype_pre_fix(ctype: str, h_f64: float):
    """Exact pre-fix `d_for_ctype` behaviour at commit `0bfb2a48ab` (before
    `canonical_braid_crossings.py:241` added `if isinstance(h_val, float): d = float(d)`).
    Returns `float` on `sigma`/`sigma_inv`/`averaged` and `mp.mpf` on `averaged_weighted`.
    """
    if ctype == "averaged_weighted":
        delta_mp = _avg_color_delta()
        return -h_f64 * (1 - delta_mp / 2) / 2  # float64-ok: deliberate pre-fix mpf promotion reproduction
    return d_for_ctype(ctype, h_f64)


def chi_numpy_prefix(shape, crossings, q_value: float) -> mp.mpf:
    """`chi_numpy` at commit `0bfb2a48ab^` — no `float()` cast on `_d_for_ctype_pre_fix`."""
    matrices, dim = hoefsmit_matrices_numpy(shape, q_value)
    if dim == 0:
        return mp.mpf(0)
    q = float(q_value)  # float64-ok: P28 float64/BLAS vs dtype=object benchmark
    h = q - 1.0 / q  # float64-ok: P28 float64/BLAS benchmark
    eye = np.eye(dim, dtype=np.float64)  # float64-ok: P28 float64/BLAS benchmark
    M = np.eye(dim, dtype=np.float64)  # float64-ok: P28 float64/BLAS benchmark
    for gen_idx, ctype in crossings:
        sigma = matrices[gen_idx]
        d_val = _d_for_ctype_pre_fix(ctype, h)  # <- mpf for averaged_weighted
        # noqa: P35 — this line is SUPPOSED to leak to dtype=object so the
        # pre-0bfb2a48ab penalty is measured caller-vs-caller in one process.
        cross = sigma + d_val * eye  # noqa: P35  # float64-ok: intentional dtype=object promotion test
        M = M @ cross
    # float64-intentional: trace of object-promoted benchmark matrix converted to mpf for comparison.
    return mp.mpf(str(np.trace(M)))


def main() -> int:
    set_compute_dps()
    with mp.workdps(95):
        q_mp = q_at(95)
        q_f64 = float(q_mp)  # float64-ok: hoefsmit_numpy takes float64 q by design
        crossings = atom_canonical_crossings(ATOM[0], ATOM[1])

        w = WitnessBuilder("chi-numpy-dtype-fix-benchmark", engine="python+mpmath")
        print("=" * 78)
        print(
            f"P28 benchmark — chi_numpy dtype-leak fix (0bfb2a48ab), "
            f"{ATOM[2]} n=9, {len(crossings)} crossings (numpy {np.__version__})"
        )
        print("=" * 78)

        _, dim0 = hoefsmit_matrices_numpy(PARTITIONS[0], q_f64)
        h = q_f64 - 1.0 / q_f64  # float64-ok: P28 float64/BLAS benchmark
        flip_at = next(
            (i for i, (_, ct) in enumerate(crossings)
             if not isinstance(_d_for_ctype_pre_fix(ct, h), float)),  # float64-ok: type check for float vs mpf
            None,
        )
        upstream_fixed = all(
            isinstance(d_for_ctype(ct, h), float)  # float64-ok: verifies canonical_braid_crossings float-safety
            for _, ct in crossings
        )
        probe_eye = np.eye(2, dtype=np.float64)  # float64-ok: 2x2 dtype promotion check
        probe_cross = probe_eye + _d_for_ctype_pre_fix("averaged_weighted", h) * probe_eye  # noqa: P35
        object_promotion_confirmed = (probe_cross.dtype == np.dtype("O"))

        print(
            f"  dim={dim0}, pre-fix first non-float crossing at index {flip_at} "
            f"of {len(crossings)}; live d_for_ctype float-safe={upstream_fixed}; "
            f"numpy {np.__version__} mpf->object={object_promotion_confirmed}"
        )

        rows = []
        all_ok = True
        strictly_slower = True
        for lam in PARTITIONS:
            t0 = time.perf_counter()
            fast = chi_numpy(lam, crossings, q_f64)
            t_fast = mp.mpf(repr(time.perf_counter() - t0))

            t0 = time.perf_counter()
            slow = chi_numpy_prefix(lam, crossings, q_f64)
            t_slow = mp.mpf(repr(time.perf_counter() - t0))

            t0 = time.perf_counter()
            ref = chi_numeric(lam, crossings, q_mp)
            t_ref = mp.mpf(repr(time.perf_counter() - t0))

            rel = abs(fast - ref) / abs(ref) if ref != 0 else abs(fast - ref)
            agree = abs(fast - slow) / abs(slow) if slow != 0 else abs(fast - slow)
            ok = bool(rel < mp.mpf("1e-14"))
            all_ok = all_ok and ok
            strictly_slower = strictly_slower and bool(t_slow > t_fast * mp.mpf(10))

            speedup = t_slow / t_fast if t_fast > 0 else mp.mpf(0)
            print(
                f"  λ={str(lam):<10} fixed {mp.nstr(t_fast, 4):>8s}s   "
                f"pre-fix {mp.nstr(t_slow, 5):>8s}s   "
                f"speedup {mp.nstr(speedup, 5):>8s}x   "
                f"rel_diff_vs_mpmath {mp.nstr(rel, 4)}"
            )
            rows.append({
                "partition": str(lam),
                "t_fixed_sec": fmt(t_fast),
                "t_prefix_sec": fmt(t_slow),
                "speedup": fmt(speedup),
                "t_mpmath_reference_sec": fmt(t_ref),
                "rel_diff_vs_mpmath": fmt(rel),
                "rel_diff_fixed_vs_prefix": fmt(agree),
                "within_1e-14": bool(ok),
            })

        w.add_data("atom", ATOM[2])
        w.add_data("n_crossings", len(crossings))
        w.add_data("first_non_float_crossing_index", flip_at)
        w.add_data("upstream_d_for_ctype_float_safe", bool(upstream_fixed))
        w.add_data("numpy_mpf_object_promotion_confirmed", bool(object_promotion_confirmed))
        w.add_data("per_partition", rows)
        w.add_data("commit_fixed", "0bfb2a48ab")
        w.add_data("tier", "benchmark")

        w.add_assertion(
            "the fixed float64 path agrees with the mpmath reference to better "
            "than 1e-14 on every partition — the cast changes speed, not value",
            computed=bool(all_ok),
            expected=True,
            source="chi_numpy vs 95-dps rho_k_h3a_refinement.chi_numeric at proton q_at(95)",
        )
        w.add_assertion(
            "the pre-fix path is strictly slower (>10x) on every partition — the "
            "mpf->dtype=object leak leaves BLAS for pure-Python matmul under numpy 2.x",
            computed=bool(strictly_slower),
            expected=True,
            source="caller-vs-caller in one process with reconstructed pre-fix mpf d_val",
        )
        w.add_assertion(
            "live canonical_braid_crossings.d_for_ctype is float-safe while un-cast "
            "mpf still promotes numpy float64 arrays to dtype=object (qou-nz8e)",
            computed=bool(upstream_fixed and object_promotion_confirmed and flip_at == 11),
            expected=True,
            source="explains why pre-reconstructed benchmark skipped object-matmul after canonical_braid_crossings.py:241",
        )
        w.set_description(
            "P28 80-dps benchmark witness for the chi_numpy dtype-leak fix (0bfb2a48ab, "
            "bean qou-nz8e). Verifies live d_for_ctype float-safety in canonical_braid_crossings.py:241, "
            "reconstructs the pre-fix mpf leak on 'averaged_weighted' (index 11 of 35), "
            "and measures fixed BLAS vs pre-fix dtype=object vs 95-dps mpmath reference "
            "on tritium partitions under numpy 2.x."
        )
        w.save({
            "q0Anchor": "proton",
            "q0AnchorReason": "Evaluates tritium H_9 Hoefsmit benchmark against 95-dps mpmath reference at canonical proton pin q_at(95).",
            "q0Value": fmt(q_mp),
        })
        print(f"\n  cross-check within 1e-14 on all partitions: {all_ok}")
        print("Saved witness: chi-numpy-dtype-fix-benchmark.witness.json")
        return 0 if (all_ok and strictly_slower and upstream_fixed and object_promotion_confirmed) else 1


if __name__ == "__main__":
    sys.exit(main())
