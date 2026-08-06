---
# qou-8pl3
title: 'PLAUSIBLE-NOT-PROVED: routes to N = 3 for the flavour fundamental'
status: todo
type: task
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-08-06T00:00:00Z
---

## The blocker

Quantum Schur-Weyl duality gives the eightfold-way multiplets only when the
fibre has `dim V = N = 3`. The single-fibre tower yields a quantum form of
`SU(2)`, `dim V = 2`. The row cap `ℓ(λ) <= dim V` then **kills the
antisymmetric partition `(1³)`** — at `N = 2` the decomposition is
`4·1 + 2·2 = 8 = 2³`, with no singlet. No choice of `q` restores it: the cap is
on the dimension, not the deformation.

Every flavour statement in the chapter is conditional on this. It is the
chapter's principal open problem.

## Route A — multi-fibre groupoid (plausible, untried)

Construct a three-dimensional object `W` in the multi-fibre groupoid whose
symmetric square `Sym²(W)` is irreducible (carries no singlet). Inequivalent
fibre objects whose interaction space is 3-dimensional. **Nothing has been
built.** Tracked historically as T3b.

Constraint to respect: the `SU(2)`-emergence theorem says the tensor-automorphism
gauge group of a *single* fibre is exactly `SU(2)`, so any `N = 3` must come from
groupoid-level structure — multi-strand, framing, or inter-fibre. A construction
placing it inside `Aut^⊗(τ)` of one fibre contradicts a proved theorem.

## Route B — octonionic `G_2` stabiliser (partial, and possibly the wrong target)

The Günaydin–Gürsey decomposition `Im(𝕆) ≅ ℝ ⊕ ℂ³` under `SU(3) ⊂ G_2` supplies a
non-self-dual triple, and the `3`/`3̄` of `PSL(2,7)` are complex conjugate as
required.

**Two gaps.** (i) The `Sym²` gate "pass" is a literature decomposition; the Lean
file proves only arithmetic (bean `qou-sym2`). (ii) **This route produces
colour, not flavour.** Whether the octonionic `SU(3)` can also serve as flavour
is item 4 of the chapter's open problems and is untested — and the chapter's own
obstruction audit argues they cannot both come from the same construction, since
the `Sym²` gate excludes the icosahedral colour triple `T_1` while the `G_2`
route passes it.

## What would settle it

Either construction, explicitly, with `Sym²` irreducibility checked against the
actual constructed object rather than cited. A **negative** is equally valuable:
a proof that no groupoid-level `N = 3` exists compatible with the `SU(2)`
fibre theorem would refute the eightfold-way chapter's premise outright, which is
worth knowing.

## Scope discipline

Scope-(a) throughout. No proved invariant forbids `N = 3`; it is simply not
constructed.
