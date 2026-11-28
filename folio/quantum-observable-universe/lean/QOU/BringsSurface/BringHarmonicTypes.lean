import QOU.BringsSurface.BringSymmetryQuotientGenus
import QOU.BringsSurface.BringRegularMap
import Mathlib.Tactic

/-!
# The harmonic types of Bring's surface, and why the list is exhaustive

Bean `qou-u81q` (owner pick "Also Maass harmonics", 2026-11-27). The owner asked for the
harmonics of Bring's surface `B` classified by `S₅` type, with the exhaustiveness proved in
Lean. Following the owner ruling that the χ = −6 chain starts from the finite Bring map
(`QOU/BringsSurface/BringMapChain.lean`), everything here is finite: characters of `S₅`, the
cells of the map, and integer matrices. **No eigenvalue appears.** The analytic reading
(Maass forms) is in `QOU/Transcendental/BringsSurface/BringMaassTypes.lean`.

## Results

1. **The seven types are all of them** (`column_orthogonality`, `sum_dim_sq`,
   `class_function_expansion`, `expansion_unique`). The seven characters of `S₅` satisfy the
   column relations as well as the row relations, so they are a basis of the class functions.
   Any finite-dimensional `S₅`-module (an eigenspace of any `S₅`-invariant operator on `B`) has
   a class function as character, and that class function is one and only one rational
   combination of the seven. There is no eighth type.

2. **Which quotient sees which type** (`fixedDim_table`, `fixedDim_frobenius`). For each of
   the 19 conjugacy classes of subgroups `H ≤ S₅` and each type `ρ`, the dimension
   `dim ρ^H` (the number of independent `ρ`-type harmonics that descend to the orbifold
   `B/H`). Each row satisfies `Σ_ρ dim ρ · dim ρ^H = [S₅ : H]` (functions on `S₅/H`).

3. **Seven quotients determine every type, over `ℤ`** (`quotient_matrix_det`,
   `quotient_matrix_inverse`). The `7 × 7` block for `H = S₃, S₃ × S₂, A₄, F₂₀, S₄, A₅, S₅`
   has determinant `−1`. If `d_H` counts the `H`-invariant harmonics of one eigenvalue (the
   multiplicity on the orbifold `B/H`), then the multiplicity `m_ρ` of each type is
   ```
   m_triv = d_S₅                      m_[4,1]   = d_S₄ − d_S₅
   m_sgn  = d_A₅ − d_S₅                m_[3,2]   = d_{S₃×S₂} − d_S₄
   m_[2,2,1] = d_F₂₀ − d_S₅            m_[3,1,1] = d_S₃ − d_{S₃×S₂} − d_S₄ + d_S₅
   m_[2,1,1,1] = d_A₄ − d_S₄ − d_A₅ + d_S₅
   ```
   Six of these quotients are spheres and `B/A₄` is a torus. The torus is needed:
   `std ⊗ sgn = [2,1,1,1]` has no fixed vector under any subgroup with a spherical quotient
   (`spheres_miss_2111`), because `dim [2,1,1,1]^H` is the genus of `B/H`.

4. **One genus-2 quotient sees every type** (`double_transposition_sees_all`,
   `C3_sees_all`). Every type has a fixed vector under `⟨(01)(23)⟩` and under `C₃`, so every
   harmonic of `B` is a sum of `S₅`-translates of lifts from the genus-2 quotient
   `B/⟨(01)(23)⟩` (or `B/C₃`). No single sphere or torus quotient does this
   (`no_genus_le_one_quotient_sees_all`).

   Also: the 19 rows are pairwise distinct (`fixedDim_rows_nodup`), so `S₅` has no Sunada
   pair (bears on `conj:bring-isospectrality-question`, item 1, previously a probe only).

5. **The harmonic 1-cochains of the Bring map are `2 × [2,1,1,1]`, with no analysis**
   (`hopf_trace_h1`). The cells of the map are the cosets of `⟨S⟩ ≅ C₄` (30 vertices),
   `⟨A⟩ ≅ C₂` (60 edges, the stabiliser reversing its edge) and `⟨S·A⟩ ≅ C₅` (24 faces). The
   Hopf trace formula `χ_{H⁰} − χ_{H¹} + χ_{H²} = χ_{C⁰} − χ_{C¹} + χ_{C²}` with
   `H⁰ = H² = triv` gives `χ_{H¹} = 2·[2,1,1,1]`. Since `H¹ = H⁰(K) ⊕ conj` and every `S₅`
   character is real, `H⁰(K) = [2,1,1,1]`, which is `h0K_character_forced` reached by a
   second route (cellular instead of Riemann–Hurwitz).

6. **The vertex functions of the map** (`vertex_functions_decomposition`) are
   `triv + [4,1] + [2,1,1,1] + [3,2] + 2·[2,2,1] + [3,1,1]`, matching the exact vertex
   Laplacian in `computations/probes/bring_discrete_harmonics_probe.py` (eigenvalues
   `0; 2; 4; 5; 6; 7` with types `triv; [3,2]+[3,1,1]; [2,2,1]; [4,1]; [2,2,1]; [2,1,1,1]`).
   The eigenvalues themselves are not proved here; the types are.

## Inputs, cited and not derived

* The character table `S5Char.chi*` (Fulton–Harris §2.3), as in
  `BraidKnotOctonion/S5CharactersOnBringDeformations.lean`. `charTable_orthonormal` and
  `column_orthogonality` check it; `std_is_fixed_points_minus_one` checks `[4,1]` against
  the permutations. **Since 2026-11-28 the whole table is derived** from the permutations in
  `QOU/BringsSurface/S5CharacterDerivation.lean` (`derived_eq_table_everywhere`,
  `derived_orthonormal`, `class_sizes_derived`), so it is no longer a cited input.
* Every finite-dimensional complex representation of a finite group is a sum of irreducibles
  and is determined by its character (Maschke; Mathlib has the orthogonality relations,
  `FDRep.char_orthonormal`). Number of irreducibles = number of classes = `7`.
* The subgroup list `subgroupClasses` (from the enumeration probe
  `computations/probes/bring_symmetry_quotient_genus_probe.py`).
* The Hopf trace formula for a finite cell complex, and Hodge `H¹ = H⁰(K) ⊕ conj`.

Everything is integer or rational arithmetic. No empirical value enters.

-- Ref: [fulton-harris1991] W. Fulton and J. Harris, *Representation Theory*, §2.3.
-- Ref: [edge1978] W. L. Edge, *Bring's curve*, J. London Math. Soc. (1978).
-/

namespace QOU.Brings.HarmonicTypes

open QOU.Brings.S5Char QOU.Brings.SymmetryQuotientGenus

/-! ## 1. The seven types are all of them -/

/-- The seven harmonic types, indexed `triv, sgn, [4,1], [2,1,1,1], [3,2], [2,2,1], [3,1,1]`. -/
def irr : Fin 7 → Fin 7 → ℤ := ![chiTriv, chiSign, chiStd, chi2111, chi32, chi221, chi311]

/-- Order of the centraliser of an element of each class, `120 / classSize`. -/
def centraliser : Fin 7 → ℤ := ![120, 12, 8, 6, 6, 4, 5]

theorem centraliser_mul_classSize : ∀ i, centraliser i * classSize i = 120 := by decide

/-- `Σ_ρ χ_ρ(i) χ_ρ(j)`. -/
def colSum (i j : Fin 7) : ℤ :=
  irr 0 i * irr 0 j + irr 1 i * irr 1 j + irr 2 i * irr 2 j + irr 3 i * irr 3 j +
    irr 4 i * irr 4 j + irr 5 i * irr 5 j + irr 6 i * irr 6 j

/-- **Column orthogonality.** `Σ_ρ χ_ρ(i) χ_ρ(j) = δ_ij · |C(g_i)|`. With the row relations
(`charTable_orthonormal`) this says the `7 × 7` table is invertible: the seven characters are
a basis of the class functions. -/
theorem column_orthogonality :
    ∀ i j : Fin 7, colSum i j = if i = j then centraliser i else 0 := by decide

/-- **`Σ dim² = |S₅|`.** The seven types exhaust the regular representation. -/
theorem sum_dim_sq : colSum 0 0 = 120 := by decide

/-- `[4,1]` is the permutation character on `{0,…,4}` minus one, checked on a representative of
each class (`1, (01), (01)(23), (012), (012)(34), (0123), (01234)`). -/
theorem std_is_fixed_points_minus_one :
    let reps : Fin 7 → Equiv.Perm (Fin 5) :=
      ![1, Equiv.swap 0 1, Equiv.swap 0 1 * Equiv.swap 2 3,
        Equiv.swap 0 1 * Equiv.swap 1 2, Equiv.swap 0 1 * Equiv.swap 1 2 * Equiv.swap 3 4,
        Equiv.swap 0 1 * Equiv.swap 1 2 * Equiv.swap 2 3,
        Equiv.swap 0 1 * Equiv.swap 1 2 * Equiv.swap 2 3 * Equiv.swap 3 4]
    ∀ i, ((Finset.univ.filter (fun x => reps i x = x)).card : ℤ) - 1 = chiStd i := by
  decide

/-- The class-weighted pairing of a rational class function with a type, `120 ⟨f, χ_ρ⟩`. -/
def pairQ (f : Fin 7 → ℚ) (r : Fin 7) : ℚ :=
  (classSize 0 : ℚ) * f 0 * irr r 0 + (classSize 1 : ℚ) * f 1 * irr r 1 +
    (classSize 2 : ℚ) * f 2 * irr r 2 + (classSize 3 : ℚ) * f 3 * irr r 3 +
    (classSize 4 : ℚ) * f 4 * irr r 4 + (classSize 5 : ℚ) * f 5 * irr r 5 +
    (classSize 6 : ℚ) * f 6 * irr r 6

/-- The combination `Σ_ρ a_ρ χ_ρ` at class `i`. -/
def combo (a : Fin 7 → ℚ) (i : Fin 7) : ℚ :=
  a 0 * irr 0 i + a 1 * irr 1 i + a 2 * irr 2 i + a 3 * irr 3 i + a 4 * irr 4 i +
    a 5 * irr 5 i + a 6 * irr 6 i

/-- **Exhaustiveness.** Every class function is the combination of the seven types with
coefficients `⟨f, χ_ρ⟩`: `f = Σ_ρ ⟨f, χ_ρ⟩ χ_ρ`. -/
theorem class_function_expansion (f : Fin 7 → ℚ) (i : Fin 7) :
    combo (fun r => pairQ f r / 120) i = f i := by
  fin_cases i <;>
    simp [combo, pairQ, irr, classSize, chiTriv, chiSign, chiStd, chi2111, chi32, chi221,
      chi311] <;> ring

/-- **Uniqueness.** The seven types are linearly independent: a combination that vanishes on
every class has all coefficients zero. -/
theorem expansion_unique (a : Fin 7 → ℚ) (h : ∀ i, combo a i = 0) : a = 0 := by
  have h0 := h 0; have h1 := h 1; have h2 := h 2; have h3 := h 3
  have h4 := h 4; have h5 := h 5; have h6 := h 6
  simp only [combo, irr, chiTriv, chiSign, chiStd, chi2111, chi32, chi221, chi311] at h0 h1 h2 h3 h4 h5 h6
  simp at h0 h1 h2 h3 h4 h5 h6
  funext r
  fin_cases r <;> simp <;> linarith

/-! ## 2. Which quotient sees which type -/

/-- `|H| · dim ρ^H = Σ_classes k_i χ_ρ(i)` for the class distribution `k` of `H`. -/
def fixedSum' (k : Fin 7 → ℤ) (r : Fin 7) : ℤ :=
  k 0 * irr r 0 + k 1 * irr r 1 + k 2 * irr r 2 + k 3 * irr r 3 + k 4 * irr r 4 +
    k 5 * irr r 5 + k 6 * irr r 6

/-- The row `(dim ρ^H)_ρ` for a subgroup class `(|H|, k)`. -/
def fixedRow (p : ℕ × (Fin 7 → ℤ)) : List ℤ :=
  (List.finRange 7).map (fun r => fixedSum' p.2 r / p.1)

/-- Every `|H| · dim ρ^H` is divisible by `|H|`. -/
theorem fixedSum_divisible :
    subgroupClasses.all
      (fun p => (List.finRange 7).all (fun r => decide ((p.1 : ℤ) ∣ fixedSum' p.2 r))) = true := by
  decide

/-- **The table `dim ρ^H`.** Rows: the 19 subgroup classes of `subgroupClasses`
(`1, ⟨(01)(23)⟩, ⟨(01)⟩, C₃, ⟨(01),(23)⟩, V₄, C₄, C₅, C₆, S₃, S₃ twisted, D₄, D₅, S₃ × S₂, A₄,
F₂₀, S₄, A₅, S₅`). Columns: `triv, sgn, [4,1], [2,1,1,1], [3,2], [2,2,1], [3,1,1]`. -/
theorem fixedDim_table :
    subgroupClasses.map fixedRow =
      [ [1, 1, 4, 4, 5, 5, 6],
        [1, 1, 2, 2, 3, 3, 2],
        [1, 0, 3, 1, 3, 2, 3],
        [1, 1, 2, 2, 1, 1, 2],
        [1, 0, 2, 0, 2, 1, 1],
        [1, 1, 1, 1, 2, 2, 0],
        [1, 0, 1, 1, 1, 2, 1],
        [1, 1, 0, 0, 1, 1, 2],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 2, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0] ] := by
  decide

/-- **Frobenius reciprocity, row by row.** `Σ_ρ dim ρ · dim ρ^H = [S₅ : H]`: the functions on
`S₅/H` are exhausted by the seven types. -/
theorem fixedDim_frobenius :
    subgroupClasses.all (fun p =>
      decide (((fixedRow p).zipWith (· * ·) [1, 1, 4, 4, 5, 5, 6]).sum * (p.1 : ℤ) = 120)) = true := by
  decide

/-- The `[2,1,1,1]` column is the genus of the quotient (`quotient_genus_table`). -/
theorem column_2111_is_genus :
    subgroupClasses.map (fun p => (fixedRow p).getD 3 0) =
      [4, 2, 1, 2, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0] := by
  decide

/-- **Spheres miss `std ⊗ sgn`.** Whenever `B/H` is a sphere, `[2,1,1,1]^H = 0`. -/
theorem spheres_miss_2111 :
    subgroupClasses.all (fun p =>
      decide (fixedSum p.2 = 0 → (fixedRow p).getD 3 0 = 0)) = true := by
  decide

/-- **No Sunada pair in `S₅`.** The 19 rows are pairwise distinct. Two subgroups that meet every
class in the same number of elements have the same row, so no two non-conjugate subgroups of
`S₅` are almost conjugate, and no two quotients `B/H₁`, `B/H₂` are Sunada-isospectral. -/
theorem fixedDim_rows_nodup : (subgroupClasses.map fixedRow).Nodup := by decide

/-- The same statement before the change of basis: the class distributions are pairwise distinct. -/
theorem class_distributions_nodup :
    (subgroupClasses.map (fun p => (List.finRange 7).map p.2)).Nodup := by decide

/-! ## 3. Seven quotients determine every type, over `ℤ` -/

/-- The rows of `S₃, S₃ × S₂, A₄, F₂₀, S₄, A₅, S₅`. -/
def quotientMatrix : Matrix (Fin 7) (Fin 7) ℤ :=
  !![1, 0, 2, 0, 1, 0, 1;
     1, 0, 1, 0, 1, 0, 0;
     1, 1, 1, 1, 0, 0, 0;
     1, 0, 0, 0, 0, 1, 0;
     1, 0, 1, 0, 0, 0, 0;
     1, 1, 0, 0, 0, 0, 0;
     1, 0, 0, 0, 0, 0, 0]

/-- The block is taken from the table (rows 9, 13, 14, 15, 16, 17, 18). -/
theorem quotientMatrix_rows :
    [9, 13, 14, 15, 16, 17, 18].map (fun n => (subgroupClasses.map fixedRow).getD n []) =
      (List.finRange 7).map (fun i => (List.finRange 7).map (fun j => quotientMatrix i j)) := by
  decide

/-- Its inverse, read off as the formulas `m_ρ = …` in the module docstring. Rows: types;
columns: `d_{S₃}, d_{S₃×S₂}, d_{A₄}, d_{F₂₀}, d_{S₄}, d_{A₅}, d_{S₅}`. -/
def recoveryMatrix : Matrix (Fin 7) (Fin 7) ℤ :=
  !![0, 0, 0, 0, 0, 0, 1;
     0, 0, 0, 0, 0, 1, -1;
     0, 0, 0, 0, 1, 0, -1;
     0, 0, 1, 0, -1, -1, 1;
     0, 1, 0, 0, -1, 0, 0;
     0, 0, 0, 1, 0, 0, -1;
     1, -1, 0, 0, -1, 0, 1]

/-- **Integral recovery.** `R · Q = 1`: the seven quotient multiplicities `d_H = Σ_ρ
dim ρ^H · m_ρ` (that is, `d = Q m`) determine every type multiplicity `m_ρ` by an integer
formula, `m = R d`. -/
theorem quotient_matrix_inverse : recoveryMatrix * quotientMatrix = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [recoveryMatrix, quotientMatrix, Matrix.mul_apply, Fin.sum_univ_seven]

/-- The other order, so `Q` is unimodular. -/
theorem quotient_matrix_inverse' : quotientMatrix * recoveryMatrix = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [recoveryMatrix, quotientMatrix, Matrix.mul_apply, Fin.sum_univ_seven]

/-- `Q` is unimodular: `det Q = ±1` (the probe gives `−1`). -/
theorem det_unit_of_left_inverse {n : ℕ} (R Q : Matrix (Fin n) (Fin n) ℤ) (h : R * Q = 1) :
    Q.det = 1 ∨ Q.det = -1 := by
  have h' : R.det * Q.det = 1 := by rw [← Matrix.det_mul, h, Matrix.det_one]
  exact Int.isUnit_iff.mp (isUnit_of_mul_eq_one_right _ _ h')

theorem quotient_matrix_det : quotientMatrix.det = 1 ∨ quotientMatrix.det = -1 :=
  det_unit_of_left_inverse _ _ quotient_matrix_inverse

/-- **Recovery, as a statement about multiplicities.** If the quotient multiplicities are
`d_H = Σ_ρ dim ρ^H · m_ρ`, then `m = R d`. -/
theorem recover_types (m : Fin 7 → ℤ) :
    recoveryMatrix.mulVec (quotientMatrix.mulVec m) = m := by
  rw [Matrix.mulVec_mulVec, quotient_matrix_inverse, Matrix.one_mulVec]

/-- Of the seven quotients, only `B/A₄` has positive genus (a torus). -/
theorem recovery_quotients_genus :
    [9, 13, 14, 15, 16, 17, 18].map (fun n => (subgroupClasses.map fixedRow).getD n [] |>.getD 3 0)
      = [0, 0, 1, 0, 0, 0, 0] := by
  decide

/-! ## 4. One genus-2 quotient sees every type -/

/-- Every type has a fixed vector under `⟨(01)(23)⟩` (genus-2 quotient). -/
theorem double_transposition_sees_all :
    (fixedRow (2, ![1, 0, 1, 0, 0, 0, 0])).all (fun d => decide (0 < d)) = true := by decide

/-- Every type has a fixed vector under `C₃` (genus-2 quotient). -/
theorem C3_sees_all :
    (fixedRow (3, ![1, 0, 0, 2, 0, 0, 0])).all (fun d => decide (0 < d)) = true := by decide

/-- No subgroup whose quotient is a sphere or a torus sees every type. -/
theorem no_genus_le_one_quotient_sees_all :
    subgroupClasses.all (fun p =>
      decide (fixedSum p.2 ≤ p.1 → ∃ d ∈ fixedRow p, d = 0)) = true := by
  decide

/-! ## 5. Harmonic 1-cochains of the Bring map: `2 × [2,1,1,1]` -/

section Cells

open QOU.BringRegularMap Equiv

/-- The vertex stabiliser `⟨S⟩`: `S` and `S³` are 4-cycles, `S²` is a double transposition. -/
theorem S_powers : S ^ 2 = swap 1 3 * swap 2 4 ∧ S ^ 3 = S⁻¹ ∧ S ^ 4 = 1 := by decide

/-- The face stabiliser `⟨S·A⟩`: its four non-identity elements are 5-cycles. -/
theorem SA_powers : (S * A) ^ 5 = 1 ∧ ∀ k ∈ [1, 2, 3, 4], ∀ x, ((S * A) ^ k) x ≠ x := by
  decide

/-- The edge stabiliser `⟨A⟩` reverses its edge: the two darts `g`, `g·A` of the edge
`g⟨A⟩` are swapped by `g A g⁻¹`. -/
theorem A_reverses (g : Perm (Fin 5)) : (g * A * g⁻¹) * g = g * A ∧ g * A ≠ g := by
  refine ⟨by group, ?_⟩
  intro h
  have : A = 1 := by simpa using congrArg (g⁻¹ * ·) h
  exact absurd this (by decide)

end Cells

/-- Induced (or sign-twisted induced) character: `Ind_H^G ε (g_i) = |C(g_i)|/|H| · Σ_{h ∈ H ∩ i} ε(h)`,
from the signed class distribution `kε`. -/
def indChar (n : ℤ) (kε : Fin 7 → ℤ) (i : Fin 7) : ℤ := centraliser i * kε i / n

/-- `C⁰`: functions on the 30 vertices, induced from `⟨S⟩ ≅ C₄`. -/
def chiC0 : Fin 7 → ℤ := indChar 4 ![1, 0, 1, 0, 0, 2, 0]
/-- `C¹`: oriented 1-cochains on the 60 edges, induced from the sign of `⟨A⟩ ≅ C₂`. -/
def chiC1 : Fin 7 → ℤ := indChar 2 ![1, -1, 0, 0, 0, 0, 0]
/-- `C²`: 2-cochains on the 24 faces (rotations keep orientation), induced from `⟨S·A⟩ ≅ C₅`. -/
def chiC2 : Fin 7 → ℤ := indChar 5 ![1, 0, 0, 0, 0, 0, 4]

theorem cell_dims : chiC0 0 = 30 ∧ chiC1 0 = 60 ∧ chiC2 0 = 24 := by decide

theorem cell_characters :
    chiC0 = ![30, 0, 2, 0, 0, 2, 0] ∧ chiC1 = ![60, -6, 0, 0, 0, 0, 0] ∧
      chiC2 = ![24, 0, 0, 0, 0, 0, 4] := by
  decide

/-- **Hopf trace.** `χ_{H¹} = χ_{H⁰} + χ_{H²} − (χ_{C⁰} − χ_{C¹} + χ_{C²}) = 2·[2,1,1,1]`,
with `H⁰ = H² = triv` (connected, `S₅` orientation-preserving). -/
theorem hopf_trace_h1 :
    (fun i => 2 * chiTriv i - (chiC0 i - chiC1 i + chiC2 i)) = fun i => 2 * chi2111 i := by
  decide

/-- So `H¹` has no other type: `⟨χ_{H¹}, χ_ρ⟩ = 2 δ_{ρ,[2,1,1,1]}`. -/
theorem h1_types :
    (List.finRange 7).map (fun r => inner (fun i => 2 * chi2111 i) (irr r)) =
      [0, 0, 0, 240, 0, 0, 0] := by
  decide

/-- Halving with Hodge `H¹ = H⁰(K) ⊕ conj` and real characters gives `H⁰(K) = [2,1,1,1]`, the
same answer as `h0K_character_forced`. Euler check: `30 − 60 + 24 = −6`. -/
theorem cell_euler : chiC0 0 - chiC1 0 + chiC2 0 = -6 := by decide

/-! ## 6. Vertex, edge and face functions by type -/

/-- Functions on the 30 vertices: `triv + [4,1] + [2,1,1,1] + [3,2] + 2·[2,2,1] + [3,1,1]`. -/
theorem vertex_functions_decomposition :
    chiC0 = fun i => chiTriv i + chiStd i + chi2111 i + chi32 i + 2 * chi221 i + chi311 i := by
  decide

/-- Oriented 1-cochains on the 60 edges:
`sgn + [4,1] + 3·[2,1,1,1] + 2·[3,2] + 3·[2,2,1] + 3·[3,1,1]`. -/
theorem edge_cochains_decomposition :
    chiC1 = fun i => chiSign i + chiStd i + 3 * chi2111 i + 2 * chi32 i + 3 * chi221 i +
      3 * chi311 i := by
  decide

/-- Functions on the 24 faces: `triv + sgn + [3,2] + [2,2,1] + 2·[3,1,1]`. -/
theorem face_functions_decomposition :
    chiC2 = fun i => chiTriv i + chiSign i + chi32 i + chi221 i + 2 * chi311 i := by
  decide

end QOU.Brings.HarmonicTypes
