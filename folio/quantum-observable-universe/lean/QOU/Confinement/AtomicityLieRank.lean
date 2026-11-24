import Mathlib.Algebra.Lie.Rank
import Mathlib.Algebra.Lie.Classical
import Mathlib.Algebra.Lie.CartanExists
import Mathlib.Algebra.Lie.Abelian
import Mathlib.Tactic

/-!
# Atomicity — the Lie-algebra-rank route to the upper bound (`qou-atsd`, T3-lie)

The atomicity upper bound needs `rank G ≤ 1` for the Tannaka dual `G` — the piece
the elementary matrix route (`AtomicityFromSelfDuality.lean`) could not close,
because algebraic-**group** rank is not in Mathlib. But `rank G = rank Lie(G)`, and
Mathlib **does** have Lie-algebra rank (`LieAlgebra.rank`) together with the
specific-element upper bound

  `rank R L ≤ (ad R L x).charpoly.natTrailingDegree`   (`rank_le_natTrailingDegree_charpoly_ad`).

So the residual reframes to a **Mathlib-reachable** statement: for `Lie(SL₂) = 𝔰𝔩₂`
with the regular diagonal `h = diag(1,−1)`, `ad h` has characteristic polynomial
`X³ − 4X` (eigenvalues `0, 2, −2` on the basis `h, e, f`), whose trailing degree is
`1` — giving `rank 𝔰𝔩₂ ≤ 1`, the atomicity upper bound.

This file lands the **frame** (`rank_le_one_of_ad_charpoly_trailing`): the general
reduction from a trailing-degree-≤1 witness to `rank ≤ 1`. The concrete `𝔰𝔩₂`
charpoly computation `natTrailingDegree (charpoly (ad h)) = 1` — the genuine
remaining core — is bean `qou-atsd-t3-lie`.

-- Ref: [leitner2026] conj:binding-manybody-eq-jet-filtration (atomicity); def:tannaka-dual
-/

namespace QOU.Atomicity

open LieAlgebra

/-- **Lie-rank route to the atomicity upper bound (frame).** If a Lie algebra `L`
    over `R` carries an element `x` whose `ad`-characteristic polynomial has
    trailing degree `≤ 1`, then `rank R L ≤ 1`. Immediate from Mathlib's
    specific-element rank bound `rank_le_natTrailingDegree_charpoly_ad`.

    This is the closeable reframing of the atomicity residual: with `rank G =
    rank Lie(G)` it replaces the (Mathlib-absent) algebraic-group root count by a
    Lie-algebra charpoly computation. Applied to `𝔰𝔩₂` and the regular diagonal
    `h` (whose `ad h` charpoly is `X³ − 4X`, trailing degree 1) it yields
    `rank 𝔰𝔩₂ ≤ 1` — the atomicity upper bound. The concrete `𝔰𝔩₂` computation is
    the remaining core (bean `qou-atsd-t3-lie`); no instance is fabricated here. -/
theorem rank_le_one_of_ad_charpoly_trailing
    {R L : Type*} [CommRing R] [Nontrivial R] [LieRing L] [LieAlgebra R L]
    [Module.Finite R L] [Module.Free R L] (x : L)
    (hx : (ad R L x).charpoly.natTrailingDegree ≤ 1) :
    rank R L ≤ 1 :=
  (rank_le_natTrailingDegree_charpoly_ad R x).trans hx

/-! ## The 𝔰𝔩₂ triple and its `ad h` eigenstructure (T3-lie core, in progress)

The standard basis of `𝔰𝔩₂ = sl (Fin 2) R`: `e = E₀₁`, `f = E₁₀`, `h = diag(1,−1)`.
The bracket is the matrix commutator (`sl_bracket`). The Cartan element `h` acts by
`[h,e]=2e`, `[h,f]=−2f`, `[h,h]=0` — so on the basis `(h,e,f)`, `ad h` is
`diag(0,2,−2)`, charpoly `X³−4X`, trailing degree `1`. This section lands the
bracket relations; the basis + charpoly assembly is bean `qou-atsd-t3-lie`. -/

section SL2
open Matrix LieAlgebra.SpecialLinear

variable (R : Type*) [CommRing R]

/-- `e = E₀₁ ∈ 𝔰𝔩₂`. -/
noncomputable def sl2E : sl (Fin 2) R := single 0 1 (by decide) 1
/-- `f = E₁₀ ∈ 𝔰𝔩₂`. -/
noncomputable def sl2F : sl (Fin 2) R := single 1 0 (by decide) 1
/-- `h = diag(1,−1) ∈ 𝔰𝔩₂`. -/
noncomputable def sl2H : sl (Fin 2) R := singleSubSingle 0 1 1

/-- **`[h,e] = 2e`** — the raising eigenvalue. -/
theorem sl2_bracket_h_e : ⁅sl2H R, sl2E R⁆ = (2 : R) • sl2E R := by
  apply Subtype.ext
  rw [sl_bracket]
  simp only [sl2H, sl2E, val_singleSubSingle, val_single, SetLike.val_smul]
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [Matrix.single, Matrix.of_apply, Matrix.mul_apply]
  all_goals ring

/-- **`[h,f] = −2f`** — the lowering eigenvalue. -/
theorem sl2_bracket_h_f : ⁅sl2H R, sl2F R⁆ = (-2 : R) • sl2F R := by
  apply Subtype.ext
  rw [sl_bracket]
  simp only [sl2H, sl2F, val_singleSubSingle, val_single, SetLike.val_smul]
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [Matrix.single, Matrix.of_apply, Matrix.mul_apply]
  all_goals ring

/-- **`[h,h] = 0`** — the Cartan element is `ad`-fixed. -/
theorem sl2_bracket_h_h : ⁅sl2H R, sl2H R⁆ = (0 : sl (Fin 2) R) := by
  apply Subtype.ext
  rw [sl_bracket]
  simp [sl2H, val_singleSubSingle]

/-- **Trace-zero coordinates.** Every `x ∈ 𝔰𝔩₂` decomposes on the triple as
    `x = x₀₀·h + x₀₁·e + x₁₀·f` — the `(1,1)` entry is `−x₀₀` by tracelessness. This
    is the constructive spanning statement for the basis `(h,e,f)`. -/
theorem sl2_decomp (x : sl (Fin 2) R) :
    x = (x.val 0 0) • sl2H R + (x.val 0 1) • sl2E R + (x.val 1 0) • sl2F R := by
  have htr : x.val 0 0 + x.val 1 1 = 0 := by
    have h0 : Matrix.trace x.val = 0 := x.2
    rwa [Matrix.trace_fin_two] at h0
  apply Subtype.ext
  simp only [sl2H, sl2E, sl2F]
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [Matrix.single, Matrix.of_apply]
  linear_combination htr

/-- **Linear independence** of the 𝔰𝔩₂ triple `(h,e,f)` — read `g₀=g₁=g₂=0` off the
    `(0,0)/(0,1)/(1,0)` entries of a vanishing combination. With `sl2_decomp`
    (spanning) this makes `(h,e,f)` a basis of `𝔰𝔩₂`. -/
theorem sl2_linindep : LinearIndependent R ![sl2H R, sl2E R, sl2F R] := by
  rw [Fintype.linearIndependent_iff]
  intro g hg i
  rw [Fin.sum_univ_three] at hg
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.cons_val_two, Matrix.tail_cons] at hg
  have hv : ∀ a b, (g 0 • sl2H R + g 1 • sl2E R + g 2 • sl2F R).val a b = 0 := by
    intro a b; rw [hg]; simp
  have e00 := hv 0 0
  have e01 := hv 0 1
  have e10 := hv 1 0
  simp [sl2H, sl2E, sl2F, Matrix.single, Matrix.of_apply] at e00 e01 e10
  fin_cases i <;> assumption

/-- **The 𝔰𝔩₂ basis `(h,e,f)`** — from linear independence (`sl2_linindep`) and
    spanning (`sl2_decomp`). Gives `finrank R 𝔰𝔩₂ = 3`, `Module.Free`, and unblocks
    `charpoly (ad h)`. -/
noncomputable def sl2Basis : Module.Basis (Fin 3) R (sl (Fin 2) R) :=
  Module.Basis.mk (sl2_linindep R) <| by
    intro x _
    rw [sl2_decomp R x]
    refine Submodule.add_mem _ (Submodule.add_mem _ ?_ ?_) ?_
    · exact Submodule.smul_mem _ _ (Submodule.subset_span ⟨0, by simp⟩)
    · exact Submodule.smul_mem _ _ (Submodule.subset_span ⟨1, by simp⟩)
    · exact Submodule.smul_mem _ _ (Submodule.subset_span ⟨2, by simp⟩)

/-! ### `ad h` as an endomorphism — the eigenvector equations (`toMatrix` columns) -/

/-- `ad h (h) = 0`. -/
theorem sl2_ad_h_h : ad R (sl (Fin 2) R) (sl2H R) (sl2H R) = 0 := by
  rw [LieAlgebra.ad_apply]; exact sl2_bracket_h_h R

/-- `ad h (e) = 2e` — eigenvalue `2`. -/
theorem sl2_ad_h_e : ad R (sl (Fin 2) R) (sl2H R) (sl2E R) = (2 : R) • sl2E R := by
  rw [LieAlgebra.ad_apply]; exact sl2_bracket_h_e R

/-- `ad h (f) = −2f` — eigenvalue `−2`. -/
theorem sl2_ad_h_f : ad R (sl (Fin 2) R) (sl2H R) (sl2F R) = (-2 : R) • sl2F R := by
  rw [LieAlgebra.ad_apply]; exact sl2_bracket_h_f R

/-- **`ad h` is `diag(0,2,−2)` in the `(h,e,f)` basis.** Each basis vector is an
    eigenvector (`sl2_ad_h_*`), so the matrix is diagonal with the eigenvalues. -/
theorem sl2_toMatrix_ad_h :
    LinearMap.toMatrix (sl2Basis R) (sl2Basis R) (ad R (sl (Fin 2) R) (sl2H R))
      = Matrix.diagonal ![(0 : R), 2, -2] := by
  have hb : ∀ j, sl2Basis R j = ![sl2H R, sl2E R, sl2F R] j := fun j =>
    Module.Basis.mk_apply _ _ j
  have hb0 : sl2Basis R 0 = sl2H R := by rw [hb 0]; rfl
  have hb1 : sl2Basis R 1 = sl2E R := by rw [hb 1]; rfl
  have hb2 : sl2Basis R 2 = sl2F R := by rw [hb 2]; rfl
  have hh : (sl2Basis R).repr (sl2H R) = Finsupp.single 0 1 := by
    rw [← hb0]; exact Module.Basis.repr_self _ _
  have he : (sl2Basis R).repr (sl2E R) = Finsupp.single 1 1 := by
    rw [← hb1]; exact Module.Basis.repr_self _ _
  have hf : (sl2Basis R).repr (sl2F R) = Finsupp.single 2 1 := by
    rw [← hb2]; exact Module.Basis.repr_self _ _
  have rhe : (sl2Basis R).repr ⁅sl2H R, sl2E R⁆ = Finsupp.single 1 2 := by
    rw [sl2_bracket_h_e R, map_smul, he, Finsupp.smul_single, smul_eq_mul, mul_one]
  have rhf : (sl2Basis R).repr ⁅sl2H R, sl2F R⁆ = Finsupp.single 2 (-2) := by
    rw [sl2_bracket_h_f R, map_smul, hf, Finsupp.smul_single, smul_eq_mul, mul_one]
  ext i j
  fin_cases j <;> fin_cases i <;>
    simp [LinearMap.toMatrix_apply, hb0, hb1, hb2, LieAlgebra.ad_apply, rhe, rhf]

/-- **T3-lie CLOSED — `rank 𝔰𝔩₂ ≤ 1`** (over a field with `2 ≠ 0`, e.g. the
    characteristic-zero substrate). Chain: the frame
    (`rank ≤ natTrailingDegree (charpoly (ad h))`), basis-independence of `charpoly`
    (`charpoly_toMatrix`), the diagonal `toMatrix` (`sl2_toMatrix_ad_h`), and
    `charpoly (diagonal ![0,2,−2]) = ∏(X − C dᵢ) = X³ − 4X` whose trailing
    coefficient (degree 1) is `−4 ≠ 0`. This is the atomicity **upper bound** on the
    Lie side — the piece the elementary group route could not reach. -/
theorem sl2_rank_le_one {K : Type*} [Field K] (h2 : (2 : K) ≠ 0) :
    LieAlgebra.rank K (sl (Fin 2) K) ≤ 1 := by
  haveI : Module.Finite K (sl (Fin 2) K) := Module.Finite.of_basis (sl2Basis K)
  haveI : Module.Free K (sl (Fin 2) K) := Module.Free.of_basis (sl2Basis K)
  refine rank_le_one_of_ad_charpoly_trailing (sl2H K) ?_
  rw [← LinearMap.charpoly_toMatrix (ad K (sl (Fin 2) K) (sl2H K)) (sl2Basis K),
    sl2_toMatrix_ad_h, Matrix.charpoly_diagonal]
  have hpoly : (∏ i : Fin 3, (Polynomial.X - Polynomial.C ((![0, 2, -2] : Fin 3 → K) i)))
      = Polynomial.X ^ 3 - Polynomial.C 4 * Polynomial.X := by
    simp only [Fin.prod_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
      Matrix.cons_val_two, Matrix.tail_cons, map_zero, map_neg, map_ofNat, sub_zero,
      sub_neg_eq_add]
    ring
  rw [hpoly]
  refine Polynomial.natTrailingDegree_le_of_ne_zero ?_
  have h4 : (4 : K) ≠ 0 := by
    have h42 : (4 : K) = 2 * 2 := by norm_num
    rw [h42]; exact mul_ne_zero h2 h2
  have hc : (Polynomial.X ^ 3 - Polynomial.C (4 : K) * Polynomial.X).coeff 1 = -4 := by
    rw [Polynomial.coeff_sub, Polynomial.coeff_X_pow, Polynomial.coeff_C_mul,
      Polynomial.coeff_X_one, mul_one, if_neg (by decide : ¬ (1 = 3)), zero_sub]
  rw [hc, neg_ne_zero]
  exact h4

/-- The characteristic polynomial of `ad h` on `𝔰𝔩₂` is `X³ − 4X`
(eigenvalues `0, 2, −2` on the basis `(h, e, f)`). Factored out of `sl2_rank_le_one`
so the trailing-degree and Cartan-dimension results share it. -/
theorem sl2_charpoly_ad_h {K : Type*} [Field K] :
    (ad K (sl (Fin 2) K) (sl2H K)).charpoly
      = Polynomial.X ^ 3 - Polynomial.C 4 * Polynomial.X := by
  haveI : Module.Finite K (sl (Fin 2) K) := Module.Finite.of_basis (sl2Basis K)
  haveI : Module.Free K (sl (Fin 2) K) := Module.Free.of_basis (sl2Basis K)
  rw [← LinearMap.charpoly_toMatrix (ad K (sl (Fin 2) K) (sl2H K)) (sl2Basis K),
    sl2_toMatrix_ad_h, Matrix.charpoly_diagonal]
  simp only [Fin.prod_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.cons_val_two, Matrix.tail_cons, map_zero, map_neg, map_ofNat, sub_zero, sub_neg_eq_add]
  ring

/-- The trailing degree of `charpoly (ad h)` is exactly `1`: the constant coefficient
of `X³ − 4X` vanishes (0 is a root — `h` centralizes itself) while the degree-1
coefficient `−4 ≠ 0`. Needs `2 ≠ 0` so that `4 ≠ 0`. -/
theorem sl2_ntd_ad_h {K : Type*} [Field K] (h2 : (2 : K) ≠ 0) :
    (ad K (sl (Fin 2) K) (sl2H K)).charpoly.natTrailingDegree = 1 := by
  have h4 : (4 : K) ≠ 0 := by
    have h42 : (4 : K) = 2 * 2 := by norm_num
    rw [h42]; exact mul_ne_zero h2 h2
  rw [sl2_charpoly_ad_h]
  set p : Polynomial K := Polynomial.X ^ 3 - Polynomial.C (4 : K) * Polynomial.X with hp
  have hc1 : p.coeff 1 = -4 := by
    rw [hp, Polynomial.coeff_sub, Polynomial.coeff_X_pow, Polynomial.coeff_C_mul,
      Polynomial.coeff_X_one, mul_one, if_neg (by decide : ¬ (1 = 3)), zero_sub]
  have hc0 : p.coeff 0 = 0 := by
    rw [hp, Polynomial.coeff_sub, Polynomial.coeff_X_pow, Polynomial.coeff_C_mul,
      Polynomial.coeff_X_zero, if_neg (by decide : ¬ (0 = 3)), mul_zero, sub_zero]
  have hne : p ≠ 0 := by
    intro h
    have : (-4 : K) = 0 := by rw [← hc1, h, Polynomial.coeff_zero]
    exact h4 (neg_eq_zero.mp this)
  have hle : p.natTrailingDegree ≤ 1 :=
    Polynomial.natTrailingDegree_le_of_ne_zero (by rw [hc1]; exact neg_ne_zero.mpr h4)
  have hge : 1 ≤ p.natTrailingDegree := by
    rcases Nat.eq_zero_or_pos p.natTrailingDegree with h0 | hpos
    · exfalso
      have hcn := Polynomial.coeff_natTrailingDegree_ne_zero.mpr hne
      rw [h0] at hcn
      exact hcn hc0
    · exact hpos
  exact le_antisymm hle hge

/-- **Cartan dimension of `𝔰𝔩₂` is `1`.** The Engel subalgebra (generalized `0`-eigenspace
of `ad h`) at the regular diagonal `h` has `finrank = 1`, since
`finrank (engel h) = natTrailingDegree (charpoly (ad h)) = 1`
(`LieAlgebra.finrank_engel`). This is the reusable toral-dimension datum for `𝔰𝔩₂`. -/
theorem sl2_finrank_engel_h_eq_one {K : Type*} [Field K] (h2 : (2 : K) ≠ 0) :
    Module.finrank K (LieSubalgebra.engel K (sl2H K)) = 1 := by
  haveI : Module.Finite K (sl (Fin 2) K) := Module.Finite.of_basis (sl2Basis K)
  haveI : Module.Free K (sl (Fin 2) K) := Module.Free.of_basis (sl2Basis K)
  rw [LieAlgebra.finrank_engel, sl2_ntd_ad_h h2]

/-- **The rank of `𝔰𝔩₂` is exactly `1`.** Combines the upper bound `sl2_rank_le_one`
with the lower bound `1 ≤ rank`: over an infinite field a regular element `x` exists,
`rank = finrank (engel x)`, and that regular `x` is nonzero (were `x = 0`, `engel 0 = ⊤`
would force `rank = finrank 𝔰𝔩₂ = 3 > 1`), so `x ∈ engel x` makes `engel x` nontrivial,
giving `finrank ≥ 1`. -/
theorem sl2_rank_eq_one {K : Type*} [Field K] [Infinite K] (h2 : (2 : K) ≠ 0) :
    LieAlgebra.rank K (sl (Fin 2) K) = 1 := by
  haveI : Module.Finite K (sl (Fin 2) K) := Module.Finite.of_basis (sl2Basis K)
  haveI : Module.Free K (sl (Fin 2) K) := Module.Free.of_basis (sl2Basis K)
  refine le_antisymm (sl2_rank_le_one h2) ?_
  obtain ⟨x, hx⟩ := LieAlgebra.exists_isRegular K (sl (Fin 2) K)
  have hrank : LieAlgebra.rank K (sl (Fin 2) K)
      = Module.finrank K (LieSubalgebra.engel K x) :=
    ((LieAlgebra.isRegular_iff_finrank_engel_eq_rank K x).mp hx).symm
  have hx0 : x ≠ 0 := by
    rintro rfl
    rw [LieSubalgebra.engel_zero, (LieSubalgebra.topEquiv.toLinearEquiv).finrank_eq,
      Module.finrank_eq_card_basis (sl2Basis K)] at hrank
    have hle := sl2_rank_le_one h2
    simp only [Fintype.card_fin] at hrank
    omega
  rw [hrank]
  have hne : (⟨x, LieSubalgebra.self_mem_engel K x⟩ : LieSubalgebra.engel K x) ≠ 0 := by
    intro h
    exact hx0 (by simpa using congrArg Subtype.val h)
  haveI : Nontrivial (LieSubalgebra.engel K x) := nontrivial_of_ne _ 0 hne
  exact Module.finrank_pos_iff.mpr this

/-- **Tier-B keystone: the centralizer of a nonzero `X ∈ 𝔰𝔩₂` is at most 1-dimensional.**
`ker (ad X) ≤ K ∙ X` — a matrix commuting with a nonzero traceless `2×2` matrix is a scalar
multiple of it. In coordinates `⁅X, y⁆ = 0` is the vanishing of the cross product
`(X₀₀,X₀₁,X₁₀) × (y₀₀,y₀₁,y₁₀)`, forcing collinearity. Needs `2 ≠ 0`. -/
theorem sl2_ker_ad_le_span {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    (X : sl (Fin 2) K) (hX : X ≠ 0) :
    LinearMap.ker (ad K (sl (Fin 2) K) X) ≤ Submodule.span K {X} := by
  have hXtr : X.val 1 1 = - X.val 0 0 := by
    have h0 : Matrix.trace X.val = 0 := X.2
    rw [Matrix.trace_fin_two] at h0; linear_combination h0
  intro y hy
  rw [LinearMap.mem_ker, LieAlgebra.ad_apply] at hy
  have hytr : y.val 1 1 = - y.val 0 0 := by
    have h0 : Matrix.trace y.val = 0 := y.2
    rw [Matrix.trace_fin_two] at h0; linear_combination h0
  have hcomm : X.val * y.val - y.val * X.val = 0 := by
    have hb := congrArg Subtype.val hy
    rwa [sl_bracket, ZeroMemClass.coe_zero] at hb
  have e00 := congrFun (congrFun hcomm 0) 0
  have e01 := congrFun (congrFun hcomm 0) 1
  have e10 := congrFun (congrFun hcomm 1) 0
  simp only [Matrix.sub_apply, Matrix.mul_apply, Fin.sum_univ_two, Matrix.zero_apply,
    hXtr, hytr] at e00 e01 e10
  have k00 : X.val 0 1 * y.val 1 0 - X.val 1 0 * y.val 0 1 = 0 := by linear_combination e00
  have k01 : X.val 0 0 * y.val 0 1 - X.val 0 1 * y.val 0 0 = 0 := by
    have h2e : (2 : K) * (X.val 0 0 * y.val 0 1 - X.val 0 1 * y.val 0 0) = 0 := by
      linear_combination e01
    exact (mul_eq_zero.mp h2e).resolve_left h2
  have k10 : X.val 1 0 * y.val 0 0 - X.val 0 0 * y.val 1 0 = 0 := by
    have h2e : (2 : K) * (X.val 1 0 * y.val 0 0 - X.val 0 0 * y.val 1 0) = 0 := by
      linear_combination e10
    exact (mul_eq_zero.mp h2e).resolve_left h2
  rw [Submodule.mem_span_singleton]
  by_cases ha : X.val 0 0 = 0
  · by_cases hb : X.val 0 1 = 0
    · -- `X₀₀ = X₀₁ = 0`, so `X₁₀ ≠ 0` (else `X = 0`); scale by `y₁₀ / X₁₀`.
      have hc : X.val 1 0 ≠ 0 := by
        intro hc0
        apply hX
        apply Subtype.ext
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [ZeroMemClass.coe_zero, ha, hb, hc0, hXtr]
      have hy00 : y.val 0 0 = 0 := by
        have hh : X.val 1 0 * y.val 0 0 = 0 := by linear_combination k10 + y.val 1 0 * ha
        exact (mul_eq_zero.mp hh).resolve_left hc
      have hy01 : y.val 0 1 = 0 := by
        have hh : X.val 1 0 * y.val 0 1 = 0 := by linear_combination -k00 + y.val 1 0 * hb
        exact (mul_eq_zero.mp hh).resolve_left hc
      refine ⟨y.val 1 0 / X.val 1 0, ?_⟩
      apply Subtype.ext
      ext i j
      fin_cases i <;> fin_cases j
      · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero, ha, mul_zero]
        exact hy00.symm
      · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero, Fin.mk_one, hb, mul_zero]
        exact hy01.symm
      · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero, Fin.mk_one]
        field_simp
      · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_one, hXtr, hytr, ha,
          hy00, mul_zero, neg_zero]
    · -- `X₀₀ = 0`, `X₀₁ ≠ 0`; scale by `y₀₁ / X₀₁`.
      have hy00 : y.val 0 0 = 0 := by
        have hh : X.val 0 1 * y.val 0 0 = 0 := by linear_combination -k01 + y.val 0 1 * ha
        exact (mul_eq_zero.mp hh).resolve_left hb
      refine ⟨y.val 0 1 / X.val 0 1, ?_⟩
      apply Subtype.ext
      ext i j
      fin_cases i <;> fin_cases j
      · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero, ha, mul_zero]
        exact hy00.symm
      · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero, Fin.mk_one]
        field_simp
      · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero, Fin.mk_one]
        field_simp
        linear_combination -k00
      · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_one, hXtr, hytr, ha,
          hy00, mul_zero, neg_zero]
  · -- `X₀₀ ≠ 0`; scale by `y₀₀ / X₀₀`.
    refine ⟨y.val 0 0 / X.val 0 0, ?_⟩
    apply Subtype.ext
    ext i j
    fin_cases i <;> fin_cases j
    · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero]
      field_simp
    · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero, Fin.mk_one]
      field_simp
      linear_combination -k01
    · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_zero, Fin.mk_one]
      field_simp
      linear_combination k10
    · simp only [SetLike.val_smul, Matrix.smul_apply, smul_eq_mul, Fin.mk_one, hXtr, hytr]
      field_simp

/-- **Corollary: the centralizer of a nonzero `X ∈ 𝔰𝔩₂` has `finrank ≤ 1`.** Immediate from
`sl2_ker_ad_le_span` (`ker (ad X) ≤ K ∙ X`) and `finrank (K ∙ X) = 1`. -/
theorem sl2_centralizer_finrank_le_one {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    (X : sl (Fin 2) K) (hX : X ≠ 0) :
    Module.finrank K (LinearMap.ker (ad K (sl (Fin 2) K) X)) ≤ 1 := by
  haveI : Module.Finite K (sl (Fin 2) K) := Module.Finite.of_basis (sl2Basis K)
  calc Module.finrank K (LinearMap.ker (ad K (sl (Fin 2) K) X))
      ≤ Module.finrank K (Submodule.span K {X}) :=
        Submodule.finrank_mono (sl2_ker_ad_le_span h2 X hX)
    _ = 1 := finrank_span_singleton hX

/-- **Central-element reduction (the Tier-B bridge).** A subalgebra `A ⊆ 𝔰𝔩₂` containing a
nonzero element `X` that commutes with all of `A` has `finrank A ≤ 1` — because `A ⊆ ker (ad X)`,
whose finrank is `≤ 1` (`sl2_centralizer_finrank_le_one`). Both the abelian case (any nonzero
`X ∈ A`) and the nilpotent case (a nonzero central element, via
`non_trivial_center_of_isNilpotent`) feed this. -/
theorem sl2_finrank_le_one_of_central {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    (A : LieSubalgebra K (sl (Fin 2) K)) (X : sl (Fin 2) K) (hX : X ≠ 0)
    (hcentral : ∀ y ∈ A, ⁅X, y⁆ = (0 : sl (Fin 2) K)) :
    Module.finrank K A ≤ 1 := by
  haveI : Module.Finite K (sl (Fin 2) K) := Module.Finite.of_basis (sl2Basis K)
  have hsub : (A : Submodule K (sl (Fin 2) K)) ≤ LinearMap.ker (ad K (sl (Fin 2) K) X) := by
    intro y hy
    rw [LinearMap.mem_ker, LieAlgebra.ad_apply]
    exact hcentral y hy
  calc Module.finrank K A
      = Module.finrank K (A : Submodule K (sl (Fin 2) K)) := rfl
    _ ≤ Module.finrank K (LinearMap.ker (ad K (sl (Fin 2) K) X)) := Submodule.finrank_mono hsub
    _ ≤ 1 := sl2_centralizer_finrank_le_one h2 X hX

/-- **Abelian subalgebras of 𝔰𝔩₂ are `≤ 1`-dimensional.** Any nonzero element of an abelian
subalgebra commutes with the whole subalgebra, so `sl2_finrank_le_one_of_central` applies. (The
maximal abelian — Cartan/toral — subalgebras of 𝔰𝔩₂ are exactly the `1`-dimensional ones.) -/
theorem sl2_abelian_finrank_le_one {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    (A : LieSubalgebra K (sl (Fin 2) K)) [IsLieAbelian A] [Nontrivial A] :
    Module.finrank K A ≤ 1 := by
  obtain ⟨a, ha0⟩ := exists_ne (0 : A)
  have ha0' : a.val ≠ 0 := by simp only [ne_eq, ZeroMemClass.coe_eq_zero]; exact ha0
  refine sl2_finrank_le_one_of_central h2 A a.val ha0' ?_
  intro y hy
  have h0 := trivial_lie_zero A A a ⟨y, hy⟩
  have hc := congrArg Subtype.val h0
  rwa [LieSubalgebra.coe_bracket, ZeroMemClass.coe_zero] at hc

set_option maxHeartbeats 1600000 in
set_option synthInstance.maxHeartbeats 400000 in
/-- **Tier-B assembly: every subalgebra `𝔤 ⊆ 𝔰𝔩₂` has `rank 𝔤 ≤ 1`.** Over an infinite field a
Cartan subalgebra `H = engel_𝔤 x` exists (nilpotent), and `rank 𝔤 ≤ finrank H`
(`rank_le_finrank_engel`). If `H` is nontrivial its center is nonzero
(`non_trivial_center_of_isNilpotent`); a nonzero central `Z` commutes with all of `H`, so under the
inclusion `ι : H ↪ 𝔰𝔩₂` the whole image lies in `ker(ad (ι Z))`, whose finrank is `≤ 1`
(`sl2_centralizer_finrank_le_one`). Hence `finrank H ≤ 1`, so `rank 𝔤 ≤ 1`. This is the atomicity
upper bound `rank G ≤ 1` at the Lie level (`rank G = rank Lie(G)`), for a self-dual rank-2 `V`.
(The generous heartbeat limits absorb typeclass search over the nested `engel ⊆ 𝔤 ⊆ 𝔰𝔩₂` types.) -/
theorem sl2_subalgebra_rank_le_one {K : Type*} [Field K] [Infinite K] (h2 : (2 : K) ≠ 0)
    (𝔤 : LieSubalgebra K (sl (Fin 2) K)) :
    LieAlgebra.rank K 𝔤 ≤ 1 := by
  haveI : Module.Finite K (sl (Fin 2) K) := Module.Finite.of_basis (sl2Basis K)
  haveI : Module.Finite K 𝔤 := inferInstance
  haveI : Module.Free K 𝔤 := inferInstance
  obtain ⟨x, hcartan⟩ := LieAlgebra.exists_isCartanSubalgebra_engel (K := K) (L := 𝔤)
  haveI := hcartan
  refine le_trans (LieAlgebra.rank_le_finrank_engel K x) ?_
  set H := LieSubalgebra.engel K x with hHdef
  rcases subsingleton_or_nontrivial H with hs | hn
  · haveI := hs
    rw [Module.finrank_zero_of_subsingleton]; exact zero_le_one
  · haveI := hn
    haveI : Nontrivial (LieAlgebra.center K H) := LieAlgebra.non_trivial_center_of_isNilpotent
    obtain ⟨Z, hZ⟩ := exists_ne (0 : LieAlgebra.center K H)
    have hZc : ∀ w : H, ⁅(Z : H), w⁆ = 0 := by
      intro w
      have hmem : ∀ v : H, ⁅v, (Z : H)⁆ = 0 :=
        (LieModule.mem_maxTrivSubmodule K H H (Z : H)).mp Z.2
      rw [← lie_skew, hmem w, neg_zero]
    set ι : H →ₗ⁅K⁆ sl (Fin 2) K := (𝔤.incl).comp H.incl with hιdef
    have hιinj : Function.Injective ι := by
      have h1 : Function.Injective (⇑(𝔤.incl)) := by
        rw [LieSubalgebra.coe_incl]; exact Subtype.val_injective
      have h2 : Function.Injective (⇑(H.incl)) := by
        rw [LieSubalgebra.coe_incl]; exact Subtype.val_injective
      intro a b hab
      rw [hιdef] at hab
      simp only [LieHom.coe_comp, Function.comp_apply] at hab
      exact h2 (h1 hab)
    set X : sl (Fin 2) K := ι (Z : H) with hXdef
    have hX : X ≠ 0 := by
      rw [hXdef]; intro h
      exact hZ (Subtype.ext (hιinj (h.trans (LieHom.map_zero ι).symm)))
    have hrange : LinearMap.range ι.toLinearMap ≤ LinearMap.ker (ad K (sl (Fin 2) K) X) := by
      rintro _ ⟨w, rfl⟩
      rw [LinearMap.mem_ker, LieAlgebra.ad_apply, hXdef, LieHom.coe_toLinearMap,
        ← LieHom.map_lie, hZc w, LieHom.map_zero]
    calc Module.finrank K H
        = Module.finrank K (LinearMap.range ι.toLinearMap) :=
          (LinearMap.finrank_range_of_inj hιinj).symm
      _ ≤ Module.finrank K (LinearMap.ker (ad K (sl (Fin 2) K) X)) := Submodule.finrank_mono hrange
      _ ≤ 1 := sl2_centralizer_finrank_le_one h2 X hX

end SL2

end QOU.Atomicity
