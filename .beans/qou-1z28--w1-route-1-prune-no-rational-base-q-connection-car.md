---
# qou-1z28
title: 'W1 route-1 prune: no rational base q-connection carries the SW roots — the colour cubic is irreducible over ℂ(z) (Lean), its roots are D-finite, and D-finite ∧ q-holonomic ⇒ rational (Bézivin–Ramis / Schäfke–Singer); the classical prolongation exists and is exact, the rational q-analogue does not exist'
status: todo
type: task
created_at: 2026-09-04T21:04:54Z
updated_at: 2026-09-04T21:04:54Z
---

## Question (2026-09-04, follows qou-an6y / #6652)

#6652 counted that on the level axis the content of 'symbol = L_K' is entirely in where D_q's weights come from — wall W1 (qou-d8de). W1's first named route is a q-shift on the base z ↦ q²z with a q-connection lift. Formalize-first: before building it, ask whether it can exist at all.

Claim to test: the SW roots X_i(z) of the colour cubic P(X,z) = X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1) are algebraic, hence D-finite (they satisfy a linear ODE with polynomial coefficients — the classical prolongation, proved exact/dead in prop:sw-classical-jet-exactness). If a rational rank-3 q-difference system in z ↦ q^k z (q^k not a root of unity) had the three roots as solutions, a dimension count over ℂ(z) gives X_1 a scalar linear q-difference equation with rational coefficients; a power series that is both D-finite and q-holonomic is RATIONAL (Bézivin; Ramis; unified in Schäfke–Singer 2019). So irreducibility of P over ℂ(z) excludes the route, scope-(b) with the theorem as the cited invariant, restricted to GLOBAL RATIONAL coefficients.

## PLAN
1. Corpus-grep (six paths) for Bézivin / Schäfke–Singer / 'D-finite and q-holonomic'.
2. Lean: P has no root in K[z] for any char-0 field K (degree argument + the two linear-root cases, exact certificates) ⇒ irreducible over K(z). Sorry-free, generic K.
3. Probe (exact): irreducibility cross-check; exhibit the linear ODE the root satisfies (D-finite side, explicit); finite search for a q-difference equation of bounded order/degree at z=0 — must return none (corroboration, not proof).
4. Audit doc; scope note on qou-d8de route 1; scope note on the conjecture block only if warranted.
