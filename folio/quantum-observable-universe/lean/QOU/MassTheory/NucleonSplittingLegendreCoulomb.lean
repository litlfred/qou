/-
Copyright (c) 2026 Quantum Observable Universe Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases

/-!
# Nucleon Splitting Legendre–Coulomb Identities (`QOU.MassTheory.NucleonSplittingLegendreCoulomb`)

Exact algebraic and matrix identities over generic commutative rings and fields (§7c)
governing the two-channel neutron–proton mass difference `Δm_np = m_n - m_p` and
free-neutron beta-decay endpoint `Q_β(n) = Δm_np - m_e` (`qou-cds1`, `qou-15sj`, `qou-37y0`):

## Main Declarations

1. **Canonical Reeb-Momentum Legendre Transform & Two-Channel Sign Flip:**
   - `reebLagrangianQuad`, `reebCanonicalMomentum`, `reebHamiltonianCan`:
     Quadratic Reeb-velocity polynomial `L(v) = a₂ v² + a₁ v + a₀`, conjugate momentum
     `p = 2 a₂ v + a₁`, and canonical Hamiltonian `H_can(p) = (p - a₁)² / (4 a₂) - a₀`.
   - `legendre_duality_exact`:
     Exact Legendre inversion `p * v - L(v) = H_can(p)` at `v = (p - a₁) / (2 a₂)`.
   - `hamiltonian_at_two_a2_eq`:
     Evaluated at unshifted kinetic momentum `p = 2 a₂`,
     `H_can(2 a₂) = a₂ - a₁ + a₁² / (4 a₂) - a₀`, flipping `+a₁ ↦ -a₁` and `+a₀ ↦ -a₀`
     relative to `L(1) = a₂ + a₁ + a₀` while `p(1) * 1 - L(1) = a₂ - a₀` cancels `a₁`.
   - `delta_hamiltonian_two_channel_split`:
     Exact four-piece neutron-minus-proton decomposition
     `ΔH_can = Δa₂ - Δa₁ + Δ(a₁² / (4 a₂)) - Δa₀`.
   - `legendre_own_sector_q_inv_sq_shift`:
     When `a₀_p = c` and `a₀_n = q⁻¹ ^ 2 * c` (`q ≠ 0`), the Legendre horizontal channel
     `-(a₀_n - a₀_p)` equals `(1 - q⁻¹ ^ 2) * c = ((q ^ 2 - 1) / q ^ 2) * c`.

2. **All-3-Pairs `(12, 23, 13)` Charge Operators & Cartan Quantum-Trace Identities:**
   - `Q12p`, `Q23p`, `Q13p`, `Q12n`, `Q23n`, `Q13n`, `QSelfP`, `QSelfN`:
     Constituent 3×3 diagonal charge operators on the `(u, u, d)` and `(u, d, d)` sectors
     with all three strand pairs `(12, 23, 13)` retained symmetrically.
   - `all_three_pairs_charge_sum_and_self_identities`:
     `Q₁₂^{(p)} + Q₂₃^{(p)} + Q₁₃^{(p)} = 0`, `Q₁₂^{(n)} + Q₂₃^{(n)} + Q₁₃^{(n)} = (-1/3) • 1`,
     unweighted pairwise and self-charge `n - p` differences both equal `(-1/3) • 1`, and
     total-charge-square `QSelf + 2 • QPair` equals `1` on `p` and `0` on `n`.
   - `cartan_qtrace_breaks_self_pair_degeneracy`:
     Under Cartan weights `(q⁻¹` on `W_n`, `q` on `W_p)`, the self-charge difference
     `(2/3) q⁻¹ - q` and pairwise difference `(-1/3) q⁻¹ - 0` differ by `-(q - q⁻¹)`,
     which vanishes iff `q ^ 2 = 1`.
   - `eps_flavour_eq_neg_three_q_sq_sub_one_mul_deltaT_allPairs`:
     Universal field identity `epsFlavour = -3 * (q ^ 2 - 1) * deltaTAllPairsRaw`
     alongside `deltaTAllPairsConnected = 0` for arbitrary 3-strand trace `trV3`.

3. **Two-Row Parameter `z(q) = q³ / (q² + 1)` Bar-Involution & `N = 2` Bracket Identity:**
   - `two_row_z_bar_defect_and_n2_rung`:
     `z(q⁻¹) = q⁻¹ ^ 4 * z(q)`, `z(q) - z(q⁻¹) = q - q⁻¹`,
     `(q + q⁻¹)² - (q² + 1 + q⁻¹ ^ 2) = 1`, and
     `1 - 1 / (q + q⁻¹)² = (q² + 1 + q⁻¹ ^ 2) / (q + q⁻¹)²`.

4. **`§3b-cond` Two-Channel Nucleon Splitting & Cottingham Sign Consequences:**
   - `TwoChannelNucleonSplittingHypothesis`: conditional hypothesis class encoding the
     two-channel decomposition `Δm_np = Δm_strong + Δm_em` with repulsive pairwise Coulomb
     shift `Δm_em = -(1 / 3) * k_em` and beta-decay endpoint `Q_β = Δm_np - m_e`.
   - `two_channel_qbeta_and_strong_enhancement_of_cottingham`:
     Composes the class hypotheses over `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`
     to obtain `Q_β = Δm_strong - (1 / 3) * k_em - m_e`,
     `Δm_strong = Δm_np + (1 / 3) * k_em`, and `Δm_np < Δm_strong` whenever `0 < k_em`.

## References
- [leitner2026] `prop:neutron-proton-mass-splitting`, `def:categorical-lagrangian`
- [cottingham1963] W. N. Cottingham, *Ann. Phys.* 25 (1963), 424–432
-/

set_option autoImplicit false

namespace QOU.MassTheory.NucleonSplittingLegendreCoulomb

open Matrix

/-! ## 1. Canonical Reeb-Momentum Legendre Transform & Two-Channel Sign Flip -/

section LegendreTwoChannel

/-- Quadratic Reeb-velocity Lagrangian polynomial `L(v) = a₂ * v² + a₁ * v + a₀`. -/
def reebLagrangianQuad {R : Type*} [CommRing R] (a₂ a₁ a₀ v : R) : R :=
  a₂ * v ^ 2 + a₁ * v + a₀

/-- Canonical momentum `p = ∂L/∂v = 2 * a₂ * v + a₁` conjugate to Reeb velocity `v`. -/
def reebCanonicalMomentum {R : Type*} [CommRing R] (a₂ a₁ v : R) : R :=
  2 * a₂ * v + a₁

/-- Canonical Legendre Hamiltonian `H_can(p) = (p - a₁)² / (4 * a₂) - a₀`. -/
def reebHamiltonianCan {K : Type*} [Field K] (a₂ a₁ a₀ p : K) : K :=
  (p - a₁) ^ 2 / (4 * a₂) - a₀

/-- Exact Legendre inversion over any field `K` (`2 ≠ 0`, `a₂ ≠ 0`): evaluating at
`v = (p - a₁) / (2 * a₂)` recovers `reebCanonicalMomentum a₂ a₁ v = p` and
`p * v - reebLagrangianQuad a₂ a₁ a₀ v = reebHamiltonianCan a₂ a₁ a₀ p`. -/
theorem legendre_duality_exact {K : Type*} [Field K] (a₂ a₁ a₀ p : K)
    (h2 : (2 : K) ≠ 0) (ha₂ : a₂ ≠ 0) :
    let v := (p - a₁) / (2 * a₂)
    reebCanonicalMomentum a₂ a₁ v = p ∧
      p * v - reebLagrangianQuad a₂ a₁ a₀ v = reebHamiltonianCan a₂ a₁ a₀ p := by
  have h4 : (4 : K) ≠ 0 := by
    rw [show (4 : K) = 2 * 2 by ring]
    exact mul_ne_zero h2 h2
  refine ⟨?_, ?_⟩
  · dsimp only [reebCanonicalMomentum]
    field_simp [h2, ha₂]
    ring
  · dsimp only [reebLagrangianQuad, reebHamiltonianCan]
    field_simp [h2, h4, ha₂]
    ring

/-- Evaluation of `reebHamiltonianCan` at unshifted kinetic momentum `p = 2 * a₂` vs `L(1)`:
1. `H_can(2 * a₂) = a₂ - a₁ + a₁² / (4 * a₂) - a₀` (flipping `+a₁ ↦ -a₁` and `+a₀ ↦ -a₀`),
2. `L(1) = a₂ + a₁ + a₀`,
3. `p(1) * 1 - L(1) = a₂ - a₀` (fixed-velocity `v = 1` Legendre value cancels `a₁`). -/
theorem hamiltonian_at_two_a2_eq {K : Type*} [Field K] (a₂ a₁ a₀ : K)
    (h2 : (2 : K) ≠ 0) (ha₂ : a₂ ≠ 0) :
    reebHamiltonianCan a₂ a₁ a₀ (2 * a₂) = a₂ - a₁ + a₁ ^ 2 / (4 * a₂) - a₀ ∧
      reebLagrangianQuad a₂ a₁ a₀ 1 = a₂ + a₁ + a₀ ∧
      reebCanonicalMomentum a₂ a₁ 1 * 1 - reebLagrangianQuad a₂ a₁ a₀ 1 = a₂ - a₀ := by
  have h4 : (4 : K) ≠ 0 := by
    rw [show (4 : K) = 2 * 2 by ring]
    exact mul_ne_zero h2 h2
  refine ⟨?_, ?_, ?_⟩
  · unfold reebHamiltonianCan
    field_simp [h4, ha₂]
    ring
  · unfold reebLagrangianQuad
    ring
  · unfold reebCanonicalMomentum reebLagrangianQuad
    ring

/-- Four-piece neutron-minus-proton decomposition of `reebHamiltonianCan` at `p = 2 * a₂`:
`H_can^{(n)}(2 a_{2,n}) - H_can^{(p)}(2 a_{2,p}) = (a_{2,n} - a_{2,p}) - (a_{1,n} - a_{1,p}) +
(a_{1,n}² / (4 a_{2,n}) - a_{1,p}² / (4 a_{2,p})) - (a_{0,n} - a_{0,p})`. -/
theorem delta_hamiltonian_two_channel_split {K : Type*} [Field K]
    (a₂_n a₁_n a₀_n a₂_p a₁_p a₀_p : K)
    (h2 : (2 : K) ≠ 0) (ha₂_n : a₂_n ≠ 0) (ha₂_p : a₂_p ≠ 0) :
    reebHamiltonianCan a₂_n a₁_n a₀_n (2 * a₂_n) -
        reebHamiltonianCan a₂_p a₁_p a₀_p (2 * a₂_p) =
      (a₂_n - a₂_p) - (a₁_n - a₁_p) +
        (a₁_n ^ 2 / (4 * a₂_n) - a₁_p ^ 2 / (4 * a₂_p)) - (a₀_n - a₀_p) := by
  have hn := (hamiltonian_at_two_a2_eq a₂_n a₁_n a₀_n h2 ha₂_n).1
  have hp := (hamiltonian_at_two_a2_eq a₂_p a₁_p a₀_p h2 ha₂_p).1
  rw [hn, hp]
  ring

/-- Specialization of `delta_hamiltonian_two_channel_split` when `a₁_p = 0` (matching the
vanishing pairwise charge sum on the proton `(u, u, d)` sector) and `a₀_p = c`,
`a₀_n = q⁻¹ ^ 2 * c` (`q ≠ 0`): the recoil shift simplifies to `+a₁_n² / (4 a₂_n)` and the
Legendre horizontal shift `-(a₀_n - a₀_p)` equals `(1 - q⁻¹ ^ 2) * c = ((q² - 1) / q²) * c`. -/
theorem legendre_own_sector_q_inv_sq_shift {K : Type*} [Field K]
    (a₂_n a₁_n a₂_p q c : K)
    (h2 : (2 : K) ≠ 0) (ha₂_n : a₂_n ≠ 0) (ha₂_p : a₂_p ≠ 0) (hq : q ≠ 0) :
    reebHamiltonianCan a₂_n a₁_n (q⁻¹ ^ 2 * c) (2 * a₂_n) -
        reebHamiltonianCan a₂_p 0 c (2 * a₂_p) =
      (a₂_n - a₂_p) - a₁_n + a₁_n ^ 2 / (4 * a₂_n) + (1 - q⁻¹ ^ 2) * c ∧
      (1 - q⁻¹ ^ 2) * c = ((q ^ 2 - 1) / q ^ 2) * c := by
  have hsplit :=
    delta_hamiltonian_two_channel_split a₂_n a₁_n (q⁻¹ ^ 2 * c) a₂_p 0 c h2 ha₂_n ha₂_p
  refine ⟨?_, ?_⟩
  · rw [hsplit]
    ring
  · field_simp [hq]

end LegendreTwoChannel

/-! ## 2. All-3-Pairs `(12, 23, 13)` Charge Matrices & Cartan Quantum-Trace Identities -/

section AllPairsWeightSpace

/-- Pairwise charge matrix `Q₁₂` on the proton `(2, 1)` weight space (`uud, udu, duu`). -/
def Q12p {K : Type*} [Field K] : Matrix (Fin 3) (Fin 3) K :=
  !![4 / 9, 0, 0; 0, -2 / 9, 0; 0, 0, -2 / 9]

/-- Pairwise charge matrix `Q₂₃` on the proton `(2, 1)` weight space (`uud, udu, duu`). -/
def Q23p {K : Type*} [Field K] : Matrix (Fin 3) (Fin 3) K :=
  !![-2 / 9, 0, 0; 0, -2 / 9, 0; 0, 0, 4 / 9]

/-- Pairwise charge matrix `Q₁₃` on the proton `(2, 1)` weight space (`uud, udu, duu`). -/
def Q13p {K : Type*} [Field K] : Matrix (Fin 3) (Fin 3) K :=
  !![-2 / 9, 0, 0; 0, 4 / 9, 0; 0, 0, -2 / 9]

/-- Pairwise charge matrix `Q₁₂` on the neutron `(1, 2)` weight space (`udd, dud, ddu`). -/
def Q12n {K : Type*} [Field K] : Matrix (Fin 3) (Fin 3) K :=
  !![-2 / 9, 0, 0; 0, -2 / 9, 0; 0, 0, 1 / 9]

/-- Pairwise charge matrix `Q₂₃` on the neutron `(1, 2)` weight space (`udd, dud, ddu`). -/
def Q23n {K : Type*} [Field K] : Matrix (Fin 3) (Fin 3) K :=
  !![1 / 9, 0, 0; 0, -2 / 9, 0; 0, 0, -2 / 9]

/-- Pairwise charge matrix `Q₁₃` on the neutron `(1, 2)` weight space (`udd, dud, ddu`). -/
def Q13n {K : Type*} [Field K] : Matrix (Fin 3) (Fin 3) K :=
  !![-2 / 9, 0, 0; 0, 1 / 9, 0; 0, 0, -2 / 9]

/-- Constituent self-charge-squared matrix `Q₁² + Q₂² + Q₃²` on the proton `(2, 1)` sector. -/
def QSelfP {K : Type*} [Field K] : Matrix (Fin 3) (Fin 3) K :=
  !![4 / 9 + 4 / 9 + 1 / 9, 0, 0; 0, 4 / 9 + 1 / 9 + 4 / 9, 0; 0, 0, 1 / 9 + 4 / 9 + 4 / 9]

/-- Constituent self-charge-squared matrix `Q₁² + Q₂² + Q₃²` on the neutron `(1, 2)` sector. -/
def QSelfN {K : Type*} [Field K] : Matrix (Fin 3) (Fin 3) K :=
  !![4 / 9 + 1 / 9 + 1 / 9, 0, 0; 0, 1 / 9 + 4 / 9 + 1 / 9, 0; 0, 0, 1 / 9 + 1 / 9 + 4 / 9]

/-- All-3-pairs `(12, 23, 13)` symmetric charge identities on `(2, 1)` vs `(1, 2)` (`3 ≠ 0`):
1. `Q₁₂^{(p)} + Q₂₃^{(p)} + Q₁₃^{(p)} = 0`,
2. `Q₁₂^{(n)} + Q₂₃^{(n)} + Q₁₃^{(n)} = (-1 / 3) • 1`,
3. `QSelfP = 1` and `QSelfN = (2 / 3) • 1`,
4. Unweighted `n - p` differences of pairwise sum and self-charge sum both equal `(-1 / 3) • 1`,
5. Total-charge-squared `QSelf + 2 • QPair` equals `1` on `(2, 1)` and `0` on `(1, 2)`. -/
theorem all_three_pairs_charge_sum_and_self_identities {K : Type*} [Field K] (h3 : (3 : K) ≠ 0) :
    let qPairP : Matrix (Fin 3) (Fin 3) K := Q12p + Q23p + Q13p
    let qPairN : Matrix (Fin 3) (Fin 3) K := Q12n + Q23n + Q13n
    qPairP = 0 ∧
      qPairN = (-1 / 3 : K) • (1 : Matrix (Fin 3) (Fin 3) K) ∧
      (QSelfP : Matrix (Fin 3) (Fin 3) K) = 1 ∧
      (QSelfN : Matrix (Fin 3) (Fin 3) K) = (2 / 3 : K) • (1 : Matrix (Fin 3) (Fin 3) K) ∧
      qPairN - qPairP = (QSelfN : Matrix (Fin 3) (Fin 3) K) - QSelfP ∧
      (QSelfP : Matrix (Fin 3) (Fin 3) K) + (2 : K) • qPairP = 1 ∧
      (QSelfN : Matrix (Fin 3) (Fin 3) K) + (2 : K) • qPairN = 0 := by
  have h9 : (9 : K) = 3 * 3 := by ring
  have hp : (Q12p : Matrix (Fin 3) (Fin 3) K) + Q23p + Q13p = 0 := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [Q12p, Q23p, Q13p] <;> ring
  have hn : (Q12n : Matrix (Fin 3) (Fin 3) K) + Q23n + Q13n = (-1 / 3 : K) • 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [Q12n, Q23n, Q13n]
    all_goals (rw [h9]; field_simp [h3]; ring)
  have hsp : (QSelfP : Matrix (Fin 3) (Fin 3) K) = 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [QSelfP]
    all_goals (rw [h9]; field_simp [h3]; ring)
  have hsn : (QSelfN : Matrix (Fin 3) (Fin 3) K) = (2 / 3 : K) • 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [QSelfN]
    all_goals (rw [h9]; field_simp [h3]; ring)
  refine ⟨hp, hn, hsp, hsn, ?_, ?_, ?_⟩
  · rw [hp, hn, hsp, hsn]
    ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp [h3] <;> ring
  · rw [hp, hsp, smul_zero, add_zero]
  · rw [hn, hsn]
    ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp [h3] <;> ring

/-- Cartan quantum-trace weights (`q⁻¹` on `W_n`, `q` on `W_p`) lift the unweighted `q = 1`
degeneracy between `QSelf` (`2/3 - 1 = -1/3`) and `QPair` (`-1/3 - 0 = -1/3`):
`((2 / 3) * q⁻¹ - q * 1) - ((-1 / 3) * q⁻¹ - q * 0) = -(q - q⁻¹)`,
which vanishes iff `q ^ 2 = 1`. -/
theorem cartan_qtrace_breaks_self_pair_degeneracy {K : Type*} [Field K]
    (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    let deltaPair := (-1 / 3 : K) * q⁻¹ - q * 0
    let deltaSelf := (2 / 3 : K) * q⁻¹ - q * 1
    deltaSelf - deltaPair = -(q - q⁻¹) ∧
      (deltaSelf = deltaPair ↔ q ^ 2 = 1) := by
  refine ⟨?_, ?_⟩
  · field_simp [hq, h3]
    ring
  · constructor
    · intro heq
      have hdiff : ((2 / 3 : K) * q⁻¹ - q * 1) - ((-1 / 3 : K) * q⁻¹ - q * 0) = 0 :=
        sub_eq_zero.mpr heq
      have hrew : ((2 / 3 : K) * q⁻¹ - q * 1) - ((-1 / 3 : K) * q⁻¹ - q * 0) =
          -(q ^ 2 - 1) / q := by
        field_simp [hq, h3]
        ring
      rw [hrew, div_eq_zero_iff] at hdiff
      rcases hdiff with hnum | hq0
      · linear_combination -hnum
      · exact False.elim (hq hq0)
    · intro hq2
      have hdiff : ((2 / 3 : K) * q⁻¹ - q * 1) - ((-1 / 3 : K) * q⁻¹ - q * 0) =
          -(q ^ 2 - 1) / q := by
        field_simp [hq, h3]
        ring
      have hz : -(q ^ 2 - 1) / q = 0 := by
        rw [hq2]
        ring
      exact sub_eq_zero.mp (hdiff.trans hz)

/-- Universal polynomial relation between the 3-strand flavour quantum-trace difference
`epsFlavour = (q - q⁻¹) * trV3 / (q + q⁻¹) ^ 3` and the raw all-3-pairs charge quantum-trace
difference `deltaTAllPairsRaw = (q⁻¹ * ((-1/3) * trV3) - q * 0) / (q + q⁻¹) ^ 3`, together
with exact vanishing of the connected all-3-pairs quantum-trace difference:
`epsFlavour = -3 * (q ^ 2 - 1) * deltaTAllPairsRaw` and `deltaTAllPairsConn = 0`. -/
theorem eps_flavour_eq_neg_three_q_sq_sub_one_mul_deltaT_allPairs {K : Type*} [Field K]
    (q trV3 : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h3 : (3 : K) ≠ 0) :
    let qdim3 := (q + q⁻¹) ^ 3
    let epsFlavour := (q - q⁻¹) * trV3 / qdim3
    let deltaTAllPairsRaw := (q⁻¹ * ((-1 / 3 : K) * trV3) - q * 0) / qdim3
    let deltaTAllPairsConn :=
      (q⁻¹ * ((-1 / 3 : K) * trV3 + (1 / 3 : K) * trV3) - q * 0) / qdim3
    epsFlavour = -3 * (q ^ 2 - 1) * deltaTAllPairsRaw ∧ deltaTAllPairsConn = 0 := by
  have hsum_ne : q + q⁻¹ ≠ 0 := by
    have hrew : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp [hq]
    rw [hrew]
    exact div_ne_zero hq2 hq
  have hqdim_ne : (q + q⁻¹) ^ 3 ≠ 0 := pow_ne_zero 3 hsum_ne
  refine ⟨?_, ?_⟩
  · try dsimp only
    field_simp [hq, h3, hqdim_ne]
    ring
  · try dsimp only
    ring

end AllPairsWeightSpace

/-! ## 3. Two-Row Parameter `z(q) = q³ / (q² + 1)` Bar-Involution & `N = 2` Bracket Identity -/

section TwoRowParameterIdentities

/-- Canonical two-row trace parameter `z(q) = q ^ 3 / (q ^ 2 + 1)`. -/
def twoRowParam {K : Type*} [Field K] (q : K) : K :=
  q ^ 3 / (q ^ 2 + 1)

/-- Bar-involution (`q ↦ q⁻¹`) and `N = 2` bracket identities (`qou-cds1`):
1. `twoRowParam q⁻¹ = q⁻¹ ^ 4 * twoRowParam q` (bar-weight `-4`),
2. `twoRowParam q - twoRowParam q⁻¹ = q - q⁻¹` (exchanges `z` and `z - (q - q⁻¹)`),
3. `(q + q⁻¹)² - (q² + 1 + q⁻¹ ^ 2) = 1` (`[2]_q² - [3]_q = 1`),
4. `1 - 1 / (q + q⁻¹)² = (q² + 1 + q⁻¹ ^ 2) / (q + q⁻¹)²` (`b² = [3]_q / [2]_q²`). -/
theorem two_row_z_bar_defect_and_n2_rung {K : Type*} [Field K]
    (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    twoRowParam q⁻¹ = q⁻¹ ^ 4 * twoRowParam q ∧
      twoRowParam q - twoRowParam q⁻¹ = q - q⁻¹ ∧
      (q + q⁻¹) ^ 2 - (q ^ 2 + 1 + q⁻¹ ^ 2) = 1 ∧
      1 - 1 / (q + q⁻¹) ^ 2 = (q ^ 2 + 1 + q⁻¹ ^ 2) / (q + q⁻¹) ^ 2 := by
  have h1q2 : 1 + q ^ 2 ≠ 0 := by
    rw [add_comm]
    exact hq2
  have hqinv2 : q⁻¹ ^ 2 + 1 ≠ 0 := by
    have hrew : q⁻¹ ^ 2 + 1 = (1 + q ^ 2) / q ^ 2 := by field_simp [hq]
    rw [hrew]
    exact div_ne_zero h1q2 (pow_ne_zero 2 hq)
  have h2q : (q + q⁻¹) ^ 2 ≠ 0 := by
    have hrew : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp [hq]
    rw [hrew]
    exact pow_ne_zero 2 (div_ne_zero hq2 hq)
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold twoRowParam
    field_simp [hq, hq2, h1q2, hqinv2]
    ring
  · unfold twoRowParam
    field_simp [hq, hq2, h1q2, hqinv2]
    ring
  · field_simp [hq]
    ring
  · field_simp [hq, h2q]
    ring

end TwoRowParameterIdentities

/-! ## 4. `§3b-cond` Two-Channel Nucleon Splitting & Cottingham Sign Consequences -/

section ConditionalTwoChannelModel

/-- `@conjecture: primary`
Conditional hypothesis class (`§3b-cond`) for a two-channel nucleon mass-splitting model over
`K`: total `Δm_np = m_n - m_p` decomposes into `dm_strong + dm_em`, the all-pairs repulsive
Coulomb channel satisfies `dm_em = -(1 / 3) * k_em` (`Σ_{i<j} Q_i Q_j(n - p) = -1/3`), and
free-neutron beta decay satisfies `q_beta = dm_np - m_e`. No instance is registered; concrete
spatial-kernel selection for `k_em` and `dm_strong` remains open (`qou-37y0`).
-- Ref: [cottingham1963] W. N. Cottingham, Ann. Phys. 25 (1963), 424-432
-- Ref: [leitner2026] prop:neutron-proton-mass-splitting -/
class TwoChannelNucleonSplittingHypothesis (K : Type*) [Field K]
    (dm_np dm_strong dm_em k_em m_e q_beta : K) : Prop where
  /-- Two-channel additive decomposition `Δm_np = Δm_strong + Δm_em`. -/
  splitting_add : dm_np = dm_strong + dm_em
  /-- Pairwise `(u, d, d) - (u, u, d)` Coulomb channel `Δm_em = -(1 / 3) * k_em`. -/
  em_pair_law : dm_em = -(1 / 3 : K) * k_em
  /-- Kinematic beta-decay endpoint relation `Q_β(n) = Δm_np - m_e`. -/
  qbeta_kinematic : q_beta = dm_np - m_e

/-- Conditional consequences of `TwoChannelNucleonSplittingHypothesis` over an ordered field:
for any repulsive coupling `0 < k_em`,
1. `q_beta = dm_strong - (1 / 3) * k_em - m_e`,
2. `dm_strong = dm_np + (1 / 3) * k_em`,
3. `dm_em < 0` and `dm_np < dm_strong` (the strong isospin split strictly exceeds `m_n - m_p`). -/
theorem two_channel_qbeta_and_strong_enhancement_of_cottingham
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {dm_np dm_strong dm_em k_em m_e q_beta : K}
    [h : TwoChannelNucleonSplittingHypothesis K dm_np dm_strong dm_em k_em m_e q_beta]
    (hk : 0 < k_em) :
    q_beta = dm_strong - (1 / 3 : K) * k_em - m_e ∧
      dm_strong = dm_np + (1 / 3 : K) * k_em ∧
      dm_em < 0 ∧
      dm_np < dm_strong := by
  have h1 : q_beta = dm_strong - (1 / 3 : K) * k_em - m_e := by
    rw [h.qbeta_kinematic, h.splitting_add, h.em_pair_law]
    ring
  have h2 : dm_strong = dm_np + (1 / 3 : K) * k_em := by
    have hs := h.splitting_add
    rw [h.em_pair_law] at hs
    linear_combination -hs
  have hthird : (0 : K) < 1 / 3 := by norm_num
  have hpos : 0 < (1 / 3 : K) * k_em := mul_pos hthird hk
  have h3 : dm_em < 0 := by
    rw [h.em_pair_law]
    linarith
  have h4 : dm_np < dm_strong := by
    rw [h2]
    linarith
  exact ⟨h1, h2, h3, h4⟩

end ConditionalTwoChannelModel

end QOU.MassTheory.NucleonSplittingLegendreCoulomb
