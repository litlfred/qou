---
# qou-8pl3
title: 'PLAUSIBLE-NOT-PROVED: routes to N = 3 for the flavour fundamental'
status: todo
type: task
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-08-06T00:00:00Z
---

## UPDATE 2026-08-07 — the obstruction half is now PROVED

`QOU/Eightfold/RowCapObstruction.lean` (sorry-free, lean-direct exit 0):

* `weyl_dim_alt_eq_zero_iff` : `dim V_{(1³)} = C(N,3) = 0  ↔  N < 3`
* `decuplet_forces_three`    : `dim V_{(3)} = 10  →  N = 3`
* `singlet_forces_three`     : `dim V_{(1³)} = 1  →  N = 3`
* `schur_weyl_cube_split_two_three` : `8 = 4+4+0` at N=2, `27 = 10+16+1` at N=3

So `N = 2` is a **scope-(b) structural exclusion** from carrying the
eightfold-way decomposition, with the justifying invariant cited (the
Schur-Weyl row cap `ℓ(λ) ≤ N`). The chapter previously stated this; it is now
a theorem. Wired as the `lean:` sibling of `prop:schur-weyl-eightfold`.

**This does not narrow the search.** It excludes N=2 from *hosting* the
decomposition; it says nothing against any route below that produces N=3.
If anything it raises the value of Route A/B, because the target is now
sharply characterised: produce `dim V = 3`, and the decuplet/octet/singlet
structure follows by the arithmetic already proved.

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
