import QOU.Hecke.InstanceH2
import Mathlib.LinearAlgebra.Dimension.Free
import Mathlib.LinearAlgebra.FreeModule.Finite.Basic

/-!
# `QOU.Hecke.FullRank` — the missing rank axiom, and how to establish it inductively

`QOU.Hecke.HeckeAlgebra R n q A` asks for generators, the three relations, and
spanning. It does **not** ask that `A` be free of rank `n!` over `R`, and without
that it does not characterise `H_n(q)`: `QOU.Hecke.InstanceH2.rankOneModel`
exhibits `ℚ` itself as a `HeckeAlgebra ℚ n 1 ℚ` for *every* `n`.

This file adds the missing condition as a **companion predicate** rather than by
strengthening `HeckeAlgebra` in place, so existing consumers keep compiling and
each can be upgraded deliberately.

## Why a rank condition is the right axiom

`spans` says the canonical map from the abstract algebra with these generators
and relations onto `A` is surjective. The Iwahori basis theorem says that
abstract algebra has dimension `n!`. Granting that (it is *not* formalised here,
and nothing below depends on it), a surjection between `R`-spaces of equal
finite dimension is an isomorphism — so `HeckeAlgebra R n q A` together with
`finrank R A = n!` pins `A` down to `H_n(q)` up to isomorphism, while either
alone does not.

What the predicate does **not** do is name the basis: it fixes the dimension,
not the `{T_w}_{w ∈ S_n}` labelling. That is deliberate — the dimension is what
every downstream argument in the corpus actually uses, and it is what the
degenerate models fail.

> **Correction (2026-08-30, bean `qou-0y6h`) — the granted assumption is no
> longer an assumption over a field.** The paragraph above says the Iwahori
> basis theorem *"is not formalised here"*. It is now formalised in this
> corpus: `QOU.Hecke.TwBasis.basisTwOfField` is a genuine
> `Module.Basis (Equiv.Perm (Fin (n+1))) K (QOU.Hecke.IwahoriHecke K q n)` whose
> vectors are the `T_w`, giving
> `finrank_eq_factorial : Module.finrank K (IwahoriHecke K q n) = (n+1)!`.
> `QOU.Hecke.TwFullRank` discharges `IsHeckeOfFullRank` from it, so the
> predicate now holds of the honest `RingQuot` presentation at **every** rank,
> not only of the tree's `H3A` / `H4A` (where, per
> `QOU.Hecke.FullRankFromWedderburn`, the dimension is true by construction of
> the carrier and carries no Hecke content).
>
> Two scope notes. The basis is a **field** statement — everything upstream of
> `QOU/Hecke/TwBasisField.lean` holds over an arbitrary commutative ring, but
> the dimension squeeze does not. And it does **not** supply an instance of
> *this* class, `QOU.Hecke.HeckeAlgebra`, for `IwahoriHecke`: this class's
> quadratic field is `σ² = (q - q⁻¹)σ + 1` while `IwahoriHecke`'s is
> `σ² = (q-1)σ + q`, so the two are related by a rescaling of `q`, not by an
> instance (bean `qou-img9`). Name the class when you say that: the corpus
> carries several distinct declarations spelled `HeckeAlgebra` across two
> quadratic conventions, and `(q-1)σ + q` is the *shared* one — it is what
> `QOU.MathlibExt.IwahoriHecke.HeckeAlgebra` uses too, at the same `q`. This
> class is the odd one out (bean `qou-csgy`).

## The inductive route

The point of `§ Inductive assembly` below: the rank condition is not something
to re-establish level by level. `H_{n+1}` is free of rank `n+1` over `H_n` (the
Iwahori coset decomposition
`H_{n+1} = ⊕_{i=0}^{n} H_n · σ_n σ_{n-1} ⋯ σ_{n-i+1}`), so the tower law gives
`finrank R H_{n+1} = (n+1) · finrank R H_n`, and `1 = 0!` starts the induction.
`finrank_of_rank_recursion` closes it: a rank function satisfying those two
facts *is* `n!`.

So a tower only ever has to supply **one rung at a time** — "free of rank `n+1`
over the level below" — and full rank at every level follows. That is strictly
less work than constructing each `H_n` and computing its dimension from scratch,
and it is the shape `QOU.Mathlib.HeckeAlgebra.basis_dimension_recurses` and
`HnCarrierRec` were already reaching for.
-/

namespace QOU.Hecke

open QOU.Hecke.InstanceH2

universe u

/-! ## The predicate -/

/--
**`A` has the full Hecke rank at level `n`**: free over `R` of dimension `n!`.

Pair it with `HeckeAlgebra R n q A` at any site that needs `A` to genuinely be
the Hecke algebra rather than some quotient satisfying the same relations:

```
variable [HeckeAlgebra R n q A] [IsHeckeOfFullRank R n A]
```

It is stated without reference to `q` because the dimension of `H_n(q)` does not
depend on the parameter.
-/
class IsHeckeOfFullRank (R : Type u) (n : ℕ) (A : Type u)
    [Field R] [Ring A] [Algebra R A] : Prop where
  /-- `A` is free as an `R`-module. -/
  free : Module.Free R A
  /-- …of rank exactly `n!` — the Iwahori basis size. -/
  finrank_eq : Module.finrank R A = n.factorial

attribute [instance] IsHeckeOfFullRank.free

/-! ## It excludes the degenerate models

This is the whole point of the predicate: the rank-one model that satisfies
`HeckeAlgebra ℚ n 1 ℚ` at every `n` fails it as soon as `n! ≠ 1`. -/

/-- **`ℚ` is not a full-rank Hecke algebra at `n = 3`.** It *is* a
`HeckeAlgebra ℚ 3 1 ℚ` (`InstanceH2.rankOneModel`), which is exactly why the
extra predicate is needed: `finrank ℚ ℚ = 1` but `3! = 6`. -/
theorem not_isHeckeOfFullRank_rankOne_three : ¬ IsHeckeOfFullRank ℚ 3 ℚ := by
  rintro ⟨-, h⟩
  rw [Module.finrank_self] at h
  norm_num [Nat.factorial] at h

/-- More sharply: the rank-one model fails at **every** `n ≥ 2`, since `n! ≥ 2`
there. Only `n = 0, 1` — where `H_n(q)` really is one-dimensional — survive. -/
theorem not_isHeckeOfFullRank_rankOne {n : ℕ} (hn : 2 ≤ n) :
    ¬ IsHeckeOfFullRank ℚ n ℚ := by
  rintro ⟨-, h⟩
  rw [Module.finrank_self] at h
  have h2 : 2 ≤ n.factorial := by
    calc 2 = Nat.factorial 2 := rfl
      _ ≤ n.factorial := Nat.factorial_le hn
  omega

/-! ## `H₂(q)` satisfies it

`AdjoinRoot` of a monic quadratic is free of rank `2 = 2!`, so the instance built
in `QOU.Hecke.InstanceH2` is the genuine two-strand algebra — the `HeckeAlgebra`
class simply could not say so. -/

section H2

open Polynomial

variable (R : Type u) [Field R] (q : R)

/-- `X² − h·X − 1` is monic. -/
theorem heckePoly_monic : (heckePoly R q).Monic := by
  unfold heckePoly
  monicity!

/-- …of degree exactly `2`. -/
theorem heckePoly_natDegree : (heckePoly R q).natDegree = 2 := by
  unfold heckePoly
  compute_degree!

/-- **`H₂(q)` is free of rank `2` over `R`.** -/
theorem finrank_H2 : Module.finrank R (H2 R q) = 2 := by
  have hb := (AdjoinRoot.powerBasis' (heckePoly_monic R q)).basis
  rw [Module.finrank_eq_card_basis hb, Fintype.card_fin, AdjoinRoot.powerBasis'_dim,
    heckePoly_natDegree]

/-- **`H₂(q)` has the full Hecke rank**, `2 = 2!`. Together with
`InstanceH2.instHeckeAlgebraH2` this is the first object to satisfy the
`HeckeAlgebra` class *and* have its dimension pinned.

(The tree's `QOU.Machinery.HeckeH3AlgebraInstance.H3A` and `…HeckeH4AlgebraLaws.H4A`
are honest Hecke algebras too, with sorry-free Wedderburn isomorphisms giving
their dimensions — they simply had no `HeckeAlgebra` class instance. Wiring this
predicate to them is the better route; bean qou-awp7.) -/
instance instIsHeckeOfFullRankH2 : IsHeckeOfFullRank R 2 (H2 R q) where
  free := (heckePoly_monic R q).free_adjoinRoot
  finrank_eq := by rw [finrank_H2]; rfl

end H2

/-! ## Inductive assembly

The two halves of the induction, each proved in full: the **tower law** turns one
rung into a rank multiplication, and the **numeric recursion** closes `d 0 = 1`,
`d (n+1) = (n+1) · d n` into `d n = n!`. Neither mentions the Hecke relations —
a concrete tower supplies only the rung. -/

section Tower

/-- **One rung of the tower multiplies the rank.** If `A` is free of rank `n+1`
over `B` and `B` is free of rank `n!` over `R`, then `A` is free of rank
`(n+1)!` over `R`.

This is the Iwahori coset decomposition
`H_{n+1} = ⊕_{i=0}^{n} H_n · (σ_n ⋯ σ_{n-i+1})` in rank form: `n+1` summands,
each a free rank-one `H_n`-module. -/
theorem finrank_succ_of_rung (R : Type u) (B : Type u) (A : Type u)
    [Field R] [Field B] [AddCommGroup A] [Module B A] [Module R B] [Module R A]
    [IsScalarTower R B A] [Module.Free R B] [Module.Free B A] {n : ℕ}
    (hB : Module.finrank R B = n.factorial)
    (hA : Module.finrank B A = n + 1) :
    Module.finrank R A = (n + 1).factorial := by
  rw [← Module.finrank_mul_finrank R B A, hB, hA, Nat.factorial_succ, Nat.mul_comm]

/-- **The numeric induction.** A rank function that starts at `1` and multiplies
by `n+1` at each rung *is* the factorial. This is the whole content of
"assemble inductively": a tower need only exhibit each rung.

Compare `QOU.Mathlib.HeckeAlgebra.basis_dimension_recurses`, which states the
same recursion for `Hn_basis_dimension`; this closes it. -/
theorem finrank_of_rank_recursion (d : ℕ → ℕ) (h0 : d 0 = 1)
    (hstep : ∀ n, d (n + 1) = (n + 1) * d n) (n : ℕ) : d n = n.factorial := by
  induction n with
  | zero => simpa using h0
  | succ k ih => rw [hstep k, ih, Nat.factorial_succ]

/-- The two halves composed, as a tower would use them: full rank at level `n`
plus a rung to `n+1` gives full rank at `n+1`. Stated as its own lemma so a
concrete tower can `exact` it inside an `induction`. -/
theorem isHeckeOfFullRank_succ (R : Type u) (B : Type u) (A : Type u)
    [Field R] [Field B] [Ring A] [Algebra R B] [Algebra B A] [Algebra R A]
    [IsScalarTower R B A] [Module.Free B A] {n : ℕ}
    [hBrank : IsHeckeOfFullRank R n B]
    (hA : Module.finrank B A = n + 1) :
    IsHeckeOfFullRank R (n + 1) A where
  free := Module.Free.trans (R := R) (S := B) (M := A)
  finrank_eq :=
    finrank_succ_of_rung R B A hBrank.finrank_eq hA

/-- **Base of the induction**: `R` itself is the level-`0` (equivalently
level-`1`) algebra, free of rank `1 = 0! = 1!`. -/
instance instIsHeckeOfFullRankBase (R : Type u) [Field R] : IsHeckeOfFullRank R 0 R where
  free := inferInstance
  finrank_eq := by rw [Module.finrank_self]; rfl

instance instIsHeckeOfFullRankOne (R : Type u) [Field R] : IsHeckeOfFullRank R 1 R where
  free := inferInstance
  finrank_eq := by rw [Module.finrank_self]; rfl

end Tower

/-! ## What is still missing

`finrank_succ_of_rung` is the *step*; supplying it at `n = 2 → 3` means
exhibiting `H₃(q)` as a free rank-`3` module over `H₂(q)`. That is the concrete
work bean qou-jr3k tracks (`H3.mul` associativity, then `Ring`/`Algebra`), and it
is now a single rung rather than a from-scratch dimension computation.

Nothing above asserts that such a tower exists — it says what a tower owes, and
discharges the arithmetic once and for all. -/

end QOU.Hecke
