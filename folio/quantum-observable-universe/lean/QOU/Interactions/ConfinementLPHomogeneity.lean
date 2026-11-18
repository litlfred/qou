/-!
# Confinement-LP Homogeneity and the Converse Shadow-Price Criterion

Bean `qou-ndsa`. Companion to `QOU.ParticleInteractions.operator_selection_lp`
and `computations/confinement_lp_braid_gram_probe.py`.

## Mathematical Statement

The operator-selection LP (`min t·x` subject to `𝟙·x = n_target`, `Gx ≥ 0`)
has two structural properties that together explain why Candidates 1, 2, and 3
of `qou-ndsa` fail and what a surviving formulation must satisfy:

1. **Primal cone homogeneity under `n_target` scaling:**
   Because the Frobenius positivity cone `Gx ≥ 0` is homogeneous, scaling any
   primal vector `x` by a non-negative scalar `k ≥ 0` scales the net sum
   `𝟙·(kx) = k(𝟙·x)`, scales the Frobenius slacks `G(kx) = k(Gx) ≥ 0`, and
   scales the objective `t·(kx) = k(t·x)` linearly. Therefore, letting the braid
   word enter *only* `n_target` scales `x*` homogeneously without changing the
   normalised operator profile.

2. **Dual pairing identity and converse non-degeneracy criterion:**
   For any dual-feasible decomposition `t = y₀·𝟙 + c` where the constraint
   contribution `c` is orthogonal to a radical direction `v` (`⟨c, v⟩ = 0`),
   pairing `t` with `v` yields the exact identity

       ⟨t, v⟩ = y₀ · ⟨𝟙, v⟩.

   Consequently:
   - **Degeneracy (`y₀ = 0`):** If `⟨t, v⟩ = 0` and `⟨𝟙, v⟩ ≠ 0`, then `y₀ = 0`
     (which rules out Candidate 2 `G^w` and Candidate 3 moment-SDP lifts, since
     the sign-block q-antisymmetriser `V` satisfies `G^w v = 0` and
     `⟨t, v⟩ = tr_M(V) = 0`).
   - **Converse (`y₀ ≠ 0` requires `⟨t(β), v⟩ ≠ 0`):** For *any* dual-feasible
     formulation whose constraint contribution annihilates `v`, achieving a
     non-zero shadow price `y₀ ≠ 0` **requires** `⟨t(β), v⟩ ≠ 0` — the cost
     vector itself must have a non-zero projection onto the radical direction
     `v` (breaking pure Markov-trace orthogonality on the sign block).

-- Ref: [leitner2026] bean qou-ndsa; QOU/ParticleInteractions/operator_selection_lp.lean;
-- computations/confinement_lp_braid_gram_probe.py
-/

namespace QOU.Interactions

/-- Pointwise scalar multiplication of an integer vector `x : Nat → Int`. -/
def scaleVec (k : Int) (x : Nat → Int) (j : Nat) : Int := k * x j

/-- Finite dot product `Σ_{j < d} a(j) · b(j)`. -/
def dotFin : Nat → (Nat → Int) → (Nat → Int) → Int
  | 0, _, _ => 0
  | d + 1, a, b => dotFin d a b + a d * b d

/-- Finite sum `Σ_{j < d} x(j) = ⟨𝟙, x⟩`. -/
def sumFin : Nat → (Nat → Int) → Int
  | 0, _ => 0
  | d + 1, x => sumFin d x + x d

/-- **Homogeneity of the net sum under target scaling:**
    `sumFin d (scaleVec k x) = k * sumFin d x`. -/
theorem sumFin_scaleVec (d : Nat) (k : Int) (x : Nat → Int) :
    sumFin d (scaleVec k x) = k * sumFin d x := by
  induction d with
  | zero => simp [sumFin]
  | succ n ih =>
    simp only [sumFin, scaleVec, ih, Int.mul_add]

/-- **Homogeneity of any linear pairing (objective or Gram row) under scaling:**
    `dotFin d a (scaleVec k x) = k * dotFin d a x`. -/
theorem dotFin_scaleVec_right (d : Nat) (k : Int) (a x : Nat → Int) :
    dotFin d a (scaleVec k x) = k * dotFin d a x := by
  induction d with
  | zero => simp [dotFin]
  | succ n ih =>
    simp only [dotFin, scaleVec, ih, Int.mul_add]
    have hmul : a n * (k * x n) = k * (a n * x n) := by
      rw [← Int.mul_assoc, Int.mul_comm (a n) k, Int.mul_assoc]
    rw [hmul]

/-- **Cone preservation under non-negative scaling (`0 ≤ k`):**
    if a Gram row pairing `dotFin d (G i) x` is non-negative, then so is
    `dotFin d (G i) (scaleVec k x)`. -/
theorem gramRow_nonneg_scaleVec (d : Nat) {k : Int} (hk : 0 ≤ k)
    (Gi x : Nat → Int) (hGx : 0 ≤ dotFin d Gi x) :
    0 ≤ dotFin d Gi (scaleVec k x) := by
  rw [dotFin_scaleVec_right]
  exact Int.mul_nonneg hk hGx

/-- Dual decomposition identity along a vector `v`: if `t j = y₀ + c j` for all
    `j`, then `⟨t, v⟩ = y₀ · ⟨𝟙, v⟩ + ⟨c, v⟩`. -/
theorem dotFin_dual_decomp (d : Nat) (t c v : Nat → Int) (y₀ : Int)
    (hdual : ∀ j, t j = y₀ + c j) :
    dotFin d t v = y₀ * sumFin d v + dotFin d c v := by
  induction d with
  | zero => simp [dotFin, sumFin]
  | succ n ih =>
    simp only [dotFin, sumFin, hdual n, Int.add_mul, Int.mul_add, ih]
    omega

/-- **Exact radical pairing identity (`qou-ndsa`).**
    Whenever the constraint contribution `c` is orthogonal to the radical
    direction `v` (`dotFin d c v = 0`), any dual-feasible cost vector
    `t = y₀·𝟙 + c` satisfies `⟨t, v⟩ = y₀ · ⟨𝟙, v⟩`. -/
theorem radical_pairing_eq_shadow_price_mul_net (d : Nat) (t c v : Nat → Int) (y₀ : Int)
    (hdual : ∀ j, t j = y₀ + c j)
    (hcv : dotFin d c v = 0) :
    dotFin d t v = y₀ * sumFin d v := by
  rw [dotFin_dual_decomp d t c v y₀ hdual, hcv, Int.add_zero]

/-- **Converse non-degeneracy theorem (`qou-ndsa`):**
    If the constraint contribution annihilates the radical (`⟨c, v⟩ = 0`), then
    a non-zero shadow price (`y₀ ≠ 0`) on a direction with `⟨𝟙, v⟩ ≠ 0`
    **requires** the cost vector to have non-zero pairing with the radical
    (`⟨t, v⟩ ≠ 0`).

    In particular, any reformulation that keeps the pure trace-functional cost vector
    `t_j = tr_M(b_j)` (which has `⟨t, v⟩ = tr_M(V) = 0`) cannot achieve `y₀ ≠ 0`;
    breaking homogeneity requires a braid-dependent cost `t(β)` with
    `⟨t(β), v⟩ ≠ 0`. -/
theorem radical_pairing_ne_zero_of_shadow_price_ne_zero
    (d : Nat) (t c v : Nat → Int) (y₀ : Int)
    (hdual : ∀ j, t j = y₀ + c j)
    (hcv : dotFin d c v = 0)
    (hone : sumFin d v ≠ 0)
    (hy₀ : y₀ ≠ 0) :
    dotFin d t v ≠ 0 := by
  rw [radical_pairing_eq_shadow_price_mul_net d t c v y₀ hdual hcv]
  exact Int.mul_ne_zero hy₀ hone

/-- **Shadow-price uniqueness from the radical pairing:**
    when `⟨c, v⟩ = 0`, any two dual certificates `(y₀, c)` and `(y₀', c')` for the
    same cost vector `t` on a radical direction with `⟨𝟙, v⟩ ≠ 0` force
    `y₀ * ⟨𝟙, v⟩ = y₀' * ⟨𝟙, v⟩`, and hence `y₀ = y₀'`. -/
theorem shadow_price_unique_of_radical (d : Nat) (t c₁ c₂ v : Nat → Int) (y₁ y₂ : Int)
    (hdual₁ : ∀ j, t j = y₁ + c₁ j)
    (hdual₂ : ∀ j, t j = y₂ + c₂ j)
    (hcv₁ : dotFin d c₁ v = 0)
    (hcv₂ : dotFin d c₂ v = 0)
    (hone : sumFin d v ≠ 0) :
    y₁ = y₂ := by
  have h1 := radical_pairing_eq_shadow_price_mul_net d t c₁ v y₁ hdual₁ hcv₁
  have h2 := radical_pairing_eq_shadow_price_mul_net d t c₂ v y₂ hdual₂ hcv₂
  have heq : y₁ * sumFin d v = y₂ * sumFin d v := h1.symm.trans h2
  exact Int.eq_of_mul_eq_mul_right hone heq

end QOU.Interactions
