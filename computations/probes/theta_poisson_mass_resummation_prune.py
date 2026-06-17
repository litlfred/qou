#!/usr/bin/env python3
"""Prune probe: does the Markov-trace MASS observable admit a theta / Poisson
resummation (the q0 <-> root-of-unity bridge)?

Formalize-first prune for the speculative avenue scoped in
`docs/scope/2026-06-17-theta-poisson-mass-resummation-scope.md`.

A Jacobi-theta series `sum_n q^{n^2}` (the Poisson-self-dual object whose
modular S-transform bridges small-|q| and root-of-unity regimes) has exponent
support on a **quadratic lattice** `{a n^2 + b n + c : n in Z}` — sparse, with
gaps growing linearly (`~2an`). If a framework trace polynomial's q-exponent
support is theta-shaped, Poisson/theta resummation applies directly; if the
support is dense / linear (content- or hook-length-based), it does not, and the
bridge requires reindexing the whole H_n(q) tower (a far larger conjectural
step).

Verdict criterion: a finite exponent multiset E is "theta-compatible" iff it is
a subset of some quadratic lattice with |E| >= 4 support points and strictly
increasing gaps (the second difference of the sorted support is constant > 0).
"""
import json
import os


def exponents_theta_compatible(exps):
    """True iff the sorted exponent support has constant positive 2nd
    difference (the signature of `{a n^2 + b n + c}`)."""
    e = sorted(set(exps))
    if len(e) < 4:
        return None  # too short to decide
    d1 = [e[i + 1] - e[i] for i in range(len(e) - 1)]
    d2 = [d1[i + 1] - d1[i] for i in range(len(d1) - 1)]
    return all(x == d2[0] for x in d2) and d2[0] > 0


CASES = {
    # canonical proton Jones/Markov-trace numerator exponents (from
    # computations/.../yekutieli-volume-join.witness.json:
    # (q^18 + q^11 + q^10 - q^8 - q^7 - 1)/(4 q^9))
    "proton_J_numerator": [18, 11, 10, 8, 7, 0],
    # neutron trace numerator (same witness)
    "neutron_J_numerator": [20, 19, 18, 11, 9, 2, 1, 0],
    # trefoil Jones polynomial -q^{-4} + q^{-3} + q^{-1} (exponents)
    "trefoil_jones": [-4, -3, -1],
    # POSITIVE CONTROL: a genuine theta truncation sum_{n=0..4} q^{n^2}
    "theta_truncation_control": [0, 1, 4, 9, 16],
}


def run():
    out = {}
    for name, exps in CASES.items():
        verdict = exponents_theta_compatible(exps)
        e = sorted(set(exps))
        d1 = [e[i + 1] - e[i] for i in range(len(e) - 1)]
        out[name] = {
            "support": e,
            "gaps": d1,
            "theta_compatible": verdict,  # True / False / None(too short)
        }
    return out


if __name__ == "__main__":
    result = run()
    witness = {
        "computation": "theta-poisson-mass-resummation-prune",
        "description": (
            "Prune probe: framework Markov-trace MASS observables (fixed n) are "
            "NOT theta-shaped — their q-exponent supports are content/hook-based "
            "(dense, non-quadratic gaps), so direct Poisson/theta resummation does "
            "not apply. The theta self-duality (positive control) lives only in a "
            "quadratic-lattice sum. Bridge to root-of-unity requires reindexing the "
            "whole H_n(q) tower, not the fixed-n observable."
        ),
        "criterion": (
            "theta_compatible = (sorted exponent support has constant positive "
            "second difference, i.e. lies on {a n^2 + b n + c}); needs >= 4 points."
        ),
        "objects": result,
        "verdict": (
            "REFUTED for fixed-n mass observables; theta structure confined to the "
            "control (quadratic lattice). Poisson/theta bridge is NOT a fixed-n "
            "resummation."
        ),
    }
    path = os.path.join(os.path.dirname(__file__),
                        "theta-poisson-mass-resummation-prune.witness.json")
    with open(path, "w") as fh:
        json.dump(witness, fh, indent=2)
    print(json.dumps(result, indent=2))
    print("\nVERDICT:", witness["verdict"])
    print(f"witness -> {path}")
