#!/usr/bin/env python3
"""The octahedral e₂ (where g₂ lives): the exact 2509.02354 construction — g₂ is the finite part of a
χ-coloring quadratic form in the PINCHED (torus-knot/flat) limit. Forward, symbolic, **no fit to g₂**.

CHAIN (read first):
  * PR #4309: the single shape modulus is purely bar-odd (z=1/2 is a Rogers-dilog inflection, Lean-
    proved), so g₂ (bar-even) is entirely the pairwise e₂ coupling of the 4 octahedral tetrahedra
    (FourDilogFirstOrder.e2).
  * 2509.02354 (McPhail-Snyder–Reshetikhin) eq (4.11-4.14): a positive crossing's χ-coloring gives
    FOUR tetrahedron shape-logs
        ζ⁰_r = ε(β₂′−β₁),  ζ⁰_t = ε(β₂−β₁−μ₁),
        ζ⁰_l = ε(β₂−β₁′+μ₂−μ₁),  ζ⁰_b = ε(β₂′−β₁′+μ₂),
    shapes z_j = exp(2πi ζ⁰_j), tetrahedron relation exp(2πi ζ¹_j) = 1/(1−exp(2πi ζ⁰_j)); the
    R-matrix factorizes (4.19) as (1/N) Z_b (Z_r⊗Z_l) Z_t. The amplitudes a_j = log Λ(ζ⁰_j,ζ¹_j) are
    bar-odd (linear in ζ⁰ at leading order); e₂ = Σ_{i<j} a_i a_j is bar-even.

WHAT THIS PROBE ESTABLISHES (all forward; symbolic identities, no coloring fitted):
  A. The OCTAHEDRAL CONSTRAINT ζ⁰_r+ζ⁰_l = ζ⁰_t+ζ⁰_b holds identically ⇒ z_r z_l = z_t z_b (the
     octahedron's edge-gluing). Verified symbolically from the paper formulas.
  B. e₁ = Σ ζ⁰_j is bar-ODD and e₂ = Σ_{i<j} ζ⁰_i ζ⁰_j is bar-EVEN under the bar involution
     ζ⁰_j ↦ −ζ⁰_j (z_j ↦ 1/z_j) — with the REAL paper shapes, confirming FourDilogFirstOrder.e2.
  C. e₂ is an EXPLICIT QUADRATIC FORM in the 6 χ-coloring log-params (β₁,β₂,β₁′,β₂′,μ₁,μ₂). g₂ is its
     value at the deuteron trefoil coloring, in the pinched limit.
  D. PINCHED-LIMIT identification: the deuteron σ₁³ = trefoil is a TORUS knot (flat, PR #4301); its
     crossings are PINCHED (ζ⁰_j ∈ ℤ ⇒ z_j = 1, degenerate). g₂ is the FINITE PART of e₂ in this
     pinched limit (paper §5.2) — NOT the generic-coloring value.

CORRECTION (honest): an earlier note guessed a_r = −a_l (exact conjugate pair). The real formulas
show the r↔l transposition is in the INDEX CONVOLUTION of Z_r/Z_l (sums over n′−n vs n−n′), not the
shapes; ζ⁰_r and ζ⁰_l are independent. Retracted here.

THE WALL (honest, no fishing): computing the numeric g₂ requires (i) solving the trefoil boundary-
parabolic coloring — the 6 log-params pinned by the knot relations (⟨a,b|a²b³⟩) + strand-conjugacy
μ₁=μ₂=μ + substrate μ↔q₀ — and (ii) the pinched-limit finite part. e₂ is a 6-variable quadratic
form; ALL coloring DOF must be pinned rigorously or the residual freedom is the wall. This probe sets
up the form and identifies the obstruction; it does NOT fabricate a coloring to hit g₂ (§2e entropy
bound). scope-(a); nothing wired.

EXPLORATORY — audit + witness only.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    b1, b2, b1p, b2p, m1, m2, eps = sp.symbols("b1 b2 b1p b2p m1 m2 eps")
    # paper 2509.02354 eq (4.11-4.14)
    z0 = {
        "r": eps * (b2p - b1),
        "t": eps * (b2 - b1 - m1),
        "l": eps * (b2 - b1p + m2 - m1),
        "b": eps * (b2p - b1p + m2),
    }
    Z = [z0["r"], z0["t"], z0["l"], z0["b"]]

    # A. octahedral constraint
    constraint = sp.simplify((z0["r"] + z0["l"]) - (z0["t"] + z0["b"]))
    constraint_holds = constraint == 0

    # B. bar-parity (ζ⁰_j ↦ −ζ⁰_j)
    e1 = sum(Z)
    e2 = sum(Z[i] * Z[j] for i in range(4) for j in range(i + 1, 4))
    e1_bar_odd = sp.simplify(sum(-z for z in Z) + e1) == 0
    e2_bar_even = sp.simplify(sum((-Z[i]) * (-Z[j]) for i in range(4) for j in range(i + 1, 4)) - e2) == 0

    # C. e₂ explicit quadratic form (factor ε²)
    e2_form = sp.expand(e2 / eps ** 2)

    # D. pinched limit: strand-conjugacy μ₁=μ₂=μ (single knot component) collapses the form
    mu = sp.symbols("mu")
    e2_conj = sp.expand(e2_form.subs({m1: mu, m2: mu}))
    # count residual free coloring DOF after conjugacy (β's + μ) that still parametrize e2
    free_syms = sorted({str(s) for s in e2_conj.free_symbols}, key=str)

    result = {
        "A_octahedral_constraint": {
            "z0_r+z0_l - (z0_t+z0_b)": str(constraint),
            "holds_identically": bool(constraint_holds),
            "meaning": "z_r·z_l = z_t·z_b (octahedron edge-gluing), from paper eq 4.11-4.14.",
        },
        "B_bar_parity": {
            "e1_bar_odd": bool(e1_bar_odd),
            "e2_bar_even": bool(e2_bar_even),
            "meaning": "with the REAL paper shapes: e₁ bar-odd (μ₀ first order), e₂ bar-even (g₂). "
                       "Confirms FourDilogFirstOrder.e2_bar_even for the actual construction.",
        },
        "C_e2_quadratic_form": {
            "e2_over_eps2": str(e2_form),
            "note": "g₂ = value of this quadratic form at the deuteron trefoil coloring (pinched limit).",
        },
        "D_pinched_limit": {
            "strand_conjugacy": "μ₁=μ₂=μ (single knot component ⇒ conjugate meridians)",
            "e2_after_conjugacy_over_eps2": str(e2_conj),
            "residual_free_coloring_syms": free_syms,
            "pinched": "deuteron trefoil crossings are pinched (ζ⁰∈ℤ, z_j→1, degenerate — torus knot, "
                       "PR #4301). g₂ = finite part of e₂ in the pinched limit (paper §5.2).",
        },
        "correction": {
            "retracted": "earlier a_r = −a_l guess — the r↔l transposition is in the Z_r/Z_l INDEX "
                         "convolution, not the shapes; ζ⁰_r, ζ⁰_l independent.",
        },
        "wall": {
            "to_get_g2": "solve the trefoil boundary-parabolic coloring (6 log-params pinned by "
                         "⟨a,b|a²b³⟩ + μ₁=μ₂ + substrate μ↔q₀) AND take the pinched-limit finite part.",
            "anti_fit": "e₂ is a 6-var quadratic form; ALL coloring DOF must be pinned rigorously or "
                        "the residual freedom is the wall. No coloring fabricated to hit g₂.",
            "scope": "scope-(a): grounds g₂ in the exact paper construction + identifies the pinched-"
                     "limit obstruction; does not derive g₂; nothing wired.",
        },
    }

    payload = {
        "computation": "octahedral-e2-coloring-quadratic",
        "description": ("The octahedral e₂ (where g₂ lives), from 2509.02354 eq (4.11-4.14, 4.19): a "
                        "crossing's χ-coloring gives 4 tetrahedron shape-logs ζ⁰_{r,t,l,b}; the "
                        "octahedral constraint ζ⁰_r+ζ⁰_l=ζ⁰_t+ζ⁰_b holds identically (z_r z_l=z_t z_b); "
                        "e₁ is bar-odd (μ₀), e₂ bar-even (g₂) with the REAL paper shapes. e₂ is an "
                        "explicit quadratic form in the 6 χ-coloring log-params; g₂ is its finite part "
                        "at the deuteron trefoil coloring in the PINCHED limit (torus knot, ζ⁰∈ℤ, "
                        "paper §5.2). Retracts an earlier a_r=−a_l guess. Getting the number needs the "
                        "trefoil coloring solution + pinched limit (all DOF pinned, no fit) — the "
                        "identified wall. scope-(a), audit-only, nothing wired."),
        "audit_only": True,
        "tier": "exact paper construction + symbolic identities (octahedral constraint, e₂ bar-parity, "
                "quadratic form) + pinched-limit obstruction; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, g₂ = octahedral e₂ finite part (pinched limit)",
            "paper": "library/arxiv-2509.02354v2/2509.02354v2.pdf eq (4.11-4.14), (4.19); pinched §5.2",
            "lean": "QOU/MassTheory/FourDilogFirstOrder.lean (e2_bar_even); RogersDilogInflection.lean",
            "builds_on": "PR #4309 (single modulus purely bar-odd), #4301 (deuteron=trefoil), #4127",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "octahedral-e2-coloring-quadratic", payload,
        script_path=__file__, engine="sympy", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("octahedral_constraint_holds", computed=str(bool(constraint_holds)), expected="True")
    wb.add_assertion("e1_bar_odd", computed=str(bool(e1_bar_odd)), expected="True")
    wb.add_assertion("e2_bar_even", computed=str(bool(e2_bar_even)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Octahedral e₂ (where g₂ lives) — 2509.02354 construction ===")
    print(f"A. octahedral constraint ζ⁰_r+ζ⁰_l−(ζ⁰_t+ζ⁰_b) = {constraint}  (holds: {constraint_holds}) "
          f"⇒ z_r z_l = z_t z_b")
    print(f"B. e₁ bar-odd: {e1_bar_odd}   e₂ bar-even: {e2_bar_even}   (REAL paper shapes; confirms "
          f"FourDilogFirstOrder.e2)")
    print(f"C. e₂/ε² = {e2_form}")
    print(f"D. pinched limit (μ₁=μ₂=μ): residual coloring syms = {free_syms}; deuteron trefoil "
          f"crossings PINCHED (ζ⁰∈ℤ) ⇒ g₂ = finite part (paper §5.2)")
    print("WALL: g₂ needs the trefoil coloring solution + pinched limit, all DOF pinned (no fit). "
          "scope-(a). Retracted earlier a_r=−a_l guess.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
