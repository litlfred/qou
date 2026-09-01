/-
# From a solution of the linear system to the auxiliary polynomial

`RothAuxiliaryPolynomial` established that the index condition **is** a linear system, that the
system is underdetermined, and that its entries are small.  This file closes the loop on the
polynomial side: a coefficient vector solving the system **is** an auxiliary polynomial, with the
degree bound, the index bound and its coefficients read off.

The endpoint is `exists_ofBox_of_solution`.  Siegel's lemma supplies exactly the vector it wants
— non-zero, and annihilating every vanishing condition — so what remains between here and the
auxiliary polynomial is the call itself.

## Three things that had to be proved rather than assumed

* **`translate` is natural in the coefficient ring** (`map_translate`).  The polynomial is built
  over `𝓞 K` — the entries must be algebraic *integers* for Siegel — while `index` is read over
  `K`.  Without naturality those are unrelated statements; with it, `index_map` says the index
  does not notice.
* **Outside the box the translate has no coefficients** (`coeff_translate_eq_zero_of_notMem`).
  The system is indexed by the box, but `le_index_iff_coeff_eq_zero` quantifies over *all*
  multi-indices of low weight, and there are such indices outside the box.  They cost nothing
  only because translation preserves every `degreeOf` — `degreeOf_translate_eq`, which the arc
  proved long before it knew what for.
* **The sum runs over the box, not the support** (`coeff_translate_ofBox`).  `coeff_translate_eq_sum`
  sums over `P.support`, which is what a polynomial gives you; a matrix row needs a fixed index
  set.  Extending to the box is free because the extra coefficients are zero, but the two are not
  the same sum and Siegel only accepts the second.

⚠ Not Mathlib-only: imports `QOU/Mathlib/RothAuxiliaryPolynomial.lean`.  It deliberately does
**not** import `RothHouseBound`, so the construction stays usable without the number-field
dependency.
-/
import QOU.Mathlib.RothAuxiliaryPolynomial

namespace MvPolynomial

variable {σ R S : Type*} [CommRing R] [CommRing S]


/-- **`translate` is natural in the coefficient ring.** -/
theorem map_translate (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    map f (translate α P) = translate (fun j => f (α j)) (map f P) := by
  induction P using MvPolynomial.induction_on with
  | C a => simp [translate]
  | add p q hp hq =>
      have e1 : translate α (p + q) = translate α p + translate α q := by
        rw [translate, map_add, ← translate, ← translate]
      have e2 : translate (fun j => f (α j)) (map f (p + q))
          = translate (fun j => f (α j)) (map f p)
            + translate (fun j => f (α j)) (map f q) := by
        rw [map_add, translate, map_add, ← translate, ← translate]
      rw [e1, map_add, hp, hq, e2]
  | mul_X p j hp =>
      have h1 : translate α (p * X j) = translate α p * (X j + C (α j)) := by
        rw [translate, map_mul, aeval_X, ← translate]
      have h2 : translate (fun j => f (α j)) (map f (p * X j))
          = translate (fun j => f (α j)) (map f p) * (X j + C (f (α j))) := by
        rw [map_mul, map_X, translate, map_mul, aeval_X, ← translate]
      rw [h1, h2, map_mul, hp, map_add, map_X, map_C]

/-- **…hence so is the translate matrix.** -/
theorem translateMatrix_map (f : R →+* S) (α : σ → R) (i n : σ →₀ ℕ) :
    f (translateMatrix α i n) = translateMatrix (fun j => f (α j)) i n := by
  rw [translateMatrix, translateMatrix, ← coeff_map, map_translate]
  congr 1
  rw [map_monomial, map_one]

open Finset in
/-- **The polynomial carrying a prescribed coefficient vector on the box.**  This is what
Siegel's solution vector becomes. -/
noncomputable def ofBox {m : ℕ} (r : Fin m → ℕ) (c : (Fin m →₀ ℕ) → R) :
    MvPolynomial (Fin m) R :=
  ∑ n ∈ idxBoxF r, monomial n (c n)

theorem coeff_ofBox {m : ℕ} (r : Fin m → ℕ) (c : (Fin m →₀ ℕ) → R) (k : Fin m →₀ ℕ) :
    coeff k (ofBox r c) = if k ∈ idxBoxF r then c k else 0 := by
  classical
  rw [ofBox, coeff_sum]
  simp only [coeff_monomial]
  exact Finset.sum_ite_eq' (idxBoxF r) k c

theorem degreeOf_ofBox_le {m : ℕ} (r : Fin m → ℕ) (c : (Fin m →₀ ℕ) → R) (h : Fin m) :
    degreeOf h (ofBox r c) ≤ r h := by
  classical
  rw [degreeOf_le_iff]
  intro k hk
  have hne : coeff k (ofBox r c) ≠ 0 := mem_support_iff.mp hk
  rw [coeff_ofBox] at hne
  split_ifs at hne with hmem
  · exact (mem_idxBoxF r k).mp hmem h
  · exact absurd rfl hne

/-- **Outside the box the translate has no coefficients**, because translation preserves every
`degreeOf`.  This is what lets the linear system be indexed by the box alone. -/
theorem coeff_translate_eq_zero_of_notMem {m : ℕ} (r : Fin m → ℕ) (c : (Fin m →₀ ℕ) → R)
    (α : Fin m → R) {i : Fin m →₀ ℕ} (hi : i ∉ idxBoxF r) :
    coeff i (translate α (ofBox r c)) = 0 := by
  classical
  obtain ⟨h, hh⟩ : ∃ h, r h < i h := by
    by_contra hc
    push_neg at hc
    exact hi ((mem_idxBoxF r i).mpr hc)
  by_contra hne
  have hmem : i ∈ (translate α (ofBox r c)).support := mem_support_iff.mpr hne
  have hle : degreeOf h (translate α (ofBox r c)) ≤ r h := by
    rw [degreeOf_translate_eq]; exact degreeOf_ofBox_le r c h
  have := (degreeOf_le_iff.mp hle) i hmem
  omega

theorem support_ofBox_subset {m : ℕ} (r : Fin m → ℕ) (c : (Fin m →₀ ℕ) → R) :
    (ofBox r c).support ⊆ idxBoxF r := by
  classical
  intro n hn
  have hne : coeff n (ofBox r c) ≠ 0 := mem_support_iff.mp hn
  rw [coeff_ofBox] at hne
  split_ifs at hne with hmem
  · exact hmem
  · exact absurd rfl hne

/-- **The translate coefficients are the linear system.**  Each is `∑_n c_n · translateMatrix`,
summed over the whole box — the row of the matrix Siegel is handed. -/
theorem coeff_translate_ofBox {m : ℕ} (r : Fin m → ℕ) (c : (Fin m →₀ ℕ) → R)
    (α : Fin m → R) (i : Fin m →₀ ℕ) :
    coeff i (translate α (ofBox r c))
      = ∑ n ∈ idxBoxF r, c n * translateMatrix α i n := by
  classical
  rw [coeff_translate_eq_sum,
    Finset.sum_subset (support_ofBox_subset r c) (fun n _ hns => by
      rw [notMem_support_iff.mp hns, zero_mul])]
  exact Finset.sum_congr rfl fun n hn => by rw [coeff_ofBox, if_pos hn]

/-- **Solving the system forces the index.**  The conditions need only be imposed on the box:
outside it the translate has no coefficients at all. -/
theorem le_index_ofBox {m : ℕ} (r : Fin m → ℕ) (c : (Fin m →₀ ℕ) → R) (α : Fin m → R) (μ : ℚ)
    (h : ∀ i ∈ idxBoxF r, idxWeight r i < μ →
      ∑ n ∈ idxBoxF r, c n * translateMatrix α i n = 0) :
    ((μ : ℚ) : WithTop ℚ) ≤ index r α (ofBox r c) := by
  classical
  rw [le_index_iff_coeff_eq_zero]
  intro i hi
  by_cases hmem : i ∈ idxBoxF r
  · rw [coeff_translate_ofBox]; exact h i hmem hi
  · exact coeff_translate_eq_zero_of_notMem r c α hmem

/-- **The index is insensitive to an injective change of coefficient ring.**  Needed because the
auxiliary polynomial is built over `𝓞 K` while `index` is read over `K`. -/
theorem index_map [DecidableEq σ] (f : R →+* S) (hf : Function.Injective f) (d : σ → ℕ)
    (α : σ → R) (P : MvPolynomial σ R) :
    index d (fun j => f (α j)) (map f P) = index d α P := by
  rw [index, index, ← map_translate, support_map_of_injective _ hf]

/-- **A solution of the system is an auxiliary polynomial.**

Everything the construction has to deliver, from a coefficient vector that (a) is not identically
zero on the box and (b) kills every vanishing condition of weight below `μ`.  Siegel's lemma
supplies exactly such a vector; this theorem is what turns it into a polynomial. -/
theorem exists_ofBox_of_solution {m : ℕ} (r : Fin m → ℕ)
    (α : Fin m → R) (μ : ℚ) (c : (Fin m →₀ ℕ) → R)
    (hc : ∃ n ∈ idxBoxF r, c n ≠ 0)
    (heq : ∀ i ∈ idxBoxF r, idxWeight r i < μ →
      ∑ n ∈ idxBoxF r, c n * translateMatrix α i n = 0) :
    ∃ P : MvPolynomial (Fin m) R, P ≠ 0 ∧ (∀ h, degreeOf h P ≤ r h) ∧
      ((μ : ℚ) : WithTop ℚ) ≤ index r α P ∧
      ∀ n, coeff n P = if n ∈ idxBoxF r then c n else 0 := by
  classical
  obtain ⟨n₀, hn₀box, hn₀⟩ := hc
  refine ⟨ofBox r c, ?_, degreeOf_ofBox_le r c, le_index_ofBox r c α μ heq, ?_⟩
  · intro hz
    apply hn₀
    have hcz : coeff n₀ (ofBox r c) = c n₀ := by rw [coeff_ofBox, if_pos hn₀box]
    rw [hz, coeff_zero] at hcz
    exact hcz.symm
  · intro n
    rw [coeff_ofBox]

end MvPolynomial
