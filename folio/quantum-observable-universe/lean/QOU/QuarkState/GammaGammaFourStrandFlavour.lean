/-
# Strand-1–3 γγ vertices fix the `Ja` flavour line; two strand-4 words keep `J₄` flavour

Bean `qou-a1hh` / `qou-wkcd`. Uses the explicit `(3,1)` representation of `H₄(q)` and the
`J₄` flavour projectors `Ja`, `Jb` of `FlavourDoubletFourStrands.lean` (PR #7957).

γγ vertices (sites 0-indexed): `V₀ = σ₁σ₂⁻¹`, `V̄₀ = σ₁⁻¹σ₂`, `V₁ = σ₂σ₃⁻¹`, `V̄₁ = σ₂⁻¹σ₃`.

Results, for every field `K` and every `q` with `q ≠ 0`, `q² + 1 ≠ 0`, `q⁴ + q² + 1 ≠ 0`:
* `Ja` is the `(3)` (trivial) sector of `H₃` on the left doublet: `σ₁, σ₂` act on it by `q`
  from both sides (`s1_Ja` … `Ja_s2`). Hence **every site-0 γγ vertex acts as the identity
  on `Ja`**: `V₀ Ja = Ja = Ja V₀`, same for `V̄₀` (`V0_Ja` … `Ja_B0`).
* The two six-vertex words `w₁ = V₁V̄₀V₀V̄₀V̄₁V₁` and `w₂ = V̄₁V₀V̄₀V₀V₁V̄₁` use the strand-4
  site yet **commute with `J₄`** (`word1_comm_J4`, `word2_comm_J4`), fix `Ja` from both sides,
  and mix neither flavour into the other (`word1_no_mix` …).

So reaching strand 4 is necessary for a `J₄`-flavour change (PR #7957,
`three_strand_word_no_mix`) but **not sufficient**.

Scope: model statements about `H₄(q)`; no empirical number, no physical identification.
"`J₄` flavour" here only names the `H₃` isotypic label of the left doublet (`Ja` = `(3)`,
`Jb` = `(2,1)`), i.e. three-strand isospin 3/2 vs 1/2 under Schur–Weyl. It is **not** the
`n ↔ p` label: Hecke elements commute with the `U_q` action and cannot change `T³`
(PR #7975, beans `qou-wkcd` / `qou-0whz`).
No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [humphreys1990] §7.4 (Hecke algebra, generic q)
-/
import QOU.QuarkState.FlavourDoubletFourStrands

namespace QOU.QuarkState.GammaGammaFourStrand

open Matrix QOU.QuarkState.FlavourDoubletFour

local macro "mat3" : tactic =>
  `(tactic| ((try simp only [Matrix.mul_fin_three, Matrix.one_fin_three, Matrix.smul_of,
      Matrix.smul_vec3, Matrix.of_sub_of, Matrix.of_add_of]) <;> ext i j <;>
    fin_cases i <;> fin_cases j <;> (try simp) <;> (try field_simp) <;> (try ring) <;> (try simp)))

variable {K : Type*} [Field K]

/-- Site-0 γγ vertex `V₀ = σ₁σ₂⁻¹`. -/
def V0 (q : K) : Matrix (Fin 3) (Fin 3) K := s1 q * s2i q
/-- Its mirror `V̄₀ = σ₁⁻¹σ₂`. -/
def B0 (q : K) : Matrix (Fin 3) (Fin 3) K := s1i q * s2 q
/-- Site-1 γγ vertex `V₁ = σ₂σ₃⁻¹` (reaches strand 4). -/
def V1 (q : K) : Matrix (Fin 3) (Fin 3) K := s2 q * s3i q
/-- Its mirror `V̄₁ = σ₂⁻¹σ₃`. -/
def B1 (q : K) : Matrix (Fin 3) (Fin 3) K := s2i q * s3 q

/-- `w₁ = V₁V̄₀V₀V̄₀V̄₁V₁`. -/
def word1 (q : K) : Matrix (Fin 3) (Fin 3) K := V1 q * B0 q * V0 q * B0 q * B1 q * V1 q
/-- `w₂ = V̄₁V₀V̄₀V₀V₁V̄₁`. -/
def word2 (q : K) : Matrix (Fin 3) (Fin 3) K := B1 q * V0 q * B0 q * V0 q * V1 q * B1 q

section
variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0) (hD : q ^ 4 + q ^ 2 + 1 ≠ 0)
include hq hn hD

theorem s1_Ja : s1 q * Ja q = q • Ja q := by unfold s1 Ja; mat3
theorem s2_Ja : s2 q * Ja q = q • Ja q := by unfold s2 Ja; mat3
theorem Ja_s1 : Ja q * s1 q = q • Ja q := by unfold s1 Ja; mat3
theorem Ja_s2 : Ja q * s2 q = q • Ja q := by unfold s2 Ja; mat3
theorem s1i_Ja : s1i q * Ja q = q⁻¹ • Ja q := by unfold s1i Ja; mat3
theorem s2i_Ja : s2i q * Ja q = q⁻¹ • Ja q := by unfold s2i Ja; mat3
theorem Ja_s1i : Ja q * s1i q = q⁻¹ • Ja q := by unfold s1i Ja; mat3
theorem Ja_s2i : Ja q * s2i q = q⁻¹ • Ja q := by unfold s2i Ja; mat3

private theorem cancel (M : Matrix (Fin 3) (Fin 3) K) : q • q⁻¹ • M = M := by
  rw [smul_smul, mul_inv_cancel₀ hq, one_smul]
private theorem cancel' (M : Matrix (Fin 3) (Fin 3) K) : q⁻¹ • q • M = M := by
  rw [smul_smul, inv_mul_cancel₀ hq, one_smul]

/-- **A site-0 γγ vertex acts as the identity on `Ja`** (left action). -/
theorem V0_Ja : V0 q * Ja q = Ja q := by
  unfold V0; rw [mul_assoc, s2i_Ja hq hn hD, Matrix.mul_smul, s1_Ja hq hn hD, cancel' hq hn hD]
theorem B0_Ja : B0 q * Ja q = Ja q := by
  unfold B0; rw [mul_assoc, s2_Ja hq hn hD, Matrix.mul_smul, s1i_Ja hq hn hD, cancel hq hn hD]
/-- **A site-0 γγ vertex acts as the identity on `Ja`** (right action). -/
theorem Ja_V0 : Ja q * V0 q = Ja q := by
  unfold V0; rw [← mul_assoc, Ja_s1 hq hn hD, Matrix.smul_mul, Ja_s2i hq hn hD, cancel hq hn hD]
theorem Ja_B0 : Ja q * B0 q = Ja q := by
  unfold B0; rw [← mul_assoc, Ja_s1i hq hn hD, Matrix.smul_mul, Ja_s2 hq hn hD, cancel' hq hn hD]

theorem V0_eq : V0 q =
    !![(-q^4 + q^2) / (q^2 + 1), (-q^4 - 1) / (q^2 + 1), (q^6 + q^2) / (q^2 + 1);
     (-q^2) / (q^2 + 1), (1) / (q^2 + 1), (q^4) / (q^2 + 1);
     (-1) / (q^2*(q^2 + 1)), (-1) / (q^2*(q^2 + 1)), (-1) / (q^2*(q^2 + 1))] := by
  unfold V0 s1 s2i; mat3

theorem B0_eq : B0 q =
    !![(q^2 - 1) / (q^2*(q^2 + 1)), (-q^4 - 1) / (q^2*(q^2 + 1)), (q^4 + 1) / (q^2 + 1);
     (-1) / (q^2 + 1), (q^2) / (q^2 + 1), (q^2) / (q^2 + 1);
     (-1) / (q^2 + 1), (-1) / (q^2 + 1), (-q^4) / (q^2 + 1)] := by
  unfold B0 s1i s2; mat3

theorem V1_eq : V1 q =
    !![(q^2 - 1) / (q^2*(q^2 + 1)), (q^4 + 1) / (q^2 + 1), (q^4 + 1) / (q^2 + 1);
     (-1) / (q^2 + 1), (-q^4) / (q^2 + 1), (q^2) / (q^2 + 1);
     (1) / (q^2*(q^2 + 1)), (-1) / (q^2 + 1), (q^2) / (q^2 + 1)] := by
  unfold V1 s2 s3i; mat3

theorem B1_eq : B1 q =
    !![(-q^4 + q^2) / (q^2 + 1), (q^4 + 1) / (q^2*(q^2 + 1)), (q^6 + q^2) / (q^2 + 1);
     (-q^2) / (q^2 + 1), (-1) / (q^2*(q^2 + 1)), (q^4) / (q^2 + 1);
     (1) / (q^2 + 1), (-1) / (q^2*(q^2 + 1)), (1) / (q^2 + 1)] := by
  unfold B1 s2i s3; mat3

theorem word1_p2 : V1 q * B0 q =
    !![(-2*q^6 + 2*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1)), (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^8 + 2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1));
     (q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-q^6 + q^4 - q^2 + 1) / (q^2*(q^2 + 1)), (-2*q^4 + q^2 - 1) / (q^2 + 1);
     (-q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (-2*q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (-q^6 + q^4 - q^2 + 1) / (q^2*(q^2 + 1))] := by
  rw [V1_eq hq hn hD, B0_eq hq hn hD]; mat3

theorem word1_p3 : V1 q * B0 q * V0 q =
    !![(q^8 - 2*q^6 + 3*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1)), (2*q^8 - 2*q^6 + 3*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^10 + q^8 - 3*q^6 + 2*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1));
     (2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-q^6 + 2*q^4 - q^2 + 1) / (q^2*(q^2 + 1)), (-q^6 + 2*q^4 - q^2 + 1) / (q^2*(q^2 + 1));
     (q^6 - q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (q^6 - 2*q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (-q^8 + q^6 - q^4 + q^2 - 1) / (q^4*(q^2 + 1))] := by
  rw [word1_p2 hq hn hD, V0_eq hq hn hD]; mat3

theorem word1_p4 : V1 q * B0 q * V0 q * B0 q =
    !![(q^10 - 3*q^8 + 5*q^6 - 5*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (2*q^10 - 3*q^8 + 5*q^6 - 4*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (q^12 - q^10 + 4*q^8 - 4*q^6 + 4*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1));
     (2*q^6 - 4*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (-q^8 + 2*q^6 - 3*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (q^8 - 2*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1));
     (q^8 - 2*q^6 + 3*q^4 - 2*q^2 + 1) / (q^6*(q^2 + 1)), (q^8 - 3*q^6 + 2*q^4 - 2*q^2 + 1) / (q^6*(q^2 + 1)), (q^10 - q^8 + 2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1))] := by
  rw [word1_p3 hq hn hD, B0_eq hq hn hD]; mat3

theorem word1_p5 : V1 q * B0 q * V0 q * B0 q * B1 q =
    !![(q^8 - 2*q^6 + 3*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1)), (-2*q^8 + 2*q^6 - 3*q^4 + 2*q^2 - 1) / (q^6*(q^2 + 1)), (q^10 - q^8 + 3*q^6 - 2*q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1));
     (2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (q^6 - 2*q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (q^6 - 2*q^4 + q^2 - 1) / (q^2 + 1);
     (q^6 - q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (-q^6 + 2*q^4 - q^2 + 1) / (q^6*(q^2 + 1)), (q^8 - q^6 + q^4 - q^2 + 1) / (q^2*(q^2 + 1))] := by
  rw [word1_p4 hq hn hD, B1_eq hq hn hD]; mat3

theorem word1_p6 : V1 q * B0 q * V0 q * B0 q * B1 q * V1 q =
    !![(q^8 - q^6 + 3*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (q^10 - q^8 + 2*q^6 - 2*q^4 + q^2 - 1) / (q^2*(q^2 + 1));
     (q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (2*q^4 - q^2 + 1) / (q^2*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^2 + 1);
     (q^6 - q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (q^8 - q^6 + q^4 + 1) / (q^2*(q^2 + 1))] := by
  rw [word1_p5 hq hn hD, V1_eq hq hn hD]; mat3

theorem word2_p2 : B1 q * V0 q =
    !![(q^6 - 3*q^4 + 2*q^2 - 2) / (q^2 + 1), (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-q^8 + 2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^2 + 1);
     (q^4 - 2*q^2 + 1) / (q^2 + 1), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (-q^6 + q^4 - 2*q^2) / (q^2 + 1);
     (-q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (-q^4 + q^2 - 2) / (q^2*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [B1_eq hq hn hD, V0_eq hq hn hD]; mat3

theorem word2_p3 : B1 q * V0 q * B0 q =
    !![(q^8 - 3*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (q^8 - 2*q^6 + 3*q^4 - 2*q^2 + 2) / (q^2*(q^2 + 1)), (q^10 - 2*q^8 + 2*q^6 - 3*q^4 + q^2 - 1) / (q^2 + 1);
     (q^4 - 2*q^2 + 2) / (q^2 + 1), (q^6 - q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - q^2) / (q^2 + 1);
     (-q^6 + 2*q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (-q^6 + q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^8 + q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [word2_p2 hq hn hD, B0_eq hq hn hD]; mat3

theorem word2_p4 : B1 q * V0 q * B0 q * V0 q =
    !![(-q^10 + 3*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^2*(q^2 + 1)), (-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 2) / (q^2*(q^2 + 1)), (q^12 - 3*q^10 + 4*q^8 - 4*q^6 + 4*q^4 - q^2 + 1) / (q^2*(q^2 + 1));
     (-q^6 + 2*q^4 - 4*q^2 + 2) / (q^2 + 1), (-q^8 + 2*q^6 - 3*q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (q^8 - 2*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2 + 1);
     (q^8 - 2*q^6 + 3*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (q^8 - 2*q^6 + 2*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1)), (-q^10 + 2*q^8 - 2*q^6 + 2*q^4 - q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [word2_p3 hq hn hD, V0_eq hq hn hD]; mat3

theorem word2_p5 : B1 q * V0 q * B0 q * V0 q * V1 q =
    !![(q^8 - 3*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-q^8 + 2*q^6 - 3*q^4 + 2*q^2 - 2) / (q^2 + 1), (-q^10 + 2*q^8 - 2*q^6 + 3*q^4 - q^2 + 1) / (q^2*(q^2 + 1));
     (q^4 - 2*q^2 + 2) / (q^2 + 1), (-q^6 + q^4 - 2*q^2 + 1) / (q^2 + 1), (-q^6 + q^4 - 2*q^2 + 1) / (q^2 + 1);
     (-q^6 + 2*q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (q^6 - q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (q^8 - q^6 + q^4 - q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [word2_p4 hq hn hD, V1_eq hq hn hD]; mat3

theorem word2_p6 : B1 q * V0 q * B0 q * V0 q * V1 q * B1 q =
    !![(q^8 - 2*q^6 + 3*q^4 - q^2 + 1) / (q^2*(q^2 + 1)), (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-q^10 + q^8 - 2*q^6 + 2*q^4 - q^2 + 1) / (q^2*(q^2 + 1));
     (q^4 - 2*q^2 + 1) / (q^2 + 1), (q^4 - q^2 + 2) / (q^2 + 1), (-q^6 + q^4 - q^2 + 1) / (q^2 + 1);
     (-q^6 + q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (-q^6 + q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (q^8 + q^4 - q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [word2_p5 hq hn hD, B1_eq hq hn hD]; mat3

/-- `w₁` commutes with `J₄` although it uses the strand-4 site twice. -/
theorem word1_comm_J4 : Commute (word1 q) (J4 q) := by
  unfold Commute SemiconjBy word1; rw [word1_p6 hq hn hD, J4_eq hq hn]; mat3
/-- `w₂` commutes with `J₄`. -/
theorem word2_comm_J4 : Commute (word2 q) (J4 q) := by
  unfold Commute SemiconjBy word2; rw [word2_p6 hq hn hD, J4_eq hq hn]; mat3

/-- `w₁` fixes the `Ja` flavour line from both sides. -/
theorem word1_Ja : word1 q * Ja q = Ja q := by
  unfold word1; rw [word1_p6 hq hn hD]; have := D_ne' hD; have := D_ne'' hD; unfold Ja; mat3
theorem Ja_word1 : Ja q * word1 q = Ja q := by
  unfold word1; rw [word1_p6 hq hn hD]; have := D_ne' hD; have := D_ne'' hD; unfold Ja; mat3
theorem word2_Ja : word2 q * Ja q = Ja q := by
  unfold word2; rw [word2_p6 hq hn hD]; have := D_ne' hD; have := D_ne'' hD; unfold Ja; mat3
theorem Ja_word2 : Ja q * word2 q = Ja q := by
  unfold word2; rw [word2_p6 hq hn hD]; have := D_ne' hD; have := D_ne'' hD; unfold Ja; mat3

/-- **`w₁` does not mix the `J₄` flavour**, in either direction. -/
theorem word1_no_mix : Ja q * word1 q * Jb q = 0 ∧ Jb q * word1 q * Ja q = 0 := by
  constructor
  · rw [Ja_word1 hq hn hD, Ja_Jb hq hn hD]
  · rw [mul_assoc, word1_Ja hq hn hD, Jb_Ja hq hn hD]
/-- **`w₂` does not mix the `J₄` flavour**, in either direction. -/
theorem word2_no_mix : Ja q * word2 q * Jb q = 0 ∧ Jb q * word2 q * Ja q = 0 := by
  constructor
  · rw [Ja_word2 hq hn hD, Ja_Jb hq hn hD]
  · rw [mul_assoc, word2_Ja hq hn hD, Jb_Ja hq hn hD]

end

end QOU.QuarkState.GammaGammaFourStrand
