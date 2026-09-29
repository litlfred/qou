/-
# The auxiliary polynomial

`exists_auxiliary_polynomial` — the construction Roth's theorem opens with, complete:

> Given degrees `r`, algebraic integers `α`, and `ε` with `0 < ε ≤ ½` and `m > 1/(4ε²)`, there is
> a non-zero `P ∈ 𝓞 K[x₁,…,x_m]` with `degreeOf h P ≤ r h`, index at least `m(½ − ε)` at
> `(α₁,…,α_m)`, and every coefficient of house at most Siegel's bound.

Everything it consumes was built over the previous parts: the system
(`le_index_iff_coeff_eq_zero`, `coeff_translate_eq_sum`), its size (`fintypeCard_idxWeight_lt`),
the entry bound (`house_translateMatrix_le`), and the packaging
(`exists_ofBox_of_solution`).  The engine is
`NumberField.house.exists_ne_zero_int_vec_house_le`.

## Two things worth knowing before reading it

**`ε ≤ ½` is not decoration.**  Siegel needs `0 < p` — at least one equation — and the equation
set is `{i ∈ box : idxWeight r i ≤ m(½ − ε)}`.  The zero multi-index has weight `0`, so it is an
equation exactly when `m(½ − ε) ≥ 0`, i.e. `ε ≤ ½`.  ⚠ This is **not** implied by the counting
hypothesis `1 < 4ε²m`, which `ε = 10, m = 1` satisfies while making the threshold negative and
the equation set empty.  It is free in Roth's regime — there `ε` is small — but it had to be
found and stated rather than assumed.

**Siegel's height bound is stated with a `private` constant.**  `c₁` in
`Mathlib/NumberTheory/NumberField/House.lean` is `private def`, so the bound in
`exists_ne_zero_int_vec_house_le`'s conclusion cannot be named by a downstream statement in the
ordinary way.  `open private c₁ from …` reaches it, and `auxHeightBound` below is that
expression given a name.  Without it the height clause would have had to be dropped or weakened
to a contentless `∃ C`.

⚠ Not Mathlib-only, and **not in the default closure**: imports
`Mathlib.NumberTheory.NumberField.House`, which a fresh container must build first
(`lake build Mathlib.NumberTheory.NumberField.House`, ~4 min, 40 modules).
-/
import QOU.Mathlib.RothAuxiliaryConstruction
import Mathlib.NumberTheory.NumberField.House

namespace MvPolynomial
open NumberField Finset

open private c₁ from Mathlib.NumberTheory.NumberField.House in
/-- Siegel's height bound, named so the statement below can mention it. -/
noncomputable def auxHeightBound (K : Type*) [Field K] [NumberField K]
    [DecidableEq (K →+* ℂ)] (p q : ℕ) (A : ℝ) : ℝ :=
  c₁ K * ((c₁ K * q * A) ^ ((p : ℝ) / (q - p)))

variable {K : Type*} [Field K] [NumberField K] [DecidableEq (K →+* ℂ)]

theorem translateMatrix_zero_zero {R : Type*} [CommRing R] {σ : Type*} [DecidableEq σ]
    (α : σ → R) :
    translateMatrix α 0 0 = 1 := by
  rw [translateMatrix, monomial_zero', map_one, translate, map_one, coeff_one, if_pos rfl]

theorem exists_auxiliary_polynomial {m : ℕ} (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    (α : Fin m → 𝓞 K) {ε : ℚ} (hε : 0 < ε) (hε2 : ε ≤ 1 / 2)
    (hm : 1 < 4 * ε ^ 2 * (m : ℚ)) {A : ℝ}
    (hA : ∀ i n : Fin m →₀ ℕ,
      house ((algebraMap (𝓞 K) K) (translateMatrix α i n)) ≤ A) :
    ∃ P : MvPolynomial (Fin m) (𝓞 K), P ≠ 0 ∧ (∀ h, degreeOf h P ≤ r h) ∧
      ((((m : ℚ) / 2 - ε * (m : ℚ) : ℚ)) : WithTop ℚ)
        ≤ index r (fun h => ((algebraMap (𝓞 K) K) (α h)))
            (map (algebraMap (𝓞 K) K) P) ∧
      ∀ n, house ((algebraMap (𝓞 K) K) (coeff n P))
        ≤ auxHeightBound K
            (Fintype.card {i // i ∈ (idxBoxF r).filter
              (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ))})
            (Fintype.card {n // n ∈ idxBoxF r}) A := by
  classical
  set μ : ℚ := (m : ℚ) / 2 - ε * (m : ℚ) with hμ
  set Efin : Finset (Fin m →₀ ℕ) := (idxBoxF r).filter (fun i => idxWeight r i ≤ μ) with hE
  have hmQ : (0 : ℚ) < (m : ℚ) := by nlinarith [sq_nonneg ε]
  have hμ0 : (0 : ℚ) ≤ μ := by rw [hμ]; nlinarith
  have hzerobox : (0 : Fin m →₀ ℕ) ∈ idxBoxF r := (mem_idxBoxF r 0).mpr (fun h => Nat.zero_le _)
  have hzeroE : (0 : Fin m →₀ ℕ) ∈ Efin := by
    rw [hE, Finset.mem_filter]
    exact ⟨hzerobox, by simpa [idxWeight] using hμ0⟩
  have h0p : 0 < Fintype.card {i // i ∈ Efin} := Fintype.card_pos_iff.mpr ⟨⟨0, hzeroE⟩⟩
  have hpq : Fintype.card {i // i ∈ Efin} < Fintype.card {n // n ∈ idxBoxF r} :=
    fintypeCard_idxWeight_lt r hr hε hm
  -- the matrix
  set a : Matrix {i // i ∈ Efin} {n // n ∈ idxBoxF r} (𝓞 K) :=
    Matrix.of (fun i n => translateMatrix α i.1 n.1) with ha_def
  have ha : a ≠ 0 := by
    intro hz
    have h1 : a ⟨0, hzeroE⟩ ⟨0, hzerobox⟩ = 0 := by rw [hz]; rfl
    rw [ha_def] at h1
    simp only [Matrix.of_apply] at h1
    rw [translateMatrix_zero_zero] at h1
    exact one_ne_zero h1
  have habs : ∀ k l, house ((algebraMap (𝓞 K) K) (a k l)) ≤ A := fun k l => hA _ _
  obtain ⟨ξ, hξ0, hξeq, hξb⟩ :=
    NumberField.house.exists_ne_zero_int_vec_house_le (K := K) a ha h0p hpq rfl habs rfl
  -- the coefficient vector
  set c : (Fin m →₀ ℕ) → 𝓞 K := fun n => if h : n ∈ idxBoxF r then ξ ⟨n, h⟩ else 0 with hc_def
  have hcne : ∃ n ∈ idxBoxF r, c n ≠ 0 := by
    obtain ⟨n₀, hn₀⟩ := Function.ne_iff.mp hξ0
    refine ⟨n₀.1, n₀.2, ?_⟩
    rw [hc_def]
    simpa using hn₀
  have heq : ∀ i ∈ idxBoxF r, idxWeight r i < μ →
      ∑ n ∈ idxBoxF r, c n * translateMatrix α i n = 0 := by
    intro i hibox hilt
    have hiE : i ∈ Efin := by rw [hE, Finset.mem_filter]; exact ⟨hibox, le_of_lt hilt⟩
    have h0 : ∑ n : {n // n ∈ idxBoxF r}, a ⟨i, hiE⟩ n * ξ n = 0 := by
      have := congrFun hξeq ⟨i, hiE⟩
      simpa [Matrix.mulVec, dotProduct] using this
    have hpt : ∀ n : {n // n ∈ idxBoxF r},
        c n.1 * translateMatrix α i n.1 = a ⟨i, hiE⟩ n * ξ n := by
      intro n
      rw [hc_def, ha_def]
      simp only [dif_pos n.2, Matrix.of_apply]
      ring
    rw [← Finset.sum_coe_sort (idxBoxF r) (fun n => c n * translateMatrix α i n),
      Finset.sum_congr rfl (fun n _ => hpt n)]
    exact h0
  obtain ⟨P, hP0, hPdeg, hPidx, hPcoeff⟩ := exists_ofBox_of_solution r α μ c hcne heq
  have hbound0 : (0 : ℝ) ≤ auxHeightBound K
      (Fintype.card {i // i ∈ Efin}) (Fintype.card {n // n ∈ idxBoxF r}) A :=
    le_trans (house_nonneg _) (hξb ⟨0, hzerobox⟩)
  refine ⟨P, hP0, hPdeg, ?_, ?_⟩
  · rw [index_map (algebraMap (𝓞 K) K) RingOfIntegers.coe_injective]
    exact hPidx
  · intro n
    rw [hPcoeff n]
    split_ifs with hn
    · rw [hc_def]
      simp only [dif_pos hn]
      exact hξb ⟨n, hn⟩
    · rw [map_zero]
      simpa [house] using hbound0

end MvPolynomial
