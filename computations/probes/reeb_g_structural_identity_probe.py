#!/usr/bin/env python3
"""Structural derivation of the Reeb-flow pn magnitude g — exact identities.

Substantiates (what can be substantiated of) the #3407 claim for

    g = 1/sqrt( 5 + (q0-1)^2/q0 )  ≈ 0.446727

by reducing it to DERIVED constants and exact algebraic identities. With
v = sqrt(q), [2]_v = v + v^{-1} the balanced quantum integer, and
z = 1/[2]_v the canonical Markov-peel bond factor (a derived constant,
b4_1four_complete_graph_writhe_signs.py):

  I1 (polynomial, CommRing):   5 + (v − v⁻¹)² = 1 + (v + v⁻¹)²
      [both sides = (v⁴+3v²+1)/v²; it is (a+b)² − (a−b)² = 4ab with ab = 1]
  I2 (deformed ceiling):       g = 1/sqrt(1 + [2]_v²)
      — the CLASSICAL [1⁴] ss-sector ceiling is 1/sqrt(5) = 1/sqrt(1+2²),
      the eigenvalue of [[1,2],[2,−1]] (pp−nn asymmetry 1, pn-degree 2).
      g is EXACTLY the q-deformed ceiling with the integer pn-degree
      2 → [2]_v: the traceless matrix [[1,[2]_v],[[2]_v,−1]] has
      eigenvalues ±sqrt(1+[2]_v²) = ±1/g.  So g is not merely "below the
      classical ceiling" — it sits AT criticality of the q-deformed
      ss-sector exchange (det(I + g·M_q) = 0), and the classical-S
      headroom 1−√5·g ≈ (v−v⁻¹)²/10 is the substrate deformation.
  I3 (projection form):        g = z/sqrt(1+z²) = sin(arctan z)
      — z is the tangent (crossing density per unit base parameter) of the
      linking inclination; g is its sine (per unit arc length).  tan → sin
      is unit-vector normalization, the natural Reeb-flow arc-length
      measure, and automatically enforces g < 1 and g < ceiling.

I1–I3 are exact (verified 50 dps; I1 is ring-provable).  What REMAINS a
physical identification (not proved here): that the physical magnitude is
the arc-length-normalized component (I3) — equivalently the deformed-
criticality value (I2).  That is ONE assumption, replacing the three
unsubstantiated "routes" of the #3407 audit doc.

RECONCILIATION (linear 5g law vs det form) — decisive, scope-(a):
under B = E0·(−ln det(I+G)) the deuteron needs an effective magnitude
g_eff with 1−g_eff² = exp(−B_AME/E0)  ⇒  g_eff ≈ 0.642 — ABOVE the [1⁴]
ceiling 0.447.  So NO uniform per-pair magnitude makes the det form fit
both A=2 and A=4: the linear B(²H) = 5g law is structurally a separate
assertion.  Its own fingerprint: 5g = μ_cl²·g = μ_cl²/μ_q, so at q→1 it
degenerates to B(²H) = √5 MeV exactly — dimensionally unanchored (the
MeV unit is implicit).  Recorded plainly; no wire/unwire recommendation.

-- Ref: b4_1four_complete_graph_writhe_signs.py (ceiling, z);
categorical_linking_reeb_flow_probe.py (the landed formula);
docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
COMP = str(_COMP)

AME_B_2H = mp.mpf("2.224566")


def main() -> int:
    t0 = time.monotonic()
    q, qi, z = load_q_50dps()
    v = mp.sqrt(q)
    two_v = v + 1 / v                       # [2]_v
    g_landed = 1 / mp.sqrt(5 + (q - 1) ** 2 / q)
    m_e = mp.mpf(str(M_E_MEV))
    E0 = m_e / (q * (q - 1))

    # I1 — polynomial identity (exact, ring-provable)
    i1_lhs = 5 + (v - 1 / v) ** 2
    i1_rhs = 1 + two_v ** 2
    # I2 — deformed ss-ceiling
    g_i2 = 1 / mp.sqrt(1 + two_v ** 2)
    M_q = mp.matrix([[1, two_v], [two_v, -1]])
    mu = mp.eig(M_q)[0]
    mu_max = max(abs(mu[0]), abs(mu[1]))
    # I3 — projection (sin from tan)
    g_i3 = z / mp.sqrt(1 + z * z)
    theta = mp.atan(z)
    # headroom = substrate deformation / 10 (leading order)
    headroom = 1 - mp.sqrt(5) * g_landed
    defo = (v - 1 / v) ** 2

    # Reconciliation: det-form effective magnitude the deuteron would need
    g_eff = mp.sqrt(1 - mp.exp(-AME_B_2H / E0))
    ceiling_cl = 1 / mp.sqrt(5)

    result = {
        "constants": {"q0": mp.nstr(q, 12), "v": mp.nstr(v, 12),
                      "[2]_v": mp.nstr(two_v, 12), "z=1/[2]_v": mp.nstr(z, 12),
                      "g_landed": mp.nstr(g_landed, 15), "E0_MeV": mp.nstr(E0, 8)},
        "I1_polynomial": {"lhs_5+(v-1/v)^2": mp.nstr(i1_lhs, 15),
                          "rhs_1+[2]^2": mp.nstr(i1_rhs, 15)},
        "I2_deformed_ceiling": {"g": mp.nstr(g_i2, 15),
                                "ss_matrix_eig_magnitude": mp.nstr(mu_max, 15),
                                "1/g": mp.nstr(1 / g_landed, 15),
                                "classical_limit_v=1": "1/sqrt(5)"},
        "I3_projection": {"g=z/sqrt(1+z^2)": mp.nstr(g_i3, 15),
                          "theta=arctan_z_rad": mp.nstr(theta, 10),
                          "reading": "g = sin(theta), z = tan(theta); "
                                     "1-g^2 = cos^2(theta) is the A=2 det factor"},
        "headroom_vs_deformation": {"1-sqrt5*g": mp.nstr(headroom, 8),
                                    "(v-1/v)^2/10": mp.nstr(defo / 10, 8)},
        "reconciliation_5g_vs_det": {
            "g_eff_deuteron_needs_under_det_form": mp.nstr(g_eff, 8),
            "classical_ceiling": mp.nstr(ceiling_cl, 8),
            "g_eff_exceeds_ceiling": bool(g_eff > ceiling_cl),
            "linear_law_q_to_1_limit": "B(2H) = sqrt(5) MeV (unit implicit)",
            "verdict": ("scope-(a): no uniform per-pair magnitude serves both "
                        "A=2 and A=4 under the det form; the linear 5g law is "
                        "a separate assertion with an implicit MeV anchor."),
        },
        "remaining_assumption": (
            "ONE physical identification: magnitude = arc-length-normalized "
            "transverse component (I3) ≡ deformed-criticality value (I2). "
            "This replaces the three unsubstantiated #3407 'routes'."),
    }

    payload = {
        "computation": "reeb-g-structural-identity",
        "description": ("Exact structural identities for the Reeb-flow pn magnitude: "
                        "g = 1/sqrt(1+[2]_v^2) = z/sqrt(1+z^2) (q-deformed ss-ceiling / "
                        "sin-from-tan); polynomial identity 5+(v-1/v)^2 = 1+(v+1/v)^2; "
                        "det-vs-linear reconciliation verdict. audit-only."),
        "tier": "structural (exact identities; one named physical identification remains)",
        "result": result,
    }
    wb = WitnessBuilder.wrap_legacy(
        "reeb-g-structural-identity", payload,
        script_path=__file__, engine="python+mpmath",
        output_dir=os.path.join(COMP, "probes"), start_time=t0,
    )
    # I1/I2 are EXACT identities, so their residual is the arithmetic floor,
    # not a physical quantity — it is never bit-identically 0.0 at finite dps.
    # Both carried tolerance=None, which makes Assertion.passed fall back to
    # STRING equality ("7.2445e-71" == "0.0" -> False), so they read as failures
    # the moment the residual stopped landing on a bare zero. Give them the same
    # structural-exactness bar the sibling I3 already uses below (10**-45);
    # the residuals sit 26+ orders of magnitude beneath it, so the threshold is
    # the file's own convention rather than one fitted to these values. Passed
    # as a string per the drained no-float64 convention (qou-t0rf).
    wb.add_assertion("I1_polynomial_identity", computed=mp.nstr(i1_lhs - i1_rhs, 5),
                     expected="0.0", tolerance="1e-45")
    wb.add_assertion("I2_g_equals_inverse_deformed_eig",
                     computed=mp.nstr(abs(g_landed - 1 / mu_max), 5), expected="0.0",
                     tolerance="1e-45")
    wb.add_assertion("I3_g_equals_sin_arctan_z",
                     computed=str(bool(abs(g_landed - g_i3) < mp.mpf(10) ** (-45))),
                     expected="True")
    wb.add_assertion("det_form_deuteron_needs_supercritical_g",
                     computed=str(bool(g_eff > ceiling_cl)), expected="True")
    wb.save(extra={"auditOnly": True})

    print("=== structural identities for g_reeb ===")
    print(f"  g = {float(g_landed):.9f}  =  1/sqrt(1+[2]_v^2)  =  z/sqrt(1+z^2)  [I1-I3 exact]")
    print(f"  deformed ss-ceiling eig = {float(mu_max):.9f} = 1/g  (classical: sqrt5)")
    print(f"  headroom 1-sqrt5*g = {float(headroom):.3e}  ≈  (v-1/v)^2/10 = {float(defo/10):.3e}")
    print(f"  reconciliation: det form needs g_eff = {float(g_eff):.4f} for 2H"
          f"  >  ceiling {float(ceiling_cl):.4f}  ⇒ forms irreconcilable at uniform g")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
