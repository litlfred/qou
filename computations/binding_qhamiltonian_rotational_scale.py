#!/usr/bin/env python3
"""
binding_qhamiltonian_rotational_scale.py — is the binding energy the
q-Hamiltonian ROTATIONAL energy μ₀·ℏ_q·J_q²(j=n/2), with EVERY factor
derived? (Derive-or-refute; NO fitting.)

The q-energy block (climax-volume-mass/q-energy) gives the q-Hamiltonian
  𝔈_q = J_q²·ℏ_q (rotational) + p_q²·ℏ_q/(2[n]_q) (translational) + S_q,
so a q-Reeb rotation is the rotational term J_q²·ℏ_q·μ₀. ALL factors are
substrate-derived:
  μ₀  = m_e / (3·(q−q⁻¹)/2)        — the per-crossing mass scale, fixed so
        the electron (trefoil, 3 crossings) gives m_e (universal-ilp-algorithm)
  ℏ_q = 1 − q⁻¹                     — q-Planck constant
  J_q²(j) = [j]_q[j+1]_q,  j = n/2  — q-angular momentum, highest-weight
        (q-angular-momentum), n = 3A strands

RESULT (honest):
  μ₀ = 1.6295 MeV (DERIVED — NOT the 249 MeV of the earlier draft, which
  mistakenly used the spin-½ quantum j=½ instead of j=n/2). With j=3A/2:

    atom   E_rot = μ₀·ℏ_q·J_q²(n/2)   B_AME    err
    D      2.02                        2.225    −9%
    T      4.36                        8.482   −49%
    ³He    4.36                        7.718   −44%
    ⁴He    7.87                       28.296   −72%

  The DEUTERON binding is reproduced to −9% from FULLY DERIVED quantities
  (zero free parameters) — a second, independent derivation of B_D beside
  the m_e·Vol(𝓑₃)·Δtr endomorphism (+0.19%). But A≥3 undershoots by the
  SAME 44–72% deficit. So the gate is NOT "derive the scale" (μ₀ is
  derived) — it is the per-rep A≥3 structure: the highest-weight j=n/2
  collapses the per-block phase exactly as the scalar trace does. Deriving
  μ₀ does not close A≥3; the residual is unchanged.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-qhamiltonian-rotational-scale", engine="mpmath")

    q = Q_MP
    m_e = mpf(str(M_E_MEV))
    h = q - 1 / q
    hbar_q = 1 - 1 / q
    mu0 = m_e / (3 * h / 2)          # DERIVED per-crossing mass scale

    def br(x):
        return (q**x - q**(-x)) / (q - q**(-1))

    def Jq2(j):
        return br(j) * br(j + 1)

    AME = {"D": (6, float(AME_B_DEUTERON_MEV_VALIDATION)),
           "T": (9, float(AME_B_TRITIUM_MEV_VALIDATION)),
           "3He": (9, float(AME_B_HE3_MEV_VALIDATION)),
           "4He": (12, float(AME_B_HE4_MEV_VALIDATION))}

    print("=" * 70)
    print("q-HAMILTONIAN ROTATIONAL ENERGY  E_rot = μ₀·ℏ_q·J_q²(j=n/2)")
    print("=" * 70)
    print(f"  DERIVED: μ₀ = m_e/(3h/2) = {float(mu0):.4f} MeV ; "
          f"ℏ_q = {float(hbar_q):.4f} ; μ₀·ℏ_q = {float(mu0 * hbar_q):.4f}")
    print(f"  {'atom':5s}{'n':>4s}{'j':>5s}{'J_q²':>9s}"
          f"{'E_rot':>9s}{'B_AME':>9s}{'err':>7s}")
    results = {}
    for iso, (n, B) in AME.items():
        j = mpf(n) / 2
        J = Jq2(j)
        Erot = mu0 * hbar_q * J
        err = float((Erot - B) / B * 100)
        results[iso] = {"n": n, "j": float(j), "Jq2": mp.nstr(J, 8),
                        "E_rot_MeV": mp.nstr(Erot, 8), "B_AME_MeV": B,
                        "err_pct": round(err, 1)}
        print(f"  {iso:5s}{n:>4d}{float(j):>5.1f}{float(J):>9.3f}"
              f"{float(Erot):>9.3f}{B:>9.3f}{err:>+6.0f}%")
    print()
    print("  μ₀ is DERIVED. Deuteron reproduced to −9% from fully-derived")
    print("  quantities (0 free params); A≥3 undershoots 44–72% — the same")
    print("  per-rep deficit. The gate is the A≥3 structure, NOT the scale.")

    wb.set_description(
        "Derive-or-refute: is binding the q-Hamiltonian rotational energy "
        "E_rot = μ₀·ℏ_q·J_q²(j=n/2) with all factors derived? μ₀ = "
        "m_e/(3(q−q⁻¹)/2) ≈ 1.63 MeV (DERIVED, per-crossing scale; the "
        "earlier 249 MeV used the wrong spin-½ quantum). Result: D −9% "
        "(deuteron reproduced from fully-derived quantities, 0 free params), "
        "but T/³He/⁴He undershoot 44–72% — the same per-rep A≥3 deficit. So "
        "the gate is NOT the scale (μ₀ is derived) but the per-rep A≥3 "
        "structure: highest-weight j=n/2 collapses the per-block phase like "
        "the scalar trace. No fit."
    )
    wb.add_data("derived_scales", {
        "mu0_MeV": mp.nstr(mu0, 10), "hbar_q": mp.nstr(hbar_q, 10),
        "mu0_def": "m_e / (3*(q - q^-1)/2)  [per-crossing scale]",
    })
    wb.add_data("rotational_energy_vs_AME", results)
    wb.add_data("conclusion", {
        "mu0_derived": True,
        "deuteron_err_pct": results["D"]["err_pct"],
        "A3_deficit": "T −49%, ³He −44%, ⁴He −72% (same per-rep deficit)",
        "gate": "NOT the scale (μ₀ derived) — the per-rep A≥3 structure; "
                "j=n/2 highest-weight collapses the per-block phase",
        "prior_error_corrected": "earlier draft used spin-½ (j=½) → bogus "
                                 "249 MeV; correct j=n/2 gives derived 1.63 MeV",
    })
    wb.add_assertion(
        "deuteron_rotational_energy_derived_within_10pct",
        computed=abs(results["D"]["err_pct"]),
        expected=9.0,
        tolerance=1.0,
        source="E_rot(D) = μ₀·ℏ_q·J_q²(3) reproduces B_D to −9% with zero "
               "free parameters (μ₀, ℏ_q, J_q² all derived)",
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    wb.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "folio/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    wb.save()


if __name__ == "__main__":
    main()
