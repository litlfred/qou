#!/usr/bin/env sage
"""
C_geom from knot invariants — Sage computation.

alpha = tanh(ln q) / C_geom
Target: C_geom ~ 14.25

Run from repo root:
    sage computations/sage-cgeom.sage
"""

import json
import math
from datetime import datetime, timezone

print("=" * 60)
print("C_geom from knot invariants")
print("=" * 60)
print()

# Canonical q from Vol(4_1)/(m_μ/m_e):
VOL_41 = 2.029883212819307
MU_E   = 206.7682830
q_num  = 1.0 / (1.0 - sqrt(VOL_41 / MU_E))  # = 1.10997859...

# ── Jones polynomials via braid closures ─────────────────────────
# Sage constructs knots/links from braid words.

from sage.knots.knot import Knot
from sage.knots.link import Link

# Trefoil: braid word [1, 1, 1] on 2 strands
B2 = BraidGroup(2)
trefoil_braid = B2([1, 1, 1])
K_trefoil = Knot(trefoil_braid)
J_trefoil = K_trefoil.jones_polynomial()
print(f"Trefoil Jones polynomial: {J_trefoil}")

# Mirror trefoil: braid word [-1, -1, -1]
mirror_braid = B2([-1, -1, -1])
K_mirror = Knot(mirror_braid)
J_mirror = K_mirror.jones_polynomial()
print(f"Mirror trefoil Jones polynomial: {J_mirror}")

# Figure-eight: braid word [1, -2, 1, -2] on 3 strands
B3 = BraidGroup(3)
fig8_braid = B3([1, -2, 1, -2])
K_fig8 = Knot(fig8_braid)
J_fig8 = K_fig8.jones_polynomial()
print(f"Figure-eight Jones polynomial: {J_fig8}")

# Hopf link: braid word [1, 1] on 2 strands (2-component link)
hopf_braid = B2([1, 1])
L_hopf = Link(hopf_braid)
J_hopf = L_hopf.jones_polynomial()
print(f"Hopf link Jones polynomial: {J_hopf}")
print()

# ── Borromean rings ──────────────────────────────────────────────
# Borromean rings as braid closure on 6 strands
# Standard representation: sigma_1 sigma_3^{-1} sigma_2^{-1} sigma_4
# repeated to close into 3 components
B6 = BraidGroup(6)
try:
    # Borromean rings: one standard braid representation
    borr_braid = B6([1, -3, -2, 4, 1, -3, -2, 4])
    L_borr = Link(borr_braid)
    J_borr = L_borr.jones_polynomial()
    print(f"Borromean rings Jones polynomial: {J_borr}")
    borr_computed = True
except Exception as e:
    print(f"Borromean computation: {e}")
    print("  Known: J_Borromean = 1 in fundamental rep")
    J_borr = None
    borr_computed = False
print()

# ── Evaluate all Jones polynomials at q = 1.110 ─────────────────
# Sage Jones polynomials use variable 't' — substitute directly
var('t')

print(f"Jones polynomial evaluations at q = {q_num}:")
jones_vals = {}
for name, J in [("trefoil", J_trefoil), ("mirror_trefoil", J_mirror),
                ("figure_eight", J_fig8)]:
    val = float(J.subs(t=q_num))
    jones_vals[name] = {"polynomial": str(J), "value": val}
    print(f"  J_{name}({q_num}) = {val:.6f}")

val_hopf = float(J_hopf.subs(t=q_num))
jones_vals["hopf"] = {"polynomial": str(J_hopf), "value": val_hopf}
print(f"  J_hopf({q_num}) = {val_hopf:.6f}")

if borr_computed and J_borr is not None:
    val_borr = float(J_borr.subs(t=q_num))
    jones_vals["borromean"] = {"polynomial": str(J_borr), "value": val_borr}
    print(f"  J_borromean({q_num}) = {val_borr:.6f}")
print()

# ── Quantum group data ───────────────────────────────────────────
ha = q_num - 1.0/q_num
two_q = q_num + 1.0/q_num
tanh_ln_q = ha / two_q
alpha_target = 1.0 / 137.036
C_geom_target = tanh_ln_q / alpha_target

def q_int(n, q=q_num):
    return (q^n - q^(-n)) / (q - q^(-1))

print(f"Quantum group data at q = {q_num}:")
print(f"  tanh(ln q) = {tanh_ln_q:.6f}")
print(f"  alpha target = {alpha_target:.6f}")
print(f"  C_geom target = {C_geom_target:.4f}")
print(f"  [2]_q = {q_int(2):.6f}")
print(f"  [3]_q = {q_int(3):.6f}")
print(f"  [5]_q = {q_int(5):.6f}")
print(f"  [7]_q = {q_int(7):.6f}")
print()

# ── Test q-integer formulas for C_geom ───────────────────────────
print("Formula candidates for C_geom:")
candidates = {}
borr_val = val_borr if (borr_computed and J_borr is not None) else 1.0
for name, val in [
    ("[2]_q * [7]_q", q_int(2) * q_int(7)),
    ("[3]_q * [5]_q", q_int(3) * q_int(5)),
    ("[2]_q^2 * [3]_q", q_int(2)^2 * q_int(3)),
    ("Sum [2j+1] j=0..2", 1 + q_int(3) + q_int(5)),
    ("[2]_q * [3]_q", q_int(2) * q_int(3)),
    ("[2]_q^4 / [3]_q", q_int(2)^4 / q_int(3)),
    ("J_Borr * [2]_q * [7]_q", borr_val * q_int(2) * q_int(7)),
    ("[2]_q * [7]_q / J_Borr", q_int(2) * q_int(7) / borr_val),
    ("J_Borr * [3]_q * [5]_q", borr_val * q_int(3) * q_int(5)),
    ("[3]_q * [5]_q / J_Borr", q_int(3) * q_int(5) / borr_val),
]:
    alpha_pred = tanh_ln_q / val
    inv_alpha = 1.0 / alpha_pred
    err = abs(inv_alpha - 137.036) / 137.036 * 100
    candidates[name] = {"C_geom": float(val), "1/alpha": float(inv_alpha),
                        "error_pct": float(err)}
    print(f"  {name:25s} = {val:.4f}  ->  1/alpha = {inv_alpha:.2f}  (err {err:.1f}%)")
print()

# ── Colored Jones (adjoint rep) ──────────────────────────────────
# Sage can compute colored Jones polynomials for knots
print("Colored Jones polynomials:")
for n_color, label in [(2, "fundamental"), (3, "adjoint/spin-1"),
                        (4, "spin-3/2"), (5, "spin-2")]:
    try:
        J_col = K_trefoil.colored_jones_polynomial(n_color)
        # colored_jones_polynomial returns a Laurent polynomial, not symbolic
        # Evaluate by substituting into the Laurent polynomial ring
        R_eval = J_col.parent()
        val_col = float(J_col.substitute(q_num))
        print(f"  J_trefoil(n={n_color}, {label}, q={q_num}) = {val_col:.6f}")
        jones_vals[f"trefoil_colored_{n_color}"] = {
            "polynomial": str(J_col), "value": val_col}
    except Exception as e:
        try:
            # Alternative: evaluate the polynomial as a function
            val_col = float(J_col(q_num))
            print(f"  J_trefoil(n={n_color}, {label}, q={q_num}) = {val_col:.6f}")
            jones_vals[f"trefoil_colored_{n_color}"] = {
                "polynomial": str(J_col), "value": val_col}
        except Exception as e2:
            print(f"  n={n_color} ({label}): {e2}")
print()

# ── Assemble witness ─────────────────────────────────────────────
witness = {
    "computation": "sage-cgeom",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "sage_version": sage.version.version,
    "q": q_num,
    "target": {"C_geom": float(C_geom_target), "alpha": alpha_target},
    "jones_polynomials": jones_vals,
    "q_dependent_exact": {"tanh_ln_q": float(tanh_ln_q)},
    "formula_candidates": candidates,
}

import os
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "sage-cgeom.witness.json")
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2, default=str)

print(f"Witness written to {out_path}")
