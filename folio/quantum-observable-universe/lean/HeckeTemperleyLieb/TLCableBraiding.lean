import HeckeTemperleyLieb.TLPositiveLoopCrossingTwist

/-!
# The cable crossing, the half twist and the balancing identity in Temperley–Lieb

Bean `hkmt`. This file builds, inside one Temperley–Lieb algebra `TL_{N+1}(δ)` with
`δ = A² + A⁻²`, the braiding and twist data of the braided monoidal structure, **placed** on
consecutive blocks of strands. Everything is indexed by natural numbers, so a single ambient
algebra holds every block and no reindexing is needed.

* `E N i`, `X N i`: the generator `e_i` and the positive-loop crossing `σᵢ = A·1 − A⁻¹·eᵢ`
  indexed by `i : ℕ` (`0` and `1` outside the range).
* `H s m = σ_{s+m} ⋯ σ_s`: the strand at `s` passes the `m + 1` strands to its right.
* `C s n m = H s m · H (s+1) m ⋯ H (s+n) m`: the **cable crossing** of the block `[s, s+n]`
  past the block `[s+n+1, s+n+m+1]`.
* `C_mul_E_left`, `C_mul_E_right`: **naturality on generators**: `C` carries `e_{s+i}` of the
  left block to `e_{s+m+1+i}` and `e_{s+n+1+j}` of the right block to `e_{s+j}`.
  `C_mul_pl_left`, `C_mul_pl_right`: the same for every element placed in either block.
* `C_mul_Ci`, `Ci_mul_C`: the cable crossing is invertible.
* `C_hex_left`, `C_hex_right`: **the two hexagon identities**.
* `D s n`: the **half twist** on `[s, s+n]`, `D s (n+1) = D (s+1) n · C s n 0`.
  `D_split`: `D s (n+m+1) = D s m · D (s+m+1) n · C s n m` for every split (Yang–Baxter for
  blocks); `D_mul_E`: `D` reverses the block.
* `Θ s n = D s n · D s n`: the **full twist**. `Θ_balance`: the balancing identity
  `Θ s (n+m+1) = Θ s n · Θ (s+n+1) m · C s m n · C s n m`. `Θ_mul_E`: `Θ` commutes with every
  generator of its block.
* `X_mul_E_self`, `E_mul_loop`, `wind_mul_E`: a crossing on its own cap is `−A⁻³`, a cap slides
  off a double crossing, and a cap is unchanged when a block winds around it (the input to
  ribbon compatibility).
* `jw_mul_Θ`: `Θ 0 n` acts on the Jones–Wenzl projector `p_n` by `A^{n(n+1)}`, the same scalar as
  `fullTwist` in `TLPositiveLoopCrossingTwist`.

No empirical input; everything is over an arbitrary field with `A ≠ 0` and `δ = A² + A⁻²`.

-- Ref: [kassel1995] Kassel, *Quantum groups*, XIII.1 (braidings) and XIV.3 (twists).
-- Ref: [joyal1993] Joyal–Street, *Braided tensor categories*, Adv. Math. 102 (1993).
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLCableBraiding

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLPositiveLoop

variable {K : Type*} [Field K] {δ A : K}

/-! ## Generators and crossings by natural index -/

section Index

variable (δ) in
/-- `e_i` by natural index, `0` when `i ≥ N`. -/
noncomputable def E (N i : ℕ) : TLFin K δ N := if h : i < N then e K δ adjFin ⟨i, h⟩ else 0

variable (δ A) in
/-- `σᵢ` by natural index, `1` when `i ≥ N`. -/
noncomputable def X (N i : ℕ) : TLFin K δ N := if h : i < N then crossing δ A ⟨i, h⟩ else 1

variable (δ A) in
/-- `σᵢ⁻¹` by natural index, `1` when `i ≥ N`. -/
noncomputable def Xi (N i : ℕ) : TLFin K δ N :=
  if h : i < N then crossingInv δ A ⟨i, h⟩ else 1

variable {N : ℕ}

theorem E_of_lt {i : ℕ} (h : i < N) : E δ N i = e K δ adjFin ⟨i, h⟩ := dif_pos h

theorem X_of_lt {i : ℕ} (h : i < N) : X δ A N i = crossing δ A ⟨i, h⟩ := dif_pos h

theorem X_eq {i : ℕ} (h : i < N) : X δ A N i = A • 1 - A⁻¹ • E δ N i := by
  rw [X_of_lt h, E_of_lt h]; rfl

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

include hA in
theorem E_eq {i : ℕ} (h : i < N) : E δ N i = A ^ 2 • 1 - A • X δ A N i := by
  rw [X_eq h, smul_sub, smul_smul, smul_smul, mul_inv_cancel₀ hA, one_smul, sq]
  abel

include hA hδ in
theorem X_mul_Xi (i : ℕ) : X δ A N i * Xi δ A N i = 1 := by
  unfold X Xi; split_ifs with h
  · exact crossing_mul_crossingInv hA hδ _
  · exact one_mul 1

include hA hδ in
theorem Xi_mul_X (i : ℕ) : Xi δ A N i * X δ A N i = 1 := by
  unfold X Xi; split_ifs with h
  · exact crossingInv_mul_crossing hA hδ _
  · exact one_mul 1

/-- Far generators commute. -/
theorem E_comm_E {i j : ℕ} (h : i + 2 ≤ j ∨ j + 2 ≤ i) : Commute (E δ N i) (E δ N j) := by
  unfold E; split_ifs with hi hj hj
  · exact e_commute_fin (by simpa using h)
  all_goals simp

theorem X_comm_E {i j : ℕ} (h : i + 2 ≤ j ∨ j + 2 ≤ i) : Commute (X δ A N i) (E δ N j) := by
  by_cases hi : i < N
  · rw [X_eq hi]
    exact ((Commute.one_left _).smul_left A).sub_left ((E_comm_E h).smul_left _)
  · unfold X; rw [dif_neg hi]; exact Commute.one_left _

theorem X_comm_X {i j : ℕ} (h : i + 2 ≤ j ∨ j + 2 ≤ i) : Commute (X δ A N i) (X δ A N j) := by
  by_cases hj : j < N
  · rw [X_eq (A := A) hj]
    exact ((Commute.one_right _).smul_right A).sub_right ((X_comm_E h).smul_right _)
  · unfold X; rw [dif_neg hj]; exact Commute.one_right _

theorem Xi_comm_X {i j : ℕ} (h : i + 2 ≤ j ∨ j + 2 ≤ i) : Commute (Xi δ A N i) (X δ A N j) := by
  unfold Xi; split_ifs with hi
  · have : crossingInv δ A ⟨i, hi⟩ = A⁻¹ • 1 - A • E δ N i := by rw [E_of_lt hi]; rfl
    rw [this]
    exact ((Commute.one_left _).smul_left _).sub_left ((X_comm_E (Or.symm h)).symm.smul_left _)
  · exact Commute.one_left _

include hA hδ in
theorem X_braid {i : ℕ} (h : i + 1 < N) :
    X δ A N i * X δ A N (i + 1) * X δ A N i = X δ A N (i + 1) * X δ A N i * X δ A N (i + 1) := by
  rw [X_of_lt (by omega : i < N), X_of_lt h]
  exact crossing_braid hA hδ (Or.inl rfl)

include hA hδ in
/-- `σᵢσᵢ₊₁ eᵢ = eᵢ₊₁ σᵢσᵢ₊₁`. -/
theorem XX_mul_E_up {i : ℕ} (h : i + 1 < N) :
    X δ A N i * X δ A N (i + 1) * E δ N i = E δ N (i + 1) * (X δ A N i * X δ A N (i + 1)) := by
  rw [E_eq hA (by omega : i < N), E_eq hA h]
  simp only [mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, mul_one, one_mul]
  rw [X_braid hA hδ h, mul_assoc (X δ A N (i + 1))]

include hA hδ in
/-- `σᵢ₊₁σᵢ eᵢ₊₁ = eᵢ σᵢ₊₁σᵢ`. -/
theorem XX_mul_E_down {i : ℕ} (h : i + 1 < N) :
    X δ A N (i + 1) * X δ A N i * E δ N (i + 1) = E δ N i * (X δ A N (i + 1) * X δ A N i) := by
  rw [E_eq hA (by omega : i < N), E_eq hA h]
  simp only [mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, mul_one, one_mul]
  rw [← X_braid hA hδ h, mul_assoc (X δ A N i)]

end Index

/-! ## One strand past a block -/

section Strand

variable {N : ℕ}

variable (δ A N) in
/-- `H s m = σ_{s+m} ⋯ σ_{s+1} σ_s`. -/
noncomputable def H (s : ℕ) : ℕ → TLFin K δ N
  | 0 => X δ A N s
  | m + 1 => X δ A N (s + m + 1) * H s m

variable (δ A N) in
/-- Its inverse `σ_s⁻¹ ⋯ σ_{s+m}⁻¹`. -/
noncomputable def Hi (s : ℕ) : ℕ → TLFin K δ N
  | 0 => Xi δ A N s
  | m + 1 => Hi s m * Xi δ A N (s + m + 1)

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

include hA hδ in
theorem H_mul_Hi (s : ℕ) : ∀ m, H δ A N s m * Hi δ A N s m = 1
  | 0 => X_mul_Xi hA hδ s
  | m + 1 => by
    simp only [H, Hi]
    rw [mul_assoc, ← mul_assoc (H δ A N s m), H_mul_Hi s m, one_mul, X_mul_Xi hA hδ]

include hA hδ in
theorem Hi_mul_H (s : ℕ) : ∀ m, Hi δ A N s m * H δ A N s m = 1
  | 0 => Xi_mul_X hA hδ s
  | m + 1 => by
    simp only [H, Hi]
    rw [mul_assoc, ← mul_assoc (Xi δ A N _), Xi_mul_X hA hδ, one_mul, Hi_mul_H s m]

/-- `H s m` commutes with every generator at distance `≥ 2` from `[s, s+m]`. -/
theorem H_comm_E (s : ℕ) : ∀ (m : ℕ) {j : ℕ}, (j + 2 ≤ s ∨ s + m + 2 ≤ j) →
    Commute (H δ A N s m) (E δ N j)
  | 0, j, h => X_comm_E (by omega)
  | m + 1, j, h => (X_comm_E (by omega)).mul_left (H_comm_E s m (by omega))

theorem H_comm_X (s : ℕ) : ∀ (m : ℕ) {j : ℕ}, (j + 2 ≤ s ∨ s + m + 2 ≤ j) →
    Commute (H δ A N s m) (X δ A N j)
  | 0, j, h => X_comm_X (by omega)
  | m + 1, j, h => (X_comm_X (by omega)).mul_left (H_comm_X s m (by omega))

/-- Disjoint far blocks commute. -/
theorem H_comm_H (s t m : ℕ) (h : s + m + 2 ≤ t) : ∀ p, Commute (H δ A N s m) (H δ A N t p)
  | 0 => H_comm_X s m (by omega)
  | p + 1 => (H_comm_X s m (by omega)).mul_right (H_comm_H s t m h p)

include hA hδ in
/-- **One strand past a block shifts the block down**: `H s m · e_{s+1+j} = e_{s+j} · H s m`. -/
theorem H_mul_E (s : ℕ) : ∀ (m : ℕ) {j : ℕ}, j < m → s + m < N →
    H δ A N s m * E δ N (s + 1 + j) = E δ N (s + j) * H δ A N s m
  | 0, j, hj, _ => absurd hj (Nat.not_lt_zero _)
  | m + 1, j, hj, hN => by
    rcases Nat.lt_succ_iff_lt_or_eq.mp hj with hj | rfl
    · simp only [H]
      rw [mul_assoc, H_mul_E s m hj (by omega), ← mul_assoc, ← mul_assoc,
        (X_comm_E (by omega)).eq]
    · cases j with
      | zero =>
        simp only [H, Nat.add_zero]
        have := XX_mul_E_down (N := N) hA hδ (i := s) (by omega)
        simpa [mul_assoc] using this
      | succ j =>
        simp only [H]
        have hc := H_comm_E (N := N) (δ := δ) (A := A) s j (j := s + 1 + (j + 1)) (by omega)
        have key := XX_mul_E_down (N := N) hA hδ (i := s + j + 1) (by omega)
        rw [show s + (j + 1) + 1 = s + j + 1 + 1 by omega, show s + 1 + (j + 1) = s + j + 1 + 1 by
          omega] at *
        rw [show s + (j + 1) = s + j + 1 by omega]
        rw [mul_assoc, mul_assoc, hc.eq, ← mul_assoc, ← mul_assoc, key, mul_assoc, mul_assoc]

include hA hδ in
/-- **Two consecutive strands past a block**: `H s m · H (s+1) m · e_s = e_{s+m+1} · H s m ·
H (s+1) m`. -/
theorem HH_mul_E (s : ℕ) : ∀ (m : ℕ), s + m + 1 < N →
    H δ A N s m * H δ A N (s + 1) m * E δ N s =
      E δ N (s + m + 1) * (H δ A N s m * H δ A N (s + 1) m)
  | 0, hN => by
    simp only [H, Nat.add_zero]
    exact XX_mul_E_up hA hδ (by omega)
  | m + 1, hN => by
    have hc : Commute (H δ A N s m) (X δ A N (s + 1 + m + 1)) := H_comm_X s m (by omega)
    have hsplit : H δ A N s (m + 1) * H δ A N (s + 1) (m + 1) =
        X δ A N (s + m + 1) * X δ A N (s + m + 1 + 1) * (H δ A N s m * H δ A N (s + 1) m) := by
      simp only [H]
      rw [mul_assoc, ← mul_assoc (H δ A N s m), hc.eq]
      rw [show s + 1 + m + 1 = s + m + 1 + 1 by omega]
      simp only [mul_assoc]
    rw [hsplit, mul_assoc, HH_mul_E s m (by omega), ← mul_assoc, XX_mul_E_up hA hδ (by omega)]
    rw [show s + (m + 1) + 1 = s + m + 1 + 1 by omega, mul_assoc]

end Strand

/-! ## The cable crossing -/

section Cable

variable {N : ℕ}

variable (δ A N) in
/-- **The cable crossing** of the block `[s, s+n]` past the block `[s+n+1, s+n+m+1]`:
`C s n m = H s m · H (s+1) m ⋯ H (s+n) m`. -/
noncomputable def C (s : ℕ) : ℕ → ℕ → TLFin K δ N
  | 0, m => H δ A N s m
  | n + 1, m => C s n m * H δ A N (s + n + 1) m

variable (δ A N) in
/-- Its inverse. -/
noncomputable def Ci (s : ℕ) : ℕ → ℕ → TLFin K δ N
  | 0, m => Hi δ A N s m
  | n + 1, m => Hi δ A N (s + n + 1) m * Ci s n m

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

include hA hδ in
theorem C_mul_Ci (s : ℕ) : ∀ n m, C δ A N s n m * Ci δ A N s n m = 1
  | 0, m => H_mul_Hi hA hδ s m
  | n + 1, m => by
    simp only [C, Ci]
    rw [mul_assoc, ← mul_assoc (H δ A N _ m), H_mul_Hi hA hδ, one_mul, C_mul_Ci s n m]

include hA hδ in
theorem Ci_mul_C (s : ℕ) : ∀ n m, Ci δ A N s n m * C δ A N s n m = 1
  | 0, m => Hi_mul_H hA hδ s m
  | n + 1, m => by
    simp only [C, Ci]
    rw [mul_assoc, ← mul_assoc (Ci δ A N s n m), Ci_mul_C s n m, one_mul, Hi_mul_H hA hδ]

theorem C_comm_E (s : ℕ) : ∀ (n m : ℕ) {j : ℕ}, (j + 2 ≤ s ∨ s + n + m + 2 ≤ j) →
    Commute (C δ A N s n m) (E δ N j)
  | 0, m, j, h => H_comm_E s m (by omega)
  | n + 1, m, j, h => (C_comm_E s n m (by omega)).mul_left (H_comm_E _ m (by omega))

theorem C_comm_X (s : ℕ) : ∀ (n m : ℕ) {j : ℕ}, (j + 2 ≤ s ∨ s + n + m + 2 ≤ j) →
    Commute (C δ A N s n m) (X δ A N j)
  | 0, m, j, h => H_comm_X s m (by omega)
  | n + 1, m, j, h => (C_comm_X s n m (by omega)).mul_left (H_comm_X _ m (by omega))

theorem C_comm_H (s n m t : ℕ) (h : s + n + m + 2 ≤ t) :
    ∀ p, Commute (C δ A N s n m) (H δ A N t p)
  | 0 => C_comm_X s n m (by omega)
  | p + 1 => (C_comm_X s n m (by omega)).mul_right (C_comm_H s n m t h p)

include hA hδ in
/-- **Naturality, right block**: `C s n m · e_{s+n+1+j} = e_{s+j} · C s n m` for `j < m`. -/
theorem C_mul_E_right (s : ℕ) : ∀ (n m : ℕ) {j : ℕ}, j < m → s + n + m < N →
    C δ A N s n m * E δ N (s + n + 1 + j) = E δ N (s + j) * C δ A N s n m
  | 0, m, j, hj, hN => by
    simp only [C, Nat.add_zero]; exact H_mul_E hA hδ s m hj (by omega)
  | n + 1, m, j, hj, hN => by
    simp only [C]
    have h1 := H_mul_E (N := N) hA hδ (s + n + 1) m hj (by omega)
    rw [show s + n + 1 + 1 + j = s + n + 1 + 1 + j from rfl] at h1
    rw [show s + (n + 1) + 1 + j = s + n + 1 + 1 + j by omega, mul_assoc, h1,
      show s + n + 1 + j = s + n + 1 + j from rfl, ← mul_assoc, C_mul_E_right s n m hj (by omega),
      mul_assoc]

include hA hδ in
/-- **Naturality, left block**: `C s n m · e_{s+i} = e_{s+m+1+i} · C s n m` for `i < n`. -/
theorem C_mul_E_left (s : ℕ) : ∀ (n m : ℕ) {i : ℕ}, i < n → s + n + m < N →
    C δ A N s n m * E δ N (s + i) = E δ N (s + m + 1 + i) * C δ A N s n m
  | 0, m, i, hi, _ => absurd hi (Nat.not_lt_zero _)
  | n + 1, m, i, hi, hN => by
    rcases Nat.lt_succ_iff_lt_or_eq.mp hi with hi | rfl
    · simp only [C]
      rw [mul_assoc, (H_comm_E (s + n + 1) m (j := s + i) (by omega)).eq, ← mul_assoc,
        C_mul_E_left s n m hi (by omega), mul_assoc]
    · cases i with
      | zero =>
        simp only [C, Nat.add_zero]
        have := HH_mul_E (N := N) hA hδ s m (by omega)
        rw [this]
      | succ i =>
        simp only [C]
        have key := HH_mul_E (N := N) hA hδ (s + i + 1) m (by omega)
        have hc := C_comm_E (δ := δ) (A := A) (N := N) s i m (j := s + i + 1 + m + 1) (by omega)
        rw [show s + (i + 1) = s + i + 1 by omega,
          show s + m + 1 + (i + 1) = s + i + 1 + m + 1 by omega]
        rw [mul_assoc (C δ A N s i m * _), mul_assoc (C δ A N s i m), ← mul_assoc (H δ A N (s + i + 1) m),
          key, ← mul_assoc, hc.eq, mul_assoc, mul_assoc]

/-! ### The hexagons -/

/-- `H k (m + p + 1) = H (k + m + 1) p · H k m`. -/
theorem H_split (k m : ℕ) : ∀ p, H δ A N k (m + p + 1) = H δ A N (k + m + 1) p * H δ A N k m
  | 0 => rfl
  | p + 1 => by
    show X δ A N (k + (m + p + 1) + 1) * H δ A N k (m + p + 1) = _
    rw [H_split k m p]
    show _ = X δ A N (k + m + 1 + p + 1) * H δ A N (k + m + 1) p * H δ A N k m
    rw [show k + (m + p + 1) + 1 = k + m + 1 + p + 1 by omega, mul_assoc]

/-- **First hexagon**: splitting the left block, `C s (n+m+1) p = C s n p · C (s+n+1) m p`. -/
theorem C_hex_left (s n p : ℕ) : ∀ m,
    C δ A N s (n + m + 1) p = C δ A N s n p * C δ A N (s + n + 1) m p
  | 0 => rfl
  | m + 1 => by
    show C δ A N s (n + m + 1) p * H δ A N (s + (n + m + 1) + 1) p = _
    rw [C_hex_left s n p m]
    show _ = C δ A N s n p * (C δ A N (s + n + 1) m p * H δ A N (s + n + 1 + m + 1) p)
    rw [show s + (n + m + 1) + 1 = s + n + 1 + m + 1 by omega, mul_assoc]

/-- **Second hexagon**: splitting the right block,
`C s n (m+p+1) = C (s+m+1) n p · C s n m`. -/
theorem C_hex_right (s m p : ℕ) : ∀ n,
    C δ A N s n (m + p + 1) = C δ A N (s + m + 1) n p * C δ A N s n m
  | 0 => H_split s m p
  | n + 1 => by
    show C δ A N s n (m + p + 1) * H δ A N (s + n + 1) (m + p + 1) = _
    rw [C_hex_right s m p n, H_split]
    show _ = C δ A N (s + m + 1) n p * H δ A N (s + m + 1 + n + 1) p *
      (C δ A N s n m * H δ A N (s + n + 1) m)
    have hc := C_comm_H (δ := δ) (A := A) (N := N) s n m (s + n + 1 + m + 1) (by omega) p
    rw [show s + m + 1 + n + 1 = s + n + 1 + m + 1 by omega]
    simp only [mul_assoc]
    rw [← mul_assoc (C δ A N s n m), hc.eq, mul_assoc]

end Cable

/-! ## Placing a smaller algebra on a block of strands -/

section Place

variable {N : ℕ}

variable (δ) in
/-- `pl t M h : TL_{M+1} → TL_{N+1}`, `e_j ↦ e_{t+j}`: the strands `[t, t+M]`. -/
noncomputable def pl (t M : ℕ) (h : t + M ≤ N) : TLFin K δ M →ₐ[K] TLFin K δ N :=
  lift K δ adjFin (fun j => E δ N (t + j))
    (fun j => by dsimp only; rw [E_of_lt (by omega)]; exact e_sq _)
    (fun i j hij => by
      dsimp only
      rw [E_of_lt (by omega), E_of_lt (by omega)]
      exact e_adjacent (by simp only [adjFin] at hij ⊢; omega))
    (fun i j hij => by
      dsimp only
      rw [E_of_lt (by omega), E_of_lt (by omega)]
      exact e_farCommute (by simp only [adjFin] at hij ⊢; omega))

@[simp] theorem pl_e (t M : ℕ) (h : t + M ≤ N) (j : Fin M) :
    pl δ t M h (e K δ adjFin j) = E δ N (t + j) := lift_e _ _ _ _ _ _ _ j

theorem pl_E (t M : ℕ) (h : t + M ≤ N) {j : ℕ} (hj : j < M) :
    pl δ t M h (E δ M j) = E δ N (t + j) := by
  rw [E_of_lt hj, pl_e]

theorem pl_X (t M : ℕ) (h : t + M ≤ N) {i : ℕ} (hi : i < M) :
    pl δ t M h (X δ A M i) = X δ A N (t + i) := by
  rw [X_eq hi, X_eq (by omega), map_sub, map_smul, map_smul, map_one, pl_E t M h hi]

theorem pl_H (t M : ℕ) (h : t + M ≤ N) (a : ℕ) : ∀ m, a + m < M →
    pl δ t M h (H δ A M a m) = H δ A N (t + a) m
  | 0, hm => pl_X t M h (by omega)
  | m + 1, hm => by
    show pl δ t M h (X δ A M (a + m + 1) * H δ A M a m) = X δ A N (t + a + m + 1) * _
    rw [map_mul, pl_X t M h (by omega), pl_H t M h a m (by omega),
      show t + (a + m + 1) = t + a + m + 1 by omega]

theorem pl_C (t M : ℕ) (h : t + M ≤ N) (a m : ℕ) : ∀ n, a + n + m < M →
    pl δ t M h (C δ A M a n m) = C δ A N (t + a) n m
  | 0, hn => pl_H t M h a m (by omega)
  | n + 1, hn => by
    show pl δ t M h (C δ A M a n m * H δ A M (a + n + 1) m) =
      C δ A N (t + a) n m * H δ A N (t + a + n + 1) m
    rw [map_mul, pl_C t M h a m n (by omega), pl_H t M h _ m (by omega),
      show t + (a + n + 1) = t + a + n + 1 by omega]

/-- An algebra map out of `TL` is determined, up to conjugation by `c`, by the generators. -/
theorem conj_of_gens {M : ℕ} {B : Type*} [Ring B] [Algebra K B]
    (f g : TLFin K δ M →ₐ[K] B) (c : B) (hg : ∀ i, c * f (e K δ adjFin i) = g (e K δ adjFin i) * c)
    (x : TLFin K δ M) : c * f x = g x * c := by
  induction mem_adjoin_e x using Algebra.adjoin_induction with
  | mem y hy => obtain ⟨j, rfl⟩ := hy; exact hg j
  | algebraMap r => rw [AlgHom.commutes, AlgHom.commutes, Algebra.commutes]
  | add y z _ _ hy hz => rw [map_add, map_add, mul_add, add_mul, hy, hz]
  | mul y z _ _ hy hz => rw [map_mul, map_mul, ← mul_assoc, hy, mul_assoc, hz, mul_assoc]

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

include hA hδ in
/-- **Naturality of the cable crossing, right block.** -/
theorem C_mul_pl_right (s n m : ℕ) (hN : s + n + m < N) (x : TLFin K δ m) :
    C δ A N s n m * pl δ (s + n + 1) m (by omega) x = pl δ s m (by omega) x * C δ A N s n m :=
  conj_of_gens _ _ _ (fun j => by
    rw [pl_e, pl_e]; exact C_mul_E_right hA hδ s n m j.isLt hN) x

include hA hδ in
/-- **Naturality of the cable crossing, left block.** -/
theorem C_mul_pl_left (s n m : ℕ) (hN : s + n + m < N) (x : TLFin K δ n) :
    C δ A N s n m * pl δ s n (by omega) x = pl δ (s + m + 1) n (by omega) x * C δ A N s n m :=
  conj_of_gens _ _ _ (fun i => by
    rw [pl_e, pl_e]; exact C_mul_E_left hA hδ s n m i.isLt hN) x

end Place

/-! ## The half twist and the full twist -/

section Twist

variable {N : ℕ}

variable (δ A N) in
/-- **The half twist** on the strands `[s, s+n]`: `D s 0 = 1`, `D s (n+1) = D (s+1) n · C s n 0`
(move the first `n + 1` strands past the last one, then half-twist them). -/
noncomputable def D : ℕ → ℕ → TLFin K δ N
  | _, 0 => 1
  | s, n + 1 => D (s + 1) n * C δ A N s n 0

variable (δ A N) in
/-- **The full twist** `Θ s n = D s n · D s n` on the strands `[s, s+n]`. -/
noncomputable def Θ (s n : ℕ) : TLFin K δ N := D δ A N s n * D δ A N s n

theorem D_comm_X : ∀ (n s : ℕ) {j : ℕ}, (j + 2 ≤ s ∨ s + n + 1 ≤ j) →
    Commute (D δ A N s n) (X δ A N j)
  | 0, s, j, _ => Commute.one_left _
  | n + 1, s, j, h => (D_comm_X n (s + 1) (by omega)).mul_left (C_comm_X s n 0 (by omega))

theorem D_comm_E : ∀ (n s : ℕ) {j : ℕ}, (j + 2 ≤ s ∨ s + n + 1 ≤ j) →
    Commute (D δ A N s n) (E δ N j)
  | 0, s, j, _ => Commute.one_left _
  | n + 1, s, j, h => (D_comm_E n (s + 1) (by omega)).mul_left (C_comm_E s n 0 (by omega))

/-- Everything commuting with the crossings `σ_j`, `s ≤ j ≤ s + m`, commutes with `H s m`. -/
theorem H_comm_of (s : ℕ) (y : TLFin K δ N) : ∀ m, (∀ j, s ≤ j → j ≤ s + m → Commute (X δ A N j) y) →
    Commute (H δ A N s m) y
  | 0, h => h s le_rfl (by omega)
  | m + 1, h => (h _ (by omega) (by omega)).mul_left (H_comm_of s y m fun j h1 h2 => h j h1 (by omega))

theorem C_comm_of (s m : ℕ) (y : TLFin K δ N) : ∀ n,
    (∀ j, s ≤ j → j ≤ s + n + m → Commute (X δ A N j) y) → Commute (C δ A N s n m) y
  | 0, h => H_comm_of s y m fun j h1 h2 => h j h1 (by omega)
  | n + 1, h => (C_comm_of s m y n fun j h1 h2 => h j h1 (by omega)).mul_left
      (H_comm_of _ y m fun j h1 h2 => h j (by omega) (by omega))

theorem D_comm_D (s n t p : ℕ) (h : s + n + 1 ≤ t) : Commute (D δ A N s n) (D δ A N t p) := by
  induction n generalizing s with
  | zero => exact Commute.one_left _
  | succ n ih =>
    exact (ih (s + 1) (by omega)).mul_left
      (C_comm_of s 0 _ n fun j _ h2 => (D_comm_X p t (by omega)).symm)

theorem pl_D (t M : ℕ) (h : t + M ≤ N) : ∀ (n a : ℕ), a + n ≤ M →
    pl δ t M h (D δ A M a n) = D δ A N (t + a) n
  | 0, a, _ => map_one _
  | n + 1, a, hn => by
    show pl δ t M h (D δ A M (a + 1) n * C δ A M a n 0) = D δ A N (t + a + 1) n * C δ A N (t + a) n 0
    rw [map_mul, pl_D t M h n (a + 1) (by omega), pl_C t M h a 0 n (by omega)]
    rfl

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

variable (δ A N) in
/-- The inverse half twist: `Di s (n+1) = Ci s n 0 · Di (s+1) n`. -/
noncomputable def Di : ℕ → ℕ → TLFin K δ N
  | _, 0 => 1
  | s, n + 1 => Ci δ A N s n 0 * Di (s + 1) n

variable (δ A N) in
/-- The inverse full twist. -/
noncomputable def Θi (s n : ℕ) : TLFin K δ N := Di δ A N s n * Di δ A N s n

include hA hδ in
theorem D_mul_Di : ∀ (n s : ℕ), D δ A N s n * Di δ A N s n = 1
  | 0, s => mul_one 1
  | n + 1, s => by
    show D δ A N (s + 1) n * C δ A N s n 0 * (Ci δ A N s n 0 * Di δ A N (s + 1) n) = 1
    rw [mul_assoc, ← mul_assoc (C δ A N s n 0), C_mul_Ci hA hδ, one_mul, D_mul_Di n (s + 1)]

include hA hδ in
theorem Di_mul_D : ∀ (n s : ℕ), Di δ A N s n * D δ A N s n = 1
  | 0, s => mul_one 1
  | n + 1, s => by
    show Ci δ A N s n 0 * Di δ A N (s + 1) n * (D δ A N (s + 1) n * C δ A N s n 0) = 1
    rw [mul_assoc, ← mul_assoc (Di δ A N (s + 1) n), Di_mul_D n (s + 1), one_mul, Ci_mul_C hA hδ]

include hA hδ in
theorem Θ_mul_Θi (s n : ℕ) : Θ δ A N s n * Θi δ A N s n = 1 := by
  rw [Θ, Θi, mul_assoc, ← mul_assoc (D δ A N s n) (Di δ A N s n), D_mul_Di hA hδ, one_mul,
    D_mul_Di hA hδ]

include hA hδ in
theorem Θi_mul_Θ (s n : ℕ) : Θi δ A N s n * Θ δ A N s n = 1 := by
  rw [Θ, Θi, mul_assoc, ← mul_assoc (Di δ A N s n) (D δ A N s n), Di_mul_D hA hδ, one_mul,
    Di_mul_D hA hδ]

include hA hδ in
/-- **Yang–Baxter for blocks**: `C (s+1) n m · C s (n+m+1) 0 = C s m 0 · C s n (m+1)`. -/
theorem C_yang_baxter (s n m : ℕ) (hN : s + n + m + 1 < N) :
    C δ A N (s + 1) n m * C δ A N s (n + m + 1) 0 = C δ A N s m 0 * C δ A N s n (m + 1) := by
  have h2 := C_hex_right (δ := δ) (A := A) (N := N) s 0 m n
  rw [show 0 + m + 1 = m + 1 by omega, show s + 0 + 1 = s + 1 by omega] at h2
  have hnat := C_mul_pl_right (N := N) hA hδ s n (m + 1) (by omega) (C δ A (m + 1) 0 m 0)
  rw [pl_C _ _ _ 0 0 m (by omega), pl_C _ _ _ 0 0 m (by omega)] at hnat
  simp only [Nat.add_zero] at hnat
  rw [C_hex_left, ← mul_assoc, ← h2, hnat]

include hA hδ in
/-- **The half twist on any split**: `D s (n+m+1) = D s m · D (s+m+1) n · C s n m`. -/
theorem D_split (s n : ℕ) (m : ℕ) (hN : s + n + m + 1 ≤ N) :
    D δ A N s (n + m + 1) = D δ A N s m * D δ A N (s + m + 1) n * C δ A N s n m := by
  induction m generalizing s with
  | zero => show D δ A N (s + 1) n * C δ A N s n 0 = 1 * D δ A N (s + 0 + 1) n * _; simp
  | succ m ih =>
    show D δ A N (s + 1) (n + m + 1) * C δ A N s (n + m + 1) 0 =
      D δ A N (s + 1) m * C δ A N s m 0 * D δ A N (s + (m + 1) + 1) n * C δ A N s n (m + 1)
    have hc : Commute (C δ A N s m 0) (D δ A N (s + (m + 1) + 1) n) :=
      C_comm_of s 0 _ m fun j _ h2 => (D_comm_X n _ (by omega)).symm
    rw [ih (s + 1) (by omega), show s + 1 + m + 1 = s + (m + 1) + 1 by omega,
      mul_assoc (D δ A N (s + 1) m * _), C_yang_baxter hA hδ s n m (by omega),
      mul_assoc (D δ A N (s + 1) m), ← mul_assoc (D δ A N (s + (m + 1) + 1) n), ← hc.eq]
    simp only [mul_assoc]

include hA hδ in
/-- **The half twist reverses its block**: `D s n · e_{s+i} = e_{s+n-1-i} · D s n`. -/
theorem D_mul_E : ∀ (n s : ℕ) {i : ℕ}, i < n → s + n ≤ N →
    D δ A N s n * E δ N (s + i) = E δ N (s + n - 1 - i) * D δ A N s n
  | 0, s, i, hi, _ => absurd hi (Nat.not_lt_zero _)
  | n + 1, s, i, hi, hN => by
    rcases Nat.lt_succ_iff_lt_or_eq.mp hi with hi | hin
    · show D δ A N (s + 1) n * C δ A N s n 0 * E δ N (s + i) =
        E δ N (s + (n + 1) - 1 - i) * (D δ A N (s + 1) n * C δ A N s n 0)
      have h1 := C_mul_E_left (N := N) hA hδ s n 0 hi (by omega)
      have h2 := D_mul_E n (s + 1) hi (by omega)
      rw [show s + 0 + 1 + i = s + 1 + i by omega] at h1
      rw [mul_assoc, h1, ← mul_assoc, h2, mul_assoc, show s + 1 + n - 1 - i = s + (n + 1) - 1 - i by
        omega]
    · rw [hin]
      have hs := D_split (N := N) hA hδ s 0 n (by omega)
      rw [show 0 + n + 1 = n + 1 by omega] at hs
      rw [hs, show D δ A N (s + n + 1) 0 = 1 from rfl, mul_one]
      cases n with
      | zero =>
        simp only [D, C, H, one_mul, Nat.add_zero]
        by_cases h : s < N
        · rw [X_eq h]
          exact ((Commute.one_left _).smul_left _).sub_left ((Commute.refl _).smul_left _)
        · unfold X; rw [dif_neg h, one_mul, mul_one]; simp
      | succ n =>
        have h1 := C_mul_E_right (N := N) hA hδ s 0 (n + 1) (j := n) (by omega) (by omega)
        have h2 := D_mul_E (n + 1) s (i := n) (by omega) (by omega)
        rw [show s + 0 + 1 + n = s + (n + 1) by omega] at h1
        rw [mul_assoc, h1, ← mul_assoc, h2, mul_assoc]
        congr 2; omega

include hA hδ in
/-- **The full twist is central in its block**. -/
theorem Θ_mul_E (n s : ℕ) {i : ℕ} (hi : i < n) (hN : s + n ≤ N) :
    Θ δ A N s n * E δ N (s + i) = E δ N (s + i) * Θ δ A N s n := by
  unfold Θ
  have h1 := D_mul_E (N := N) hA hδ n s hi hN
  have h2 := D_mul_E (N := N) hA hδ n s (i := n - 1 - i) (by omega) hN
  rw [show s + (n - 1 - i) = s + n - 1 - i by omega, show s + n - 1 - (n - 1 - i) = s + i by
    omega] at h2
  rw [mul_assoc, h1, ← mul_assoc, h2, mul_assoc]

theorem Θ_comm_E (n s : ℕ) {j : ℕ} (h : j + 2 ≤ s ∨ s + n + 1 ≤ j) :
    Commute (Θ δ A N s n) (E δ N j) :=
  (D_comm_E n s h).mul_left (D_comm_E n s h)

include hA hδ in
/-- **The balancing identity**:
`Θ s (n+m+1) = Θ s n · Θ (s+n+1) m · C s m n · C s n m`. -/
theorem Θ_balance (s n m : ℕ) (hN : s + n + m + 1 ≤ N) :
    Θ δ A N s (n + m + 1) =
      Θ δ A N s n * Θ δ A N (s + n + 1) m * C δ A N s m n * C δ A N s n m := by
  have hsplit1 := D_split (N := N) hA hδ s m n (by omega)
  have hsplit2 := D_split (N := N) hA hδ s n m hN
  rw [show m + n + 1 = n + m + 1 by omega] at hsplit1
  have hnat_l := C_mul_pl_left (N := N) hA hδ s m n (by omega) (D δ A m 0 m)
  have hnat_r := C_mul_pl_right (N := N) hA hδ s m n (by omega) (D δ A n 0 n)
  rw [pl_D s m _ m 0 (by omega), pl_D (s + n + 1) m _ m 0 (by omega)] at hnat_l
  rw [pl_D (s + m + 1) n _ n 0 (by omega), pl_D s n _ n 0 (by omega)] at hnat_r
  simp only [Nat.add_zero] at hnat_l hnat_r
  have hc : Commute (D δ A N s n) (D δ A N (s + n + 1) m) := D_comm_D s n _ m le_rfl
  unfold Θ
  nth_rewrite 2 [hsplit2]
  rw [hsplit1]
  -- `D s n · D' · C s m n · (D s m · D (s+m+1) n · C s n m)`
  rw [show D δ A N s n * D δ A N (s + n + 1) m * C δ A N s m n *
      (D δ A N s m * D δ A N (s + m + 1) n * C δ A N s n m) =
      D δ A N s n * D δ A N (s + n + 1) m * ((C δ A N s m n * D δ A N s m) *
        D δ A N (s + m + 1) n) * C δ A N s n m by simp only [mul_assoc]]
  rw [hnat_l, mul_assoc (D δ A N (s + n + 1) m), hnat_r]
  rw [show D δ A N s n * D δ A N (s + n + 1) m *
      (D δ A N (s + n + 1) m * (D δ A N s n * C δ A N s m n)) * C δ A N s n m =
      D δ A N s n * (D δ A N (s + n + 1) m * D δ A N (s + n + 1) m * D δ A N s n) *
        C δ A N s m n * C δ A N s n m by simp only [mul_assoc]]
  rw [show D δ A N (s + n + 1) m * D δ A N (s + n + 1) m * D δ A N s n =
      D δ A N s n * (D δ A N (s + n + 1) m * D δ A N (s + n + 1) m) by
    rw [mul_assoc, ← hc.eq, ← mul_assoc, ← mul_assoc, hc.eq, mul_assoc]]
  simp only [mul_assoc]

end Twist

/-! ## A cap is unaffected by winding around a block (ribbon compatibility) -/

section Cap

variable {N : ℕ} (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

include hA hδ in
/-- A crossing absorbed by its own cap: `σᵢ eᵢ = −A⁻³ eᵢ`. -/
theorem X_mul_E_self {i : ℕ} (h : i < N) : X δ A N i * E δ N i = (-(A⁻¹ ^ 3)) • E δ N i := by
  rw [X_eq h, sub_mul, smul_mul_assoc, one_mul, smul_mul_assoc, E_of_lt h, e_sq', smul_smul,
    ← sub_smul, hδ]
  congr 1
  field_simp
  ring

include hA hδ in
/-- **A cap slides off a double crossing**: `e_{i+1} σᵢσᵢ₊₁σᵢ₊₁σᵢ = e_{i+1}`. -/
theorem E_mul_loop {i : ℕ} (h : i + 1 < N) :
    E δ N (i + 1) * (X δ A N i * X δ A N (i + 1) * (X δ A N (i + 1) * X δ A N i)) =
      E δ N (i + 1) := by
  rw [X_eq (by omega : i < N), X_eq h]
  rw [E_of_lt (by omega : i < N), E_of_lt h]
  set a := e K δ adjFin (⟨i, by omega⟩ : Fin N)
  set b := e K δ adjFin (⟨i + 1, h⟩ : Fin N)
  have haa : a * a = δ • a := e_sq' δ _
  have hbb : b * b = δ • b := e_sq' δ _
  have hbab : b * (a * b) = b := by rw [← mul_assoc]; exact e_adjacent_fin (Or.inr rfl)
  have haba : a * (b * a) = a := by rw [← mul_assoc]; exact e_adjacent_fin (Or.inl rfl)
  -- cap slides: `b σᵢσᵢ₊₁ = −b a` and `a σᵢ₊₁σᵢ = −a b`
  have h1 : b * ((A • 1 - A⁻¹ • a) * (A • 1 - A⁻¹ • b)) = -(b * a) := by
    simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
      ← mul_assoc, hbb]
    rw [mul_assoc b a b, hbab]
    match_scalars <;> (try simp only [hδ]) <;> (field_simp; try ring)
  have h2 : a * ((A • 1 - A⁻¹ • b) * (A • 1 - A⁻¹ • a)) = -(a * b) := by
    simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
      ← mul_assoc, haa]
    rw [mul_assoc a b a, haba]
    match_scalars <;> (try simp only [hδ]) <;> (field_simp; try ring)
  calc b * ((A • 1 - A⁻¹ • a) * (A • 1 - A⁻¹ • b) * ((A • 1 - A⁻¹ • b) * (A • 1 - A⁻¹ • a)))
      = (b * ((A • 1 - A⁻¹ • a) * (A • 1 - A⁻¹ • b))) *
          ((A • 1 - A⁻¹ • b) * (A • 1 - A⁻¹ • a)) := by simp only [mul_assoc]
    _ = -(b * (a * ((A • 1 - A⁻¹ • b) * (A • 1 - A⁻¹ • a)))) := by
          rw [h1, neg_mul, mul_assoc]
    _ = b := by rw [h2, mul_neg, neg_neg, hbab]

include hA hδ in
/-- **A cap on `[s+n+1, s+n+2]` is unaffected by the block `[s, s+n]` winding around it**:
`C s 1 n · C s n 1 · e_{s+n+1} = e_{s+n+1}`. -/
theorem wind_mul_E (s : ℕ) : ∀ n, s + n + 2 < N + 1 →
    C δ A N s 1 n * C δ A N s n 1 * E δ N (s + n + 1) = E δ N (s + n + 1)
  | 0, hN => by
    show H δ A N s 0 * H δ A N (s + 0 + 1) 0 * H δ A N s 1 * E δ N (s + 0 + 1) = _
    simp only [H, Nat.add_zero]
    have hd := XX_mul_E_down (N := N) hA hδ (i := s) (by omega)
    have hu := XX_mul_E_up (N := N) hA hδ (i := s) (by omega)
    rw [mul_assoc, hd, ← mul_assoc, hu, mul_assoc, E_mul_loop hA hδ (by omega)]
  | n + 1, hN => by
    have hl := C_hex_left (δ := δ) (A := A) (N := N) s n 1 0
    have hr := C_hex_right (δ := δ) (A := A) (N := N) s n 0 1
    simp only [Nat.add_zero] at hl hr
    rw [hl, hr]
    set t := s + n + 1
    have hZ := C_mul_E_right (N := N) hA hδ t 0 1 (j := 0) (by omega) (by omega)
    have ih := wind_mul_E s n (by omega)
    simp only [Nat.add_zero] at hZ
    rw [show s + (n + 1) + 1 = t + 0 + 1 + 0 by omega]
    rw [show C δ A N t 1 0 * C δ A N s 1 n * (C δ A N s n 1 * C δ A N t 0 1) * E δ N (t + 0 + 1 + 0) =
      C δ A N t 1 0 * (C δ A N s 1 n * C δ A N s n 1) * (C δ A N t 0 1 * E δ N (t + 0 + 1 + 0)) by
        simp only [mul_assoc]]
    simp only [Nat.add_zero] at *
    rw [hZ, ← mul_assoc, mul_assoc (C δ A N t 1 0), ih]
    show H δ A N t 0 * H δ A N (t + 0 + 1) 0 * E δ N t * H δ A N t 1 = E δ N (t + 1)
    simp only [H, Nat.add_zero]
    rw [XX_mul_E_up hA hδ (by omega), mul_assoc, E_mul_loop hA hδ (by omega)]

end Cap

/-! ## The twist on the Jones–Wenzl projector -/

section JW

variable {n : ℕ}

/-- `tri k = k (k + 1) / 2`, the length of the half twist. -/
def tri : ℕ → ℕ
  | 0 => 0
  | k + 1 => tri k + (k + 1)

theorem two_mul_tri : ∀ k, 2 * tri k = k * (k + 1)
  | 0 => rfl
  | k + 1 => by rw [tri, mul_add, two_mul_tri k]; ring

variable (hS : JWSpec δ n)
include hS

theorem jw_mul_X {i : ℕ} (hi : i < n) : jw δ n * X δ A n i = A • jw δ n := by
  rw [X_of_lt hi, jw_mul_crossing hS]

theorem jw_mul_H (a : ℕ) : ∀ m, a + m < n → jw δ n * H δ A n a m = A ^ (m + 1) • jw δ n
  | 0, h => by rw [zero_add, pow_one]; exact jw_mul_X hS (by omega)
  | m + 1, h => by
    show jw δ n * (X δ A n (a + m + 1) * H δ A n a m) = _
    rw [← mul_assoc, jw_mul_X hS (by omega), smul_mul_assoc, jw_mul_H a m (by omega), smul_smul,
      pow_succ' A (m + 1)]

theorem jw_mul_C (a m : ℕ) : ∀ k, a + k + m < n →
    jw δ n * C δ A n a k m = A ^ ((k + 1) * (m + 1)) • jw δ n
  | 0, h => by rw [zero_add, one_mul]; exact jw_mul_H hS a m (by omega)
  | k + 1, h => by
    show jw δ n * (C δ A n a k m * H δ A n (a + k + 1) m) = _
    rw [← mul_assoc, jw_mul_C a m k (by omega), smul_mul_assoc, jw_mul_H hS _ m (by omega),
      smul_smul, ← pow_add]
    congr 1; ring

theorem jw_mul_D : ∀ (k a : ℕ), a + k ≤ n → jw δ n * D δ A n a k = A ^ tri k • jw δ n
  | 0, a, _ => by simp [D, tri]
  | k + 1, a, h => by
    show jw δ n * (D δ A n (a + 1) k * C δ A n a k 0) = _
    rw [← mul_assoc, jw_mul_D k (a + 1) (by omega), smul_mul_assoc, jw_mul_C hS a 0 k (by omega),
      smul_smul, ← pow_add, tri]
    congr 1; ring

/-- **The full twist acts on `p_n` by `A^{n(n+1)}`**, as `fullTwist` does. -/
theorem jw_mul_Θ : jw δ n * Θ δ A n 0 n = A ^ (n * (n + 1)) • jw δ n := by
  rw [Θ, ← mul_assoc, jw_mul_D hS n 0 (by omega), smul_mul_assoc, jw_mul_D hS n 0 (by omega),
    smul_smul, ← pow_add, ← two_mul_tri, two_mul]

end JW

end QOU.HeckeTemperleyLieb.TLCableBraiding
