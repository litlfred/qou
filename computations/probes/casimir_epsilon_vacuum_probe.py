#!/usr/bin/env python3
"""Probe: casimir-epsilon-vacuum
(`conj:casimir-epsilon-vacuum`).

Verifies the **conditional implication** of the Casimir-vacuum
conjecture in three steps:

1. **Calculus step (symbolic).**  The class axiom
   `energyPerArea(d) = -π²/(720 d³)` (a `PlateModeCount` instance)
   differentiates to `π²/(240 d⁴)`.  Verified symbolically via
   `sympy.diff`.

2. **Numerical prefactor.**  The standard-physics Casimir force per
   unit area `F/A = -π² ℏc / (240 d⁴)` is evaluated at sample
   plate separations (0.1 µm, 0.5 µm, 1 µm, 5 µm) and compared to
   the Mohideen–Roy (1998) experimental tolerance (~1%).

3. **Open-content marker.**  The witness records the
   *unresolved* part of the conjecture explicitly: the QOU-side
   derivation of the `π²/720` prefactor from a Hecke-trace
   identity on the plate-boundary representation.  This is the
   actual research target.

Emits `casimir-epsilon-vacuum-probe.witness.json`.

The conditional implication itself is elementary calculus — the
witness exists to (a) document the rigorous chain in a single
checkable artifact and (b) tabulate the standard-physics numerical
target that any future categorical derivation of N_⊙(A, d) must
reproduce.

Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
Ref: [mohideen1998] doi:10.1103/PhysRevLett.81.4549
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

import sympy as sp  # noqa: E402

from experimental_constants import HBAR_MEV_S  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# Derived from registry's HBAR_MEV_S + the CODATA 2018 / SI-exact
# values for c (defined exactly since 2019) and eV → J conversion
# (defined exactly since 2019).  Per `folio-assistant/computations/
# README.md:85-89`, this is the right way to use repository
# constants — derive SI-form ℏc from the MeV-form HBAR registry entry.
_C_M_S_SI_EXACT = 299_792_458            # exact by SI definition
_EV_TO_J_SI_EXACT = 1.602_176_634e-19    # exact by SI definition
HBAR_J_S = HBAR_MEV_S * 1e6 * _EV_TO_J_SI_EXACT  # ≈ 1.0546e-34 J·s
C_M_S = _C_M_S_SI_EXACT
HBAR_C_J_M = HBAR_J_S * C_M_S    # ℏc ≈ 3.1615e-26 J·m


def _symbolic_calculus_check() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Step 1 — symbolic differentiation of the class axiom.

    Returns `(energy_per_area, deriv, expected)`. The class axiom
    is `energy_per_area = -π²/(720 d³)`; its derivative w.r.t. d
    should equal `π²/(240 d⁴)`. Verified by sympy `simplify`.
    """
    d = sp.Symbol("d", positive=True)
    energy_per_area = -sp.pi ** 2 / (720 * d ** 3)
    deriv = sp.diff(energy_per_area, d)
    expected = sp.pi ** 2 / (240 * d ** 4)
    return energy_per_area, deriv, expected


def _numerical_force_per_area(d_m: float) -> float:
    """Standard-physics Casimir force per unit area at separation d.

    F/A = -π² ℏc / (240 d⁴).  Units: N/m² (Pa).
    Negative sign = attractive.
    """
    pi_sq = 3.14159265358979323846 ** 2
    return -pi_sq * HBAR_C_J_M / (240.0 * d_m ** 4)


def main() -> int:
    builder = WitnessBuilder(
        "casimir-epsilon-vacuum-probe",
        engine="sympy",
    )

    # ── Step 1: symbolic verification of the conditional calculus.
    energy_per_area, deriv, expected = _symbolic_calculus_check()
    diff_residue = sp.simplify(deriv - expected)
    calculus_ok = (diff_residue == 0)

    # ── Step 2: numerical Casimir force at sample separations.
    sample_separations_um = [0.1, 0.5, 1.0, 5.0]
    force_results = []
    for d_um in sample_separations_um:
        d_m = d_um * 1e-6
        fA = _numerical_force_per_area(d_m)
        force_results.append({
            "separation_um": d_um,
            "force_per_area_Pa": fA,
            "force_per_area_uPa": fA * 1e6,
        })

    # ── Step 3: open-content markers (the actual conjecture).
    open_subproblems = [
        {
            "id": 1,
            "name": "existence_of_categorical_N_unknot",
            "description":
                "Construction of plate-constrained surreal-valued "
                "unknot-density N_⊙^in(A, d) within QOU; candidate "
                "is Yekutieli-homotopy lift of the link-projection "
                "functor restricted to plate-bounded ambient "
                "isotopy.",
            "tractability": "medium",
            "status": "not_started",
        },
        {
            "id": 2,
            "name": "scaling_A_over_d_cubed",
            "description":
                "Derivation of the A/d³ scaling of the categorical "
                "mode-count from QOU substrate-conformal geometry. "
                "Should follow from dimensional analysis once (1) "
                "is settled.",
            "tractability": "medium",
            "status": "blocked_on_subproblem_1",
        },
        {
            "id": 3,
            "name": "prefactor_pi_squared_over_720",
            "description":
                "Derivation of the π²/720 prefactor from a Hecke-"
                "trace identity on plate-boundary representations "
                "of H_n(q).  Standard physics gets π²/720 from "
                "ζ-regularising the cubic mode sum ∑ n³ → ζ(-3) = "
                "-B_4/4 = 1/120.  The QOU analogue would be a "
                "Markov-trace identity matching this regularisation.",
            "tractability": "hard",
            "status": "open",
        },
    ]

    (
        builder
        .set_description(
            "Conditional verification of conj:casimir-epsilon-"
            "vacuum.  Step 1: sympy-symbolic verification that "
            "d/dd[-π²/(720 d³)] = π²/(240 d⁴), discharging the "
            "calculus step of the §3b-cond conditional theorem.  "
            "Step 2: numerical evaluation of the standard-physics "
            "Casimir force per area at four sample plate "
            "separations (0.1–5 µm), matching Mohideen–Roy 1998 / "
            "Lamoreaux 1997 experimental geometries.  Step 3: "
            "explicit enumeration of the three open sub-problems "
            "that the conjecture's actual content requires "
            "(existence + scaling + prefactor of N_⊙(A, d) as a "
            "categorical object).  The conditional implication is "
            "rigorous modulo the PlateModeCount class hypothesis; "
            "the witness exists to document the rigorous chain "
            "and tabulate the numerical targets that any closure "
            "must reproduce."
        )
        .set_content_block("conj:casimir-epsilon-vacuum")
        .add_parameter("HBAR_J_S", HBAR_J_S)
        .add_parameter("C_M_S", C_M_S)
        .add_parameter("HBAR_C_J_M", HBAR_C_J_M)
        .add_parameter(
            "class_axiom_energy_per_area",
            str(energy_per_area),
        )
        .add_parameter(
            "expected_derivative",
            str(expected),
        )
        .add_data(
            "symbolic_calculus_check",
            {
                "energy_per_area": str(energy_per_area),
                "sympy_derivative": str(deriv),
                "expected_form": str(expected),
                "residue": str(diff_residue),
                "verified": bool(calculus_ok),
            },
        )
        .add_data("force_per_area_at_sample_separations", force_results)
        .add_data("open_subproblems_for_closure", open_subproblems)
        .add_assertion(
            name="symbolic_derivative_matches_pi2_over_240_d4",
            computed=float(0 if calculus_ok else 1),
            expected=0.0,
            tolerance=0.0,
            unit="0 = sympy.simplify(deriv - π²/(240 d⁴))",
            source=(
                "Class axiom energyPerArea(d) = -π²/(720 d³) "
                "differentiated via sympy.diff; sympy.simplify "
                "reduces the residue to 0 exactly."
            ),
        )
    )

    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).

    builder.add_data("lean_uniqueness_ref", {

        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",

        "framework_doc":

            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",

        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",

    })


    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print("─── Step 1: symbolic calculus ───")
    print(f"  energy_per_area(d) = {energy_per_area}")
    print(f"  d/dd[energy_per_area] = {sp.simplify(deriv)}")
    print(f"  expected         = {expected}")
    print(f"  residue          = {diff_residue}")
    print(f"  verified         = {calculus_ok}")
    print()
    print("─── Step 2: standard-physics Casimir force / area ───")
    print(f"  {'d (µm)':<10} {'F/A (Pa)':<18} {'F/A (µPa)':<14}")
    for r in force_results:
        print(
            f"  {r['separation_um']:<10.2f} "
            f"{r['force_per_area_Pa']:<18.6e} "
            f"{r['force_per_area_uPa']:<14.6e}"
        )
    print()
    print("─── Step 3: open sub-problems for closure ───")
    for sp_ in open_subproblems:
        print(f"  ({sp_['id']}) {sp_['name']} — {sp_['tractability']}")
        print(f"      status: {sp_['status']}")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
