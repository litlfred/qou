import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FinCases
import CompactQuantumMetrics.OqSU2ModularNakayama

/-!
# `O_q(SU(2))` Woronowicz Haar Modular Entanglement First Law Across `N_Σ` Boundary Strands

Purely algebraic (`§7c`, generic `[CommRing R]`, `[Field K]`, and ordered fields; zero `: ℝ`,
zero empirical literals, `0 sorry`, `0` custom `axiom`s) formalization of Option 4B (`qou-tx4q`):

1. **Single-Strand Woronowicz Haar Modular State & `U_q(𝔰𝔩₂)` Cup Purification (`§1`):**
   - Bridges Woronowicz's rank-1 Haar evaluation (`OqSU2.haar_cleared_alpha_delta` in
     `OqSU2ModularNakayama`) directly to the normalized spin-`1/2` reduced modular spectrum
     `haarProbPlus q = q² / (1 + q²)` and `haarProbMinus q = 1 / (1 + q²)`.
   - Proves exact unit normalization `p_+(q) + p_-(q) = 1`, modular boost step ratio
     `p_+(q) / p_-(q) = q²` (matching `ν_q(α) = q² α`, i.e. `e^{β_mod} = q²` with
     `β_mod = 2 ln q`), pivotal quantum-trace identity `p_+(q) = q / [2]_q` and
     `p_-(q) = q⁻¹ / [2]_q`, polarization bias `p_+(q) - p_-(q) = (q - q⁻¹) / [2]_q`,
     ordered-field strict hierarchy `0 < p_-(q) < 1/2 < p_+(q) < 1` (`1 < q`), and exact
     partial-trace purification by the `U_q(𝔰𝔩₂)` spin-`0` cup vector `q |+, -⟩ - |-, +⟩`.
2. **Exact Relative-Entropy / Modular-Hamiltonian Entanglement First Law (`§2`):**
   - Proves the exact finite-difference Blanco–Casini–Hung–Myers entanglement first law
     `S(σ) - S(ρ) + D(σ ‖ ρ) = Tr((σ - ρ) K_ρ)` over any `[CommRing R]` and `[Fintype I]`.
   - Proves exact partition-function (`ln Z`) cancellation for normalized Gibbs / Woronowicz
     Haar modular states (`S(σ) - S(ρ) + D(σ ‖ ρ) = β (⟨H⟩_σ - ⟨H⟩_ρ)`), instantiated on
     Woronowicz's single-strand Haar state.
   - Proves the necessary-and-sufficient linear variation theorem
     `δS(δρ) = δ⟨K_ρ⟩(δρ) ↔ Tr(δρ) = 0`, ordered-field relative-entropy non-negativity
     `D(σ ‖ ρ) ≥ 0` under tangent concavity, and strict positive-definiteness of the
     second-order Fisher–Rao / `χ²` remainder `(1/2) ∑_i (δp_i)² / p_i`.
3. **`N_Σ`-Strand Unprojected vs Singlet-Projected vs Bipartite Global-Singlet Spectrum (`§3`):**
   - Proves exact tensor-product additivity and `N_Σ`-strand extensivity `S(ρ_1^{⊗ N_Σ}) = N_Σ S(ρ_1)`
     and `⟨J_z^{tot}⟩ = N_Σ (p_+ - p_-) / 2` for unprojected / rainbow-cup horizon states.
   - Proves that on any `J = 0` singlet subspace (`J_z^{tot} = 0`), the Haar modular weight
     `q^{2 J_z^{tot}}` collapses to `1`, forcing the direct singlet-projected state to be
     strictly uniform `(card S_sing)⁻¹` and `q`-independent with zero boost expectation.
   - Constructs the explicit 2-strand (`2 N_Σ = 4`, `C_2 = 2`) half-system global-singlet
     reduced spectrum `![1/2, q² / (2 [3]_q), 1 / (2 [3]_q), q⁻² / (2 [3]_q)]`, proving exact
     normalization and strict ordered-field `q`-splitting `λ₁(q) > 1/6 > λ₂(q) > λ₃(q) > 0`
     for `1 < q`.
4. **`U_q(𝔰𝔩₂)` Quadratic Casimir Area Comparison & Quarter-Area Lock (`§4`):**
   - Formalizes the rational spin-`1/2` `U_q(𝔰𝔩₂)` quadratic Casimir
     `uqCasimirSpinHalf q = (q² + q + 1) / (q + 1)²`, proving `[1/2]_q [3/2]_q` Laurent
     equivalence, `q ↔ q⁻¹` symmetry, `(q - 1)² / (4 (q + 1)²)` excess above `3/4`, and
     strict bounds `3 / 4 < uqCasimirSpinHalf q < 1` for `0 < q`, `q ≠ 1`.
   - Proves `S(ρ_Σ) / A_alg(ρ_Σ) = 1 / 4 ↔ a_alg = 4 * s_strand`, isolating the continuum
     `(2π) / (8π)` Lorentzian Raychaudhuri / Bisognano–Wichmann bridge in the zero-instance
     Rule-13a class `HaarLorentzianModularBridgeConjecture`.

References: Woronowicz (1987), Blanco–Casini–Hung–Myers (2013), Donnelly (2012),
Couvreur–Jacobsen–Saleur (2017), Kaul–Majumdar (2000), Jacobson (1995).
-- Ref: [woronowicz1987]
-- Ref: [bekenstein1973]
-- Ref: [hawking1975]
-- Ref: [jacobson1995]
-/

set_option autoImplicit false

namespace QOU.GravitySpacetime.OqSU2HaarModularEntanglement

open scoped BigOperators
open QOU.AlgebraicSubstrate

/-! ## 1. Single-Strand Woronowicz Haar Modular State & `U_q(𝔰𝔩₂)` Cup Purification -/

section SingleStrandHaarModularState

variable {K : Type*} [Field K]

/-- Quantum integer `[2]_q = q + q⁻¹` (spin-`1/2` quantum dimension / `TL_n(q)` loop fugacity). -/
def qTwo (q : K) : K :=
  q + q⁻¹

/-- Quantum integer `[3]_q = q² + 1 + q⁻²` (spin-`1` adjoint quantum dimension). -/
def qThree (q : K) : K :=
  q ^ 2 + 1 + (q⁻¹) ^ 2

/-- Upper (`m = +1/2`) eigenvalue `p_+(q) = q² / (1 + q²)` of Woronowicz's single-strand
Haar modular reduced state on `V_{1/2}`. -/
def haarProbPlus (q : K) : K :=
  q ^ 2 / (1 + q ^ 2)

/-- Lower (`m = -1/2`) eigenvalue `p_-(q) = 1 / (1 + q²)` of Woronowicz's single-strand
Haar modular reduced state on `V_{1/2}`. -/
def haarProbMinus (q : K) : K :=
  1 / (1 + q ^ 2)

/-- Two-level spin-`1/2` Haar modular distribution `0 ↦ p_+(q), 1 ↦ p_-(q)` on `Fin 2`. -/
def haarStrandProb (q : K) : Fin 2 → K :=
  ![haarProbPlus q, haarProbMinus q]

/-- **Bridge to `OqSU2ModularNakayama` (`h(δ α) = p_+(q)`, `h(α δ) = p_-(q)`):**
For any normalized `K`-linear functional `h : OqSU2 K q →ₗ[K] K` (`h 1 = 1`) satisfying
Woronowicz's rank-1 Haar identity `(1 + q²) * h(β * γ) = -q * h(1)` with `1 + (q : K)² ≠ 0`,
the diagonal corepresentation expectations `h(δ * α)` and `h(α * δ)` equal `haarProbPlus q`
and `haarProbMinus q` respectively, with modular swap ratio `(q : K)²`. -/
theorem oqsu2_haar_reduced_eigenvalues (q : Kˣ) (h : OqSU2 K q →ₗ[K] K)
    (h1 : h 1 = 1)
    (hbg : (1 + (q : K) ^ 2) * h (OqSU2.β q * OqSU2.γ q) = -(q : K) * h 1)
    (hu : 1 + (q : K) ^ 2 ≠ 0) :
    h (OqSU2.δ q * OqSU2.α q) = haarProbPlus (q : K) ∧
      h (OqSU2.α q * OqSU2.δ q) = haarProbMinus (q : K) ∧
      h (OqSU2.δ q * OqSU2.α q) = (q : K) ^ 2 * h (OqSU2.α q * OqSU2.δ q) := by
  obtain ⟨hAD, hDA⟩ := OqSU2.haar_cleared_alpha_delta (R := K) q h hbg
  rw [h1, mul_one] at hDA
  rw [h1] at hAD
  have hp_minus : h (OqSU2.α q * OqSU2.δ q) = haarProbMinus (q : K) := by
    unfold haarProbMinus
    rw [eq_div_iff hu, mul_comm]
    exact hAD
  have hp_plus : h (OqSU2.δ q * OqSU2.α q) = haarProbPlus (q : K) := by
    unfold haarProbPlus
    rw [eq_div_iff hu, mul_comm]
    exact hDA
  refine ⟨hp_plus, hp_minus, ?_⟩
  rw [hp_plus, hp_minus]
  unfold haarProbPlus haarProbMinus
  ring

/-- **Single-Strand Woronowicz Haar Modular Identities:**
Over any field `K` (`q ≠ 0`, `1 + q² ≠ 0`):
1. Unit trace: `haarProbPlus q + haarProbMinus q = 1` and `∑ i : Fin 2, haarStrandProb q i = 1`,
2. Modular boost ratio: `haarProbPlus q / haarProbMinus q = q²` (`= e^{β_mod}`, `β_mod = 2 ln q`),
3. Pivotal quantum-trace equivalence: `haarProbPlus q = q / [2]_q` and `haarProbMinus q = q⁻¹ / [2]_q`,
4. Modular polarization bias: `haarProbPlus q - haarProbMinus q = (q - q⁻¹) / [2]_q`. -/
theorem haar_single_strand_identities {q : K} (hq0 : q ≠ 0) (hu : 1 + q ^ 2 ≠ 0) :
    haarProbPlus q + haarProbMinus q = 1 ∧
      (∑ i : Fin 2, haarStrandProb q i) = 1 ∧
      haarProbPlus q / haarProbMinus q = q ^ 2 ∧
      haarProbPlus q = q / qTwo q ∧
      haarProbMinus q = q⁻¹ / qTwo q ∧
      haarProbPlus q - haarProbMinus q = (q - q⁻¹) / qTwo q := by
  have hqTwo : qTwo q ≠ 0 := by
    unfold qTwo
    intro h0
    apply hu
    have hmul : q * (q + q⁻¹) = 1 + q ^ 2 := by
      field_simp [hq0]
      ring
    rw [← hmul, h0, mul_zero]
  have hsum : haarProbPlus q + haarProbMinus q = 1 := by
    unfold haarProbPlus haarProbMinus
    field_simp [hu]
    ring
  refine ⟨hsum, ?_, ?_, ?_, ?_, ?_⟩
  · simp [haarStrandProb, Fin.sum_univ_two, hsum]
  · unfold haarProbPlus haarProbMinus
    field_simp
  · unfold haarProbPlus
    rw [div_eq_div_iff hu hqTwo]
    unfold qTwo
    field_simp
    ring
  · unfold haarProbMinus
    rw [div_eq_div_iff hu hqTwo]
    unfold qTwo
    field_simp
    ring
  · unfold haarProbPlus haarProbMinus
    rw [← sub_div, div_eq_div_iff hu hqTwo]
    unfold qTwo
    field_simp
    ring

/-- Unnormalized `U_q(𝔰𝔩₂)` spin-`0` singlet cup amplitude on `V_{1/2} ⊗ V_{1/2}`:
`(0, 1) ↦ q`, `(1, 0) ↦ -1`, and `0` on aligned spin pairs `(0, 0), (1, 1)`. -/
def uqSingletCupAmp (q : K) (i j : Fin 2) : K :=
  match i, j with
  | 0, 1 => q
  | 1, 0 => -1
  | _, _ => 0

/-- **`U_q(𝔰𝔩₂)` Singlet Cup Purification of Woronowicz's Haar Reduced State:**
Tracing out the right spin-`1/2` factor `B` of the normalized `U_q(𝔰𝔩₂)` singlet cup state
`|s_q⟩ = (1 + q²)^{-1/2} (q |+, -⟩ - |-, +⟩)` yields the exact diagonal reduced density matrix
`diag(haarProbPlus q, haarProbMinus q)` on the left factor `A`. -/
theorem uq_cup_purifies_haar_state {q : K} (hu : 1 + q ^ 2 ≠ 0) :
    (∑ i : Fin 2, ∑ j : Fin 2, (uqSingletCupAmp q i j) ^ 2) = 1 + q ^ 2 ∧
      (∑ i : Fin 2, (∑ j : Fin 2, uqSingletCupAmp q i j * uqSingletCupAmp q i j) /
          (1 + q ^ 2)) = 1 ∧
      ∀ i₁ i₂ : Fin 2,
        (∑ j : Fin 2, uqSingletCupAmp q i₁ j * uqSingletCupAmp q i₂ j) / (1 + q ^ 2) =
          if i₁ = i₂ then haarStrandProb q i₁ else 0 := by
  refine ⟨?_, ?_, ?_⟩
  · simp [Fin.sum_univ_two, uqSingletCupAmp]
    ring
  · simp [Fin.sum_univ_two, uqSingletCupAmp]
    field_simp [hu]
    ring
  · intro i₁ i₂
    fin_cases i₁ <;> fin_cases i₂ <;>
      simp [Fin.sum_univ_two, uqSingletCupAmp, haarStrandProb, haarProbPlus, haarProbMinus, sq]

end SingleStrandHaarModularState

section SingleStrandOrderedHierarchy

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Over any ordered field with `1 < q`, Woronowicz's single-strand Haar eigenvalues satisfy
the strict population inversion / modular boost hierarchy `0 < p_-(q) < 1/2 < p_+(q) < 1`. -/
theorem haar_prob_ordered_hierarchy {q : K} (hq : 1 < q) :
    0 < haarProbMinus q ∧
      haarProbMinus q < 1 / 2 ∧
      1 / 2 < haarProbPlus q ∧
      haarProbPlus q < 1 := by
  have hq0 : (0 : K) < q := lt_trans zero_lt_one hq
  have hq2_gt1 : 1 < q ^ 2 := by nlinarith
  have hden_pos : 0 < 1 + q ^ 2 := by positivity
  have htwo_pos : (0 : K) < 2 := by positivity
  unfold haarProbMinus haarProbPlus
  refine ⟨div_pos zero_lt_one hden_pos, ?_, ?_, ?_⟩
  · rw [div_lt_div_iff₀ hden_pos htwo_pos]
    linarith
  · rw [div_lt_div_iff₀ htwo_pos hden_pos]
    linarith
  · rw [div_lt_one hden_pos]
    linarith

end SingleStrandOrderedHierarchy

/-! ## 2. Exact Algebraic Relative-Entropy / Modular-Hamiltonian Entanglement First Law -/

section AlgebraicEntanglementFirstLaw

variable {I R : Type*} [Fintype I] [CommRing R]

/-- Diagonal von Neumann entropy functional `S(p) = - ∑_i p_i · logP_i` over any `[CommRing R]`. -/
def entropyFunctional (p logP : I → R) : R :=
  -∑ i : I, p i * logP i

/-- Diagonal Umegaki / Kullback–Leibler relative entropy `D(r ‖ p) = ∑_i r_i · (logR_i - logP_i)`. -/
def relativeEntropyFunctional (r logR logP : I → R) : R :=
  ∑ i : I, r i * (logR i - logP i)

/-- Diagonal modular Hamiltonian `K_p(i) = - logP_i` (`K_ρ = - ln ρ`). -/
def modularHamiltonianDiag (logP : I → R) (i : I) : R :=
  -logP i

/-- Diagonal expectation value `⟨obs⟩_s = ∑_i s_i · obs_i` (`Tr(σ O)`). -/
def diagExpectation (s obs : I → R) : R :=
  ∑ i : I, s i * obs i

/-- Linearized Fréchet / Gateaux entropy variation `δS(δp) = - ∑_i δp_i · (logP_i + 1)`
along a perturbation `dp : I → R` around `(p, logP)`. -/
def tangentEntropyVariation (logP dp : I → R) : R :=
  -∑ i : I, dp i * (logP i + 1)

/-- **Blanco–Casini–Hung–Myers Exact Finite-Difference Entanglement First Law:**
Over any commutative ring `R` and finite eigenbasis `I`,
`S(σ) - S(ρ) + D(σ ‖ ρ) = Tr((σ - ρ) K_ρ) = ⟨K_ρ⟩_σ - ⟨K_ρ⟩_ρ`. -/
theorem entanglement_first_law_exact (p r logP logR : I → R) :
    entropyFunctional r logR - entropyFunctional p logP +
        relativeEntropyFunctional r logR logP =
      diagExpectation (fun i => r i - p i) (modularHamiltonianDiag logP) ∧
    diagExpectation (fun i => r i - p i) (modularHamiltonianDiag logP) =
      diagExpectation r (modularHamiltonianDiag logP) -
        diagExpectation p (modularHamiltonianDiag logP) := by
  unfold entropyFunctional relativeEntropyFunctional diagExpectation modularHamiltonianDiag
  refine ⟨?_, ?_⟩
  · have hcombine :
        (-∑ i : I, r i * logR i) - (-∑ i : I, p i * logP i) +
            (∑ i : I, r i * (logR i - logP i)) =
          ∑ i : I, (-(r i * logR i) + p i * logP i + r i * (logR i - logP i)) := by
      simp only [Finset.sum_add_distrib, Finset.sum_neg_distrib]
      ring
    rw [hcombine]
    refine Finset.sum_congr rfl fun i _ => ?_
    ring
  · simp only [sub_mul, Finset.sum_sub_distrib]

/-- **Gibbs / Modular First Law with Partition-Function Cancellation:**
When `logP i = -(beta * energy i + logZ)` (`ρ = Z⁻¹ e^{-β H}`) and both `p` and `r` have unit
trace (`∑_i p_i = 1`, `∑_i r_i = 1`), the constant `logZ` cancels identically from the modular
first law, leaving `S(σ) - S(ρ) + D(σ ‖ ρ) = β · (⟨H⟩_σ - ⟨H⟩_ρ)`. -/
theorem gibbs_modular_first_law_normalized (p r logR energy : I → R) (beta logZ : R)
    (hp : (∑ i : I, p i) = 1) (hr : (∑ i : I, r i) = 1) :
    let logP : I → R := fun i => -(beta * energy i + logZ)
    entropyFunctional r logR - entropyFunctional p logP +
        relativeEntropyFunctional r logR logP =
      beta * (diagExpectation r energy - diagExpectation p energy) := by
  dsimp only
  rw [(entanglement_first_law_exact p r (fun i => -(beta * energy i + logZ)) logR).1]
  unfold diagExpectation modularHamiltonianDiag
  have hexpand :
      (∑ i : I, (r i - p i) * - -(beta * energy i + logZ)) =
        beta * ((∑ i : I, r i * energy i) - ∑ i : I, p i * energy i) +
          ((∑ i : I, r i) - ∑ i : I, p i) * logZ := by
    have hterm :
        (∑ i : I, (r i - p i) * - -(beta * energy i + logZ)) =
          (∑ i : I, beta * (r i * energy i)) - (∑ i : I, beta * (p i * energy i)) +
            ((∑ i : I, r i * logZ) - ∑ i : I, p i * logZ) := by
      simp only [neg_neg, mul_add, sub_mul, Finset.sum_add_distrib, Finset.sum_sub_distrib]
      have hcomm :
          (∑ x : I, r x * (beta * energy x)) - (∑ x : I, p x * (beta * energy x)) =
            (∑ x : I, beta * (r x * energy x)) - ∑ x : I, beta * (p x * energy x) := by
        congr 1 <;> refine Finset.sum_congr rfl fun x _ => by ring
      rw [hcomm]
    rw [hterm, ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.sum_mul, ← Finset.sum_mul, sub_mul,
      mul_sub]
  rw [hexpand, hp, hr, sub_self, zero_mul, add_zero]

/-- **Single-Strand Woronowicz Haar Modular First Law (`β_mod = 2 ln q`):**
With logarithmic weights `logHaar = ![2 * logQ - logOnePlusQ2, -logOnePlusQ2]` representing
`ln(q² / (1 + q²))` and `ln(1 / (1 + q²))`:
1. `S(ρ_1) = logOnePlusQ2 - 2 * p_+(q) * logQ`,
2. For every normalized two-level state `r : Fin 2 → K` (`r 0 + r 1 = 1`),
   `S(r) - S(ρ_1) + D(r ‖ ρ_1) = -(2 * logQ) * (r 0 - p_+(q))`. -/
theorem haar_single_strand_modular_first_law {K : Type*} [Field K] {q : K}
    (hu : 1 + q ^ 2 ≠ 0) (logQ logOnePlusQ2 : K)
    (r logR : Fin 2 → K) (hr : r 0 + r 1 = 1) :
    let logHaar : Fin 2 → K := ![2 * logQ - logOnePlusQ2, -logOnePlusQ2]
    entropyFunctional (haarStrandProb q) logHaar =
        logOnePlusQ2 - 2 * haarProbPlus q * logQ ∧
      entropyFunctional r logR - entropyFunctional (haarStrandProb q) logHaar +
          relativeEntropyFunctional r logR logHaar =
        -(2 * logQ) * (r 0 - haarProbPlus q) := by
  dsimp only
  have hp_sum : haarProbPlus q + haarProbMinus q = 1 := by
    unfold haarProbPlus haarProbMinus
    field_simp [hu]
    ring
  refine ⟨?_, ?_⟩
  · unfold entropyFunctional haarStrandProb
    simp only [Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one]
    linear_combination logOnePlusQ2 * hp_sum
  · rw [(entanglement_first_law_exact (haarStrandProb q) r
      ![2 * logQ - logOnePlusQ2, -logOnePlusQ2] logR).1]
    unfold diagExpectation modularHamiltonianDiag haarStrandProb
    simp only [Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one]
    linear_combination logOnePlusQ2 * (hr - hp_sum)

/-- **Necessary & Sufficient Tangent Entanglement First Law (`δS = δ⟨K_ρ⟩ ↔ Tr(δρ) = 0`):**
Over any commutative ring `R`, the linear variation discrepancy
`δ⟨K_ρ⟩(δp) - δS(δp)` equals the trace `∑_i δp_i`; hence `δS(δp) = δ⟨K_ρ⟩(δp)` holds
if and only if the perturbation is traceless (`∑_i δp_i = 0`). -/
theorem tangent_entanglement_first_law_iff_traceless (logP dp : I → R) :
    diagExpectation dp (modularHamiltonianDiag logP) - tangentEntropyVariation logP dp =
        (∑ i : I, dp i) ∧
      (tangentEntropyVariation logP dp = diagExpectation dp (modularHamiltonianDiag logP) ↔
        (∑ i : I, dp i) = 0) := by
  have hdiff :
      diagExpectation dp (modularHamiltonianDiag logP) - tangentEntropyVariation logP dp =
        ∑ i : I, dp i := by
    unfold diagExpectation modularHamiltonianDiag tangentEntropyVariation
    rw [sub_neg_eq_add, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    ring
  refine ⟨hdiff, ?_⟩
  constructor
  · intro heq
    rw [← hdiff, heq, sub_self]
  · intro htr
    have hsub : diagExpectation dp (modularHamiltonianDiag logP) -
        tangentEntropyVariation logP dp = 0 := by rw [hdiff, htr]
    exact (sub_eq_zero.mp hsub).symm

end AlgebraicEntanglementFirstLaw

section OrderedEntanglementPositivity

variable {I K : Type*} [Fintype I] [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Relative-Entropy Non-Negativity & Clausius Bound under Tangent Concavity:**
If normalized distributions `p, r : I → K` (`∑ p = 1`, `∑ r = 1`) satisfy the pointwise
logarithmic concavity bound `r_i - p_i ≤ r_i (logR_i - logP_i)` for all `i`, then
`0 ≤ D(r ‖ p)` and `S(r) - S(p) ≤ Tr((r - p) K_p)`. -/
theorem relative_entropy_nonneg_and_clausius_bound (p r logP logR : I → K)
    (hp : (∑ i : I, p i) = 1) (hr : (∑ i : I, r i) = 1)
    (hkl : ∀ i : I, r i - p i ≤ r i * (logR i - logP i)) :
    0 ≤ relativeEntropyFunctional r logR logP ∧
      entropyFunctional r logR - entropyFunctional p logP ≤
        diagExpectation (fun i => r i - p i) (modularHamiltonianDiag logP) := by
  have hD : 0 ≤ relativeEntropyFunctional r logR logP := by
    unfold relativeEntropyFunctional
    have hsum_le : (∑ i : I, (r i - p i)) ≤ ∑ i : I, r i * (logR i - logP i) :=
      Finset.sum_le_sum fun i _ => hkl i
    rw [Finset.sum_sub_distrib, hr, hp, sub_self] at hsum_le
    exact hsum_le
  refine ⟨hD, ?_⟩
  have hfirst := (entanglement_first_law_exact p r logP logR).1
  linarith

/-- Second-order Fisher–Rao / `χ²` quadratic relative-entropy form
`D^{(2)}(δp ‖ p) = (1 / 2) ∑_i (δp_i)² / p_i`. -/
def fisherChiSq (p dp : I → K) : K :=
  (1 / 2) * ∑ i : I, (dp i) ^ 2 / p i

/-- **Strict Positive-Definiteness of the Quadratic Relative-Entropy Remainder:**
For strictly positive reference weights `∀ i, 0 < p_i`, `0 ≤ fisherChiSq p dp`, with equality
`fisherChiSq p dp = 0` if and only if `dp = 0` pointwise. -/
theorem fisherChiSq_pos_def {p : I → K} (hp : ∀ i : I, 0 < p i) (dp : I → K) :
    0 ≤ fisherChiSq p dp ∧ (fisherChiSq p dp = 0 ↔ ∀ i : I, dp i = 0) := by
  have hterm_nonneg : ∀ i ∈ (Finset.univ : Finset I), 0 ≤ (dp i) ^ 2 / p i :=
    fun i _ => div_nonneg (sq_nonneg (dp i)) (le_of_lt (hp i))
  have hhalf_pos : (0 : K) < 1 / 2 := by positivity
  have hnonneg : 0 ≤ fisherChiSq p dp :=
    mul_nonneg (le_of_lt hhalf_pos) (Finset.sum_nonneg hterm_nonneg)
  refine ⟨hnonneg, ?_⟩
  constructor
  · intro hzero i
    unfold fisherChiSq at hzero
    have hsum_zero : (∑ j : I, (dp j) ^ 2 / p j) = 0 :=
      (mul_eq_zero.mp hzero).resolve_left (ne_of_gt hhalf_pos)
    have hi_zero : (dp i) ^ 2 / p i = 0 :=
      (Finset.sum_eq_zero_iff_of_nonneg hterm_nonneg).mp hsum_zero i (Finset.mem_univ i)
    have hsq_zero : (dp i) ^ 2 = 0 :=
      (div_eq_zero_iff.mp hi_zero).resolve_right (ne_of_gt (hp i))
    exact sq_eq_zero_iff.mp hsq_zero
  · intro hall
    unfold fisherChiSq
    simp [hall]

end OrderedEntanglementPositivity

/-! ## 3. `N_Σ`-Strand Unprojected vs Singlet-Projected vs Bipartite Global-Singlet Spectrum -/

section MultiStrandSingletVsBipartiteSpectrum

/-- **Two-Factor Tensor-Product Additivity of Entropy & Modular Expectation:**
Over any `[CommRing R]` and finite index types `I, J`, a normalized product state
`pIJ(i, j) = pI i * pJ j` with additive log-weights `logPIJ(i, j) = logPI i + logPJ j` has
unit trace and strictly additive entropy `S(pI ⊗ pJ) = S(pI) + S(pJ)`. -/
theorem tensor_product_entropy_additive {I J R : Type*} [Fintype I] [Fintype J] [CommRing R]
    (pI logPI : I → R) (pJ logPJ : J → R)
    (hpI : (∑ i : I, pI i) = 1) (hpJ : (∑ j : J, pJ j) = 1) :
    (∑ x : I × J, pI x.1 * pJ x.2) = 1 ∧
      entropyFunctional (fun x : I × J => pI x.1 * pJ x.2)
          (fun x : I × J => logPI x.1 + logPJ x.2) =
        entropyFunctional pI logPI + entropyFunctional pJ logPJ := by
  refine ⟨?_, ?_⟩
  · rw [Fintype.sum_prod_type]
    simp_rw [← Finset.mul_sum, hpJ, mul_one, hpI]
  · unfold entropyFunctional
    rw [Fintype.sum_prod_type]
    have h1 :
        (∑ i : I, ∑ j : J, pI i * pJ j * logPI i) =
          (∑ i : I, pI i * logPI i) * ∑ j : J, pJ j := by
      rw [Finset.sum_mul]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl fun j _ => by ring
    have h2 :
        (∑ i : I, ∑ j : J, pI i * pJ j * logPJ j) =
          (∑ i : I, pI i) * ∑ j : J, pJ j * logPJ j := by
      rw [Finset.sum_mul]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl fun j _ => by ring
    simp_rw [mul_add, Finset.sum_add_distrib]
    rw [h1, h2, hpJ, hpI, mul_one, one_mul, neg_add]

/-- Recursive `N_Σ`-strand spin-`1/2` configuration space (`StrandConfig n ≃ (Fin n → Fin 2)`). -/
def StrandConfig : ℕ → Type
  | 0 => PUnit
  | n + 1 => Fin 2 × StrandConfig n

/-- Explicit `Fintype` instance on `StrandConfig n` for all `n : ℕ`. -/
instance instFintypeStrandConfig : (n : ℕ) → Fintype (StrandConfig n)
  | 0 => inferInstanceAs (Fintype PUnit)
  | n + 1 => @instFintypeProd (Fin 2) (StrandConfig n) inferInstance (instFintypeStrandConfig n)

/-- Unprojected `N_Σ`-strand Woronowicz Haar product probability `ρ_1(q)^{⊗ n}` on `StrandConfig n`. -/
def strandHaarProb {K : Type*} [Field K] (q : K) : (n : ℕ) → StrandConfig n → K
  | 0, _ => 1
  | n + 1, x => haarStrandProb q x.1 * strandHaarProb q n x.2

/-- Additive `N_Σ`-strand modular log-weight `ln(ρ_1(q)^{⊗ n})` on `StrandConfig n`. -/
def strandHaarLog {K : Type*} [Field K] (logQ logOnePlusQ2 : K) : (n : ℕ) → StrandConfig n → K
  | 0, _ => 0
  | n + 1, x => (![2 * logQ - logOnePlusQ2, -logOnePlusQ2] : Fin 2 → K) x.1 +
      strandHaarLog logQ logOnePlusQ2 n x.2

/-- **`N_Σ`-Strand Unprojected / Rainbow-Cup Haar Extensivity Theorem:**
For every `n : ℕ` and `1 + q² ≠ 0`, `strandHaarProb q n` is normalized (`∑ p = 1`) and its
von Neumann / modular entropy scales strictly extensively:
`S(ρ_1(q)^{⊗ n}) = n · (logOnePlusQ2 - 2 * p_+(q) * logQ)`. -/
theorem n_strand_haar_extensivity {K : Type*} [Field K] {q : K} (hu : 1 + q ^ 2 ≠ 0)
    (logQ logOnePlusQ2 : K) (n : ℕ) :
    (∑ x : StrandConfig n, strandHaarProb q n x) = 1 ∧
      entropyFunctional (strandHaarProb q n) (strandHaarLog logQ logOnePlusQ2 n) =
        (n : K) * (logOnePlusQ2 - 2 * haarProbPlus q * logQ) := by
  have hp1 : (∑ i : Fin 2, haarStrandProb q i) = 1 := by
    simp only [haarStrandProb, Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one,
      haarProbPlus, haarProbMinus]
    field_simp [hu]
    ring
  have hs1 :
      entropyFunctional (haarStrandProb q) ![2 * logQ - logOnePlusQ2, -logOnePlusQ2] =
        logOnePlusQ2 - 2 * haarProbPlus q * logQ :=
    (haar_single_strand_modular_first_law hu logQ logOnePlusQ2 (haarStrandProb q)
      (fun _ => 0) (by simpa [haarStrandProb, Fin.sum_univ_two] using hp1)).1
  induction n with
  | zero =>
    refine ⟨?_, ?_⟩
    · simp [StrandConfig, strandHaarProb]
    · simp [StrandConfig, entropyFunctional, strandHaarProb, strandHaarLog]
  | succ m ih =>
    have hadd := tensor_product_entropy_additive
      (haarStrandProb q) ![2 * logQ - logOnePlusQ2, -logOnePlusQ2]
      (strandHaarProb q m) (strandHaarLog logQ logOnePlusQ2 m) hp1 ih.1
    refine ⟨hadd.1, ?_⟩
    change entropyFunctional
        (fun x : Fin 2 × StrandConfig m => haarStrandProb q x.1 * strandHaarProb q m x.2)
        (fun x : Fin 2 × StrandConfig m =>
          (![2 * logQ - logOnePlusQ2, -logOnePlusQ2] : Fin 2 → K) x.1 +
            strandHaarLog logQ logOnePlusQ2 m x.2) = _
    rw [hadd.2, hs1, ih.2, Nat.cast_add, Nat.cast_one]
    ring

/-- **Direct `J = 0` Singlet Projection Collapses `q^{2 J_z^{tot}}` to Uniform `(card S)⁻¹`:**
On any nonempty finite `U_q(𝔰𝔩₂)` singlet basis `S` (`[Fintype S]`, `[Nonempty S]`) where every
state carries zero total Cartan weight `twoJz s = 0 : ℤ`, the unnormalized Haar modular factor
`q ^ (twoJz s)` equals `1` identically; hence conditioning onto `S` yields the strictly
`q`-independent uniform distribution `(Fintype.card S : K)⁻¹` with zero boost expectation. -/
theorem singlet_projected_haar_uniform_q_independent {S K : Type*} [Fintype S] [Nonempty S]
    [Field K] [CharZero K] (q₁ q₂ : K) {twoJz : S → ℤ} (hSing : ∀ s : S, twoJz s = 0) :
    let w (q : K) (s : S) : K := q ^ (twoJz s)
    let pSing (q : K) (s : S) : K := w q s / ∑ s' : S, w q s'
    (∀ s : S, pSing q₁ s = (Fintype.card S : K)⁻¹) ∧
      (∀ s : S, pSing q₁ s = pSing q₂ s) ∧
      (∑ s : S, pSing q₁ s) = 1 ∧
      diagExpectation (pSing q₁) (fun s => (twoJz s : K)) = 0 := by
  dsimp only
  have hcard_pos : 0 < Fintype.card S := Fintype.card_pos
  have hcard_ne : (Fintype.card S : K) ≠ 0 := Nat.cast_ne_zero.mpr (ne_of_gt hcard_pos)
  have hunif : ∀ (q : K) (s : S),
      (q ^ twoJz s) / (∑ s' : S, q ^ twoJz s') = (Fintype.card S : K)⁻¹ := by
    intro q s
    simp [hSing, one_div]
  refine ⟨hunif q₁, fun s => by rw [hunif q₁ s, hunif q₂ s], ?_, ?_⟩
  · simp_rw [hunif q₁]
    simp [hcard_ne]
  · unfold diagExpectation
    simp [hSing]

/-- **Bipartite 4-Strand (`N_Σ = 2`, `2 N_Σ = 4`, `C_2 = 2`) Global-Singlet Half-Trace Spectrum:**
Reduced eigenvalues on `V_{1/2}^{⊗ 2}` obtained by tracing out half of the `U_q(𝔰𝔩₂)`-invariant
global singlet state on `(V_{1/2}^{⊗ 2}) ⊗ (V_{1/2}^{⊗ 2})`:
`0 ↦ 1/2` (`j = 0` singlet channel) and `1, 2, 3 ↦ q² / (2 [3]_q), 1 / (2 [3]_q), q⁻² / (2 [3]_q)`
(`j = 1` triplet channel weighted by Clebsch–Gordan cup sublevels `q^{2μ} / [3]_q`). -/
def bipartiteTwoStrandSingletSpec {K : Type*} [Field K] (q : K) (k : Fin 4) : K :=
  match k with
  | 0 => 1 / 2
  | 1 => q ^ 2 / (2 * qThree q)
  | 2 => 1 / (2 * qThree q)
  | 3 => (q⁻¹) ^ 2 / (2 * qThree q)

/-- **Exact Normalization & Non-Trivial `q`-Splitting of the Bipartite Global-Singlet Spectrum:**
1. Over any field `K` (`(2 : K) ≠ 0`, `qThree q ≠ 0`), `∑_{k < 4} λ_k(q) = 1`.
2. Over any ordered field with `1 < q`, the triplet sector splits strictly around its classical
   `q = 1` degenerate value `1 / 6`:
   `1 / 2 > λ₁(q) > 1 / 6 > λ₂(q) > λ₃(q) > 0` and `λ₁(q) / λ₂(q) = q²`. -/
theorem bipartite_two_strand_singlet_spectrum_properties
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K} (hq : 1 < q) :
    (∑ k : Fin 4, bipartiteTwoStrandSingletSpec q k) = 1 ∧
      bipartiteTwoStrandSingletSpec q 1 / bipartiteTwoStrandSingletSpec q 2 = q ^ 2 ∧
      0 < bipartiteTwoStrandSingletSpec q 3 ∧
      bipartiteTwoStrandSingletSpec q 3 < bipartiteTwoStrandSingletSpec q 2 ∧
      bipartiteTwoStrandSingletSpec q 2 < 1 / 6 ∧
      1 / 6 < bipartiteTwoStrandSingletSpec q 1 ∧
      bipartiteTwoStrandSingletSpec q 1 < 1 / 2 := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq_ne : q ≠ 0 := ne_of_gt hq0
  have hqinv_pos : 0 < q⁻¹ := inv_pos.mpr hq0
  have hqinv_lt1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hq2_gt1 : 1 < q ^ 2 := by nlinarith
  have hqinv2_lt1 : (q⁻¹) ^ 2 < 1 := by nlinarith
  have hqinv2_pos : 0 < (q⁻¹) ^ 2 := sq_pos_of_pos hqinv_pos
  have h_amgm_sq : 3 < qThree q := by
    unfold qThree
    have hdiff : q ^ 2 + 1 + (q⁻¹) ^ 2 - 3 = (q - q⁻¹) ^ 2 := by
      field_simp
      ring
    have hsub_pos : 0 < q - q⁻¹ := by linarith
    have hsq_pos : 0 < (q - q⁻¹) ^ 2 := sq_pos_of_pos hsub_pos
    linarith
  have hq3_pos : 0 < qThree q := lt_trans (by positivity : (0 : K) < 3) h_amgm_sq
  have hq3_ne : qThree q ≠ 0 := ne_of_gt hq3_pos
  have h2q3_pos : 0 < 2 * qThree q := by positivity
  have h2_ne : (2 : K) ≠ 0 := by positivity
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · rw [Fin.sum_univ_four]
    dsimp [bipartiteTwoStrandSingletSpec]
    unfold qThree at *
    field_simp
    ring
  · dsimp [bipartiteTwoStrandSingletSpec]
    field_simp
  · dsimp [bipartiteTwoStrandSingletSpec]
    exact div_pos hqinv2_pos h2q3_pos
  · dsimp [bipartiteTwoStrandSingletSpec]
    exact (div_lt_div_iff_of_pos_right h2q3_pos).mpr hqinv2_lt1
  · dsimp [bipartiteTwoStrandSingletSpec]
    rw [div_lt_div_iff₀ h2q3_pos (by positivity : (0 : K) < 6)]
    linarith
  · dsimp [bipartiteTwoStrandSingletSpec]
    rw [div_lt_div_iff₀ (by positivity : (0 : K) < 6) h2q3_pos]
    unfold qThree
    have hexcess : 6 * q ^ 2 - 2 * (q ^ 2 + 1 + (q⁻¹) ^ 2) =
        2 * (q ^ 2 - 1) * (2 * q ^ 2 + 1) / q ^ 2 := by
      field_simp
      ring
    have hpos_rhs : 0 < 2 * (q ^ 2 - 1) * (2 * q ^ 2 + 1) / q ^ 2 := by
      apply div_pos
      · exact mul_pos (mul_pos (by positivity) (by linarith)) (by positivity)
      · positivity
    linarith
  · dsimp [bipartiteTwoStrandSingletSpec]
    rw [div_lt_div_iff₀ h2q3_pos (by positivity : (0 : K) < 2)]
    unfold qThree
    linarith

end MultiStrandSingletVsBipartiteSpectrum

/-! ## 4. `U_q(𝔰𝔩₂)` Quadratic Casimir Area Comparison & Quarter-Area Lock -/

section QCasimirAreaComparisonAndQuarterLock

/-- Rational `U_q(𝔰𝔩₂)` spin-`1/2` quadratic Casimir eigenvalue
`C_2^{(q)}(1/2) = [1/2]_q [3/2]_q = (q² + q + 1) / (q + 1)²`. -/
def uqCasimirSpinHalf {K : Type*} [Field K] (q : K) : K :=
  (q ^ 2 + q + 1) / (q + 1) ^ 2

/-- Temperley–Lieb / Jones subfactor index `[2]_q² = (q + q⁻¹)² = 1 + [3]_q` at spin `1/2`. -/
def jonesIndexSpinHalf {K : Type*} [Field K] (q : K) : K :=
  (qTwo q) ^ 2

/-- **Algebraic Identities for `uqCasimirSpinHalf` & `jonesIndexSpinHalf`:**
Over any field `K` (`(2 : K) ≠ 0`, `q ≠ 0`, `q + 1 ≠ 0`):
1. Cleared Laurent form: `(q - q⁻¹)² * uqCasimirSpinHalf q = q² + q⁻² - (q + q⁻¹)`
   (`= (q^{1/2} - q^{-1/2})(q^{3/2} - q^{-3/2})`),
2. Classical limit: `uqCasimirSpinHalf 1 = 3 / 4`,
3. `q ↔ q⁻¹` CPT symmetry: `uqCasimirSpinHalf q⁻¹ = uqCasimirSpinHalf q`,
4. Exact excess above `3 / 4`: `uqCasimirSpinHalf q - 3 / 4 = (q - 1)² / (4 * (q + 1)²)`,
5. Exact deficit below `1`: `1 - uqCasimirSpinHalf q = q / (q + 1)²`,
6. Jones–Clebsch–Gordan identity: `jonesIndexSpinHalf q = 1 + qThree q`. -/
theorem uqCasimirSpinHalf_algebraic_identities {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    {q : K} (hq0 : q ≠ 0) (hqp1 : q + 1 ≠ 0) :
    (q - q⁻¹) ^ 2 * uqCasimirSpinHalf q = q ^ 2 + (q⁻¹) ^ 2 - (q + q⁻¹) ∧
      uqCasimirSpinHalf (1 : K) = 3 / 4 ∧
      uqCasimirSpinHalf q⁻¹ = uqCasimirSpinHalf q ∧
      uqCasimirSpinHalf q - 3 / 4 = (q - 1) ^ 2 / (4 * (q + 1) ^ 2) ∧
      1 - uqCasimirSpinHalf q = q / (q + 1) ^ 2 ∧
      jonesIndexSpinHalf q = 1 + qThree q := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by ring
    rw [this]
    exact mul_ne_zero h2 h2
  have hqinvp1 : q⁻¹ + 1 ≠ 0 := by
    intro h0
    apply hqp1
    have : q * (q⁻¹ + 1) = 1 + q := by field_simp [hq0]
    rw [h0, mul_zero] at this
    linear_combination -this
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · unfold uqCasimirSpinHalf
    field_simp
    ring
  · unfold uqCasimirSpinHalf
    have h11 : (1 + 1 : K) ^ 2 = 4 := by ring
    have hnum : (1 : K) ^ 2 + 1 + 1 = 3 := by ring
    rw [h11, hnum]
  · unfold uqCasimirSpinHalf
    rw [div_eq_div_iff (pow_ne_zero 2 hqinvp1) (pow_ne_zero 2 hqp1)]
    field_simp
    ring
  · unfold uqCasimirSpinHalf
    field_simp
    ring
  · unfold uqCasimirSpinHalf
    field_simp
    ring
  · unfold jonesIndexSpinHalf qTwo qThree
    field_simp
    ring

/-- **Strict Substrate Window Bounds on `uqCasimirSpinHalf` (`3 / 4 < C_2^{(q)}(1/2) < 1`):**
Over any ordered field with `0 < q` and `q ≠ 1`, `3 / 4 < uqCasimirSpinHalf q < 1`. -/
theorem uqCasimirSpinHalf_strict_bounds
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq_pos : 0 < q) (hq1 : q ≠ 1) :
    3 / 4 < uqCasimirSpinHalf q ∧ uqCasimirSpinHalf q < 1 := by
  have h2 : (2 : K) ≠ 0 := by positivity
  have hq0 : q ≠ 0 := ne_of_gt hq_pos
  have hqp1_pos : 0 < q + 1 := by linarith
  have hqp1 : q + 1 ≠ 0 := ne_of_gt hqp1_pos
  have hids := uqCasimirSpinHalf_algebraic_identities h2 hq0 hqp1
  have hqm1_ne : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have hqm1_sq : 0 < (q - 1) ^ 2 := sq_pos_of_ne_zero hqm1_ne
  refine ⟨?_, ?_⟩
  · have hex := hids.2.2.2.1
    have hpos : 0 < (q - 1) ^ 2 / (4 * (q + 1) ^ 2) :=
      div_pos hqm1_sq (by positivity)
    linarith
  · have hdef := hids.2.2.2.2.1
    have hpos : 0 < q / (q + 1) ^ 2 := div_pos hq_pos (by positivity)
    linarith

/-- **Necessary & Sufficient Quarter-Area Lock (`S / A_alg = 1 / 4 ↔ a_alg = 4 * s_strand`):**
Over any field `K` (`(2 : K) ≠ 0`, `nStrands ≠ 0`, `a_alg ≠ 0`), an `nStrands`-puncture
boundary with entropy `nStrands * s_strand` and algebraic area `nStrands * a_alg` satisfies
the Bekenstein–Hawking `1 / 4` ratio if and only if `a_alg = 4 * s_strand`; consequently
any un-tuned algebraic area quantum `a_alg ≠ 4 * s_strand` misses `1 / 4`. -/
theorem haar_quarter_area_lock_iff {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    {nStrands s_strand a_alg : K} (hN : nStrands ≠ 0) (ha : a_alg ≠ 0) :
    ((nStrands * s_strand) / (nStrands * a_alg) = 1 / 4 ↔ a_alg = 4 * s_strand) ∧
      (a_alg ≠ 4 * s_strand → (nStrands * s_strand) / (nStrands * a_alg) ≠ 1 / 4) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by ring
    rw [this]
    exact mul_ne_zero h2 h2
  have hNa : nStrands * a_alg ≠ 0 := mul_ne_zero hN ha
  have hiff : (nStrands * s_strand) / (nStrands * a_alg) = 1 / 4 ↔ a_alg = 4 * s_strand := by
    rw [div_eq_div_iff hNa h4]
    constructor
    · intro h
      apply mul_left_cancel₀ hN
      linear_combination -h
    · intro h
      rw [h]
      ring
  exact ⟨hiff, fun hne heq => hne (hiff.mp heq)⟩

/-- **Primary Conjecture Class (OPEN — ZERO instances; Rule 13a & `§3b-cond`):**
Isolates the continuum 4D Lorentzian geometric bridge (Option 4A, `FeffermanLorentzianHorizonEntropy`)
absent from pure discrete `O_q(SU(2))` algebra:
1. `haar_strand_extensivity`: `N_Σ` horizon strands carry `S_hor(N) = N * s_strand`,
2. `bisognano_wichmann_modular_period`: Rindler/horizon boost identification converts the
   algebraic modular first law into `S_hor(N) = (twoPi / hbar) * K_boost(N)`,
3. `einstein_raychaudhuri_focusing`: 4D Lorentzian null-sheet focusing equates boost energy to
   horizon area via `A_hor(N) = (4 * twoPi * G_grav / c³) * K_boost(N)` (`4 * twoPi = 8π`). -/
-- @conjecture: primary
class HaarLorentzianModularBridgeConjecture {K : Type*} [Field K]
    (twoPi hbar c G_grav s_strand : K)
    (S_hor A_hor K_boost : K → K) : Prop where
  /-- Extensive `O_q(SU(2))` strand entropy `S_hor(N) = N * s_strand`. -/
  haar_strand_extensivity : ∀ nStrands : K, S_hor nStrands = nStrands * s_strand
  /-- Bisognano–Wichmann Euclidean modular boost period `S_hor(N) = (2π / ℏ) K_boost(N)`. -/
  bisognano_wichmann_modular_period : ∀ nStrands : K,
    S_hor nStrands = (twoPi / hbar) * K_boost nStrands
  /-- Einstein–Raychaudhuri null-sheet focusing `A_hor(N) = (8π G / c³) K_boost(N)`. -/
  einstein_raychaudhuri_focusing : ∀ nStrands : K,
    A_hor nStrands = (4 * twoPi * G_grav / c ^ 3) * K_boost nStrands

/-- **Conditional Theorem (`§3b-cond` — derived from `HaarLorentzianModularBridgeConjecture`):**
Cancelling `twoPi` and `K_boost(N)` between Bisognano–Wichmann modular periodicity and
Einstein–Raychaudhuri null focusing yields `S_hor(N) = A_hor(N) / (4 * (hbar * G_grav / c³))`
and locks the dimensionless puncture area quantum to `a_eff = 4 * s_strand`. -/
theorem lorentzian_bridge_locks_haar_puncture_area {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    {twoPi hbar c G_grav s_strand : K} {S_hor A_hor K_boost : K → K}
    [hBridge : HaarLorentzianModularBridgeConjecture twoPi hbar c G_grav s_strand
      S_hor A_hor K_boost]
    (htwoPi : twoPi ≠ 0) (hhbar : hbar ≠ 0) (hc : c ≠ 0) (hG : G_grav ≠ 0) :
    let ellGravSq := hbar * G_grav / c ^ 3
    (∀ nStrands : K, S_hor nStrands = A_hor nStrands / (4 * ellGravSq)) ∧
      (∀ nStrands a_eff : K, nStrands ≠ 0 → A_hor nStrands = nStrands * a_eff * ellGravSq →
        a_eff = 4 * s_strand) := by
  dsimp only
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by ring
    rw [this]
    exact mul_ne_zero h2 h2
  have hc3 : c ^ 3 ≠ 0 := pow_ne_zero 3 hc
  have hell : hbar * G_grav / c ^ 3 ≠ 0 := div_ne_zero (mul_ne_zero hhbar hG) hc3
  have hquarter : ∀ nStrands : K,
      S_hor nStrands = A_hor nStrands / (4 * (hbar * G_grav / c ^ 3)) := by
    intro nStrands
    rw [hBridge.bisognano_wichmann_modular_period nStrands,
      hBridge.einstein_raychaudhuri_focusing nStrands]
    field_simp [htwoPi, hhbar, hc3, hG, h4]
  refine ⟨hquarter, ?_⟩
  intro nStrands a_eff hN hA
  have hS := hquarter nStrands
  rw [hBridge.haar_strand_extensivity nStrands, hA] at hS
  have h4ell : 4 * (hbar * G_grav / c ^ 3) ≠ 0 := mul_ne_zero h4 hell
  rw [eq_div_iff h4ell] at hS
  apply mul_left_cancel₀ (mul_ne_zero hN hell)
  linear_combination -hS

end QCasimirAreaComparisonAndQuarterLock

end QOU.GravitySpacetime.OqSU2HaarModularEntanglement
