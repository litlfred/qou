import QOU.ParticleInteractions.operator_selection_lp
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
import QOU.Interactions.NuclearOperatorRegimes

/-!
# Two-Term Photon/QED Cost Operator and GPMT Full-Rank Gram Completion for the Confinement LP/SDP

Under the one-term Markov trace on the six-dimensional normal-form basis
`[γ = 1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, e⁻ = σ₀σ₁σ₀]` of `H₃(q)` at Convention D (`z_D = q³ / (q² + 1)`),
two distinct degeneracies govern the operator-selection linear and semidefinite programs
(`qou-augu`, `qou-ndsa`, `qou-fadg`, `qou-egqr`):

1. **Identity-Row Cost Tautology (`c = G e₀ ⇒ y₀* = 0`, `qou-augu` & `qou-ndsa`)**:
   Whenever the cost vector equals row `0` of the Gram matrix (`c_j = τ(b_j) = τ(1 · b_j) = G_{0j}`),
   the pair `(y₀, s) = (0, e₀)` is dual-feasible with dual value `0`, bounding the primal objective
   by its own `i = 0` Frobenius constraint `(G x)₀ ≥ 0`. This holds for *every* one-term trace
   functional `τ` on `H₃(q)`, regardless of whether `G` is singular or invertible.

2. **Convention-D Antisymmetric Radical (`rank G^{z_D} = 5 < 6`, `qou-fadg` & `qou-egqr`)**:
   At `z_D = q³ / (q² + 1)`, the `(1³)` Wedderburn weight vanishes (`w_{(1³)}(z_D) = 0`), leaving a
   one-dimensional radical spanned by the `q`-antisymmetriser `radicalVec q`. Moreover, because the
   three-strand two-flavour weight spaces `(2,1)` and `(1,2)` of `(K²)^{⊗3}` contain only Young
   diagrams of at most two rows, any two-flavour electromagnetic trace insertion `tr(Q b_j)` is
   orthogonal to `radicalVec q`; hence on the uncompleted rank-5 Gram `G^{z_D}`, `y₀ = 0` remains
   forced by `y_0_eq_zero_of_cost_perp_radical`.

3. **Joint Resolution via Two-Term Photon/QED Cost + GPMT Modified-Trace Gram Completion**:
   * **Mechanism 2 (GPMT Gram Completion)**: Adding the positive Geer–Patureau-Mirand–Turaev
     modified quantum dimension `|d_D(S^{(1³)})| = q³ / ((q² + 1)(q⁴ + q² + 1)) = 1 / ([2]_q [3]_q)`
     on the killed `(1³)` sector yields `trGPMT` and `gramGPMT`, whose three Wedderburn weights
     `(w_{(3)}(z_D), w_{(2,1)}(z_D), |d_D(S^{(1³)})|)` are all strictly positive for every real
     `q > 0`. On `gramGPMT`, `radicalVec q` becomes an eigenvector of eigenvalue `q⁻³ > 0`, the
     pairing on `K × M₂(K) × K` (`1 + 4 + 1 = 6`) has trivial kernel, `det(gramGPMT q) ≠ 0`, and
     every normal-form demand `gramGPMT q *ᵥ x = nf` has a unique solution `x*`.
   * **Mechanism 1 (Two-Term Photon/QED Cost & Polarized / `γγ`-Vertex Chirality Split)**:
     Adding the two-term electromagnetic charge trace `qedCostProton` (`Q₁₂^{(p)} + Q₂₃^{(p)}`) or
     `qedCostNeutron` (`Q₁₂^{(n)} + Q₂₃^{(n)}`) breaks proportionality to the Markov cost row
     (`c_twoTerm ≠ λ • TRM`) and breaks `σ₀ ↔ σ₁` generator mirror symmetry on `(u,u,d)` and
     `(u,d,d)`. Coupling with polarized crossing operators (`Q₂₃^{(p)} A₁`, `Q₁₂^{(p)} ≠ Q₂₃^{(p)}`)
     or the `γγ` pair-production vertex `V = σ₀ σ₁⁻¹` (`qou-ales`) further splits `L₊ = σ₀σ₁` from
     `L₋ = σ₁σ₀` (`NuclearOperatorRegimes.hopf_links_distinct`). On the GPMT-completed simplex cone
     (`1 < q ≤ 9/8`, `0 < α ≤ 1`, containing `q₀` and `α_EM(q₀)`), the two-term proton program
     admits a closed-form unique primal–dual optimum concentrated on the trefoil channel `e⁻` with
     strictly negative shadow price `y₀*(q, α) < 0` (`y₀* ≠ 0`).
   * **Mechanism 3 (`RegimeTransitionZ2` & `He4DemandClosure`, `cj01` & `qou-j540`)**:
     On `21/20 ≤ q ≤ 6/5` (`q₀ ≈ 1.10998`), `L₊` strictly dominates `T_{2,5}` under both `trGPMT`
     and the two-term proton functional (`RegimeTransitionZ2`), and `He4DemandClosure` is equivalent
     to vanishing demand magnitude `listDemMag coeffs = 0`.
-/

namespace QOU.Interactions.TwoTermPhotonGPMTConfinementSDP

open Matrix BigOperators
open QOU.ParticleInteractions
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
open QOU.Machinery.H3
open QOU.Interactions

-- ============================================================================
-- § 1. Identity-Row Cost Degeneracy (`c = G e₀ ⇒ y₀* = 0`, `qou-augu`)
-- ============================================================================

section IdentityRowDegeneracy

/-- When the cost vector `c` coincides with row `0` of `G` and `x_star` is feasible with
tight `0`-th Frobenius row, `(y₀* = 0, s* = e₀)` forms an `OperatorSelectionLpContext`
certificate with zero duality gap. -/
def lpContextOfCostEqGramRow0 {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (n d : ℕ) [NeZero d] (n_target : R) (c : Fin d → R) (G : Fin d → Fin d → R)
    (x_star : Fin d → R)
    (hc : ∀ j, c j = G 0 j)
    (hnet : (∑ j, x_star j) = n_target)
    (hpos : ∀ i, 0 ≤ ∑ j, G i j * x_star j)
    (htight0 : (∑ j, G 0 j * x_star j) = 0) :
    OperatorSelectionLpContext R :=
  OperatorSelectionLpContext.ofCertificate n d n_target c G x_star 0
    (fun i => if i = 0 then 1 else 0)
    (fun i => by by_cases h : i = 0 <;> simp [h])
    (fun j => by simp [hc j, ite_mul])
    hnet hpos
    (fun i => by
      by_cases h : i = 0
      · subst h; simp [htight0]
      · simp [h])

/-- Root-cause theorem for `qou-augu`: whenever `c = G e₀` and a feasible `x_star` satisfies
`(G x_star)₀ = 0`, `y₀* = 0` with `s* = e₀` is dual-optimal and the minimum objective over all
feasible vectors is identically `0`, independent of `n_target`. -/
theorem zero_shadow_price_optimal_of_cost_eq_gram_row0
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    {d : ℕ} [NeZero d] {n_target : R} {c : Fin d → R} {G : Fin d → Fin d → R}
    {x_star : Fin d → R}
    (hc : ∀ j, c j = G 0 j)
    (hnet : (∑ j, x_star j) = n_target)
    (hpos : ∀ i, 0 ≤ ∑ j, G i j * x_star j)
    (htight0 : (∑ j, G 0 j * x_star j) = 0) :
    DualCertificateExists c G ∧
    (∑ j, c j * x_star j) = 0 ∧
    ∀ x : Fin d → R,
      ((∑ i, x i) = n_target ∧ ∀ i, 0 ≤ ∑ j, G i j * x j) →
        0 ≤ ∑ j, c j * x j := by
  let ctx := lpContextOfCostEqGramRow0 3 d n_target c G x_star hc hnet hpos htight0
  have hmain := @operator_selection_lp R _ _ _ ctx
  refine ⟨dualCertificateExists_of_cost_eq_gram_row c G 0 hc, ?_, ?_⟩
  · have hgap := hmain.2.2
    change (∑ i, c i * x_star i) = n_target * 0 at hgap
    simpa using hgap
  · intro x hx
    have hle := hmain.2.1 x hx
    have hgap := hmain.2.2
    change (∑ i, c i * x_star i) = n_target * 0 at hgap
    rw [mul_zero] at hgap
    change (∑ i, c i * x_star i) ≤ ∑ i, c i * x i at hle
    rwa [hgap] at hle

/-- Bilinear Gram matrix associated to any linear functional `τ` on `H₃(q)` normal-form vectors. -/
def gramOfTrace {R : Type*} [CommRing R] (h : R) (τ : (Fin 6 → R) → R) (i j : Fin 6) : R :=
  τ (mulNF h (Pi.single i 1) (Pi.single j 1))

/-- Left identity law of `mulNF` at the empty-word basis vector `Pi.single 0 1`. -/
theorem mulNF_unit_left {R : Type*} [CommRing R] (h : R) (v : Fin 6 → R) :
    mulNF h (Pi.single 0 1) v = v := by
  funext k
  fin_cases k <;> simp [mulNF, mulσ₀, mulσ₁]

/-- For *any* trace functional `τ` on `H₃(q)` (Convention C, Convention D, or GPMT-completed),
its one-term basis cost vector `j ↦ τ(b_j)` is identically row `0` of its own Gram matrix. -/
theorem oneTerm_cost_eq_gramOfTrace_row0 {R : Type*} [CommRing R] (h : R)
    (τ : (Fin 6 → R) → R) (j : Fin 6) :
    τ (Pi.single j 1) = gramOfTrace h τ 0 j := by
  unfold gramOfTrace
  rw [mulNF_unit_left]

end IdentityRowDegeneracy

-- ============================================================================
-- § 2. Two-Term Photon/QED Cost Vector: Breaking `c = λ G e₀` and Mirror Symmetry
-- ============================================================================

section TwoTermQEDCost

variable {K : Type*} [Field K]

/-- The six normal-form basis matrices `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]` on the 3D proton
`(2,1)` weight space (matching the coordinate order of `QOU.Machinery.H3.mulNF`). -/
def nfBasisProton (q : K) : Fin 6 → Matrix (Fin 3) (Fin 3) K
  | 0 => 1
  | 1 => A₁ q
  | 2 => A₂ q
  | 3 => A₂ q * A₁ q
  | 4 => A₁ q * A₂ q
  | 5 => A₁ q * A₂ q * A₁ q

/-- The six normal-form basis matrices `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]` on the 3D neutron
`(1,2)` weight space (matching the coordinate order of `QOU.Machinery.H3.mulNF`). -/
def nfBasisNeutron (q : K) : Fin 6 → Matrix (Fin 3) (Fin 3) K
  | 0 => 1
  | 1 => B₁ q
  | 2 => B₂ q
  | 3 => B₂ q * B₁ q
  | 4 => B₁ q * B₂ q
  | 5 => B₁ q * B₂ q * B₁ q

/-- Adjacent-crossing electromagnetic trace vector `j ↦ tr((Q₁₂^{(p)} + Q₂₃^{(p)}) b_j)` on `(u,u,d)`. -/
def qedCostProton (q : K) (j : Fin 6) : K :=
  ((Q12p + Q23p : Matrix (Fin 3) (Fin 3) K) * nfBasisProton q j).trace

/-- Adjacent-crossing electromagnetic trace vector `j ↦ tr((Q₁₂^{(n)} + Q₂₃^{(n)}) b_j)` on `(u,d,d)`. -/
def qedCostNeutron (q : K) (j : Fin 6) : K :=
  ((Q12n + Q23n : Matrix (Fin 3) (Fin 3) K) * nfBasisNeutron q j).trace

/-- Two-term confinement cost vector `c_j = E₀ · τ_j + α · E₀ · qed_j` combining a strong
trace vector `τ` with a photon/QED charge-insertion vector `qed` at coupling `α`. -/
def twoTermCost (E0 α : K) (τ qed : Fin 6 → K) (j : Fin 6) : K :=
  E0 * τ j + α * E0 * qed j

theorem qedCostProton_zero (q : K) : qedCostProton q 0 = 0 := by
  simp [qedCostProton, nfBasisProton, Q12p, Q23p, Matrix.trace_fin_three]
  ring

theorem qedCostProton_one (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    qedCostProton q 1 = 2 * (2 * q ^ 2 - 1) / (9 * q) := by
  have h9 : (9 : K) = 3 * 3 := by ring
  simp [qedCostProton, nfBasisProton, Q12p, Q23p, A₁, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem qedCostProton_two (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    qedCostProton q 2 = -2 * (q ^ 2 - 2) / (9 * q) := by
  have h9 : (9 : K) = 3 * 3 := by ring
  simp [qedCostProton, nfBasisProton, Q12p, Q23p, A₂, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem qedCostProton_three (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    qedCostProton q 3 = 2 * (q ^ 2 - 1) / 9 := by
  have h9 : (9 : K) = 3 * 3 := by ring
  simp [qedCostProton, nfBasisProton, Q12p, Q23p, A₁, A₂, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem qedCostProton_four (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    qedCostProton q 4 = 2 * (q ^ 2 - 1) / 9 := by
  have h9 : (9 : K) = 3 * 3 := by ring
  simp [qedCostProton, nfBasisProton, Q12p, Q23p, A₁, A₂, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem qedCostProton_five (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    qedCostProton q 5 = 2 * q * (q ^ 2 - 3) / 9 := by
  have h9 : (9 : K) = 3 * 3 := by ring
  simp [qedCostProton, nfBasisProton, Q12p, Q23p, A₁, A₂, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

/-- Generator mirror-symmetry breaking on `(u,u,d)`: `qedCostProton q 1 - qedCostProton q 2`
equals `2 (q² - 1) / (3 q)`, which is non-zero whenever `q ≠ 0, ±1`. -/
theorem qedCostProton_gen_asymmetry (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    qedCostProton q 1 - qedCostProton q 2 = 2 * (q ^ 2 - 1) / (3 * q) := by
  have h9 : (9 : K) = 3 * 3 := by ring
  rw [qedCostProton_one q hq h3, qedCostProton_two q hq h3, h9]
  field_simp
  ring

/-- Generator mirror-symmetry breaking on `(u,d,d)`: `qedCostNeutron q 1 - qedCostNeutron q 2`
equals `-(q² - 1) / (3 q)`, half the magnitude and opposite in sign to the proton split. -/
theorem qedCostNeutron_gen_asymmetry (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    qedCostNeutron q 1 - qedCostNeutron q 2 = -(q ^ 2 - 1) / (3 * q) := by
  have h9 : (9 : K) = 3 * 3 := by ring
  simp [qedCostNeutron, nfBasisNeutron, Q12n, Q23n, B₁, B₂, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

/-- **Breaking `c = λ G e₀` on the proton (`qou-augu` & `qou-ndsa`)**:
For any mirror-symmetric strong trace vector `τ` (`τ 1 = τ 2`, including both Convention-D
`TRM (zD q)` and GPMT-completed `trGPMT q`) and non-zero `E0, α`, the two-term proton cost
vector is not a scalar multiple of `τ` whenever `q ≠ 0` and `q² ≠ 1`. -/
theorem twoTermCost_proton_not_collinear
    (q E0 α : K) (τ : Fin 6 → K) (hτ_sym : τ 1 = τ 2)
    (hq : q ≠ 0) (hq1 : q ^ 2 ≠ 1) (hE0 : E0 ≠ 0) (hα : α ≠ 0)
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    ¬ ∃ lam : K, ∀ j : Fin 6, twoTermCost E0 α τ (qedCostProton q) j = lam * τ j := by
  rintro ⟨lam, hlam⟩
  have hsub : twoTermCost E0 α τ (qedCostProton q) 1 -
      twoTermCost E0 α τ (qedCostProton q) 2 = 0 := by
    rw [hlam 1, hlam 2, hτ_sym, sub_self]
  have hdiff : twoTermCost E0 α τ (qedCostProton q) 1 -
      twoTermCost E0 α τ (qedCostProton q) 2 =
      α * E0 * (qedCostProton q 1 - qedCostProton q 2) := by
    unfold twoTermCost
    rw [hτ_sym]
    ring
  rw [hdiff, qedCostProton_gen_asymmetry q hq h3] at hsub
  have hnum : 2 * (q ^ 2 - 1) / (3 * q) ≠ 0 :=
    div_ne_zero (mul_ne_zero h2 (sub_ne_zero.mpr hq1)) (mul_ne_zero h3 hq)
  exact mul_ne_zero (mul_ne_zero hα hE0) hnum hsub

/-- **Breaking `c = λ G e₀` on the neutron (`qou-augu` & `qou-ndsa`)**:
For any mirror-symmetric strong trace vector `τ` (`τ 1 = τ 2`) and non-zero `E0, α`, the
two-term neutron cost vector is not a scalar multiple of `τ` whenever `q ≠ 0` and `q² ≠ 1`. -/
theorem twoTermCost_neutron_not_collinear
    (q E0 α : K) (τ : Fin 6 → K) (hτ_sym : τ 1 = τ 2)
    (hq : q ≠ 0) (hq1 : q ^ 2 ≠ 1) (hE0 : E0 ≠ 0) (hα : α ≠ 0)
    (h3 : (3 : K) ≠ 0) :
    ¬ ∃ lam : K, ∀ j : Fin 6, twoTermCost E0 α τ (qedCostNeutron q) j = lam * τ j := by
  rintro ⟨lam, hlam⟩
  have hsub : twoTermCost E0 α τ (qedCostNeutron q) 1 -
      twoTermCost E0 α τ (qedCostNeutron q) 2 = 0 := by
    rw [hlam 1, hlam 2, hτ_sym, sub_self]
  have hdiff : twoTermCost E0 α τ (qedCostNeutron q) 1 -
      twoTermCost E0 α τ (qedCostNeutron q) 2 =
      α * E0 * (qedCostNeutron q 1 - qedCostNeutron q 2) := by
    unfold twoTermCost
    rw [hτ_sym]
    ring
  rw [hdiff, qedCostNeutron_gen_asymmetry q hq h3] at hsub
  have hnum : -(q ^ 2 - 1) / (3 * q) ≠ 0 :=
    div_ne_zero (neg_ne_zero.mpr (sub_ne_zero.mpr hq1)) (mul_ne_zero h3 hq)
  exact mul_ne_zero (mul_ne_zero hα hE0) hnum hsub

/-- In particular, `twoTermCost` on the Convention-D Markov vector `TRM (zD q) (q - q⁻¹)` is
never proportional to `TRM (zD q) (q - q⁻¹)` for `q ≠ 0, ±1`. -/
theorem twoTermCost_proton_not_collinear_TRM
    (q E0 α : K) (hq : q ≠ 0) (hq1 : q ^ 2 ≠ 1) (hE0 : E0 ≠ 0) (hα : α ≠ 0)
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    ¬ ∃ lam : K, ∀ j : Fin 6,
      twoTermCost E0 α (TRM (zD q) (q - q⁻¹)) (qedCostProton q) j =
        lam * TRM (zD q) (q - q⁻¹) j :=
  twoTermCost_proton_not_collinear q E0 α (TRM (zD q) (q - q⁻¹)) rfl hq hq1 hE0 hα h2 h3

/-- The two local pairwise charge operators `Q₁₂^{(p)}` and `Q₂₃^{(p)}` on `(u,u,d)` are distinct. -/
theorem Q12p_ne_Q23p (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    (Q12p : Matrix (Fin 3) (Fin 3) K) ≠ Q23p := by
  intro h
  have h00 : ((Q12p - Q23p : Matrix (Fin 3) (Fin 3) K) 0 0) = 0 := by
    rw [sub_eq_zero.mpr h, Matrix.zero_apply]
  have hval : ((Q12p - Q23p : Matrix (Fin 3) (Fin 3) K) 0 0) = 2 / 3 := by
    have h9 : (9 : K) = 3 * 3 := by ring
    simp [Q12p, Q23p]
    rw [h9]; field_simp; ring
  rw [hval] at h00
  exact div_ne_zero h2 h3 h00

/-- **Polarized Crossing Asymmetry Splits `L₊ = σ₀σ₁` from `L₋ = σ₁σ₀`**:
Companion to `NuclearOperatorRegimes.hopf_links_distinct` (`hopfPlus ≠ hopfMinus`): while any
diagonal operator gives equal traces on `L₊` and `L₋`, the polarized crossing insertion
`Q₂₃^{(p)} A₁` separates `nfBasisProton q 4` (`σ₀σ₁`) from `nfBasisProton q 3` (`σ₁σ₀`) by `2 / (3q)`. -/
theorem polarized_crossing_splits_hopf_links
    (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    ((Q23p : Matrix (Fin 3) (Fin 3) K) * A₁ q * nfBasisProton q 4).trace -
      ((Q23p : Matrix (Fin 3) (Fin 3) K) * A₁ q * nfBasisProton q 3).trace =
        2 / (3 * q) ∧
    ((Q23p : Matrix (Fin 3) (Fin 3) K) * A₁ q * nfBasisProton q 4).trace ≠
      ((Q23p : Matrix (Fin 3) (Fin 3) K) * A₁ q * nfBasisProton q 3).trace := by
  have h9 : (9 : K) = 3 * 3 := by ring
  have heq :
      ((Q23p : Matrix (Fin 3) (Fin 3) K) * A₁ q * nfBasisProton q 4).trace -
        ((Q23p : Matrix (Fin 3) (Fin 3) K) * A₁ q * nfBasisProton q 3).trace =
        2 / (3 * q) := by
    simp [nfBasisProton, Q23p, A₁, A₂, Matrix.trace_fin_three]
    rw [h9]; field_simp; ring
  refine ⟨heq, fun hsame => ?_⟩
  rw [sub_eq_zero.mpr hsame] at heq
  exact div_ne_zero h2 (mul_ne_zero h3 hq) heq.symm

end TwoTermQEDCost

-- ============================================================================
-- § 3. GPMT Modified-Trace Gram Completion: Resolving Rank-5 Singularity (`qou-fadg`, `qou-egqr`)
-- ============================================================================

section GPMTGramCompletion

variable {K : Type*} [Field K]

/-- The Convention-D Frobenius Gram matrix on `H₃(q)` normal-form coordinates. -/
def gramD (q : K) (i j : Fin 6) : K :=
  trM (zD q) (q - q⁻¹) (mulNF (q - q⁻¹) (Pi.single i 1) (Pi.single j 1))

/-- Positive GPMT modified quantum dimension `|d_D(S^{(1³)})| = -dMod111 q = 1 / ([2]_q [3]_q)`
of the antisymmetric `(1³)` sector at Convention D. -/
def dMod111Abs (q : K) : K := -dMod111 q

theorem dMod111Abs_eq (q : K) :
    dMod111Abs q = q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  unfold dMod111Abs dMod111
  ring

theorem dMod111Abs_eq_inv_qInt2_mul_qInt3 (q : K) (hq : q ≠ 0) :
    dMod111Abs q = 1 / ((q + q⁻¹) * QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.qInt3 q) := by
  rw [dMod111Abs_eq]
  unfold QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.qInt3
  field_simp

/-- The GPMT-completed trace functional `trGPMT q v = tr_M^{z_D}(v) + |d_D(S^{(1³)})| χ_{(1³)}(v)`
restoring the killed `(1³)` sector with positive weight `dMod111Abs q`. -/
noncomputable def trGPMT (q : K) (v : Fin 6 → K) : K :=
  trM (zD q) (q - q⁻¹) v + dMod111Abs q * chi111 q v

/-- The `6 × 6` GPMT-completed Frobenius Gram matrix on `H₃(q)`. -/
noncomputable def gramGPMT (q : K) (i j : Fin 6) : K :=
  trGPMT q (mulNF (q - q⁻¹) (Pi.single i 1) (Pi.single j 1))

/-- Three-sector Wedderburn character decomposition of `trGPMT`. -/
theorem trGPMT_eq_wedderburn_sum (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (v : Fin 6 → K) :
    trGPMT q v =
      w3 q (zD q) * chi3 q v + w21 q (zD q) * chi21 q v + dMod111Abs q * chi111 q v := by
  unfold trGPMT
  rw [trM_eq_wedderburn_sum q (zD q) hq hq2 hq4 v, w111_conventionD q hq2, zero_mul, add_zero]

/-- `trGPMT` is additive. -/
theorem trGPMT_add (q : K) (u v : Fin 6 → K) :
    trGPMT q (u + v) = trGPMT q u + trGPMT q v := by
  unfold trGPMT chi111
  rw [trM_add]
  simp only [chiNF, Pi.add_apply]
  ring

/-- `trGPMT` is `K`-homogeneous. -/
theorem trGPMT_smul (q c : K) (v : Fin 6 → K) :
    trGPMT q (c • v) = c * trGPMT q v := by
  unfold trGPMT chi111
  rw [trM_smul]
  simp only [chiNF, Pi.smul_apply, smul_eq_mul]
  ring

/-- `trGPMT` is cyclic (`trGPMT q (u · v) = trGPMT q (v · u)`), so `gramGPMT q` is symmetric. -/
theorem trGPMT_cyclic (q : K) (hq : q ≠ 0) (u v : Fin 6 → K) :
    trGPMT q (mulNF (q - q⁻¹) u v) = trGPMT q (mulNF (q - q⁻¹) v u) := by
  have hl : (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by
    field_simp; ring
  unfold trGPMT chi111
  rw [trM_cyclic, chiNF_mulNF (q - q⁻¹) (-q⁻¹) hl u v,
      chiNF_mulNF (q - q⁻¹) (-q⁻¹) hl v u]
  ring

theorem gramGPMT_symm (q : K) (hq : q ≠ 0) (i j : Fin 6) :
    gramGPMT q i j = gramGPMT q j i :=
  trGPMT_cyclic q hq (Pi.single i 1) (Pi.single j 1)

/-- Right-linearity of `mulNF` decomposed along the six normal-form basis vectors `Pi.single j 1`,
without unfolding the generator actions `mulσ₀`, `mulσ₁`. -/
theorem mulNF_eq_sum_single_right {R : Type*} [CommRing R] (h : R) (u v : Fin 6 → R) :
    mulNF h u v =
      v 0 • mulNF h u (Pi.single 0 1) +
      v 1 • mulNF h u (Pi.single 1 1) +
      v 2 • mulNF h u (Pi.single 2 1) +
      v 3 • mulNF h u (Pi.single 3 1) +
      v 4 • mulNF h u (Pi.single 4 1) +
      v 5 • mulNF h u (Pi.single 5 1) := by
  funext k
  simp only [mulNF, Pi.add_apply, Pi.smul_apply, smul_eq_mul, Pi.single_apply,
    Fin.isValue, Fin.reduceEq, ↓reduceIte]
  ring

/-- Row dot-product of `gramGPMT q` with any vector `v` equals `trGPMT q (b_i · v)`. -/
theorem gramGPMT_row_dot (q : K) (i : Fin 6) (v : Fin 6 → K) :
    (∑ j : Fin 6, gramGPMT q i j * v j) =
      trGPMT q (mulNF (q - q⁻¹) (Pi.single i 1) v) := by
  rw [mulNF_eq_sum_single_right (q - q⁻¹) (Pi.single i 1) v]
  simp only [trGPMT_add, trGPMT_smul, Fin.sum_univ_six, gramGPMT]
  ring

/-- Wedderburn character decomposition of the `i`-th row dot-product `(gramGPMT q *ᵥ w)_i`. -/
theorem gramGPMT_mulVec_wedderburn (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (w : Fin 6 → K) (i : Fin 6) :
    (∑ j : Fin 6, gramGPMT q i j * w j) =
      w3 q (zD q) * chi3 q (Pi.single i 1) * chi3 q w +
      w21 q (zD q) * (blockOf q (Pi.single i 1) * blockOf q w).trace +
      dMod111Abs q * chi111 q (Pi.single i 1) * chi111 q w := by
  have hq_root : q * q = (q - q⁻¹) * q + 1 := by field_simp; ring
  have hl_root : (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by field_simp; ring
  rw [gramGPMT_row_dot q i w, trGPMT_eq_wedderburn_sum q hq hq2 hq4]
  unfold chi3 chi21 chiM chi111
  rw [chiNF_mulNF (q - q⁻¹) q hq_root, blockOf_mulNF q hq hq2,
      chiNF_mulNF (q - q⁻¹) (-q⁻¹) hl_root]
  ring

/-- Bilinear pairing identity: `∑_{i,j} u_i · gramGPMT_{ij} · v_j = trGPMT(u · v)`. -/
theorem gramGPMT_bilinear_eq_trGPMT (q : K) (hq : q ≠ 0) (u v : Fin 6 → K) :
    (∑ i : Fin 6, u i * ∑ j : Fin 6, gramGPMT q i j * v j) =
      trGPMT q (mulNF (q - q⁻¹) u v) := by
  simp_rw [gramGPMT_row_dot q _ v, trGPMT_cyclic q hq _ v]
  rw [mulNF_eq_sum_single_right (q - q⁻¹) v u]
  simp only [trGPMT_add, trGPMT_smul, Fin.sum_univ_six]

/-- The `q`-antisymmetriser vector `v_j = (-q⁻¹)^{len(b_j)}` spanning `ker(gramD q)`. -/
def radicalVec (q : K) : Fin 6 → K :=
  ![1, -q⁻¹, -q⁻¹, q⁻¹ ^ 2, q⁻¹ ^ 2, -q⁻¹ ^ 3]

/-- The `q`-symmetriser vector `v_j = q^{len(b_j)}` projecting onto the `(3)` sector. -/
def symVec (q : K) : Fin 6 → K :=
  ![1, q, q, q ^ 2, q ^ 2, q ^ 3]

theorem chi3_radicalVec_eq_zero (q : K) (hq : q ≠ 0) :
    chi3 q (radicalVec q) = 0 := by
  unfold chi3 chiNF radicalVec
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp; ring

theorem blockOf_radicalVec_eq_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    blockOf q (radicalVec q) = 0 := by
  ext r s
  fin_cases r <;> fin_cases s <;>
    (simp [blockOf, radicalVec, S0, S1]; field_simp; ring)

theorem chi111_radicalVec_eq (q : K) (hq : q ≠ 0) :
    chi111 q (radicalVec q) = (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / q ^ 6 := by
  unfold chi111 chiNF radicalVec
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp; ring

theorem chi111_symVec_eq_zero (q : K) (hq : q ≠ 0) :
    chi111 q (symVec q) = 0 := by
  unfold chi111 chiNF symVec
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp; ring

theorem blockOf_symVec_eq_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    blockOf q (symVec q) = 0 := by
  ext r s
  fin_cases r <;> fin_cases s <;>
    (simp [blockOf, symVec, S0, S1]; field_simp; ring)

theorem chi3_symVec_eq (q : K) :
    chi3 q (symVec q) = (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) := by
  unfold chi3 chiNF symVec
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  ring

/-- Convention-D singularity (`qou-fadg`, `qou-egqr`): `radicalVec q` lies in the right kernel
of `gramD q`. -/
theorem gramD_mul_radicalVec_eq_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (i : Fin 6) :
    (∑ j : Fin 6, gramD q i j * radicalVec q j) = 0 := by
  have hlin : (∑ j : Fin 6, gramD q i j * radicalVec q j) =
      trM (zD q) (q - q⁻¹) (mulNF (q - q⁻¹) (Pi.single i 1) (radicalVec q)) := by
    rw [mulNF_eq_sum_single_right (q - q⁻¹) (Pi.single i 1) (radicalVec q)]
    simp only [trM_add, trM_smul, Fin.sum_univ_six, gramD]
    ring
  rw [hlin, trM_conventionD_eq_twoRow_sum q hq hq2 hq4]
  have hq_root : q * q = (q - q⁻¹) * q + 1 := by field_simp; ring
  have hc3 : chi3 q (mulNF (q - q⁻¹) (Pi.single i 1) (radicalVec q)) = 0 := by
    unfold chi3
    rw [chiNF_mulNF (q - q⁻¹) q hq_root, show chiNF q (radicalVec q) = chi3 q (radicalVec q) from rfl,
      chi3_radicalVec_eq_zero q hq, mul_zero]
  have hc21 : chi21 q (mulNF (q - q⁻¹) (Pi.single i 1) (radicalVec q)) = 0 := by
    unfold chi21 chiM
    rw [blockOf_mulNF q hq hq2, blockOf_radicalVec_eq_zero q hq hq2, mul_zero, Matrix.trace_zero]
  rw [hc3, hc21, mul_zero, mul_zero, add_zero]

/-- Two-flavour weight-space obstruction (`qou-ndsa`): because `(2,1)` has at most two Young rows,
`qedCostProton q` is orthogonal to `radicalVec q`, so on the uncompleted rank-5 `gramD` any
dual-feasible solution still has `y₀ = 0` forced by `y_0_eq_zero_of_cost_perp_radical`. -/
theorem qedCostProton_perp_radicalVec (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    (∑ j : Fin 6, qedCostProton q j * radicalVec q j) = 0 := by
  rw [Fin.sum_univ_six, qedCostProton_zero, qedCostProton_one q hq h3,
      qedCostProton_two q hq h3, qedCostProton_three q hq h3,
      qedCostProton_four q hq h3, qedCostProton_five q hq h3]
  have h9 : (9 : K) = 3 * 3 := by ring
  simp only [radicalVec, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  rw [h9]; field_simp; ring

/-- Under GPMT completion, `radicalVec q` is lifted out of the kernel to become an exact
eigenvector of `gramGPMT q` with eigenvalue `q⁻³ ≠ 0`. -/
theorem gramGPMT_mul_radicalVec_eq_eigenvalue (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (i : Fin 6) :
    (∑ j : Fin 6, gramGPMT q i j * radicalVec q j) = q⁻¹ ^ 3 * radicalVec q i := by
  have hq4' : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    intro h; apply hq4; linear_combination h
  have hsplit : ∀ j : Fin 6,
      gramGPMT q i j * radicalVec q j =
        gramD q i j * radicalVec q j +
          dMod111Abs q *
            chi111 q (mulNF (q - q⁻¹) (Pi.single i 1) (Pi.single j 1)) * radicalVec q j := by
    intro j
    unfold gramGPMT trGPMT gramD
    ring
  simp_rw [hsplit]
  rw [Finset.sum_add_distrib, gramD_mul_radicalVec_eq_zero q hq hq2 hq4 i, zero_add]
  have hl : (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by field_simp; ring
  have hchi : ∀ j : Fin 6,
      dMod111Abs q * chi111 q (mulNF (q - q⁻¹) (Pi.single i 1) (Pi.single j 1)) * radicalVec q j =
        dMod111Abs q * chi111 q (Pi.single i 1) * (chi111 q (Pi.single j 1) * radicalVec q j) := by
    intro j
    unfold chi111
    rw [chiNF_mulNF (q - q⁻¹) (-q⁻¹) hl]
    ring
  simp_rw [hchi, ← Finset.mul_sum]
  have hsum : (∑ j : Fin 6, chi111 q (Pi.single j 1) * radicalVec q j) =
      chi111 q (radicalVec q) := by
    unfold chi111 chiNF
    simp [Fin.sum_univ_six, radicalVec]
    ring
  rw [hsum, dMod111Abs_eq, chi111_radicalVec_eq q hq]
  have hrad_i : chi111 q (Pi.single i 1) = radicalVec q i := by
    fin_cases i
    · simp [chi111, chiNF, radicalVec]
    · simp [chi111, chiNF, radicalVec]
    · simp [chi111, chiNF, radicalVec]
    · simp [chi111, chiNF, radicalVec]
    · simp [chi111, chiNF, radicalVec]
    · simp [chi111, chiNF, radicalVec]; ring
  rw [hrad_i]
  field_simp

/-- **`γγ` Pair-Production Vertex Splits `L₊` and `L₋` under `trGPMT` (`qou-ales` & `qou-ndsa`)**:
Let `vtxNF q = ![0, -(q - q⁻¹), 0, 0, 1, 0]` represent `V = σ₀ σ₁⁻¹ = σ₀ (σ₁ - h)` in `mulNF`
coordinates (`b₄ = σ₀σ₁ = L₊`, `b₃ = σ₁σ₀ = L₋`). Seeding `trGPMT` with `V` splits `L₊` from
`L₋` by `-(q⁴ + q² + 1) / (q² + 1)²`, which is non-zero even at `q = 1` (`-3/4`). -/
def vtxNF (q : K) : Fin 6 → K :=
  ![0, -(q - q⁻¹), 0, 0, 1, 0]

theorem trGPMT_vtx_splits_hopf_links (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    trGPMT q (mulNF (q - q⁻¹) (vtxNF q) (Pi.single 4 1)) -
      trGPMT q (mulNF (q - q⁻¹) (vtxNF q) (Pi.single 3 1)) =
        -(q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hq4' : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    intro h; apply hq4; linear_combination h
  have hm4_step : mulNF (q - q⁻¹) (vtxNF q) (Pi.single 4 1) =
      mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (vtxNF q)) := by
    funext k
    simp [mulNF]
  have hm3_step : mulNF (q - q⁻¹) (vtxNF q) (Pi.single 3 1) =
      mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (vtxNF q)) := by
    funext k
    simp [mulNF]
  rw [hm4_step, hm3_step]
  unfold trGPMT trM TRM zD dMod111Abs dMod111 chi111 chiNF mulσ₀ mulσ₁ vtxNF
  simp only [Fin.sum_univ_six, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp
  ring

/-- **Explicit Wedderburn Reconstruction / Injectivity on `H₃(q)` (`1 + 4 + 1 = 6`)**:
Over any field `K` with `q ≠ 0`, `q² + 1 ≠ 0`, and `q⁴ + q² + 1 ≠ 0`, the Wedderburn map
`v ↦ (chi3 q v, blockOf q v, chi111 q v)` into `K × M₂(K) × K` has trivial kernel. -/
theorem wedderburn_triple_injective (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (v : Fin 6 → K)
    (h3 : chi3 q v = 0) (h21 : blockOf q v = 0) (h111 : chi111 q v = 0) :
    v = 0 := by
  have hm00 : blockOf q v 0 0 = 0 := by rw [h21]; rfl
  have hm01 : blockOf q v 0 1 = 0 := by rw [h21]; rfl
  have hm10 : blockOf q v 1 0 = 0 := by rw [h21]; rfl
  have hm11 : blockOf q v 1 1 = 0 := by rw [h21]; rfl
  simp only [chi3, chi111, chiNF] at h3 h111
  simp only [blockOf, S0, S1, Matrix.add_apply, Matrix.smul_apply, Matrix.mul_apply,
    Fin.sum_univ_two, Matrix.one_apply, Matrix.of_apply, Matrix.cons_val_zero,
    Matrix.cons_val_one, smul_eq_mul, Fin.isValue, Fin.reduceEq, ↓reduceIte] at hm00 hm01 hm10 hm11
  have eq3 : q ^ 3 * (v 0 + q * (v 1 + v 2) + q ^ 2 * (v 3 + v 4) + q ^ 3 * v 5) = 0 := by
    rw [h3, mul_zero]
  have eq111 : q ^ 3 * (v 0 + (-q⁻¹) * (v 1 + v 2) + (-q⁻¹) ^ 2 * (v 3 + v 4) + (-q⁻¹) ^ 3 * v 5) = 0 := by
    rw [h111, mul_zero]
  have eq111' : q ^ 3 * v 0 - q ^ 2 * (v 1 + v 2) + q * (v 3 + v 4) - v 5 = 0 := by
    calc q ^ 3 * v 0 - q ^ 2 * (v 1 + v 2) + q * (v 3 + v 4) - v 5
      _ = q ^ 3 * (v 0 + (-q⁻¹) * (v 1 + v 2) + (-q⁻¹) ^ 2 * (v 3 + v 4) + (-q⁻¹) ^ 3 * v 5) := by
          field_simp; ring
      _ = 0 := eq111
  have eq00 : q * (q ^ 2 + 1) * v 0 + q ^ 2 * (q ^ 2 + 1) * v 1 - v 2 - q * v 3 - q * v 4 - q ^ 2 * v 5 = 0 := by
    have htmp := congrArg (fun x => q * (q ^ 2 + 1) * x) hm00
    simp only [mul_zero] at htmp
    rw [← htmp]; field_simp; ring
  have eq01_raw : q * v 2 - v 3 + q ^ 2 * v 4 - q * v 5 = 0 := by
    have htmp := congrArg (fun x => q * x) hm01
    simp only [mul_zero] at htmp
    rw [← htmp]; field_simp; ring
  have eq10 : (q ^ 4 + q ^ 2 + 1) * (q * v 2 + q ^ 2 * v 3 - v 4 - q * v 5) = 0 := by
    have htmp := congrArg (fun x => q * (q ^ 2 + 1) ^ 2 * x) hm10
    simp only [mul_zero] at htmp
    rw [← htmp]; field_simp; ring
  have eq10' : q * v 2 + q ^ 2 * v 3 - v 4 - q * v 5 = 0 :=
    (mul_eq_zero.mp eq10).resolve_left hq4
  have eq11 : q * (q ^ 2 + 1) * v 0 - (q ^ 2 + 1) * v 1 + q ^ 4 * v 2 - q ^ 3 * v 3 -
      q ^ 3 * v 4 + q ^ 2 * v 5 = 0 := by
    have htmp := congrArg (fun x => q * (q ^ 2 + 1) * x) hm11
    simp only [mul_zero] at htmp
    rw [← htmp]; field_simp; ring
  have hD : (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) ≠ 0 :=
    mul_ne_zero (pow_ne_zero 2 hq2) hq4
  have hqD : q ^ 3 * ((q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) ≠ 0 :=
    mul_ne_zero (pow_ne_zero 3 hq) hD
  funext k
  fin_cases k
  · change v 0 = 0
    apply mul_left_cancel₀ hqD
    rw [mul_zero]
    linear_combination
      (q ^ 2 + 1) * eq3 + q ^ 6 * (q ^ 2 + 1) * eq111' +
      q ^ 4 * (q ^ 2 + 1) * eq00 + q ^ 4 * (q ^ 2 + 1) * eq11
  · change v 1 = 0
    apply mul_left_cancel₀ hqD
    rw [mul_zero]
    linear_combination
      q * (q ^ 2 + 1) * eq3 - q ^ 5 * (q ^ 2 + 1) * eq111' +
      q ^ 5 * (q ^ 2 + 1) * eq00 - q ^ 3 * (q ^ 2 + 1) * eq11
  · change v 2 = 0
    apply mul_left_cancel₀ hqD
    rw [mul_zero]
    linear_combination
      q * (q ^ 2 + 1) * eq3 - q ^ 5 * (q ^ 2 + 1) * eq111' -
      q ^ 3 * eq00 + q ^ 4 * (q ^ 4 + q ^ 2 + 1) * eq01_raw +
      q ^ 4 * (q ^ 4 + q ^ 2 + 1) * eq10' + q ^ 7 * eq11
  · change v 3 = 0
    apply mul_left_cancel₀ hqD
    rw [mul_zero]
    linear_combination
      q ^ 2 * (q ^ 2 + 1) * eq3 + q ^ 4 * (q ^ 2 + 1) * eq111' -
      q ^ 4 * eq00 - q ^ 3 * (q ^ 4 + q ^ 2 + 1) * eq01_raw +
      q ^ 5 * (q ^ 4 + q ^ 2 + 1) * eq10' - q ^ 6 * eq11
  · change v 4 = 0
    apply mul_left_cancel₀ hqD
    rw [mul_zero]
    linear_combination
      q ^ 2 * (q ^ 2 + 1) * eq3 + q ^ 4 * (q ^ 2 + 1) * eq111' -
      q ^ 4 * eq00 + q ^ 5 * (q ^ 4 + q ^ 2 + 1) * eq01_raw -
      q ^ 3 * (q ^ 4 + q ^ 2 + 1) * eq10' - q ^ 6 * eq11
  · change v 5 = 0
    apply mul_left_cancel₀ hqD
    rw [mul_zero]
    linear_combination
      q ^ 3 * (q ^ 2 + 1) * eq3 - q ^ 3 * (q ^ 2 + 1) * eq111' -
      q ^ 5 * eq00 - q ^ 4 * (q ^ 4 + q ^ 2 + 1) * eq01_raw -
      q ^ 4 * (q ^ 4 + q ^ 2 + 1) * eq10' + q ^ 5 * eq11

/-- Trace-pairing non-degeneracy on the `2 × 2` Hoefsmit block `M₂(K)`: if `M` has zero trace
against `1`, `S₀ q`, `S₁ q`, and `S₀ q * S₁ q`, then `M = 0`. -/
theorem hoefsmit_M2_trace_pairing_nondegenerate (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (M : Matrix (Fin 2) (Fin 2) K)
    (t0 : (1 * M).trace = 0)
    (t1 : (S0 q * M).trace = 0)
    (t2 : (S1 q * M).trace = 0)
    (t4 : (S0 q * S1 q * M).trace = 0) :
    M = 0 := by
  simp only [Matrix.one_mul, Matrix.trace_fin_two, S0, S1, Matrix.mul_apply,
    Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one] at t0 t1 t2 t4
  have e1' : q ^ 2 * M 0 0 - M 1 1 = 0 := by
    have htmp := congrArg (fun x => q * x) t1
    simp only [mul_zero] at htmp
    rw [← htmp]; field_simp; ring
  have hm00 : M 0 0 = 0 := by
    apply mul_left_cancel₀ hq2
    rw [mul_zero]
    linear_combination t0 + e1'
  have hm11 : M 1 1 = 0 := by
    linear_combination t0 - hm00
  have e2' : -(q ^ 2 + 1) * M 0 0 + q * (q ^ 2 + 1) ^ 2 * M 1 0 +
      q * (q ^ 4 + q ^ 2 + 1) * M 0 1 + q ^ 4 * (q ^ 2 + 1) * M 1 1 = 0 := by
    have htmp := congrArg (fun x => q * (q ^ 2 + 1) ^ 2 * x) t2
    simp only [mul_zero] at htmp
    rw [← htmp]; field_simp; ring
  have e4 : -q * (q ^ 2 + 1) * M 0 0 + q ^ 2 * (q ^ 2 + 1) ^ 2 * M 1 0 -
      (q ^ 4 + q ^ 2 + 1) * M 0 1 - q ^ 3 * (q ^ 2 + 1) * M 1 1 = 0 := by
    have htmp := congrArg (fun x => q * (q ^ 2 + 1) ^ 2 * x) t4
    simp only [mul_zero] at htmp
    rw [← htmp]; field_simp; ring
  rw [hm00, hm11] at e2' e4
  have hm01 : M 0 1 = 0 := by
    apply mul_left_cancel₀ (mul_ne_zero hq2 hq4)
    rw [mul_zero]
    linear_combination q * e2' - e4
  have hm10 : M 1 0 = 0 := by
    apply mul_left_cancel₀ (mul_ne_zero hq (pow_ne_zero 2 hq2))
    rw [mul_zero]
    linear_combination e2' - q * (q ^ 4 + q ^ 2 + 1) * hm01
  ext r s
  fin_cases r <;> fin_cases s
  · exact hm00
  · exact hm01
  · exact hm10
  · exact hm11

/-- **Full-Rank Non-Degeneracy of `gramGPMT` (`qou-fadg` & `qou-egqr` Resolved)**:
Over any field `K` with `q ≠ 0`, `q² + 1 ≠ 0`, `q⁴ + 1 ≠ 0`, and `q⁴ + q² + 1 ≠ 0`,
the `6 × 6` GPMT-completed Gram matrix `gramGPMT q` has trivial kernel. -/
theorem gramGPMT_kernel_trivial (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0)
    (u : Fin 6 → K) (hu : ∀ i : Fin 6, (∑ j : Fin 6, gramGPMT q i j * u j) = 0) :
    u = 0 := by
  have hpair : ∀ v : Fin 6 → K, trGPMT q (mulNF (q - q⁻¹) v u) = 0 := by
    intro v
    rw [← gramGPMT_bilinear_eq_trGPMT q hq v u]
    simp [hu]
  have hw3_ne : w3 q (zD q) ≠ 0 := by
    rw [w3_conventionD q hq2 hq4]
    exact div_ne_zero hq41 (pow_ne_zero 2 hq2)
  have hw21_ne : w21 q (zD q) ≠ 0 := by
    rw [w21_conventionD q hq2 hq4]
    exact div_ne_zero (pow_ne_zero 2 hq) (pow_ne_zero 2 hq2)
  have hd_ne : dMod111Abs q ≠ 0 := by
    rw [dMod111Abs_eq]
    exact div_ne_zero (pow_ne_zero 3 hq) (mul_ne_zero hq2 hq4)
  have hq_root : q * q = (q - q⁻¹) * q + 1 := by field_simp; ring
  have hl_root : (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by field_simp; ring
  -- 1. Project along `symVec q` to show `chi3 q u = 0`:
  have h3_u : chi3 q u = 0 := by
    have hs := hpair (symVec q)
    rw [trGPMT_eq_wedderburn_sum q hq hq2 hq4] at hs
    have hc21_s : chi21 q (mulNF (q - q⁻¹) (symVec q) u) = 0 := by
      unfold chi21 chiM
      rw [blockOf_mulNF q hq hq2, blockOf_symVec_eq_zero q hq hq2, zero_mul, Matrix.trace_zero]
    have hc111_s : chi111 q (mulNF (q - q⁻¹) (symVec q) u) = 0 := by
      unfold chi111
      rw [chiNF_mulNF (q - q⁻¹) (-q⁻¹) hl_root,
          show chiNF (-q⁻¹) (symVec q) = chi111 q (symVec q) from rfl,
          chi111_symVec_eq_zero q hq, zero_mul]
    have hc3_s : chi3 q (mulNF (q - q⁻¹) (symVec q) u) =
        ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) * chi3 q u := by
      unfold chi3
      rw [chiNF_mulNF (q - q⁻¹) q hq_root,
          show chiNF q (symVec q) = chi3 q (symVec q) from rfl,
          chi3_symVec_eq q]
    rw [hc3_s, hc21_s, hc111_s, mul_zero, mul_zero, add_zero, add_zero] at hs
    have hs' : (w3 q (zD q) * ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))) * chi3 q u = 0 := by
      linear_combination hs
    exact (mul_eq_zero.mp hs').resolve_left (mul_ne_zero hw3_ne (mul_ne_zero hq2 hq4))
  -- 2. Project along `radicalVec q` to show `chi111 q u = 0`:
  have h111_u : chi111 q u = 0 := by
    have hr := hpair (radicalVec q)
    rw [trGPMT_eq_wedderburn_sum q hq hq2 hq4] at hr
    have hc3_r : chi3 q (mulNF (q - q⁻¹) (radicalVec q) u) = 0 := by
      unfold chi3
      rw [chiNF_mulNF (q - q⁻¹) q hq_root,
          show chiNF q (radicalVec q) = chi3 q (radicalVec q) from rfl,
          chi3_radicalVec_eq_zero q hq, zero_mul]
    have hc21_r : chi21 q (mulNF (q - q⁻¹) (radicalVec q) u) = 0 := by
      unfold chi21 chiM
      rw [blockOf_mulNF q hq hq2, blockOf_radicalVec_eq_zero q hq hq2, zero_mul, Matrix.trace_zero]
    have hc111_r : chi111 q (mulNF (q - q⁻¹) (radicalVec q) u) =
        ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / q ^ 6) * chi111 q u := by
      unfold chi111
      rw [chiNF_mulNF (q - q⁻¹) (-q⁻¹) hl_root,
          show chiNF (-q⁻¹) (radicalVec q) = chi111 q (radicalVec q) from rfl,
          chi111_radicalVec_eq q hq]
    rw [hc3_r, hc21_r, hc111_r, mul_zero, mul_zero, zero_add, zero_add] at hr
    have hrad_ne : (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / q ^ 6 ≠ 0 :=
      div_ne_zero (mul_ne_zero hq2 hq4) (pow_ne_zero 6 hq)
    have hr' : (dMod111Abs q * ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / q ^ 6)) * chi111 q u = 0 := by
      linear_combination hr
    exact (mul_eq_zero.mp hr').resolve_left (mul_ne_zero hd_ne hrad_ne)
  -- 3. Every test vector `v` now gives `trace (blockOf q v * blockOf q u) = 0`:
  have h21_pair : ∀ v : Fin 6 → K, (blockOf q v * blockOf q u).trace = 0 := by
    intro v
    have hv := hpair v
    rw [trGPMT_eq_wedderburn_sum q hq hq2 hq4] at hv
    have hc3_v : chi3 q (mulNF (q - q⁻¹) v u) = 0 := by
      unfold chi3
      rw [chiNF_mulNF (q - q⁻¹) q hq_root, show chiNF q u = chi3 q u from rfl, h3_u, mul_zero]
    have hc111_v : chi111 q (mulNF (q - q⁻¹) v u) = 0 := by
      unfold chi111
      rw [chiNF_mulNF (q - q⁻¹) (-q⁻¹) hl_root, show chiNF (-q⁻¹) u = chi111 q u from rfl,
          h111_u, mul_zero]
    rw [hc3_v, hc111_v, mul_zero, mul_zero, zero_add, add_zero] at hv
    have htr := (mul_eq_zero.mp hv).resolve_left hw21_ne
    unfold chi21 chiM at htr
    rwa [blockOf_mulNF q hq hq2] at htr
  have hb0 : blockOf q (Pi.single 0 1) = 1 := by
    ext r s; fin_cases r <;> fin_cases s <;> simp [blockOf]
  have hb1 : blockOf q (Pi.single 1 1) = S0 q := by
    ext r s; fin_cases r <;> fin_cases s <;> simp [blockOf]
  have hb2 : blockOf q (Pi.single 2 1) = S1 q := by
    ext r s; fin_cases r <;> fin_cases s <;> simp [blockOf]
  have hb4 : blockOf q (Pi.single 4 1) = S0 q * S1 q := by
    ext r s; fin_cases r <;> fin_cases s <;> simp [blockOf]
  have hblock_u : blockOf q u = 0 :=
    hoefsmit_M2_trace_pairing_nondegenerate q hq hq2 hq4 (blockOf q u)
      (by simpa [hb0] using h21_pair (Pi.single 0 1))
      (by simpa [hb1] using h21_pair (Pi.single 1 1))
      (by simpa [hb2] using h21_pair (Pi.single 2 1))
      (by simpa [hb4] using h21_pair (Pi.single 4 1))
  exact wedderburn_triple_injective q hq hq2 hq4 u h3_u hblock_u h111_u

end GPMTGramCompletion

-- ============================================================================
-- § 4. Archimedean Positivity, Invertibility of `gramGPMT`, and Closed-Form `y₀* < 0`
-- ============================================================================

section ArchimedeanConfinementResolution

/-- Over `ℝ`, all three GPMT-completed Wedderburn weights `(w_{(3)}(z_D), w_{(2,1)}(z_D), |d_D(S^{(1³)})|)`
are strictly positive for every `q > 0`. -/
theorem gpmt_wedderburn_weights_pos (q : ℝ) (hq : 0 < q) :
    0 < w3 q (zD q) ∧ 0 < w21 q (zD q) ∧ 0 < dMod111Abs q := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  rw [w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4, dMod111Abs_eq]
  refine ⟨by positivity, by positivity, by positivity⟩

/-- Over `ℝ`, any square matrix `M` with trivial right kernel has `M.det ≠ 0` and admits a
unique solution `x` to `M.mulVec x = nf` for every right-hand side `nf`. -/
theorem unique_mulVec_of_trivial_kernel {n : Type*} [Fintype n] [DecidableEq n]
    (M : Matrix n n ℝ) (hker : ∀ u : n → ℝ, M.mulVec u = 0 → u = 0) :
    M.det ≠ 0 ∧ ∀ nf : n → ℝ, ∃! x : n → ℝ, M.mulVec x = nf := by
  have hdet : M.det ≠ 0 := by
    intro hzero
    obtain ⟨u, hu_ne, hu0⟩ := Matrix.exists_mulVec_eq_zero_iff.mpr hzero
    exact hu_ne (hker u hu0)
  have hunit : IsUnit M.det := isUnit_iff_ne_zero.mpr hdet
  have hinv : ∀ nf : n → ℝ, M.mulVec (M⁻¹.mulVec nf) = nf := by
    intro nf
    rw [Matrix.mulVec_mulVec, Matrix.mul_nonsing_inv M hunit, Matrix.one_mulVec]
  refine ⟨hdet, fun nf => ⟨M⁻¹.mulVec nf, hinv nf, ?_⟩⟩
  intro y hy
  have hdiff : M.mulVec (y - M⁻¹.mulVec nf) = 0 := by
    rw [Matrix.mulVec_sub, hy, hinv nf, sub_self]
  exact sub_eq_zero.mp (hker _ hdiff)

/-- Over `ℝ`, for every `q > 0`, the `6 × 6` GPMT-completed Gram matrix `gramGPMT q` has non-zero
determinant (`det ≠ 0`, full rank 6) and every normal-form demand equation `gramGPMT q *ᵥ x = nf`
has a unique solution `x* ∈ ℝ⁶` (`qou-fadg` & `qou-egqr`). -/
theorem gramGPMT_real_det_ne_zero_and_unique_solve (q : ℝ) (hq : 0 < q) :
    (Matrix.of (gramGPMT q)).det ≠ 0 ∧
    ∀ nf : Fin 6 → ℝ, ∃! x : Fin 6 → ℝ, (Matrix.of (gramGPMT q)).mulVec x = nf := by
  apply unique_mulVec_of_trivial_kernel (Matrix.of (gramGPMT q))
  intro u hu
  apply gramGPMT_kernel_trivial q (ne_of_gt hq) (by positivity) (by positivity) (by positivity) u
  intro i
  exact congrFun hu i

/-- Exact closed-form vector `aGPMT q = (gramGPMT q)⁻¹ 1` over `ℚ(q)`. -/
noncomputable def aGPMT (q : ℝ) : Fin 6 → ℝ :=
  let D := (q ^ 2 + 1) * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) * (q ^ 2 + q + 1)
  ![ (q ^ 15 - q ^ 14 + q ^ 13 - q ^ 12 + 4 * q ^ 11 + 5 * q ^ 9 + q ^ 8 + q ^ 7 -
        3 * q ^ 6 - 2 * q ^ 5 + q ^ 3 + 3 * q ^ 2 + q + 1) / D,
     -(q ^ 14 - q ^ 13 - 3 * q ^ 11 - 4 * q ^ 9 + 2 * q ^ 8 + q ^ 7 + 3 * q ^ 6 -
        q ^ 5 - 2 * q ^ 4 - 3 * q ^ 3 - 3 * q ^ 2 - q - 1) / D,
     -(q ^ 14 - q ^ 13 - 3 * q ^ 11 - 4 * q ^ 9 + 2 * q ^ 8 + q ^ 7 + 3 * q ^ 6 -
        q ^ 5 - 2 * q ^ 4 - 3 * q ^ 3 - 3 * q ^ 2 - q - 1) / D,
     (q ^ 13 + q ^ 11 - q ^ 10 - 5 * q ^ 8 - q ^ 7 - q ^ 6 + 4 * q ^ 5 + 3 * q ^ 4 +
        5 * q ^ 3 + 3 * q ^ 2 + 2 * q + 1) / D,
     (q ^ 13 + q ^ 11 - q ^ 10 - 5 * q ^ 8 - q ^ 7 - q ^ 6 + 4 * q ^ 5 + 3 * q ^ 4 +
        5 * q ^ 3 + 3 * q ^ 2 + 2 * q + 1) / D,
     -q * (q ^ 11 + q ^ 10 + 3 * q ^ 9 + 3 * q ^ 8 + 4 * q ^ 7 - 2 * q ^ 6 - 2 * q ^ 5 -
        6 * q ^ 4 - 4 * q ^ 3 - 6 * q ^ 2 - 2 * q - 2) / D ]

/-- Exact closed-form vector `betaQAdjp q = (gramGPMT q)⁻¹ (qedCostProton q)` over `ℚ(q)`. -/
noncomputable def betaQAdjp (q : ℝ) : Fin 6 → ℝ :=
  let D := 9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)
  ![ -2 * q ^ 2 * (q ^ 2 - 1) ^ 2 * (q ^ 2 + 1) / D,
     2 * (q ^ 2 + 1) * (q ^ 8 + 3 * q ^ 6 + q ^ 2 - 1) / (q * D),
     -2 * (q ^ 2 + 1) * (2 * q ^ 8 - 3 * q ^ 6 - q ^ 2 - 2) / (q * D),
     2 * (q ^ 2 - 1) * (q ^ 2 + 1) * (2 * q ^ 4 + q ^ 2 + 1) / D,
     2 * (q ^ 2 - 1) * (q ^ 2 + 1) * (2 * q ^ 4 + q ^ 2 + 1) / D,
     -2 * q * (q ^ 2 + 1) * (3 * q ^ 4 + 2 * q ^ 2 + 3) / D ]

/-- Explicit `2 × 2` matrix entries of `blockOf q v` for any normal-form vector `v`. -/
theorem blockOf_entries (q : ℝ) (hq : q ≠ 0) (v : Fin 6 → ℝ) :
    blockOf q v 0 0 = v 0 + q * v 1 - v 2 / (q * (q ^ 2 + 1)) -
        v 3 / (q ^ 2 + 1) - v 4 / (q ^ 2 + 1) - q * v 5 / (q ^ 2 + 1) ∧
    blockOf q v 0 1 = v 2 - q⁻¹ * v 3 + q * v 4 - v 5 ∧
    blockOf q v 1 0 = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 *
        (v 2 + q * v 3 - q⁻¹ * v 4 - v 5) ∧
    blockOf q v 1 1 = v 0 - q⁻¹ * v 1 + q ^ 3 / (q ^ 2 + 1) * v 2 -
        q ^ 2 / (q ^ 2 + 1) * v 3 - q ^ 2 / (q ^ 2 + 1) * v 4 + q / (q ^ 2 + 1) * v 5 := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    (simp only [blockOf, S0, S1, Matrix.add_apply, Matrix.smul_apply, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.one_apply, Matrix.of_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one, smul_eq_mul, Fin.isValue, Fin.reduceEq, ↓reduceIte];
     field_simp; ring)

/-- Explicit trace formulas `(blockOf q (Pi.single i 1) * M).trace` for any `2 × 2` matrix `M`. -/
theorem trace_blockOf_single_mul (q : ℝ) (hq : q ≠ 0) (M : Matrix (Fin 2) (Fin 2) ℝ) :
    (blockOf q (Pi.single 0 1) * M).trace = M 0 0 + M 1 1 ∧
    (blockOf q (Pi.single 1 1) * M).trace = q * M 0 0 - q⁻¹ * M 1 1 ∧
    (blockOf q (Pi.single 2 1) * M).trace =
      -(1 / (q * (q ^ 2 + 1))) * M 0 0 + M 1 0 +
        (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 * M 0 1 + q ^ 3 / (q ^ 2 + 1) * M 1 1 ∧
    (blockOf q (Pi.single 3 1) * M).trace =
      -(1 / (q ^ 2 + 1)) * M 0 0 - q⁻¹ * M 1 0 +
        q * (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 * M 0 1 - q ^ 2 / (q ^ 2 + 1) * M 1 1 ∧
    (blockOf q (Pi.single 4 1) * M).trace =
      -(1 / (q ^ 2 + 1)) * M 0 0 + q * M 1 0 -
        (q ^ 4 + q ^ 2 + 1) / (q * (q ^ 2 + 1) ^ 2) * M 0 1 - q ^ 2 / (q ^ 2 + 1) * M 1 1 ∧
    (blockOf q (Pi.single 5 1) * M).trace =
      -(q / (q ^ 2 + 1)) * M 0 0 - M 1 0 -
        (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 * M 0 1 + q / (q ^ 2 + 1) * M 1 1 := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (simp only [blockOf, S0, S1, Pi.single_apply, Matrix.trace_fin_two, Matrix.add_apply,
      Matrix.smul_apply, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val_one, smul_eq_mul, Fin.isValue, Fin.reduceEq,
      ↓reduceIte];
     field_simp; ring)

theorem chi3_aGPMT (q : ℝ) (hq : 0 < q) :
    chi3 q (aGPMT q) =
      (q + 1) * (q ^ 2 + 1) * (q ^ 2 + q + 1) / ((q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  unfold chi3 chiNF aGPMT
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp; ring

theorem chi111_aGPMT (q : ℝ) (hq : 0 < q) :
    chi111 q (aGPMT q) = (q - 1) * (q ^ 2 - q + 1) := by
  unfold chi111 chiNF aGPMT
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp; ring

theorem blockOf_aGPMT (q : ℝ) (hq : 0 < q) :
    blockOf q (aGPMT q) =
      Matrix.of
        ![![(q ^ 2 - 1) * (q ^ 2 + 1) * (q ^ 2 + q + 1) / (q * (q ^ 4 + q ^ 2 + 1)),
            (q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (q * (q ^ 4 + q ^ 2 + 1))],
          ![(q ^ 2 - 1) / q,
            (q ^ 2 - 1) * (q ^ 2 + 1) / (q * (q ^ 2 + q + 1))]] := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hent := blockOf_entries q hq0 (aGPMT q)
  ext r s
  fin_cases r <;> fin_cases s
  · change blockOf q (aGPMT q) 0 0 =
      (q ^ 2 - 1) * (q ^ 2 + 1) * (q ^ 2 + q + 1) / (q * (q ^ 4 + q ^ 2 + 1))
    rw [hent.1]
    unfold aGPMT
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
    field_simp; ring
  · change blockOf q (aGPMT q) 0 1 = (q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (q * (q ^ 4 + q ^ 2 + 1))
    rw [hent.2.1]
    unfold aGPMT
    simp only [Matrix.cons_val]
    field_simp; ring
  · change blockOf q (aGPMT q) 1 0 = (q ^ 2 - 1) / q
    rw [hent.2.2.1]
    unfold aGPMT
    simp only [Matrix.cons_val]
    field_simp; ring
  · change blockOf q (aGPMT q) 1 1 = (q ^ 2 - 1) * (q ^ 2 + 1) / (q * (q ^ 2 + q + 1))
    rw [hent.2.2.2]
    unfold aGPMT
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
    field_simp; ring

theorem chi3_betaQAdjp (q : ℝ) (hq : 0 < q) :
    chi3 q (betaQAdjp q) =
      2 * (q ^ 2 - 1) ^ 2 * (q ^ 2 + 1) ^ 2 / (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq41 : q ^ 4 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have hq4' : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by positivity
  unfold chi3 chiNF betaQAdjp
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp; ring

theorem chi111_betaQAdjp (q : ℝ) (hq : 0 < q) :
    chi111 q (betaQAdjp q) = 0 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq41 : q ^ 4 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have hq4' : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by positivity
  unfold chi111 chiNF betaQAdjp
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp; ring

theorem blockOf_betaQAdjp (q : ℝ) (hq : 0 < q) :
    blockOf q (betaQAdjp q) =
      Matrix.of
        ![![2 * (q ^ 2 + 1) * (q ^ 6 + 2 * q ^ 4 + 2 * q ^ 2 - 2) /
              (9 * q ^ 2 * (q ^ 4 + q ^ 2 + 1)),
            2 * (q ^ 2 + 1) ^ 2 / (3 * q * (q ^ 4 + q ^ 2 + 1))],
          ![2 / (3 * q),
            -2 * (q ^ 2 + 1) * (2 * q ^ 2 - 1) / (9 * q ^ 2)]] := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq41 : q ^ 4 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have hq4' : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by positivity
  have hent := blockOf_entries q hq0 (betaQAdjp q)
  ext r s
  fin_cases r <;> fin_cases s
  · change blockOf q (betaQAdjp q) 0 0 =
      2 * (q ^ 2 + 1) * (q ^ 6 + 2 * q ^ 4 + 2 * q ^ 2 - 2) / (9 * q ^ 2 * (q ^ 4 + q ^ 2 + 1))
    rw [hent.1]
    unfold betaQAdjp
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
    field_simp; ring
  · change blockOf q (betaQAdjp q) 0 1 =
      2 * (q ^ 2 + 1) ^ 2 / (3 * q * (q ^ 4 + q ^ 2 + 1))
    rw [hent.2.1]
    unfold betaQAdjp
    simp only [Matrix.cons_val]
    field_simp; ring
  · change blockOf q (betaQAdjp q) 1 0 = 2 / (3 * q)
    rw [hent.2.2.1]
    unfold betaQAdjp
    simp only [Matrix.cons_val]
    field_simp; ring
  · change blockOf q (betaQAdjp q) 1 1 = -2 * (q ^ 2 + 1) * (2 * q ^ 2 - 1) / (9 * q ^ 2)
    rw [hent.2.2.2]
    unfold betaQAdjp
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
    field_simp; ring

/-- Verification that `gramGPMT q *ᵥ aGPMT q = 1` for every `q > 0`. -/
theorem gramGPMT_mul_aGPMT_eq_one (q : ℝ) (hq : 0 < q) (i : Fin 6) :
    (∑ j : Fin 6, gramGPMT q i j * aGPMT q j) = 1 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have htr := trace_blockOf_single_mul q hq0 (blockOf q (aGPMT q))
  rw [gramGPMT_mulVec_wedderburn q hq0 hq2 hq4 (aGPMT q) i,
      w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4, dMod111Abs_eq,
      chi3_aGPMT q hq, chi111_aGPMT q hq]
  fin_cases i
  · change _ + _ * (blockOf q (Pi.single 0 1) * blockOf q (aGPMT q)).trace + _ = 1
    rw [htr.1, blockOf_aGPMT q hq]
    simp [chi3, chi111, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 1 1) * blockOf q (aGPMT q)).trace + _ = 1
    rw [htr.2.1, blockOf_aGPMT q hq]
    simp [chi3, chi111, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 2 1) * blockOf q (aGPMT q)).trace + _ = 1
    rw [htr.2.2.1, blockOf_aGPMT q hq]
    simp [chi3, chi111, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 3 1) * blockOf q (aGPMT q)).trace + _ = 1
    rw [htr.2.2.2.1, blockOf_aGPMT q hq]
    simp [chi3, chi111, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 4 1) * blockOf q (aGPMT q)).trace + _ = 1
    rw [htr.2.2.2.2.1, blockOf_aGPMT q hq]
    simp [chi3, chi111, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 5 1) * blockOf q (aGPMT q)).trace + _ = 1
    rw [htr.2.2.2.2.2, blockOf_aGPMT q hq]
    simp [chi3, chi111, chiNF]; field_simp; ring

/-- Verification that `gramGPMT q *ᵥ betaQAdjp q = qedCostProton q` for every `q > 0`. -/
theorem gramGPMT_mul_betaQAdjp_eq_qedCostProton (q : ℝ) (hq : 0 < q) (i : Fin 6) :
    (∑ j : Fin 6, gramGPMT q i j * betaQAdjp q j) = qedCostProton q i := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have h3 : (3 : ℝ) ≠ 0 := by norm_num
  have htr := trace_blockOf_single_mul q hq0 (blockOf q (betaQAdjp q))
  rw [gramGPMT_mulVec_wedderburn q hq0 hq2 hq4 (betaQAdjp q) i,
      w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4,
      chi3_betaQAdjp q hq, chi111_betaQAdjp q hq, mul_zero, add_zero]
  fin_cases i
  · change _ + _ * (blockOf q (Pi.single 0 1) * blockOf q (betaQAdjp q)).trace = qedCostProton q 0
    rw [htr.1, blockOf_betaQAdjp q hq, qedCostProton_zero]
    simp [chi3, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 1 1) * blockOf q (betaQAdjp q)).trace = qedCostProton q 1
    rw [htr.2.1, blockOf_betaQAdjp q hq, qedCostProton_one q hq0 h3]
    simp [chi3, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 2 1) * blockOf q (betaQAdjp q)).trace = qedCostProton q 2
    rw [htr.2.2.1, blockOf_betaQAdjp q hq, qedCostProton_two q hq0 h3]
    simp [chi3, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 3 1) * blockOf q (betaQAdjp q)).trace = qedCostProton q 3
    rw [htr.2.2.2.1, blockOf_betaQAdjp q hq, qedCostProton_three q hq0 h3]
    simp [chi3, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 4 1) * blockOf q (betaQAdjp q)).trace = qedCostProton q 4
    rw [htr.2.2.2.2.1, blockOf_betaQAdjp q hq, qedCostProton_four q hq0 h3]
    simp [chi3, chiNF]; field_simp; ring
  · change _ + _ * (blockOf q (Pi.single 5 1) * blockOf q (betaQAdjp q)).trace = qedCostProton q 5
    rw [htr.2.2.2.2.2, blockOf_betaQAdjp q hq, qedCostProton_five q hq0 h3]
    simp [chi3, chiNF]; field_simp; ring

/-- Strict positivity of all six simplex weights `aGPMT q i > 0` on `1 ≤ q ≤ 9/8`
(containing both substrate pins `q₀ ≈ 1.10997858` and `q_{2t} ≈ 1.10997860`). -/
theorem aGPMT_pos_on_substrate_interval (q : ℝ) (hq_lo : 1 ≤ q) (hq_hi : q ≤ 9 / 8) :
    ∀ i : Fin 6, 0 < aGPMT q i := by
  set t : ℝ := q - 1
  have ht0 : 0 ≤ t := by linarith
  have ht1 : t ≤ 1 / 8 := by linarith
  have hq_eq : q = 1 + t := by linarith
  have hD : 0 < (q ^ 2 + 1) * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) * (q ^ 2 + q + 1) := by
    positivity
  have ht7 : t ^ 7 ≤ (1 / 8 : ℝ) ^ 7 := pow_le_pow_left₀ ht0 ht1 7
  have ht8 : t ^ 8 ≤ (1 / 8 : ℝ) ^ 8 := pow_le_pow_left₀ ht0 ht1 8
  have ht9 : t ^ 9 ≤ (1 / 8 : ℝ) ^ 9 := pow_le_pow_left₀ ht0 ht1 9
  have ht10 : t ^ 10 ≤ (1 / 8 : ℝ) ^ 10 := pow_le_pow_left₀ ht0 ht1 10
  have ht11 : t ^ 11 ≤ (1 / 8 : ℝ) ^ 11 := pow_le_pow_left₀ ht0 ht1 11
  have ht12 : t ^ 12 ≤ (1 / 8 : ℝ) ^ 12 := pow_le_pow_left₀ ht0 ht1 12
  have ht13 : t ^ 13 ≤ (1 / 8 : ℝ) ^ 13 := pow_le_pow_left₀ ht0 ht1 13
  have ht14 : t ^ 14 ≤ (1 / 8 : ℝ) ^ 14 := pow_le_pow_left₀ ht0 ht1 14
  have hn0 : 0 < q ^ 15 - q ^ 14 + q ^ 13 - q ^ 12 + 4 * q ^ 11 + 5 * q ^ 9 + q ^ 8 +
      q ^ 7 - 3 * q ^ 6 - 2 * q ^ 5 + q ^ 3 + 3 * q ^ 2 + q + 1 := by
    have hexp : q ^ 15 - q ^ 14 + q ^ 13 - q ^ 12 + 4 * q ^ 11 + 5 * q ^ 9 + q ^ 8 +
        q ^ 7 - 3 * q ^ 6 - 2 * q ^ 5 + q ^ 3 + 3 * q ^ 2 + q + 1 =
        12 + 88 * t + 416 * t ^ 2 + 1249 * t ^ 3 + 2584 * t ^ 4 + 4031 * t ^ 5 +
        5094 * t ^ 6 + 5436 * t ^ 7 + 4930 * t ^ 8 + 3723 * t ^ 9 + 2266 * t ^ 10 +
        1071 * t ^ 11 + 376 * t ^ 12 + 92 * t ^ 13 + 14 * t ^ 14 + t ^ 15 := by
      rw [hq_eq]; ring
    rw [hexp]; positivity
  have hn1 : 0 < -(q ^ 14 - q ^ 13 - 3 * q ^ 11 - 4 * q ^ 9 + 2 * q ^ 8 + q ^ 7 +
      3 * q ^ 6 - q ^ 5 - 2 * q ^ 4 - 3 * q ^ 3 - 3 * q ^ 2 - q - 1) := by
    have hexp : -(q ^ 14 - q ^ 13 - 3 * q ^ 11 - 4 * q ^ 9 + 2 * q ^ 8 + q ^ 7 +
        3 * q ^ 6 - q ^ 5 - 2 * q ^ 4 - 3 * q ^ 3 - 3 * q ^ 2 - q - 1) =
        (12 + 56 * t + 208 * t ^ 2 + 567 * t ^ 3 + 995 * t ^ 4 + 1025 * t ^ 5 + 369 * t ^ 6) -
        (599 * t ^ 7 + 1187 * t ^ 8 + 1118 * t ^ 9 + 682 * t ^ 10 + 283 * t ^ 11 +
          78 * t ^ 12 + 13 * t ^ 13 + t ^ 14) := by
      rw [hq_eq]; ring
    have hlo : 12 ≤ 12 + 56 * t + 208 * t ^ 2 + 567 * t ^ 3 + 995 * t ^ 4 + 1025 * t ^ 5 + 369 * t ^ 6 := by
      have : 0 ≤ 56 * t + 208 * t ^ 2 + 567 * t ^ 3 + 995 * t ^ 4 + 1025 * t ^ 5 + 369 * t ^ 6 := by
        positivity
      linarith
    rw [hexp]; linarith
  have hn3 : 0 < q ^ 13 + q ^ 11 - q ^ 10 - 5 * q ^ 8 - q ^ 7 - q ^ 6 + 4 * q ^ 5 +
      3 * q ^ 4 + 5 * q ^ 3 + 3 * q ^ 2 + 2 * q + 1 := by
    have hexp : q ^ 13 + q ^ 11 - q ^ 10 - 5 * q ^ 8 - q ^ 7 - q ^ 6 + 4 * q ^ 5 +
        3 * q ^ 4 + 5 * q ^ 3 + 3 * q ^ 2 + 2 * q + 1 =
        12 * (1 - t ^ 2) + (16 * t + 53 * t ^ 3 + 458 * t ^ 4 + 1194 * t ^ 5 + 1820 * t ^ 6 +
        1885 * t ^ 7 + 1402 * t ^ 8 + 760 * t ^ 9 + 296 * t ^ 10 + 79 * t ^ 11 +
        13 * t ^ 12 + t ^ 13) := by
      rw [hq_eq]; ring
    have h1t2 : 0 < 1 - t ^ 2 := by nlinarith
    have hrest : 0 ≤ 16 * t + 53 * t ^ 3 + 458 * t ^ 4 + 1194 * t ^ 5 + 1820 * t ^ 6 +
        1885 * t ^ 7 + 1402 * t ^ 8 + 760 * t ^ 9 + 296 * t ^ 10 + 79 * t ^ 11 +
        13 * t ^ 12 + t ^ 13 := by positivity
    rw [hexp]; linarith
  have hn5 : 0 < -q * (q ^ 11 + q ^ 10 + 3 * q ^ 9 + 3 * q ^ 8 + 4 * q ^ 7 - 2 * q ^ 6 -
      2 * q ^ 5 - 6 * q ^ 4 - 4 * q ^ 3 - 6 * q ^ 2 - 2 * q - 2) := by
    have ht2 : t ^ 2 ≤ (1 / 8 : ℝ) ^ 2 := pow_le_pow_left₀ ht0 ht1 2
    have ht3 : t ^ 3 ≤ (1 / 8 : ℝ) ^ 3 := pow_le_pow_left₀ ht0 ht1 3
    have ht4 : t ^ 4 ≤ (1 / 8 : ℝ) ^ 4 := pow_le_pow_left₀ ht0 ht1 4
    have ht5 : t ^ 5 ≤ (1 / 8 : ℝ) ^ 5 := pow_le_pow_left₀ ht0 ht1 5
    have ht6 : t ^ 6 ≤ (1 / 8 : ℝ) ^ 6 := pow_le_pow_left₀ ht0 ht1 6
    have hinner : 0 < -(q ^ 11 + q ^ 10 + 3 * q ^ 9 + 3 * q ^ 8 + 4 * q ^ 7 - 2 * q ^ 6 -
        2 * q ^ 5 - 6 * q ^ 4 - 4 * q ^ 3 - 6 * q ^ 2 - 2 * q - 2) := by
      have hexp : -(q ^ 11 + q ^ 10 + 3 * q ^ 9 + 3 * q ^ 8 + 4 * q ^ 7 - 2 * q ^ 6 -
          2 * q ^ 5 - 6 * q ^ 4 - 4 * q ^ 3 - 6 * q ^ 2 - 2 * q - 2) =
          12 - 28 * t - 272 * t ^ 2 - 757 * t ^ 3 - 1222 * t ^ 4 - 1330 * t ^ 5 -
          1034 * t ^ 6 - 586 * t ^ 7 - 240 * t ^ 8 - 68 * t ^ 9 - 12 * t ^ 10 - t ^ 11 := by
        rw [hq_eq]; ring
      rw [hexp]; linarith
    have hq_pos : 0 < q := by linarith
    nlinarith
  intro i
  fin_cases i
  · exact div_pos hn0 hD
  · exact div_pos hn1 hD
  · exact div_pos hn1 hD
  · exact div_pos hn3 hD
  · exact div_pos hn3 hD
  · exact div_pos hn5 hD

/-- Sign distribution of `e₀ + α • betaQAdjp q` on `1 < q ≤ 9/8` and `0 < α ≤ 1`:
coordinates `0, 1, 2, 3, 4` are strictly positive while the trefoil coordinate `5` (`e⁻`) is
strictly negative. -/
theorem twoTerm_proton_beta_signs_on_substrate_interval
    (q α : ℝ) (hq_lo : 1 < q) (hq_hi : q ≤ 9 / 8) (hα_lo : 0 < α) (hα_hi : α ≤ 1) :
    0 < 1 + α * betaQAdjp q 0 ∧
    0 < α * betaQAdjp q 1 ∧
    0 < α * betaQAdjp q 2 ∧
    0 < α * betaQAdjp q 3 ∧
    0 < α * betaQAdjp q 4 ∧
    α * betaQAdjp q 5 < 0 := by
  set t : ℝ := q - 1
  have ht0 : 0 < t := by linarith
  have ht1 : t ≤ 1 / 8 := by linarith
  have hq_eq : q = 1 + t := by linarith
  have hq_pos : 0 < q := by linarith
  have hD : 0 < 9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) := by positivity
  have hqD : 0 < q * (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by positivity
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · -- Coordinate 0: `1 + α * betaQAdjp q 0 > 0`
    simp only [betaQAdjp, Matrix.cons_val_zero]
    have hb0_abs : 2 * q ^ 2 * (q ^ 2 - 1) ^ 2 * (q ^ 2 + 1) <
        9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) := by
      have h1 : q ^ 2 ≤ (9 / 8 : ℝ) ^ 2 := by nlinarith
      have hq2_lo : 0 ≤ q ^ 2 - 1 := by nlinarith
      have hq2_hi : q ^ 2 - 1 ≤ (9 / 8 : ℝ) ^ 2 - 1 := by nlinarith
      have h2 : (q ^ 2 - 1) ^ 2 ≤ ((9 / 8 : ℝ) ^ 2 - 1) ^ 2 :=
        pow_le_pow_left₀ hq2_lo hq2_hi 2
      have h3 : q ^ 2 + 1 ≤ (9 / 8 : ℝ) ^ 2 + 1 := by nlinarith
      have h4 : 9 * (1 + 1 : ℝ) * (1 + 1 + 1) ≤ 9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) := by
        nlinarith [sq_nonneg (q ^ 2 - 1)]
      nlinarith
    have hdiv : 2 * q ^ 2 * (q ^ 2 - 1) ^ 2 * (q ^ 2 + 1) /
        (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) < 1 := (div_lt_one hD).mpr hb0_abs
    have hnonneg : 0 ≤ 2 * q ^ 2 * (q ^ 2 - 1) ^ 2 * (q ^ 2 + 1) /
        (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by positivity
    have hrewrite : -2 * q ^ 2 * (q ^ 2 - 1) ^ 2 * (q ^ 2 + 1) /
        (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) =
        -(2 * q ^ 2 * (q ^ 2 - 1) ^ 2 * (q ^ 2 + 1) /
          (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))) := by ring
    rw [hrewrite]
    nlinarith
  · -- Coordinate 1
    simp only [betaQAdjp, Matrix.cons_val_one, Matrix.cons_val_zero]
    have hb1 : 0 < 2 * (q ^ 2 + 1) * (q ^ 8 + 3 * q ^ 6 + q ^ 2 - 1) := by
      have hq8 : 1 ≤ q ^ 8 := one_le_pow₀ (le_of_lt hq_lo)
      have hq6 : 1 ≤ q ^ 6 := one_le_pow₀ (le_of_lt hq_lo)
      have hq2' : 1 ≤ q ^ 2 := one_le_pow₀ (le_of_lt hq_lo)
      nlinarith
    exact mul_pos hα_lo (div_pos hb1 hqD)
  · -- Coordinate 2
    change 0 < α * (-2 * (q ^ 2 + 1) * (2 * q ^ 8 - 3 * q ^ 6 - q ^ 2 - 2) /
      (q * (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))))
    have ht2 : t ^ 2 ≤ (1 / 8 : ℝ) ^ 2 := pow_le_pow_left₀ (le_of_lt ht0) ht1 2
    have ht3 : t ^ 3 ≤ (1 / 8 : ℝ) ^ 3 := pow_le_pow_left₀ (le_of_lt ht0) ht1 3
    have ht4 : t ^ 4 ≤ (1 / 8 : ℝ) ^ 4 := pow_le_pow_left₀ (le_of_lt ht0) ht1 4
    have ht5 : t ^ 5 ≤ (1 / 8 : ℝ) ^ 5 := pow_le_pow_left₀ (le_of_lt ht0) ht1 5
    have ht6 : t ^ 6 ≤ (1 / 8 : ℝ) ^ 6 := pow_le_pow_left₀ (le_of_lt ht0) ht1 6
    have ht7 : t ^ 7 ≤ (1 / 8 : ℝ) ^ 7 := pow_le_pow_left₀ (le_of_lt ht0) ht1 7
    have ht8 : t ^ 8 ≤ (1 / 8 : ℝ) ^ 8 := pow_le_pow_left₀ (le_of_lt ht0) ht1 8
    have hpoly : 0 < -(2 * q ^ 8 - 3 * q ^ 6 - q ^ 2 - 2) := by
      have hexp : -(2 * q ^ 8 - 3 * q ^ 6 - q ^ 2 - 2) =
          4 + 4 * t - 10 * t ^ 2 - 52 * t ^ 3 - 95 * t ^ 4 - 94 * t ^ 5 -
          53 * t ^ 6 - 16 * t ^ 7 - 2 * t ^ 8 := by
        rw [hq_eq]; ring
      rw [hexp]; linarith
    have hb2 : 0 < -2 * (q ^ 2 + 1) * (2 * q ^ 8 - 3 * q ^ 6 - q ^ 2 - 2) := by nlinarith
    exact mul_pos hα_lo (div_pos hb2 hqD)
  · -- Coordinate 3
    change 0 < α * (2 * (q ^ 2 - 1) * (q ^ 2 + 1) * (2 * q ^ 4 + q ^ 2 + 1) /
      (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)))
    have hq2m1 : 0 < q ^ 2 - 1 := by nlinarith
    have hb3 : 0 < 2 * (q ^ 2 - 1) * (q ^ 2 + 1) * (2 * q ^ 4 + q ^ 2 + 1) := by positivity
    exact mul_pos hα_lo (div_pos hb3 hD)
  · -- Coordinate 4
    change 0 < α * (2 * (q ^ 2 - 1) * (q ^ 2 + 1) * (2 * q ^ 4 + q ^ 2 + 1) /
      (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)))
    have hq2m1 : 0 < q ^ 2 - 1 := by nlinarith
    have hb4 : 0 < 2 * (q ^ 2 - 1) * (q ^ 2 + 1) * (2 * q ^ 4 + q ^ 2 + 1) := by positivity
    exact mul_pos hα_lo (div_pos hb4 hD)
  · -- Coordinate 5 (`e⁻` trefoil channel): strictly negative!
    change α * (-2 * q * (q ^ 2 + 1) * (3 * q ^ 4 + 2 * q ^ 2 + 3) /
      (9 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))) < 0
    have hb5 : -2 * q * (q ^ 2 + 1) * (3 * q ^ 4 + 2 * q ^ 2 + 3) < 0 := by nlinarith [sq_nonneg (q ^ 2)]
    exact mul_neg_of_pos_of_neg hα_lo (div_neg_of_neg_of_pos hb5 hD)

/-- Exact closed-form dual shadow price `y₀*(q, α)` of the Two-Term Photon/QED + GPMT proton
confinement LP on `1 < q ≤ 9/8`, `0 < α ≤ 1`. -/
noncomputable def y0StarProtonTwoTermGPMT (q α : ℝ) : ℝ :=
  (α * betaQAdjp q 5) / aGPMT q 5

/-- **Strict Non-Zero Dual Shadow Price & Exact Primal–Dual Certificate (`qou-augu` & `qou-ndsa` Resolved)**:
On `1 < q ≤ 9/8` (`q₀ ≈ 1.10998`, `q_{2t} ≈ 1.10998`) and `0 < α ≤ 1` (`α_EM(q₀) ≈ 1/137.036`),
the Two-Term Photon/QED + GPMT proton confinement LP (`c_j = trGPMT(b_j) + α · qedCostProton(b_j)`,
`G = gramGPMT q`) admits an exact primal–dual optimum `(x*, y₀*, s*)` with:
1. **Strictly negative (hence non-zero) shadow price**: `y₀*(q, α) < 0` (`y₀*(q, α) ≠ 0`),
2. **Valid `OperatorSelectionLpContext ℝ` strong-duality certificate**: for any `n_target ≥ 0`,
   `∑_j c_j x*_j = n_target · y₀*(q, α)` and `n_target · y₀*(q, α) ≤ ∑_j c_j x_j` for every
   feasible `x` (`∑ x = n_target`, `gramGPMT q *ᵥ x ≥ 0`). -/
theorem twoTerm_proton_gpmt_strict_negative_shadow_price
    (q α n_target : ℝ) (hq_lo : 1 < q) (hq_hi : q ≤ 9 / 8)
    (hα_lo : 0 < α) (hα_hi : α ≤ 1) (hn : 0 ≤ n_target) :
    y0StarProtonTwoTermGPMT q α < 0 ∧
    y0StarProtonTwoTermGPMT q α ≠ 0 ∧
    ∃ (x_star s_star : Fin 6 → ℝ),
      (∀ i, 0 ≤ s_star i) ∧
      (∀ j, twoTermCost 1 α (fun k => trGPMT q (Pi.single k 1)) (qedCostProton q) j =
        y0StarProtonTwoTermGPMT q α + ∑ i, s_star i * gramGPMT q i j) ∧
      (∑ j, x_star j) = n_target ∧
      (∀ i, 0 ≤ ∑ j, gramGPMT q i j * x_star j) ∧
      (∑ j, twoTermCost 1 α (fun k => trGPMT q (Pi.single k 1)) (qedCostProton q) j * x_star j) =
        n_target * y0StarProtonTwoTermGPMT q α := by
  have hq_pos : 0 < q := by linarith
  have ha := aGPMT_pos_on_substrate_interval q (le_of_lt hq_lo) hq_hi
  have hbeta := twoTerm_proton_beta_signs_on_substrate_interval q α hq_lo hq_hi hα_lo hα_hi
  have hy0_neg : y0StarProtonTwoTermGPMT q α < 0 :=
    div_neg_of_neg_of_pos hbeta.2.2.2.2.2 (ha 5)
  let betaVec : Fin 6 → ℝ :=
    fun i => (if i = 0 then (1 : ℝ) else 0) + α * betaQAdjp q i
  let s_star : Fin 6 → ℝ :=
    fun i => betaVec i - y0StarProtonTwoTermGPMT q α * aGPMT q i
  let u_star : Fin 6 → ℝ := fun i => if i = 5 then n_target / aGPMT q 5 else 0
  obtain ⟨x_star, hx_solve, _⟩ := (gramGPMT_real_det_ne_zero_and_unique_solve q hq_pos).2 u_star
  have hs5 : s_star 5 = 0 := by
    have ha5 : aGPMT q 5 ≠ 0 := ne_of_gt (ha 5)
    dsimp [s_star, betaVec, y0StarProtonTwoTermGPMT]
    field_simp
    ring
  have hdual : ∀ j, twoTermCost 1 α (fun k => trGPMT q (Pi.single k 1)) (qedCostProton q) j =
      y0StarProtonTwoTermGPMT q α + ∑ i, s_star i * gramGPMT q i j := by
    intro j
    have hsym : ∀ i, gramGPMT q i j = gramGPMT q j i :=
      fun i => gramGPMT_symm q (ne_of_gt hq_pos) i j
    have hsum : (∑ i : Fin 6, s_star i * gramGPMT q i j) =
        gramGPMT q j 0 + α * (∑ i : Fin 6, gramGPMT q j i * betaQAdjp q i) -
          y0StarProtonTwoTermGPMT q α * (∑ i : Fin 6, gramGPMT q j i * aGPMT q i) := by
      have hterm : ∀ i : Fin 6, s_star i * gramGPMT q i j =
          ((if i = 0 then gramGPMT q j i else 0) + α * (gramGPMT q j i * betaQAdjp q i)) -
            y0StarProtonTwoTermGPMT q α * (gramGPMT q j i * aGPMT q i) := by
        intro i
        dsimp [s_star, betaVec]
        rw [hsym i]
        by_cases hi : i = 0
        · simp [hi]; ring
        · simp [hi]; ring
      simp_rw [hterm]
      rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum]
      simp
    rw [hsum, gramGPMT_mul_betaQAdjp_eq_qedCostProton q hq_pos j,
        gramGPMT_mul_aGPMT_eq_one q hq_pos j, ← hsym 0]
    have hrow0 : trGPMT q (Pi.single j 1) = gramGPMT q 0 j :=
      oneTerm_cost_eq_gramOfTrace_row0 (q - q⁻¹) (trGPMT q) j
    dsimp [twoTermCost]
    rw [hrow0]
    ring
  have hnet : (∑ j, x_star j) = n_target := by
    have h1 : ∀ j : Fin 6, x_star j = x_star j * (∑ i : Fin 6, gramGPMT q j i * aGPMT q i) := by
      intro j
      rw [gramGPMT_mul_aGPMT_eq_one q hq_pos j, mul_one]
    calc (∑ j : Fin 6, x_star j)
      _ = ∑ j : Fin 6, x_star j * (∑ i : Fin 6, gramGPMT q j i * aGPMT q i) :=
          Finset.sum_congr rfl fun j _ => h1 j
      _ = ∑ i : Fin 6, aGPMT q i * (∑ j : Fin 6, gramGPMT q i j * x_star j) := by
          simp_rw [Finset.mul_sum]
          rw [Finset.sum_comm]
          refine Finset.sum_congr rfl fun i _ => ?_
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [gramGPMT_symm q (ne_of_gt hq_pos) j i]
          ring
      _ = ∑ i : Fin 6, aGPMT q i * u_star i := by
          refine Finset.sum_congr rfl fun i _ => ?_
          have hi := congrFun hx_solve i
          simpa [Matrix.mulVec, dotProduct] using congrArg (aGPMT q i * ·) hi
      _ = n_target := by
          simp only [u_star, mul_ite, mul_zero, Finset.sum_ite_eq', Finset.mem_univ, ↓reduceIte]
          exact mul_div_cancel₀ n_target (ne_of_gt (ha 5))
  refine ⟨hy0_neg, ne_of_lt hy0_neg, x_star, s_star, ?_, hdual, hnet, ?_, ?_⟩
  · -- 1. `s_star i ≥ 0` for all `i : Fin 6`:
    intro i
    fin_cases i
    · have hb0 : 0 < betaVec 0 := by simpa [betaVec] using hbeta.1
      have hterm : 0 < -y0StarProtonTwoTermGPMT q α * aGPMT q 0 :=
        mul_pos (neg_pos.mpr hy0_neg) (ha 0)
      dsimp [s_star]; linarith
    · have hb1 : 0 < betaVec 1 := by simpa [betaVec] using hbeta.2.1
      have hterm : 0 < -y0StarProtonTwoTermGPMT q α * aGPMT q 1 :=
        mul_pos (neg_pos.mpr hy0_neg) (ha 1)
      dsimp [s_star]; linarith
    · have hb2 : 0 < betaVec 2 := by simpa [betaVec] using hbeta.2.2.1
      have hterm : 0 < -y0StarProtonTwoTermGPMT q α * aGPMT q 2 :=
        mul_pos (neg_pos.mpr hy0_neg) (ha 2)
      dsimp [s_star]; linarith
    · have hb3 : 0 < betaVec 3 := by simpa [betaVec] using hbeta.2.2.2.1
      have hterm : 0 < -y0StarProtonTwoTermGPMT q α * aGPMT q 3 :=
        mul_pos (neg_pos.mpr hy0_neg) (ha 3)
      dsimp [s_star]; linarith
    · have hb4 : 0 < betaVec 4 := by simpa [betaVec] using hbeta.2.2.2.2.1
      have hterm : 0 < -y0StarProtonTwoTermGPMT q α * aGPMT q 4 :=
        mul_pos (neg_pos.mpr hy0_neg) (ha 4)
      dsimp [s_star]; linarith
    · change 0 ≤ s_star 5
      rw [hs5]
  · -- 4. Primal Frobenius positivity `(gramGPMT q *ᵥ x_star)_i ≥ 0`:
    intro i
    have hi : (∑ j : Fin 6, gramGPMT q i j * x_star j) = u_star i := by
      simpa [Matrix.mulVec, dotProduct] using congrFun hx_solve i
    rw [hi]
    dsimp [u_star]
    by_cases h5 : i = 5
    · rw [if_pos h5]; exact div_nonneg hn (le_of_lt (ha 5))
    · rw [if_neg h5]
  · -- 5. Zero duality gap by `zero_gap_of_complementary_slackness`:
    apply zero_gap_of_complementary_slackness (s := s_star) (G := gramGPMT q) hdual hnet
    intro i
    have hi : (∑ j : Fin 6, gramGPMT q i j * x_star j) = u_star i := by
      simpa [Matrix.mulVec, dotProduct] using congrFun hx_solve i
    rw [hi]
    by_cases h5 : i = 5
    · subst h5
      rw [hs5, zero_mul]
    · simp [u_star, h5]

end ArchimedeanConfinementResolution

-- ============================================================================
-- § 5. `RegimeTransitionZ2` & `He4DemandClosure` under GPMT + Two-Term Photon/QED (`cj01`, `qou-j540`)
-- ============================================================================

section NuclearRegimesAndHe4Closure

/-- Normal-form vector `[0, 0, 1, h, h, h²]` of the cinquefoil word `T_{2,5} = (σ₀σ₁)²σ₀` in `H₃(q)`. -/
def t25NF {R : Type*} [CommRing R] (h : R) : Fin 6 → R :=
  ![0, 0, 1, h, h, h ^ 2]

/-- Normal-form vector `[0, 0, 0, 0, 1, 0]` of `L₊ = σ₀σ₁` in `QOU.Machinery.H3.mulNF` coordinates. -/
def hopfPlusNF {R : Type*} [CommRing R] : Fin 6 → R :=
  ![0, 0, 0, 0, 1, 0]

/-- Verification that `t25NF h` equals the five-step fold `σ₀ · σ₁ · σ₀ · σ₁ · σ₀` in `H₃(q)`. -/
theorem t25NF_eq_fold {R : Type*} [CommRing R] (h : R) :
    mulσ₀ h (mulσ₁ h (mulσ₀ h (mulσ₁ h (mulσ₀ h (Pi.single 0 1))))) = t25NF h := by
  funext k
  fin_cases k <;>
    (simp only [mulσ₀, mulσ₁, t25NF, Pi.single_apply, Fin.isValue, Fin.reduceEq,
      ↓reduceIte, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]; ring)

/-- Linear pairing of any normal-form vector `v` against a basis cost vector `c`. -/
def evalCostNF {R : Type*} [CommRing R] (c v : Fin 6 → R) : R :=
  ∑ j : Fin 6, c j * v j

/-- Closed-form GPMT trace difference `trGPMT q (T_{2,5}) - trGPMT q (L₊)`. -/
theorem trGPMT_t25_sub_hopfPlus (q : ℝ) (hq : q ≠ 0) :
    trGPMT q (t25NF (q - q⁻¹)) - trGPMT q hopfPlusNF =
      (q ^ 2 - q + 1) *
        (q ^ 13 + q ^ 12 + q ^ 11 - q ^ 10 - q ^ 6 + q ^ 4 - q ^ 2 - q - 1) /
          (q ^ 2 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have hq4' : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by positivity
  rw [trGPMT_eq_wedderburn_sum q hq hq2 hq4, trGPMT_eq_wedderburn_sum q hq hq2 hq4,
      w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4, dMod111Abs_eq,
      chi21, chi21, chiM_eq_closed q hq hq2, chiM_eq_closed q hq hq2]
  unfold chi3 chi111 chiNF t25NF hopfPlusNF
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp
  ring

/-- Closed-form QED adjacent-charge cost difference `qedCostProton(T_{2,5}) - qedCostProton(L₊)`. -/
theorem qedCostProton_t25_sub_hopfPlus (q : ℝ) (hq : q ≠ 0) :
    evalCostNF (qedCostProton q) (t25NF (q - q⁻¹)) - evalCostNF (qedCostProton q) hopfPlusNF =
      2 * (q ^ 6 - 3 * q ^ 4 - q ^ 3 + 2 * q ^ 2 + q + 1) / (9 * q) := by
  have h3 : (3 : ℝ) ≠ 0 := by norm_num
  unfold evalCostNF
  rw [Fin.sum_univ_six, Fin.sum_univ_six, qedCostProton_zero,
      qedCostProton_one q hq h3, qedCostProton_two q hq h3,
      qedCostProton_three q hq h3, qedCostProton_four q hq h3, qedCostProton_five q hq h3]
  simp only [t25NF, hopfPlusNF, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  field_simp
  ring

/-- **Unconditional `RegimeTransitionZ2` Instance on `[21/20, 6/5]` under Two-Term GPMT Cost**:
For every `q ∈ [21/20, 6/5]` (`[1.05, 1.20]`, containing `q₀ ≈ 1.10998` and `q_{2t} ≈ 1.10998`),
`E0 > 0`, and `α ≥ 0` (`α_EM(q₀) > 0`), `L₊` strictly dominates `T_{2,5}` (`RegimeTransitionZ2`). -/
theorem regimeTransitionZ2_twoTerm_gpmt
    (q E0 α : ℝ) (hq_lo : 21 / 20 ≤ q) (hq_hi : q ≤ 6 / 5)
    (hE0 : 0 < E0) (hα : 0 ≤ α) :
    RegimeTransitionZ2
      (evalCostNF (twoTermCost E0 α (fun j => trGPMT q (Pi.single j 1)) (qedCostProton q))
        (t25NF (q - q⁻¹)))
      (evalCostNF (twoTermCost E0 α (fun j => trGPMT q (Pi.single j 1)) (qedCostProton q))
        hopfPlusNF) := by
  set t : ℝ := q - 1
  have ht_lo : 1 / 20 ≤ t := by linarith
  have ht_hi : t ≤ 1 / 5 := by linarith
  have ht0 : 0 < t := by linarith
  have hq_pos : 0 < q := by linarith
  have hq_eq : q = 1 + t := by linarith
  -- 1. Strong GPMT difference is strictly positive for all `q ≥ 21/20`:
  have hgpmt_lin : ∀ v : Fin 6 → ℝ,
      evalCostNF (fun j => trGPMT q (Pi.single j 1)) v = trGPMT q v := by
    intro v
    unfold evalCostNF trGPMT trM chi111
    simp [Fin.sum_univ_six, TRM, chiNF]
    ring
  have hgpmt_pos : 0 < trGPMT q (t25NF (q - q⁻¹)) - trGPMT q hopfPlusNF := by
    rw [trGPMT_t25_sub_hopfPlus q (ne_of_gt hq_pos)]
    have hden : 0 < q ^ 2 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) := by positivity
    have hnum : 0 < (q ^ 2 - q + 1) *
        (q ^ 13 + q ^ 12 + q ^ 11 - q ^ 10 - q ^ 6 + q ^ 4 - q ^ 2 - q - 1) := by
      have hexp15 : (q ^ 2 - q + 1) *
          (q ^ 13 + q ^ 12 + q ^ 11 - q ^ 10 - q ^ 6 + q ^ 4 - q ^ 2 - q - 1) =
          (20 * t - 1) + (164 * t ^ 2 + 700 * t ^ 3 + 1995 * t ^ 4 + 4134 * t ^ 5 +
            6490 * t ^ 6 + 7892 * t ^ 7 + 7511 * t ^ 8 + 5600 * t ^ 9 + 3244 * t ^ 10 +
            1433 * t ^ 11 + 467 * t ^ 12 + 106 * t ^ 13 + 15 * t ^ 14 + t ^ 15) := by
        rw [hq_eq]; ring
      have hrest : 0 < 164 * t ^ 2 + 700 * t ^ 3 + 1995 * t ^ 4 + 4134 * t ^ 5 +
          6490 * t ^ 6 + 7892 * t ^ 7 + 7511 * t ^ 8 + 5600 * t ^ 9 + 3244 * t ^ 10 +
          1433 * t ^ 11 + 467 * t ^ 12 + 106 * t ^ 13 + 15 * t ^ 14 + t ^ 15 := by positivity
      rw [hexp15]; linarith
    exact div_pos hnum hden
  -- 2. QED proton difference is strictly positive on `1 ≤ q ≤ 6/5`:
  have hqed_pos : 0 < evalCostNF (qedCostProton q) (t25NF (q - q⁻¹)) -
      evalCostNF (qedCostProton q) hopfPlusNF := by
    rw [qedCostProton_t25_sub_hopfPlus q (ne_of_gt hq_pos)]
    have ht2 : t ^ 2 ≤ (1 / 5 : ℝ) ^ 2 := pow_le_pow_left₀ (le_of_lt ht0) ht_hi 2
    have hnum : 0 < 2 * (q ^ 6 - 3 * q ^ 4 - q ^ 3 + 2 * q ^ 2 + q + 1) := by
      have hexp : q ^ 6 - 3 * q ^ 4 - q ^ 3 + 2 * q ^ 2 + q + 1 =
          (1 - 4 * t - 4 * t ^ 2) + (7 * t ^ 3 + 12 * t ^ 4 + 6 * t ^ 5 + t ^ 6) := by
        rw [hq_eq]; ring
      have hrest : 0 < 7 * t ^ 3 + 12 * t ^ 4 + 6 * t ^ 5 + t ^ 6 := by positivity
      rw [hexp]; linarith
    exact div_pos hnum (by positivity)
  -- 3. Combine both positive terms into `RegimeTransitionZ2`:
  refine ⟨?_⟩
  have hcomb :
      evalCostNF (twoTermCost E0 α (fun j => trGPMT q (Pi.single j 1)) (qedCostProton q))
          (t25NF (q - q⁻¹)) -
        evalCostNF (twoTermCost E0 α (fun j => trGPMT q (Pi.single j 1)) (qedCostProton q))
          hopfPlusNF =
        E0 * (trGPMT q (t25NF (q - q⁻¹)) - trGPMT q hopfPlusNF) +
          α * E0 * (evalCostNF (qedCostProton q) (t25NF (q - q⁻¹)) -
            evalCostNF (qedCostProton q) hopfPlusNF) := by
    rw [← hgpmt_lin (t25NF (q - q⁻¹)), ← hgpmt_lin hopfPlusNF]
    unfold evalCostNF twoTermCost
    simp only [Fin.sum_univ_six]
    ring
  have hpos_total : 0 <
      E0 * (trGPMT q (t25NF (q - q⁻¹)) - trGPMT q hopfPlusNF) +
        α * E0 * (evalCostNF (qedCostProton q) (t25NF (q - q⁻¹)) -
          evalCostNF (qedCostProton q) hopfPlusNF) :=
    add_pos_of_pos_of_nonneg (mul_pos hE0 hgpmt_pos)
      (mul_nonneg (mul_nonneg hα (le_of_lt hE0)) (le_of_lt hqed_pos))
  linarith

/-- Demand magnitude `|dem(coeffs)| = ∑_{c ∈ coeffs} max(0, -c)` of a normal-form coefficient list. -/
def listDemMag (coeffs : List ℝ) : ℝ :=
  (coeffs.map fun c => max 0 (-c)).sum

theorem listDemMag_nonneg (coeffs : List ℝ) : 0 ≤ listDemMag coeffs := by
  induction coeffs with
  | nil => simp [listDemMag]
  | cons c cs ih =>
    simp only [listDemMag, List.map_cons, List.sum_cons]
    exact add_nonneg (le_max_left 0 (-c)) ih

/-- Equivalence between `NuclearOperatorRegimes.He4DemandClosure coeffs` (`∀ c ∈ coeffs, 0 ≤ c`)
and vanishing demand magnitude `listDemMag coeffs = 0` (`cj01` & `qou-j540`). -/
theorem he4DemandClosure_iff_listDemMag_eq_zero (coeffs : List ℝ) :
    He4DemandClosure coeffs ↔ listDemMag coeffs = 0 := by
  constructor
  · intro hcl
    induction coeffs with
    | nil => simp [listDemMag]
    | cons c cs ih =>
      simp only [listDemMag, List.map_cons, List.sum_cons]
      have hc : max (0 : ℝ) (-c) = 0 :=
        max_eq_left (neg_nonpos.mpr (hcl.all_nonneg c (List.mem_cons_self ..)))
      rw [hc, zero_add]
      exact ih ⟨fun x hx => hcl.all_nonneg x (List.mem_cons_of_mem c hx)⟩
  · intro hzero
    refine ⟨?_⟩
    induction coeffs with
    | nil => intro x hx; cases hx
    | cons c cs ih =>
      simp only [listDemMag, List.map_cons, List.sum_cons] at hzero
      have hm_nonneg : 0 ≤ max (0 : ℝ) (-c) := le_max_left 0 (-c)
      have hcs_nonneg : 0 ≤ listDemMag cs := listDemMag_nonneg cs
      have hc0 : max (0 : ℝ) (-c) = 0 := by
        change max 0 (-c) + listDemMag cs = 0 at hzero
        linarith
      have hcs0 : listDemMag cs = 0 := by
        change max 0 (-c) + listDemMag cs = 0 at hzero
        linarith
      have hc_ge : 0 ≤ c := by
        have hle : -c ≤ 0 := by
          calc -c ≤ max 0 (-c) := le_max_right 0 (-c)
          _ = 0 := hc0
        linarith
      intro x hx
      rcases List.mem_cons.mp hx with rfl | hmem
      · exact hc_ge
      · exact ih hcs0 x hmem

/-- Reading-3 Wedderburn Frobenius positivity (`chi3 ≥ 0`, `chi21 ≥ 0`, `chi111 ≥ 0` with `chi3 > 0`,
as satisfied by `(V³)^m` and the bare `⁴He` nuclear normal form) implies `trGPMT q v > 0` for
every real `q > 0`, whereas `L₊` alone violates `(2,1)` character positivity (`chi21(L₊) = -1 < 0`). -/
theorem trGPMT_pos_of_wedderburn_frobenius_feasible
    (q : ℝ) (hq : 0 < q) (v : Fin 6 → ℝ)
    (hc3 : 0 < chi3 q v) (hc21 : 0 ≤ chi21 q v) (hc111 : 0 ≤ chi111 q v) :
    0 < trGPMT q v ∧ chi21 q hopfPlusNF = -1 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  obtain ⟨hw3, hw21, hd⟩ := gpmt_wedderburn_weights_pos q hq
  refine ⟨?_, ?_⟩
  · rw [trGPMT_eq_wedderburn_sum q hq0 hq2 hq4 v]
    have t1 : 0 < w3 q (zD q) * chi3 q v := mul_pos hw3 hc3
    have t2 : 0 ≤ w21 q (zD q) * chi21 q v := mul_nonneg (le_of_lt hw21) hc21
    have t3 : 0 ≤ dMod111Abs q * chi111 q v := mul_nonneg (le_of_lt hd) hc111
    linarith
  · rw [chi21, chiM_eq_closed q hq0 hq2]
    simp [hopfPlusNF]

end NuclearRegimesAndHe4Closure

end QOU.Interactions.TwoTermPhotonGPMTConfinementSDP
