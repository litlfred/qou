---
# qou-phir
title: 'B2: Iwahori–Hecke algebra H_n(q) as field-algebra (via Mathlib Coxeter T_w basis / quadratic+braid rels) + cell/Specht modules'
status: todo
type: task
priority: normal
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-08-30T02:56:37Z
---

## Worked 2026-08-30 — the ALGEBRA is built; the basis and cell modules are not

This bean was a bare title with no body, so recording both what it turned out to
mean and where it now stands. It has three parts and **one of them is done**.

### First: "we already have Hecke in Lean" is true in a much weaker sense than it sounds

- **Mathlib has no Hecke algebra of any kind.** Measured against the built `.olean`
  tree, because the Mathlib **source is absent in this container** — an initial
  source grep returned zero and that was a *false negative from an empty
  directory*, not a measurement. Re-run over the oleans with `CoxeterSystem` as a
  positive control: `CoxeterSystem` in 3 modules, `Hecke` in **1**, and that one is
  `Mathlib/NumberTheory/FLT/Basic`, a docstring mention of Hecke *operators*.
- **The corpus's `QOU/IwahoriHecke/` is 1429 lines across 7 files and is entirely
  self-contained** — nothing outside that directory imports it.
- **What it builds is not a Hecke algebra.** `IwahoriHeckeQuot` imposes the
  **quadratic relation only**; braid relations were deferred. So it is the free
  product of one copy of `R[x]/((x−q)(x+1))` per generator, and every theorem
  stated about it is a theorem about that free product.
- **The generic `IwahoriHecke W R q` is worse than "quadratic-only": it is
  mis-shaped.** It is `IwahoriHeckeQuot R q (Set.univ : Set W)` — quadratic
  relations imposed on **every group element**, not on simple reflections. For the
  real Hecke algebra `T_w` with `ℓ(w) ≥ 2` does *not* satisfy `(T_w − q)(T_w+1) = 0`,
  so this is not the "well-defined intermediate object" its docstring claims. The
  construction already takes an arbitrary `S : Set W`; the defect is purely that
  this caller passes the wrong `S`. NOT fixed here — see below.
- **`IwahoriHeckeOfSn` is correctly shaped**: it passes
  `adjacentTranspositionIndex n : Set (Fin (n-1))`, i.e. the simple reflections.
  Only braid relations were missing from it.

### Second: a live AXIOM, on a stale excuse — now proved and deleted

`Defn.lean` carried `axiom universal_property`. Its docstring gave the reason: two
tactic attempts *"could not be verified locally because the remote container has no
`lake` binary and elan cannot reach the Lean release server (network policy)"*.

That obstacle is gone. Existence was already proved; only **uniqueness** was
axiomatised, and it is three steps — `RingQuot.mkAlgHom` is surjective, so two
algebra maps out of the quotient agree as soon as their composites with it do; those
are maps out of a **free** algebra, so `FreeAlgebra.hom_ext` reduces that to the
generators, which is the hypothesis. Landed as `Quotient.hom_ext`;
`universal_property` is now a theorem. Choice-free (`[propext, Quot.sound]`).

### Third: the algebra itself — DONE

`QOU/MathlibExt/IwahoriHeckeAlgebra.lean`, Mathlib-style, generic `[CommRing R]`:
`HeckeAlgebra R q M` for a Coxeter matrix `M`, as `RingQuot` of `FreeAlgebra R B`
modulo an **inductive** relation carrying both the quadratic and the braid family.
Delivers `T`, `T_quadratic`, `T_braid`, `lift`, `lift_T`, `hom_ext`,
`exists_unique_lift`. All choice-free.

Three design choices worth keeping: the relation is an inductive rather than a set
of ideal generators (`RingQuot` closes an arbitrary relation into a ring congruence,
so no ideal-membership reasoning reaches any downstream proof); `M` is a bare
`B → B → ℕ` rather than a `CoxeterMatrix` (nothing needs symmetry or the diagonal
condition, and requiring it would couple the file to an API that has drifted across
Mathlib refactors); and `altProd` plus `map_altProd` are defined here because
Mathlib has no alternating-word product over a monoid.

Type A landed alongside it in `QOU/BraidKnot/HeckeTypeAInstance.lean` and closes
`qou-0o6j`.

### What is STILL OPEN in this bean

1. **The `T_w` basis.** The bean's title says "via Mathlib Coxeter `T_w` basis". Not
   built. The construction above is by generators and relations; the standard basis
   indexed by `W` with the length-based multiplication rule
   (`T_s T_w = T_{sw}` when `ℓ(sw) > ℓ(w)`, else `q T_{sw} + (q−1) T_w`) is a
   separate theorem — and it is the one that needs Matsumoto / reduced expressions,
   i.e. the genuinely hard part.
2. **Cell / Specht modules.** Not started.
3. **The mis-shaped generic `IwahoriHecke W R q`** (`Set.univ` over `W`). Deliberately
   not touched: changing which `S` it passes is a signature change across the five
   consumers in that directory, and it is a different job from building the algebra.
   Worth its own bean.

Note for whoever takes (1): the blocker this arc has cited for a year — the Coxeter
order accessor being "in flux in Mathlib's `CoxeterSystem` API" — is not a blocker
for the *presentation*. `m_{st}` is just `orderOf (s * t : W)`. It may still bite for
the basis, where reduced expressions really are needed.
