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

Pure Python (no numpy/sympy). Emits charm-mass-tower.witness.json.
"""
import json


def morgan_voyce_B(n: int, X: float) -> float:
    """F_0=0, F_1=1, F_{n+1} = X*F_n + F_{n-1} (Fibonacci polynomial = the
    T(2,n) Morgan-Voyce continuant, evaluated at argument X)."""
    a, b = 0.0, 1.0
    for _ in range(n):
        a, b = b, X * b + a
    return a


def cont_ratio(n: int, X: float) -> float:
    """contRatio(n) = b_n / b_{n-2}: the scaffold's two-step tower ratio."""
    return morgan_voyce_B(n, X) / morgan_voyce_B(n - 2, X)


def X_for_ratio(target: float) -> float:
    """X > 0 such that contRatio(5, X) = target (monotone bisection)."""
    lo, hi = 0.0, 60.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if cont_ratio(5, mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> None:
    q0 = 1.10998                       # substrate modulus (documented pin)
    X_bracket = q0 + 1.0 / q0          # [2]_q at substrate ~ 2.011 (candidate arg)

    cr5 = cont_ratio(5, X_bracket)     # gen1 -> gen2
    cr7 = cont_ratio(7, X_bracket)     # gen2 -> gen3

    # Observed charm/light hierarchy, two schemes (PDG central values, MeV).
    targets = {
        "current_mc_over_mu": 1270.0 / 2.2,          # ~577
        "current_mc_over_md": 1270.0 / 4.7,          # ~270
        "constituent_mc_over_mlight": 1500.0 / 336.0,  # ~4.46
    }
    needed_X = {k: X_for_ratio(v) for k, v in targets.items()}

    print(f"substrate X = [2]_q = {X_bracket:.4f}")
    print(f"contRatio(5) = {cr5:.3f}   contRatio(7) = {cr7:.3f}   "
          f"(nearly n-independent -> ~geometric ladder)")
    for k, v in targets.items():
        print(f"  target {k:28s} = {v:8.2f}   needs X ~ {needed_X[k]:.2f}")

    verdict = (
        "scope-(a) REFUTED as sole hierarchy mechanism: contRatio(5) ~ "
        f"{cr5:.2f} at substrate X=[2]_q~{X_bracket:.2f} gives a nearly "
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
        "inputs": {"q0": q0, "X_substrate_bracket_2q": X_bracket},
        "results": {
            "contRatio_5_at_substrate": cr5,
            "contRatio_7_at_substrate": cr7,
            "targets": targets,
            "X_needed_for_target": needed_X,
        },
        "verdict": verdict,
        "scope": "(a) scope-limited negative: continuant-ratio contRatio alone; "
                 "does NOT exclude the complex-mass functional (Im/CS part "
                 "untested here).",
    }
    with open("computations/charm-mass-tower.witness.json", "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwrote computations/charm-mass-tower.witness.json")


if __name__ == "__main__":
    main()
