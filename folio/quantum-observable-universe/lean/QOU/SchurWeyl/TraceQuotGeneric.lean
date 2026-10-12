/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.MarkovTraceInstance
import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.SchurWeyl.MarkovConventionD
import QOU.SchurWeyl.TwoRowCorners
import QOU.QBeta.MarkovTraceQuotient
import QOU.Mathlib.YoungLatticeUpOperator
import QOU.Mathlib.BallotNumbers
import QOU.Mathlib.StandardYoungTableauBot
import QOU.Mathlib.TwoRowDimCatalan
import Mathlib.RingTheory.TwoSidedIdeal.Kernel
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix

/-!
# The trace-radical results over a generic field

The arc `WtraceRadicalIdeal` → `WtraceRadicalQuotient` → `TraceQuotCatalan` proves, at
convention D (`z = q³/(q²+1)`),

* `rad(wtrace) = ker(two-row projection)` (as two-sided ideals),
* `H_n(q)/rad(wtrace) ≃ₐ ∏_{ℓ(λ) ≤ 2} M_{f^λ}`,
* `finrank (H_n(q)/rad(wtrace)) = catalan (n+1)`,

but only for `q : ℝ`.  This file restates and proves all three over an arbitrary field `K`
with `[CharZero K]`, so that they apply at complex `q = e^{iπλ}` (non-root-of-unity `λ`).

## Where `ℝ` was used: nowhere essential

Audited line by line.  Every input is already generic:

* `wtrace`, `wtrace_cyclic`, `wtrace_one` (`MarkovTraceInstance`) — `[Field K]`;
* `heckeProduct`, `heckeProduct_surjective` (`HeckeProductSurjective`) — `[Field K] [CharZero K]`;
* `ocneanuWeight_conventionD_eq_zero_of_three_rows` (`OcneanuWeight`) — `[Field R]`;
* `ocneanuWeight_conventionD_ne_zero_of_two_rows` (`OcneanuWeightTwoRowNonzero`) — `[Field R]`;
* the matrix-pairing lemma — `[CommRing R]`.

No ordering, no positivity of the Ocneanu weights, no `Real.*` function is used anywhere in
the chain.  The `ℝ` in the three files was a **signature** specialisation only.  The one
algebraic fact the `⊆` half spends about the weights is that the at-most-two-row weights are
**nonzero**, and that is proved from genericity alone.

## The hypotheses collapse to `q ≠ 0` and `NotRootOfUnity q`

The `ℝ` statements carry four hypotheses: `hq0`, `hq2 : NotRootOfUnity q`,
`hq21 : q² + 1 ≠ 0`, `hgen : ∀ k > 0, (q²)^k ≠ 1`.  Two of them are **redundant**:

* `hgen` follows from `hq2`, because `(q²)^k = q^(2k)` and `2k > 0`
  (`hgen_of_notRootOfUnity`);
* `hq21` follows from `hq2`, because `q² = −1` gives `q⁴ = 1` (`hq21_of_notRootOfUnity`).

So the generic statements here take only `hq0` and `hq2`.  Note this **contradicts** the
docstring of `WtraceRadicalIdeal`, which says `hgen` is "strictly stronger than `hq2`"; the
implication runs the other way (`hq2 ⇒ hgen`).

`[CharZero K]` is inherited from `heckeProduct` (the seminormal construction divides by
quantum integers whose non-vanishing is argued there under `CharZero`); it is not used
anywhere else in this file.

## Why the file is self-contained

At the time of writing the restored olean tree lacks `OcneanuWeightTwoRowNonzero`,
`WtraceRadicalTwoRow*`, `WtraceRadicalIdeal`, `WtraceRadicalQuotient`,
`WtraceRadicalSemisimple`, `TwoRowIdxReindex` and `TwoRowSYTBallot`.  The short generic
lemmas they contribute are therefore re-proved here, inside this namespace, rather than
imported.  Their proofs are copies of those files' proofs with `ℝ` replaced by `K`; the
two-row tableau count (`numSYT_twoRow_eq_ballot`) has no field at all and is copied verbatim.

## 🛑 Scope, unchanged from the `ℝ` files

* Convention **D** only.
* `catalan (n+1)` is a **dimension**; this is **not** an isomorphism with `TL_n(δ)`.
* Genericity is required: at a root of unity `heckeProduct` is not defined by this
  construction and the statements are not claimed.

LaTeX label: `thm:trace-radical-generic-field`
-/

namespace QOU.SchurWeyl.TraceQuotGeneric

open YoungDiagram QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep
open QOU.QBeta.TemperleyLiebTower QOU.QBeta.MarkovTraceQuotient

/-! ## The genericity hypotheses that are implied by `NotRootOfUnity q` -/

/-- `NotRootOfUnity q` implies `q²` is not a root of unity. -/
theorem hgen_of_notRootOfUnity {K : Type*} [Field K] {q : K}
    (hq2 : GenericParameter.NotRootOfUnity q) :
    ∀ k : ℕ, 0 < k → (q ^ 2 : K) ^ k ≠ 1 := by
  intro k hk
  rw [← pow_mul]
  exact hq2 (2 * k) (by omega)

/-- `NotRootOfUnity q` implies `q² + 1 ≠ 0`: otherwise `q⁴ = (q²)² = 1`. -/
theorem hq21_of_notRootOfUnity {K : Type*} [Field K] {q : K}
    (hq2 : GenericParameter.NotRootOfUnity q) : q ^ 2 + 1 ≠ 0 := by
  intro h
  have hq : q ^ 2 = -1 := eq_neg_of_add_eq_zero_left h
  apply hq2 4 (by norm_num)
  rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, hq]
  norm_num

/-! ## Non-vanishing of the at-most-two-row Ocneanu weights (generic field)

Copied from `OcneanuWeightTwoRowNonzero` (whose olean is not in the restored tree); already
generic there. -/

theorem hookLength_pos' {mu : YoungDiagram} {c : ℕ × ℕ} (hc : c ∈ mu.cells) :
    0 < hookLength mu c := by
  classical
  have hmem : c ∈ mu.cells.filter (fun d => d.1 = c.1 ∧ c.2 ≤ d.2) := by
    simp [Finset.mem_filter, hc]
  have h1 : 0 < (mu.cells.filter (fun d => d.1 = c.1 ∧ c.2 ≤ d.2)).card :=
    Finset.card_pos.mpr ⟨c, hmem⟩
  simp only [hookLength]
  omega

theorem numFactor_conventionD {R : Type*} [Field R] (q : R)
    (hq21 : q ^ 2 + 1 ≠ 0) (i j : ℕ) :
    q ^ (2 * i) * (q ^ 2 - 1 - q * (q ^ 3 / (q ^ 2 + 1)))
        + q ^ (2 * j + 1) * (q ^ 3 / (q ^ 2 + 1))
      = (q ^ (2 * j + 4) - q ^ (2 * i)) / (q ^ 2 + 1) := by
  field_simp
  ring

theorem numFactor_conventionD_ne_zero {R : Type*} [Field R] (q : R)
    (hq0 : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : R) ^ k ≠ 1) (i j : ℕ) (hij : i ≤ j + 1) :
    q ^ (2 * i) * (q ^ 2 - 1 - q * (q ^ 3 / (q ^ 2 + 1)))
        + q ^ (2 * j + 1) * (q ^ 3 / (q ^ 2 + 1)) ≠ 0 := by
  rw [numFactor_conventionD q hq21 i j]
  refine div_ne_zero ?_ hq21
  have hsplit : q ^ (2 * j + 4) - q ^ (2 * i)
      = q ^ (2 * i) * ((q ^ 2) ^ (j + 2 - i) - 1) := by
    rw [mul_sub, mul_one, ← pow_mul, ← pow_add]
    congr 2
    omega
  rw [hsplit]
  exact mul_ne_zero (pow_ne_zero _ hq0)
    (sub_ne_zero_of_ne (hgen _ (by omega)))

theorem row_le_one_of_rowLen_two_eq_zero' {mu : YoungDiagram} (h : mu.rowLen 2 = 0)
    {c : ℕ × ℕ} (hc : c ∈ mu.cells) : c.1 ≤ 1 := by
  by_contra hlt
  have h2 : (2, c.2) ∈ mu := mu.up_left_mem (by omega) le_rfl hc
  rw [mem_iff_lt_rowLen, h] at h2
  omega

/-- **The convention-D Ocneanu weight of an at-most-two-row shape is nonzero**, over any
field, from `q ≠ 0` and `NotRootOfUnity q` alone. -/
theorem ocneanuWeight_ne_zero_of_two_rows {K : Type*} [Field K] (q : K)
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (mu : YoungDiagram) (h : mu.rowLen 2 = 0) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu ≠ 0 := by
  have hq21 := hq21_of_notRootOfUnity hq2
  have hgen := hgen_of_notRootOfUnity hq2
  rw [ocneanuWeight]
  refine div_ne_zero (Finset.prod_ne_zero_iff.mpr ?_) (Finset.prod_ne_zero_iff.mpr ?_)
  · intro c hc
    exact numFactor_conventionD_ne_zero q hq0 hq21 hgen c.1 c.2
      (le_trans (row_le_one_of_rowLen_two_eq_zero' h hc) (by omega))
  · intro c hc
    refine sub_ne_zero_of_ne ?_
    rw [pow_mul]
    exact hgen _ (hookLength_pos' hc)

/-! ## The radical of `wtrace` is the three-row part (generic field) -/

theorem exists_trace_mul_ne_zero {ι : Type*} [Fintype ι] [DecidableEq ι]
    {R : Type*} [CommRing R] {M : Matrix ι ι R} (hM : M ≠ 0) :
    ∃ N : Matrix ι ι R, (M * N).trace ≠ 0 := by
  classical
  obtain ⟨i, j, hij⟩ : ∃ i j, M i j ≠ 0 := by
    by_contra h
    push_neg at h
    exact hM (by ext a b; simpa using h a b)
  refine ⟨Matrix.of fun a b => if a = j ∧ b = i then (1 : R) else 0, ?_⟩
  have key : (M * Matrix.of fun a b => if a = j ∧ b = i then (1 : R) else 0).trace
      = M i j := by
    rw [Matrix.trace]
    rw [Finset.sum_eq_single_of_mem i (Finset.mem_univ i)]
    · simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.of_apply]
      rw [Finset.sum_eq_single_of_mem j (Finset.mem_univ j)]
      · simp
      · intro b _ hb
        simp [hb]
    · intro a _ ha
      simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.of_apply]
      exact Finset.sum_eq_zero fun b _ => by simp [ha]
  rw [key]
  exact hij

variable {K : Type*} [Field K] [CharZero K]

omit [CharZero K] in
/-- **⊇** over a generic field: needs only `q² + 1 ≠ 0` (for the three-row weights to vanish),
which `NotRootOfUnity q` supplies; no `CharZero`. -/
theorem mem_rad_of_twoRow_blocks_vanish {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (x : Hecke K q q⁻¹ n)
    (hx : ∀ (d : YoungDiagram) (hd : d.cells.card = n + 1), d.rowLen 2 = 0 →
      seminormalRep q hq0 hq2 n hd x = 0)
    (b : Hecke K q q⁻¹ n) :
    wtrace q hq0 hq2 n (x * b) = 0 := by
  rw [wtrace_apply]
  refine Finset.sum_eq_zero ?_
  rintro ⟨d, hd⟩ -
  rcases Nat.eq_zero_or_pos (d.rowLen 2) with hrow | hrow
  · have hxb : seminormalRep q hq0 hq2 n hd (x * b) = 0 := by
      rw [map_mul, hx d hd hrow, zero_mul]
    rw [hxb, Matrix.trace_zero, mul_zero]
  · have hw : ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) d = 0 :=
      ocneanuWeight_conventionD_eq_zero_of_three_rows q (hq21_of_notRootOfUnity hq2) d hrow
    rw [hw, zero_mul]

/-- **⊆** over a generic field: a live two-row block is seen by `wtrace`.  Uses only that
the two-row weights are **nonzero** — no positivity. -/
theorem notMem_rad_of_twoRow_block_ne_zero {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (x : Hecke K q q⁻¹ n) (d : YoungDiagram) (hd : d.cells.card = n + 1)
    (hrow : d.rowLen 2 = 0) (hne : seminormalRep q hq0 hq2 n hd x ≠ 0) :
    ∃ b : Hecke K q q⁻¹ n, wtrace q hq0 hq2 n (x * b) ≠ 0 := by
  classical
  obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq d hd
  subst hlam₀
  obtain ⟨N, hN⟩ := exists_trace_mul_ne_zero
    (M := seminormalRep q hq0 hq2 n hd x) hne
  obtain ⟨b, hb⟩ := heckeProduct_surjective q hq0 hq2 n (Function.update 0 lam₀ N)
  refine ⟨b, ?_⟩
  rw [wtrace_apply]
  rw [← Equiv.sum_comp (partitionShapeEquiv (n + 1))
    (fun ν : {ν : YoungDiagram // ν.cells.card = n + 1} =>
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1
        * (seminormalRep q hq0 hq2 n ν.2 (x * b)).trace)]
  have hρ : ∀ (lam : Nat.Partition (n + 1)) (y : Hecke K q q⁻¹ n),
      seminormalRep q hq0 hq2 n (partitionShapeEquiv (n + 1) lam).2 y
        = heckeProduct q hq0 hq2 n y lam := fun _ _ => rfl
  rw [Finset.sum_eq_single_of_mem lam₀ (Finset.mem_univ lam₀)]
  · have hbN : heckeProduct q hq0 hq2 n b lam₀ = N := by rw [hb]; simp
    have htr : (seminormalRep q hq0 hq2 n (partitionShapeEquiv (n + 1) lam₀).2 (x * b)).trace
        = (seminormalRep q hq0 hq2 n hd x * N).trace := by
      rw [map_mul, hρ lam₀ b, hbN]
      rfl
    refine mul_ne_zero (ocneanuWeight_ne_zero_of_two_rows q hq0 hq2 _ hrow) ?_
    rw [htr]; exact hN
  · intro lam _ hlam
    have hbz : heckeProduct q hq0 hq2 n b lam = 0 := by rw [hb]; simp [hlam]
    have hz : seminormalRep q hq0 hq2 n (partitionShapeEquiv (n + 1) lam).2 (x * b) = 0 := by
      rw [map_mul, hρ lam b, hbz, mul_zero]
    rw [hz, Matrix.trace_zero, mul_zero]

/-- **The radical of `wtrace` is exactly the three-row part**, over any `CharZero` field. -/
theorem mem_rad_iff_twoRow_blocks_vanish {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    (∀ b : Hecke K q q⁻¹ n, wtrace q hq0 hq2 n (x * b) = 0)
      ↔ ∀ (d : YoungDiagram) (hd : d.cells.card = n + 1), d.rowLen 2 = 0 →
          seminormalRep q hq0 hq2 n hd x = 0 := by
  refine ⟨fun h d hd hrow => ?_, fun h => mem_rad_of_twoRow_blocks_vanish hq0 hq2 n x h⟩
  by_contra hne
  obtain ⟨b, hb⟩ := notMem_rad_of_twoRow_block_ne_zero hq0 hq2 n x d hd hrow hne
  exact hb (h b)

/-! ## Theorem 1: `rad(wtrace) = ker(twoRowProduct)` -/

/-- The at-most-two-row partitions of `n+1`. -/
abbrev TwoRowIdx (n : ℕ) : Type :=
  {lam : Nat.Partition (n + 1) // (partitionShape lam).rowLen 2 = 0}

/-- The target of the two-row projection over `K`. -/
abbrev TwoRowBlocks (K : Type*) [Field K] (n : ℕ) : Type _ :=
  ∀ lam : TwoRowIdx n, Matrix (StandardYoungTableau (partitionShape lam.1))
    (StandardYoungTableau (partitionShape lam.1)) K

/-- The two-row projection over a generic field. -/
noncomputable def twoRowProduct (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Hecke K q q⁻¹ n →ₐ[K] TwoRowBlocks K n :=
  Pi.algHom _ _ (fun lam => seminormalRep q hq0 hq2 n (partitionShape_card_succ lam.1))

omit [CharZero K] in
@[simp] theorem twoRowProduct_apply (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (x : Hecke K q q⁻¹ n) (lam : TwoRowIdx n) :
    twoRowProduct q hq0 hq2 n x lam
      = seminormalRep q hq0 hq2 n (partitionShape_card_succ lam.1) x := rfl

theorem twoRowProduct_surjective (q : K) (hq0 : q ≠ 0)
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

omit [CharZero K] in
theorem mem_ker_twoRowProduct_iff {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x : Hecke K q q⁻¹ n) :
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

omit [CharZero K] in
theorem twoRow_blocks_vanish_iff {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x : Hecke K q q⁻¹ n) :
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
two-sided ideals, over any `CharZero` field `K`, for `q ≠ 0` not a root of unity. -/
theorem traceRadicalIdeal_eq_ker {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    traceRadicalIdeal (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)
      = TwoSidedIdeal.ker (twoRowProduct q hq0 hq2 n) := by
  ext x
  rw [mem_traceRadicalIdeal, mem_ker_twoRowProduct_iff,
    twoRow_blocks_vanish_iff hq0 hq2 n x]
  exact mem_rad_iff_twoRow_blocks_vanish hq0 hq2 n x

/-! ## Theorem 2: `H/rad ≃ₐ[K] ∏_{ℓ(λ) ≤ 2} M_{f^λ}(K)` -/

theorem ringCon_iff_twoRowProduct_eq {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x y : Hecke K q q⁻¹ n) :
    (traceRadicalIdeal (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)).ringCon x y
      ↔ twoRowProduct q hq0 hq2 n x = twoRowProduct q hq0 hq2 n y := by
  rw [TwoSidedIdeal.rel_iff, traceRadicalIdeal_eq_ker hq0 hq2 n,
    TwoSidedIdeal.mem_ker, map_sub, sub_eq_zero]

/-- The two-row projection descended to the quotient (inlined against the corpus's
`instAlgebraTraceQuot`, for the instance-collision reason recorded in
`WtraceRadicalQuotient.twoRowQuotHom`). -/
noncomputable def twoRowQuotHom {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n) →ₐ[K] TwoRowBlocks K n where
  toFun := Quotient.lift (⇑(twoRowProduct q hq0 hq2 n))
    (fun x y h => (ringCon_iff_twoRowProduct_eq hq0 hq2 n x y).mp h)
  map_one' := map_one (twoRowProduct q hq0 hq2 n)
  map_mul' := by rintro ⟨a⟩ ⟨b⟩; exact map_mul (twoRowProduct q hq0 hq2 n) a b
  map_zero' := map_zero (twoRowProduct q hq0 hq2 n)
  map_add' := by rintro ⟨a⟩ ⟨b⟩; exact map_add (twoRowProduct q hq0 hq2 n) a b
  commutes' r := (twoRowProduct q hq0 hq2 n).commutes r

@[simp] theorem twoRowQuotHom_coe {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    twoRowQuotHom hq0 hq2 n
        (x : TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n))
      = twoRowProduct q hq0 hq2 n x := rfl

theorem twoRowQuotHom_bijective {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Function.Bijective (twoRowQuotHom hq0 hq2 n) := by
  constructor
  · rintro ⟨a⟩ ⟨b⟩ hab
    exact Quotient.sound ((ringCon_iff_twoRowProduct_eq hq0 hq2 n a b).mpr hab)
  intro f
  obtain ⟨b, hb⟩ := twoRowProduct_surjective q hq0 hq2 n f
  refine ⟨(b : TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)), ?_⟩
  rw [twoRowQuotHom_coe]
  exact hb

/-- **`H_n(q)/rad(wtrace) ≃ₐ[K] ∏_{ℓ(λ) ≤ 2} M_{f^λ}(K)`**, over any `CharZero` field `K`,
convention D, for `q ≠ 0` not a root of unity. -/
noncomputable def traceQuotEquiv {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n) ≃ₐ[K] TwoRowBlocks K n :=
  AlgEquiv.ofBijective _ (twoRowQuotHom_bijective hq0 hq2 n)

@[simp] theorem traceQuotEquiv_coe {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    traceQuotEquiv hq0 hq2 n
        (x : TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n))
      = twoRowProduct q hq0 hq2 n x := rfl

omit [CharZero K] in
/-- The isomorphism is not between one-point algebras: `[1] ≠ 0` in the quotient. -/
theorem traceQuot_one_ne_zero {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    ((1 : Hecke K q q⁻¹ n) :
        TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) ≠ 0 :=
  quot_one_ne_zero (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)
    (by rw [wtrace_one q hq0 hq2 (hq21_of_notRootOfUnity hq2) (hgen_of_notRootOfUnity hq2) n]
        exact one_ne_zero)

/-! ## Theorem 3: `finrank (H/rad) = catalan (n+1)` -/

theorem finrank_traceQuot {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Module.finrank K (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n))
      = ∑ lam : TwoRowIdx n,
          Fintype.card (StandardYoungTableau (partitionShape lam.1))
            * Fintype.card (StandardYoungTableau (partitionShape lam.1)) := by
  haveI : ∀ lam : TwoRowIdx n, Module.Finite K (Matrix (StandardYoungTableau (partitionShape lam.1))
      (StandardYoungTableau (partitionShape lam.1)) K) := fun _ => Module.Finite.matrix
  rw [(traceQuotEquiv hq0 hq2 n).toLinearEquiv.finrank_eq,
    Module.finrank_pi_fintype]
  refine Finset.sum_congr rfl fun lam _ => ?_
  rw [Module.finrank_matrix, Module.finrank_self, mul_one]

/-! ### Reindexing by second-row length (field-free; copied from `TwoRowIdxReindex`) -/

theorem rowLen_twoRow_two {m k : ℕ} (h : k ≤ m) : (twoRow m k h).rowLen 2 = 0 := by
  by_contra hne
  have hmem : (2, 0) ∈ twoRow m k h :=
    YoungDiagram.mem_iff_lt_rowLen.mpr (by omega)
  rw [mem_twoRow] at hmem
  omega

theorem twoRow_congr {m m' k k' : ℕ} (h : k ≤ m) (h' : k' ≤ m') (hm : m = m') (hk : k = k') :
    twoRow m k h = twoRow m' k' h' := by
  subst hm; subst hk; rfl

theorem rowLen_add {n : ℕ} (lam : TwoRowIdx n) :
    (partitionShape lam.1).rowLen 0 + (partitionShape lam.1).rowLen 1 = n + 1 := by
  have hc : (partitionShape lam.1).cells.card = n + 1 := partitionShape_card_succ lam.1
  rw [eq_twoRow_of_rowLen_two_eq_zero _ lam.2, card_twoRow] at hc
  exact hc

theorem secondRow_le {n : ℕ} (lam : TwoRowIdx n) :
    (partitionShape lam.1).rowLen 1 ≤ (n + 1) / 2 := by
  have h1 := rowLen_add lam
  have h2 : (partitionShape lam.1).rowLen 1 ≤ (partitionShape lam.1).rowLen 0 :=
    YoungDiagram.rowLen_anti _ 0 1 (by omega)
  omega

noncomputable def ofSecondRow (n k : ℕ) (hk : 2 * k ≤ n + 1) : TwoRowIdx n :=
  ⟨(exists_partitionShape_eq (twoRow (n + 1 - k) k (by omega))
      (by rw [card_twoRow]; omega)).choose,
   by
     rw [(exists_partitionShape_eq (twoRow (n + 1 - k) k (by omega))
       (by rw [card_twoRow]; omega)).choose_spec]
     exact rowLen_twoRow_two _⟩

@[simp] theorem shape_ofSecondRow (n k : ℕ) (hk : 2 * k ≤ n + 1) :
    partitionShape (ofSecondRow n k hk).1 = twoRow (n + 1 - k) k (by omega) :=
  (exists_partitionShape_eq (twoRow (n + 1 - k) k (by omega))
    (by rw [card_twoRow]; omega)).choose_spec

@[simp] theorem secondRow_ofSecondRow (n k : ℕ) (hk : 2 * k ≤ n + 1) :
    (partitionShape (ofSecondRow n k hk).1).rowLen 1 = k := by
  rw [shape_ofSecondRow, rowLen_twoRow_one]

theorem ofSecondRow_secondRow {n : ℕ} (lam : TwoRowIdx n) :
    ofSecondRow n ((partitionShape lam.1).rowLen 1)
        (by have := secondRow_le lam; omega) = lam := by
  refine Subtype.ext (partitionShape_injective ?_)
  rw [shape_ofSecondRow]
  refine (twoRow_congr _ _ ?_ rfl).trans (eq_twoRow_of_rowLen_two_eq_zero _ lam.2).symm
  have := rowLen_add lam
  omega

noncomputable def twoRowIdxEquiv (n : ℕ) : TwoRowIdx n ≃ Fin ((n + 1) / 2 + 1) where
  toFun lam := ⟨(partitionShape lam.1).rowLen 1, by have := secondRow_le lam; omega⟩
  invFun k := ofSecondRow n k.1 (by have := k.2; omega)
  left_inv lam := ofSecondRow_secondRow lam
  right_inv k := Fin.ext (by simp [rowLen_twoRow_one])

@[simp] theorem twoRowIdxEquiv_apply {n : ℕ} (lam : TwoRowIdx n) :
    (twoRowIdxEquiv n lam : ℕ) = (partitionShape lam.1).rowLen 1 := rfl

noncomputable def twoRowDim (m k : ℕ) : ℕ :=
  if h : k ≤ m then numStandardYoungTableaux (twoRow m k h) else 0

theorem twoRowDim_eq {m k : ℕ} (h : k ≤ m) :
    twoRowDim m k = numStandardYoungTableaux (twoRow m k h) := by
  rw [twoRowDim, dif_pos h]

theorem finrank_traceQuot_eq_range_sum {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Module.finrank K (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n))
      = ∑ k ∈ Finset.range ((n + 1) / 2 + 1), twoRowDim (n + 1 - k) k ^ 2 := by
  rw [finrank_traceQuot hq0 hq2 n,
    ← Fin.sum_univ_eq_sum_range (fun k => twoRowDim (n + 1 - k) k ^ 2) ((n + 1) / 2 + 1)]
  refine Fintype.sum_equiv (twoRowIdxEquiv n) _ _ ?_
  intro lam
  have hle : (partitionShape lam.1).rowLen 1 ≤ n + 1 - (partitionShape lam.1).rowLen 1 := by
    have := rowLen_add lam
    have h2 : (partitionShape lam.1).rowLen 1 ≤ (partitionShape lam.1).rowLen 0 :=
      YoungDiagram.rowLen_anti _ 0 1 (by omega)
    omega
  have hshape : twoRow (n + 1 - (partitionShape lam.1).rowLen 1)
      ((partitionShape lam.1).rowLen 1) hle = partitionShape lam.1 := by
    refine (twoRow_congr _ _ ?_ rfl).trans (eq_twoRow_of_rowLen_two_eq_zero _ lam.2).symm
    have := rowLen_add lam
    omega
  have hnum : numStandardYoungTableaux (partitionShape lam.1)
      = Fintype.card (StandardYoungTableau (partitionShape lam.1)) :=
    Nat.card_eq_fintype_card
  rw [twoRowIdxEquiv_apply, twoRowDim_eq hle, hshape, hnum, sq]

/-! ### Two-row tableau count = ballot number (field-free; copied from `TwoRowSYTBallot`) -/

section Ballot

def cornerTwoRow (m k : ℕ) : Finset (ℕ × ℕ) :=
  (if k < m then {((0 : ℕ), m - 1)} else ∅) ∪ (if 0 < k then {((1 : ℕ), k - 1)} else ∅)

theorem mem_cornerTwoRow {m k : ℕ} (r : ℕ × ℕ) :
    r ∈ cornerTwoRow m k ↔ (r = (0, m - 1) ∧ k < m) ∨ (r = (1, k - 1) ∧ 0 < k) := by
  unfold cornerTwoRow
  split_ifs <;> simp_all [Prod.ext_iff] <;> omega

theorem cornerCells_twoRow {m k : ℕ} (h : k ≤ m) :
    cornerCells (twoRow m k h) = cornerTwoRow m k := by
  ext r
  rw [mem_cornerCells, isCornerCell_twoRow_iff h, mem_cornerTwoRow]

theorem sum_cornerTwoRow_expand {m k : ℕ} {M : Type*} [AddCommMonoid M] (f : ℕ × ℕ → M) :
    ∑ r ∈ cornerTwoRow m k, f r
      = (if k < m then f (0, m - 1) else 0) + (if 0 < k then f (1, k - 1) else 0) := by
  unfold cornerTwoRow
  split_ifs <;>
    simp [Finset.sum_insert, Prod.ext_iff] <;> abel

theorem eraseCornerOrSelf_twoRow_row0 {m k : ℕ} (h : k ≤ m) (hkm : k < m) :
    eraseCornerOrSelf (twoRow m k h) (0, m - 1) = twoRow (m - 1) k (by omega) := by
  have hc : IsCornerCell (twoRow m k h) (0, m - 1) :=
    (isCornerCell_twoRow_iff h _).mpr (Or.inl ⟨rfl, hkm⟩)
  rw [eraseCornerOrSelf_of hc]
  ext c
  obtain ⟨i, j⟩ := c
  rw [show ((i, j) ∈ (eraseCorner (twoRow m k h) (0, m - 1) hc).cells)
      ↔ ((i, j) ∈ eraseCorner (twoRow m k h) (0, m - 1) hc) from Iff.rfl,
    mem_eraseCorner _ _ hc,
    show ((i, j) ∈ (twoRow (m - 1) k (by omega : k ≤ m - 1)).cells)
      ↔ ((i, j) ∈ twoRow (m - 1) k (by omega : k ≤ m - 1)) from Iff.rfl,
    mem_twoRow, mem_twoRow]
  simp only [ne_eq, Prod.mk.injEq, not_and]
  omega

theorem eraseCornerOrSelf_twoRow_row1 {m k : ℕ} (h : k ≤ m) (hk0 : 0 < k) :
    eraseCornerOrSelf (twoRow m k h) (1, k - 1) = twoRow m (k - 1) (by omega) := by
  have hc : IsCornerCell (twoRow m k h) (1, k - 1) :=
    (isCornerCell_twoRow_iff h _).mpr (Or.inr ⟨rfl, hk0⟩)
  rw [eraseCornerOrSelf_of hc]
  ext c
  obtain ⟨i, j⟩ := c
  rw [show ((i, j) ∈ (eraseCorner (twoRow m k h) (1, k - 1) hc).cells)
      ↔ ((i, j) ∈ eraseCorner (twoRow m k h) (1, k - 1) hc) from Iff.rfl,
    mem_eraseCorner _ _ hc,
    show ((i, j) ∈ (twoRow m (k - 1) (by omega : k - 1 ≤ m)).cells)
      ↔ ((i, j) ∈ twoRow m (k - 1) (by omega : k - 1 ≤ m)) from Iff.rfl,
    mem_twoRow, mem_twoRow]
  simp only [ne_eq, Prod.mk.injEq, not_and]
  omega

theorem eraseCornerOrSelf_twoRow_row0_succ (M k : ℕ) (h : k ≤ M + 1) (hkm : k < M + 1) :
    eraseCornerOrSelf (twoRow (M + 1) k h) (0, M) = twoRow M k (by omega) := by
  simpa using eraseCornerOrSelf_twoRow_row0 h hkm

theorem eraseCornerOrSelf_twoRow_row1_succ (m j : ℕ) (h : j + 1 ≤ m) :
    eraseCornerOrSelf (twoRow m (j + 1) h) (1, j) = twoRow m j (by omega) := by
  simpa using eraseCornerOrSelf_twoRow_row1 h (Nat.succ_pos j)

theorem twoRow_zero_zero : twoRow 0 0 le_rfl = (⊥ : YoungDiagram) := by
  ext c
  obtain ⟨i, j⟩ := c
  rw [show ((i, j) ∈ (twoRow 0 0 le_rfl).cells) ↔ ((i, j) ∈ twoRow 0 0 le_rfl) from Iff.rfl,
    mem_twoRow]
  simp

theorem numSYT_twoRow_zero (m : ℕ) (h : 0 ≤ m) :
    numStandardYoungTableaux (twoRow m 0 h) = 1 := by
  induction m with
  | zero => rw [twoRow_zero_zero, numStandardYoungTableaux_bot]
  | succ n ih =>
      rw [branching_finset _ (by rw [card_twoRow]; omega), cornerCells_twoRow h,
        sum_cornerTwoRow_expand, if_pos (Nat.succ_pos n),
        if_neg (by omega : ¬ (0 : ℕ) < 0), add_zero]
      rw [show (n + 1 - 1 : ℕ) = n from rfl,
        eraseCornerOrSelf_twoRow_row0_succ n 0 h (Nat.succ_pos n)]
      exact ih (Nat.zero_le n)

theorem numSYT_twoRow_rec_lt (M j : ℕ) (hjM : j + 1 ≤ M) :
    numStandardYoungTableaux (twoRow (M + 1) (j + 1) (by omega))
      = numStandardYoungTableaux (twoRow M (j + 1) (by omega))
        + numStandardYoungTableaux (twoRow (M + 1) j (by omega)) := by
  rw [branching_finset _ (by rw [card_twoRow]; omega), cornerCells_twoRow (by omega : j + 1 ≤ M + 1),
    sum_cornerTwoRow_expand, if_pos (by omega : j + 1 < M + 1), if_pos (Nat.succ_pos j),
    show (M + 1 - 1 : ℕ) = M from rfl,
    show (j + 1 - 1 : ℕ) = j from rfl,
    eraseCornerOrSelf_twoRow_row0_succ M (j + 1) (by omega) (by omega),
    eraseCornerOrSelf_twoRow_row1_succ (M + 1) j (by omega)]

theorem numSYT_twoRow_rec_eq (j : ℕ) :
    numStandardYoungTableaux (twoRow (j + 1) (j + 1) le_rfl)
      = numStandardYoungTableaux (twoRow (j + 1) j (by omega)) := by
  rw [branching_finset _ (by rw [card_twoRow]; omega), cornerCells_twoRow le_rfl,
    sum_cornerTwoRow_expand, if_neg (by omega : ¬ j + 1 < j + 1), if_pos (Nat.succ_pos j),
    zero_add, show (j + 1 - 1 : ℕ) = j from rfl,
    eraseCornerOrSelf_twoRow_row1_succ (j + 1) j le_rfl]

theorem numSYT_twoRow_eq_ballot (m k : ℕ) (h : k ≤ m) :
    (numStandardYoungTableaux (twoRow m k h) : ℤ) = ballot (m + k) k := by
  induction k generalizing m with
  | zero => rw [numSYT_twoRow_zero m h, ballot_zero]; norm_num
  | succ j ihj =>
      induction m, h using Nat.le_induction with
      | base =>
          rw [numSYT_twoRow_rec_eq j, ihj (j + 1) (by omega)]
          have hbs := ballot_succ_succ (2 * j + 1) j
          have hbz := ballot_boundary_zero j
          rw [show (j + 1 + (j + 1) : ℕ) = 2 * j + 1 + 1 from by omega, hbs, hbz, zero_add,
            show (j + 1 + j : ℕ) = 2 * j + 1 from by omega]
      | succ M hjM ihM =>
          rw [numSYT_twoRow_rec_lt M j hjM]
          push_cast
          rw [ihM, ihj (M + 1) (by omega)]
          have hbs := ballot_succ_succ (M + j + 1) j
          rw [show (M + 1 + (j + 1) : ℕ) = M + j + 1 + 1 from by omega,
            show (M + (j + 1) : ℕ) = M + j + 1 from by omega,
            show (M + 1 + j : ℕ) = M + j + 1 from by omega, hbs]

end Ballot

/-- **`dim_K (H_n(q)/rad(wtrace)) = catalan (n+1)`**, over any `CharZero` field `K`, for
`q ≠ 0` not a root of unity.  🛑 A dimension, **not** an isomorphism with `TL_n(δ)`. -/
theorem finrank_traceQuot_eq_catalan {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    (Module.finrank K (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) : ℤ)
      = catalan (n + 1) := by
  rw [finrank_traceQuot_eq_range_sum hq0 hq2 n, ← dimHLF_two_row_sq_sum (n + 1)]
  push_cast
  refine Finset.sum_congr rfl fun k hk => ?_
  have hkr : k < (n + 1) / 2 + 1 := Finset.mem_range.mp hk
  have hk2 : 2 * k ≤ n + 1 := by omega
  have h1 : k ≤ n + 1 - k := by omega
  rw [twoRowDim_eq h1]
  rw [numSYT_twoRow_eq_ballot (n + 1 - k) k h1,
    show (n + 1 - k + k : ℕ) = n + 1 from by omega,
    ← dimHLF_two_row_eq_ballot (n + 1) k hk2]

/-! ## The `ℝ` and `ℂ` instances

The `ℝ` corollaries carry the original four-hypothesis signature, to show the extra two are
dead weight; they are the generic theorems at `K := ℝ`.  (They are not literally the
declarations in `WtraceRadicalIdeal` / `TraceQuotCatalan`, whose oleans are not in the
restored tree, but `wtrace`, `heckeProduct` and `seminormalRep` are generic definitions, so
both sides of each statement are the same terms.) -/

theorem traceRadicalIdeal_eq_ker_real {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (_hq21 : q ^ 2 + 1 ≠ 0)
    (_hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) :
    traceRadicalIdeal (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)
      = TwoSidedIdeal.ker (twoRowProduct q hq0 hq2 n) :=
  traceRadicalIdeal_eq_ker hq0 hq2 n

theorem finrank_traceQuot_eq_catalan_real {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (_hq21 : q ^ 2 + 1 ≠ 0)
    (_hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    (Module.finrank ℝ (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) : ℤ)
      = catalan (n + 1) :=
  finrank_traceQuot_eq_catalan hq0 hq2 n

/-- The complex instance: the dimension count at any nonzero complex `q` that is not a root of
unity (e.g. `q = e^{iπλ}` with `λ` irrational), as needed for the Kohno comparison. -/
theorem finrank_traceQuot_eq_catalan_complex {q : ℂ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    (Module.finrank ℂ (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) : ℤ)
      = catalan (n + 1) :=
  finrank_traceQuot_eq_catalan hq0 hq2 n

end QOU.SchurWeyl.TraceQuotGeneric
