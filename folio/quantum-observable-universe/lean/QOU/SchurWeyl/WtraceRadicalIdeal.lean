/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.WtraceRadicalTwoRowSubset
import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.QBeta.MarkovTraceQuotient
import Mathlib.RingTheory.TwoSidedIdeal.Kernel

/-!
# The trace radical IS the kernel of the two-row projection

`WtraceRadicalTwoRowSubset.mem_rad_iff_twoRow_blocks_vanish` identifies the radical of
`wtrace` **pointwise**: a given `x` is invisible to the Ocneanu trace form exactly when
every at-most-two-row block kills it.  That is a statement about elements.  This file
packages it as a statement about **objects** — an equality of two-sided ideals,

`traceRadicalIdeal (wtrace …) = TwoSidedIdeal.ker (twoRowProduct …)`,

together with surjectivity of `twoRowProduct`.

## Why the packaging is not bookkeeping

The phrase *"`H_n(q)/\mathrm{rad}` is the Temperley–Lieb algebra"* needs `rad` to be an
**ideal** and needs a **map** whose kernel it is.  A pointwise iff over `x` supplies
neither: `mem_rad_iff_twoRow_blocks_vanish` characterises membership in a `Set`, and says
nothing about that set being closed under anything.  The closure properties live in
`QBeta.MarkovTraceQuotient` (three additive, two multiplicative, cyclicity spent in
exactly one) and are what `traceRadicalIdeal` is assembled from; what was missing is the
identification of that ideal with a kernel.

Together, `traceRadicalIdeal_eq_ker` and `twoRowProduct_surjective` are exactly the data
of the first isomorphism theorem for this pair.

## 🛑 What this file does NOT claim

**It does not claim `H_n(q)/\mathrm{rad} \cong \prod_{\ell(\lambda)\le 2} M_{f^\lambda}`.**
The two theorems here are the *input* to that isomorphism, not the isomorphism.  Producing
the `≃ₐ` needs a lift out of `TwoSidedIdeal.ringCon.Quotient`, and the pinned Mathlib has
no first-isomorphism lemma at that generality: `Mathlib/RingTheory/Congruence/` and
`Mathlib/RingTheory/TwoSidedIdeal/` contain `ker`, `mem_ker` and `ker_eq_bot`, and no
`lift` or `quotientKerEquivOfSurjective`.  So the remaining step is a construction, and it
is not done here.  Three artifacts record the isomorphism as open —
`mass-theory/hecke-radical-is-temperley-lieb.md`, `MathlibExt/HeckeToTemperleyLieb.lean`'s
§"What this file does NOT claim", and bean `qou-0cyu` item G3 — and **they stay correct**.

**Nor does it re-prove the dimension count.**  `Mathlib/TwoRowDimCatalan.dimHLF_two_row_sq_sum`
already gives `∑_{ℓ(λ)≤2} (f^λ)² = catalan n`, sorry-free and for every `n`.  That is a
statement about the *target* of `twoRowProduct`; nothing here connects it to the `finrank`
of a quotient type, because that connection is the missing isomorphism.

## Scope

Convention **D** (`z = q³/(q²+1)`) throughout — the vanishing that makes the two-row part
the whole story is `ocneanuWeight_conventionD_eq_zero_of_three_rows`.  Base ring `ℝ`,
inherited from `wtrace`; `heckeProduct` itself is generic over `[Field K] [CharZero K]`, so
the pin enters only through the trace.  The ⊆ half takes `hgen : ∀ k, 0 < k → (q²)^k ≠ 1`
as a separate hypothesis, but it is **implied** by `hq2 : NotRootOfUnity q`, since
`(q²)^k = q^(2k)` (corrected 2026-10-11; this said "strictly stronger"). The generic-field
restatement `QOU.SchurWeyl.TraceQuotGeneric` takes only `hq0` and `hq2`.
-/

namespace QOU.SchurWeyl.WtraceRadicalIdeal

open YoungDiagram QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep
open QOU.SchurWeyl.WtraceRadicalTwoRow
open QOU.QBeta.TemperleyLiebTower QOU.QBeta.MarkovTraceQuotient

/-- **The at-most-two-row partitions of `n+1`.**  "At most two rows" is spelled
`rowLen 2 = 0` — row index 2 is empty — matching the hypothesis shape of
`mem_rad_iff_twoRow_blocks_vanish`.  Note the index shift: `Hecke ℝ q q⁻¹ n` is the algebra
whose blocks are partitions of `n + 1`. -/
abbrev TwoRowIdx (n : ℕ) : Type :=
  {lam : Nat.Partition (n + 1) // (partitionShape lam).rowLen 2 = 0}

/-- **The two-row projection.**  `heckeProduct` restricted to the at-most-two-row blocks;
at convention D these are exactly the blocks the Ocneanu weight does *not* kill. -/
noncomputable def twoRowProduct (q : ℝ) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Hecke ℝ q q⁻¹ n →ₐ[ℝ] (∀ lam : TwoRowIdx n,
      Matrix (StandardYoungTableau (partitionShape lam.1))
        (StandardYoungTableau (partitionShape lam.1)) ℝ) :=
  Pi.algHom _ _ (fun lam => seminormalRep q hq0 hq2 n (partitionShape_card_succ lam.1))

@[simp] theorem twoRowProduct_apply (q : ℝ) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (x : Hecke ℝ q q⁻¹ n) (lam : TwoRowIdx n) :
    twoRowProduct q hq0 hq2 n x lam
      = seminormalRep q hq0 hq2 n (partitionShape_card_succ lam.1) x := rfl

/-- **The two-row projection is onto.**  A component of `twoRowProduct` *is* the same
component of `heckeProduct`, so this is `heckeProduct_surjective` applied to the tuple that
extends the target by zero off the two-row blocks. -/
theorem twoRowProduct_surjective (q : ℝ) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Function.Surjective (twoRowProduct q hq0 hq2 n) := by
  classical
  intro f
  obtain ⟨b, hb⟩ := heckeProduct_surjective q hq0 hq2 n
    (fun lam => if h : (partitionShape lam).rowLen 2 = 0 then f ⟨lam, h⟩ else 0)
  refine ⟨b, ?_⟩
  funext lam
  have h1 : twoRowProduct q hq0 hq2 n b lam = heckeProduct q hq0 hq2 n b lam.1 := rfl
  rw [h1, hb]
  simp only [dif_pos lam.2]

/-- Kernel membership, unfolded to the blockwise condition. -/
theorem mem_ker_twoRowProduct_iff {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    x ∈ TwoSidedIdeal.ker (twoRowProduct q hq0 hq2 n)
      ↔ ∀ lam : TwoRowIdx n,
          seminormalRep q hq0 hq2 n (partitionShape_card_succ lam.1) x = 0 := by
  rw [TwoSidedIdeal.mem_ker]
  constructor
  · intro h lam
    have := congrFun h lam
    simpa using this
  · intro h
    funext lam
    simpa using h lam

/-- **The index bridge.**  `mem_rad_iff_twoRow_blocks_vanish` quantifies over *diagrams*
with `n+1` cells; `twoRowProduct` is indexed by *partitions* of `n+1`.  Forward is
instantiation at `partitionShape lam`; backward is `exists_partitionShape_eq` followed by
`subst` — not transport, since `d` is a variable, so no `HEq` is created.  The two
cardinality proofs that remain differ only as `Prop` terms, which proof irrelevance
closes. -/
theorem twoRow_blocks_vanish_iff {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    (∀ lam : TwoRowIdx n,
        seminormalRep q hq0 hq2 n (partitionShape_card_succ lam.1) x = 0)
      ↔ ∀ (d : YoungDiagram) (hd : d.cells.card = n + 1), d.rowLen 2 = 0 →
          seminormalRep q hq0 hq2 n hd x = 0 := by
  constructor
  · intro h d hd hrow
    obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq d hd
    subst hlam₀
    exact h ⟨lam₀, hrow⟩
  · intro h lam
    exact h _ (partitionShape_card_succ lam.1) lam.2

/-- **The trace radical of `wtrace` IS the kernel of the two-row projection**, as
two-sided ideals, for every `n`.

This is the object-level form of `mem_rad_iff_twoRow_blocks_vanish`.  With
`twoRowProduct_surjective` it is the full input to the first isomorphism theorem — but see
the file docstring: the isomorphism itself is **not** claimed here. -/
theorem traceRadicalIdeal_eq_ker {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) :
    traceRadicalIdeal (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)
      = TwoSidedIdeal.ker (twoRowProduct q hq0 hq2 n) := by
  ext x
  rw [mem_traceRadicalIdeal, mem_ker_twoRowProduct_iff,
    twoRow_blocks_vanish_iff hq0 hq2 n x]
  exact mem_rad_iff_twoRow_blocks_vanish hq0 hq2 hq21 hgen n x

/-- **The radical is proper**: `1` is not in it, so the quotient is nontrivial.  Immediate
from `wtrace 1 = 1`; recorded because a kernel identity alone does not rule out the
degenerate case where the projection is zero. -/
theorem one_notMem_traceRadicalIdeal {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    (1 : Hecke ℝ q q⁻¹ n) ∉ traceRadicalIdeal (wtrace q hq0 hq2 n)
      (wtrace_cyclic q hq0 hq2 n) := by
  rw [mem_traceRadicalIdeal]
  exact one_not_mem_traceRadical (wtrace q hq0 hq2 n)
    (by rw [wtrace_one q hq0 hq2 hq21 hgen n]; exact one_ne_zero)

end QOU.SchurWeyl.WtraceRadicalIdeal
