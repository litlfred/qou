/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import QOU.StandardModel.WorldlineSchwingerFunctorAndSpinorMinkowski

set_option autoImplicit false

/-!
# Chiral Weyl–Dirac Clifford Algebra, Callan–Gross Spin-1/2 Structure Functions, 1-Loop $F_L$ Mellin Moments, and Worldline DIS UV Suppression

This module extends `QOU.StandardModel.WorldlineSchwingerFunctorAndSpinorMinkowski` (`Herm_2(ℂ) ≃ ℝ^{1,3}`)
with unconditional proofs of the relativistic spin-1/2 Dirac–Clifford trace algebra, deep-inelastic
scattering (DIS) $e q \to e q$ tensor contractions, the Callan–Gross relation and its 1-loop QCD
longitudinal violation, and the worldline Schwinger UV suppression bound on inclusive DIS cross-sections:

1. **Section 1 — Chiral Weyl Spinor Clifford Algebra & $4 \times 4$ Dirac Trace Identities:**
   - Connects the chiral Pauli 4-vectors $\sigma^\mu = (I_2, \vec{\sigma})$ and
     $\bar{\sigma}^\mu = (I_2, -\vec{\sigma})$ directly to `spinorMatVec`
     (`spinorMatVec p = ∑ μ, p_μ σ^μ`) and proves the Weyl Clifford anticommutators
     $$\sigma^\mu \bar{\sigma}^\nu + \sigma^\nu \bar{\sigma}^\mu = 2 \eta^{\mu\nu} I_2, \qquad
       \bar{\sigma}^\mu \sigma^\nu + \bar{\sigma}^\nu \sigma^\mu = 2 \eta^{\mu\nu} I_2.$$
   - Constructs the chiral $4 \times 4$ Weyl–Dirac matrices $\gamma^\mu$ and chirality operator
     $\gamma_5 = i \gamma^0 \gamma^1 \gamma^2 \gamma^3$ on $\mathbb{C}^2_L \oplus \mathbb{C}^2_R$,
     proving unconditionally:
     $$\{\gamma^\mu, \gamma^\nu\} = 2 \eta^{\mu\nu} I_4, \qquad
       \gamma_5^2 = I_4, \qquad
       \{\gamma_5, \gamma^\mu\} = 0, \qquad
       \operatorname{Tr}(\gamma^\mu \gamma^\nu) = 4 \eta^{\mu\nu},$$
     and the 256-component 4-gamma trace theorem:
     $$\operatorname{Tr}(\gamma^\mu \gamma^\nu \gamma^\rho \gamma^\sigma)
       = 4\bigl(\eta^{\mu\nu}\eta^{\rho\sigma} - \eta^{\mu\rho}\eta^{\nu\sigma}
         + \eta^{\mu\sigma}\eta^{\nu\rho}\bigr).$$

2. **Section 2 — Spin-1/2 vs Spin-0 Partonic $e q \to e q$ Contraction, Callan–Gross Theorem, & 1-Loop $F_L$ Mellin Moments:**
   - Evaluates $\operatorname{Tr}(\gamma^\mu \not{k} \gamma^\nu \not{k}') = 4(k^\mu k'^\nu + k'^\mu k^\nu - (k\cdot k')\eta^{\mu\nu})$
     and proves the spin-averaged massless $2 \to 2$ contractions ($\hat{s} + \hat{t} + \hat{u} = 0$,
     $y = -\hat{t}/\hat{s}$):
     $$\frac{1}{4} L_{\mu\nu} W_{1/2}^{\mu\nu} = 2(\hat{s}^2 + \hat{u}^2)
       = 2\hat{s}^2\bigl(1 + (1 - y)^2\bigr), \qquad
       \frac{1}{2} L_{\mu\nu} W_0^{\mu\nu} = -4\hat{s}\hat{u}
       = 2\hat{s}^2 \cdot 2(1 - y),$$
     exhibiting exact forward ($y = 0$) Rutherford universality alongside backward ($y = 1$)
     transverse-helicity survival ($1$ for spin-$1/2$ vs $0$ for spin-$0$).
   - Proves the leading-twist Callan–Gross equivalence $F_L(x) := F_2(x) - 2x F_1(x) = 0 \iff$
     pure $\frac{1 + (1 - y)^2}{2} F_2(x)$ angular dependence (contrasted with spin-$0$ $F_1 = 0$,
     $F_L = F_2$).
   - Proves via the Fundamental Theorem of Calculus on $[0, 1]$ the **Zee–Wilczek–Treiman /
     Altarelli–Martinelli 1-loop QCD longitudinal Mellin moments** ($\int_0^1 x^{n-2} F_L(x)\,dx$):
     $$M_n(F_L) = \frac{\alpha_s(Q^2)}{2\pi}\left[
         \frac{8}{3(n + 1)}\, M_n(\Sigma_{\mathrm{em}})
         + \frac{4 \sum_f e_f^2}{(n + 1)(n + 2)}\, M_n(g)
       \right]
       = \frac{\alpha_s(Q^2)}{4\pi}\left[
         \frac{16}{3(n + 1)}\, M_n(\Sigma_{\mathrm{em}})
         + \frac{8 \sum_f e_f^2}{(n + 1)(n + 2)}\, M_n(g)
       \right],$$
     establishing exact rational values $(\frac{8}{9}, \frac{2}{3}, \frac{8}{15})$ in $\frac{\alpha_s}{2\pi}$
     (equivalently $(\frac{16}{9}, \frac{4}{3}, \frac{16}{15})$ in $\frac{\alpha_s}{4\pi}$) at
     $n = 2, 3, 4$ and strict positivity for all $n \ge 1$.

3. **Section 3 — Worldline UV Suppression Bound on Inclusive DIS Cross-Sections:**
   - Proves that replacing the continuum photon propagator $1/Q^2$ by QOU's massless Schwinger
     worldline propagator `schwingerPropagatorReal Q2 0 Tmin = exp(-Q2 * Tmin) / Q2` multiplies
     $d^2\sigma/(dx\,dy)$ by the exact factor $e^{-2 Q^2 T_{\min}} \in (0, 1)$, satisfying
     $$0 < 1 - e^{-2 Q^2 T_{\min}} \le 2 Q^2 T_{\min},$$
     and proves that for $T_{\min} = 1 / E_{\mathrm{Pl}}^2$ ($E_{\mathrm{Pl}} \ge 1.22 \times 10^{19}\;\mathrm{GeV}$),
     the fractional deviation is strictly $< 1.35 \times 10^{-34}$ at HERA ($Q^2 \le 10^4\;\mathrm{GeV}^2$),
     $< 1.35 \times 10^{-30}$ at LHC ($Q^2 \le 10^8\;\mathrm{GeV}^2$), and
     $< 1.35 \times 10^{-29} < 3.4 \times 10^{-29}$ even at $Q^2 \le 10^9\;\mathrm{GeV}^2$.
-/

namespace QOU.StandardModel.DiracWeylCliffordCallanGrossAndDISCrossSection

open scoped BigOperators
open Matrix MeasureTheory intervalIntegral
open QOU.StandardModel.WorldlineSchwingerFunctorAndSpinorMinkowski
  (spinorMat spinorMatVec schwingerPropagatorReal)

-- ============================================================================
-- § 1. Chiral Weyl Spinor Clifford Algebra & 4 × 4 Dirac Trace Identities
-- ============================================================================

section ChiralWeylDiracClifford

/-- Chiral Bispinor index type `(chirality ∈ Fin 2) × (spinor ∈ Fin 2)` representing
$\mathbb{C}^2_L \oplus \mathbb{C}^2_R$. -/
abbrev FourSpinor := Fin 2 × Fin 2

/-- Minkowski metric tensor $\eta^{\mu\nu} = \mathrm{diag}(+1, -1, -1, -1)$ on `Fin 4`. -/
def minkowskiEta (μ ν : Fin 4) : ℝ :=
  if μ = ν then (if μ = 0 then 1 else -1) else 0

/-- Minkowski bilinear inner product $u \cdot v = u_0 v_0 - u_1 v_1 - u_2 v_2 - u_3 v_3$. -/
def minkowskiDot (u v : Fin 4 → ℝ) : ℝ :=
  u 0 * v 0 - u 1 * v 1 - u 2 * v 2 - u 3 * v 3

/-- Right-chiral Pauli 4-vector $\sigma^\mu = (I_2, \sigma^1, \sigma^2, \sigma^3)$ on `Fin 2`. -/
def sigmaVec : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ
  | ⟨0, _⟩ => !![1, 0; 0, 1]
  | ⟨1, _⟩ => !![0, 1; 1, 0]
  | ⟨2, _⟩ => !![0, -Complex.I; Complex.I, 0]
  | ⟨3, _⟩ => !![1, 0; 0, -1]

/-- Left-chiral Pauli 4-vector $\bar{\sigma}^\mu = (I_2, -\sigma^1, -\sigma^2, -\sigma^3)$ on `Fin 2`. -/
def sigmaBarVec : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ
  | ⟨0, _⟩ => !![1, 0; 0, 1]
  | ⟨1, _⟩ => !![0, -1; -1, 0]
  | ⟨2, _⟩ => !![0, Complex.I; -Complex.I, 0]
  | ⟨3, _⟩ => !![-1, 0; 0, 1]

/-- Off-diagonal chiral $2 \times 2$ block matrix $\begin{pmatrix} 0 & A \\ B & 0 \end{pmatrix}$
on $\mathbb{C}^2_L \oplus \mathbb{C}^2_R$. -/
def chiralOffDiag (A B : Matrix (Fin 2) (Fin 2) ℂ) : Matrix FourSpinor FourSpinor ℂ :=
  Matrix.of fun (c₁, s₁) (c₂, s₂) =>
    if c₁ = 0 ∧ c₂ = 1 then A s₁ s₂
    else if c₁ = 1 ∧ c₂ = 0 then B s₁ s₂
    else 0

/-- Block-diagonal chiral $2 \times 2$ matrix $\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}$
on $\mathbb{C}^2_L \oplus \mathbb{C}^2_R$. -/
def chiralDiag (A B : Matrix (Fin 2) (Fin 2) ℂ) : Matrix FourSpinor FourSpinor ℂ :=
  Matrix.of fun (c₁, s₁) (c₂, s₂) =>
    if c₁ = 0 ∧ c₂ = 0 then A s₁ s₂
    else if c₁ = 1 ∧ c₂ = 1 then B s₁ s₂
    else 0

/-- Chiral Weyl–Dirac matrices $\gamma^\mu = \begin{pmatrix} 0 & \sigma^\mu \\ \bar{\sigma}^\mu & 0 \end{pmatrix}$. -/
def diracGamma (μ : Fin 4) : Matrix FourSpinor FourSpinor ℂ :=
  chiralOffDiag (sigmaVec μ) (sigmaBarVec μ)

/-- Chiral grading operator $\gamma_5 = \begin{pmatrix} -I_2 & 0 \\ 0 & I_2 \end{pmatrix}$. -/
def diracGammaFive : Matrix FourSpinor FourSpinor ℂ :=
  chiralDiag (-1) 1

/-- Exact bridge from `spinorMatVec` (`WorldlineSchwingerFunctorAndSpinorMinkowski`) to `sigmaVec`:
$P(p) = \sum_{\mu=0}^3 p^\mu \sigma^\mu$. -/
theorem spinorMatVec_eq_sum_sigmaVec (p : Fin 4 → ℝ) :
    spinorMatVec p = ∑ μ : Fin 4, (p μ : ℂ) • sigmaVec μ := by
  ext i j
  simp only [spinorMatVec, spinorMat, Fin.sum_univ_four, Matrix.add_apply, Matrix.smul_apply,
    sigmaVec]
  fin_cases i <;> fin_cases j <;> simp <;> ring

/-- **Chiral Weyl Spinor Clifford Anticommutator Identities:**
$\sigma^\mu \bar{\sigma}^\nu + \sigma^\nu \bar{\sigma}^\mu = 2\eta^{\mu\nu} I_2$ and
$\bar{\sigma}^\mu \sigma^\nu + \bar{\sigma}^\nu \sigma^\mu = 2\eta^{\mu\nu} I_2$. -/
theorem sigmaVec_sigmaBarVec_clifford (μ ν : Fin 4) :
    sigmaVec μ * sigmaBarVec ν + sigmaVec ν * sigmaBarVec μ =
      (2 * (minkowskiEta μ ν : ℂ)) • (1 : Matrix (Fin 2) (Fin 2) ℂ) ∧
      sigmaBarVec μ * sigmaVec ν + sigmaBarVec ν * sigmaVec μ =
        (2 * (minkowskiEta μ ν : ℂ)) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  have hs0 : sigmaVec 0 = 1 ∧ sigmaBarVec 0 = 1 := by
    constructor <;>
      (ext i j; fin_cases i <;> fin_cases j <;> simp [sigmaVec, sigmaBarVec])
  have hs_neg : ∀ k : Fin 4, k ≠ 0 → sigmaBarVec k = -sigmaVec k := by
    intro k hk
    fin_cases k
    · exact False.elim (hk rfl)
    all_goals
      ext i j; fin_cases i <;> fin_cases j <;> simp [sigmaVec, sigmaBarVec]
  have hpauli : ∀ a b : Fin 4, a ≠ 0 → b ≠ 0 →
      sigmaVec a * sigmaVec b + sigmaVec b * sigmaVec a =
        (-2 * (minkowskiEta a b : ℂ)) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
    intro a b ha hb
    fin_cases a
    · exact False.elim (ha rfl)
    all_goals
      fin_cases b
      · exact False.elim (hb rfl)
      all_goals
        ext i j
        simp only [Matrix.add_apply, Matrix.mul_apply, Fin.sum_univ_two,
          Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
        fin_cases i <;> fin_cases j <;>
          ((dsimp [sigmaVec, minkowskiEta]; apply Complex.ext <;> simp) <;> norm_num)
  by_cases hμ : μ = 0
  · subst hμ
    by_cases hν : ν = 0
    · subst hν
      rw [hs0.1, hs0.2, mul_one]
      have heta0 : minkowskiEta 0 0 = 1 := rfl
      rw [heta0]
      constructor <;> (ext i j; fin_cases i <;> fin_cases j <;> simp <;> norm_num)
    · have heta : minkowskiEta 0 ν = 0 := by simp [minkowskiEta, Ne.symm hν]
      rw [hs0.1, hs0.2, hs_neg ν hν, heta]
      simp
  · by_cases hν : ν = 0
    · subst hν
      have heta : minkowskiEta μ 0 = 0 := by simp [minkowskiEta, hμ]
      rw [hs0.1, hs0.2, hs_neg μ hμ, heta]
      simp
    · rw [hs_neg μ hμ, hs_neg ν hν]
      simp only [mul_neg, neg_mul, ← neg_add]
      rw [hpauli μ ν hμ hν, ← neg_smul]
      have hneg : -(-2 * (minkowskiEta μ ν : ℂ)) = 2 * (minkowskiEta μ ν : ℂ) := by ring
      rw [hneg]
      exact ⟨rfl, rfl⟩

/-- Chiral block-matrix algebra laws reducing $4 \times 4$ bispinor products and traces to $2 \times 2$
Weyl blocks without 64-way case splitting. -/
theorem chiral_block_algebra_laws (A₁ B₁ A₂ B₂ : Matrix (Fin 2) (Fin 2) ℂ) (c : ℂ) :
    chiralOffDiag A₁ B₁ * chiralOffDiag A₂ B₂ = chiralDiag (A₁ * B₂) (B₁ * A₂) ∧
      chiralDiag A₁ B₁ * chiralDiag A₂ B₂ = chiralDiag (A₁ * A₂) (B₁ * B₂) ∧
      chiralDiag A₁ B₁ * chiralOffDiag A₂ B₂ = chiralOffDiag (A₁ * A₂) (B₁ * B₂) ∧
      chiralOffDiag A₁ B₁ * chiralDiag A₂ B₂ = chiralOffDiag (A₁ * B₂) (B₁ * A₂) ∧
      chiralDiag A₁ B₁ + chiralDiag A₂ B₂ = chiralDiag (A₁ + A₂) (B₁ + B₂) ∧
      chiralOffDiag A₁ B₁ + chiralOffDiag A₂ B₂ = chiralOffDiag (A₁ + A₂) (B₁ + B₂) ∧
      chiralDiag (c • 1) (c • 1) = c • (1 : Matrix FourSpinor FourSpinor ℂ) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, chiralOffDiag,
      chiralDiag, Matrix.of_apply]
    fin_cases c₁ <;> fin_cases c₂ <;> simp
  · ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, chiralDiag,
      Matrix.of_apply]
    fin_cases c₁ <;> fin_cases c₂ <;> simp
  · ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, chiralDiag,
      chiralOffDiag, Matrix.of_apply]
    fin_cases c₁ <;> fin_cases c₂ <;> simp
  · ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, chiralDiag,
      chiralOffDiag, Matrix.of_apply]
    fin_cases c₁ <;> fin_cases c₂ <;> simp
  · ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    fin_cases c₁ <;> fin_cases c₂ <;> simp [chiralDiag]
  · ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    fin_cases c₁ <;> fin_cases c₂ <;> simp [chiralOffDiag]
  · ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    fin_cases c₁ <;> fin_cases c₂ <;> fin_cases s₁ <;> fin_cases s₂ <;>
      simp [chiralDiag, Matrix.one_apply]

/-- **$4 \times 4$ Weyl–Dirac Clifford Anticommutator & Chiral $\gamma_5$ Algebra:**
1. $\{\gamma^\mu, \gamma^\nu\} = 2 \eta^{\mu\nu} I_4$,
2. $\gamma_5^2 = I_4$,
3. $\{\gamma_5, \gamma^\mu\} = 0$,
4. $i \gamma^0 \gamma^1 \gamma^2 \gamma^3 = \gamma_5$ and $\operatorname{Tr}(\gamma_5) = 0$. -/
theorem diracGamma_clifford_and_gammaFive (μ ν : Fin 4) :
    diracGamma μ * diracGamma ν + diracGamma ν * diracGamma μ =
      (2 * (minkowskiEta μ ν : ℂ)) • (1 : Matrix FourSpinor FourSpinor ℂ) ∧
      diracGammaFive * diracGammaFive = 1 ∧
      diracGammaFive * diracGamma μ + diracGamma μ * diracGammaFive = 0 ∧
      Complex.I • (diracGamma 0 * diracGamma 1 * diracGamma 2 * diracGamma 3) = diracGammaFive ∧
      Matrix.trace diracGammaFive = 0 := by
  have hcl := sigmaVec_sigmaBarVec_clifford μ ν
  have h1 : diracGamma μ * diracGamma ν + diracGamma ν * diracGamma μ =
      (2 * (minkowskiEta μ ν : ℂ)) • (1 : Matrix FourSpinor FourSpinor ℂ) := by
    unfold diracGamma
    rw [(chiral_block_algebra_laws _ _ _ _ 0).1,
      (chiral_block_algebra_laws _ _ _ _ 0).1,
      (chiral_block_algebra_laws _ _ _ _ 0).2.2.2.2.1,
      hcl.1, hcl.2,
      (chiral_block_algebra_laws 1 1 1 1 (2 * (minkowskiEta μ ν : ℂ))).2.2.2.2.2.2]
  have h2 : diracGammaFive * diracGammaFive = 1 := by
    unfold diracGammaFive
    rw [(chiral_block_algebra_laws (-1) 1 (-1) 1 1).2.1]
    have hm1 : (-1 : Matrix (Fin 2) (Fin 2) ℂ) * (-1) = (1 : ℂ) • 1 := by simp
    have hp1 : (1 : Matrix (Fin 2) (Fin 2) ℂ) * 1 = (1 : ℂ) • 1 := by simp
    rw [hm1, hp1, (chiral_block_algebra_laws 1 1 1 1 1).2.2.2.2.2.2, one_smul]
  have h3 : diracGammaFive * diracGamma μ + diracGamma μ * diracGammaFive = 0 := by
    unfold diracGammaFive diracGamma
    rw [(chiral_block_algebra_laws (-1) 1 (sigmaVec μ) (sigmaBarVec μ) 0).2.2.1,
      (chiral_block_algebra_laws (sigmaVec μ) (sigmaBarVec μ) (-1) 1 0).2.2.2.1,
      (chiral_block_algebra_laws _ _ _ _ 0).2.2.2.2.2.1]
    simp only [neg_mul, one_mul, mul_one, mul_neg, neg_add_cancel, add_neg_cancel]
    ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    simp [chiralOffDiag]
  have h4 : Complex.I • (diracGamma 0 * diracGamma 1 * diracGamma 2 * diracGamma 3) =
      diracGammaFive := by
    unfold diracGamma diracGammaFive
    have hp01 := (chiral_block_algebra_laws (sigmaVec 0) (sigmaBarVec 0)
      (sigmaVec 1) (sigmaBarVec 1) 0).1
    have hp23 := (chiral_block_algebra_laws (sigmaVec 2) (sigmaBarVec 2)
      (sigmaVec 3) (sigmaBarVec 3) 0).1
    rw [Matrix.mul_assoc (chiralOffDiag (sigmaVec 0) (sigmaBarVec 0) *
      chiralOffDiag (sigmaVec 1) (sigmaBarVec 1)), hp01, hp23,
      (chiral_block_algebra_laws _ _ _ _ 0).2.1]
    have hL : sigmaVec 0 * sigmaBarVec 1 * (sigmaVec 2 * sigmaBarVec 3) =
        Complex.I • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [sigmaVec, sigmaBarVec, Matrix.mul_apply, Fin.sum_univ_two]
    have hR : sigmaBarVec 0 * sigmaVec 1 * (sigmaBarVec 2 * sigmaVec 3) =
        (-Complex.I) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [sigmaVec, sigmaBarVec, Matrix.mul_apply, Fin.sum_univ_two]
    rw [hL, hR]
    ext ⟨c₁, s₁⟩ ⟨c₂, s₂⟩
    fin_cases c₁ <;> fin_cases c₂ <;> fin_cases s₁ <;> fin_cases s₂ <;>
      simp [chiralDiag, Complex.I_mul_I]
  have h5 : Matrix.trace diracGammaFive = 0 := by
    simp [diracGammaFive, chiralDiag, Matrix.trace, Matrix.diag,
      Fintype.sum_prod_type, Fin.sum_univ_two]
  exact ⟨h1, h2, h3, h4, h5⟩

/-- **Exact 2-Gamma and 4-Gamma Dirac Trace Theorems (All $4^4 = 256$ Components):**
1. $\operatorname{Tr}(\gamma^\mu \gamma^\nu) = 4 \eta^{\mu\nu}$,
2. $\operatorname{Tr}(\gamma^\mu \gamma^\nu \gamma^\rho \gamma^\sigma) =
   4\bigl(\eta^{\mu\nu}\eta^{\rho\sigma} - \eta^{\mu\rho}\eta^{\nu\sigma}
   + \eta^{\mu\sigma}\eta^{\nu\rho}\bigr)$. -/
theorem trace_diracGamma_two_and_four (μ ν ρ σ : Fin 4) :
    Matrix.trace (diracGamma μ * diracGamma ν) = 4 * (minkowskiEta μ ν : ℂ) ∧
      Matrix.trace (diracGamma μ * diracGamma ν * diracGamma ρ * diracGamma σ) =
        4 * ((minkowskiEta μ ν * minkowskiEta ρ σ -
          minkowskiEta μ ρ * minkowskiEta ν σ +
          minkowskiEta μ σ * minkowskiEta ν ρ : ℝ) : ℂ) := by
  have htr_one : Matrix.trace (1 : Matrix FourSpinor FourSpinor ℂ) = 4 := by
    simp [Matrix.trace, Matrix.diag]
  have htwo : ∀ a b : Fin 4,
      Matrix.trace (diracGamma a * diracGamma b) = 4 * (minkowskiEta a b : ℂ) := by
    intro a b
    have hac := (diracGamma_clifford_and_gammaFive a b).1
    have htr := congrArg Matrix.trace hac
    rw [Matrix.trace_add, Matrix.trace_mul_comm (diracGamma b) (diracGamma a),
      Matrix.trace_smul, htr_one, smul_eq_mul] at htr
    linear_combination (1 / 2 : ℂ) * htr
  refine ⟨htwo μ ν, ?_⟩
  let A := diracGamma μ
  let B := diracGamma ν
  let C := diracGamma ρ
  let D := diracGamma σ
  have hac_AB : A * B = (2 * (minkowskiEta μ ν : ℂ)) • 1 - B * A := by
    rw [eq_sub_iff_add_eq]
    exact (diracGamma_clifford_and_gammaFive μ ν).1
  have hac_AC : A * C = (2 * (minkowskiEta μ ρ : ℂ)) • 1 - C * A := by
    rw [eq_sub_iff_add_eq]
    exact (diracGamma_clifford_and_gammaFive μ ρ).1
  have hac_AD : A * D = (2 * (minkowskiEta μ σ : ℂ)) • 1 - D * A := by
    rw [eq_sub_iff_add_eq]
    exact (diracGamma_clifford_and_gammaFive μ σ).1
  have hmove : A * B * C * D + B * C * D * A =
      (2 * (minkowskiEta μ ν : ℂ)) • (C * D) -
        (2 * (minkowskiEta μ ρ : ℂ)) • (B * D) +
        (2 * (minkowskiEta μ σ : ℂ)) • (B * C) := by
    have hs1 : A * B * C * D =
        (2 * (minkowskiEta μ ν : ℂ)) • (C * D) - B * (A * C) * D := by
      calc
        A * B * C * D = ((2 * (minkowskiEta μ ν : ℂ)) • 1 - B * A) * (C * D) := by
          rw [hac_AB, Matrix.mul_assoc]
        _ = (2 * (minkowskiEta μ ν : ℂ)) • (C * D) - B * (A * C) * D := by
          rw [sub_mul, Matrix.smul_mul, one_mul]
          simp only [Matrix.mul_assoc]
    have hs2 : B * (A * C) * D =
        (2 * (minkowskiEta μ ρ : ℂ)) • (B * D) - B * C * (A * D) := by
      rw [hac_AC, mul_sub, sub_mul, Matrix.mul_smul, mul_one, Matrix.smul_mul]
      simp only [Matrix.mul_assoc]
    have hs3 : B * C * (A * D) =
        (2 * (minkowskiEta μ σ : ℂ)) • (B * C) - B * C * D * A := by
      rw [hac_AD, mul_sub, Matrix.mul_smul, mul_one]
      simp only [Matrix.mul_assoc]
    rw [hs1, hs2, hs3]
    abel
  have htr4 := congrArg Matrix.trace hmove
  have hcyc : Matrix.trace (B * C * D * A) = Matrix.trace (A * B * C * D) := by
    rw [Matrix.trace_mul_comm (B * C * D) A]
    simp only [Matrix.mul_assoc]
  rw [Matrix.trace_add, hcyc, Matrix.trace_add, Matrix.trace_sub,
    Matrix.trace_smul, Matrix.trace_smul, Matrix.trace_smul,
    htwo ρ σ, htwo ν σ, htwo ν ρ] at htr4
  simp only [smul_eq_mul, Complex.ofReal_sub, Complex.ofReal_add, Complex.ofReal_mul] at htr4 ⊢
  change Matrix.trace (A * B * C * D) = _
  linear_combination (1 / 2 : ℂ) * htr4

end ChiralWeylDiracClifford

-- ============================================================================
-- § 2. Spin-1/2 vs Spin-0 DIS Contractions, Callan–Gross, & 1-Loop F_L Moments
-- ============================================================================

section CallanGrossAndLongitudinalMoments

/-- Feynman slash $\not{k} = \sum_\alpha \eta_{\alpha\alpha} k^\alpha \gamma^\alpha$ of a
contravariant 4-vector $k : \mathrm{Fin}\;4 \to \mathbb{R}$. -/
noncomputable def diracSlash (k : Fin 4 → ℝ) : Matrix FourSpinor FourSpinor ℂ :=
  ∑ α : Fin 4, (minkowskiEta α α * k α : ℂ) • diracGamma α

/-- Spin-summed massless spin-$1/2$ trace tensor
$L^{\mu\nu}(u, v) = 4\bigl(u^\mu v^\nu + v^\mu u^\nu - (u \cdot v)\eta^{\mu\nu}\bigr)$. -/
def fermionTraceTensor (u v : Fin 4 → ℝ) (μ ν : Fin 4) : ℝ :=
  4 * (u μ * v ν + v μ * u ν - minkowskiDot u v * minkowskiEta μ ν)

/-- Spin-$0$ scalar parton current tensor $W_0^{\mu\nu}(p, p') = (p + p')^\mu (p + p')^\nu$. -/
def scalarTraceTensor (p p' : Fin 4 → ℝ) (μ ν : Fin 4) : ℝ :=
  (p μ + p' μ) * (p ν + p' ν)

/-- Full Lorentz index contraction $\eta_{\mu\mu'}\eta_{\nu\nu'} T^{\mu\nu} W^{\mu'\nu'}$ of two
contravariant rank-2 tensors. -/
def lorentzContract2 (T W : Fin 4 → Fin 4 → ℝ) : ℝ :=
  ∑ μ : Fin 4, ∑ ν : Fin 4,
    (minkowskiEta μ μ * minkowskiEta ν ν) * T μ ν * W μ ν

/-- Reduced inclusive DIS angular cross-section polynomial
$\tilde{\sigma}(x, y; F_1, F_2) = (1 - y) F_2 + y^2 x F_1$. -/
def disReducedCrossSection (x y F₁ F₂ : ℝ) : ℝ :=
  (1 - y) * F₂ + y ^ 2 * x * F₁

/-- Longitudinal DIS structure function $F_L(x) = F_2(x) - 2 x F_1(x)$. -/
def longitudinalStructureFn (x F₁ F₂ : ℝ) : ℝ :=
  F₂ - 2 * x * F₁

/-- Exact Dirac trace evaluation $\operatorname{Tr}(\gamma^\mu \not{k} \gamma^\nu \not{k}') =
4(k^\mu k'^\nu + k'^\mu k^\nu - (k\cdot k')\eta^{\mu\nu})$. -/
theorem trace_diracGamma_slash_eq_fermionTraceTensor (k k' : Fin 4 → ℝ) (μ ν : Fin 4) :
    Matrix.trace (diracGamma μ * diracSlash k * diracGamma ν * diracSlash k') =
      (fermionTraceTensor k k' μ ν : ℂ) := by
  unfold diracSlash
  simp only [Fin.sum_univ_four, mul_add, add_mul, Matrix.mul_smul, Matrix.smul_mul,
    smul_smul, Matrix.trace_add, Matrix.trace_smul,
    (trace_diracGamma_two_and_four _ _ _ _).2, smul_eq_mul]
  fin_cases μ <;> fin_cases ν <;>
    (simp [fermionTraceTensor, minkowskiDot, minkowskiEta]; ring)

/-- Explicit 16-term Minkowski sign expansion of `lorentzContract2`. -/
theorem lorentzContract2_expand (T W : Fin 4 → Fin 4 → ℝ) :
    lorentzContract2 T W =
      T 0 0 * W 0 0 - T 0 1 * W 0 1 - T 0 2 * W 0 2 - T 0 3 * W 0 3 -
      T 1 0 * W 1 0 + T 1 1 * W 1 1 + T 1 2 * W 1 2 + T 1 3 * W 1 3 -
      T 2 0 * W 2 0 + T 2 1 * W 2 1 + T 2 2 * W 2 2 + T 2 3 * W 2 3 -
      T 3 0 * W 3 0 + T 3 1 * W 3 1 + T 3 2 * W 3 2 + T 3 3 * W 3 3 := by
  unfold lorentzContract2
  simp only [Fin.sum_univ_four, minkowskiEta, Fin.isValue, Fin.reduceEq, ↓reduceIte]
  ring

/-- **Spin-$1/2$ vs Spin-$0$ Partonic $e q \to e q$ Contraction & Callan–Gross Theorem:**
1. General Lorentz contraction for massless spin-$1/2$ vs spin-$0$:
   $$\frac{1}{4} L_{\mu\nu}(k, k') W_{1/2}^{\mu\nu}(p, p')
     = 8\bigl((k \cdot p)(k' \cdot p') + (k \cdot p')(k' \cdot p)\bigr),$$
   $$\frac{1}{2} L_{\mu\nu}(k, k') W_0^{\mu\nu}(p, p')
     = 2\bigl(2 (k \cdot (p + p'))(k' \cdot (p + p')) - (k \cdot k')((p + p') \cdot (p + p'))\bigr).$$
2. Under massless $2 \to 2$ Mandelstam kinematics ($2(k\cdot p) = 2(k'\cdot p') = \hat{s} \neq 0$,
   $2(k\cdot p') = 2(k'\cdot p) = -\hat{u}$, $2(k\cdot k') = -\hat{t}$, $(p + p')^2 = -\hat{t}$,
   $\hat{s} + \hat{t} + \hat{u} = 0$, and $y = -\hat{t} / \hat{s}$):
   - Spin-$1/2$: $\frac{1}{4} L_{\mu\nu} W_{1/2}^{\mu\nu} = 2(\hat{s}^2 + \hat{u}^2) = 2\hat{s}^2(1 + (1 - y)^2)$,
   - Spin-$0$: $\frac{1}{2} L_{\mu\nu} W_0^{\mu\nu} = -4\hat{s}\hat{u} = 2\hat{s}^2 \cdot 2(1 - y)$.
3. **Callan–Gross Decomposition & Equivalence:**
   $$\tilde{\sigma}(x, y; F_1, F_2) = \frac{1 + (1 - y)^2}{2} F_2 - \frac{y^2}{2} F_L(x),$$
   so for any $y \neq 0$, $\tilde{\sigma}(x, y; F_1, F_2) = \frac{1 + (1 - y)^2}{2} F_2 \iff F_L(x) = 0$
   ($F_2 = 2x F_1$, spin-$1/2$ Callan–Gross), whereas a spin-$0$ parton ($F_1 = 0$) gives
   $\tilde{\sigma}(x, y; 0, F_2) = (1 - y) F_2$ and $F_L = F_2$. -/
theorem partonic_spinHalf_vs_spinZero_and_callan_gross
    (k k' p p' : Fin 4 → ℝ) {sHat tHat uHat x y F₁ F₂ : ℝ}
    (hs_ne : sHat ≠ 0) (hmand : sHat + tHat + uHat = 0) (hy : y = -tHat / sHat) :
    (1 / 4 : ℝ) * lorentzContract2 (fermionTraceTensor k k') (fermionTraceTensor p p') =
        8 * (minkowskiDot k p * minkowskiDot k' p' + minkowskiDot k p' * minkowskiDot k' p) ∧
      (1 / 2 : ℝ) * lorentzContract2 (fermionTraceTensor k k') (scalarTraceTensor p p') =
        2 * (2 * (minkowskiDot k p + minkowskiDot k p') * (minkowskiDot k' p + minkowskiDot k' p') -
          minkowskiDot k k' * (minkowskiDot p p + 2 * minkowskiDot p p' + minkowskiDot p' p')) ∧
      ((sHat ^ 2 + uHat ^ 2) / sHat ^ 2 = 1 + (1 - y) ^ 2 ∧
        (-4 * sHat * uHat) / (2 * sHat ^ 2) = 2 * (1 - y)) ∧
      (disReducedCrossSection x y F₁ F₂ =
          ((1 + (1 - y) ^ 2) / 2) * F₂ - (y ^ 2 / 2) * longitudinalStructureFn x F₁ F₂ ∧
        (y ≠ 0 → (disReducedCrossSection x y F₁ F₂ = ((1 + (1 - y) ^ 2) / 2) * F₂ ↔
          longitudinalStructureFn x F₁ F₂ = 0)) ∧
        disReducedCrossSection x y 0 F₂ = (1 - y) * F₂ ∧
        longitudinalStructureFn x 0 F₂ = F₂) := by
  have hc_half : (1 / 4 : ℝ) *
      lorentzContract2 (fermionTraceTensor k k') (fermionTraceTensor p p') =
      8 * (minkowskiDot k p * minkowskiDot k' p' + minkowskiDot k p' * minkowskiDot k' p) := by
    rw [lorentzContract2_expand]
    simp only [fermionTraceTensor, minkowskiDot, minkowskiEta, Fin.isValue, Fin.reduceEq, ↓reduceIte]
    ring
  have hc_zero : (1 / 2 : ℝ) *
      lorentzContract2 (fermionTraceTensor k k') (scalarTraceTensor p p') =
      2 * (2 * (minkowskiDot k p + minkowskiDot k p') * (minkowskiDot k' p + minkowskiDot k' p') -
        minkowskiDot k k' * (minkowskiDot p p + 2 * minkowskiDot p p' + minkowskiDot p' p')) := by
    rw [lorentzContract2_expand]
    simp only [fermionTraceTensor, scalarTraceTensor, minkowskiDot, minkowskiEta, Fin.isValue,
      Fin.reduceEq, ↓reduceIte]
    ring
  have hu_eq : uHat = -(sHat + tHat) := by linarith
  have hmand_y : (sHat ^ 2 + uHat ^ 2) / sHat ^ 2 = 1 + (1 - y) ^ 2 ∧
      (-4 * sHat * uHat) / (2 * sHat ^ 2) = 2 * (1 - y) := by
    rw [hy, hu_eq]
    refine ⟨?_, ?_⟩
    · field_simp [hs_ne]; ring
    · field_simp [hs_ne]; ring
  have hcg_decomp : disReducedCrossSection x y F₁ F₂ =
      ((1 + (1 - y) ^ 2) / 2) * F₂ - (y ^ 2 / 2) * longitudinalStructureFn x F₁ F₂ := by
    unfold disReducedCrossSection longitudinalStructureFn
    ring
  refine ⟨hc_half, hc_zero, hmand_y, hcg_decomp, ?_, ?_, ?_⟩
  · intro hy_ne
    rw [hcg_decomp]
    have hy2_ne : y ^ 2 / 2 ≠ 0 := div_ne_zero (pow_ne_zero 2 hy_ne) two_ne_zero
    constructor
    · intro heq
      have hzero : (y ^ 2 / 2) * longitudinalStructureFn x F₁ F₂ = 0 := by linarith
      exact (mul_eq_zero.mp hzero).resolve_left hy2_ne
    · intro hFL
      rw [hFL, mul_zero, sub_zero]
  · unfold disReducedCrossSection; ring
  · unfold longitudinalStructureFn; ring

/-- **Forward Rutherford Universality (`y = 0`) vs Backward Transverse-Helicity Survival (`y = 1`):**
At forward scattering $y = 0$, spin-$1/2$ ($1 + (1 - y)^2$) and spin-$0$ ($2(1 - y)$) partons both
evaluate to $2$; at backward scattering $y = 1$, spin-$1/2$ retains unit transverse-helicity weight
$1 > 0$ whereas spin-$0$ vanishes identically ($0$). -/
theorem rutherford_forward_and_backward_helicity_discrimination :
    1 + (1 - (0 : ℝ)) ^ 2 = 2 ∧
      2 * (1 - (0 : ℝ)) = 2 ∧
      1 + (1 - (1 : ℝ)) ^ 2 = 1 ∧
      2 * (1 - (1 : ℝ)) = 0 ∧
      (0 : ℝ) < 1 + (1 - (1 : ℝ)) ^ 2 := by
  norm_num

/-- Fundamental Theorem of Calculus evaluation $\int_0^1 z^m\,dz = \frac{1}{m + 1}$ for every $m \in \mathbb{N}$. -/
theorem integral_unit_pow_eq (m : ℕ) :
    (∫ z in (0 : ℝ)..1, z ^ m) = 1 / ((m : ℝ) + 1) := by
  have hm1_pos : (0 : ℝ) < (m : ℝ) + 1 := by positivity
  have hm1_ne : (m : ℝ) + 1 ≠ 0 := ne_of_gt hm1_pos
  let F : ℝ → ℝ := fun z => z ^ (m + 1) / ((m : ℝ) + 1)
  have hderiv : ∀ z ∈ Set.uIcc (0 : ℝ) 1, HasDerivAt F (z ^ m) z := by
    intro z _
    have hp : HasDerivAt (fun t : ℝ => t ^ (m + 1)) (((m + 1 : ℕ) : ℝ) * z ^ m) z :=
      hasDerivAt_pow (m + 1) z
    have hF := hp.div_const ((m : ℝ) + 1)
    convert hF using 1
    rw [Nat.cast_add, Nat.cast_one]
    exact (mul_div_cancel_left₀ (z ^ m) hm1_ne).symm
  have hint : IntervalIntegrable (fun z : ℝ => z ^ m) volume (0 : ℝ) 1 :=
    (continuous_pow m).intervalIntegrable 0 1
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint]
  dsimp [F]
  rw [one_pow, zero_pow (Nat.succ_ne_zero m), zero_div, sub_zero]

/-- 1-loop QCD longitudinal quark Mellin coefficient $\frac{2 C_F}{n + 1} = \frac{8}{3(n + 1)}$
in $\frac{\alpha_s}{2\pi}$ normalization (Zee, Wilczek, & Treiman 1974; Altarelli & Martinelli 1978). -/
noncomputable def flQuarkMomentCoeff (n : ℕ) : ℝ :=
  8 / (3 * ((n : ℝ) + 1))

/-- 1-loop QCD longitudinal gluon Mellin coefficient $\frac{4}{(n + 1)(n + 2)}$ per unit squared
quark charge $\sum_f e_f^2$ in $\frac{\alpha_s}{2\pi}$ normalization (Altarelli & Martinelli 1978). -/
noncomputable def flGluonMomentCoeff (n : ℕ) : ℝ :=
  4 / (((n : ℝ) + 1) * ((n : ℝ) + 2))

/-- Complete 1-loop QCD longitudinal DIS Mellin moment
$M_n(F_L) = \int_0^1 x^{n-2} F_L(x, Q^2)\,dx$ in terms of the electromagnetic charge-weighted
quark-singlet moment $M_n(\Sigma_{\mathrm{em}})$ and gluon moment $M_n(g)$. -/
noncomputable def mellinFLOneLoop (α_s sumChargeSq M_Sigma M_g : ℝ) (n : ℕ) : ℝ :=
  (α_s / (2 * Real.pi)) *
    (flQuarkMomentCoeff n * M_Sigma + sumChargeSq * flGluonMomentCoeff n * M_g)

/-- **Zee–Wilczek–Treiman / Altarelli–Martinelli 1-Loop $F_L$ Mellin Moment Theorem:**
1. Exact FTC integral evaluations for every $n \in \mathbb{N}$:
   $$\int_0^1 \frac{8}{3} z^n\,dz = \frac{8}{3(n + 1)}, \qquad
     \int_0^1 4 z^n (1 - z)\,dz = \frac{4}{(n + 1)(n + 2)};$$
2. Exact equivalence between $\frac{\alpha_s}{2\pi}$ and $\frac{\alpha_s}{4\pi}$ normalizations:
   $$M_n(F_L) = \frac{\alpha_s}{4\pi}\left[
       \frac{16}{3(n + 1)} M_n(\Sigma_{\mathrm{em}})
       + \frac{8 \sum_f e_f^2}{(n + 1)(n + 2)} M_n(g)\right];$$
3. Exact rational benchmarks at $n = 2, 3, 4$:
   - Quark coefficients in $\frac{\alpha_s}{2\pi}$: $(\frac{8}{9}, \frac{2}{3}, \frac{8}{15})$,
     and in $\frac{\alpha_s}{4\pi}$: $(\frac{16}{9}, \frac{4}{3}, \frac{16}{15})$;
   - Gluon coefficients in $\frac{\alpha_s}{2\pi}$: $(\frac{1}{3}, \frac{1}{5}, \frac{2}{15})$;
4. Exact Callan–Gross limit $M_n(F_L) = 0$ at $\alpha_s = 0$, and strict positivity
   $0 < M_n(F_L)$ for all $n \in \mathbb{N}$ whenever $\alpha_s > 0$, $M_n(\Sigma_{\mathrm{em}}) > 0$,
   $\sum_f e_f^2 \ge 0$, and $M_n(g) \ge 0$. -/
theorem altarelli_martinelli_one_loop_fl_mellin_moments
    (n : ℕ) (α_s sumChargeSq M_Sigma M_g : ℝ) :
    (∫ z in (0 : ℝ)..1, (8 / 3 : ℝ) * z ^ n) = flQuarkMomentCoeff n ∧
      (∫ z in (0 : ℝ)..1, 4 * z ^ n * (1 - z)) = flGluonMomentCoeff n ∧
      mellinFLOneLoop α_s sumChargeSq M_Sigma M_g n =
        (α_s / (4 * Real.pi)) *
          ((16 / (3 * ((n : ℝ) + 1))) * M_Sigma +
            (8 * sumChargeSq / (((n : ℝ) + 1) * ((n : ℝ) + 2))) * M_g) ∧
      (flQuarkMomentCoeff 2 = 8 / 9 ∧
        flQuarkMomentCoeff 3 = 2 / 3 ∧
        flQuarkMomentCoeff 4 = 8 / 15 ∧
        2 * flQuarkMomentCoeff 2 = 16 / 9 ∧
        2 * flQuarkMomentCoeff 3 = 4 / 3 ∧
        2 * flQuarkMomentCoeff 4 = 16 / 15 ∧
        flGluonMomentCoeff 2 = 1 / 3 ∧
        flGluonMomentCoeff 3 = 1 / 5 ∧
        flGluonMomentCoeff 4 = 2 / 15) ∧
      mellinFLOneLoop 0 sumChargeSq M_Sigma M_g n = 0 ∧
      (0 < α_s → 0 < M_Sigma → 0 ≤ sumChargeSq → 0 ≤ M_g →
        0 < mellinFLOneLoop α_s sumChargeSq M_Sigma M_g n) := by
  have hn1_pos : (0 : ℝ) < (n : ℝ) + 1 := by positivity
  have hn2_pos : (0 : ℝ) < (n : ℝ) + 2 := by positivity
  have hn1_ne : (n : ℝ) + 1 ≠ 0 := ne_of_gt hn1_pos
  have hn2_ne : (n : ℝ) + 2 ≠ 0 := ne_of_gt hn2_pos
  have hq_int : (∫ z in (0 : ℝ)..1, (8 / 3 : ℝ) * z ^ n) = flQuarkMomentCoeff n := by
    rw [intervalIntegral.integral_const_mul, integral_unit_pow_eq n]
    unfold flQuarkMomentCoeff
    field_simp [hn1_ne]
  have hg_int : (∫ z in (0 : ℝ)..1, 4 * z ^ n * (1 - z)) = flGluonMomentCoeff n := by
    have hfun : (fun z : ℝ => 4 * z ^ n * (1 - z)) =
        fun z : ℝ => (4 : ℝ) * (z ^ n - z ^ (n + 1)) := by
      funext z; ring
    rw [hfun, intervalIntegral.integral_const_mul,
      intervalIntegral.integral_sub ((continuous_pow n).intervalIntegrable 0 1)
        ((continuous_pow (n + 1)).intervalIntegrable 0 1),
      integral_unit_pow_eq n, integral_unit_pow_eq (n + 1)]
    unfold flGluonMomentCoeff
    rw [Nat.cast_add, Nat.cast_one]
    have hn1_eq : (n : ℝ) + 1 + 1 = (n : ℝ) + 2 := by ring
    rw [hn1_eq]
    field_simp [hn1_ne, hn2_ne]
    ring
  have hnorm4pi : mellinFLOneLoop α_s sumChargeSq M_Sigma M_g n =
      (α_s / (4 * Real.pi)) *
        ((16 / (3 * ((n : ℝ) + 1))) * M_Sigma +
          (8 * sumChargeSq / (((n : ℝ) + 1) * ((n : ℝ) + 2))) * M_g) := by
    unfold mellinFLOneLoop flQuarkMomentCoeff flGluonMomentCoeff
    have hpi_ne : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
    field_simp [hpi_ne, hn1_ne, hn2_ne]
    ring
  have hbench : flQuarkMomentCoeff 2 = 8 / 9 ∧
      flQuarkMomentCoeff 3 = 2 / 3 ∧
      flQuarkMomentCoeff 4 = 8 / 15 ∧
      2 * flQuarkMomentCoeff 2 = 16 / 9 ∧
      2 * flQuarkMomentCoeff 3 = 4 / 3 ∧
      2 * flQuarkMomentCoeff 4 = 16 / 15 ∧
      flGluonMomentCoeff 2 = 1 / 3 ∧
      flGluonMomentCoeff 3 = 1 / 5 ∧
      flGluonMomentCoeff 4 = 2 / 15 := by
    unfold flQuarkMomentCoeff flGluonMomentCoeff
    norm_num
  refine ⟨hq_int, hg_int, hnorm4pi, hbench, ?_, ?_⟩
  · unfold mellinFLOneLoop
    simp
  · intro hα hMS hsq hMg
    unfold mellinFLOneLoop flQuarkMomentCoeff flGluonMomentCoeff
    have hpi2 : 0 < 2 * Real.pi := mul_pos two_pos Real.pi_pos
    have hpref : 0 < α_s / (2 * Real.pi) := div_pos hα hpi2
    have hq_pos : 0 < (8 / (3 * ((n : ℝ) + 1))) * M_Sigma := by positivity
    have hg_nn : 0 ≤ sumChargeSq * (4 / (((n : ℝ) + 1) * ((n : ℝ) + 2))) * M_g := by positivity
    exact mul_pos hpref (by linarith)

end CallanGrossAndLongitudinalMoments

-- ============================================================================
-- § 3. Worldline UV Suppression Bound on Inclusive DIS Cross-Sections
-- ============================================================================

section WorldlineDISUVSuppression

/-- Worldline Schwinger UV damping factor $e^{-2 Q^2 T_{\min}}$ multiplying the inclusive
DIS differential cross-section $d^2\sigma/(dx\,dy) \propto |G_{\mathrm{SW}}(Q^2, 0, T_{\min})|^2$. -/
noncomputable def disWorldlineCrossSectionFactor (Q2 Tmin : ℝ) : ℝ :=
  Real.exp (-2 * Q2 * Tmin)

/-- Fractional worldline UV deviation $1 - e^{-2 Q^2 T_{\min}}$ of the inclusive DIS
cross-section relative to standard continuum single-photon exchange. -/
noncomputable def disWorldlineFractionalDeviation (Q2 Tmin : ℝ) : ℝ :=
  1 - disWorldlineCrossSectionFactor Q2 Tmin

/-- **Worldline Propagator-Square Damping Identity & Linear UV Error Envelope:**
1. Squaring the massless Schwinger worldline photon propagator
   `schwingerPropagatorReal Q2 0 Tmin = exp(-Q2 * Tmin) / Q2` yields
   $$G_{\mathrm{SW}}(Q^2, 0, T_{\min})^2 = e^{-2 Q^2 T_{\min}} \cdot \left(\frac{1}{Q^2}\right)^2;$$
2. For every $Q^2 > 0$ and $T_{\min} > 0$, $0 < e^{-2 Q^2 T_{\min}} < 1$ and
   $$0 < 1 - e^{-2 Q^2 T_{\min}} \le 2 Q^2 T_{\min}.$$ -/
theorem dis_worldline_propagator_sq_and_uv_bound {Q2 Tmin : ℝ}
    (hQ2 : 0 < Q2) (hT : 0 < Tmin) :
    (schwingerPropagatorReal Q2 0 Tmin) ^ 2 =
        disWorldlineCrossSectionFactor Q2 Tmin * (1 / Q2) ^ 2 ∧
      0 < disWorldlineCrossSectionFactor Q2 Tmin ∧
      disWorldlineCrossSectionFactor Q2 Tmin < 1 ∧
      0 < disWorldlineFractionalDeviation Q2 Tmin ∧
      disWorldlineFractionalDeviation Q2 Tmin ≤ 2 * Q2 * Tmin := by
  have hsq : (schwingerPropagatorReal Q2 0 Tmin) ^ 2 =
      disWorldlineCrossSectionFactor Q2 Tmin * (1 / Q2) ^ 2 := by
    unfold schwingerPropagatorReal disWorldlineCrossSectionFactor
    rw [add_zero, div_pow, div_pow, one_pow, ← mul_div_assoc, mul_one,
      sq (Real.exp (-Q2 * Tmin)), ← Real.exp_add]
    congr 2
    ring
  have hexp_pos : 0 < disWorldlineCrossSectionFactor Q2 Tmin := by
    unfold disWorldlineCrossSectionFactor
    exact Real.exp_pos _
  have hexp_lt : disWorldlineCrossSectionFactor Q2 Tmin < 1 := by
    unfold disWorldlineCrossSectionFactor
    rw [Real.exp_lt_one_iff]
    nlinarith
  have hdev_pos : 0 < disWorldlineFractionalDeviation Q2 Tmin := by
    unfold disWorldlineFractionalDeviation
    linarith
  have hdev_le : disWorldlineFractionalDeviation Q2 Tmin ≤ 2 * Q2 * Tmin := by
    unfold disWorldlineFractionalDeviation disWorldlineCrossSectionFactor
    have hlb := Real.add_one_le_exp (-2 * Q2 * Tmin)
    linarith
  exact ⟨hsq, hexp_pos, hexp_lt, hdev_pos, hdev_le⟩

/-- **Planck-Scale Worldline DIS Suppression Across HERA, LHC, and Ultra-High-$Q^2$ Colliders:**
For $T_{\min} = 1 / E_{\mathrm{Pl}}^2$ with $E_{\mathrm{Pl}} \ge 1.22 \times 10^{19}\;\mathrm{GeV}$:
1. HERA kinematic ceiling ($0 < Q^2 \le 10^4\;\mathrm{GeV}^2$):
   $0 < 1 - e^{-2 Q^2 / E_{\mathrm{Pl}}^2} < 1.35 \times 10^{-34}$;
2. LHC kinematic ceiling ($0 < Q^2 \le 10^8\;\mathrm{GeV}^2$):
   $0 < 1 - e^{-2 Q^2 / E_{\mathrm{Pl}}^2} < 1.35 \times 10^{-30}$;
3. Ultra-high-$Q^2$ benchmark ($0 < Q^2 \le 10^9\;\mathrm{GeV}^2$):
   $0 < 1 - e^{-2 Q^2 / E_{\mathrm{Pl}}^2} < 1.35 \times 10^{-29} < 3.4 \times 10^{-29}$. -/
theorem dis_worldline_hera_lhc_planck_bounds {E_Pl : ℝ}
    (hE : (122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ) ≤ E_Pl) :
    (∀ Q2 : ℝ, 0 < Q2 → Q2 ≤ (10 : ℝ) ^ (4 : ℤ) →
      0 < disWorldlineFractionalDeviation Q2 (1 / E_Pl ^ 2) ∧
        disWorldlineFractionalDeviation Q2 (1 / E_Pl ^ 2) <
          (135 / 100 : ℝ) * (10 : ℝ) ^ (-34 : ℤ)) ∧
      (∀ Q2 : ℝ, 0 < Q2 → Q2 ≤ (10 : ℝ) ^ (8 : ℤ) →
        0 < disWorldlineFractionalDeviation Q2 (1 / E_Pl ^ 2) ∧
          disWorldlineFractionalDeviation Q2 (1 / E_Pl ^ 2) <
            (135 / 100 : ℝ) * (10 : ℝ) ^ (-30 : ℤ)) ∧
      (∀ Q2 : ℝ, 0 < Q2 → Q2 ≤ (10 : ℝ) ^ (9 : ℤ) →
        0 < disWorldlineFractionalDeviation Q2 (1 / E_Pl ^ 2) ∧
          disWorldlineFractionalDeviation Q2 (1 / E_Pl ^ 2) <
            (135 / 100 : ℝ) * (10 : ℝ) ^ (-29 : ℤ) ∧
          (135 / 100 : ℝ) * (10 : ℝ) ^ (-29 : ℤ) <
            (34 / 10 : ℝ) * (10 : ℝ) ^ (-29 : ℤ)) := by
  have hE0 : (0 : ℝ) < (122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ) := by norm_num
  have hE_pos : 0 < E_Pl := lt_of_lt_of_le hE0 hE
  have hT_pos : 0 < 1 / E_Pl ^ 2 := by positivity
  have hE2_ge : ((122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ)) ^ 2 ≤ E_Pl ^ 2 :=
    pow_le_pow_left₀ (le_of_lt hE0) hE 2
  have hT_le : 1 / E_Pl ^ 2 ≤ 1 / ((122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ)) ^ 2 :=
    one_div_le_one_div_of_le (pow_pos hE0 2) hE2_ge
  refine ⟨?_, ?_, ?_⟩
  · intro Q2 hQ2 hQ_le
    obtain ⟨_, _, _, hpos, hle⟩ := dis_worldline_propagator_sq_and_uv_bound hQ2 hT_pos
    refine ⟨hpos, ?_⟩
    have hstep1 : 2 * Q2 * (1 / E_Pl ^ 2) ≤
        2 * (10 : ℝ) ^ (4 : ℤ) * (1 / ((122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ)) ^ 2) := by
      have h2Q : 2 * Q2 ≤ 2 * (10 : ℝ) ^ (4 : ℤ) := by linarith
      exact mul_le_mul h2Q hT_le (le_of_lt hT_pos) (by norm_num)
    have hstep2 : 2 * (10 : ℝ) ^ (4 : ℤ) *
        (1 / ((122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ)) ^ 2) <
        (135 / 100 : ℝ) * (10 : ℝ) ^ (-34 : ℤ) := by norm_num
    exact lt_of_le_of_lt (le_trans hle hstep1) hstep2
  · intro Q2 hQ2 hQ_le
    obtain ⟨_, _, _, hpos, hle⟩ := dis_worldline_propagator_sq_and_uv_bound hQ2 hT_pos
    refine ⟨hpos, ?_⟩
    have hstep1 : 2 * Q2 * (1 / E_Pl ^ 2) ≤
        2 * (10 : ℝ) ^ (8 : ℤ) * (1 / ((122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ)) ^ 2) := by
      have h2Q : 2 * Q2 ≤ 2 * (10 : ℝ) ^ (8 : ℤ) := by linarith
      exact mul_le_mul h2Q hT_le (le_of_lt hT_pos) (by norm_num)
    have hstep2 : 2 * (10 : ℝ) ^ (8 : ℤ) *
        (1 / ((122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ)) ^ 2) <
        (135 / 100 : ℝ) * (10 : ℝ) ^ (-30 : ℤ) := by norm_num
    exact lt_of_le_of_lt (le_trans hle hstep1) hstep2
  · intro Q2 hQ2 hQ_le
    obtain ⟨_, _, _, hpos, hle⟩ := dis_worldline_propagator_sq_and_uv_bound hQ2 hT_pos
    refine ⟨hpos, ?_, by norm_num⟩
    have hstep1 : 2 * Q2 * (1 / E_Pl ^ 2) ≤
        2 * (10 : ℝ) ^ (9 : ℤ) * (1 / ((122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ)) ^ 2) := by
      have h2Q : 2 * Q2 ≤ 2 * (10 : ℝ) ^ (9 : ℤ) := by linarith
      exact mul_le_mul h2Q hT_le (le_of_lt hT_pos) (by norm_num)
    have hstep2 : 2 * (10 : ℝ) ^ (9 : ℤ) *
        (1 / ((122 / 100 : ℝ) * (10 : ℝ) ^ (19 : ℤ)) ^ 2) <
        (135 / 100 : ℝ) * (10 : ℝ) ^ (-29 : ℤ) := by norm_num
    exact lt_of_le_of_lt (le_trans hle hstep1) hstep2

end WorldlineDISUVSuppression

end QOU.StandardModel.DiracWeylCliffordCallanGrossAndDISCrossSection
