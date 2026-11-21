import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Algebra.Equiv
import QOU.QBeta.TemperleyLiebTower

/-!
# The trace radical of a weighted block trace vanishes

**Bean `qou-cds1`.** Wedderburn-side infrastructure for the one open item left by
`QOU.MathlibExt.HeckeToTemperleyLieb`:

> `⟨U_i U_j U_i − v²·U_i⟩ = traceRadical tr_M` — the `⊇` half.

That half says the Markov trace *sees everything outside the ideal*, i.e. the
induced form on `TL_n(δ)` is nondegenerate. Once `TL_n(δ)` is known semisimple
and its Markov trace is identified as a weighted sum of block traces, the
nondegeneracy is **pure algebra**, and this file supplies it in the shape the
application needs:

    A ≃ₐ[K] Π i, Matrix (d i) (d i) K      and      τ = Σ_i y_i · trace_i
    with every  y_i ≠ 0                    ⟹        traceRadical τ = {0}.

## What was already in Mathlib, and what was not

**The single-block case is in Mathlib and I nearly re-proved it.** A first search
for `nondegenerate` / `trace.*eq_zero` came back empty and I recorded the matrix
trace form as a Mathlib gap; it is not one. `Matrix.ext_iff_trace_mul_right`
(`A = B ↔ ∀ x, (A * x).trace = (B * x).trace`) is exactly nondegeneracy, phrased
as an extensionality lemma, which is why a search on the word "nondegenerate"
misses it. Recorded because the near-miss is the interesting part: the lemma you
want may be in Mathlib under the *shape* it is used for rather than the *name*
it is known by.

**The weighted-product case is genuinely absent**, and it is the one the
application needs — the Markov trace is not a block trace, it is a weighted sum
of them, and the weights are what carry the physics.

## What this file does NOT do

It does **not** prove `TL_n(δ)` semisimple, and does not produce the `AlgEquiv`.
That is the deep input, and it remains open. What is closed here is everything
downstream of it: given the decomposition and nonzero weights, the radical is
zero. The nonzero-weights hypothesis is *already discharged in this corpus* —
`QOU.QBeta.TemperleyLiebTower.yw_pos` gives `0 < y_λ` for `1 < q` — so the
decomposition is the sole remaining input.

-- Ref: [leitner2026] rem:hecke-radical-is-temperley-lieb — the claim this serves.
-/

namespace QOU.MathlibExt.TraceRadicalNondegenerate

open QOU.QBeta.TemperleyLiebTower (traceRadical)

/-! ## One block -/

section OneBlock

variable {n : Type*} [Fintype n] [DecidableEq n] {K : Type*} [CommRing K]

/-- **The matrix trace form has zero radical.**

A restatement of `Matrix.ext_iff_trace_mul_right` in the `traceRadical`
vocabulary this corpus uses. Kept because the translation is where the two
libraries meet, not because the content is new. -/
theorem matrix_traceRadical_eq_zero :
    traceRadical (Matrix.trace : Matrix n n K → K) = {(0 : Matrix n n K)} := by
  ext A
  constructor
  · intro hA
    have h : ∀ x : Matrix n n K, (A * x).trace = ((0 : Matrix n n K) * x).trace := by
      intro x
      rw [hA x, zero_mul, Matrix.trace_zero]
    exact Matrix.ext_iff_trace_mul_right.mpr h
  · rintro rfl
    intro b
    rw [zero_mul, Matrix.trace_zero]

omit [DecidableEq n] in
/-- The form of the above actually used below: pairing to zero against every
matrix forces vanishing. -/
theorem matrix_eq_zero_of_forall_trace_mul {A : Matrix n n K}
    (h : ∀ x : Matrix n n K, (A * x).trace = 0) : A = 0 :=
  Matrix.ext_iff_trace_mul_right.mpr fun x => by rw [h x, zero_mul, Matrix.trace_zero]

end OneBlock

/-! ## Many blocks, with weights -/

section Blocks

variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {d : ι → Type*} [∀ i, Fintype (d i)] [∀ i, DecidableEq (d i)]
variable {K : Type*} [Field K]

/-- **The weighted block trace** `τ(a) = Σ_i y_i · tr(a_i)` on a finite product
of matrix algebras.

This is the shape of every Markov trace in this corpus: `tr_M = Σ_λ y_λ χ_λ`,
with the `y_λ` the Wedderburn weights. -/
def weightedBlockTrace (y : ι → K) (a : ∀ i, Matrix (d i) (d i) K) : K :=
  ∑ i, y i * (a i).trace

omit [DecidableEq ι] [∀ i, DecidableEq (d i)] in
@[simp] theorem weightedBlockTrace_zero (y : ι → K) :
    weightedBlockTrace (d := d) y 0 = 0 := by
  simp [weightedBlockTrace]

/-- **The radical of a weighted block trace is zero exactly when no weight
vanishes — the `←` direction.**

If some `y_j = 0` the `j`-th block is invisible to `τ` and lies in the radical;
with every weight nonzero, testing against `Pi.single j x` isolates one block and
`matrix_eq_zero_of_forall_trace_mul` finishes it.

The weights are where the content is: this is the formal statement of "the trace
sees every block". -/
theorem weightedBlockTrace_traceRadical_eq_zero {y : ι → K} (hy : ∀ i, y i ≠ 0) :
    traceRadical (weightedBlockTrace (d := d) y) = {(0 : ∀ i, Matrix (d i) (d i) K)} := by
  ext a
  constructor
  · intro ha
    funext j
    refine matrix_eq_zero_of_forall_trace_mul fun x => ?_
    have hb := ha (Pi.single j x)
    rw [weightedBlockTrace, Finset.sum_eq_single j] at hb
    · have : y j * (a j * x).trace = 0 := by
        simpa [Pi.single_eq_same] using hb
      exact (mul_eq_zero.mp this).resolve_left (hy j)
    · intro i _ hij
      simp [Pi.single_eq_of_ne hij]
    · intro h
      exact absurd (Finset.mem_univ j) h
  · rintro rfl
    intro b
    rw [zero_mul]
    exact weightedBlockTrace_zero y

/-- **The nonzero-weight hypothesis cannot be dropped.**

If `y j = 0` and the `j`-th block is not the zero algebra, then that whole block
lies in the radical, so the radical is strictly bigger than `{0}`. The witness is
the identity of the `j`-th block, sitting at `j` and zero elsewhere.

Stated so that `weightedBlockTrace_traceRadical_eq_zero`'s hypothesis is visibly
load-bearing rather than decorative: with it the radical vanishes, without it —
at any single index — it does not. -/
theorem weightedBlockTrace_traceRadical_ne_zero {y : ι → K} {j : ι}
    (hj : y j = 0) [Nonempty (d j)] :
    traceRadical (weightedBlockTrace (d := d) y)
      ≠ {(0 : ∀ i, Matrix (d i) (d i) K)} := by
  intro hcontra
  have hmem : Pi.single j (1 : Matrix (d j) (d j) K)
      ∈ traceRadical (weightedBlockTrace (d := d) y) := by
    intro b
    rw [weightedBlockTrace, Finset.sum_eq_zero]
    intro i _
    by_cases hij : i = j
    · subst hij
      simp [hj]
    · simp [Pi.single_eq_of_ne hij]
  -- the witness is in the radical, so by `hcontra` it is `0` — but its `j`-th
  -- component is `1`, and `Matrix (d j) (d j) K` is nontrivial.
  rw [hcontra, Set.mem_singleton_iff] at hmem
  have h1 := congrFun hmem j
  simp at h1

end Blocks

/-! ## Transport along an algebra isomorphism -/

section Transport

variable {K : Type*} [CommRing K] {A B : Type*} [Ring A] [Ring B]
variable [Algebra K A] [Algebra K B]

/-- **The trace radical transports along an algebra isomorphism.**

Only surjectivity and multiplicativity are used, so this holds for any
`τ : B → K` whatever — no trace axioms needed. -/
theorem traceRadical_comp_algEquiv (φ : A ≃ₐ[K] B) (τ : B → K) :
    traceRadical (τ ∘ φ) = φ ⁻¹' traceRadical τ := by
  ext a
  simp only [traceRadical, Set.mem_setOf_eq, Set.mem_preimage, Function.comp_apply]
  constructor
  · intro h b
    obtain ⟨c, rfl⟩ := φ.surjective b
    have hc := h c
    rwa [map_mul] at hc
  · intro h b
    rw [map_mul]
    exact h (φ b)

end Transport

/-! ## The packaged statement -/

section Packaged

variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {d : ι → Type*} [∀ i, Fintype (d i)] [∀ i, DecidableEq (d i)]
variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A]

/-- **The shape the Temperley–Lieb application needs.**

If `A` decomposes as a finite product of matrix algebras and `τ` is the weighted
block trace pulled back along that decomposition, then `τ` has **zero radical**
provided no weight vanishes.

Applied to `TL_n(δ)`: the two inputs are (i) the Wedderburn decomposition, still
open, and (ii) `y_λ ≠ 0`, which `QOU.QBeta.TemperleyLiebTower.yw_pos` already
supplies for `1 < q`. So this reduces the `⊇` half of
`⟨relators⟩ = traceRadical tr_M` to the decomposition alone. -/
theorem traceRadical_eq_zero_of_algEquiv_pi_matrix
    (φ : A ≃ₐ[K] ∀ i, Matrix (d i) (d i) K) {y : ι → K} (hy : ∀ i, y i ≠ 0) :
    traceRadical (weightedBlockTrace (d := d) y ∘ φ) = {(0 : A)} := by
  rw [traceRadical_comp_algEquiv φ, weightedBlockTrace_traceRadical_eq_zero hy]
  ext a
  simp only [Set.mem_preimage, Set.mem_singleton_iff]
  constructor
  · intro h
    have : φ a = φ 0 := by rw [h, map_zero]
    exact φ.injective this
  · rintro rfl
    exact map_zero φ

end Packaged

end QOU.MathlibExt.TraceRadicalNondegenerate
