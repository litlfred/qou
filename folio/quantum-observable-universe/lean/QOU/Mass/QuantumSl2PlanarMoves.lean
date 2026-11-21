import QOU.Mass.QuantumSl2CrossingSymmetry

/-!
# Planar moves for the unoriented `U_q(sl₂)` calculus

With the Kauffman-normalised cup and cap of `QuantumSl2CupCap`, a crossing turned a quarter
turn is the inverse crossing (`rotOp_rCheck_mul_rCheck`). This file adds the other local moves
that relate two closed diagrams of the same link:

* **second snake** `(1 ⊗ cap)(cup ⊗ 1) = 1`, coefficientwise (`sum_cup_cap`);
* **slide** a crossing through a cup:
  `(Z ⊗ 1)(1 ⊗ cup) = (1 ⊗ rot Z)(cup ⊗ 1)` for every `Z` (`slide_cup`), so with crossing
  symmetry `(Ř ⊗ 1)(1 ⊗ cup) = (1 ⊗ Ř⁻¹)(cup ⊗ 1)`;
* **Reidemeister I** `Ř · cup = (−1)^m s^{−m(m+2)} cup` (`rCheck_cupVec`);
* **rotation inside a trace** `tr(W · rot M) = tr(nat W · M)` (`trace_mul_rotOp`);
* **trace as closure** `cap (A ⊗ 1) cup = (−1)^m tr(K A)` (`cap_closure_eq_trace`): the
  quantum trace with `K` is the cup/cap closure up to the Kauffman sign `(−1)^m`. This is the
  source of the `(−1)^{N−1}` between the braid-closure trace and van der Veen's printed formula.

All four were checked exactly in sympy at `N = 2, 3` before formalisation (issue #7912).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-- Ref: [kauffman1987] Kauffman, "State models and the Jones polynomial", Topology 26 (1987)
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

section Snake

variable (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)

include hq hint in
/-- **Second snake identity**, coefficientwise: `Σ_p cup(i,p) cap(p,β) = δ_{iβ}`. -/
theorem sum_cup_cap (i β : Fin (m + 1)) :
    ∑ p : Fin (m + 1), cupVec q m (i, p) * capVec q m (p, β) = if i = β then 1 else 0 := by
  rw [Finset.sum_eq_single (⟨m - i, by omega⟩ : Fin (m + 1))]
  · simp only [cupVec, hwVec, capVec]
    rw [if_pos (by omega)]
    by_cases h : i = β
    · subst h
      rw [if_pos (by omega), if_pos rfl]
      exact snake_coef' q hq m hint i (by omega)
    · rw [if_neg (fun h' => h (Fin.ext (by omega))), if_neg h, mul_zero]
  · intro p _ hp
    have : ¬ ((i : ℕ) + p = m) := fun h => hp (Fin.ext (by simp; omega))
    simp [cupVec, hwVec, this]
  · simp

end Snake

section Slide

variable (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)

include hq hint in
/-- **Sliding through a cup.** `(Z ⊗ 1)(1 ⊗ cup) = (1 ⊗ rot Z)(cup ⊗ 1)` as maps
`V → V ⊗ V ⊗ V`, entrywise. With `rot Ř = Ř⁻¹` this moves a crossing past a cup. -/
theorem slide_cup (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (i j k l : Fin (m + 1)) :
    ∑ p : Fin (m + 1), Z (i, j) (l, p) * cupVec q m (p, k)
      = ∑ p : Fin (m + 1), cupVec q m (i, p) * rotOp q m Z (j, k) (p, l) := by
  simp only [rotOp_apply, Finset.mul_sum]
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun β _ => (Finset.sum_comm)]
  have h : ∀ β : Fin (m + 1), ∑ γ : Fin (m + 1), ∑ p : Fin (m + 1),
      cupVec q m (i, p) * (capVec q m (p, β) * Z (β, j) (l, γ) * cupVec q m (γ, k))
      = if i = β then ∑ γ : Fin (m + 1), Z (β, j) (l, γ) * cupVec q m (γ, k) else 0 := by
    intro β
    have hs := sum_cup_cap q hq m hint i β
    split_ifs with hiβ
    · refine Finset.sum_congr rfl fun γ _ => ?_
      rw [show (∑ p : Fin (m + 1), cupVec q m (i, p) * (capVec q m (p, β) * Z (β, j) (l, γ)
          * cupVec q m (γ, k))) = (∑ p : Fin (m + 1), cupVec q m (i, p) * capVec q m (p, β))
          * (Z (β, j) (l, γ) * cupVec q m (γ, k)) by rw [Finset.sum_mul]; congr 1; ext p; ring,
        hs, if_pos hiβ, one_mul]
    · refine Finset.sum_eq_zero fun γ _ => ?_
      rw [show (∑ p : Fin (m + 1), cupVec q m (i, p) * (capVec q m (p, β) * Z (β, j) (l, γ)
          * cupVec q m (γ, k))) = (∑ p : Fin (m + 1), cupVec q m (i, p) * capVec q m (p, β))
          * (Z (β, j) (l, γ) * cupVec q m (γ, k)) by rw [Finset.sum_mul]; congr 1; ext p; ring,
        hs, if_neg hiβ, zero_mul]
  rw [Finset.sum_congr rfl fun β _ => h β, Finset.sum_ite_eq]
  simp

end Slide

section Closure

variable (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)

include hq hint in
/-- **Trace as closure.** `cap (A ⊗ 1) cup = (−1)^m tr(K A)` on `V_{m+1}`. -/
theorem cap_closure_eq_trace (A : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) :
    ∑ a : Fin (m + 1), ∑ b : Fin (m + 1), ∑ c : Fin (m + 1),
        capVec q m (a, b) * A a c * cupVec q m (c, b)
      = (-1) ^ m * trace (irrepKp q m * A) := by
  have hterm : ∀ a : Fin (m + 1), ∑ b : Fin (m + 1), ∑ c : Fin (m + 1),
      capVec q m (a, b) * A a c * cupVec q m (c, b)
        = (-1) ^ m * (q ^ (m - (a : ℕ)) * q⁻¹ ^ (a : ℕ) * A a a) := by
    intro a
    rw [Finset.sum_eq_single (⟨m - a, by omega⟩ : Fin (m + 1))]
    · rw [Finset.sum_eq_single a]
      · simp only [capVec, cupVec, hwVec]
        rw [if_pos (by omega), if_pos (by omega)]
        have hA := hwCoef_ne_zero q hq m hint a (by omega)
        rw [kp_eq_zpow q hq (show (a : ℕ) ≤ m by omega)]
        unfold capCoefQ
        rw [show wt m a = (m : ℤ) - 2 * ((a : ℕ) : ℤ) from rfl]
        field_simp
      · intro c _ hc
        have : ¬ ((c : ℕ) + (m - a) = m) := fun h => hc (Fin.ext (by have := a.isLt; omega))
        simp [cupVec, hwVec, this]
      · simp
    · intro b _ hb
      have : ¬ ((a : ℕ) + b = m) := fun h => hb (Fin.ext (by simp; omega))
      refine Finset.sum_eq_zero fun c _ => ?_
      simp [capVec, this]
    · simp
  rw [Finset.sum_congr rfl fun a _ => hterm a, ← Finset.mul_sum]
  congr 1
  simp [trace, irrepKp, diagonal_mul]

end Closure

section ReidemeisterI

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hq2 in
/-- **Reidemeister I.** `Ř · cup = (−1)^m s^{−m(m+2)} cup`: a kink is a scalar. -/
theorem rCheck_cupVec (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0) :
    rCheckMat s hs m m *ᵥ cupVec (s ^ 2) m
      = ((-1) ^ m * s ^ (-((m : ℤ) * (m + 2)))) • cupVec (s ^ 2) m := by
  have hr : ∀ k < rOrder m m, qint (s ^ 2) (k + 1) ≠ 0 := fun k hk =>
    hint (k + 1) (by omega) (by unfold rOrder at hk; omega)
  have hc : ∀ p < m, qint (s ^ 2) (m - p) ≠ 0 := fun p hp => hint (m - p) (by omega) (by omega)
  have h := rCheck_hwVec s hs hq2 m m m le_rfl le_rfl hr hc hc
  rw [braidEigen_eq s hs m m le_rfl hc] at h
  rw [rCheckMat_mulVec]
  unfold cupVec
  rw [h]
  congr 1
  congr 1
  ring_nf

end ReidemeisterI

section RotTrace

variable (q : 𝕜) (m : ℕ)

/-- Rotation of the *other* operator inside a trace: bend the first output of `W` down to the
left and its second input up to the right. -/
def natOp (W : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  fun y x => ∑ a : Fin (m + 1), ∑ d : Fin (m + 1),
    capVec q m (a, x.1) * W (a, y.1) (x.2, d) * cupVec q m (y.2, d)

/-- **Rotation inside a trace.** `tr(W · rot M) = tr(nat W · M)`. -/
theorem trace_mul_rotOp (W M : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    trace (W * rotOp q m M) = trace (natOp q m W * M) := by
  simp only [trace, diag, mul_apply, rotOp_apply, natOp, Fintype.sum_prod_type,
    Finset.mul_sum, Finset.sum_mul]
  rw [Finset.sum_comm]
  conv_lhs => enter [2, x0, 2, x1, 2, x2, 2, x3]; rw [Finset.sum_comm]
  conv_lhs => enter [2, x0, 2, x1, 2, x2]; rw [Finset.sum_comm]
  conv_lhs => enter [2, x0, 2, x1]; rw [Finset.sum_comm]
  conv_lhs => enter [2, x0]; rw [Finset.sum_comm]
  conv_lhs => enter [2, x0, 2, x1, 2, x2, 2, x3]; rw [Finset.sum_comm]
  conv_lhs => enter [2, x0, 2, x1, 2, x2]; rw [Finset.sum_comm]
  conv_lhs => enter [2, x0, 2, x1]; rw [Finset.sum_comm]
  conv_lhs => enter [2, x0, 2, x1, 2, x2]; rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
    Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => ?_
  ring

end RotTrace

end QOU.Mass.QuantumSl2

