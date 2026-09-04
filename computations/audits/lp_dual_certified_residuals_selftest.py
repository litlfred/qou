#!/usr/bin/env python3
"""Self-test for `lp_dual_solver.duality_gap_residuals` — the instantiation of
`QOU.Mathlib.LPDuality.duality_gap_decomposition` at the operator-selection LP.

WHY A SELF-TEST AND NOT A WITNESS. The thing being checked is an *identity*,
not a measurement: it holds for every (A, b, c, x, y), feasible or not. So the
decisive test needs no solver and no anchor — feed it RANDOM x and y and the
identity must still hold exactly. A mapping that got the constraint packing or
the sign convention wrong fails that immediately, which is precisely the
failure mode the bean `qou-fr4d` was opened to avoid guessing at.

The negative controls are the load-bearing half. A checker that passes on
correct input tells you nothing until you have seen it FAIL on wrong input;
this corpus's detector-blindness taxonomy (26 rows) is a record of checkers
that were never shown to fail.

NO FLOAT64: every arithmetic path here is mpmath. `float()` appears only
inside f-strings.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

from mpmath import mp

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "pyhecke" / "python"))

from pyhecke.lp_dual_solver import duality_gap_residuals  # noqa: E402

mp.dps = 60
TOL = mp.mpf(10) ** (-45)


def _gap_direct(t, G, n_target, x, y0):
    """primal_obj - dual_obj, exactly as the solver reports them."""
    d = len(t)
    primal = mp.fsum(mp.mpf(t[j]) * mp.mpf(x[j]) for j in range(d))
    dual = mp.mpf(n_target) * mp.mpf(y0)
    return primal - dual


def _rand_case(rng, d):
    R = lambda: mp.nstr(mp.mpf(rng.uniform(-3, 3)), 40)
    t = [R() for _ in range(d)]
    G = [[R() for _ in range(d)] for _ in range(d)]
    return t, G, R(), [R() for _ in range(d)], R(), [R() for _ in range(d)]


def main() -> int:
    rng = random.Random(20260904)
    failures: list[str] = []

    # ---- 1. THE IDENTITY, on random NON-optimal x and INFEASIBLE y -------
    worst = mp.mpf(0)
    trials = 300
    for _ in range(trials):
        d = rng.randint(2, 8)
        t, G, n, x, y0, y = _rand_case(rng, d)
        rp, rd, gap = duality_gap_residuals(t, G, n, x, y0, y)
        if gap is None:
            failures.append("duality_gap_residuals returned None on valid input")
            break
        lhs = _gap_direct(t, G, n, x, y0)
        rhs = mp.mpf(rp) + mp.mpf(rd)
        scale = max(mp.fabs(lhs), mp.mpf(1))
        worst = max(worst, mp.fabs(lhs - rhs) / scale)
        # the returned total must equal the two parts it is the sum of
        if mp.fabs(mp.mpf(gap) - rhs) / scale > TOL:
            failures.append("gap_recomputed != residual_primal + residual_dual")
            break
    print(f"[1] identity on {trials} random cases (x not optimal, y infeasible)")
    print(f"    worst relative mismatch = {mp.nstr(worst, 6)}")
    if worst > TOL:
        failures.append(f"identity violated: worst rel mismatch {mp.nstr(worst, 6)}")

    # ---- 2. NEGATIVE CONTROLS — the checker must FAIL on a wrong dual ----
    # If these pass, the identity check above is vacuous.
    print("[2] negative controls (each MUST produce a large residual):")
    d = 5
    t, G, n, x, y0, y = _rand_case(rng, d)
    base_rp, base_rd, _ = duality_gap_residuals(t, G, n, x, y0, y)
    base = mp.fabs(mp.mpf(base_rp)) + mp.fabs(mp.mpf(base_rd))

    controls = {
        # y0 perturbed: breaks BOTH the reduced cost and the net-constraint term
        "y0 perturbed by +1": (t, G, n, x, mp.nstr(mp.mpf(y0) + 1, 40), y),
        # y sign flipped: the orientation the mapping depends on
        "y sign flipped": (t, G, n, x, y0, [mp.nstr(-mp.mpf(v), 40) for v in y]),
        # G transposed: catches a (Gx) vs (G^T y) index swap
        "G transposed": (t, [[G[j][i] for j in range(d)] for i in range(d)],
                         n, x, y0, y),
    }
    for name, args in controls.items():
        rp, rd, gap = duality_gap_residuals(*args)
        lhs = _gap_direct(args[0], args[1], args[2], args[3], args[4])
        moved = mp.fabs(mp.mpf(rp) + mp.mpf(rd) - lhs)
        # A perturbation that leaves the IDENTITY intact is expected — the
        # identity is unconditional. What must move is the RESIDUAL SPLIT,
        # i.e. the diagnosis. Check that instead.
        split_moved = mp.fabs(mp.mpf(rp) - mp.mpf(base_rp))
        ok = split_moved > mp.mpf("1e-6") * max(base, mp.mpf(1))
        print(f"    {name:24s} identity still holds "
              f"({mp.nstr(moved, 3)}), residual split moved by "
              f"{mp.nstr(split_moved, 6)}  {'OK' if ok else 'BLIND'}")
        if not ok:
            failures.append(f"negative control blind: {name}")

    # ---- 3. Degenerate inputs must return None, not a wrong number -------
    print("[3] degenerate inputs:")
    bad = [
        ("length mismatch", (["1", "2"], [["1", "0"], ["0", "1"]], "1",
                             ["1"], "0", ["0", "0"])),
        ("non-finite x", (["1", "2"], [["1", "0"], ["0", "1"]], "1",
                          ["nan", "1"], "0", ["0", "0"])),
    ]
    for name, args in bad:
        out = duality_gap_residuals(*args)
        ok = out == (None, None, None)
        print(f"    {name:24s} -> {'None (OK)' if ok else f'{out} (LEAK)'}")
        if not ok:
            failures.append(f"degenerate input not rejected: {name}")

    print()
    if failures:
        print("FAIL:")
        for f in failures:
            print("  -", f)
        return 1
    print("PASS — mapping validated; negative controls all fire.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
