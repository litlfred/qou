---
# qou-6ort
title: Extract 6_1 kappa-series from ki6c.pdf (Ohtsuki-Yokota 6-crossing) — Ohtsuki-tower third-knot leg
status: todo
type: task
created_at: 2026-08-15T11:35:54Z
updated_at: 2026-08-15T11:35:54Z
---


## 2026-08-15 extraction pass (pypdf; library/ki6c/ki6c.pdf = Ohtsuki-Yokota,
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

## 2026-08-19 rescope — the machinery EXISTS; this is reuse, not build-from-scratch

Two corpus-greps changed the cost estimate and killed one phantom hazard.

**1. No κ symbol collision (a hazard I nearly recorded, then disproved).**
I suspected the corpus κ_n (`OhtsukiKappaVsCkSign.kappa1 = 11√3π/108`, cited
to [andersen-hansen2006]) might be the Andersen-Hansen *b*-tower — a different
object from Ohtsuki's ℏ-series κᵢ in ki6c, which would need a conversion step.
It is NOT: `docs/audits/2026-07-12-ohtsuki-higher-rungs-exact.md` line 22 states
the corpus tower is `log(1 + Σ κ_n^Oht ℏⁿ)` with **ℏ = 2πi/N**, and line 10 has
`κ₁ = [1/N] log J_N(4₁)`. Same object. So a 6₁ κ-series IS directly a
third-knot rung of the corpus tower — qou-6ort is correctly aimed.

**2. The extraction producer exists and is a template.**
`docs/audits/scripts/qbeta_ohtsuki_higher_rungs.py` computed 4₁'s κ₁..κ₄ to
36/30/25/19 digits at dps 220 by: direct `log_kashaev_4_1(N)` evaluation over
many N → `poly_fit_1_over_N` → `pslq_rational_multiple` against the real
cyclotomic subfield. The 6₁ job is the same pipeline with two substitutions:
  (a) the ⟨6₁⟩_N state sum (ki6c §3 gives the 3-variable potential
      V(t,s,u); the Kashaev sum is finite and directly evaluable) in place of
      the 1-variable 4₁ sum;
  (b) a DIFFERENT PSLQ recognition basis — 4₁'s parity pattern (odd n → ℚ·√3·πⁿ,
      even n → ℚ·πⁿ) is trace-field-specific to ℚ(√-3) and will NOT transfer;
      6₁'s field is the quartic 2z'⁴ − z'³ − 2z'² + z' + 1 (ki6c p.18).

**Validation gate before trusting any 6₁ rung**: ki6c prints ς(6̄₁) =
0.5035603... − i·1.08078... and ω(6̄₁) = −0.52139... + i·0.071732... to ~6
digits. The fit's leading terms must reproduce BOTH before any κ is read;
mirror/conjugation convention (the paper works with 6̄₁) must be pinned
explicitly, not assumed.

**Cost**: session-scale for the pipeline port + 4₁ re-validation; the 6₁ state
sum at the N needed for 4+ rungs is the compute risk (long-compute logging
discipline applies). NOT a from-scratch saddle-point/Feynman-diagram build,
which is what the previous note implied.
