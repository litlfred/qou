import QOU.Hecke.Wedderburn
import QOU.Mathlib.SYTHookFormulaRows
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

**And the last free field is now gone too (2026-08-30, second tranche).**
`blockDim` was an untied natural, so the weight could be any `1/d` — a
one-parameter family, not all of `ℚ`, but still not determined. It is no longer
a field: `QOU.Hecke.blockDim λ = dimHLF λ.parts`, the Frame–Robinson–Thrall
hook-length dimension, computed from the partition alone. `rankOneWedderburnDim`
**cannot be written** any more — a witness has no `d` to choose — and the family
collapses onto its `d = 1` member. On this carrier the weight is *determined*:
`yLambda_forced_one` gives `y_λ = 1` at the supported partition, for an
arbitrary decomposition rather than for a witness.

And there is no residue: `dimHLF λ = #SYT(λ)` is Frame–Robinson–Thrall, which
this corpus **proves sorry-free at general `n`**
(`QOU.Mathlib.SYTEnum.numSYTenum_eq_dimHLF`, the GNW route). `blockDim` is
therefore `f^λ` as a theorem (`QOU.Hecke.blockDim_eq_numSYT`), not as an assumed
formula. An earlier version of this paragraph called the general theorem open —
that was false, taken from a stale header in `SYTHookFormulaRows.lean`, and both
are corrected in the same commit.

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
  rho := fun lam => Algebra.ofId ℚ
    (Matrix (Fin (blockDim lam)) (Fin (blockDim lam)) ℚ)
  block_scaling := by
    intro x lam
    -- the trace of a scalar matrix is its size times the scalar, at any block size
    have htr : ∀ y : ℚ, Matrix.trace ((algebraMap ℚ
        (Matrix (Fin (blockDim lam)) (Fin (blockDim lam)) ℚ)) y)
        = (blockDim lam : ℚ) * y := by
      intro y
      simp [Algebra.algebraMap_eq_smul_one, Matrix.trace_smul, Matrix.trace_one,
            smul_eq_mul, mul_comm]
    by_cases h : lam.parts = (lam0 n).parts
    · -- on the supported partition the shape is the single column, so f^λ = 1
      have hb : blockDim lam = 1 := by
        simp [blockDim, h, lam0, QOU.Mathlib.SYTHookRows.dimHLF_column]
      simp only [h, if_pos, rankOneMarkov, Algebra.ofId_apply, htr, hb]
      simp
    · simp only [h, rankOneMarkov, Algebra.ofId_apply, htr]
      simp

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

/-! ## The consequence, restated for the current class -/

/-- **The block dimension at the supported partition is forced to `1`.**

`lam0 n` is the single column `[1,1,…,1]`, whose only standard tableau fills the
column in increasing order — so `f^λ = 1`. Since 2026-08-30 `blockDim` is
`dimHLF ∘ Partition.parts` rather than a field, this is a *computation*, not a
choice the witness makes. -/
theorem rankOne_blockDim_forced (n : ℕ) : blockDim (lam0 n) = 1 := by
  simp [blockDim, lam0, QOU.Mathlib.SYTHookRows.dimHLF_column]

/-- **The weight at the supported partition is forced to `1`** — for an
ARBITRARY decomposition on this carrier, not just the witness above.

This is what closes `qou-luq7`. The morning's version of this file exhibited
`rankOneWedderburnDim n d`, an instance with `y_λ = 1/d` for every `d ≥ 1`, and
recorded that one-parameter family as the freedom surviving item 1. **That
definition can no longer be written**: `blockDim` is not a field, so a witness
cannot choose `d`, and `rho` must land in `M_{f^λ}(ℚ)` with `f^λ` computed from
`λ`. The family collapses to its `d = 1` member, which is `rankOneWedderburn`.

So on this carrier `y_λ` is not merely constrained, it is determined. -/
theorem yLambda_forced_one (n : ℕ) (WD : WedderburnDecomp (R := ℚ) n 1 ℚ)
    (hpi : WD.pi_lambda (lam0 n) = 1) :
    WD.y_lambda (lam0 n) = 1 := by
  have hdet := WedderburnDecomp.yLambda_determined (WD := WD) (lam0 n)
  rw [hpi, rankOne_blockDim_forced] at hdet
  have h1 : (MarkovTrace.trace (R := ℚ) n 1) (1 : ℚ) = 1 := MarkovTrace.normalised
  rw [h1] at hdet
  simpa using hdet.symm

/-- **`y_λ = 2` is not realisable**, kept from the morning as the coarser
statement: it holds at every `λ` with `π_λ = 1`, where `yLambda_forced_one`
gives the exact value only at `lam0 n`. Both now follow from
`yLambda_determined`; before `blockDim` was computed, neither did. -/
theorem yLambda_two_not_realisable (n : ℕ) (lam : Partition n)
    (WD : WedderburnDecomp (R := ℚ) n 1 ℚ)
    (hpi : WD.pi_lambda lam = 1) :
    WD.y_lambda lam ≠ 2 := by
  intro h2
  have hdet := WedderburnDecomp.yLambda_determined (WD := WD) lam
  rw [hpi, h2] at hdet
  have h1 : (MarkovTrace.trace (R := ℚ) n 1) (1 : ℚ) = 1 := MarkovTrace.normalised
  rw [h1] at hdet
  rcases Nat.eq_zero_or_pos (blockDim lam) with h0 | hpos
  · rw [h0] at hdet; norm_num at hdet
  · have hge : (2 : ℚ) ≤ 2 * (blockDim lam : ℚ) := by
      have : (1 : ℚ) ≤ (blockDim lam : ℚ) := by exact_mod_cast hpos
      linarith
    rw [← hdet] at hge; norm_num at hge

end QOU.Hecke.RankOneDegeneracy
