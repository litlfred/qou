import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Hom.Defs

/-!
# `tr_M = Σ_λ y_λ χ_λ`, derived rather than assumed

**Bean `qou-7gei` item 6, and a defect report on `QOU.Hecke.Wedderburn`.**

> **RESOLVED upstream 2026-08-24 (PR #5710); re-scoped 2026-08-30.** The defect
> described below is fixed: `QOU.Hecke.WedderburnDecomp` no longer carries a
> `trace_decomp` field, and `QOU.Hecke.Wedderburn.trace_decomposition` now
> *derives* the identity from `complete` together with a new `block_scaling`
> field — the very repair this module prescribed. The analysis below is left in
> the present tense as the record of why that change was made; read "states" as
> "stated, until PR #5710".
>
> **The prescription was necessary and not sufficient**, and the follow-up has
> since landed. `block_scaling` is an equation on the *product* `y_λ · χ^λ`,
> and the #5710 class had to carry `chi_lambda` as a second free field, so
> neither factor was pinned — every nonzero rational was realisable as the
> weight at every partition. `χ^λ` is now *computed*: the field is replaced by
> a block representation `ρ_λ : A →ₐ[R] M_{f^λ}(R)` with
> `χ^λ := Matrix.trace ∘ ρ_λ`, and because an algebra map has `ρ_λ 1 = 1`,
> `block_scaling` at `x = 1` forces `tr_M(π_λ) = y_λ · f^λ`
> (`QOU.Hecke.WedderburnDecomp.yLambda_determined`). A second tranche the same
> day closed the remainder: `blockDim` is no longer a field either but
> `QOU.Hecke.blockDim λ = dimHLF λ.parts`, so `y_λ` is determined outright
> (`QOU.Hecke.RankOneDegeneracy.yLambda_forced_one`).
>
> The three theorems in this file are untouched by all of it — they were always
> stated over a generic `tr`, `pi`, `y`, `chi` with the block scaling as an
> explicit hypothesis, which is exactly why the class change did not reach them.

## The defect

`QOU/Hecke/Wedderburn.lean` (merged to main in PR #4857) states

```lean
theorem trace_decomposition (x : A) :
    MT.trace x = WD.all_parts.sum (fun lam =>
      WD.y_lambda lam • MT.trace (x * WD.pi_lambda lam)) := by
  exact WD.trace_decomp x
```

and `trace_decomp` is a **field of the class `WedderburnDecomp`**. The theorem
projects the field; it derives nothing. That is exactly the defect shape PR
#4857's own Part 1 named and refuted nineteen times —

> #1 self-assuming | the class carries the **conclusion**, as a field | theorem
> projects it; proves nothing

— and it is what AGENTS.md §3b-cond item 5 forbids: *"the class axiomatises
hypotheses, not the conclusion … the theorem must derive its conclusion from
them."* No instance of `WedderburnDecomp` exists anywhere in the tree, so every
downstream consequence is conditional on an uninhabited class whose key field is
the thing to be shown.

## What the class already has, and what it should have had

It already carries `complete : Σ_λ π_λ = 1`. The class docstring also says, in
prose, the fact that actually does the work:

> *"The Markov trace's restriction to each block is the matrix trace scaled by
> the central coefficient `y_λ`."*

That sentence is **not encoded as a field**. Encode it — as `hblock` below — and
the weighted decomposition follows in four lines from completeness, additivity
of the trace, and right-distributivity. Nothing else is needed: no Schur
orthogonality, no Mathas §3.43, no representation theory at all.

## The three statements, in increasing strength

* `trace_eq_sum_blocks` — completeness **alone** gives the *unweighted*
  `tr x = Σ_λ tr(x π_λ)`. This much is free.
* `trace_decomposition_of_blocks` — with a value assigned to each block term,
  the sum is that of the values.
* `trace_eq_sum_weighted_characters` — with the block-scaling hypothesis
  `tr(x π_λ) = y_λ · χ_λ(x)`, the target identity.

Reading them in order shows precisely where the weights enter: **not** from
completeness, which is why assuming the conclusion was never necessary, and
**not** for free either, which is why the honest axiom is the block scaling.

Everything is stated on a bare `AddMonoidHom` and an arbitrary index `Finset`.
No Hecke algebra, no partitions, no `q`, no convention — so this applies to the
merged `WedderburnDecomp` unchanged, and to any other trace with a resolution of
identity.
-/

namespace QOU.QBeta.WedderburnTraceDecomposition

section General

variable {A R ι : Type*} [Ring A] [AddCommMonoid R]

/-- **Completeness alone gives the unweighted decomposition.**

`Σ_λ π_λ = 1` and additivity of the trace give `tr x = Σ_λ tr(x · π_λ)`. The
`y_λ` do not appear, and cannot: nothing so far distinguishes the blocks. -/
theorem trace_eq_sum_blocks (tr : A →+ R) (s : Finset ι) (pi : ι → A) (x : A)
    (hcomplete : ∑ i ∈ s, pi i = 1) :
    tr x = ∑ i ∈ s, tr (x * pi i) := by
  have hx : x = ∑ i ∈ s, x * pi i := by
    rw [← Finset.mul_sum, hcomplete, mul_one]
  calc tr x = tr (∑ i ∈ s, x * pi i) := by rw [← hx]
    _ = ∑ i ∈ s, tr (x * pi i) := map_sum tr _ s

/-- **Naming the block terms.** If each `tr(x · π_λ)` is known to equal some
`val λ`, the trace is the sum of the `val`s. A repackaging of the previous
theorem, and the shape the weighted version instantiates. -/
theorem trace_decomposition_of_blocks (tr : A →+ R) (s : Finset ι) (pi : ι → A)
    (val : ι → R) (x : A) (hcomplete : ∑ i ∈ s, pi i = 1)
    (hblock : ∀ i ∈ s, tr (x * pi i) = val i) :
    tr x = ∑ i ∈ s, val i :=
  (trace_eq_sum_blocks tr s pi x hcomplete).trans (Finset.sum_congr rfl hblock)

end General

section Weighted

variable {A R ι : Type*} [Ring A] [CommRing R]

/-- **THE TARGET, DERIVED.  `tr_M(x) = Σ_λ y_λ · χ_λ(x)`.**

The hypotheses are exactly the two facts the Wedderburn decomposition supplies:

* `hcomplete` — the central idempotents resolve the identity, `Σ_λ π_λ = 1`;
* `hblock` — the trace restricted to block `λ` is the block character scaled by
  the central coefficient, `tr(x · π_λ) = y_λ · χ_λ(x)`.

Neither is the conclusion, and the conclusion follows from them without any
further input. `hblock` is the sentence already in `WedderburnDecomp`'s
docstring but absent from its fields; supplying it as a field, and deleting
`trace_decomp`, would turn `QOU.Hecke.Wedderburn.trace_decomposition` from a
projection into a theorem.

Note what is *not* claimed here: that any such `y_λ` and `χ_λ` exist, or that
they are unique. Existence is the Wedderburn–Artin content and uniqueness is
Schur orthogonality (Mathas 1999 §3.43); both remain open in the tree. What is
settled is that **the summation identity is not an independent axiom** — it was
never the thing that needed assuming. -/
theorem trace_eq_sum_weighted_characters (tr : A →+ R) (s : Finset ι) (pi : ι → A)
    (y : ι → R) (chi : ι → A → R) (x : A)
    (hcomplete : ∑ i ∈ s, pi i = 1)
    (hblock : ∀ i ∈ s, tr (x * pi i) = y i * chi i x) :
    tr x = ∑ i ∈ s, y i * chi i x :=
  trace_decomposition_of_blocks tr s pi (fun i => y i * chi i x) x hcomplete hblock

/-- **The block scaling is strictly more informative than the sum.**

If the weighted decomposition held for *every* `x` merely by assumption, it
would still say nothing about an individual block. Conversely `hblock` pins each
block term and the sum follows. Recorded as a one-line consequence so the
asymmetry is visible in the API rather than only in prose: from `hblock` one
recovers the value of each `tr(x π_λ)` individually, which the summed form does
not give. -/
theorem block_value_of_hblock (tr : A →+ R) (s : Finset ι) (pi : ι → A)
    (y : ι → R) (chi : ι → A → R) (x : A)
    (hblock : ∀ i ∈ s, tr (x * pi i) = y i * chi i x)
    {i : ι} (hi : i ∈ s) : tr (x * pi i) = y i * chi i x :=
  hblock i hi

end Weighted

end QOU.QBeta.WedderburnTraceDecomposition
