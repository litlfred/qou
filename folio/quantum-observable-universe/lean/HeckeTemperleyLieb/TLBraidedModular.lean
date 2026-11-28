import HeckeTemperleyLieb.TLCableLoop

/-!
# The `S`- and `T`-matrices of the Temperley–Lieb tower at a root of unity, from braiding

Bean `hkmt`. `TLRootOfUnitySMatrixNondegenerate` proves the modular relations for the matrices
`S_{ij} = [(i+1)(j+1)]` and `T = diag(ω^{(j+1)²})`. This file shows that both are what the
braiding of the Temperley–Lieb tower gives on the Jones–Wenzl projectors `p_0, …, p_{k−1}` and the
vacuum, for any Markov trace with `δε = 1`.

* `braidS`: the matrix of unnormalised Hopf-link traces. Entry `(0,0)` is the empty diagram, entry
  `(0, j+1)` and `(j+1, 0)` the closure of `p_j`, entry `(i+1, j+1)` the Hopf link of `p_i` with
  the cable carrying `p_j` (`TLCable.cH`).
* `braidS_eq_sMatrix`: `braidS = S`, entrywise from `vacuum_row_eq_sMatrix` and
  `cable_row_eq_sMatrix`.
* `braidS_mul_self`, `braidS_det_ne_zero`: `S² = D²·1` and `det S ≠ 0` for the braid-derived
  matrix. Nondegeneracy of `S` on the simples is the modularity condition for the braiding.
* `ribbon_jw`: the ribbon element (full twist `Δ²` with one framing curl `A³` per strand) acts on
  `p_n` by `ω⁻¹·T_{n+1}`, so the twist eigenvalues are also derived from braiding.
* `braid_modular_relation`: `δ·(S T)³ = −G·S²` with `S = braidS`.

Scope: this is the statement on the Jones–Wenzl projectors and their traces. That the vacuum and
`p_0, …, p_{k−1}` are exactly the simple objects of the semisimplified quotient category is not
proved here.

No empirical input; everything is over an arbitrary field.

-- Ref: [turaev1994] Quantum invariants of knots and 3-manifolds, ch. II.
-- Ref: [kirbymelvin1991] https://doi.org/10.1007/BF01239527
-/

namespace QOU.HeckeTemperleyLieb.TLBraidedModular

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLPositiveLoop QOU.HeckeTemperleyLieb.TLHopfRow
open QOU.HeckeTemperleyLieb.TLRootOfUnity QOU.HeckeTemperleyLieb.TLVacuumRow
open QOU.HeckeTemperleyLieb.TLCable

variable {K : Type*} [Field K]

/-- The unnormalised Hopf-link trace of the `i`-th and `j`-th objects (`0` = vacuum, `n + 1` = the
Jones–Wenzl projector `p_n` on `n + 1` strands). -/
noncomputable def braidEntry {δ ε : K} (A : K) (T : MarkovTower δ ε) : ℕ → ℕ → K
  | 0, 0 => T.τ 0 1
  | 0, j + 1 => δ ^ (j + 1) * T.τ j (jw δ j)
  | i + 1, 0 => δ ^ (i + 1) * T.τ i (jw δ i)
  | i + 1, j + 1 => δ ^ (i + j + 2) * cH A T i j

/-- The braid-derived `S`-matrix on the vacuum and `p_0, …, p_{k−1}`. -/
noncomputable def braidS {δ ε : K} (A : K) (T : MarkovTower δ ε) (k : ℕ) :
    Matrix (Fin (k + 1)) (Fin (k + 1)) K :=
  fun i j => braidEntry A T i.val j.val

theorem qInt_one' (ζ : Kˣ) : qInt ζ 1 = 1 := by simp [qInt]

/-- **`S` from braiding.** -/
theorem braidS_eq_sMatrix (ω : Kˣ) (k : ℕ) (hζ : IsPrimitiveRoot (ω ^ 2) (2 * (k + 2))) {ε : K}
    (T : MarkovTower (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ε)
    (hε : (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) * ε = 1) :
    braidS (ω : K) T k = sMatrix (ω ^ 2) k := by
  ext ⟨i, hi⟩ ⟨j, hj⟩
  show braidEntry (ω : K) T i j = qInt (ω ^ 2) ((i + 1) * (j + 1))
  match i, j, hi, hj with
  | 0, 0, _, _ =>
    show T.τ 0 1 = qInt (ω ^ 2) 1
    rw [T.tr_one, qInt_one']
  | 0, j + 1, _, hj =>
    have h := vacuum_row_eq_sMatrix k hζ T hε j (by omega)
    simp only [sMatrix] at h
    exact h
  | i + 1, 0, hi, _ =>
    have h := vacuum_row_eq_sMatrix k hζ T hε i (by omega)
    simp only [sMatrix, Fin.val_zero] at h
    show (_ : K) ^ (i + 1) * T.τ i (jw _ i) = qInt (ω ^ 2) ((i + 1 + 1) * (0 + 1))
    rw [h, mul_comm]
  | i + 1, j + 1, hi, hj =>
    exact cable_row_eq_sMatrix ω k hζ T hε i j (by omega) (by omega)

/-- **`S² = D²·1` for the braid-derived `S`.** -/
theorem braidS_mul_self (ω : Kˣ) (k : ℕ) (hζ : IsPrimitiveRoot (ω ^ 2) (2 * (k + 2))) {ε : K}
    (T : MarkovTower (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ε)
    (hε : (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) * ε = 1) :
    qDelta (ω ^ 2) ^ 2 • (braidS (ω : K) T k * braidS (ω : K) T k) =
      (-(2 * ((k : K) + 2))) • (1 : Matrix (Fin (k + 1)) (Fin (k + 1)) K) := by
  rw [braidS_eq_sMatrix ω k hζ T hε]; exact sMatrix_mul_self k hζ

/-- **Modularity.** The braid-derived `S`-matrix is nondegenerate. -/
theorem braidS_det_ne_zero (ω : Kˣ) (k : ℕ) (hζ : IsPrimitiveRoot (ω ^ 2) (2 * (k + 2))) {ε : K}
    (T : MarkovTower (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ε)
    (hε : (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) * ε = 1) :
    (braidS (ω : K) T k).det ≠ 0 := by
  rw [braidS_eq_sMatrix ω k hζ T hε]; exact sMatrix_det_ne_zero k hζ

/-- **The twist from braiding.** The ribbon element, the full twist `Δ²` on `n + 1` strands with
one framing curl `A³` per strand (`markov_curl`), acts on `p_n` by `ω⁻¹·T_{n+1,n+1}`. -/
theorem ribbon_jw (ω : Kˣ) (k : ℕ) {δ : K} (n : ℕ) (hS : JWSpec δ n) (hn : n + 1 ≤ k) :
    ((ω : K) ^ 3) ^ (n + 1) • (jw δ n * fullTwist δ (ω : K) n) =
      ((ω : K)⁻¹ * tMatrix ω k ⟨n + 1, by omega⟩ ⟨n + 1, by omega⟩) • jw δ n := by
  rw [jw_mul_fullTwist hS, smul_smul, tMatrix, Matrix.diagonal_apply_eq,
    ← twist_eq_tMatrix ω n]
  congr 1
  field_simp

/-- **The modular relation for the braid-derived `S`.** `δ·(S T)³ = −G·S²`. -/
theorem braid_modular_relation (ω : Kˣ) (k : ℕ) (hω : IsPrimitiveRoot ω (4 * (k + 2))) {ε : K}
    (T : MarkovTower (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ε)
    (hε : (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) * ε = 1) :
    qDelta (ω ^ 2) • (braidS (ω : K) T k * tMatrix ω k) ^ 3 =
      (-gaussSum ω (2 * (k + 2))) • (braidS (ω : K) T k * braidS (ω : K) T k) := by
  rw [braidS_eq_sMatrix ω k (isPrimitiveRoot_sq k hω) T hε]
  exact sMatrix_tMatrix_cube k hω

end QOU.HeckeTemperleyLieb.TLBraidedModular
