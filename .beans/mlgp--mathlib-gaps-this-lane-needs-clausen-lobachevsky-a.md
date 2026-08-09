---
# mlgp
title: 'Mathlib gaps this lane needs: Clausen/Lobachevsky, Λ″ = −cot, constrained concavity'
status: todo
type: epic
priority: high
tags:
    - lean
    - mathlib-gap
    - hyperbolic-volume
created_at: 2026-08-09T19:45:00Z
updated_at: 2026-08-09T19:45:00Z
---

Inventory of what Mathlib does **not** have that the volume lane needs, with what
QOU already has in its place. Checked against the vendored Mathlib 2026-08-09.

## Gap 1 — Mathlib has no Clausen and no Lobachevsky function at all

`find Mathlib -iname '*Clausen*' -o -iname '*Lobachevsky*'` → **nothing**. QOU
carries its own: `QOU/Knot/Clausen.lean` (`clausen`, `hasDerivAt_clausen`,
duplication, minimum) and `QOU/Archimedean/BlochWignerLobachevsky.lean` (`Cl_2`,
`Lob`, `tetAngle₁/₂/₃`, `tetAngles_sum_eq_pi`, `BlochWigner_lob`, and
`Vol(S(z)) = Λ(α)+Λ(β)+Λ(γ) = D(z)` as a theorem).

⚠ Correct the stale note while here: `QOU/Knot/M004AngleStructure.lean` says
"Mathlib has no ideal-tetrahedron volume theory". True of **Mathlib**, false of
**QOU** — the corpus has one. The genuinely missing piece is narrower (Gap 2).

**This is upstreamable.** `Cl₂` with its FTC derivative, duplication formula and
`Λ` normalisation is a clean, self-contained Mathlib contribution.

## Gap 2 — `Λ″ = −cot`, the blocker on Rivin concavity  ← DO THIS FIRST

`hasDerivAt_clausen : Cl₂′(θ) = −log(2 sin(θ/2))` on `(0, 2π)` exists, sorry-free,
by `integral_hasDerivAt_right`. Since `Λ(t) = Cl₂(2t)/2`, that gives
`Λ′(t) = −log(2 sin t)` by the chain rule, and then
`Λ″(t) = −cos t / sin t = −cot t` by one more differentiation — Mathlib has
`Real.hasDerivAt_log` and `Real.hasDerivAt_sin`, so this is short.

Why it matters: bean `rvnc` proved the *algebraic* half of Rivin concavity
(`cot_quadratic_pos`, sorry-free — the Hessian quadratic form is positive on the
tangent space). Without `Λ″ = −cot` that is a fact about a quadratic form
*asserted* to be the Hessian rather than *proved* to be. This closes it.

Deliverables: `hasDerivAt_Lob`, `hasDerivAt_Lob'` (i.e. `deriv^[2] Lob = -cot`),
on `(0, π)`.

## Gap 3 — strict concavity on an affine subspace

Mathlib has `StrictConcaveOn` and second-derivative tests on intervals, but the
statement needed is concavity of `Σ Λ(θᵢ)` **restricted to the affine slice** cut
out by the gluing equations. Check what `Mathlib.Analysis.Convex.*` offers for
"negative-definite Hessian on the tangent space of an affine constraint ⟹ strictly
concave on that slice" before writing anything; this may be assemblable rather
than new.

Note the boundary behaviour found in `rvnc`: strict positivity of the Hessian form
is **pointwise on the open simplex and not uniform** — the normalised minimum over
300k samples degenerates as `α → π`. Any Mathlib-shaped lemma wanting a uniform
modulus will not apply.

## Gap 4 — `SurrealField ℝ*` / nonstandard transfer (see bean `hypr`)

Not missing from Mathlib so much as un-wired: `Hyperreal` exists with `IsSt`, `st`,
`Infinitesimal`, and `ℝ*` already instances `Field`/`LinearOrder`/
`IsStrictOrderedRing`. What Mathlib lacks is the *working* NSA toolkit — there is
no "for all infinite hypernaturals" transfer, and `IsSt (ofSeq f) r` only gives
convergence along `hyperfilter ℕ ≤ atTop`, strictly weaker than `atTop`, converse
false. So this cannot replace an ε–δ whose goal is `Tendsto … atTop`. Scope
accordingly; see `hypr`.

## Gap 5 — oscillatory asymptotics (only if bean `thmb` route C is taken)

Formalising Ohtsuki §3–§5 needs saddle-point/stationary-phase with error control
and Poisson summation. Mathlib has neither in usable form. This is the expensive
one and should not be started before Gaps 1–3.

## Ordering

Gap 2 → Gap 1 (upstream) → Gap 3 → Gap 4 → Gap 5. Gap 2 is small, unblocks `rvnc`,
and is the only one on the critical path to a *volume* statement.
