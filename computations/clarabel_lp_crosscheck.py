#!/usr/bin/env python3
# polynomial_q_not_applicable: cross-check harness, not a q-compute.
"""Cross-check the MPFR Clarabel operator-selection LP against scipy.

Run this in an environment that HAS scipy + numpy AND the built binary
``clarabel-operator-selection-lp`` (``cargo build --release
--manifest-path tools/hecke-engine/Cargo.toml --features clarabel-mpfr
--bin clarabel-operator-selection-lp``).

It is the acceptance gate for flipping
``pyhecke.lp_dual_solver.solve_operator_selection_lp``'s default backend
from ``"scipy"`` to ``"clarabel"`` (per the ffi-roundtrip-audit /
compute-author discipline: verify equivalence before landing).

For each test LP it solves with BOTH backends and checks:
  * same feasibility,
  * |primal_obj_scipy − primal_obj_clarabel| / |primal_obj| < REL_TOL,
  * same active set (which Frobenius channels are tight),
  * each path independently strong-dual (gap < GAP_TOL).

The two paths only differ in the solver (HiGHS f64 vs Clarabel MPFR);
the LP is identical, so agreement should be at HiGHS' f64 floor (~1e-7),
NOT 1e-25 — the MPFR path is *more* precise, so a small disagreement
is the f64 path's roundoff, not a Clarabel error.  REL_TOL is set
accordingly.  Tighten the Clarabel CLI's solver tolerance (currently
1e-15) toward the f64 disagreement floor if you want bit-agreement.

Usage:
    python3 clarabel_lp_crosscheck.py            # dummy + random suite
    python3 clarabel_lp_crosscheck.py --seeds 50 # more random LPs
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

REL_TOL = 1e-6   # HiGHS f64 vs MPFR agreement floor (f64-limited)
GAP_TOL = 1e-6   # per-path strong-duality gap


def _spd_gram(rng, d):
    """A random symmetric positive-definite Gram (well-conditioned)."""
    import numpy as np

    a = rng.standard_normal((d, d))
    return a @ a.T + d * np.eye(d)


def _compare(t, G, n_target):
    from lp_dual_solver import (
        solve_operator_selection_lp,
        solve_psd_operator_selection_sdp,
    )

    sp = solve_operator_selection_lp(t, G, n_target, backend="scipy")
    cl = solve_operator_selection_lp(t, G, n_target, backend="clarabel")
    # SDP backend: the current PSD lift is diagonal (M(x)=diag(Gx)), so the
    # clarabel SDP path delegates to the LP and must match the scipy LP
    # objective exactly — validatable WITHOUT cvxpy.
    sdp = solve_psd_operator_selection_sdp(t, G, n_target, backend="clarabel")
    return sp, cl, sdp


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=12)
    args = ap.parse_args()

    try:
        import numpy as np
    except ImportError:
        print("FAIL: numpy not available — run this in a scipy+numpy env.")
        return 2

    cases = []
    # The canonical 3-channel dummy.
    cases.append((
        np.array([1.0, 0.5, 0.3]),
        np.array([[1.0, 0.2, 0.1], [0.2, 1.0, 0.3], [0.1, 0.3, 1.0]]),
        1.0,
        "dummy-3ch",
    ))
    # Random SPD-Gram LPs of growing size.
    rng = np.random.default_rng(0)
    for s in range(args.seeds):
        d = 3 + (s % 6)
        cases.append((
            rng.standard_normal(d),
            _spd_gram(rng, d),
            float(rng.uniform(0.5, 2.0)),
            f"rand-{s}-d{d}",
        ))

    n_fail = 0
    print(f"{'case':<14}{'feas':<6}{'rel.obj':>12}{'active==':>10}"
          f"{'gap_cl':>11}{'sdp_rel':>11}")
    print("-" * 66)
    for t, G, n_target, name in cases:
        try:
            sp, cl, sdp = _compare(t, G, n_target)
        except Exception as e:  # noqa: BLE001
            print(f"{name:<14}ERROR: {type(e).__name__}: {e}")
            n_fail += 1
            continue

        feas_ok = sp.feasible == cl.feasible
        if sp.feasible and cl.feasible:
            denom = max(abs(sp.primal_obj), 1e-30)
            rel = abs(sp.primal_obj - cl.primal_obj) / denom
            active_ok = sorted(sp.active_set) == sorted(cl.active_set)
            # SDP (clarabel) must match the scipy LP objective: the lift is
            # diagonal, so SDP ≡ LP.
            sdp_rel = (abs(sp.primal_obj - sdp.primal_obj) / denom
                       if sdp.feasible else float("inf"))
            ok = (feas_ok and rel < REL_TOL and active_ok
                  and sp.duality_gap < GAP_TOL and cl.duality_gap < GAP_TOL
                  and sdp_rel < REL_TOL)
            print(f"{name:<14}{str(feas_ok):<6}{rel:>12.2e}"
                  f"{str(active_ok):>10}{cl.duality_gap:>11.1e}{sdp_rel:>11.2e}"
                  f"  {'OK' if ok else 'FAIL'}")
            if not ok:
                n_fail += 1
        else:
            print(f"{name:<14}{str(feas_ok):<6}{'(infeasible on one/both)':>40}")
            if not feas_ok:
                n_fail += 1

    print("-" * 66)
    if n_fail:
        print(f"\n{n_fail} case(s) FAILED — do NOT flip the default backend.")
        return 1
    print("\nAll cases agree. The clarabel backend matches scipy within "
          f"{REL_TOL:.0e}; safe to consider as default.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
