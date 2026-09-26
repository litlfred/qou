---
# qou-1z28
title: 'W1 route-1 prune: no rational base q-connection carries the SW roots — the colour cubic is irreducible over ℂ(z) (Lean), its roots are D-finite, and D-finite ∧ q-holonomic ⇒ rational (Bézivin–Ramis / Schäfke–Singer); the classical prolongation exists and is exact, the rational q-analogue does not exist'
status: completed
type: task
priority: normal
created_at: 2026-09-04T21:04:54Z
updated_at: 2026-09-05T07:14:22Z
---

## Question (2026-09-04, follows qou-an6y / #6652)

#6652 counted that on the level axis the content of 'symbol = L_K' is entirely in where D_q's weights come from — wall W1 (qou-d8de). W1's first named route is a q-shift on the base z ↦ q²z with a q-connection lift. Formalize-first: before building it, ask whether it can exist at all.

Claim to test: the SW roots X_i(z) of the colour cubic P(X,z) = X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1) are algebraic, hence D-finite (they satisfy a linear ODE with polynomial coefficients — the classical prolongation, proved exact/dead in prop:sw-classical-jet-exactness). If a rational rank-3 q-difference system in z ↦ q^k z (q^k not a root of unity) had the three roots as solutions, a dimension count over ℂ(z) gives X_1 a scalar linear q-difference equation with rational coefficients; a power series that is both D-finite and q-holonomic is RATIONAL (Bézivin; Ramis; unified in Schäfke–Singer 2019). So irreducibility of P over ℂ(z) excludes the route, scope-(b) with the theorem as the cited invariant, restricted to GLOBAL RATIONAL coefficients.

## PLAN
1. Corpus-grep (six paths) for Bézivin / Schäfke–Singer / 'D-finite and q-holonomic'.
2. Lean: P has no root in K[z] for any char-0 field K (degree argument + the two linear-root cases, exact certificates) ⇒ irreducible over K(z). Sorry-free, generic K.
3. Probe (exact): irreducibility cross-check; exhibit the linear ODE the root satisfies (D-finite side, explicit); finite search for a q-difference equation of bounded order/degree at z=0 — must return none (corroboration, not proof).
4. Audit doc; scope note on qou-d8de route 1; scope note on the conjecture block only if warranted.



## RESULT (2026-09-04, PR #6695)

W1 route 1 is PRUNED, scope (b) with the invariant cited.

Lean (sorry-free, generic [Field K] [CharZero K], axioms propext/Classical.choice/Quot.sound only): QOU.Mass.ColorCubicIrreducible — colorCubicAt_ne_zero (no root in K[z]: degree >= 2 by the leading term r^3, affine roots by two integer Bezout certificates 5 and 65) and colorCubic_no_ratFunc_root (no root in K(z), by Gauss over the integrally closed K[z]). So the cubic is irreducible over K(z) and no colour sheet is a rational function of z.

Probe (exact sympy over Q and Q(q), no float64, exit 0, ALL CHECKS PASS): irreducibility cross-checked; the D-finite side exhibited as an explicit order-3 ODE whose leading coefficient (z-1)^2 (z+1)(2z^2+z+2) D(z) vanishes exactly on the branch sextic; no q-difference relation of order <= 3 and degree <= 6 on the sheet through X(0) = -1, at q in {11/10, 2, 3/2} and over Q(q) (full column rank certified mod two primes near 2^31 at q = 17/5 and 7/3); both controls found, so the null result is a property of the sheet and not of the searcher.

Two probe defects found and fixed in-tranche, both cost not correctness: rational Gaussian elimination on q^(3N)-sized entries ran 15 CPU-minutes without finishing D = 6 (replaced by the mod-p certificate); and the section-4 differential control tripped its own 'not enough equations' guard because the order-3 degree-11 ODE needs 48 unknowns against 38 usable rows from a 40-term series (the length is now derived from the ODE the probe finds, and the series is built by truncated convolution).

Container was reclaimed mid-tranche and the uncommitted probe / audit / content note were lost; they were rewritten and re-verified from scratch in the new container, including a fresh lean-direct run of the Lean file (exit 0, 0 sorry, axioms clean) on the rebased tree.



## CORRECTED 2026-09-05 (bean qou-7fnr, PR #6738) — the 'local q-dilation is not excluded' half of this bean is WRONG

The base-coordinate prune above stands unchanged. What is wrong is the scope sentence saying the LOCAL q-dilation t -> mu t at a ramification point escapes the exclusion. The reason given for it concerned POWER-SERIES coefficients; the theorem concerns RATIONAL ones, so the reason does not support the claim, and the claim is false.

Measured and proved in qou-7fnr: in the local coordinate the sheets are still algebraic over K(t), hence still D-finite, and still not rational — t^2 = z - z_c makes K(t)/K(z) quadratic, and an irreducible cubic has no root of degree <= 2 (QOU.Mass.IrreducibleCubicNoQuadraticRoot, sorry-free, generic field, no characteristic assumption). Exact cross-checks: the local cubic has no root in K[t] at any degree (leading-term bound for d >= 3; Groebner basis [1] over Q[c0,c1,c2,z_c] modulo the branch sextic for d <= 2). So the same theorem excludes the local rational q-dilation too.

What survives W1 route 1 is therefore NOT 'local at the branch point' but 'coefficients not rational in a coordinate, or an operator on Sigma'. Audit: docs/audits/2026-09-05-w1-local-qdilation-also-excluded-correction.md.
