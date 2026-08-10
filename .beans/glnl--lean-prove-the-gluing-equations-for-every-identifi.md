---
# glnl
title: 'Lean-prove the gluing equations for every identified shape field (generator with exact certificates)'
status: in-progress
type: task
priority: high
tags:
    - lean
    - hyperbolic-volume
    - gluing-equations
    - codegen
parent: m015
created_at: 2026-08-10T01:35:00Z
updated_at: 2026-08-10T01:35:00Z
---

Route 75 (`qbeta_route75_multiknot_gluing_symbolic_probe.py`) verifies the gluing
equations **exactly** for 23 hyperbolic manifolds, in Python. The corpus has Lean proofs
for only two of them — `FigureEightTriangulation.edge_zero/edge_one` (4₁) and
`FiveTwoVolumeConstant.edge_zero/one/two` (5₂). This bean closes that gap by
**generating** the rest.

## The formulation that makes this tractable

**State the identity for an arbitrary root, not the geometric one.** The verification
lives in `ℚ[x]/(P)`, so the identity holds at *every* root of `P`:

```lean
theorem edge_k (θ : ℂ) (hθ : P θ = 0) : <gluing equation in z_j(θ)> = 1
```

This sidesteps the entire root-selection problem — no need to prove a quartic or quintic
has a root with `Im > 0`, which is what would otherwise block every knot past 5₂.
Selecting the geometric root is a separate, numerical matter that Route 75 already
handles (Bloch–Wigner volume cross-check) and that Lean cannot do without more
infrastructure.

## Why every proof is a single deterministic tactic call

Nothing is guessed. For each manifold, with `P` the minimal polynomial and
`z_j = Q_j(θ)` the shapes as explicit polynomials:

1. **Non-vanishing** (`z_j ≠ 0`, `1 - z_j ≠ 0`) — by **Bézout certificate**. `P` is
   irreducible and `deg Q_j < deg P`, so `∃ u, v : u·Q_j + v·P = 1` over `ℚ[x]`,
   computed by `sympy.gcdex`. In Lean, from `hQ : Q_j θ = 0` and `hθ : P θ = 0`,
   `linear_combination u * hQ + v * hθ` proves `(0:ℂ) = 1`. Contradiction, mechanically.
2. **Edge equations** — clear denominators first. Since `z' = 1/(1−z)` and
   `z'' = (z−1)/z`, the equation `∏ z^a z'^b z''^c = 1` becomes the polynomial identity

       ∏ z_j^{a_j} · ∏ (z_j − 1)^{c_j}  =  ∏ (1 − z_j)^{b_j} · ∏ z_j^{c_j}

   whose difference is divisible by `P` **exactly** (that is precisely what Route 75's
   G4 checks). So the cofactor `q = (LHS − RHS) / P` is computed by exact polynomial
   division and the whole proof is `linear_combination (q θ) * hθ`.

⚠ **Do NOT reach for `field_simp` + guessed cofactor.** That is what the 4₁/5₂ proofs do,
and it cost several wrong-cofactor iterations in the session that wrote them (recorded:
"recomputed by polynomial division against the minimal polynomial with sympy rather than
guessed"). `field_simp`'s normal form is not predictable, so it cannot be code-generated.
The cleared form above is deterministic and needs no `field_simp` at all.

## Scope note that must not be lost

Edge equations only, in the natural nonnegative-exponent form. **Cusp** equations carry
negative exponents (e.g. 5₂'s `[2,0,-3, 1,0,-2, 0,0,1]`), which need inverses as explicit
polynomials plus `zpow` handling — a second increment, not this one. Route 75 verifies
both; Lean would cover only edges at first, and the module must say so.

## Prior art in-repo to match

`QOU/MathlibExt/IdealTriangulation.lean` already has `GluingData n e` and
`SatisfiesEdgeEquations`. Generated modules should land as instances of that, so this
becomes *certification* of the existing triangulation objects rather than a parallel
structure.

## Starting point

A partial generator exists from the session that opened this bean (identification →
shapes in `ℚ(θ)` → Bézout certificates → cleared-form cofactors, all asserted exact
before emission). It was not committed — rebuild from the recipe above; the recipe is
the valuable part, not the code.

⚠ **Unchanged scope.** None of this says any triangulation is a triangulation *of* a knot
complement. That is Thurston hyperbolisation plus Mostow rigidity, needing hyperbolic
3-manifolds that neither Mathlib nor QOU has.
