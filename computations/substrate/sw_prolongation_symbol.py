"""Keystone consistency test — does the SW prolongation give a fixed-depth
recurrence on the residue weights `a_D^{(n)}`?  (PR #1903)

The keystone conjecture (`conj:qdifference-kernel-prolongation-symbol`,
merged #1871) says the q-difference kernel `R` is the symbol of the
jet-prolongation operator — equivalently, the residue weights `a_D^{(n)}`
obey ONE depth-`d` linear recurrence with `n`-INDEPENDENT coefficients.

This module implements the **falsifiable existence test** (NOT a fit):
`minimal_recurrence(seq)` finds the smallest depth `d` and constant kernel
`c_j` such that `a[n+d] = Σ_{j<d} c_j a[n+j]` for every available window,
or reports `None` if no fixed-depth recurrence of bounded order reproduces
the sequence (which would REFUTE the keystone for the binding series).

Self-validation: the torus trace polynomials
`P_m = cosh((2m+1)η₀)/(2 cosh η₀)` satisfy the Chebyshev depth-2 recurrence
`P_{m+1} = 2 cosh(2η₀)·P_m − P_{m-1}` — the test must recover `d=2`,
`c = [−1, 2 cosh(2η₀)]`. This certifies the machinery on a KNOWN, computable
sequence before consuming the binding `a_D^{(n)}` (which need #1765's
per-knot rule at `n = 2, 3`).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
_sys.path.insert(0, str(_HERE.parent))  # computations/
_sys.path.insert(0, str(_HERE))         # substrate/
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import COMPUTE_DPS  # noqa: E402


def minimal_recurrence(seq, max_depth: int | None = None, tol=None):
    """Smallest depth-`d` constant-coefficient linear recurrence
    `seq[n+d] = Σ_{j<d} c_j seq[n+j]` holding for ALL windows, or None.

    Returns `(d, [c_0, …, c_{d-1}])`. This is a structural existence test:
    `c_j` are solved from the first `d` windows and VERIFIED on the rest;
    drift beyond `tol` means no fixed-depth recurrence (keystone refuted at
    that order)."""
    N = len(seq)
    if tol is None:
        tol = mp.mpf(10) ** (-(COMPUTE_DPS - 8))
    # Falsifiability guarantee: a depth-`d` claim needs ≥ d equations to solve
    # AND ≥ 1 out-of-sample window to verify, i.e. N ≥ 2d+1 ⇒ d ≤ (N-1)//2.
    # Cap `max_depth` at this bound regardless of how it is supplied, so the
    # routine can never degrade into a pure fit (Copilot #1903).
    hard_max = max(0, (N - 1) // 2)  # ≥ 0 even for an empty/short seq
    max_depth = hard_max if max_depth is None else min(max_depth, hard_max)
    for d in range(1, max_depth + 1):
        # Scan for a solvable d×d Hankel window (the first block may be singular
        # by symmetry while a later one is not). Restrict the start `s` so at
        # least one verification window lies beyond the solved block.
        c = None
        for s in range(0, N - 2 * d + 1):
            A = mp.matrix([[seq[s + i + j] for j in range(d)] for i in range(d)])
            b = mp.matrix([seq[s + i + d] for i in range(d)])
            try:
                c = mp.lu_solve(A, b)
                break
            except (ZeroDivisionError, ValueError):
                # singular / numerically-unsuitable window — try the next start
                continue
        if c is None:
            continue
        # Verify the candidate on EVERY window, including the out-of-sample
        # ones. mp.fdot is the precise/efficient accumulator for Σ c_j·seq.
        cj = [c[j] for j in range(d)]
        ok = all(
            abs(mp.fdot(cj, [seq[i + j] for j in range(d)]) - seq[i + d]) <= tol
            for i in range(N - d)
        )
        if ok:
            return d, [c[j] for j in range(d)]
    return None


def _torus_P(m: int, eta0: mp.mpf) -> mp.mpf:
    """Torus trace polynomial P_m = cosh((2m+1)η₀)/(2 cosh η₀)."""
    return mp.cosh((2 * m + 1) * eta0) / (2 * mp.cosh(eta0))


def _emit_witness() -> None:
    from witness_base import WitnessBuilder
    from q_parameter import Q_50_DIGIT_STR as Qs

    mp.mp.dps = COMPUTE_DPS
    q = mp.mpf(Qs)
    eta0 = mp.log(q)
    tol = mp.mpf(10) ** (-(COMPUTE_DPS - 8))

    # Self-validation sequence: torus P_m, m = 1..7 (depth-2 Chebyshev).
    torus = [_torus_P(m, eta0) for m in range(1, 8)]
    rec = minimal_recurrence(torus)
    self_ok = 0
    detail = None
    if rec is not None:
        d, c = rec
        expected_c1 = 2 * mp.cosh(2 * eta0)
        # depth 2, kernel [-1, 2cosh(2η₀)]
        if d == 2 and abs(c[0] + 1) < tol and abs(c[1] - expected_c1) < tol:
            self_ok = 1
        detail = {"depth": d, "c": [mp.nstr(x, 12) for x in c],
                  "expected_c1_2cosh2eta": mp.nstr(expected_c1, 12)}

    w = WitnessBuilder("sw-prolongation-symbol", engine="mpmath")
    w.set_audit_only(
        "docs/workplans/2026-06-05-keystone-prolongation-symbol-derivation.md"
    )
    w.add_parameter("q_0", Qs)
    w.add_data("self_validation_torus_P", detail or {"recurrence": "none"})
    w.add_data("binding_aD_status",
               "only a_D^(4)=Family-A wired; a_D^(2),a_D^(3) gated on #1765 "
               "per-knot λ(L) rule — test deferred until consumed")
    w.add_assertion(
        "machinery_recovers_chebyshev_depth2",
        computed=self_ok, expected=1,
        source="torus P_m → depth-2 recurrence c=[-1, 2cosh(2η₀)] recovered")
    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    mp.mp.dps = COMPUTE_DPS
    from q_parameter import Q_50_DIGIT_STR as Qs
    eta0 = mp.log(mp.mpf(Qs))
    print("Keystone consistency tester (PR #1903)")
    torus = [_torus_P(m, eta0) for m in range(1, 8)]
    rec = minimal_recurrence(torus)
    if rec:
        d, c = rec
        print(f"  self-test (torus P_m): depth {d}, kernel "
              f"[{', '.join(mp.nstr(x, 10) for x in c)}]")
        print(f"  expected depth 2, c=[-1, 2cosh(2η₀)={mp.nstr(2*mp.cosh(2*eta0),10)}]")
    else:
        print("  self-test FAILED to find a fixed-depth recurrence")
    print("  binding a_D^(n): only n=4 wired; needs #1765 a_D^(2),a_D^(3)")
    _emit_witness()
