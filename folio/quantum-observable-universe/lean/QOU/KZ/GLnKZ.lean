import QOU.KZ.GLnResidues
import QOU.KZ.KZPentagon
import QOU.KZ.KZHexagon
import QOU.KZ.KZShiftPhi
import Mathlib.Analysis.Matrix

/-!
# The KZ pentagon and hexagon for `𝔤𝔩_n` on `V^{⊗3}`, `V^{⊗4}`, `V = ℂⁿ`

Stage S1 of bean `qou-zoyv` (the Drinfeld category `D_ℏ`).

For `𝔤𝔩_n` with the trace form the split Casimir on legs `i, j` of `V^{⊗m}` is the flip `P_{ij}`
(`FuchsianFormal.casimir_eq_flip` for `m = 2`), so the KZ residues are `t_{ij} = ℏ P_{ij}`.
This file proves, for these concrete residues:

* the infinitesimal pure-braid relations `KZ4.Res.Rel` (`kzRes_rel`);
* non-resonance of every boundary residue `ℏ P_{ij}`, `T₁₂₃ = ℏ(P₁₂ + P₁₃ + P₂₃)`,
  `T₂₃₄`, and of `−ℏ(P₁₂ + P₂₃)`, whenever `ℏ ∉ ℚ` (via `GLnResidues.nonResonant_of_int_roots`:
  `S = P₁₂ + P₁₃ + P₂₃` satisfies `S³ = 9S`, `Q = P₁₂ + P₂₃` satisfies `(Q² − 1)(Q² − 4) = 0`);
* hence the **pentagon** (`pentagon_gln`) and the **hexagon** (`hexagon_gln`) for the concrete
  KZ associator `Φ_KZ` in the Banach algebra of matrices (operator `ℓ^∞` norm), as instances of
  `KZPentagon.pentagon` and `KZHexagon.hexagon`.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S1)
-/

namespace QOU.KZ.GLnKZ

open Polynomial QOU.KZ.FuchsianFormal QOU.KZ.GLnResidues QOU.KZ.KZ4

section NonResonance

variable {K R : Type*} [Field K] [CharZero K] [Ring R] [Algebra K R]

/-- `c (a + b + c')` is non-resonant for three involutions with the `S₃` conjugation relations,
whenever `c ∉ ℚ`. -/
theorem nonResonant_smul_sum_three (a b c' : R) (ha : a * a = 1) (hb : b * b = 1)
    (hc' : c' * c' = 1) (h1 : a * b = b * c') (h2 : b * c' = c' * a) (h3 : a * c' = c' * b)
    (h4 : c' * b = b * a) (c : K) (hc : ∀ r : ℚ, (r : K) ≠ c) :
    NonResonant (c • (a + b + c')) := by
  refine nonResonant_of_int_roots (ι := Fin 3) ![0, 3, -3] c hc _
    (aeval_smul_of_roots (fun i => ((![0, 3, -3] : Fin 3 → ℤ) i : K)) c _ ?_)
  have hcube := sum_three_cube a b c' ha hb hc' h1 h2 h3 h4
  set S := a + b + c'
  simp only [Fin.prod_univ_three, map_mul, map_sub, aeval_X, aeval_C]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.head_cons,
    Matrix.tail_cons, Int.cast_zero, Int.cast_ofNat, Int.cast_neg, map_zero, map_neg, map_ofNat,
    sub_zero, sub_neg_eq_add]
  have e : S * (S - 3) * (S + 3) = S * S * S - 9 • S := by
    rw [nsmul_eq_mul]; noncomm_ring; simp [zsmul_eq_mul]
  rw [e, hcube, sub_self]

/-- `c (a + b)` is non-resonant for two involutions with `aba = bab`, whenever `c ∉ ℚ`. -/
theorem nonResonant_smul_sum_two (a b : R) (ha : a * a = 1) (hb : b * b = 1)
    (hab : a * b * a = b * a * b) (c : K) (hc : ∀ r : ℚ, (r : K) ≠ c) :
    NonResonant (c • (a + b)) := by
  refine nonResonant_of_int_roots (ι := Fin 4) ![1, -1, 2, -2] c hc _
    (aeval_smul_of_roots (fun i => ((![1, -1, 2, -2] : Fin 4 → ℤ) i : K)) c _ ?_)
  have hq := sum_two_quartic a b ha hb hab
  set Q := a + b
  simp only [Fin.prod_univ_four, map_mul, map_sub, aeval_X, aeval_C]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three,
    Matrix.head_cons, Matrix.tail_cons, Int.cast_one, Int.cast_ofNat, Int.cast_neg, map_one,
    map_neg, map_ofNat, sub_neg_eq_add]
  have e : (Q - 1) * (Q + 1) * (Q - 2) * (Q + 2) =
      Q * Q * (Q * Q) + 4 • 1 - 5 • (Q * Q) := by
    simp only [nsmul_eq_mul, mul_one]; noncomm_ring; simp [zsmul_eq_mul]; abel
  rw [e, hq, sub_self]

end NonResonance

/-! ### The concrete residues -/

section Concrete

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable (n : ℕ)

/-- `End(V^{⊗m})`, `V = ℂⁿ`, as matrices indexed by `Fin m → Fin n`. -/
abbrev Mat (m : ℕ) := Matrix (Fin m → Fin n) (Fin m → Fin n) ℂ

/-- The flip `P_{ij}` on `V^{⊗m}` over `ℂ`. -/
noncomputable abbrev P {m : ℕ} (i j : Fin m) : Mat n m := flipP ℂ n i j

/-- Relations among flips: the equality of two products of flips reduces to an equality of
permutations. -/
theorem P_mul_P {m : ℕ} (i j k l : Fin m) :
    P n i j * P n k l = permP ℂ n (Equiv.swap k l * Equiv.swap i j) :=
  permP_mul ℂ n _ _

/-- The residues are the split Casimir tensors: `ℏ t_{ij} = ℏ P_{ij}` for `i ≠ j`. -/
theorem smul_casimirLeg {m : ℕ} {i j : Fin m} (hij : i ≠ j) (c : ℂ) :
    c • casimirLeg ℂ n i j = c • P n i j := by
  rw [casimirLeg_eq_flipP ℂ n hij]

/-- The four-point `𝔤𝔩_n` KZ residues `t_{ij} = ℏ P_{ij}`. -/
noncomputable def kzRes (c : ℂ) : Res (Mat n 4) where
  t12 := c • P n 0 1
  t13 := c • P n 0 2
  t23 := c • P n 1 2
  t24 := c • P n 1 3
  t34 := c • P n 2 3

/-- `[P_{ij}, P_{kl}] = 0` from an equality of permutations. -/
theorem commute_P {m : ℕ} {i j k l : Fin m}
    (h : Equiv.swap k l * Equiv.swap i j = Equiv.swap i j * Equiv.swap k l) :
    Commute (P n i j) (P n k l) := by
  show P n i j * P n k l = P n k l * P n i j
  rw [P_mul_P, P_mul_P, h]

/-- `[P_{ij}, P_{kl} + P_{k'l'}] = 0` when conjugation by `(ij)` swaps `(kl)` and `(k'l')`. -/
theorem commute_P_add {m : ℕ} {i j k l k' l' : Fin m}
    (h1 : Equiv.swap k l * Equiv.swap i j = Equiv.swap i j * Equiv.swap k' l')
    (h2 : Equiv.swap k' l' * Equiv.swap i j = Equiv.swap i j * Equiv.swap k l) :
    Commute (P n i j) (P n k l + P n k' l') := by
  show P n i j * (P n k l + P n k' l') = (P n k l + P n k' l') * P n i j
  rw [mul_add, add_mul, P_mul_P, P_mul_P, P_mul_P, P_mul_P, h1, h2, add_comm]

/-- **The infinitesimal pure-braid relations** for `t_{ij} = ℏ P_{ij}`. -/
theorem kzRes_rel (c : ℂ) : (kzRes n c).Rel where
  r1 := ((commute_P n (by decide)).smul_left c).smul_right c
  r2 := ((commute_P n (by decide)).smul_left c).smul_right c
  r3 := by
    show Commute (c • P n 0 1) (c • P n 0 2 + c • P n 1 2)
    rw [← smul_add]; exact ((commute_P_add n (by decide) (by decide)).smul_left c).smul_right c
  r4 := by
    show Commute (c • P n 1 2) (c • P n 0 1 + c • P n 0 2)
    rw [← smul_add]; exact ((commute_P_add n (by decide) (by decide)).smul_left c).smul_right c
  r5 := by
    show Commute (c • P n 1 2) (c • P n 1 3 + c • P n 2 3)
    rw [← smul_add]; exact ((commute_P_add n (by decide) (by decide)).smul_left c).smul_right c
  r6 := by
    show Commute (c • P n 1 3) (c • P n 1 2 + c • P n 2 3)
    rw [← smul_add]; exact ((commute_P_add n (by decide) (by decide)).smul_left c).smul_right c

variable {n}

theorem P_mul_self {m : ℕ} (i j : Fin m) : P n i j * P n i j = 1 := flipP_mul_self ℂ n i j

/-- Non-resonance of a single residue `ℏ P_{ij}`. -/
theorem nonResonant_smul_P {m : ℕ} (i j : Fin m) {c : ℂ} (hc : ∀ r : ℚ, (r : ℂ) ≠ c) :
    NonResonant (c • P n i j) :=
  nonResonant_smul_involution_of_irrational (K := ℂ) _ (P_mul_self i j) c hc

theorem nonResonant_T123 {c : ℂ} (hc : ∀ r : ℚ, (r : ℂ) ≠ c) :
    NonResonant (kzRes n c).T123 := by
  have : (kzRes n c).T123 = c • (P n 0 1 + P n 0 2 + P n 1 2) := by
    simp only [Res.T123, kzRes, smul_add]
  rw [this]
  refine nonResonant_smul_sum_three _ _ _ (P_mul_self _ _) (P_mul_self _ _) (P_mul_self _ _)
    ?_ ?_ ?_ ?_ c hc <;> (rw [P_mul_P, P_mul_P]; congr 1; decide)

theorem nonResonant_T234 {c : ℂ} (hc : ∀ r : ℚ, (r : ℂ) ≠ c) :
    NonResonant (kzRes n c).T234 := by
  have : (kzRes n c).T234 = c • (P n 1 2 + P n 1 3 + P n 2 3) := by
    simp only [Res.T234, kzRes, smul_add]
  rw [this]
  refine nonResonant_smul_sum_three _ _ _ (P_mul_self _ _) (P_mul_self _ _) (P_mul_self _ _)
    ?_ ?_ ?_ ?_ c hc <;> (rw [P_mul_P, P_mul_P]; congr 1; decide)

/-! ### Pentagon and hexagon in the Banach algebra of matrices -/

section Analytic

variable {n : ℕ} {c : ℂ}

/-- **The KZ pentagon for `𝔤𝔩_n` on `V^{⊗4}`.** For `ℏ ∉ ℚ` and `t_{ij} = ℏ P_{ij}`,
`Φ(T₂₃₄, t₁₂) Φ(t₂₃, t₃₄) Φ(T₁₂₃, T₂₃₄) Φ(t₁₂, t₂₃) Φ(t₃₄, T₁₂₃) = 1`. -/
theorem pentagon_gln (hc : ∀ r : ℚ, (r : ℂ) ≠ c) :
    KZPentagon.Φ (kzRes n c).T234 (kzRes n c).t12 (nonResonant_T234 hc)
        (nonResonant_smul_P 0 1 hc) *
      KZPentagon.Φ (kzRes n c).t23 (kzRes n c).t34 (nonResonant_smul_P 1 2 hc)
        (nonResonant_smul_P 2 3 hc) *
      KZPentagon.Φ (kzRes n c).T123 (kzRes n c).T234 (nonResonant_T123 hc)
        (nonResonant_T234 hc) *
      KZPentagon.Φ (kzRes n c).t12 (kzRes n c).t23 (nonResonant_smul_P 0 1 hc)
        (nonResonant_smul_P 1 2 hc) *
      KZPentagon.Φ (kzRes n c).t34 (kzRes n c).T123 (nonResonant_smul_P 2 3 hc)
        (nonResonant_T123 hc) = 1 :=
  KZPentagon.pentagon _ (kzRes_rel n c) _ _ _ _ _

/-- The three-point residues `A = ℏ P₁₂`, `B = ℏ P₂₃` and `C = −A − B` on `V^{⊗3}`. -/
theorem nonResonant_C (hc : ∀ r : ℚ, (r : ℂ) ≠ c) :
    NonResonant (-(c • P n (0 : Fin 3) 1) - c • P n 1 2) := by
  have : -(c • P n (0 : Fin 3) 1) - c • P n 1 2 = (-c) • (P n 0 1 + P n 1 2) := by
    rw [neg_smul, smul_add]; abel
  rw [this]
  refine nonResonant_smul_sum_two _ _ (P_mul_self _ _) (P_mul_self _ _) ?_ (-c) ?_
  · simp only [P, flipP, permP_mul]; congr 1; decide
  · intro r hr; exact hc (-r) (by push_cast; rw [hr, neg_neg])

/-- **The KZ hexagon for `𝔤𝔩_n` on `V^{⊗3}`.** For `ℏ ∉ ℚ`, `A = ℏ P₁₂`, `B = ℏ P₂₃`,
`C = −A − B`: `e^{−iπA} Φ(C,A) e^{−iπC} Φ(B,C) e^{−iπB} Φ(A,B) = 1`. -/
theorem hexagon_gln (hc : ∀ r : ℚ, (r : ℂ) ≠ c) :
    KZHexagon.eπ (c • P n (0 : Fin 3) 1) *
      KZPentagon.Φ _ _ (nonResonant_C hc) (nonResonant_smul_P 0 1 hc) *
      KZHexagon.eπ (-(c • P n (0 : Fin 3) 1) - c • P n 1 2) *
      KZPentagon.Φ _ _ (nonResonant_smul_P 1 2 hc) (nonResonant_C hc) *
      KZHexagon.eπ (c • P n (1 : Fin 3) 2) *
      KZPentagon.Φ _ _ (nonResonant_smul_P 0 1 hc) (nonResonant_smul_P 1 2 hc) = 1 := by
  have hA := nonResonant_smul_P (n := n) (0 : Fin 3) 1 hc
  have hB := nonResonant_smul_P (n := n) (1 : Fin 3) 2 hc
  have hC := nonResonant_C (n := n) hc
  exact KZHexagon.hexagon _ _ (fun k hk => (hA k hk).1) (fun k hk => (hB k hk).1)
    (fun k hk => (hC k hk).1) _ _ _ _ _ _
    (KZPentagon.H0_zero _ _ hA) (KZPentagon.H0_gauge _ _ hA)
    (KZPentagon.H0_zero _ _ hB) (KZPentagon.H0_gauge _ _ hB)
    (KZPentagon.H0_zero _ _ hB) (KZPentagon.H0_gauge _ _ hB)
    (KZPentagon.H0_zero _ _ hC) (KZPentagon.H0_gauge _ _ hC)
    (KZPentagon.H0_zero _ _ hC) (KZPentagon.H0_gauge _ _ hC)
    (KZPentagon.H0_zero _ _ hA) (KZPentagon.H0_gauge _ _ hA)

/-- Non-resonance of `ℏ (P_{ij} + P_{kl})` for two flips satisfying the braid relation. -/
theorem nonResonant_smul_P_add {m : ℕ} {i j k l : Fin m}
    (hb : Equiv.swap i j * (Equiv.swap k l * Equiv.swap i j) =
      Equiv.swap k l * (Equiv.swap i j * Equiv.swap k l))
    (hc : ∀ r : ℚ, (r : ℂ) ≠ c) : NonResonant (c • P n i j + c • P n k l) := by
  rw [← smul_add]
  refine nonResonant_smul_sum_two _ _ (P_mul_self _ _) (P_mul_self _ _) ?_ c hc
  simp only [P, flipP, permP_mul]; congr 1

/-- **The KZ pentagon for `𝔤𝔩_n` in Drinfeld's coproduct form**, on `V^{⊗4}`, `ℏ ∉ ℚ`:
`Φ^{234} Φ^{1,23,4} Φ^{123} = Φ^{1,2,34} Φ^{12,3,4}`. -/
theorem pentagon_drinfeld_gln (hc : ∀ r : ℚ, (r : ℂ) ≠ c) :
    KZPentagon.Φ (kzRes n c).t23 (kzRes n c).t34 (nonResonant_smul_P 1 2 hc)
        (nonResonant_smul_P 2 3 hc) *
      KZPentagon.Φ ((kzRes n c).t12 + (kzRes n c).t13) ((kzRes n c).t24 + (kzRes n c).t34)
        (nonResonant_smul_P_add (by decide) hc) (nonResonant_smul_P_add (by decide) hc) *
      KZPentagon.Φ (kzRes n c).t12 (kzRes n c).t23 (nonResonant_smul_P 0 1 hc)
        (nonResonant_smul_P 1 2 hc) =
    KZPentagon.Φ (kzRes n c).t12 ((kzRes n c).t23 + (kzRes n c).t24)
        (nonResonant_smul_P 0 1 hc) (nonResonant_smul_P_add (by decide) hc) *
      KZPentagon.Φ ((kzRes n c).t13 + (kzRes n c).t23) (kzRes n c).t34
        (nonResonant_smul_P_add (by decide) hc) (nonResonant_smul_P 2 3 hc) :=
  KZShiftPhi.pentagon_drinfeld _ (kzRes_rel n c) _ _ _ (nonResonant_T123 hc)
    (nonResonant_T234 hc) _ _ _ _

end Analytic

end Concrete

end QOU.KZ.GLnKZ
