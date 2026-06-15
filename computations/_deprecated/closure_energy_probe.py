#!/usr/bin/env python3
"""
Closure-energy knot operator probe — investigates the missing
binding-reducing mechanism per the user's hint:

  "real bind via knot operator that reduces binding energy.
   may not be observable not operator"

Per `prop:knot-operator-transition`, each A → A+1 nucleon-addition
operator carries a definite knot type:
  p → D:        single crossing (unknot → σ)
  D → ³H/³He:   Hopf link
  ³ → ⁴He:      trefoil T_{2,3}     ← closure at A=4
  ⁴ → ⁵He / 6Li: 4-crossing (T_{2,4}-step)

The "closure energy" hypothesis (this probe): each completed knot
type contributes binding via its q-Jones polynomial evaluated at
q_0. The trefoil completion at A=4 is the source of 4He's
exceptional binding; non-magic atoms have lower closure energy.

This is a probe, not a derivation. It tests whether the q-Jones
polynomial of the COMPLETION KNOT at each A correlates with the
SEMF binding curve.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, qi0, M_E_MEV, AME_MASS_MEV


def jones_unknot(q):
    """Unknot Jones polynomial: J_0_1(q) = 1."""
    return mpmath.mpf(1)


def jones_hopf_link(q):
    """Hopf link J(q) = -q^(1/2) - q^(5/2). (Reduced bracket.)"""
    return -mpmath.sqrt(q) - q ** mpmath.mpf("2.5")


def jones_trefoil(q):
    """Trefoil J_3_1(q) = -q^(-4) + q^(-3) + q^(-1). (Right-handed.)"""
    return -q ** (-4) + q ** (-3) + q ** (-1)


def jones_t24(q):
    """T(2,4) torus link: q^(-1) + q + q^3 - q^5. Solomon's seal."""
    return q ** (-1) + q + q ** 3 - q ** 5


def jones_t25(q):
    """T(2,5) Cinquefoil J_5_1(q) = -q^(-7) + q^(-6) - q^(-5) + q^(-4) + q^(-2)."""
    return (-q ** (-7) + q ** (-6) - q ** (-5)
            + q ** (-4) + q ** (-2))


def jones_t26(q):
    """T(2,6) Solomon's-seal-extended."""
    return q ** (-1) + q + q ** 3 - q ** 5 - q ** 7 + q ** 9 - q ** 11


# Map A → completion-knot Jones polynomial
# Per prop:knot-operator-transition + atom-knot-mass-derivation
COMPLETION_KNOT_AT_A = {
    1: ("unknot", jones_unknot),
    2: ("σ (single crossing)", lambda q: q ** mpmath.mpf("0.5")),
    3: ("Hopf link", jones_hopf_link),
    4: ("trefoil T(2,3)", jones_trefoil),
    5: ("T(2,4) Solomon", jones_t24),
    6: ("T(2,5) Cinquefoil", jones_t25),
    7: ("T(2,5) (+1)", jones_t25),
    8: ("T(2,5) (+2)", jones_t25),  # placeholder: T(2,5) extended
    9: ("T(2,5) (+3)", jones_t25),
    12: ("T(2,5) (+6)", jones_t25),
    16: ("T(2,6) extended", jones_t26),
    40: ("T(2,5) (very extended)", jones_t25),
}


def closure_energy_at_q0(A: int) -> dict:
    """Closure energy = |J_K(q_0)| where K is the completion knot at A."""
    name, fn = COMPLETION_KNOT_AT_A.get(
        A, (f"placeholder T(2,?) at A={A}", jones_t25))
    j = fn(q0)
    return {
        "A": A,
        "knot_name": name,
        "jones_at_q0": float(j),
        "abs_jones": float(abs(j)),
    }


def per_nucleon_binding_AME(A: int, ame: float) -> float:
    """AME mass per nucleon — dimensionless analog to SEMF binding."""
    M_P_MEV = 938.272
    return M_P_MEV - ame / A   # binding per nucleon


if __name__ == "__main__":
    print("=" * 88)
    print("Closure-energy knot operator probe")
    print("=" * 88)
    print(f"q_0 = {q0}")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5),
        ("12C", 6, 6), ("16O", 8, 8), ("40Ca", 20, 20),
    ]

    print(f"  {'atom':>5} {'A':>3} {'completion knot':>22} "
          f"{'|J(q_0)|':>10} {'binding/nucleon':>18}")
    print("  " + "-" * 70)
    rows = []
    for name, Z, N in ATOMS:
        A = Z + N
        ce = closure_energy_at_q0(A)
        bn = per_nucleon_binding_AME(A, AME_MASS_MEV[name])
        print(f"  {name:>5} {A:>3} {ce['knot_name']:>22} "
              f"{ce['abs_jones']:>10.4f} {bn:>18.4f}")
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            **ce,
            "binding_per_nucleon_MeV": bn,
        })

    # Correlation probe
    import numpy as np
    closures = np.array([r["abs_jones"] for r in rows])
    bindings = np.array([r["binding_per_nucleon_MeV"] for r in rows])
    if len(closures) > 1:
        corr = np.corrcoef(closures, bindings)[0, 1]
        print()
        print(f"  Correlation |J(q_0)| vs binding/nucleon: {corr:+.4f}")
        print(f"  (positive ⇒ larger closure energy at higher binding)")

    out = {
        "computation": "closure-energy-knot-operator-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0": float(q0),
        "atoms": rows,
        "correlation_jones_vs_binding": (
            float(corr) if len(closures) > 1 else None),
        "interpretation": (
            "Per prop:knot-operator-transition, each A → A+1 transition "
            "adds a definite knot type whose closure may carry a binding "
            "energy. This probe correlates |J_K(q_0)| with the AME "
            "per-nucleon binding to test the hypothesis that closure "
            "energy ~ binding enhancement at knot completion."
        ),
    }
    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-closure-energy-probe.witness.json")
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
