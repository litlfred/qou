import QOU.Hecke.Wedderburn
import QOU.Hecke.FullRank

/-!
# `WedderburnDecomp` does not characterise `H_n(q)` — an instance would prove nothing

**Bean `qou-luq7`, answered in the negative.** Re-verified against the
repaired class 2026-08-30 (bean `qou-0cyu`); see "The repair ... does not close
the hole" below.

## The question this module settles

`QOU.Hecke.WedderburnDecomp` has no instance anywhere in the tree, so its
consequences are conditional on an uninhabited class — and `#print axioms`
cannot see that. The natural repair is to *build* an instance, joining Mathlib's
Artin–Wedderburn (`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing`) to
the Hecke dimension count.

**That repair would not work, and this module proves why.** The class is
satisfiable by a **one-dimensional** algebra at every `n`. Constructing an
instance would therefore establish nothing about `H_n(q)`, whose dimension is
`n!`; it would only silence the audit.

## The mechanism

`WedderburnDecomp` takes `[HeckeAlgebra R n q A]` as a hypothesis, and
`QOU.Hecke.InstanceH2.rankOneModel` inhabits *that* class at every `n` with
`A = R = ℚ`, `q = 1`, `embed := fun _ => 1`. PR #4857 found this degeneracy and
repaired it for `HeckeAlgebra` by adding the companion predicate
`IsHeckeOfFullRank` (`QOU/Hecke/FullRank.lean`), whose whole purpose is to
exclude the rank-one model. `WedderburnDecomp` never picked that companion up,
so it inherits the hole through its own hypothesis.

Every remaining field then goes through on `ℚ` for structural reasons, not by
any dodge: `central` because `ℚ` is commutative; `idempotent` and `orthogonal`
because the family `π_λ = if λ = λ₀ then 1 else 0` is supported at one
partition; `complete` because that one value is `1`; and `block_scaling`
because the block character `χ^λ` is *itself* a free field of the class, so
`tr_M(x · π_λ) = y_λ · χ^λ(x)` constrains only the **product** `y_λ · χ^λ` —
choose `χ^λ` to absorb whatever `y_λ` you picked.

## The repair this module originally asked for has landed, and does not close
the hole

The first version of this file (2026-08-21) named a specific repair: replace
the old `trace_decomp` field — which asserted the summation identity outright
— with the block-scaling sentence `tr_M(x · π_λ) = y_λ · χ^λ(x)`, "so that
`y_λ` is pinned and `trace_decomp` can be deleted rather than assumed".

That repair landed in PR #5710 (commit `30e5df8938`), and it is a real
improvement: `trace_decomposition` is now *derived* from `complete` +
`block_scaling` rather than projected out of an axiom, and the pair of
theorems `weights_inert` / `weight_one_or_block_trace_zero` that the old field
forced are gone with it.

**It did not pin `y_λ` either — and the second repair, in this PR, now does.**
The #5710 class stored its blocks abstractly, so `χ^λ` had to come in as a
field alongside `y_λ`, and an equation on their product pins neither factor:
`rankOneWedderburnScaled` realised **every** nonzero rational as the weight at
every partition. That was this module's finding, and the reason it held was the
reason the first repair was needed — what the class stored was not enough to
*compute* the block character from, so the character was assumed, and an
assumed character absorbs an assumed weight.

So `χ^λ` is no longer assumed. The free field is replaced by a block
representation `ρ_λ : A →ₐ[R] M_{f^λ}(R)`, with `χ^λ := Matrix.trace ∘ ρ_λ`
*defined* from it. Being an algebra map, `ρ_λ 1 = 1`, hence `χ^λ(1) = f^λ` is
forced — and `block_scaling` at `x = 1` then reads `tr_M(π_λ) = y_λ · f^λ`
(`WedderburnDecomp.yLambda_determined`). The rescaling trick is dead:
`yLambda_two_not_realisable` below shows `y_λ = 2` is now impossible at
`π_λ = 1`, where before every nonzero rational was available.

**What survives is exactly one free field.** `blockDim` is still an untied
natural, so the weight can be any `1/d` (`yLambda_residual_freedom`) — a
one-parameter family indexed by the remaining freedom, not all of `ℚ`. Closing
it is the hook-length half of Mathas (1999) Thm 3.43.

## What this module does and does not claim

It does **not** claim `WedderburnDecomp` is false, or that its fields are
wrong. Each field is a true and meaningful sentence about a genuine Wedderburn
decomposition. The claim is the weaker, sharper one: **the fields do not
together pin down the algebra**, so inhabiting them is not evidence.

Scope, per AGENTS.md §"Before declaring refuted": this is a **structural
exclusion (b)**, and the invariant cited is a dimension count —
`Module.finrank ℚ ℚ = 1` against `n! ≥ 2` for `n ≥ 2`. It excludes
"an instance of the class as it stands is worth building", not the Wedderburn
decomposition itself.

## What would have to change (revised 2026-08-30)

Pairing the class with the rank predicate is still necessary:

```
variable [HeckeAlgebra R n q A] [IsHeckeOfFullRank R n A] [WedderburnDecomp n q A]
```

It is no longer *sufficient*, and the block-scaling half of the original
prescription has been tried. Two things would additionally have to hold:

1. **`χ^λ` must stop being a free field.** It has to be *computed* — as the
   trace of a matrix representation `ρ_λ : A → M_{f^λ}(R)`, which is the
   content the header docstring promises ("the matrix-algebra isomorphisms are
   captured abstractly") and the class does not carry. Only a `χ^λ` that is
   determined by the algebra makes `block_scaling` an equation about one
   unknown.
2. **`f^λ` must be tied to the partition.** `SpechtDimension` is a class with a
   free `dim` field and no link to `lam`; the hook-length formula is stated in
   its docstring and encoded nowhere. Without it there is no dimension count to
   contradict, which is why the exclusion below has to be argued from
   `Module.finrank ℚ ℚ` rather than from anything the class says.

Both are Mathas (1999) Theorem 3.43 — the seminormal form and its indexing by
`Partition n` — and neither is in Mathlib.

## References

- PR #4857 (`IsHeckeOfFullRank`, `rankOneModel`) — the same degeneracy, one
  class upstream.
- Mathas (1999), Theorem 3.43 — the mathematics an honest instance needs.
-/

namespace QOU.Hecke.RankOneDegeneracy

open QOU.Hecke

/-! ## The witness

Both instances below are **`scoped`**. Registering them globally would let
typeclass search discharge `[MarkovTrace …]` and `[WedderburnDecomp …]`
hypotheses with the degenerate model, which is the opposite of the point.
-/

/-- The Markov trace on the rank-one model: the identity functional on `ℚ`.
Normalisation, cyclicity and both generator-value axioms hold because every
generator maps to `1` and `ℚ` is commutative. -/
scoped instance rankOneMarkov (n : ℕ) : MarkovTrace (R := ℚ) n 1 ℚ where
  trace := LinearMap.id
  normalised := rfl
  cyclic := by intro x y; simp [mul_comm]
  z_param := 1
  trace_gen := by intro i; rfl
  trace_prod_gen := by intro i j _; rfl

/-- The all-ones partition `1 + 1 + ⋯ + 1 = n`. Exists at every `n`, which is
what lets the witness below be stated uniformly rather than at one fixed rank. -/
def lam0 (n : ℕ) : Partition n where
  parts := List.replicate n 1
  sum_eq := by simp
  positive := by
    intro p hp
    rw [List.eq_of_mem_replicate hp]
    norm_num
  decreasing := by
    simp [List.Sorted, List.pairwise_replicate]

open Classical in
/-- **The degenerate Wedderburn decomposition, at every `n`.**

Every field is the class's genuine equation, discharged: no `Prop`-variable
field, no `True`, no `sorry`. The carrier is `ℚ`, which is `Nontrivial` — so
this is a strictly stronger witness than a `PUnit`-style one, and it is not the
`triv_wedderburn` pattern of `QOU/Mathlib/HeckeAlgebra.lean`. -/
noncomputable scoped instance rankOneWedderburn (n : ℕ) :
    WedderburnDecomp (R := ℚ) n 1 ℚ where
  pi_lambda := fun lam => if lam.parts = (lam0 n).parts then (1 : ℚ) else 0
  idempotent := by
    intro lam; by_cases h : lam.parts = (lam0 n).parts <;> simp [h]
  orthogonal := by
    intro lam mu hne
    by_cases hl : lam.parts = (lam0 n).parts
    · by_cases hm : mu.parts = (lam0 n).parts
      · exact absurd (hl.trans hm.symm) hne
      · simp [hm]
    · simp [hl]
  central := by intro lam a; exact mul_comm _ _
  y_lambda := fun lam => if lam.parts = (lam0 n).parts then 1 else 0
  all_parts := {lam0 n}
  complete := by rw [Finset.sum_singleton]; simp
  blockDim := fun _ => 1
  rho := fun _ => Algebra.ofId ℚ (Matrix (Fin 1) (Fin 1) ℚ)
  block_scaling := by
    intro x lam
    by_cases h : lam.parts = (lam0 n).parts <;>
      simp [h, rankOneMarkov, Algebra.ofId_apply, Algebra.algebraMap_eq_smul_one]

/-! ## The consequence -/

/-- **The headline.** At every `n ≥ 2` the class `WedderburnDecomp` is
inhabited by an algebra that provably **fails** the Hecke rank predicate.

Read the two conjuncts together: inhabiting `WedderburnDecomp` is compatible
with `¬ IsHeckeOfFullRank`, so an instance of the former is not evidence that
the carrier is `H_n(q)`. The second conjunct is `not_isHeckeOfFullRank_rankOne`
from `QOU/Hecke/FullRank.lean`, i.e. the same invariant PR #4857 introduced. -/
theorem wedderburnDecomp_does_not_pin_rank {n : ℕ} (hn : 2 ≤ n) :
    Nonempty (WedderburnDecomp (R := ℚ) n 1 ℚ) ∧ ¬ IsHeckeOfFullRank ℚ n ℚ :=
  ⟨⟨rankOneWedderburn n⟩, not_isHeckeOfFullRank_rankOne hn⟩

/-- The dimension invariant the exclusion rests on, stated on its own so the
`(b)`-scope citation is checkable: the witness carrier is one-dimensional, and
`H_n(q)` is not, at every `n ≥ 2`. -/
theorem rankOne_finrank_ne_factorial {n : ℕ} (hn : 2 ≤ n) :
    Module.finrank ℚ ℚ ≠ n.factorial := by
  rw [Module.finrank_self]
  have h2 : 2 ≤ n.factorial := by
    calc 2 = Nat.factorial 2 := rfl
      _ ≤ n.factorial := Nat.factorial_le hn
  omega

/-- **The witness assigns weight `1` on its supported partition**, where a
genuine Ocneanu weight need not be `1`.

Restricted to the support since PR #6097's class change: `y_λ` must now vanish
off-support, because `block_scaling` is stated against `Matrix.trace (ρ_λ x)`
and an `AlgHom` cannot be zero there (`ρ_λ 1 = 1`). The previous
unconditional-in-`λ` form was available only while `chi_lambda` was a free
field that could itself vanish. -/
theorem rankOne_yLambda_support_one (n : ℕ) :
    (rankOneWedderburn n).y_lambda (lam0 n) = 1 := by
  simp [rankOneWedderburn]

open Classical in
/-- **The same witness at an arbitrary block dimension.** Identical to
`rankOneWedderburn` except that the block representation lands in
`M_d(ℚ)` rather than `M_1(ℚ)`, which forces `y_λ = 1/d`.

This replaces `rankOneWedderburnScaled`, which set `y_λ ≡ c` for *any* nonzero
`c` by rescaling the then-free `chi_lambda` field by `c⁻¹`. That move is no
longer available: `χ^λ` is now `Matrix.trace (ρ_λ ·)` for an algebra map, and
`ρ_λ 1 = 1` fixes `χ^λ(1) = d`. The only freedom left is `d` itself. -/
noncomputable def rankOneWedderburnDim (n : ℕ) (d : ℕ) (hd : 0 < d) :
    WedderburnDecomp (R := ℚ) n 1 ℚ where
  pi_lambda := fun lam => if lam.parts = (lam0 n).parts then (1 : ℚ) else 0
  idempotent := by
    intro lam; by_cases h : lam.parts = (lam0 n).parts <;> simp [h]
  orthogonal := by
    intro lam mu hne
    by_cases hl : lam.parts = (lam0 n).parts
    · by_cases hm : mu.parts = (lam0 n).parts
      · exact absurd (hl.trans hm.symm) hne
      · simp [hm]
    · simp [hl]
  central := by intro lam a; exact mul_comm _ _
  y_lambda := fun lam => if lam.parts = (lam0 n).parts then (d : ℚ)⁻¹ else 0
  all_parts := {lam0 n}
  complete := by rw [Finset.sum_singleton]; simp
  blockDim := fun _ => d
  rho := fun _ => Algebra.ofId ℚ (Matrix (Fin d) (Fin d) ℚ)
  block_scaling := by
    have hd' : (d : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hd.ne'
    intro x lam
    by_cases h : lam.parts = (lam0 n).parts
    · simp [h, rankOneMarkov, Algebra.ofId_apply, Algebra.algebraMap_eq_smul_one,
            Matrix.trace_smul, Matrix.trace_one, smul_eq_mul]
      field_simp
    · simp [h, rankOneMarkov, Algebra.ofId_apply, Algebra.algebraMap_eq_smul_one,
            Matrix.trace_smul, Matrix.trace_one, smul_eq_mul]

/-! ## The consequence, restated for the current class -/

/-- **The freedom that survives is exactly the block dimension.** For every
`d ≥ 1` there is a decomposition whose weight at the supported partition is
`1/d`.

So `y_λ` is still not determined by the class alone — but the residual family
is `{1/d : d ≥ 1}`, indexed by the one remaining free field, not all of `ℚ`.
Closing it is item 2: tie `blockDim` to `λ` by the hook-length formula
(Mathas 1999 Thm 3.43). -/
theorem yLambda_residual_freedom (n : ℕ) (d : ℕ) (hd : 0 < d) :
    ∃ WD : WedderburnDecomp (R := ℚ) n 1 ℚ,
      WD.y_lambda (lam0 n) = (d : ℚ)⁻¹ := by
  refine ⟨rankOneWedderburnDim n d hd, ?_⟩
  simp [rankOneWedderburnDim]

/-- **`block_scaling` now DOES constrain `y_λ` — the refutation of
`yLambda_not_pinned`.**

That theorem (this file, before PR #6097) realised *every* nonzero rational as
the weight at every partition. Here is a rational it can no longer reach: with
`π_λ = 1`, `y_λ = 2` is impossible, because `yLambda_determined` forces
`tr_M(π_λ) = y_λ · f^λ`, i.e. `1 = 2·d` for a natural `d`.

The statement is about an *arbitrary* decomposition on this carrier, not about
the witnesses above, so it is a property of the class rather than of a
construction. -/
theorem yLambda_two_not_realisable (n : ℕ) (lam : Partition n)
    (WD : WedderburnDecomp (R := ℚ) n 1 ℚ)
    (hpi : WD.pi_lambda lam = 1) :
    WD.y_lambda lam ≠ 2 := by
  intro h2
  have hdet := WedderburnDecomp.yLambda_determined (WD := WD) lam
  rw [hpi, h2] at hdet
  have h1 : (MarkovTrace.trace (R := ℚ) n 1) (1 : ℚ) = 1 := rfl
  rw [h1] at hdet
  -- hdet : (1 : ℚ) = 2 * (WD.blockDim lam : ℚ)
  rcases Nat.eq_zero_or_pos (WD.blockDim lam) with h0 | hpos
  · rw [h0] at hdet; norm_num at hdet
  · have : (2 : ℚ) ≤ 2 * (WD.blockDim lam : ℚ) := by
      have : (1 : ℚ) ≤ (WD.blockDim lam : ℚ) := by exact_mod_cast hpos
      linarith
    rw [← hdet] at this; norm_num at this

end QOU.Hecke.RankOneDegeneracy
