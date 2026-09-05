#!/usr/bin/env python3
"""charm_mass_tower_probe.py — derive-then-check test of the complex-mass
scaffold's `tower_law` with contRatio = the plain Morgan-Voyce / Fibonacci
continuant ratio b_n / b_{n-2}.

Companion to conj:complex-mass-constituent-functional
(QOU.MassTheory.ComplexMassConstituent). The scaffold's `charm_block_determined`
gives  M(proj 5 s) = contRatio(5) * M(proj 3 s), so if the physical mass is
Re(block), the second-generation/first-generation quark mass ratio should be
contRatio(5). This probe evaluates contRatio at the substrate and compares to
the observed charm/light hierarchy in both the current-mass and
constituent-mass schemes.

RESULT (see verdict below): the plain-continuant-ratio reading of contRatio is
REFUTED (scope-(a)) as the sole hierarchy mechanism — it yields a nearly
geometric ~5.85x-per-generation ladder that matches NEITHER scheme
(undershoots current masses by ~100x, overshoots constituent by ~30%).

PRECISION (2026-08-10). The first version of this probe ran in float64 and
hardcoded a truncated `q0 = 1.10998`. Both are defects under the NO-FLOAT64
family and the q0-anchor rule, and both reached `main` because the precision
gate was never run on the PR that introduced them. Now: every quantity is
`mpmath.mpf` at the repo compute precision, q0 is read from `q_parameter.Q_MP`
(the experimental / proton pin, the standing default for compute per the
2026-08-07 owner directive), and every serialized number goes through
`_precision.fmt`.

The verdict is unchanged by the repair — the mismatch is ~100x and ~30%, which
no sixth-digit shift in q0 can touch.

Emits charm-mass-tower.witness.json.
"""
from __future__ import annotations

import json

import _path_bridge  # noqa: F401
from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

from mpmath import mpf  # noqa: E402

from pathlib import Path as _PathW  # noqa: E402 — witness output root
_HERE_W = _PathW(__file__).resolve().parent


def morgan_voyce_B(n: int, X):
    """F_0=0, F_1=1, F_{n+1} = X*F_n + F_{n-1} (Fibonacci polynomial = the
    T(2,n) Morgan-Voyce continuant, evaluated at argument X)."""
    a, b = mpf(0), mpf(1)
    for _ in range(n):
        a, b = b, X * b + a
    return a


def cont_ratio(n: int, X):
    """contRatio(n) = b_n / b_{n-2}: the scaffold's two-step tower ratio."""
    return morgan_voyce_B(n, X) / morgan_voyce_B(n - 2, X)


def X_for_ratio(target):
    """X > 0 such that contRatio(5, X) = target (monotone bisection).

    Iteration count is tied to the working precision rather than fixed at 200:
    bisection gains ~1 bit per step, so `4*dps` steps clear `10^-dps` with
    room to spare.
    """
    lo, hi = mpf(0), mpf(60)
    for _ in range(4 * set_compute_dps()):
        mid = (lo + hi) / 2
        if cont_ratio(5, mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main() -> None:
    set_compute_dps()

    q0 = Q_MP                          # substrate modulus, experimental (proton) pin
    X_bracket = q0 + 1 / q0            # [2]_q at substrate ~ 2.011 (candidate arg)

    cr5 = cont_ratio(5, X_bracket)     # gen1 -> gen2
    cr7 = cont_ratio(7, X_bracket)     # gen2 -> gen3

    # Observed charm/light hierarchy, two schemes (PDG central values, MeV).
    # String-constructed so no float64 intermediate ever exists.
    targets = {
        "current_mc_over_mu": mpf("1270.0") / mpf("2.2"),            # ~577
        "current_mc_over_md": mpf("1270.0") / mpf("4.7"),            # ~270
        "constituent_mc_over_mlight": mpf("1500.0") / mpf("336.0"),  # ~4.46
    }
    needed_X = {k: X_for_ratio(v) for k, v in targets.items()}

    print(f"substrate X = [2]_q = {fmt(X_bracket, 6)}")
    print(f"contRatio(5) = {fmt(cr5, 5)}   contRatio(7) = {fmt(cr7, 5)}   "
          f"(nearly n-independent -> ~geometric ladder)")
    for k, v in targets.items():
        print(f"  target {k:28s} = {fmt(v, 6):>12s}   needs X ~ {fmt(needed_X[k], 4)}")

    verdict = (
        "scope-(a) REFUTED as sole hierarchy mechanism: contRatio(5) ~ "
        f"{fmt(cr5, 4)} at substrate X=[2]_q~{fmt(X_bracket, 4)} gives a nearly "
        "geometric per-generation ladder that matches neither scheme "
        "(current mc/mu~577 needs X~24, off ~100x; constituent mc/mlight~4.46 "
        "is overshot by ~30%). The observed hierarchy is not a constant "
        "continuant ratio. Missing steepness must come from the complex-volume "
        "/ Chern-Simons (Im) part or a non-continuant contRatio - both OPEN; "
        "no charm mass is predicted."
    )
    print("\nVERDICT:", verdict)

    witness = {
        "schema": "witness/v1-informal",
        "description": "charm_mass_tower_probe: continuant-ratio tower_law vs "
                       "observed charm/light hierarchy (derive-then-check).",
        "producer": "computations/charm_mass_tower_probe.py",
        "consumes": ["conj:complex-mass-constituent-functional"],
        "precision": {
            "engine": "mpmath",
            "dps": set_compute_dps(),
            "q0_anchor": "experimental (proton), q_parameter.Q_MP",
        },
        "inputs": {
            "q0": fmt(q0),
            "X_substrate_bracket_2q": fmt(X_bracket),
        },
        "results": {
            "contRatio_5_at_substrate": fmt(cr5),
            "contRatio_7_at_substrate": fmt(cr7),
            "targets": {k: fmt(v) for k, v in targets.items()},
            "X_needed_for_target": {k: fmt(v) for k, v in needed_X.items()},
        },
        "verdict": verdict,
        "scope": "(a) scope-limited negative: continuant-ratio contRatio alone; "
                 "does NOT exclude the complex-mass functional (Im/CS part "
                 "untested here).",
    }
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(_HERE_W / "charm-mass-tower.witness.json", "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    print("\nwrote computations/charm-mass-tower.witness.json")


if __name__ == "__main__":
    main()
