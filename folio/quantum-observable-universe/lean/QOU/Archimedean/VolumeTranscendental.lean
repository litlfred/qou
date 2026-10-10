import QOU.Archimedean.HyperbolicVolumeTranscendence
import Mathlib.RingTheory.Algebraic.Defs
import Mathlib.RingTheory.Algebraic.Basic

/-!
# `Vol(4₁)` is transcendental — the corollary `HyperbolicVolumeIndependence` already implies

`QOU/Archimedean/HyperbolicVolumeTranscendence.lean` carries three conjecture
classes and draws one implication between them:

    HyperbolicVolumeIndependence  →  SingleVolumeIrrational        (`implies_single_irrational`)
    HyperbolicVolumeIndependence  →  BorelZagierQOU                (`implies_borel_zagier`)

Both land in the *rational* register — `Vol ∉ ℚ`, and no vanishing ℚ-*linear*
combination. **Neither is the statement downstream consumers actually need**,
and the stronger one is already in the class: `no_relation` quantifies over
arbitrary finitely-supported `f : ℕ × ℕ × ℕ → ℚ`, so restricting to the
`(i, 0, 0)` slice says exactly that **no nonzero rational polynomial annihilates
`Vol(4₁)`** — transcendence, not merely irrationality.

The file's own module docstring lists the chain as
*"irrationality ⟸ ℚ-linear independence ⟸ algebraic independence"* and stops
there. The middle rung — transcendence — was never drawn, and `Transcendental`
appears nowhere in it.

## Why the distinction is load-bearing here

`computations/qbeta/qbeta_n_question_arithmetic_reduction_probe.py` reduces the
route-5 `N` question to a trichotomy on the arithmetic nature of `q₀`, closing
the rational branch (Niven) and the transcendental branch (`2cos(rπ)` is an
algebraic integer), and leaving **one** survivor: `q₀` algebraic irrational,
which by the pinning identity requires `Vol(4₁)` to be **algebraic**.

`SingleVolumeIrrational` does not touch that survivor — an irrational number may
be algebraic. `volTranscendental` below does: it is precisely the hypothesis that
kills the surviving branch, so conditional on `HyperbolicVolumeIndependence` the
Kashaev root-of-unity sublocus is **empty for every `N`**.

## 🛑 What this is NOT

This does **not** prove `Vol(4₁)` transcendental. `HyperbolicVolumeIndependence`
is a **conjecture class with no instance**, and this file adds none — it draws an
implication *between* an existing conjecture and a statement, in the §3b-cond
pattern. Every result here is conditional on `[HyperbolicVolumeIndependence]`,
and that binder is the dependency edge.

Bean `qou-82w7` records that "transcendental" is frequently an *interpretation*
of a near-singularity rather than a proved classification, and must not be used
to prune algebraic candidates. This file is compliant by construction: nothing
here asserts transcendence unconditionally, and the antecedent stays open.

Archimedean (ℝ): the volumes are real constants (§7c — genuinely archimedean).

-- Ref: [zagier1986] https://doi.org/10.1007/BFb0084581
-- Ref: [reid1991] https://doi.org/10.1112/blms/23.4.383
-/

namespace QOU.Archimedean

open Polynomial

/-- The slice map `i ↦ (i, 0, 0)` is injective. -/
theorem slice_injective : Function.Injective (fun i : ℕ => (i, (0 : ℕ), (0 : ℕ))) := by
  intro a b hab
  simpa using congrArg Prod.fst hab

/-- **`Vol(4₁)` is transcendental over ℚ**, conditional on algebraic independence.

    Restricting `HyperbolicVolumeIndependence.no_relation` to the `(i, 0, 0)`
    slice — where `vol_5_2 ^ 0 = vol_B3 ^ 0 = 1` — says that no nonzero rational
    polynomial annihilates `vol_4_1`, which is transcendence. -/
theorem volTranscendental [hvi : HyperbolicVolumeIndependence] :
    Transcendental ℚ vol_4_1 := by
  rw [transcendental_iff]
  intro p hp
  -- the slice carrying `p`'s coefficients
  set S : Finset (ℕ × ℕ × ℕ) :=
    (Finset.range (p.natDegree + 1)).image (fun i => (i, (0 : ℕ), (0 : ℕ))) with hS
  set f : ℕ × ℕ × ℕ → ℚ := fun ijk => if ijk ∈ S then p.coeff ijk.1 else 0 with hf
  have hsupp : ∀ ijk, ijk ∉ S → f ijk = 0 := by
    intro ijk h; simp [hf, h]
  have hsum :
      (S.sum fun ijk =>
        (f ijk : ℝ) * vol_4_1 ^ ijk.1 * vol_5_2 ^ ijk.2.1 * vol_B3 ^ ijk.2.2) = 0 := by
    rw [hS, Finset.sum_image (fun a _ b _ h => slice_injective h)]
    have : ∀ i ∈ Finset.range (p.natDegree + 1),
        ((f (i, 0, 0) : ℝ) * vol_4_1 ^ i * vol_5_2 ^ (0 : ℕ) * vol_B3 ^ (0 : ℕ))
          = (p.coeff i : ℝ) * vol_4_1 ^ i := by
      intro i hi
      have hmem : ((i, (0 : ℕ), (0 : ℕ)) : ℕ × ℕ × ℕ) ∈ S := by
        rw [hS]; exact Finset.mem_image_of_mem _ hi
      simp [hf, hmem]
    rw [Finset.sum_congr rfl this]
    have := Polynomial.aeval_eq_sum_range (R := ℚ) (S := ℝ) (p := p) vol_4_1
    rw [hp] at this
    simpa [Algebra.smul_def, Algebra.algebraMap_eq_smul_one] using this.symm
  have hzero := hvi.no_relation S f hsupp hsum
  -- every coefficient vanishes, so `p = 0`
  ext i
  by_cases hi : i ≤ p.natDegree
  · have hmem : ((i, (0 : ℕ), (0 : ℕ)) : ℕ × ℕ × ℕ) ∈ S := by
      rw [hS]; exact Finset.mem_image_of_mem _ (Finset.mem_range.mpr (Nat.lt_succ_of_le hi))
    have := hzero (i, 0, 0)
    simp [hf, hmem] at this
    simpa using this
  · push_neg at hi
    simp [Polynomial.coeff_eq_zero_of_natDegree_lt hi]

/-- **The transcendence rung sits strictly between the two the file already
    draws**: it implies irrationality of `vol_4_1`, and is not implied by it. -/
theorem volTranscendental_imp_irrational
    [HyperbolicVolumeIndependence] : Irrational vol_4_1 :=
  (implies_single_irrational).vol_4_1_irrational

end QOU.Archimedean
