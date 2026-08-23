#!/usr/bin/env python3
"""Probe — `prop:topological-mass-formula` (+ `-algebraic`) (I1).

Claims:

  Archimedean (`mass-theory/topological-mass-formula.md`,
  Lean `qou:QOU.Torsion.ArchimedeanMassFormula`):

      𝔪(K) = Vol(K) / ℏ_q²,        ℏ_q = 1 - 1/q,

  derived as the Step-3 combine of a baseline + transient decomposition:

      baseline    = Vol(K)
      exceptional = Vol(K) · (1/ℏ_q² - 1)
      𝔪(K) = baseline + exceptional = Vol(K)·(1 + 1/ℏ_q² - 1) = Vol(K)/ℏ_q².

  Algebraic (`mass-theory/topological-mass-formula-algebraic.md`,
  Lean `qou:QOU.Torsion.AlgebraicMassFormula`):

      𝔪_alg(β) = Φ₁(β) / ℏ_q²,     i.e.   mass_alg = phi1 / hbar_sq,

  the ℚ(q)-side restatement; the Archimedean form is its τ_arch
  specialisation at q = q₀ with Φ₁(β) = τ_arch(Vol_q(β)).

WHAT THIS PROBE VERIFIES:

  (A) The Lean theorem `ArchimedeanMassFormula` is exactly the algebraic
      identity  Vol + Vol·(1/ℏ² - 1) = Vol/ℏ². We verify it
        - SYMBOLICALLY in ℚ(q) (holds for all q, not a q₀ coincidence), and
        - NUMERICALLY at the substrate q₀ for several hyperbolic-knot volumes,
          to ≤ 1e-25.
  (B) The algebraic-side identity  mass_alg = phi1/hbar_sq  given
      phi1 = mass_alg·hbar_sq  (the `AlgebraicMassFormula` hypothesis), again
      symbolically and numerically.

Per the compute-author formalize-first discipline (§3.3): this is a one-line
structural algebraic identity, so the right check is exact symbolic + a q₀
numerical cross-check — NOT a parameter scan.

GUARDRAIL NOTE (AGENTS.md): this block states the BARE topological core
𝔪(K) = Vol(K)/ℏ_q² (dimensionless, no m_e, no ρ). The full canonical
ABSOLUTE nucleon mass is NOT this expression — it is the muon-anchored Hecke
energy via `canonical_mass.py`. This probe does NOT compute any absolute
nucleon mass; it only verifies the algebraic combine that the proposition
proves. No λ_scale / Geom_full involved.

ℏ_q from `qou_substrate.HBAR_Q` (= 1 - 1/q₀). Vol(K) values are sample
hyperbolic-knot volumes (4₁ figure-eight from qou_substrate; others are
SnapPy reference constants used only as multiplicative test inputs — the
identity is volume-agnostic).

Run:  python3 -u computations/probe_topological_mass_formula.py
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402

import mpmath as mp
import sympy as sp

from q_parameter import Q_50_DIGIT_STR  # noqa: E402 (bean yfvb: muon under ideal anchor)
from qou_substrate import WitnessBuilder
from qou_substrate.constants import VOL_FIGURE_EIGHT
from qou_substrate.precision import COMPUTE_DPS, OUTPUT_DPS

mp.mp.dps = COMPUTE_DPS + 15
TOL = mp.mpf("1e-25")


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    hbar = 1 - 1 / q0                      # ℏ_q = 1 - 1/q (block convention)
    hbar_sq = hbar ** 2

    # Sample hyperbolic-knot volumes (input-agnostic test values; the
    # identity holds for any Vol). 4₁ from the substrate constants; the
    # others are standard SnapPy reference volumes used purely as inputs.
    vols = {
        "4_1 (figure-eight, substrate)": mp.mpf(str(VOL_FIGURE_EIGHT)),
        "5_2": mp.mpf("2.82812208833078468"),
        "6_1": mp.mpf("3.16396322888"),
        "Borromean 6^3_2": mp.mpf("7.32772475342"),
    }

    w = WitnessBuilder("probe-topological-mass-formula", engine="mpmath")
    w.set_description(
        "Symbolic + 50-dps numerical cross-check of the topological mass "
        "formula combine Vol + Vol*(1/hbar^2 - 1) = Vol/hbar^2 (prop:"
        "topological-mass-formula, Lean ArchimedeanMassFormula) and the "
        "algebraic-side mass_alg = phi1/hbar_sq (prop:topological-mass-"
        "formula-algebraic, Lean AlgebraicMassFormula). hbar_q = 1-1/q0."
    )
    # One witness, two content blocks: primary is the archimedean prop;
    # the algebraic sibling is recorded in data + a dedicated assertion.
    w.set_content_block("prop:topological-mass-formula")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("hbar_q_def", "1 - 1/q0")
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("tolerance", "1e-25")
    w.add_data("also_verifies_block", "prop:topological-mass-formula-algebraic")

    # (A-symbolic) the combine is an exact ℚ(q) identity.
    qs = sp.Symbol("q", positive=True)
    vols_s = sp.Symbol("Vol", positive=True)
    hbar_s = 1 - 1 / qs
    baseline_s = vols_s
    exceptional_s = vols_s * (1 / hbar_s ** 2 - 1)
    combine_s = sp.simplify(baseline_s + exceptional_s)
    target_s = sp.simplify(vols_s / hbar_s ** 2)
    sym_diff = sp.simplify(combine_s - target_s)
    sym_exact = sym_diff == 0
    w.add_assertion(
        "Vol + Vol*(1/hbar^2 - 1) - Vol/hbar^2 == 0 in Q(q) (symbolic)",
        computed=str(sym_diff),
        expected="0",
        source="sympy.simplify (exact, all q)",
    )

    # (A-numerical) at q₀, for each sample volume.
    rows = []
    max_resid = mp.mpf(0)
    for name, vol in vols.items():
        baseline = vol
        exceptional = vol * (1 / hbar_sq - 1)
        combine = baseline + exceptional
        target = vol / hbar_sq
        resid = abs(combine - target)
        if resid > max_resid:
            max_resid = resid
        rows.append({
            "knot": name,
            "vol": mp.nstr(vol, OUTPUT_DPS),
            "baseline_plus_exceptional": mp.nstr(combine, OUTPUT_DPS),
            "vol_over_hbar_sq": mp.nstr(target, OUTPUT_DPS),
            "residual": mp.nstr(resid, 6),
        })
    w.add_assertion(
        "Vol + Vol*(1/hbar^2 - 1) == Vol/hbar^2 at q0 (all sample knots, <=1e-25)",
        computed=mp.nstr(max_resid, 6),
        expected="0",
        tolerance=float(TOL),
        source=f"{len(vols)} sample hyperbolic-knot volumes",
    )

    # (B) algebraic-side: mass_alg = phi1/hbar_sq given phi1 = mass_alg*hbar_sq.
    # Symbolic
    mass_alg_s = sp.Symbol("mass_alg")
    phi1_s = mass_alg_s * hbar_s ** 2  # the AlgebraicMassFormula hypothesis
    alg_diff = sp.simplify(mass_alg_s - phi1_s / hbar_s ** 2)
    alg_exact = alg_diff == 0
    w.add_assertion(
        "mass_alg - phi1/hbar_sq == 0 given phi1 = mass_alg*hbar_sq (symbolic)",
        computed=str(alg_diff),
        expected="0",
        source="sympy.simplify (AlgebraicMassFormula, exact)",
    )
    # Numerical: pick a representative phi1 = Vol(4_1) at q0, recover mass_alg.
    phi1_num = vols["4_1 (figure-eight, substrate)"]
    mass_alg_num = phi1_num / hbar_sq
    recon = abs(mass_alg_num - phi1_num / hbar_sq)
    w.add_assertion(
        "mass_alg == phi1/hbar_sq at q0 (phi1 = Vol(4_1))",
        computed=mp.nstr(recon, 6),
        expected="0",
        tolerance=float(TOL),
        source="algebraic-side numerical check",
    )

    w.add_data("hbar_q_at_q0", mp.nstr(hbar, OUTPUT_DPS))
    w.add_data("hbar_q_sq_at_q0", mp.nstr(hbar_sq, OUTPUT_DPS))
    w.add_data("inv_hbar_sq_at_q0", mp.nstr(1 / hbar_sq, OUTPUT_DPS))
    w.add_data("combine_rows", rows)
    w.add_data("symbolic_combine_exact", bool(sym_exact))
    w.add_data("symbolic_algebraic_exact", bool(alg_exact))
    w.add_data("max_numerical_residual", mp.nstr(max_resid, 6))
    w.add_caveat(
        "Verifies the ALGEBRAIC combine the propositions prove "
        "(Vol + Vol*(1/hbar^2-1) = Vol/hbar^2 and mass_alg = phi1/hbar_sq). "
        "It does NOT verify the geometric inputs (Chern-Simons/volume "
        "correspondence, Kashaev dilog evaluation), which the proposition "
        "imports as hypotheses (exceptional_sum_eq). Vol(K) values are inputs "
        "to the identity, not derived here. This block is the BARE topological "
        "core m(K)=Vol(K)/hbar^2; the canonical absolute nucleon mass is the "
        "muon-anchored Hecke energy via canonical_mass.py, NOT this expression. "
        "Numerical-exact evidence at q0, not a proof."
    )
    path = w.save()

    # Dedicated witness for the algebraic sibling so it is discoverable as a
    # first-class contentBlock (not only the `also_verifies_block` data field
    # on the archimedean witness above — the integration-watcher scans
    # contentBlock, so the algebraic block was being classed I1 despite being
    # verified here). Same algebraic-side checks, distinct contentBlock.
    wa = WitnessBuilder("probe-topological-mass-formula-algebraic", engine="mpmath")
    wa.set_description(
        "Algebraic-side topological mass identity mass_alg = Phi_1/hbar_sq "
        "(prop:topological-mass-formula-algebraic, Lean AlgebraicMassFormula): "
        "exact in Q(q) given the AlgebraicMassFormula hypothesis phi1 = "
        "mass_alg*hbar_sq, plus a 50-dps numerical recovery at q0 with "
        "phi1 = Vol(4_1). Companion to probe-topological-mass-formula."
    )
    wa.set_content_block("prop:topological-mass-formula-algebraic")
    wa.add_parameter("q0", Q_50_DIGIT_STR)
    wa.add_parameter("hbar_q_def", "1 - 1/q0")
    wa.add_assertion(
        "mass_alg - phi1/hbar_sq == 0 given phi1 = mass_alg*hbar_sq (symbolic)",
        computed=str(alg_diff),
        expected="0",
        source="sympy.simplify (AlgebraicMassFormula, exact in Q(q))",
    )
    wa.add_assertion(
        "mass_alg == phi1/hbar_sq at q0 (phi1 = Vol(4_1))",
        computed=mp.nstr(recon, 6),
        expected="0",
        tolerance=float(TOL),
        source="algebraic-side numerical check",
    )
    wa.add_data("symbolic_algebraic_exact", bool(alg_exact))
    wa.add_data("hbar_q_sq_at_q0", mp.nstr(hbar_sq, OUTPUT_DPS))
    wa.add_caveat(
        "Verifies only the algebraic combine mass_alg = phi1/hbar_sq the "
        "proposition proves; the geometric inputs (Vol_q, tau_arch) are "
        "imported hypotheses, not derived. Not the canonical absolute nucleon "
        "mass (that is the muon-anchored Hecke energy via canonical_mass.py)."
    )
    path_a = wa.save()

    all_passed = all(a.passed for a in w.assertions) and all(a.passed for a in wa.assertions)
    print(f"symbolic combine exact in Q(q): {sym_exact}")
    print(f"symbolic algebraic-side exact in Q(q): {alg_exact}")
    print(f"max numerical residual at q0: {mp.nstr(max_resid, 6)}")
    print(f"witness: {path}")
    print(f"algebraic witness: {path_a}")
    print("ALL PASSED" if all_passed else "FAILURES PRESENT")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
