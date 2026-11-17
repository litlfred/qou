/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# Diagonal vs Off-Diagonal Stokes Entries, Cross-Knot Candidate Split, ι-Odd Functional Classification, and Non-LCI Behrend Parity Obstruction

Formalizes the structural algebraic and arithmetic theorems for:
- **Bean `qou-3ent`**: GGM `2012.00062v3` eq. (21) `S⁺_{σ₁,σ₁}(x; q) = Ind^rot(0, x; q)`
  covers ONLY the diagonal `(0,0)` matrix entry, whose `q⁰` constant term is `1`
  (series `1 - 8q - 9q² + ⋯`, eq. 61), whereas `A_ω = 3` sits in the off-diagonal
  `(0,1)` entry (`q`-tower `3, 9, 75, 642, 5580, 48558`, eqs. 60/62). Moreover, the
  meridian Laurent polynomial `s(x) = x⁻¹ + 1 + x` (`s(1) = 3`, unit-multiplicity
  states at meridian charges `e ∈ {-1, 0, +1}`, eq. 188) appears identically in `5₂`
  (eqs. 239/277/307, where `s(1) = 3` and `s(1) + 1 = 4`), proving `s(1) = 3` is not
  a `4₁`-unique invariant.
- **Bean `qou-l15q`**: The two competing structural candidates for `A_ω(4₁) = 3` —
  Candidate A (`|disc(trace field)|`: `|-3| = 3` for `4₁`, `|-23| = 23` for `5₂`) and
  Candidate B (`|middle Alexander coefficient|`: `|3| = 3` for `Δ_{4₁}(t) = -t + 3 - t⁻¹`,
  `|-3| = 3` for `Δ_{5₂}(t) = 2t - 3 + 2t⁻¹`) — coincide at `4₁` (`3 = 3`) and split
  by `20` at `5₂` (`23 ≠ 3`), while the rank-3 Stokes matrix of `5₂` carries `3`
  upper-triangular off-diagonal entries (`{4, 0, 0}` / `{0, 3, -3}`) and lower-triangular
  entries (`{-3, -9}` / `{-4}`) with `23` absent from all off-diagonal entries.
- **Bean `qou-q05m`**: Complete classification of integer linear functionals
  `L(a, b) = α·a + β·b` on the chirality-split DT pair `(dt⁺, dt⁻)` under the mirror
  involution `barSwap (a, b) = (b, a)`: `L` is ι-odd (`L(b, a) = -L(a, b)` for all
  `a, b`) if and only if `α + β = 0`, which strictly excludes every nonzero multiple
  of the ι-even sum `a + b` and restricts all linear ι-odd observables to integer
  multiples `α · (a - b)` (taking primitive value `4 - 3 = 1` on `5₂` and `0` on `4₁`).
- **Bean `qou-dt14`**: Strengthening of the Behrend parity obstruction
  (`DTBehrendParityObstruction`): if every stratum in a Behrend stratification `S`
  carries an **odd** Behrend multiplicity `nᵢ` (in particular, any locally complete
  intersection or union of smooth strata where `nᵢ = (-1)^{dimᵢ} ∈ {-1, +1}`), then
  `(nᵢ - 1) · χᵢ` is even on every stratum, so `dtCount S - chiEuTotal S` is even.
  For `4₁` (`chiEuTotal S = -2`, `dtCount S = 3`), the difference `3 - (-2) = 5` is
  odd, proving that any Behrend stratification supplying `DT = 3` over `χ_eu = -2`
  must contain at least one non-LCI stratum with an **even** Behrend weight `nᵢ`
  paired with an **odd** Euler characteristic `χᵢ`.
-/

import Init.Data.Int.Basic
import Init.Data.List.Basic
import Init.Omega

namespace QOU.QBeta.StokesDiagonalVsOffDiagonalAndCrossKnotSplit

/-! ## 1. Diagonal vs Off-Diagonal Stokes Entries (`qou-3ent`) -/

/-- Truncated `q`-series coefficients `[c₀, c₁, c₂]` of the diagonal Stokes entry
`S⁺_{σ₁,σ₁}(1; q) = 1 - 8q - 9q² + ⋯` for `4₁` (GGM `2012.00062v3` eq. 61),
which eq. (21) identifies with the rotated 3d index `Ind^rot(0, 1; q)`. -/
def s11_41_coeffs : List Int := [1, -8, -9]

/-- Truncated `q`-tower coefficients `[c₀, c₁, c₂, c₃, c₄, c₅]` of the off-diagonal
Stokes entry `S⁺_{σ₁,σ₂}(1; q) = 3 + 9q + 75q² + 642q³ + 5580q⁴ + 48558q⁵ + ⋯`
for `4₁` (GGM `2012.00062v3` eqs. 60, 62). -/
def s12_41_tower : List Int := [3, 9, 75, 642, 5580, 48558]

/-- A Laurent polynomial represented as a list of `(exponent, coefficient)` pairs. -/
abbrev LaurentPoly := List (Int × Int)

/-- Evaluate a Laurent polynomial at `x = 1` (sum of coefficients). -/
def evalAtOne : LaurentPoly → Int
  | [] => 0
  | (_, c) :: t => c + evalAtOne t

/-- The meridian Laurent polynomial `s(x) = x⁻¹ + 1 + x` appearing in the `q → 0`
off-diagonal entry of `S⁺(x; 0)` for `4₁` (GGM eq. 188) and in the `5₂` factorizations
(GGM eqs. 239, 277, 307), encoding unit-multiplicity states at meridian charges
`e ∈ {-1, 0, +1}`. -/
def meridianPolyS : LaurentPoly := [(-1, 1), (0, 1), (1, 1)]

/-- **Diagonal vs Off-Diagonal `q⁰` Separation (`qou-3ent`).**
The diagonal entry covered by GGM eq. (21) (`s11_41_coeffs.head?`) has `q⁰` constant
term `1`, whereas the off-diagonal entry (`s12_41_tower.head?`) has `q⁰` constant
term `3`, and `1 ≠ 3`. Thus eq. (21) does not license reading `A_ω = 3` as a
diagonal 3d-index `q⁰` coefficient. -/
theorem stokes_diagonal_vs_offdiagonal_qzero_separation :
    s11_41_coeffs.head? = some 1 ∧
    s12_41_tower.head? = some 3 ∧
    s11_41_coeffs.head? ≠ s12_41_tower.head? := by
  decide

/-- **Cross-Knot Meridian Polynomial Sharing (`qou-3ent`).**
The meridian polynomial `s(x) = x⁻¹ + 1 + x` has three unit-multiplicity meridian
charge terms (`e ∈ {-1, 0, +1}`), evaluates at `x = 1` to `s(1) = 3` (the `4₁`
eq. 60 and `5₂` eq. 97 Stokes constant), and satisfies `s(1) + 1 = 4` (the `5₂`
eq. 96 Stokes constant in GGM eq. 98). -/
theorem meridian_poly_s_evaluates_to_three_and_four :
    meridianPolyS.length = 3 ∧
    evalAtOne meridianPolyS = 3 ∧
    evalAtOne meridianPolyS + 1 = 4 := by
  decide

/-- **Off-Diagonal Tower Ratio Identity (`qou-3ent`).**
Every coefficient in the first six terms `[3, 9, 75, 642, 5580, 48558]` of the `4₁`
off-diagonal Stokes tower (GGM eq. 62) is an exact integer multiple of the leading
off-diagonal constant `3`, with normalized integer quotient sequence
`[1, 3, 25, 214, 1860, 16186]`. -/
theorem stokes_offdiagonal_tower_divisible_by_three :
    s12_41_tower.map (fun c => c / 3) = [1, 3, 25, 214, 1860, 16186] ∧
    s12_41_tower.all (fun c => c % 3 == 0) = true := by
  decide

/-! ## 2. Cross-Knot Candidate Split and Rank-3 Obstruction (`qou-l15q`) -/

/-- Invariant trace field discriminant `disc(K)` for `4₁` (`ℚ(√-3)`, disc `-3`)
and `5₂` (cubic field of `y³ - 2y² + 3y - 1`, disc `-23`). -/
def traceFieldDisc_41 : Int := -3
def traceFieldDisc_52 : Int := -23

/-- Candidate A (`|disc(trace field)|`) for `4₁` and `5₂`. -/
def candidateA_41 : Int := Int.natAbs traceFieldDisc_41
def candidateA_52 : Int := Int.natAbs traceFieldDisc_52

/-- Symmetrized Alexander polynomial coefficients `[c_{-1}, c_0, c_1]` for
`Δ_{4₁}(t) = -t⁻¹ + 3 - t` and `Δ_{5₂}(t) = 2t⁻¹ - 3 + 2t`. -/
def alexanderCoeffs_41 : Int × Int × Int := (-1, 3, -1)
def alexanderCoeffs_52 : Int × Int × Int := (2, -3, 2)

/-- Candidate B (`|middle coefficient c_0 of Δ_K(t)|`) for `4₁` and `5₂`. -/
def candidateB_41 : Int := Int.natAbs alexanderCoeffs_41.2.1
def candidateB_52 : Int := Int.natAbs alexanderCoeffs_52.2.1

/-- Non-diagonal entries of the `5₂` leading Stokes matrices `S⁺(0)` and `S⁻(0)`
(GGM eqs. 96, 97, 100a). -/
def fivetwo_offdiag_entries : List Int := [4, 0, -3, -9, 3, -4]

/-- **Candidate A vs Candidate B Degeneracy at `4₁` and Sharp Split at `5₂` (`qou-l15q`).**
At `4₁`, Candidate A (`|-3| = 3`) and Candidate B (`|3| = 3`) coincide, whereas at
`5₂` Candidate A (`|-23| = 23`) and Candidate B (`|-3| = 3`) differ by `20`, and
`23` does not appear among any of the off-diagonal entries of `S⁺(0)` or `S⁻(0)`
for `5₂`. -/
theorem candidate_a_vs_b_degeneracy_and_fivetwo_split :
    candidateA_41 = 3 ∧
    candidateB_41 = 3 ∧
    candidateA_41 = candidateB_41 ∧
    candidateA_52 = 23 ∧
    candidateB_52 = 3 ∧
    candidateA_52 - candidateB_52 = 20 ∧
    (candidateA_52 ∈ fivetwo_offdiag_entries ↔ False) := by
  decide

/-- Number of strictly upper-triangular entries `r * (r - 1) / 2` in a rank-`r`
unipotent Stokes matrix. -/
def stokesUpperTriangularCount (r : Nat) : Nat := r * (r - 1) / 2

/-- **Rank-2 vs Rank-3 Stokes Multiplicity (`qou-l15q`).**
A rank-2 Stokes matrix (`4₁`) has `2 * 1 / 2 = 1` upper-triangular off-diagonal
entry, whereas a rank-3 Stokes matrix (`5₂`) has `3 * 2 / 2 = 3` upper-triangular
off-diagonal entries (encoding `3` independent Borel singularities `ι_{i,j}` with
`i < j`). -/
theorem stokes_rank_two_vs_rank_three_entry_count :
    stokesUpperTriangularCount 2 = 1 ∧
    stokesUpperTriangularCount 3 = 3 ∧
    stokesUpperTriangularCount 3 - stokesUpperTriangularCount 2 = 2 := by
  decide

/-! ## 3. Classification of ι-Odd Linear Functionals on `(dt⁺, dt⁻)` (`qou-q05m`) -/

/-- General integer linear functional `L_{α,β}(a, b) = α·a + β·b` on the ordered
chirality pair `(a, b) = (dt⁺, dt⁻)`. -/
def linearFunctional (α β a b : Int) : Int := α * a + β * b

/-- **Characterization of ι-Odd Linear Functionals (`qou-q05m`).**
An integer linear functional `L_{α,β}(a, b) = α·a + β·b` is antisymmetric under the
chirality involution `(a, b) ↦ (b, a)` on the certified `5₂` pair `(4, 3)` if and
only if `α + β = 0` (i.e. `β = -α`, so `L_{α,β}(a, b) = α · (a - b)`). -/
theorem linear_functional_iota_odd_on_52_iff (α β : Int) :
    linearFunctional α β 3 4 = - linearFunctional α β 4 3 ↔ α + β = 0 := by
  unfold linearFunctional
  omega

/-- **Universal ι-Oddness for Difference Multiples (`qou-q05m`).**
Whenever `α + β = 0`, `L_{α,β}(b, a) = - L_{α,β}(a, b)` holds for all integer pairs
`(a, b)`, vanishes on every amphichiral pair `(a, a)`, and evaluates on the `5₂`
pair `(4, 3)` to `α`. -/
theorem linear_functional_iota_odd_properties (α β a b : Int) (hodd : α + β = 0) :
    linearFunctional α β b a = - linearFunctional α β a b ∧
    linearFunctional α β a a = 0 ∧
    linearFunctional α β 4 3 = α := by
  unfold linearFunctional
  have hβ : β = -α := by omega
  rw [hβ, Int.neg_mul, Int.neg_mul, Int.neg_mul]
  omega

/-- **Exclusion of Every Nonzero ι-Even Sum Multiple (`qou-q05m`).**
For any nonzero coefficient `c ≠ 0`, the symmetric linear combination
`L_{c,c}(a, b) = c·a + c·b` fails the ι-odd antisymmetry condition on `5₂`:
`L_{c,c}(3, 4) ≠ - L_{c,c}(4, 3)`. -/
theorem iota_even_sum_multiple_never_iota_odd (c : Int) (hc : c ≠ 0) :
    linearFunctional c c 3 4 ≠ - linearFunctional c c 4 3 := by
  unfold linearFunctional
  omega

/-! ## 4. Non-LCI Behrend Weight Parity Obstruction (`qou-dt14`) -/

/-- A Behrend stratification represented as a list of `(behrendWeight, chiEuStratum)` pairs. -/
abbrev Strata := List (Int × Int)

/-- Unweighted Euler characteristic `χ_eu(M) = Σ_i χ_{eu,i}`. -/
def chiEuTotal : Strata → Int
  | [] => 0
  | p :: t => p.2 + chiEuTotal t

/-- Behrend-weighted Donaldson–Thomas count `DT(M) = Σ_i n_i · χ_{eu,i}`. -/
def dtCount : Strata → Int
  | [] => 0
  | p :: t => p.1 * p.2 + dtCount t

/-- **Two-Stratum Determinant Elimination Identity (`qou-dt14`).**
For any two-stratum Behrend decomposition `[(n₁, χ₁), (n₂, χ₂)]` with total Euler
characteristic `E = χ₁ + χ₂` and weighted DT count `D = n₁·χ₁ + n₂·χ₂`, eliminating
`χ₂` yields `(n₁ - n₂) · χ₁ = D - n₂ · E`. -/
theorem two_stratum_behrend_elimination (n₁ χ₁ n₂ χ₂ E D : Int)
    (hE : chiEuTotal [(n₁, χ₁), (n₂, χ₂)] = E)
    (hD : dtCount [(n₁, χ₁), (n₂, χ₂)] = D) :
    (n₁ - n₂) * χ₁ = D - n₂ * E := by
  simp only [chiEuTotal, dtCount] at hE hD
  have hχ₂ : χ₂ = E - χ₁ := by omega
  rw [hχ₂] at hD
  have hsub : n₂ * (E - χ₁) = n₂ * E - n₂ * χ₁ := Int.mul_sub n₂ E χ₁
  have hsub1 : (n₁ - n₂) * χ₁ = n₁ * χ₁ - n₂ * χ₁ := Int.sub_mul n₁ n₂ χ₁
  omega

/-- **Two-Stratum Opposite Weight Parity for `4₁` (`qou-dt14`).**
In any two-stratum Behrend decomposition supplying `D = 3` over `E = -2`, the eliminated
right-hand side `3 - n₂ * (-2) = 3 + 2 * n₂` is always odd, so `(n₁ - n₂) * χ₁` is odd;
in particular `n₁ ≠ n₂` and `(n₁ - n₂) % 2 ≠ 0` (one Behrend weight is even and the
other is odd). -/
theorem two_stratum_fourone_opposite_weight_parity (n₁ χ₁ n₂ χ₂ : Int)
    (hE : chiEuTotal [(n₁, χ₁), (n₂, χ₂)] = -2)
    (hD : dtCount [(n₁, χ₁), (n₂, χ₂)] = 3) :
    ((n₁ - n₂) * χ₁) % 2 ≠ 0 ∧ n₁ ≠ n₂ := by
  have helim := two_stratum_behrend_elimination n₁ χ₁ n₂ χ₂ (-2) 3 hE hD
  refine ⟨?_, ?_⟩
  · rw [helim]
    omega
  · intro heq
    rw [heq] at helim
    omega

/-- **All-Odd Behrend Weights Preserve Total Parity (`qou-dt14`).**
If every stratum `(nᵢ, χᵢ) ∈ S` has an odd Behrend weight `nᵢ` (`nᵢ % 2 ≠ 0` — which
includes every locally complete intersection / union of smooth strata where
`nᵢ = (-1)^{dimᵢ} ∈ {-1, 1}`), then `(nᵢ - 1) * χᵢ` is even on every stratum, so
`dtCount S - chiEuTotal S` is even. -/
theorem dtCount_sub_chiEuTotal_even_of_all_odd_weights (S : Strata)
    (hodd : ∀ p ∈ S, p.1 % 2 ≠ 0) :
    (dtCount S - chiEuTotal S) % 2 = 0 := by
  induction S with
  | nil => simp [dtCount, chiEuTotal]
  | cons a t ih =>
      have ha : a.1 % 2 ≠ 0 := hodd a (List.Mem.head _)
      have ht : (dtCount t - chiEuTotal t) % 2 = 0 :=
        ih (fun p hp => hodd p (List.Mem.tail _ hp))
      have hkm1 : ∃ k : Int, a.1 - 1 = 2 * k := ⟨(a.1 - 1) / 2, by omega⟩
      obtain ⟨k, hk⟩ := hkm1
      have hterm : a.1 * a.2 - a.2 = 2 * (k * a.2) := by
        calc
          a.1 * a.2 - a.2 = (a.1 - 1) * a.2 := by
            rw [Int.sub_mul, Int.one_mul]
          _ = (2 * k) * a.2 := by rw [hk]
          _ = 2 * (k * a.2) := Int.mul_assoc 2 k a.2
      simp only [dtCount, chiEuTotal]
      omega

/-- **No All-Odd-Weight (In Particular No `±1` / LCI) Stratification Yields `3` Over `-2` (`qou-dt14`).**
Because `3 - (-2) = 5` is odd, no Behrend stratification `S` with `chiEuTotal S = -2`
whose Behrend weights `nᵢ` are all odd (for instance `nᵢ ∈ {-1, 1}`) can achieve
`dtCount S = 3`. Consequently, any supplier of `A_ω(4₁) = 3` over `χ_eu = -2` must
contain at least one stratum with an **even** Behrend multiplicity `nᵢ` (a genuinely
non-LCI singularity). -/
theorem no_all_odd_behrend_weights_yield_three_over_neg_two (S : Strata)
    (hodd : ∀ p ∈ S, p.1 % 2 ≠ 0)
    (hE : chiEuTotal S = -2) :
    dtCount S ≠ 3 := by
  have heven := dtCount_sub_chiEuTotal_even_of_all_odd_weights S hodd
  intro hD
  rw [hE, hD] at heven
  omega

end QOU.QBeta.StokesDiagonalVsOffDiagonalAndCrossKnotSplit
