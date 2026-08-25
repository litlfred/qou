import QOU.SchurWeyl.HeckeProductSurjective
import QOU.SchurWeyl.HeckeCoset
import QOU.Mathlib.SchenstedRSKBurnside

/-!
# QOU.SchurWeyl.HeckeWedderburnGeneral — the Wedderburn split of `H_{n+1}(q)`, for every `n`

SW-7 (`qou-0h5k`).  Counting turns the surjection of `HeckeProductSurjective` into an isomorphism:

    H_{n+1}(q)  ≃ₐ[ℝ]  ∏_{λ ⊢ n+1} M_{#SYT λ}(ℝ)

for every real `q` that is not a root of unity.

## The direction of the count is what makes this work

The `q = 1` file `BraidKnot.SpechtWedderburnGeneral` goes **injective + equal finrank**.  That route
is unavailable here: the corpus has `HeckeCoset.finrank_le_factorial` (`dim H ≤ (n+1)!`) but not the
matching lower bound, which is the open Gröbner–Shirshov item `qou-auq3` — and injectivity together
with `dim source ≤ dim target` gives nothing.

Running it through surjectivity inverts the dependency.  A surjection forces
`dim target ≤ dim source`; the corpus supplies `dim source ≤ (n+1)!`; and SW-3 — now available at
**every** `n` (`QOU.Mathlib.rskBurnsideHolds`) — makes `dim target = Σ_λ d_λ² = (n+1)!`.  The two
inequalities close, so the map is bijective **and**

    `finrank ℝ (H_{n+1}(q)) = (n+1)!`

falls out (`finrank_hecke_eq_factorial`) — the Iwahori–Hecke basis theorem's lower bound, obtained
without the Gröbner–Shirshov route rather than waiting on it.

LaTeX label: `thm:hecke-wedderburn-general`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

/-- The Hecke algebra is finite-dimensional: the coset family is a finite spanning set. -/
theorem finiteDimensional_hecke (q qi : ℝ) (n : ℕ) :
    FiniteDimensional ℝ (Hecke ℝ q qi n) := by
  classical
  rw [FiniteDimensional, Module.finite_def,
    ← HeckeCoset.span_cosetFam_eq_top (K := ℝ) (q := q) (qi := qi) n]
  exact Submodule.fg_span (Set.finite_range _)

/-- The block product has dimension `Σ_λ d_λ²`. -/
theorem finrank_blocks (n : ℕ) :
    Module.finrank ℝ (∀ lam : Partition (n + 1),
        Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
          (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) ℝ)
      = ∑ lam : Partition (n + 1), (dLambda lam) ^ 2 := by
  classical
  rw [Module.finrank_pi_fintype]
  refine Finset.sum_congr rfl (fun lam _ => ?_)
  rw [Module.finrank_matrix]
  simp [dLambda, sq]

/-- `Σ_λ d_λ² = (n+1)!` — SW-3, now unconditional at every `n`. -/
theorem sum_dLambda_sq (n : ℕ) :
    ∑ lam : Partition (n + 1), (dLambda lam) ^ 2 = (n + 1).factorial :=
  (sum_dLambda_sq_eq_iff (n + 1)).mpr (QOU.Mathlib.rskBurnsideHolds (n + 1))

/-- The block product has dimension `(n+1)!`. -/
theorem finrank_blocks_eq_factorial (n : ℕ) :
    Module.finrank ℝ (∀ lam : Partition (n + 1),
        Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
          (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) ℝ)
      = (n + 1).factorial := by
  rw [finrank_blocks, sum_dLambda_sq]

/-- **`dim H_{n+1}(q) = (n+1)!`** — the Iwahori–Hecke basis theorem, both bounds.

The upper bound is `HeckeCoset.finrank_le_factorial`.  The lower bound is *not* proved by hand here:
it is forced by the surjection onto a space of dimension `(n+1)!`.  So the Gröbner–Shirshov route
(`qou-auq3`) is not on the critical path for this statement. -/
theorem finrank_hecke_eq_factorial (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    Module.finrank ℝ (Hecke ℝ q q⁻¹ n) = (n + 1).factorial := by
  classical
  haveI := finiteDimensional_hecke q q⁻¹ n
  have hsurj := heckeProduct_surjective q hq0 hq2 n
  have hle : Module.finrank ℝ (Hecke ℝ q q⁻¹ n) ≤ (n + 1).factorial := by
    have h := HeckeCoset.finrank_le_factorial (K := ℝ) (q := q) (qi := q⁻¹) n
    simpa using h
  have hge : (n + 1).factorial ≤ Module.finrank ℝ (Hecke ℝ q q⁻¹ n) := by
    have hrange : LinearMap.range (heckeProduct q hq0 hq2 n).toLinearMap = ⊤ :=
      LinearMap.range_eq_top.mpr hsurj
    have h1 := LinearMap.finrank_range_le (R := ℝ) (heckeProduct q hq0 hq2 n).toLinearMap
    rw [hrange] at h1
    rw [finrank_top] at h1
    rw [← finrank_blocks_eq_factorial n]
    exact h1
  omega

/-- **The Wedderburn split of `H_{n+1}(q)`, for every `n`.** -/
theorem heckeProduct_bijective (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    Function.Bijective (heckeProduct q hq0 hq2 n) := by
  classical
  haveI := finiteDimensional_hecke q q⁻¹ n
  refine ⟨?_, heckeProduct_surjective q hq0 hq2 n⟩
  have hdim : Module.finrank ℝ (Hecke ℝ q q⁻¹ n)
      = Module.finrank ℝ (∀ lam : Partition (n + 1),
          Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
            (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) ℝ) := by
    rw [finrank_hecke_eq_factorial q hq0 hq2 n, finrank_blocks_eq_factorial n]
  have hs : Function.Surjective (heckeProduct q hq0 hq2 n).toLinearMap :=
    heckeProduct_surjective q hq0 hq2 n
  exact (LinearMap.injective_iff_surjective_of_finrank_eq_finrank
    (f := (heckeProduct q hq0 hq2 n).toLinearMap) hdim).mpr hs

/-- The isomorphism itself. -/
noncomputable def heckeWedderburn (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    Hecke ℝ q q⁻¹ n ≃ₐ[ℝ] (∀ lam : Partition (n + 1),
      Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
        (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) ℝ) :=
  AlgEquiv.ofBijective (heckeProduct q hq0 hq2 n) (heckeProduct_bijective q hq0 hq2 n)

end QOU.SchurWeyl
