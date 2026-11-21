#!/usr/bin/env python3
"""ut_contact_orientation_probe.py — the contact orientation of UT(ℍ²) and conjugation, exactly (sympy).
Bean `qou-jfx8` (owner 2026-10-12: option 1 only if derivable). Companion to
`QOU/Brings/BringUTContactChirality.lean`, whose `contact_volume_coeff` takes the partial derivatives of the
Liouville form as given; this probe computes them symbolically and checks:

  1. α ∧ dα = −(1/y²) dx∧dy∧dθ for α = (cos θ dx + sin θ dy)/y  (nowhere zero; sign opposite to dx∧dy∧dθ);
  2. the lift (x, y, θ) ↦ (−x, y, π − θ) of z ↦ −z̄ pulls α back to α, with Jacobian determinant +1;
  3. a hyperbolic isometry z ↦ (az + b)/(cz + d) also preserves α (orientation-preserving control), checked on
     the dilation z ↦ λz and the inversion z ↦ −1/z.
Exact symbolic arithmetic; no floats; no q.
-- Ref: [manuscript] bean qou-jfx8; Geiges, An Introduction to Contact Topology, §1.5
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

x, y, t, lam = sp.symbols("x y theta lambda", real=True)
V = [x, y, t]
ALPHA = [sp.cos(t) / y, sp.sin(t) / y, sp.Integer(0)]


def vol(a):
    d = lambda i, j: sp.diff(a[j], V[i]) - sp.diff(a[i], V[j])  # noqa: E731
    return sp.simplify(a[0] * d(1, 2) - a[1] * d(0, 2) + a[2] * d(0, 1))


def pullback(a, F):
    """Pull back the 1-form a under F: (x,y,θ) -> F(x,y,θ)."""
    J = sp.Matrix([[sp.diff(Fi, v) for v in V] for Fi in F])
    sub = dict(zip(V, F))
    a_at = sp.Matrix([ai.subs(sub, simultaneous=True) for ai in a])
    return [sp.simplify(c) for c in (J.T * a_at)], sp.simplify(J.det())


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    v = vol(ALPHA)
    print("alpha ^ d alpha coefficient of dx^dy^dθ:", v)
    check("contact_volume_eq_minus_one_over_y_squared", sp.simplify(v + 1 / y ** 2) == 0, "Lean contact_volume_coeff")
    maps = {
        "conjugation z -> -conj(z)": [-x, y, sp.pi - t],
        "dilation z -> lambda z": [lam * x, lam * y, t],
        # z -> -1/z on the upper half plane: w' = 1/z², so the pushed unit vector has angle θ − 2 arg(z)
        "inversion z -> -1/z": [-x / (x ** 2 + y ** 2), y / (x ** 2 + y ** 2), t - 2 * sp.atan2(y, x)],
    }
    rows = {}
    for name, F in maps.items():
        pb, det = pullback(ALPHA, F)
        r = sp.sqrt(x ** 2 + y ** 2)
        rw = {sp.cos(sp.atan2(y, x)): x / r, sp.sin(sp.atan2(y, x)): y / r}
        same = all(sp.simplify(sp.expand_trig(sp.expand_trig(p - a)).subs(rw)) == 0 for p, a in zip(pb, ALPHA))
        rows[name] = {"pullback_equals_alpha": bool(same), "jacobian_det": str(det)}
        print(f"  {name}: pullback = alpha? {same}   Jacobian det = {det}")
        check(f"isometry_lift_preserves_alpha: {name}", same, "α is metric-defined")
    check("conjugation_lift_is_orientation_preserving", sp.simplify(sp.sympify(rows["conjugation z -> -conj(z)"]["jacobian_det"]) - 1) == 0,
          "Lean iota_lift_det")

    # the geodesic spray R = (y cosθ, y sinθ, −cosθ) is the Reeb field: α(R) = 1, ι_R dα = 0
    R = [y * sp.cos(t), y * sp.sin(t), -sp.cos(t)]
    alphaR = sp.simplify(sum(a * r for a, r in zip(ALPHA, R)))
    dd = lambda i, j: sp.diff(ALPHA[j], V[i]) - sp.diff(ALPHA[i], V[j])  # noqa: E731
    contr = [sp.simplify(sum(R[i] * dd(i, j) for i in range(3))) for j in range(3)]
    comps = {"dxy": sp.simplify(dd(0, 1)), "dxθ": sp.simplify(dd(0, 2)), "dyθ": sp.simplify(dd(1, 2))}
    print("alpha(R) =", alphaR, "  iota_R dalpha =", contr, "  dalpha components:", comps)
    check("geodesic_spray_is_reeb_alpha_R_eq_1", sp.simplify(alphaR - 1) == 0, "Lean reeb_alpha_eq_one")
    check("geodesic_spray_is_reeb_contraction_zero", all(c == 0 for c in contr), "Lean reeb_contraction_zero")
    check("dalpha_components_match_lean_hand_entries",
          sp.simplify(comps["dxy"] - sp.cos(t) / y ** 2) == 0 and sp.simplify(comps["dxθ"] - sp.sin(t) / y) == 0
          and sp.simplify(comps["dyθ"] + sp.cos(t) / y) == 0, "hand-entered derivatives in BringUTContactChirality.lean")
    # vertical geodesic sanity: at θ = π/2 the spray is y ∂_y (the geodesic x = const)
    check("spray_at_theta_pi_over_2_is_vertical_geodesic", [sp.simplify(r.subs(t, sp.pi / 2)) for r in R] == [0, y, 0],
          "x = const is a geodesic of the upper half-plane")

    # the second canonical contact form: Levi-Civita connection form η = dθ + dx/y, Reeb field ∂_θ
    ETA = [1 / y, sp.Integer(0), sp.Integer(1)]
    F = [sp.Integer(0), sp.Integer(0), sp.Integer(1)]
    veta = vol(ETA)
    de = lambda i, j: sp.diff(ETA[j], V[i]) - sp.diff(ETA[i], V[j])  # noqa: E731
    print("eta ^ d eta =", veta, " eta(R) =", sp.simplify(sum(a * r for a, r in zip(ETA, R))),
          " alpha(F) =", sum(a * f for a, f in zip(ALPHA, F)))
    check("fibre_contact_volume_eq_plus_one_over_y_squared", sp.simplify(veta - 1 / y ** 2) == 0, "Lean fibre_contact_volume_coeff")
    check("two_contact_orientations_opposite", sp.simplify(veta + v) == 0, "Lean contact_orientations_opposite")
    check("fibre_is_reeb_of_eta", sp.simplify(sum(e * f for e, f in zip(ETA, F)) - 1) == 0
          and all(sp.simplify(sum(F[i] * de(i, j) for i in range(3))) == 0 for j in range(3)), "η(∂θ) = 1, ι_∂θ dη = 0")
    check("legendrian_duality", sp.simplify(sum(e * r for e, r in zip(ETA, R))) == 0
          and sp.simplify(sum(a * f for a, f in zip(ALPHA, F))) == 0, "Lean legendrian_duality")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("ut-contact-orientation", engine="sympy")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": "differential geometry of the unit tangent bundle of the hyperbolic plane; never reads q",
        "description": ("PROBE (bean qou-jfx8): α ∧ dα = −(1/y²) dx∧dy∧dθ for the Liouville form of the geodesic flow; "
                        "conjugation z ↦ −z̄ lifts to a strict contactomorphism with Jacobian det +1; dilation and "
                        "inversion also preserve α. So UT(Σ₄) carries a canonical contact orientation that conjugation preserves."),
        "contact_volume_coefficient": str(v),
        "isometry_lifts": rows,
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
