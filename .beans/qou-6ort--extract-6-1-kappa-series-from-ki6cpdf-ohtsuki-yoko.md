---
# qou-6ort
title: Extract 6_1 kappa-series from ki6c.pdf (Ohtsuki-Yokota 6-crossing) — Ohtsuki-tower third-knot leg
status: todo
type: task
created_at: 2026-08-15T11:35:54Z
updated_at: 2026-08-15T11:35:54Z
---


## 2026-08-15 extraction pass (pypdf; uploads/ki6c.pdf = Ohtsuki-Yokota,
## "Kashaev invariant of the knots with 6 crossings", 72pp)

WHAT THE PAPER SUPPLIES for 6_1 (mirror 6bar_1 convention; 6_1 values
are complex conjugates):
- Leading exponent: sigma(6bar_1) = 0.5035603... - i*1.08078...
  (Re = Vol(6_1)/2pi checked: 3.16396.../2pi = 0.5035603 OK)
- omega(6bar_1) = -0.52139... + i*0.071732...  (eq on p.15; omega^2
  relates to twisted Reidemeister torsion per their [22])
- EXACT saddle data (p.18-19): gluing equations (1-x)^2 = -x^3 y^2 z,
  1-y = x^2 y^2 z, 1-z = -xyz; z' quartic 2z'^4 - z'^3 - 2z'^2 + z' + 1
  = 0; numeric saddle x0 = 0.895123+i*1.55249, y0 = 0.17385+i*1.06907,
  z0 = 0.322042+i*0.15778 (t0,s0,u0 also given)
- Exact Hessian H0 (their eq 42) in x0,y0,z0.

WHAT IT DOES NOT SUPPLY: the kappa_i(6_1) numeric values — unlike the
5_2 paper (which tabulated kappa_1..kappa_4), here the higher
coefficients exist by Theorem 1.1 + Prop 2.6 but are not printed.

COMPUTE PATH (follow-on probe, session-scale): implement Prop 2.6's
formal Gaussian expansion on their explicit potential V-hat (2Li2(x) +
Li2(y) + Li2(z) + quadratic, p.19 eq 40) at the given saddle: Newton
from their numeric seed at 60 dps, then the order-hbar correction gives
kappa_1(6_1) — the Ohtsuki-tower third-knot rung. Cross-validate
machinery first on 5_2 against the published kappa_1(5_2).
