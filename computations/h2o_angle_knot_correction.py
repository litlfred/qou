#!/usr/bin/env python3
# polynomial_q_not_applicable: eigen-phase / Reeb-rotation diagnostic, not a
# Jones-polynomial evaluation.
"""
H₂O bond-angle KNOT-HIERARCHY corrections — Reeb-rotation framework.

Owner direction (2026-06-09): the bond angle is set by a KNOT HIERARCHY —
"first knot sets the first approx of the angle, higher-order knots adjust
it appropriately" — with the **knot operator acting as a torsion / rotation
on the Reeb bundle** (non-abelian Stokes / Yekutieli holonomy; the Hecke
quadratic relation σ²=hσ+1 and det σ=−1 fix the rotation; the GB / jet-order
filtration ranks the knots). This probe grounds that program with the
concrete computed quantities and reports an honest assessment (NO fitting).

LEADING TERM (first knot). The trace-weighted VSEPR angle
(`h2o_bond_angle_magnitude_vsepr.py`, on main) gives θ₀-leading ≈ 107.19°
from the leading Hecke elements (bond = σ, lone = e⁻ = σ₀σ₁σ₀). Observed
104.5°, so the residual to explain is ≈ 2.7°.

CANDIDATE CORRECTION (next knot = figure-eight 4₁). Per
`figure-eight-reeb-rotation.md`, the knot operator
M_{4₁} = (σ₁σ₂⁻¹)² on V_{(2,1)} has unit-modulus eigenvalues e^{±iθ} — a
genuine Reeb rotation, with σ⁻¹ = σ − h from the quadratic relation. This
script computes θ_{4₁} and the per-element Reeb phases of the bond (σ) and
lone (e⁻) operators.

HONEST FINDING (reported, not fitted).
  • θ_{4₁} ≈ 117° is the LEPTON-MIXING rotation (the m_μ mechanism, large) —
    it is NOT the ≈2.7° bond-angle residual, and no clean ratio gives 2.7°
    without fitting. So the correction is NOT the next knot's *raw* rotation.
  • The bond operator σ on V_{(2,1)} is in the GROWTH channel (real
    eigenvalues q, −q⁻¹, |λ|≠1 → NO Reeb phase); the rotation channel only
    opens for alternating (figure-eight-type) sub-braids. Hence the angular
    correction must be the Reeb-PHASE DIFFERENCE between the lone sub-braid
    (dressed into the rotation channel) and the bond sub-braid — the same
    Δ-structure that gave the SIGN (Δtr = hz²). Computing that difference
    needs the bond/lone braids dressed with the 4₁ alternating block, i.e.
    an H₄⁺ seminormal compute — partly blocked here by the missing Rust
    kernel (pyhecke_native). That is the concrete next step, not a fit.

Refs: figure-eight-reeb-rotation.md; three-knot-jet-order-independence.md
(GB/jet-order filtration + Yekutieli non-abelian-Stokes holonomy);
h2o_bond_angle_magnitude_vsepr.py (leading term); reeb_rotation_pn_test.py
(Reeb-phase machinery).
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder
from q_parameter import Q as q0, HA as h
from mass_at_3A_proper import _cached_seminormal, Q0_PROTON

UNIT_TOL = 1e-9
LEADING_DEG = 107.19   # trace-weighted VSEPR leading angle (on main)
OBSERVED_DEG = 104.5


def _phases(M):
    ev = np.linalg.eigvals(M)
    mod = np.abs(ev)
    is_rot = bool(np.all(np.abs(mod - 1.0) < UNIT_TOL))
    return ev, mod, is_rot


def main() -> None:
    # Witness built up front so durationMs covers the compute (per review).
    w = WitnessBuilder("h2o-angle-knot-correction", engine="python")
    sigmas, dim, _ = _cached_seminormal((2, 1), Q0_PROTON)   # V_(2,1), dim 2
    s1, s2 = sigmas[0], sigmas[1]
    I = np.eye(dim)
    s2inv = s2 - h * I                              # σ⁻¹ = σ − h (σ²=hσ+1)

    # figure-eight knot operator M_{4₁} = (σ₁σ₂⁻¹)²
    M41 = np.linalg.matrix_power(s1 @ s2inv, 2)
    ev41, mod41, rot41 = _phases(M41)
    tr41 = float(np.trace(M41).real)
    theta41 = float(np.degrees(np.arccos(np.clip(tr41 / 2, -1, 1))))

    # leading bond (σ) and lone (e⁻ = σ₁σ₂σ₁) operators on V_(2,1)
    bond = s1
    lone = s1 @ s2 @ s1
    evb, modb, rotb = _phases(bond)
    evl, modl, rotl = _phases(lone)
    trl = float(np.trace(lone).real)
    theta_lone = float(np.degrees(np.arccos(np.clip(trl / 2, -1, 1)))) if rotl else None

    residual = LEADING_DEG - OBSERVED_DEG

    print("=" * 70)
    print("H₂O bond-angle knot-hierarchy correction — Reeb rotation")
    print("=" * 70)
    print(f"  q₀={q0:.6f}  h={h:.6f}  dim V_(2,1)={dim}")
    print(f"  leading (first knot) ≈ {LEADING_DEG}°  observed {OBSERVED_DEG}°  "
          f"residual {residual:.2f}°")
    print(f"  θ_4₁ (figure-eight Reeb rotation) = {theta41:.3f}°  "
          f"(rotation channel: {rot41})")
    print(f"  bond σ  |λ|={np.round(modb,4)}  rotation={rotb}  "
          f"(growth → no Reeb phase)")
    print(f"  lone e⁻ |λ|={np.round(modl,4)}  rotation={rotl}")
    print(f"  → θ_4₁ ({theta41:.1f}°) is the lepton-mixing rotation, NOT the "
          f"{residual:.1f}° correction; correction = bond↔lone Reeb-phase Δ "
          f"at the alternating level (H₄⁺, Rust-kernel-blocked here).")

    w.set_description(
        "H₂O bond-angle knot-hierarchy correction probe (Reeb-rotation "
        "framework). Computes the figure-eight Reeb rotation θ_4₁ on V_(2,1) "
        "(=117°, lepton-mixing) and the growth/rotation split of the leading "
        "bond (σ) and lone (e⁻) operators. Honest finding: the residual ≈2.7° "
        "is NOT the next knot's raw rotation; it is the bond↔lone Reeb-phase "
        "difference at the alternating-knot level (H₄⁺ compute, blocked by the "
        "missing Rust kernel). No fitting. Owner's knot-hierarchy direction."
    )
    w.set_content_block("prop:h2o-bond-angle-shift")
    w.add_parameter("q", float(q0))
    w.add_parameter("h", float(h))
    w.add_data("leading_angle_deg", LEADING_DEG)
    w.add_data("observed_angle_deg", OBSERVED_DEG)
    w.add_data("residual_deg", residual)
    w.add_data("theta_4_1_reeb_rotation_deg", theta41)
    w.add_data("theta_4_1_eigenvalues_real", [float(x.real) for x in ev41])
    w.add_data("theta_4_1_eigenvalues_imag", [float(x.imag) for x in ev41])
    w.add_data("bond_sigma_is_rotation_channel", rotb)
    w.add_data("bond_sigma_abs_eigs", [float(x) for x in modb])
    w.add_data("lone_e_minus_is_rotation_channel", rotl)
    w.add_data("lone_e_minus_abs_eigs", [float(x) for x in modl])
    w.add_data("theta_e_minus_lone_reeb_deg", theta_lone)  # = 90° exactly (eigs ±1)
    w.add_assertion(
        "figure-eight knot operator is a Reeb rotation (unit-modulus eigs)",
        computed=rot41, expected=True,
        source="M_4₁=(σ₁σ₂⁻¹)² on V_(2,1); σ⁻¹=σ−h; det=−1 ⇒ e^{±iθ}",
    )
    w.add_assertion(
        "bond operator σ is in the growth channel, not the rotation channel",
        computed=(not rotb), expected=True,
        source="σ eigenvalues q, −q⁻¹ are real with |λ|≠1 — no Reeb phase; "
               "the rotation correction needs alternating (4₁) dressing",
    )
    w.add_data(
        "finding",
        f"θ_4₁ = {theta41:.2f}° (figure-eight Reeb rotation, lepton-mixing) is "
        f"NOT the {residual:.2f}° bond-angle residual and no clean ratio "
        "yields it without fitting. The bond σ is growth (|λ|≠1, no phase); "
        "the rotation channel opens only for alternating sub-braids, so the "
        "angular correction is the bond↔lone Reeb-PHASE DIFFERENCE at the 4₁ "
        "level (mirrors Δtr=hz² for the sign). That difference needs the "
        "bond/lone braids dressed with the figure-eight block — an H₄⁺ "
        "seminormal compute, partly blocked by the missing Rust kernel. "
        "Concrete next step (non-abelian Stokes holonomy difference), not a fit.",
    )
    w.save()
    print("Done. Witness saved (h2o-angle-knot-correction).")


if __name__ == "__main__":
    main()
