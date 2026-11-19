/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# Infrared QFT Subsumption, Chiral Gauge Beta Multiplicities, $(g-2)_\ell$ Planck Decoupling, and Borromean Parton Moments

This module formalizes four structural theorems connecting the $q$-deformed braided Standard Model
substrate to perturbative relativistic quantum field theory and non-perturbative parton structure:

1. **Section 1 — Braid-to-Chord Perturbative Jet & Jimbo–Kohno–Drinfeld Infinitesimal 4T Identity:**
   - Defines the explicit $4 \times 4$ Jimbo $\mathfrak{sl}_2$ braided $R$-matrix `jimboRCheck q qinv`
     on `Fin 2 × Fin 2` over any commutative ring $R$, proving its classical flip limit
     `jimboRCheck 1 1 = swapMat2`, its exact quadratic Hecke relation
     `(jimboRCheck q qinv)^2 = (q - qinv) • jimboRCheck q qinv + 1` whenever `q * qinv = 1`,
     and its exact 3-strand braided Yang–Baxter relation on `Fin 2 × Fin 2 × Fin 2` ($M_8(R)$).
   - Expands the first-order perturbative jet `jimboRCheckJet h := jimboRCheck (1 + h) (1 - h) = P + h • J`,
     showing that symmetrizing the first-order $R$-derivative (`P * J + J * P = 2 • P`) or taking
     the pure-braid holonomy jet `(jimboRCheckJet h)^2 = 1 + (2 * h) • P + h^2 • J^2` extracts the
     chord/Casimir generator.
   - Embeds both the $\mathfrak{gl}_2$ permutation chord operators $(\Omega_{12}, \Omega_{23}, \Omega_{13})$
     and the traceless $\mathfrak{sl}_2$ Casimir chord operators
     $(\tilde{\Omega}_{12}, \tilde{\Omega}_{23}, \tilde{\Omega}_{13})$ ($\tilde{\Omega}_{ij} = 2\Omega_{ij} - I_8$)
     into $M_8(R)$ (`Fin 2 × Fin 2 × Fin 2`) and proves the **exact Kohno–Drinfeld / Vassiliev–Bar-Natan
     infinitesimal 4T chord commutator identities**:
     $$[\Omega_{12},\; \Omega_{13} + \Omega_{23}] = 0, \qquad
       [\Omega_{23},\; \Omega_{12} + \Omega_{13}] = 0, \qquad
       [\tilde{\Omega}_{12},\; \tilde{\Omega}_{13} + \tilde{\Omega}_{23}] = 0, \qquad
       [\tilde{\Omega}_{23},\; \tilde{\Omega}_{12} + \tilde{\Omega}_{13}] = 0.$$

2. **Section 2 — One-Loop Gauge Beta-Function Multiplicities from $\mathcal{S}_{\mathrm{chiral}}$
   (Gross–Politzer–Wilczek Asymptotic Freedom):**
   - Encodes the five chiral Weyl multiplets of one Standard Model generation
     $\mathcal{S}_{\mathrm{chiral}} = \{Q_L(3,2,\tfrac{1}{6}),\, u_R^c(\bar{3},1,-\tfrac{2}{3}),\,
     d_R^c(\bar{3},1,\tfrac{1}{3}),\, L_L(1,2,-\tfrac{1}{2}),\, e_R^c(1,1,1)\}$ (15 Weyl states,
     with exact cancellation of all four gauge/gravitational anomalies) together with $N_H$ complex
     Higgs doublets $(1, 2, \tfrac{1}{2})$.
   - Derives the exact rational 1-loop Dynkin beta coefficients
     $$b_3(N_{\mathrm{gen}}) = 11 - \frac{4}{3}N_{\mathrm{gen}}, \quad
       b_2(N_{\mathrm{gen}}, N_H) = \frac{22}{3} - \frac{4}{3}N_{\mathrm{gen}} - \frac{1}{6}N_H, \quad
       b_1(N_{\mathrm{gen}}, N_H) = -\frac{4}{3}N_{\mathrm{gen}} - \frac{1}{10}N_H,$$
     proving $b_3(3) = 7 > 0$, $b_3(N_{\mathrm{gen}}) > 0 \iff N_{\mathrm{gen}} \le 8$ ($n_f \le 16$),
     $b_2(3, 1) = \frac{19}{6} > 0$, $b_1(3, 1) = -\frac{41}{10} < 0$, the exact 1-loop RG
     inverse-coupling evolution law, and strict ultraviolet asymptotic freedom
     $\alpha_3(\mu_2) < \alpha_3(\mu_1)$ for $0 < \mu_1 < \mu_2$.

3. **Section 3 — Schwinger–Kinoshita Perturbative $(g - 2)_\ell$ Series & Weinberg EFT Planck Decoupling:**
   - Formalizes the 5-loop QED anomalous magnetic moment polynomial
     $a_\ell^{(5)}(\alpha; C_1, \dots, C_5) = \sum_{k=1}^5 C_k (\alpha/\pi)^k$ anchored at Schwinger's
     $C_1 = \tfrac{1}{2}$, proving exact 1-loop Lipschitz sensitivity
     $|a_\ell^{(1)}(\alpha_1) - a_\ell^{(1)}(\alpha_2)| = \frac{|\alpha_1 - \alpha_2|}{2\pi}$ and the
     constructive Planck-decoupling bound: for $0 < m_e \le 10^{-3}\;\mathrm{GeV}$ and
     $E_* \ge 10^{19}\;\mathrm{GeV}$, $(m_e / E_*)^2 \le 10^{-44} < 10^{-13}$.

4. **Section 4 — Non-Perturbative Borromean Proton Valence Momentum Asymmetry & 1-Loop DGLAP Moments:**
   - Formalizes the exact rational 1-loop non-singlet QCD Mellin anomalous dimensions
     $\gamma_n^{\mathrm{NS}} = \frac{4}{3}\bigl(4 H_n - 3 - \frac{2}{n(n+1)}\bigr)$, proving exact
     valence baryon-number conservation $\gamma_1^{\mathrm{NS}} = 0$, exact values
     $(\gamma_2^{\mathrm{NS}}, \gamma_3^{\mathrm{NS}}, \gamma_4^{\mathrm{NS}}) =
     (\frac{32}{9}, \frac{50}{9}, \frac{314}{45})$, strict monotonicity and positivity
     $\gamma_n^{\mathrm{NS}} > 0$ for **all** $n \ge 2$, and strict DGLAP ultraviolet moment softening
     $M_n(Q^2) < M_n(\mu_0^2)$ for all $n \ge 2$ when $Q > \mu_0 > 0$.
   - Proves on the 3-strand Jucys–Murphy spectrum $(1, q^2, q^4)$ of $[u, u, d] \in H_3(q)$ that
     both the palindromic assignment $\frac{1 + q^4}{q^2} = q^2 + q^{-2}$ and the top-two assignment
     $q^2(1 + q^2)$ reduce to the $\mathrm{SU}(6)$ ratio $2$ at $q = 1$ and strictly satisfy
     $w_u(q) / w_d(q) > 2$ across the deformed regime $q > 1$.
-/

namespace QOU.StandardModel.InfraredQFTSubsumptionAndPartonMoments

open scoped BigOperators Matrix

-- ============================================================================
-- § 1. Braid-to-Chord Perturbative Jet & Infinitesimal 4T Chord Relations
-- ============================================================================

section BraidToChordJet

/-- Two-strand tensor basis `Fin 2 × Fin 2`. -/
abbrev TwoStrand := Fin 2 × Fin 2

/-- Three-strand tensor basis `Fin 2 × Fin 2 × Fin 2`. -/
abbrev ThreeStrand := Fin 2 × Fin 2 × Fin 2

/-- Matrix commutator `[A, B] = A * B - B * A`. -/
def matComm {I R : Type*} [Fintype I] [DecidableEq I] [Ring R]
    (A B : Matrix I I R) : Matrix I I R :=
  A * B - B * A

/-- Permutation matrix associated to $\sigma \in \mathrm{Perm}(I)$ on a finite index type $I$. -/
def permMat (R : Type*) [CommRing R] {I : Type*} [Fintype I] [DecidableEq I]
    (σ : Equiv.Perm I) : Matrix I I R :=
  Matrix.of fun i j => if σ i = j then 1 else 0

/-- Multiplication of permutation matrices satisfies `permMat σ * permMat τ = permMat (σ.trans τ)`
over any commutative ring $R$, with zero case-splitting on index cardinality. -/
theorem permMat_mul (R : Type*) [CommRing R] {I : Type*} [Fintype I] [DecidableEq I]
    (σ τ : Equiv.Perm I) :
    permMat R σ * permMat R τ = permMat R (σ.trans τ) := by
  ext i k
  simp only [permMat, Matrix.mul_apply, Matrix.of_apply, Equiv.trans_apply]
  rw [Finset.sum_eq_single (σ i)]
  · simp
  · intro b _ hb
    have hne : σ i ≠ b := hb.symm
    simp [hne]
  · intro hmem
    exact absurd (Finset.mem_univ (σ i)) hmem

/-- Universal matrix commutator identity for shifted operators `(2 : R) • A - 1`. -/
theorem matComm_two_smul_sub_one {I R : Type*} [Fintype I] [DecidableEq I] [CommRing R]
    (A B C : Matrix I I R) :
    matComm ((2 : R) • A - 1) (((2 : R) • B - 1) + ((2 : R) • C - 1)) =
      (4 : R) • matComm A (B + C) ∧
      matComm ((2 : R) • A - 1) ((2 : R) • B - 1) =
        (4 : R) • matComm A B := by
  constructor
  · unfold matComm
    simp only [sub_mul, mul_sub, add_mul, mul_add, one_mul, mul_one,
      Matrix.smul_mul, Matrix.mul_smul, smul_smul]
    ext i j
    simp only [Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
    ring
  · unfold matComm
    simp only [sub_mul, mul_sub, one_mul, mul_one,
      Matrix.smul_mul, Matrix.mul_smul, smul_smul]
    ext i j
    simp only [Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]
    ring

/-- Classical tensor flip $P(e_a \otimes e_b) = e_b \otimes e_a$ on `Fin 2 × Fin 2`. -/
def swapMat2 (R : Type*) [CommRing R] : Matrix TwoStrand TwoStrand R :=
  Matrix.of fun (a, b) (c, d) =>
    (![![![![1, 0], ![0, 0]], ![![0, 0], ![1, 0]]],
       ![![![0, 1], ![0, 0]], ![![0, 0], ![0, 1]]]] :
      Fin 2 → Fin 2 → Fin 2 → Fin 2 → R) a b c d

/-- Explicit $4 \times 4$ Jimbo $\mathfrak{sl}_2$ braided $R$-matrix $\check{R}(q, q^{-1})$ on
`Fin 2 × Fin 2`: diagonal entries $q$ on $(0,0)$ and $(1,1)$, Hecke block
$\begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}$ on $\{(0,1), (1,0)\}$. -/
def jimboRCheck {R : Type*} [CommRing R] (q qinv : R) : Matrix TwoStrand TwoStrand R :=
  Matrix.of fun (a, b) (c, d) =>
    (![![![![q, 0], ![0, 0]], ![![0, q - qinv], ![1, 0]]],
       ![![![0, 1], ![0, 0]], ![![0, 0], ![0, q]]]] :
      Fin 2 → Fin 2 → Fin 2 → Fin 2 → R) a b c d

/-- Infinitesimal $(q - 1)$ derivative matrix $J = \left.\frac{d}{dh}\check{R}(1 + h, 1 - h)\right|_{h=0}$
on `Fin 2 × Fin 2`. -/
def jimboJetDeriv (R : Type*) [CommRing R] : Matrix TwoStrand TwoStrand R :=
  Matrix.of fun (a, b) (c, d) =>
    (![![![![1, 0], ![0, 0]], ![![0, 2], ![0, 0]]],
       ![![![0, 0], ![0, 0]], ![![0, 0], ![0, 1]]]] :
      Fin 2 → Fin 2 → Fin 2 → Fin 2 → R) a b c d

/-- First-order braided $R$-matrix jet $\check{R}^{(1)}(h) = \check{R}(1 + h, 1 - h)$
over any commutative ring $R$. -/
def jimboRCheckJet {R : Type*} [CommRing R] (h : R) : Matrix TwoStrand TwoStrand R :=
  jimboRCheck (1 + h) (1 - h)

/-- Embed a 2-strand matrix $M$ on strands $(1, 2)$ of `Fin 2 × Fin 2 × Fin 2`: $M \otimes I_2$. -/
def lift12 {R : Type*} [CommRing R] (M : Matrix TwoStrand TwoStrand R) :
    Matrix ThreeStrand ThreeStrand R :=
  Matrix.of fun (i₁, i₂, i₃) (j₁, j₂, j₃) =>
    if i₃ = j₃ then M (i₁, i₂) (j₁, j₂) else 0

/-- Embed a 2-strand matrix $M$ on strands $(2, 3)$ of `Fin 2 × Fin 2 × Fin 2`: $I_2 \otimes M$. -/
def lift23 {R : Type*} [CommRing R] (M : Matrix TwoStrand TwoStrand R) :
    Matrix ThreeStrand ThreeStrand R :=
  Matrix.of fun (i₁, i₂, i₃) (j₁, j₂, j₃) =>
    if i₁ = j₁ then M (i₂, i₃) (j₂, j₃) else 0

/-- Symbolic index-contraction lemma for `(lift12 A * lift23 B)` eliminating two of the three
intermediate `Fin 2` sums analytically. -/
theorem lift12_mul_lift23_apply {R : Type*} [CommRing R]
    (A B : Matrix TwoStrand TwoStrand R) (i₁ i₂ i₃ k₁ k₂ k₃ : Fin 2) :
    (lift12 A * lift23 B) (i₁, i₂, i₃) (k₁, k₂, k₃) =
      ∑ u₂ : Fin 2, A (i₁, i₂) (k₁, u₂) * B (u₂, i₃) (k₂, k₃) := by
  simp only [Matrix.mul_apply, Fintype.sum_prod_type, lift12, lift23, Matrix.of_apply]
  rw [Finset.sum_eq_single k₁]
  · apply Finset.sum_congr rfl
    intro u₂ _
    rw [Finset.sum_eq_single i₃]
    · simp
    · intro u₃ _ hu₃
      have hne : i₃ ≠ u₃ := hu₃.symm
      simp [hne]
    · intro hmem
      exact absurd (Finset.mem_univ i₃) hmem
  · intro u₁ _ hu₁
    apply Finset.sum_eq_zero
    intro u₂ _
    apply Finset.sum_eq_zero
    intro u₃ _
    simp [hu₁]
  · intro hmem
    exact absurd (Finset.mem_univ k₁) hmem

/-- Symbolic index-contraction lemma for `(lift23 A * lift12 B)` eliminating two of the three
intermediate `Fin 2` sums analytically. -/
theorem lift23_mul_lift12_apply {R : Type*} [CommRing R]
    (A B : Matrix TwoStrand TwoStrand R) (i₁ i₂ i₃ k₁ k₂ k₃ : Fin 2) :
    (lift23 A * lift12 B) (i₁, i₂, i₃) (k₁, k₂, k₃) =
      ∑ u₂ : Fin 2, A (i₂, i₃) (u₂, k₃) * B (i₁, u₂) (k₁, k₂) := by
  simp only [Matrix.mul_apply, Fintype.sum_prod_type, lift12, lift23, Matrix.of_apply]
  rw [Finset.sum_eq_single i₁]
  · apply Finset.sum_congr rfl
    intro u₂ _
    rw [Finset.sum_eq_single k₃]
    · simp
    · intro u₃ _ hu₃
      simp [hu₃]
    · intro hmem
      exact absurd (Finset.mem_univ k₃) hmem
  · intro u₁ _ hu₁
    have hne : i₁ ≠ u₁ := hu₁.symm
    apply Finset.sum_eq_zero
    intro u₂ _
    apply Finset.sum_eq_zero
    intro u₃ _
    simp [hne]
  · intro hmem
    exact absurd (Finset.mem_univ i₁) hmem

/-- Coordinate transposition $(1\;2)$ on `ThreeStrand`. -/
def perm12 : Equiv.Perm ThreeStrand where
  toFun := fun (a, b, c) => (b, a, c)
  invFun := fun (a, b, c) => (b, a, c)
  left_inv := fun ⟨_, _, _⟩ => rfl
  right_inv := fun ⟨_, _, _⟩ => rfl

/-- Coordinate transposition $(2\;3)$ on `ThreeStrand`. -/
def perm23 : Equiv.Perm ThreeStrand where
  toFun := fun (a, b, c) => (a, c, b)
  invFun := fun (a, b, c) => (a, c, b)
  left_inv := fun ⟨_, _, _⟩ => rfl
  right_inv := fun ⟨_, _, _⟩ => rfl

/-- Coordinate transposition $(1\;3)$ on `ThreeStrand`. -/
def perm13 : Equiv.Perm ThreeStrand where
  toFun := fun (a, b, c) => (c, b, a)
  invFun := fun (a, b, c) => (c, b, a)
  left_inv := fun ⟨_, _, _⟩ => rfl
  right_inv := fun ⟨_, _, _⟩ => rfl

/-- Three-strand $\mathfrak{gl}_2$ chord operators $\Omega_{12}, \Omega_{23}, \Omega_{13} \in M_8(R)$
extracted from the symmetrized first-order $R$-matrix jet. -/
def chordOmega12 (R : Type*) [CommRing R] : Matrix ThreeStrand ThreeStrand R :=
  permMat R perm12

def chordOmega23 (R : Type*) [CommRing R] : Matrix ThreeStrand ThreeStrand R :=
  permMat R perm23

def chordOmega13 (R : Type*) [CommRing R] : Matrix ThreeStrand ThreeStrand R :=
  permMat R perm13

/-- Traceless $\mathfrak{sl}_2$ quadratic Casimir matrix $2\Omega^{\mathfrak{sl}_2} = 2 P - I_4$
on `Fin 2 × Fin 2` (clearing the denominator $2$ so all entries lie in $\mathbb{Z}$). -/
def sl2CasimirTwo (R : Type*) [CommRing R] : Matrix TwoStrand TwoStrand R :=
  (2 : R) • swapMat2 R - 1

/-- Three-strand traceless $\mathfrak{sl}_2$ Casimir chord operators
$\tilde{\Omega}_{12}, \tilde{\Omega}_{23}, \tilde{\Omega}_{13} \in M_8(R)$. -/
def sl2Chord12 (R : Type*) [CommRing R] : Matrix ThreeStrand ThreeStrand R :=
  (2 : R) • chordOmega12 R - 1

def sl2Chord23 (R : Type*) [CommRing R] : Matrix ThreeStrand ThreeStrand R :=
  (2 : R) • chordOmega23 R - 1

def sl2Chord13 (R : Type*) [CommRing R] : Matrix ThreeStrand ThreeStrand R :=
  (2 : R) • chordOmega13 R - 1

/-- Agreement of `chordOmega12` and `chordOmega23` with the tensor-product embeddings
`lift12 (swapMat2 R)` and `lift23 (swapMat2 R)`. -/
theorem chordOmega_eq_lift_swap (R : Type*) [CommRing R] :
    chordOmega12 R = lift12 (swapMat2 R) ∧
      chordOmega23 R = lift23 (swapMat2 R) := by
  constructor
  · ext ⟨i₁, i₂, i₃⟩ ⟨j₁, j₂, j₃⟩
    fin_cases i₁ <;> fin_cases i₂ <;> fin_cases i₃ <;>
      fin_cases j₁ <;> fin_cases j₂ <;> fin_cases j₃ <;>
      simp [chordOmega12, permMat, perm12, lift12, swapMat2]
  · ext ⟨i₁, i₂, i₃⟩ ⟨j₁, j₂, j₃⟩
    fin_cases i₁ <;> fin_cases i₂ <;> fin_cases i₃ <;>
      fin_cases j₁ <;> fin_cases j₂ <;> fin_cases j₃ <;>
      simp [chordOmega23, permMat, perm23, lift23, swapMat2]

/-- At the classical point $q = q^{-1} = 1$, `jimboRCheck 1 1` reduces to the tensor flip `swapMat2`,
which is involutive (`P^2 = 1`). -/
theorem jimboRCheck_at_one_and_swap_involutive (R : Type*) [CommRing R] :
    jimboRCheck (1 : R) 1 = swapMat2 R ∧
      swapMat2 R * swapMat2 R = 1 := by
  constructor
  · ext ⟨a, b⟩ ⟨c, d⟩
    fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
      simp [jimboRCheck, swapMat2]
  · ext ⟨a, b⟩ ⟨c, d⟩
    simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, Matrix.one_apply,
      Prod.mk.injEq]
    fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
      simp [swapMat2]

/-- **Exact Quadratic Hecke Relation for Jimbo's $R$-Matrix:**
Whenever $q \cdot q^{-1} = 1$ in $R$, $\check{R}(q, q^{-1})^2 = (q - q^{-1})\check{R}(q, q^{-1}) + I_4$. -/
theorem jimboRCheck_hecke_quadratic {R : Type*} [CommRing R] {q qinv : R}
    (hunit : q * qinv = 1) :
    jimboRCheck q qinv * jimboRCheck q qinv =
      (q - qinv) • jimboRCheck q qinv + 1 := by
  ext ⟨a, b⟩ ⟨c, d⟩
  simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
    Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, Prod.mk.injEq, smul_eq_mul]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp only [jimboRCheck, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one,
      and_self, and_false, false_and, ↓reduceIte, Fin.zero_eta, Fin.mk_one,
      Fin.isValue, zero_ne_one, one_ne_zero] <;>
    first | ring1 | linear_combination hunit

/-- **Exact 3-Strand Braided Yang–Baxter Identity for Jimbo's $R$-Matrix:**
Whenever $q \cdot q^{-1} = 1$ in $R$,
$\check{R}_{12} \check{R}_{23} \check{R}_{12} = \check{R}_{23} \check{R}_{12} \check{R}_{23}$ on $M_8(R)$. -/
theorem jimboRCheck_braided_yang_baxter {R : Type*} [CommRing R] {q qinv : R}
    (hunit : q * qinv = 1) :
    lift12 (jimboRCheck q qinv) * lift23 (jimboRCheck q qinv) * lift12 (jimboRCheck q qinv) =
      lift23 (jimboRCheck q qinv) * lift12 (jimboRCheck q qinv) * lift23 (jimboRCheck q qinv) := by
  ext ⟨i₁, i₂, i₃⟩ ⟨j₁, j₂, j₃⟩
  have hlhs :
      (lift12 (jimboRCheck q qinv) * lift23 (jimboRCheck q qinv) * lift12 (jimboRCheck q qinv))
          (i₁, i₂, i₃) (j₁, j₂, j₃) =
        ∑ v₁ : Fin 2, ∑ v₂ : Fin 2,
          (∑ u₂ : Fin 2, jimboRCheck q qinv (i₁, i₂) (v₁, u₂) *
            jimboRCheck q qinv (u₂, i₃) (v₂, j₃)) *
          jimboRCheck q qinv (v₁, v₂) (j₁, j₂) := by
    rw [Matrix.mul_apply]
    simp_rw [Fintype.sum_prod_type]
    apply Finset.sum_congr rfl; intro v₁ _
    apply Finset.sum_congr rfl; intro v₂ _
    rw [Finset.sum_eq_single j₃]
    · rw [lift12_mul_lift23_apply]
      simp [lift12]
    · intro v₃ _ hv₃
      simp [lift12, hv₃]
    · intro hmem; exact absurd (Finset.mem_univ j₃) hmem
  have hrhs :
      (lift23 (jimboRCheck q qinv) * lift12 (jimboRCheck q qinv) * lift23 (jimboRCheck q qinv))
          (i₁, i₂, i₃) (j₁, j₂, j₃) =
        ∑ v₂ : Fin 2, ∑ v₃ : Fin 2,
          (∑ u₂ : Fin 2, jimboRCheck q qinv (i₂, i₃) (u₂, v₃) *
            jimboRCheck q qinv (i₁, u₂) (j₁, v₂)) *
          jimboRCheck q qinv (v₂, v₃) (j₂, j₃) := by
    rw [Matrix.mul_apply]
    simp_rw [Fintype.sum_prod_type]
    rw [Finset.sum_eq_single j₁]
    · apply Finset.sum_congr rfl; intro v₂ _
      apply Finset.sum_congr rfl; intro v₃ _
      rw [lift23_mul_lift12_apply]
      simp [lift23]
    · intro v₁ _ hv₁
      apply Finset.sum_eq_zero; intro v₂ _
      apply Finset.sum_eq_zero; intro v₃ _
      simp [lift23, hv₁]
    · intro hmem; exact absurd (Finset.mem_univ j₁) hmem
  rw [hlhs, hrhs]
  simp only [Fin.sum_univ_two, jimboRCheck, Matrix.of_apply]
  fin_cases i₁ <;> fin_cases i₂ <;> fin_cases i₃ <;>
    fin_cases j₁ <;> fin_cases j₂ <;> fin_cases j₃ <;>
    simp only [Fin.zero_eta, Fin.mk_one, Fin.isValue, Matrix.cons_val_zero,
      Matrix.cons_val_one] <;>
    first | ring1 | linear_combination (q - qinv) * hunit | linear_combination -(q - qinv) * hunit

/-- **Perturbative Jet Decomposition & Chord Extraction (`q = 1 + h`):**
1. $\check{R}^{(1)}(h) = P + h \cdot J$,
2. Symmetrizing the first-order jet derivative with the flip $P$ extracts twice the chord operator:
   $P J + J P = 2 P$,
3. Over any commutative ring $R$, the pure-braid square $\check{R}^{(1)}(h)^2$ expands as
   $I_4 + (2h) P + h^2 \cdot J^2$, isolating $2 P$ as the exact linear coefficient in $h$,
4. The $\mathfrak{sl}_2$ Casimir matrix `sl2CasimirTwo R` has trace $0$. -/
theorem jimboRCheckJet_expansion_and_chord_extraction {R : Type*} [CommRing R] (h : R) :
    jimboRCheckJet h = swapMat2 R + h • jimboJetDeriv R ∧
      swapMat2 R * jimboJetDeriv R + jimboJetDeriv R * swapMat2 R = (2 : R) • swapMat2 R ∧
      jimboRCheckJet h * jimboRCheckJet h =
        1 + (2 * h) • swapMat2 R + (h ^ 2) • (jimboJetDeriv R * jimboJetDeriv R) ∧
      Matrix.trace (sl2CasimirTwo R) = 0 := by
  have h1 : jimboRCheckJet h = swapMat2 R + h • jimboJetDeriv R := by
    ext ⟨a, b⟩ ⟨c, d⟩
    simp only [jimboRCheckJet, jimboRCheck, swapMat2, jimboJetDeriv, Matrix.add_apply,
      Matrix.smul_apply, Matrix.of_apply, smul_eq_mul]
    fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
      simp only [Fin.zero_eta, Fin.mk_one, Fin.isValue, Matrix.cons_val_zero,
        Matrix.cons_val_one] <;> ring
  have h2 : swapMat2 R * jimboJetDeriv R + jimboJetDeriv R * swapMat2 R =
      (2 : R) • swapMat2 R := by
    ext ⟨a, b⟩ ⟨c, d⟩
    simp only [Matrix.add_apply, Matrix.smul_apply, Matrix.mul_apply,
      Fintype.sum_prod_type, Fin.sum_univ_two, smul_eq_mul, swapMat2, jimboJetDeriv,
      Matrix.of_apply]
    fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
      simp only [Fin.zero_eta, Fin.mk_one, Fin.isValue, Matrix.cons_val_zero,
        Matrix.cons_val_one] <;> ring
  have h3 : jimboRCheckJet h * jimboRCheckJet h =
      1 + (2 * h) • swapMat2 R + (h ^ 2) • (jimboJetDeriv R * jimboJetDeriv R) := by
    rw [h1, add_mul, mul_add, mul_add, (jimboRCheck_at_one_and_swap_involutive R).2]
    have hsmul1 : swapMat2 R * (h • jimboJetDeriv R) = h • (swapMat2 R * jimboJetDeriv R) :=
      Matrix.mul_smul _ _ _
    have hsmul2 : (h • jimboJetDeriv R) * swapMat2 R = h • (jimboJetDeriv R * swapMat2 R) :=
      Matrix.smul_mul _ _ _
    have hsmul3 : (h • jimboJetDeriv R) * (h • jimboJetDeriv R) =
        (h ^ 2) • (jimboJetDeriv R * jimboJetDeriv R) := by
      rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, sq]
    rw [hsmul1, hsmul2, hsmul3, add_assoc (1 : Matrix TwoStrand TwoStrand R),
      ← add_assoc (h • (swapMat2 R * jimboJetDeriv R)), ← smul_add, h2, smul_smul,
      mul_comm h 2, ← add_assoc]
  have h4 : Matrix.trace (sl2CasimirTwo R) = 0 := by
    simp only [sl2CasimirTwo, Matrix.trace, Matrix.diag, Fintype.sum_prod_type, Fin.sum_univ_two,
      Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply, ↓reduceIte, smul_eq_mul, swapMat2,
      Matrix.of_apply, Fin.isValue, Matrix.cons_val_zero, Matrix.cons_val_one]
    ring
  exact ⟨h1, h2, h3, h4⟩

/-- **Kohno–Drinfeld / Vassiliev–Bar-Natan Infinitesimal 4T Chord Commutator Theorem:**
On the 3-strand tensor cube $M_8(R)$ (`Fin 2 × Fin 2 × Fin 2`) over any commutative ring $R$, both
the $\mathfrak{gl}_2$ chord generators $(\Omega_{12}, \Omega_{23}, \Omega_{13})$ and the traceless
$\mathfrak{sl}_2$ Casimir chord generators $(\tilde{\Omega}_{12}, \tilde{\Omega}_{23}, \tilde{\Omega}_{13})$
satisfy all infinitesimal 4T braid-chord commutator relations:
1. $[\Omega_{12},\; \Omega_{13} + \Omega_{23}] = 0$,
2. $[\Omega_{23},\; \Omega_{12} + \Omega_{13}] = 0$,
3. $[\Omega_{13},\; \Omega_{12} + \Omega_{23}] = 0$,
4. $[\tilde{\Omega}_{12},\; \tilde{\Omega}_{13} + \tilde{\Omega}_{23}] = 0$ and
   $[\tilde{\Omega}_{23},\; \tilde{\Omega}_{12} + \tilde{\Omega}_{13}] = 0$. -/
theorem infinitesimal_four_term_chord_relations (R : Type*) [CommRing R] :
    matComm (chordOmega12 R) (chordOmega13 R + chordOmega23 R) = 0 ∧
      matComm (chordOmega23 R) (chordOmega12 R + chordOmega13 R) = 0 ∧
      matComm (chordOmega13 R) (chordOmega12 R + chordOmega23 R) = 0 ∧
      matComm (sl2Chord12 R) (sl2Chord13 R + sl2Chord23 R) = 0 ∧
      matComm (sl2Chord23 R) (sl2Chord12 R + sl2Chord13 R) = 0 := by
  have hp12_13 : chordOmega12 R * chordOmega13 R = chordOmega23 R * chordOmega12 R := by
    unfold chordOmega12 chordOmega13 chordOmega23
    rw [permMat_mul, permMat_mul]
    congr 1
  have hp12_23 : chordOmega12 R * chordOmega23 R = chordOmega13 R * chordOmega12 R := by
    unfold chordOmega12 chordOmega13 chordOmega23
    rw [permMat_mul, permMat_mul]
    congr 1
  have hp23_12 : chordOmega23 R * chordOmega12 R = chordOmega13 R * chordOmega23 R := by
    unfold chordOmega12 chordOmega13 chordOmega23
    rw [permMat_mul, permMat_mul]
    congr 1
  have hp23_13 : chordOmega23 R * chordOmega13 R = chordOmega12 R * chordOmega23 R := by
    unfold chordOmega12 chordOmega13 chordOmega23
    rw [permMat_mul, permMat_mul]
    congr 1
  have hp13_12 : chordOmega13 R * chordOmega12 R = chordOmega23 R * chordOmega13 R := by
    unfold chordOmega12 chordOmega13 chordOmega23
    rw [permMat_mul, permMat_mul]
    congr 1
  have hp13_23 : chordOmega13 R * chordOmega23 R = chordOmega12 R * chordOmega13 R := by
    unfold chordOmega12 chordOmega13 chordOmega23
    rw [permMat_mul, permMat_mul]
    congr 1
  have hc1 : matComm (chordOmega12 R) (chordOmega13 R + chordOmega23 R) = 0 := by
    unfold matComm
    rw [mul_add, add_mul, hp12_13, hp12_23, add_comm (chordOmega23 R * chordOmega12 R), sub_self]
  have hc2 : matComm (chordOmega23 R) (chordOmega12 R + chordOmega13 R) = 0 := by
    unfold matComm
    rw [mul_add, add_mul, hp23_12, hp23_13, add_comm (chordOmega13 R * chordOmega23 R), sub_self]
  have hc3 : matComm (chordOmega13 R) (chordOmega12 R + chordOmega23 R) = 0 := by
    unfold matComm
    rw [mul_add, add_mul, hp13_12, hp13_23, add_comm (chordOmega23 R * chordOmega13 R), sub_self]
  refine ⟨hc1, hc2, hc3, ?_, ?_⟩
  · unfold sl2Chord12 sl2Chord13 sl2Chord23
    rw [(matComm_two_smul_sub_one (chordOmega12 R) (chordOmega13 R) (chordOmega23 R)).1,
      hc1, smul_zero]
  · unfold sl2Chord23 sl2Chord12 sl2Chord13
    rw [(matComm_two_smul_sub_one (chordOmega23 R) (chordOmega12 R) (chordOmega13 R)).1,
      hc2, smul_zero]

/-- Non-abelian colour/isospin non-commutativity witness: individual chord operators
$\tilde{\Omega}_{12}$ and $\tilde{\Omega}_{23}$ do **not** commute over $\mathbb{Z}$
($[\tilde{\Omega}_{12}, \tilde{\Omega}_{23}] \neq 0$), confirming that 4T cancellation is a
non-trivial cancellation between $(1,3)$ and $(2,3)$ channels. -/
theorem sl2Chord12_sl2Chord23_noncomm :
    matComm (sl2Chord12 ℤ) (sl2Chord23 ℤ) ≠ 0 := by
  intro hzero
  have hentry := congr_fun (congr_fun hzero (0, 0, 1)) (0, 1, 0)
  have hexp : matComm (sl2Chord12 ℤ) (sl2Chord23 ℤ) =
      (4 : ℤ) • (permMat ℤ (perm12.trans perm23) - permMat ℤ (perm23.trans perm12)) := by
    unfold sl2Chord12 sl2Chord23
    rw [(matComm_two_smul_sub_one (chordOmega12 ℤ) (chordOmega23 ℤ) 0).2]
    unfold matComm chordOmega12 chordOmega23
    rw [permMat_mul, permMat_mul]
  rw [hexp] at hentry
  simp only [Matrix.zero_apply, Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul,
    permMat, Matrix.of_apply, Equiv.trans_apply, perm12, perm23] at hentry
  exact absurd hentry (by decide)

end BraidToChordJet

-- ============================================================================
-- § 2. One-Loop Gauge Beta Multiplicities & Gross–Politzer–Wilczek Evolution
-- ============================================================================

section GaugeBetaMultiplicities

/-- Representation quantum numbers of a left-handed Weyl fermion multiplet under
$\mathrm{SU}(3)_c \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ (pure data record). -/
structure ChiralWeylMultiplet where
  /-- Dimension under $\mathrm{SU}(3)_c$. -/
  su3Dim : ℕ
  /-- Dynkin index $T(R_3)$ under $\mathrm{SU}(3)_c$. -/
  su3Dynkin : ℚ
  /-- Dimension under $\mathrm{SU}(2)_L$. -/
  su2Dim : ℕ
  /-- Dynkin index $T(R_2)$ under $\mathrm{SU}(2)_L$. -/
  su2Dynkin : ℚ
  /-- Weak hypercharge $Y$ ($Q = T_3 + Y$). -/
  hypercharge : ℚ

/-- Left-handed quark doublet $Q_L = (3, 2, 1/6)$. -/
def quarkDoubletL : ChiralWeylMultiplet := ⟨3, 1 / 2, 2, 1 / 2, 1 / 6⟩

/-- Left-handed up-type antiquark $u_R^c = (\bar{3}, 1, -2/3)$. -/
def upAntitripletL : ChiralWeylMultiplet := ⟨3, 1 / 2, 1, 0, -2 / 3⟩

/-- Left-handed down-type antiquark $d_R^c = (\bar{3}, 1, 1/3)$. -/
def downAntitripletL : ChiralWeylMultiplet := ⟨3, 1 / 2, 1, 0, 1 / 3⟩

/-- Left-handed lepton doublet $L_L = (1, 2, -1/2)$. -/
def leptonDoubletL : ChiralWeylMultiplet := ⟨1, 0, 2, 1 / 2, -1 / 2⟩

/-- Left-handed positron singlet $e_R^c = (1, 1, 1)$. -/
def electronSingletL : ChiralWeylMultiplet := ⟨1, 0, 1, 0, 1⟩

/-- Complete one-generation chiral Weyl spectrum $\mathcal{S}_{\mathrm{chiral}}$. -/
def chiralGeneration : List ChiralWeylMultiplet :=
  [quarkDoubletL, upAntitripletL, downAntitripletL, leptonDoubletL, electronSingletL]

/-- Total $\mathrm{SU}(3)_c$ Dynkin index weighted by $\mathrm{SU}(2)_L$ multiplicity across one
generation $\mathcal{S}_{\mathrm{chiral}}$. -/
def genSU3DynkinSum : ℚ :=
  (chiralGeneration.map fun m => (m.su2Dim : ℚ) * m.su3Dynkin).sum

/-- Total $\mathrm{SU}(2)_L$ Dynkin index weighted by $\mathrm{SU}(3)_c$ multiplicity across one
generation $\mathcal{S}_{\mathrm{chiral}}$. -/
def genSU2DynkinSum : ℚ :=
  (chiralGeneration.map fun m => (m.su3Dim : ℚ) * m.su2Dynkin).sum

/-- Total squared hypercharge trace $\mathrm{Tr}_{\mathcal{S}_{\mathrm{chiral}}}(Y^2)$ across one
generation. -/
def genHyperchargeSqTrace : ℚ :=
  (chiralGeneration.map fun m => (m.su3Dim : ℚ) * (m.su2Dim : ℚ) * m.hypercharge ^ 2).sum

/-- One-loop $\mathrm{SU}(3)_c$ beta coefficient $b_3(N_{\mathrm{gen}})$ over $\mathbb{Q}$. -/
def beta3Q (N_gen : ℕ) : ℚ :=
  (11 / 3 : ℚ) * 3 - (2 / 3 : ℚ) * genSU3DynkinSum * (N_gen : ℚ)

/-- One-loop $\mathrm{SU}(2)_L$ beta coefficient $b_2(N_{\mathrm{gen}}, N_H)$ over $\mathbb{Q}$. -/
def beta2Q (N_gen N_H : ℕ) : ℚ :=
  (11 / 3 : ℚ) * 2 - (2 / 3 : ℚ) * genSU2DynkinSum * (N_gen : ℚ) -
    (1 / 3 : ℚ) * (1 / 2 : ℚ) * (N_H : ℚ)

/-- One-loop GUT-normalized $\mathrm{U}(1)_Y$ beta coefficient $b_1(N_{\mathrm{gen}}, N_H)$ over $\mathbb{Q}$
($g_1^2 = \frac{5}{3} g_Y^2$, complex Higgs doublet $(1, 2, 1/2)$). -/
def beta1Q (N_gen N_H : ℕ) : ℚ :=
  -(2 / 3 : ℚ) * (3 / 5 : ℚ) * genHyperchargeSqTrace * (N_gen : ℚ) -
    (1 / 3 : ℚ) * (3 / 5 : ℚ) * (2 * (1 / 2 : ℚ) ^ 2) * (N_H : ℚ)

/-- Exact Dynkin trace sums ($2$, $2$, $\frac{10}{3}$), Weyl state count ($15$), and cancellation
of gravitational, $\mathrm{SU}(3)^2\mathrm{U}(1)_Y$, $\mathrm{SU}(2)^2\mathrm{U}(1)_Y$, and
$\mathrm{U}(1)_Y^3$ gauge anomalies on $\mathcal{S}_{\mathrm{chiral}}$. -/
theorem chiralGeneration_dynkin_sums_and_anomalies :
    (chiralGeneration.map fun m => m.su3Dim * m.su2Dim).sum = 15 ∧
      genSU3DynkinSum = 2 ∧
      genSU2DynkinSum = 2 ∧
      genHyperchargeSqTrace = 10 / 3 ∧
      (chiralGeneration.map fun m => (m.su3Dim : ℚ) * (m.su2Dim : ℚ) * m.hypercharge).sum = 0 ∧
      (chiralGeneration.map fun m => (m.su2Dim : ℚ) * m.su3Dynkin * m.hypercharge).sum = 0 ∧
      (chiralGeneration.map fun m => (m.su3Dim : ℚ) * m.su2Dynkin * m.hypercharge).sum = 0 ∧
      (chiralGeneration.map fun m => (m.su3Dim : ℚ) * (m.su2Dim : ℚ) * m.hypercharge ^ 3).sum = 0 := by
  simp only [chiralGeneration, genSU3DynkinSum, genSU2DynkinSum, genHyperchargeSqTrace,
    quarkDoubletL, upAntitripletL, downAntitripletL, leptonDoubletL, electronSingletL,
    List.map, List.sum_cons, List.sum_nil]
  norm_num

/-- Closed-form polynomial expressions for $(b_3, b_2, b_1)$ in $(N_{\mathrm{gen}}, N_H)$. -/
theorem beta_coefficients_closed_form (N_gen N_H : ℕ) :
    beta3Q N_gen = 11 - (4 / 3 : ℚ) * (N_gen : ℚ) ∧
      beta2Q N_gen N_H = 22 / 3 - (4 / 3 : ℚ) * (N_gen : ℚ) - (1 / 6 : ℚ) * (N_H : ℚ) ∧
      beta1Q N_gen N_H = -(4 / 3 : ℚ) * (N_gen : ℚ) - (1 / 10 : ℚ) * (N_H : ℚ) := by
  have h := chiralGeneration_dynkin_sums_and_anomalies
  unfold beta3Q beta2Q beta1Q
  rw [h.2.1, h.2.2.1, h.2.2.2.1]
  refine ⟨by ring, by ring, by ring⟩

/-- Three-generation QCD beta coefficient $b_3(3) = 7 > 0$. -/
theorem b3_three_gen_eq_seven : beta3Q 3 = 7 ∧ 0 < beta3Q 3 := by
  rw [(beta_coefficients_closed_form 3 0).1]
  norm_num

/-- **Gross–Politzer–Wilczek Asymptotic Freedom Threshold:**
$b_3(N_{\mathrm{gen}}) > 0$ holds if and only if $N_{\mathrm{gen}} \le 8$ (equivalently $n_f = 2 N_{\mathrm{gen}} \le 16$). -/
theorem b3_asymptotic_freedom_iff (N_gen : ℕ) :
    0 < beta3Q N_gen ↔ N_gen ≤ 8 := by
  rw [(beta_coefficients_closed_form N_gen 0).1]
  constructor
  · intro hpos
    by_contra hgt
    push_neg at hgt
    have hge9 : (9 : ℚ) ≤ (N_gen : ℚ) := by exact_mod_cast hgt
    linarith
  · intro hle
    have hle8 : (N_gen : ℚ) ≤ 8 := by exact_mod_cast hle
    linarith

/-- Standard Model ($N_{\mathrm{gen}} = 3, N_H = 1$) electroweak 1-loop beta coefficients
$b_2(3, 1) = \frac{19}{6} > 0$ and $b_1(3, 1) = -\frac{41}{10} < 0$. -/
theorem b2_sm_eq : beta2Q 3 1 = 19 / 6 ∧ 0 < beta2Q 3 1 := by
  rw [(beta_coefficients_closed_form 3 1).2.1]
  norm_num

theorem b1_sm_eq : beta1Q 3 1 = -41 / 10 ∧ beta1Q 3 1 < 0 := by
  rw [(beta_coefficients_closed_form 3 1).2.2]
  norm_num

/-- One-loop renormalization-group evolved inverse gauge coupling
$\alpha_i^{-1}(\mu_2) = \alpha_i^{-1}(\mu_1) + \frac{b_i}{2\pi}\ln(\mu_2 / \mu_1)$. -/
noncomputable def invAlphaRG (invAlpha1 b μ1 μ2 : ℝ) : ℝ :=
  invAlpha1 + (b / (2 * Real.pi)) * Real.log (μ2 / μ1)

/-- One-loop running gauge coupling $\alpha_i(\mu_2) = (\mathrm{invAlphaRG}(\alpha_1^{-1}, b_i, \mu_1, \mu_2))^{-1}$. -/
noncomputable def alphaRG (α1 b μ1 μ2 : ℝ) : ℝ :=
  (invAlphaRG α1⁻¹ b μ1 μ2)⁻¹

/-- Exact 1-loop inverse-coupling shift law, RG semigroup transitivity, and **strict ultraviolet
decrease** $0 < \alpha_3(\mu_2) < \alpha_3(\mu_1)$ for $0 < \mu_1 < \mu_2$ whenever $b > 0$. -/
theorem one_loop_rg_evolution_and_uv_asymptotic_freedom
    {α1 b μ1 μ2 μ3 : ℝ} (hα1 : 0 < α1) (hb : 0 < b)
    (hμ1 : 0 < μ1) (hμ12 : μ1 < μ2) (hμ3 : 0 < μ3) :
    invAlphaRG α1⁻¹ b μ1 μ2 - α1⁻¹ = (b / (2 * Real.pi)) * Real.log (μ2 / μ1) ∧
      invAlphaRG (invAlphaRG α1⁻¹ b μ1 μ2) b μ2 μ3 = invAlphaRG α1⁻¹ b μ1 μ3 ∧
      0 < alphaRG α1 b μ1 μ2 ∧
      alphaRG α1 b μ1 μ2 < α1 := by
  have hμ2 : 0 < μ2 := lt_trans hμ1 hμ12
  have hpi2 : 0 < 2 * Real.pi := mul_pos two_pos Real.pi_pos
  have hrat_gt_one : 1 < μ2 / μ1 := (one_lt_div hμ1).mpr hμ12
  have hlog_pos : 0 < Real.log (μ2 / μ1) := Real.log_pos hrat_gt_one
  have hshift_pos : 0 < (b / (2 * Real.pi)) * Real.log (μ2 / μ1) :=
    mul_pos (div_pos hb hpi2) hlog_pos
  have hinv1_pos : 0 < α1⁻¹ := inv_pos.mpr hα1
  have hinv2_gt : α1⁻¹ < invAlphaRG α1⁻¹ b μ1 μ2 := by
    unfold invAlphaRG
    linarith
  have hinv2_pos : 0 < invAlphaRG α1⁻¹ b μ1 μ2 := lt_trans hinv1_pos hinv2_gt
  refine ⟨by unfold invAlphaRG; ring, ?_, inv_pos.mpr hinv2_pos, ?_⟩
  · unfold invAlphaRG
    have hlog_mul : Real.log ((μ2 / μ1) * (μ3 / μ2)) =
        Real.log (μ2 / μ1) + Real.log (μ3 / μ2) :=
      Real.log_mul (ne_of_gt (div_pos hμ2 hμ1)) (ne_of_gt (div_pos hμ3 hμ2))
    have hcancel : (μ2 / μ1) * (μ3 / μ2) = μ3 / μ1 := by
      field_simp [ne_of_gt hμ1, ne_of_gt hμ2]
    rw [hcancel] at hlog_mul
    rw [hlog_mul]
    ring
  · unfold alphaRG
    have hlt := inv_strictAnti₀ hinv1_pos hinv2_gt
    simpa using hlt

end GaugeBetaMultiplicities

-- ============================================================================
-- § 3. Schwinger–Kinoshita (g - 2)_ℓ Polynomial & Weinberg Planck Decoupling
-- ============================================================================

section SchwingerAnomalousMomentAndPlanckDecoupling

/-- Universal 5-loop QED anomalous magnetic moment polynomial
$a_\ell^{(5)}(\alpha; C_1, \dots, C_5) = \sum_{k=1}^5 C_k (\alpha / \pi)^k$. -/
noncomputable def qedAnomMagMoment5 (α C1 C2 C3 C4 C5 : ℝ) : ℝ :=
  C1 * (α / Real.pi) +
    C2 * (α / Real.pi) ^ 2 +
    C3 * (α / Real.pi) ^ 3 +
    C4 * (α / Real.pi) ^ 4 +
    C5 * (α / Real.pi) ^ 5

/-- Leading 1-loop Schwinger (1948) anomalous magnetic moment $a_\ell^{(1)}(\alpha) = \frac{\alpha}{2\pi}$. -/
noncomputable def schwingerOneLoop (α : ℝ) : ℝ :=
  α / (2 * Real.pi)

/-- Specialization of `qedAnomMagMoment5` at $(C_1, C_2, C_3, C_4, C_5) = (1/2, 0, 0, 0, 0)$
recovers Schwinger's $\frac{\alpha}{2\pi}$, and its 1-loop Lipschitz sensitivity equals
$\frac{|\alpha_1 - \alpha_2|}{2\pi}$. -/
theorem schwingerOneLoop_specialization_and_lipschitz (α₁ α₂ : ℝ) :
    qedAnomMagMoment5 α₁ (1 / 2) 0 0 0 0 = schwingerOneLoop α₁ ∧
      |schwingerOneLoop α₁ - schwingerOneLoop α₂| = |α₁ - α₂| / (2 * Real.pi) := by
  have hpi2 : 0 < 2 * Real.pi := mul_pos two_pos Real.pi_pos
  refine ⟨?_, ?_⟩
  · unfold qedAnomMagMoment5 schwingerOneLoop
    ring
  · unfold schwingerOneLoop
    rw [← sub_div, abs_div, abs_of_pos hpi2]

/-- **Weinberg EFT Dimension-6 Dipole Planck-Decoupling Bound:**
For any lepton mass $0 < m_e \le 10^{-3}\;\mathrm{GeV}$, ultraviolet cutoff scale
$E_* \ge 10^{19}\;\mathrm{GeV}$, and dimension-6 Wilson coefficient magnitude
$\kappa_{\mathrm{UV}} \le 1$ with $|\delta a_e^{\mathrm{UV}}| \le \kappa_{\mathrm{UV}} (m_e / E_*)^2$:
1. $(m_e / E_*)^2 \le 10^{-44}$,
2. $10^{-44} < 10^{-13}$, and
3. $|\delta a_e^{\mathrm{UV}}| \le 10^{-44} < 10^{-13}$ (leaving the $10^{-13}$ experimental
   $(g - 2)_e$ precision window unperturbed by 31 orders of magnitude). -/
theorem planck_dipole_decoupling_bound
    {m_e E_star δa_uv κ_uv : ℝ}
    (hme_pos : 0 < m_e) (hme_le : m_e ≤ (10 : ℝ) ^ (-3 : ℤ))
    (hE_ge : (10 : ℝ) ^ (19 : ℤ) ≤ E_star)
    (hκ_le : κ_uv ≤ 1)
    (huv_bound : |δa_uv| ≤ κ_uv * (m_e / E_star) ^ 2) :
    (m_e / E_star) ^ 2 ≤ (10 : ℝ) ^ (-44 : ℤ) ∧
      (10 : ℝ) ^ (-44 : ℤ) < (10 : ℝ) ^ (-13 : ℤ) ∧
      |δa_uv| < (10 : ℝ) ^ (-13 : ℤ) := by
  have h19_pos : (0 : ℝ) < (10 : ℝ) ^ (19 : ℤ) := by norm_num
  have hE_pos : 0 < E_star := lt_of_lt_of_le h19_pos hE_ge
  have hrat_pos : 0 ≤ m_e / E_star := div_nonneg (le_of_lt hme_pos) (le_of_lt hE_pos)
  have hrat_le : m_e / E_star ≤ (10 : ℝ) ^ (-22 : ℤ) := by
    calc
      m_e / E_star ≤ (10 : ℝ) ^ (-3 : ℤ) / E_star :=
        div_le_div_of_nonneg_right hme_le (le_of_lt hE_pos)
      _ ≤ (10 : ℝ) ^ (-3 : ℤ) / (10 : ℝ) ^ (19 : ℤ) :=
        div_le_div_of_nonneg_left (by norm_num) h19_pos hE_ge
      _ = (10 : ℝ) ^ (-22 : ℤ) := by norm_num
  have hsq_le : (m_e / E_star) ^ 2 ≤ (10 : ℝ) ^ (-44 : ℤ) := by
    have hmul : (m_e / E_star) * (m_e / E_star) ≤
        (10 : ℝ) ^ (-22 : ℤ) * (10 : ℝ) ^ (-22 : ℤ) :=
      mul_le_mul hrat_le hrat_le hrat_pos (by norm_num)
    calc
      (m_e / E_star) ^ 2 = (m_e / E_star) * (m_e / E_star) := sq _
      _ ≤ (10 : ℝ) ^ (-22 : ℤ) * (10 : ℝ) ^ (-22 : ℤ) := hmul
      _ = (10 : ℝ) ^ (-44 : ℤ) := by norm_num
  have h44_lt_13 : (10 : ℝ) ^ (-44 : ℤ) < (10 : ℝ) ^ (-13 : ℤ) := by norm_num
  have hδ_le_44 : |δa_uv| ≤ (10 : ℝ) ^ (-44 : ℤ) := by
    calc
      |δa_uv| ≤ κ_uv * (m_e / E_star) ^ 2 := huv_bound
      _ ≤ 1 * (m_e / E_star) ^ 2 := mul_le_mul_of_nonneg_right hκ_le (sq_nonneg _)
      _ = (m_e / E_star) ^ 2 := one_mul _
      _ ≤ (10 : ℝ) ^ (-44 : ℤ) := hsq_le
  exact ⟨hsq_le, h44_lt_13, lt_of_le_of_lt hδ_le_44 h44_lt_13⟩

end SchwingerAnomalousMomentAndPlanckDecoupling

-- ============================================================================
-- § 4. Non-Perturbative Borromean Parton Asymmetry & 1-Loop DGLAP Moments
-- ============================================================================

section BorromeanPartonMomentsAndDGLAP

/-- Exact rational $n$-th harmonic number $H_n = \sum_{k=1}^n \frac{1}{k}$. -/
def harmonicQ : ℕ → ℚ
  | 0 => 0
  | n + 1 => harmonicQ n + 1 / ((n : ℚ) + 1)

/-- Exact rational 1-loop non-singlet QCD Mellin anomalous dimension ($C_F = \frac{4}{3}$):
$\gamma_n^{\mathrm{NS}} = \frac{4}{3}\bigl(4 H_n - 3 - \frac{2}{n(n + 1)}\bigr)$ for $n \ge 1$. -/
def gammaNonSingletQ (n : ℕ) : ℚ :=
  (4 / 3 : ℚ) * (4 * harmonicQ n - 3 - 2 / ((n : ℚ) * ((n : ℚ) + 1)))

/-- **Valence Quark-Number Conservation (`n = 1`) and Low-Moment Benchmarks (`n = 2, 3, 4`):**
$\gamma_1^{\mathrm{NS}} = 0$ (Gross–Llewellyn Smith / Adler baryon-number conservation), while
$\gamma_2^{\mathrm{NS}} = \frac{32}{9}$, $\gamma_3^{\mathrm{NS}} = \frac{50}{9}$, and
$\gamma_4^{\mathrm{NS}} = \frac{314}{45}$. -/
theorem gammaNonSingletQ_values_one_to_four :
    gammaNonSingletQ 1 = 0 ∧
      gammaNonSingletQ 2 = 32 / 9 ∧
      gammaNonSingletQ 3 = 50 / 9 ∧
      gammaNonSingletQ 4 = 314 / 45 := by
  simp only [gammaNonSingletQ, harmonicQ]
  norm_num

/-- **Strict Forward Increment of $\gamma_n^{\mathrm{NS}}$ for Every $n \ge 1$:**
$\gamma_{n+1}^{\mathrm{NS}} - \gamma_n^{\mathrm{NS}} =
  \frac{16}{3(n+1)} + \frac{16}{3 n (n+1) (n+2)} > 0$. -/
theorem gammaNonSingletQ_strict_step {n : ℕ} (hn : 1 ≤ n) :
    gammaNonSingletQ n < gammaNonSingletQ (n + 1) := by
  have hn_pos : (0 : ℚ) < (n : ℚ) := by exact_mod_cast (Nat.succ_le_iff.mp hn)
  have hn1_pos : (0 : ℚ) < (n : ℚ) + 1 := by linarith
  have hn2_pos : (0 : ℚ) < (n : ℚ) + 2 := by linarith
  have hdiff :
      gammaNonSingletQ (n + 1) - gammaNonSingletQ n =
        16 / (3 * ((n : ℚ) + 1)) +
          16 / (3 * (n : ℚ) * ((n : ℚ) + 1) * ((n : ℚ) + 2)) := by
    simp only [gammaNonSingletQ, harmonicQ, Nat.cast_add, Nat.cast_one]
    have hn_ne : (n : ℚ) ≠ 0 := ne_of_gt hn_pos
    have hn1_ne : (n : ℚ) + 1 ≠ 0 := ne_of_gt hn1_pos
    have hn2_ne : (n : ℚ) + 2 ≠ 0 := ne_of_gt hn2_pos
    have hn1_alt : (n : ℚ) + 1 + 1 = (n : ℚ) + 2 := by ring
    rw [hn1_alt]
    field_simp [hn_ne, hn1_ne, hn2_ne]
    ring
  have hpos : 0 < gammaNonSingletQ (n + 1) - gammaNonSingletQ n := by
    rw [hdiff]
    positivity
  linarith

/-- **Strict Positivity of All Higher Non-Singlet Mellin Anomalous Dimensions (`n ≥ 2`):**
For every integer $n \ge 2$, $0 < \gamma_n^{\mathrm{NS}}$. -/
theorem gammaNonSingletQ_pos_of_two_le {n : ℕ} (hn : 2 ≤ n) :
    0 < gammaNonSingletQ n := by
  induction n, hn using Nat.le_induction with
  | base =>
    rw [gammaNonSingletQ_values_one_to_four.2.1]
    norm_num
  | succ k hk ih =>
    exact lt_trans ih (gammaNonSingletQ_strict_step (by omega))

/-- One-loop non-singlet DGLAP Mellin moment evolution:
$M_n(Q^2) = M_n(\mu_0^2) \cdot (\alpha_s(Q^2) / \alpha_s(\mu_0^2))^{\gamma_n^{\mathrm{NS}} / (2 b_3)}$. -/
noncomputable def mellinMomentRG (M0 α_Q α_0 γ b3 : ℝ) : ℝ :=
  M0 * (α_Q / α_0) ^ (γ / (2 * b3))

/-- **Valence Number Conservation (`n = 1`) and Ultraviolet DGLAP Moment Softening (`n ≥ 2`):**
Whenever $M_0 > 0$, $b_3 > 0$, and $0 < \alpha_s(Q^2) < \alpha_s(\mu_0^2)$:
1. At $n = 1$, $M_1(Q^2) = M_0$ identically (scale-independent valence baryon number);
2. For every $n \ge 2$, $0 < M_n(Q^2) < M_0$ (strict ultraviolet softening of higher valence moments). -/
theorem dglap_valence_conservation_and_uv_softening
    {M0 α_Q α_0 b3 : ℝ} {n : ℕ}
    (hM0 : 0 < M0) (hb3 : 0 < b3)
    (hαQ : 0 < α_Q) (hαlt : α_Q < α_0) (hn : 2 ≤ n) :
    mellinMomentRG M0 α_Q α_0 (gammaNonSingletQ 1 : ℝ) b3 = M0 ∧
      0 < mellinMomentRG M0 α_Q α_0 (gammaNonSingletQ n : ℝ) b3 ∧
      mellinMomentRG M0 α_Q α_0 (gammaNonSingletQ n : ℝ) b3 < M0 := by
  have hα0 : 0 < α_0 := lt_trans hαQ hαlt
  have hrat_pos : 0 < α_Q / α_0 := div_pos hαQ hα0
  have hrat_lt_one : α_Q / α_0 < 1 := (div_lt_one hα0).mpr hαlt
  have hγ1 : (gammaNonSingletQ 1 : ℝ) = 0 := by
    exact_mod_cast gammaNonSingletQ_values_one_to_four.1
  have hγn_pos : (0 : ℝ) < (gammaNonSingletQ n : ℝ) := by
    exact_mod_cast gammaNonSingletQ_pos_of_two_le hn
  have hexp_pos : 0 < (gammaNonSingletQ n : ℝ) / (2 * b3) :=
    div_pos hγn_pos (mul_pos two_pos hb3)
  have hrpow_pos : 0 < (α_Q / α_0) ^ ((gammaNonSingletQ n : ℝ) / (2 * b3)) :=
    Real.rpow_pos_of_pos hrat_pos _
  have hrpow_lt_one : (α_Q / α_0) ^ ((gammaNonSingletQ n : ℝ) / (2 * b3)) < 1 :=
    Real.rpow_lt_one (le_of_lt hrat_pos) hrat_lt_one hexp_pos
  refine ⟨?_, mul_pos hM0 hrpow_pos, ?_⟩
  · unfold mellinMomentRG
    rw [hγ1, zero_div, Real.rpow_zero, mul_one]
  · unfold mellinMomentRG
    calc
      M0 * (α_Q / α_0) ^ ((gammaNonSingletQ n : ℝ) / (2 * b3)) < M0 * 1 :=
        mul_lt_mul_of_pos_left hrpow_lt_one hM0
      _ = M0 := mul_one M0

/-- Palindromic Jucys–Murphy $[u, u, d]$ valence weight ratio
$R_{ud}^{\mathrm{sym}}(q) = \frac{1 + q^4}{q^2}$ on the $H_3(q)$ spectrum $(1, q^2, q^4)$. -/
noncomputable def valenceRatioPalindromic (q : ℝ) : ℝ :=
  (1 + q ^ 4) / q ^ 2

/-- Top-two Jucys–Murphy $[u, u, d]$ valence weight ratio
$R_{ud}^{\mathrm{top}}(q) = q^2(1 + q^2)$ on the $H_3(q)$ spectrum $(1, q^2, q^4)$. -/
def valenceRatioTopTwo (q : ℝ) : ℝ :=
  q ^ 2 * (1 + q ^ 2)

/-- Palindromic $u$-quark and $d$-quark normalized momentum fractions on $(1, q^2, q^4)$. -/
noncomputable def valenceFracUpPalindromic (q : ℝ) : ℝ :=
  (1 + q ^ 4) / (1 + q ^ 2 + q ^ 4)

noncomputable def valenceFracDownPalindromic (q : ℝ) : ℝ :=
  q ^ 2 / (1 + q ^ 2 + q ^ 4)

/-- **3-Strand Jucys–Murphy Valence Momentum Asymmetry Theorem on $[u, u, d] \in H_3(q)$:**
1. At the classical symmetric boundary $q = 1$, both Jucys–Murphy assignments recover the
   exact $\mathrm{SU}(6)$ quark-counting ratio $w_u(1) / w_d(1) = 2$ (with momentum fractions
   $f_u(1) = 2/3$, $f_d(1) = 1/3$);
2. Momentum sum rule $f_u^{\mathrm{sym}}(q) + f_d^{\mathrm{sym}}(q) = 1$ holds for every $q \in \mathbb{R}$;
3. For **every** real $q > 1$, both the palindromic ratio
   $R_{ud}^{\mathrm{sym}}(q) = q^2 + q^{-2} = 2 + (q - q^{-1})^2$ and the top-two ratio
   $R_{ud}^{\mathrm{top}}(q) = q^2(1 + q^2) = 2 + (q^2 - 1)(q^2 + 2)$ strictly exceed $2$
   ($u / d > 2$ valence momentum enhancement, equivalently $f_u^{\mathrm{sym}}(q) > 2/3$ and
   $f_d^{\mathrm{sym}}(q) < 1/3$). -/
theorem jucys_murphy_valence_asymmetry_gt_two {q : ℝ} (hq : 1 < q) :
    valenceRatioPalindromic 1 = 2 ∧
      valenceRatioTopTwo 1 = 2 ∧
      valenceFracUpPalindromic 1 = 2 / 3 ∧
      valenceFracDownPalindromic 1 = 1 / 3 ∧
      valenceFracUpPalindromic q + valenceFracDownPalindromic q = 1 ∧
      valenceRatioPalindromic q - 2 = (q - q⁻¹) ^ 2 ∧
      2 < valenceRatioPalindromic q ∧
      2 < valenceRatioTopTwo q ∧
      2 / 3 < valenceFracUpPalindromic q ∧
      valenceFracDownPalindromic q < 1 / 3 := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq_ne : q ≠ 0 := ne_of_gt hq0
  have hden_pos : 0 < 1 + q ^ 2 + q ^ 4 := by positivity
  have hden_ne : 1 + q ^ 2 + q ^ 4 ≠ 0 := ne_of_gt hden_pos
  have hpal_diff : valenceRatioPalindromic q - 2 = (q - q⁻¹) ^ 2 := by
    unfold valenceRatioPalindromic
    field_simp [hq_ne]
    ring
  have hh_pos : 0 < q - q⁻¹ := by
    have heq : q - q⁻¹ = (q ^ 2 - 1) / q := by field_simp [hq_ne]
    rw [heq]
    exact div_pos (by nlinarith) hq0
  have hpal_gt2 : 2 < valenceRatioPalindromic q := by
    have hsq_pos : 0 < (q - q⁻¹) ^ 2 := sq_pos_of_pos hh_pos
    linarith [hpal_diff]
  have htop_gt2 : 2 < valenceRatioTopTwo q := by
    have htop_diff : valenceRatioTopTwo q - 2 = (q ^ 2 - 1) * (q ^ 2 + 2) := by
      unfold valenceRatioTopTwo
      ring
    have hp : 0 < (q ^ 2 - 1) * (q ^ 2 + 2) := mul_pos (by nlinarith) (by positivity)
    linarith [htop_diff]
  have hfu_diff : valenceFracUpPalindromic q - 2 / 3 =
      (q ^ 2 - 1) ^ 2 / (3 * (1 + q ^ 2 + q ^ 4)) := by
    unfold valenceFracUpPalindromic
    field_simp [hden_ne]
    ring
  have hfu_gt : 2 / 3 < valenceFracUpPalindromic q := by
    have hp : 0 < (q ^ 2 - 1) ^ 2 / (3 * (1 + q ^ 2 + q ^ 4)) :=
      div_pos (sq_pos_of_pos (by nlinarith)) (by positivity)
    linarith [hfu_diff]
  have hsum : valenceFracUpPalindromic q + valenceFracDownPalindromic q = 1 := by
    unfold valenceFracUpPalindromic valenceFracDownPalindromic
    field_simp [hden_ne]
    ring
  refine ⟨?_, ?_, ?_, ?_, hsum, hpal_diff, hpal_gt2, htop_gt2, hfu_gt, ?_⟩
  · unfold valenceRatioPalindromic; norm_num
  · unfold valenceRatioTopTwo; norm_num
  · unfold valenceFracUpPalindromic; norm_num
  · unfold valenceFracDownPalindromic; norm_num
  · linarith [hsum, hfu_gt]

end BorromeanPartonMomentsAndDGLAP

end QOU.StandardModel.InfraredQFTSubsumptionAndPartonMoments
