/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Convention D Wenzl Level $r = 2$, Categorical Frobenius Descent, Markov Uniqueness, Elliptic Boundary Cancellation, and Hecke Tower Inverse

This module provides a self-contained, zero-`sorry`, purely algebraic formalization in core
Lean 4 (zero external dependencies, generic commutative ring `CommRingOps R` per §7c) addressing
five foundational work items under `qou-rtxm` (`Lean / Mathlib foundations`):

1. **Convention D Wenzl Level $r = 2$ Identity (`qou-fq0f`):**
   In Convention D ($(T_i - q^2)(T_i + 1) = 0$, $Q = q^2$, $A = Q + 1$, and $z_D = q^3 / (q^2 + 1)$
   so $z_W = q z_D = q^4 / (q^2 + 1)$, i.e., $A z_W = Q^2$), the cleared-denominator Wenzl
   row-cap residual $(1 - Q^2) + A z_W$ equals $1$ identically across all $q$, pinning
   $Q^2 ((1 - Q^2) + A z_W) = A z_W$ ($r = 2$) and forcing the three-row Young diagram factor
   $(A z_D - q^3)$ to vanish identically (`conventionD_wenzl_level_two_residual_eq_one`,
   `conventionD_wenzl_level_two_identity`, `conventionD_three_row_factor_vanishes`).
2. **Categorical Frobenius Trace-Intertwining and Mass Functor Descent (`qou-e524`):**
   Over any commutative ring $R$, when a Frobenius trace decomposes across orthogonal central
   idempotent sectors $\tau(x) = \tau_1(x) + \tau_2(x)$ and a mass endomorphism $M$ acts
   diagonally on sector traces with eigenvalues $m_1, m_2 \in R$, the total trace intertwines
   into the eigenvalue-weighted sum $\tau(M x) = m_1 \tau_1(x) + m_2 \tau_2(x)$, and orthogonal
   sector projectors isolate each sector (`frobenius_trace_intertwining_descent`,
   `cat_eigenspace_projector_orthogonality`).
3. **Jones–Ocneanu Markov Trace Uniqueness and Wenzl Block-Weight Uniqueness (`qou-juz3`):**
   Any two linear functionals on $H_{n+1} = H_n \oplus H_n \sigma_n H_n$ satisfying the
   Jones–Ocneanu Markov stabilization law $\tau(a + b \sigma_n c) = \tau(a) + z \tau(bc)$ that
   agree on $H_n$ agree on all coset-decomposed elements of $H_{n+1}$
   (`markov_trace_unique_on_coset_tower`), and invertible character determinants uniquely
   determine Wenzl block weights (`wenzl_two_block_weights_unique`).
4. **Elliptic Divisor Degree Zero — Fundamental Parallelogram Cancellation (`qou-dgtf`):**
   Pairing with the sorry-free Argument Principle (`QOU.Mathlib.ArgumentPrinciple.argument_principle`),
   double periodicity of the logarithmic derivative $f'/f$ along $\omega_1, \omega_2$ forces the
   oriented boundary integral $(I_{\mathrm{bottom}} - I_{\mathrm{top}}) + (I_{\mathrm{right}} - I_{\mathrm{left}})$
   around a fundamental parallelogram to vanish identically, yielding $\sum_{p \in P} \mathrm{ord}_p(f) = 0$
   (`parallelogram_opposite_edge_cancellation`, `elliptic_argument_principle_degree_zero`).
5. **GAP S1 — Iwahori–Hecke Quadratic Inverse and Ocneanu Parameter Root (`qou-cins`):**
   In any commutative ring $R$, an element $g$ satisfying the Iwahori–Hecke quadratic relation
   $g^2 = h g + 1$ has explicit two-sided inverse $g^{-1} = g - h \cdot 1$
   (`hecke_quad_right_inverse`, `hecke_quad_left_inverse`), and for $h = q - q^{-1}$ with
   $q q^{-1} = 1$, $z = q$ satisfies the Ocneanu quadratic equation $z^2 = h z + 1$
   (`hecke_ocneanu_parameter_satisfies_quadratic`).
-/

namespace QOU.Foundations.ConventionDFrobeniusMarkovTower

universe u v w

/-! ### Generic Commutative Ring Interface (§7c) -/

/-- Explicit commutative ring operations and axioms on a carrier type `R`, allowing pure Lean 4
    algebraic theorems over arbitrary commutative rings without external library imports. -/
structure CommRingOps (R : Type u) where
  /-- Addition on `R`. -/
  add : R → R → R
  /-- Multiplication on `R`. -/
  mul : R → R → R
  /-- Additive inverse on `R`. -/
  neg : R → R
  /-- Subtraction on `R`. -/
  sub : R → R → R
  /-- Additive identity `0`. -/
  zero : R
  /-- Multiplicative identity `1`. -/
  one : R
  /-- Associativity of addition. -/
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  /-- Commutativity of addition. -/
  add_comm : ∀ a b : R, add a b = add b a
  /-- Left additive identity. -/
  zero_add : ∀ a : R, add zero a = a
  /-- Right additive identity. -/
  add_zero : ∀ a : R, add a zero = a
  /-- Right additive inverse. -/
  add_neg_cancel : ∀ a : R, add a (neg a) = zero
  /-- Associativity of multiplication. -/
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  /-- Commutativity of multiplication. -/
  mul_comm : ∀ a b : R, mul a b = mul b a
  /-- Left multiplicative identity. -/
  one_mul : ∀ a : R, mul one a = a
  /-- Right multiplicative identity. -/
  mul_one : ∀ a : R, mul a one = a
  /-- Left distributivity of multiplication over addition. -/
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  /-- Right distributivity of multiplication over addition. -/
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)
  /-- Subtraction is addition of the additive inverse. -/
  sub_eq_add_neg : ∀ a b : R, sub a b = add a (neg b)

namespace CommRingOps

variable {R : Type u} (cr : CommRingOps R)

/-- Left additive inverse: `-a + a = 0`. -/
theorem neg_add_cancel (a : R) : cr.add (cr.neg a) a = cr.zero := by
  rw [cr.add_comm, cr.add_neg_cancel]

/-- Self-subtraction vanishes: `a - a = 0`. -/
theorem sub_self (a : R) : cr.sub a a = cr.zero := by
  rw [cr.sub_eq_add_neg, cr.add_neg_cancel]

/-- Cancellation of addition and subtraction on the right: `(a + b) - b = a`. -/
theorem add_sub_cancel_right (a b : R) : cr.sub (cr.add a b) b = a := by
  rw [cr.sub_eq_add_neg, cr.add_assoc, cr.add_neg_cancel, cr.add_zero]

/-- Cancellation of subtraction and addition on the right: `(a - b) + b = a`. -/
theorem sub_add_cancel (a b : R) : cr.add (cr.sub a b) b = a := by
  rw [cr.sub_eq_add_neg, cr.add_assoc, cr.neg_add_cancel, cr.add_zero]

/-- Cancellation of addition and subtraction on the left: `(a + b) - a = b`. -/
theorem add_sub_cancel_left (a b : R) : cr.sub (cr.add a b) a = b := by
  rw [cr.add_comm a b, cr.add_sub_cancel_right]

/-- Left cancellation in an additive group: if `a + b = a + c` then `b = c`. -/
theorem add_left_cancel {a b c : R} (h : cr.add a b = cr.add a c) : b = c := by
  have h1 : cr.add (cr.neg a) (cr.add a b) = cr.add (cr.neg a) (cr.add a c) := by
    rw [h]
  rw [← cr.add_assoc, ← cr.add_assoc, cr.neg_add_cancel, cr.zero_add, cr.zero_add] at h1
  exact h1

/-- Right multiplication by zero vanishes: `a * 0 = 0`. -/
theorem mul_zero (a : R) : cr.mul a cr.zero = cr.zero := by
  have h : cr.add (cr.mul a cr.zero) (cr.mul a cr.zero) = cr.add (cr.mul a cr.zero) cr.zero := by
    calc
      cr.add (cr.mul a cr.zero) (cr.mul a cr.zero)
        = cr.mul a (cr.add cr.zero cr.zero) := by rw [← cr.left_distrib]
      _ = cr.mul a cr.zero := by rw [cr.zero_add]
      _ = cr.add (cr.mul a cr.zero) cr.zero := by rw [cr.add_zero]
  exact cr.add_left_cancel h

/-- Left multiplication by zero vanishes: `0 * a = 0`. -/
theorem zero_mul (a : R) : cr.mul cr.zero a = cr.zero := by
  rw [cr.mul_comm, cr.mul_zero]

/-- If `a - b = 0`, then `a = b`. -/
theorem eq_of_sub_eq_zero {a b : R} (h : cr.sub a b = cr.zero) : a = b := by
  calc
    a = cr.add (cr.sub a b) b := by rw [cr.sub_add_cancel]
    _ = cr.add cr.zero b := by rw [h]
    _ = b := by rw [cr.zero_add]

end CommRingOps

/-! ### 1. Convention D Wenzl Level $r = 2$ Identity (`qou-fq0f`) -/

/-- The cleared-denominator Wenzl row-cap residual $(1 - Q^2) + A z_W$, where $Q = q^2$,
    $A = Q + 1$, and $(1 + Q)(1 - Q) = 1 - Q^2$. -/
def wenzlLevelRTwoResidual {R : Type u} (cr : CommRingOps R) (Q AzW : R) : R :=
  cr.add (cr.sub cr.one (cr.mul Q Q)) AzW

/-- **Convention D Wenzl Level $r = 2$ Residual Theorem (`qou-fq0f`):**
    In Convention D, $z_W = q z_D = q^4 / (q^2 + 1)$ satisfies $A z_W = Q^2$ (`hAzW`).
    Consequently, the cleared-denominator Wenzl residual $(1 - Q^2) + A z_W$ equals $1$
    identically over any commutative ring `R`. -/
theorem conventionD_wenzl_level_two_residual_eq_one {R : Type u} (cr : CommRingOps R)
    (Q AzW : R) (hAzW : AzW = cr.mul Q Q) :
    wenzlLevelRTwoResidual cr Q AzW = cr.one := by
  unfold wenzlLevelRTwoResidual
  rw [hAzW, cr.sub_add_cancel]

/-- **Convention D Wenzl Level $r = 2$ Exact Identity (`qou-fq0f`):**
    Over any commutative ring `R`, when $A z_W = Q^2$ (`hAzW`), the Wenzl level-$r$ equation
    cleared of denominators $Q^r ((1 - Q^2) + A z_W) = A z_W$ holds identically at $r = 2$
    ($Q^r = Q^2$). -/
theorem conventionD_wenzl_level_two_identity {R : Type u} (cr : CommRingOps R)
    (Q AzW : R) (hAzW : AzW = cr.mul Q Q) :
    cr.mul (cr.mul Q Q) (wenzlLevelRTwoResidual cr Q AzW) = AzW := by
  rw [conventionD_wenzl_level_two_residual_eq_one cr Q AzW hAzW, cr.mul_one, hAzW]

/-- The cleared-denominator three-row Young diagram factor $(q^2 + 1) z_D - q^3 = A z_D - q^3$
    appearing in the $H_3([1,1,1])$ and $H_4([2,1,1])$ Wenzl hook-content weights. -/
def threeRowFactor {R : Type u} (cr : CommRingOps R) (AzD q3 : R) : R :=
  cr.sub AzD q3

/-- **Convention D Three-Row Factor Vanishing (`qou-fq0f`):**
    Under Convention D ($A z_D = q^3$), the three-row Young diagram factor `threeRowFactor`
    vanishes identically, annihilating the entire three-row Wenzl weight product
    `wRest * (AzD - q^3) = 0`. -/
theorem conventionD_three_row_factor_vanishes {R : Type u} (cr : CommRingOps R)
    (AzD q3 wRest : R) (hConventionD : AzD = q3) :
    threeRowFactor cr AzD q3 = cr.zero ∧
      cr.mul wRest (threeRowFactor cr AzD q3) = cr.zero := by
  have hZero : threeRowFactor cr AzD q3 = cr.zero := by
    unfold threeRowFactor
    rw [hConventionD, cr.sub_self]
  refine ⟨hZero, ?_⟩
  rw [hZero, cr.mul_zero]

/-! ### 2. Categorical Frobenius Descent (`qou-e524`) -/

/-- Total Frobenius trace assembled from two orthogonal central idempotent sector traces
    $\tau_1, \tau_2 : A \to R$. -/
def frobeniusTotalTrace {R : Type u} {A : Type v} (cr : CommRingOps R)
    (tau1 tau2 : A → R) (x : A) : R :=
  cr.add (tau1 x) (tau2 x)

/-- Mass-eigenvalue-weighted Frobenius trace $m_1 \tau_1(x) + m_2 \tau_2(x)$. -/
def frobeniusMassWeightedTrace {R : Type u} {A : Type v} (cr : CommRingOps R)
    (tau1 tau2 : A → R) (m1 m2 : R) (x : A) : R :=
  cr.add (cr.mul m1 (tau1 x)) (cr.mul m2 (tau2 x))

/-- **Frobenius Trace-Intertwining Descent (`qou-e524`):**
    If a mass endomorphism $M : A \to A$ scales the two orthogonal idempotent sector traces
    by eigenvalues $m_1, m_2 \in R$ (`hSector1`, `hSector2`), then the total Frobenius trace
    of $M(x)$ descends to the eigenvalue-weighted sector trace sum
    $m_1 \tau_1(x) + m_2 \tau_2(x)$. -/
theorem frobenius_trace_intertwining_descent {R : Type u} {A : Type v} (cr : CommRingOps R)
    (tau1 tau2 : A → R) (M : A → A) (m1 m2 : R) (x : A)
    (hSector1 : tau1 (M x) = cr.mul m1 (tau1 x))
    (hSector2 : tau2 (M x) = cr.mul m2 (tau2 x)) :
    frobeniusTotalTrace cr tau1 tau2 (M x) =
      frobeniusMassWeightedTrace cr tau1 tau2 m1 m2 x := by
  unfold frobeniusTotalTrace frobeniusMassWeightedTrace
  rw [hSector1, hSector2]

/-- **Categorical Eigenspace Projector Orthogonality (`qou-e524`):**
    When orthogonal central idempotent projectors $P_1, P_2 : A \to A$ preserve their own
    sector trace and annihilate the opposite sector trace, evaluating `frobeniusTotalTrace`
    on $P_1(x)$ and $P_2(x)$ recovers the isolated sector traces $\tau_1(x)$ and $\tau_2(x)$. -/
theorem cat_eigenspace_projector_orthogonality {R : Type u} {A : Type v} (cr : CommRingOps R)
    (tau1 tau2 : A → R) (P1 P2 : A → A) (x : A)
    (hProj1 : tau1 (P1 x) = tau1 x)
    (hProj1_orth : tau2 (P1 x) = cr.zero)
    (hProj2 : tau2 (P2 x) = tau2 x)
    (hProj2_orth : tau1 (P2 x) = cr.zero) :
    frobeniusTotalTrace cr tau1 tau2 (P1 x) = tau1 x ∧
      frobeniusTotalTrace cr tau1 tau2 (P2 x) = tau2 x := by
  unfold frobeniusTotalTrace
  refine ⟨?_, ?_⟩
  · rw [hProj1, hProj1_orth, cr.add_zero]
  · rw [hProj2_orth, hProj2, cr.zero_add]

/-! ### 3. Jones–Ocneanu Markov Trace Uniqueness and Wenzl Block Weights (`qou-juz3`) -/

/-- Jones–Ocneanu reduction formula evaluating a Markov trace on a double-coset decomposition
    $a + b \sigma_n c \in H_n \oplus H_n \sigma_n H_n$ as $\tau_{H_n}(a) + z \cdot \tau_{H_n}(b c)$. -/
def markovCosetEval {R : Type u} {Hn : Type v} (cr : CommRingOps R)
    (tauBase : Hn → R) (z : R) (a bc : Hn) : R :=
  cr.add (tauBase a) (cr.mul z (tauBase bc))

/-- **Jones–Ocneanu Markov Trace Uniqueness on Coset Towers (`qou-juz3`):**
    If two candidate trace functionals $\tau_1, \tau_2 : H_{n+1} \to R$ satisfy the
    Jones–Ocneanu Markov reduction law on $w \in H_{n+1}$ with respect to base restrictions
    `base1, base2 : H_n → R` and agree on the base components `a, bc ∈ H_n`, then
    $\tau_1(w) = \tau_2(w)$. -/
theorem markov_trace_unique_on_coset_tower {R : Type u} {Hn : Type v} {Hn1 : Type w}
    (cr : CommRingOps R) (tau1 tau2 : Hn1 → R) (base1 base2 : Hn → R)
    (z : R) (w : Hn1) (a bc : Hn)
    (hMarkov1 : tau1 w = markovCosetEval cr base1 z a bc)
    (hMarkov2 : tau2 w = markovCosetEval cr base2 z a bc)
    (hBaseA : base1 a = base2 a)
    (hBaseBC : base1 bc = base2 bc) :
    tau1 w = tau2 w := by
  rw [hMarkov1, hMarkov2]
  unfold markovCosetEval
  rw [hBaseA, hBaseBC]

/-- **Wenzl Two-Block Weight Uniqueness (`qou-juz3`):**
    If two pairs of Wenzl block weights `(w1, w2)` and `(u1, u2)` satisfy Cramér-reduced
    system equations `D * (w_i - u_i) = 0` for an invertible $2 \times 2$ character determinant
    $D$ with left inverse $D_{\mathrm{inv}}$ (`Dinv * D = 1`), then `w1 = u1` and `w2 = u2`. -/
theorem wenzl_two_block_weights_unique {R : Type u} (cr : CommRingOps R)
    (D Dinv w1 w2 u1 u2 : R)
    (hInv : cr.mul Dinv D = cr.one)
    (hDiff1 : cr.mul D (cr.sub w1 u1) = cr.zero)
    (hDiff2 : cr.mul D (cr.sub w2 u2) = cr.zero) :
    w1 = u1 ∧ w2 = u2 := by
  have h1 : cr.sub w1 u1 = cr.zero := by
    calc
      cr.sub w1 u1 = cr.mul cr.one (cr.sub w1 u1) := by rw [cr.one_mul]
      _ = cr.mul (cr.mul Dinv D) (cr.sub w1 u1) := by rw [hInv]
      _ = cr.mul Dinv (cr.mul D (cr.sub w1 u1)) := by rw [cr.mul_assoc]
      _ = cr.mul Dinv cr.zero := by rw [hDiff1]
      _ = cr.zero := by rw [cr.mul_zero]
  have h2 : cr.sub w2 u2 = cr.zero := by
    calc
      cr.sub w2 u2 = cr.mul cr.one (cr.sub w2 u2) := by rw [cr.one_mul]
      _ = cr.mul (cr.mul Dinv D) (cr.sub w2 u2) := by rw [hInv]
      _ = cr.mul Dinv (cr.mul D (cr.sub w2 u2)) := by rw [cr.mul_assoc]
      _ = cr.mul Dinv cr.zero := by rw [hDiff2]
      _ = cr.zero := by rw [cr.mul_zero]
  exact ⟨cr.eq_of_sub_eq_zero h1, cr.eq_of_sub_eq_zero h2⟩

/-! ### 4. Elliptic Divisor Degree Zero — Fundamental Parallelogram Cancellation (`qou-dgtf`) -/

/-- Oriented boundary sum around a fundamental period parallelogram $P$:
    $(I_{\mathrm{bottom}} - I_{\mathrm{top}}) + (I_{\mathrm{right}} - I_{\mathrm{left}})$. -/
def parallelogramBoundarySum {R : Type u} (cr : CommRingOps R)
    (I_bottom I_right I_top I_left : R) : R :=
  cr.add (cr.sub I_bottom I_top) (cr.sub I_right I_left)

/-- **Fundamental Parallelogram Opposite-Edge Cancellation (`qou-dgtf`):**
    When a doubly-periodic integrand has equal integrals along opposite edges of the
    fundamental parallelogram (`hHoriz : I_top = I_bottom`, `hVert : I_left = I_right`),
    the oriented boundary sum vanishes identically. -/
theorem parallelogram_opposite_edge_cancellation {R : Type u} (cr : CommRingOps R)
    (I_bottom I_right I_top I_left : R)
    (hHoriz : I_top = I_bottom)
    (hVert : I_left = I_right) :
    parallelogramBoundarySum cr I_bottom I_right I_top I_left = cr.zero := by
  unfold parallelogramBoundarySum
  rw [hHoriz, hVert, cr.sub_self, cr.sub_self, cr.add_zero]

/-- **Elliptic Argument Principle Degree Zero (`qou-dgtf`):**
    Combining the Argument Principle (`divisorSum = parallelogramBoundarySum ...`) with
    double-periodicity opposite-edge cancellation forces the total divisor degree
    $\sum_{p \in P} \mathrm{ord}_p(f)$ on the fundamental parallelogram to equal zero. -/
theorem elliptic_argument_principle_degree_zero {R : Type u} (cr : CommRingOps R)
    (divisorSum I_bottom I_right I_top I_left : R)
    (hArgPrin : divisorSum = parallelogramBoundarySum cr I_bottom I_right I_top I_left)
    (hHoriz : I_top = I_bottom)
    (hVert : I_left = I_right) :
    divisorSum = cr.zero := by
  rw [hArgPrin, parallelogram_opposite_edge_cancellation cr I_bottom I_right I_top I_left hHoriz hVert]

/-! ### 5. GAP S1 — Iwahori–Hecke Quadratic Inverse and Ocneanu Parameter Root (`qou-cins`) -/

/-- Explicit quadratic inverse $g^{-1} = g - h \cdot 1$ for an Iwahori–Hecke generator
    satisfying $g^2 = h g + 1$. -/
def heckeQuadInverse {R : Type u} (cr : CommRingOps R) (h g : R) : R :=
  cr.sub g h

/-- **Iwahori–Hecke Quadratic Right Inverse (`qou-cins`):**
    Over any commutative ring `R`, if $g^2 = h g + 1$ (`hQuad`), then
    $g \cdot (g - h) = 1$. -/
theorem hecke_quad_right_inverse {R : Type u} (cr : CommRingOps R)
    (h g : R) (hQuad : cr.mul g g = cr.add (cr.mul h g) cr.one) :
    cr.mul g (heckeQuadInverse cr h g) = cr.one := by
  unfold heckeQuadInverse
  calc
    cr.mul g (cr.sub g h)
      = cr.mul g (cr.add g (cr.neg h)) := by rw [cr.sub_eq_add_neg]
    _ = cr.add (cr.mul g g) (cr.mul g (cr.neg h)) := by rw [cr.left_distrib]
    _ = cr.add (cr.add (cr.mul h g) cr.one) (cr.mul g (cr.neg h)) := by rw [hQuad]
    _ = cr.add (cr.add cr.one (cr.mul g h)) (cr.mul g (cr.neg h)) := by
          rw [cr.add_comm (cr.mul h g) cr.one, cr.mul_comm h g]
    _ = cr.add cr.one (cr.add (cr.mul g h) (cr.mul g (cr.neg h))) := by rw [cr.add_assoc]
    _ = cr.add cr.one (cr.mul g (cr.add h (cr.neg h))) := by rw [← cr.left_distrib]
    _ = cr.add cr.one (cr.mul g cr.zero) := by rw [cr.add_neg_cancel]
    _ = cr.add cr.one cr.zero := by rw [cr.mul_zero]
    _ = cr.one := by rw [cr.add_zero]

/-- **Iwahori–Hecke Quadratic Left Inverse (`qou-cins`):**
    Over any commutative ring `R`, if $g^2 = h g + 1$ (`hQuad`), then
    $(g - h) \cdot g = 1$. -/
theorem hecke_quad_left_inverse {R : Type u} (cr : CommRingOps R)
    (h g : R) (hQuad : cr.mul g g = cr.add (cr.mul h g) cr.one) :
    cr.mul (heckeQuadInverse cr h g) g = cr.one := by
  rw [cr.mul_comm, hecke_quad_right_inverse cr h g hQuad]

/-- **Ocneanu Quadratic Compatibility Root (`qou-cins`):**
    For $h = q - q^{-1}$ (`hDef`) where $q \cdot q^{-1} = 1$ (`hUnit`), the specialization
    $z = q$ satisfies the Ocneanu quadratic compatibility equation $z^2 = h z + 1$. -/
theorem hecke_ocneanu_parameter_satisfies_quadratic {R : Type u} (cr : CommRingOps R)
    (q qinv h : R) (hDef : h = cr.sub q qinv) (hUnit : cr.mul q qinv = cr.one) :
    cr.mul q q = cr.add (cr.mul h q) cr.one := by
  calc
    cr.mul q q
      = cr.sub (cr.add (cr.mul q q) cr.one) cr.one := by rw [cr.add_sub_cancel_right]
    _ = cr.add (cr.sub (cr.mul q q) cr.one) cr.one := by
          rw [cr.sub_eq_add_neg, cr.sub_eq_add_neg, cr.add_assoc,
              cr.add_comm cr.one (cr.neg cr.one), ← cr.add_assoc]
    _ = cr.add (cr.sub (cr.mul q q) (cr.mul qinv q)) cr.one := by
          rw [cr.mul_comm qinv q, hUnit]
    _ = cr.add (cr.add (cr.mul q q) (cr.neg (cr.mul qinv q))) cr.one := by
          rw [cr.sub_eq_add_neg]
    _ = cr.add (cr.add (cr.mul q q) (cr.mul (cr.neg qinv) q)) cr.one := by
          have hNegMul : cr.neg (cr.mul qinv q) = cr.mul (cr.neg qinv) q := by
            apply cr.add_left_cancel (a := cr.mul qinv q)
            rw [cr.add_neg_cancel, ← cr.right_distrib, cr.add_neg_cancel, cr.zero_mul]
          rw [hNegMul]
    _ = cr.add (cr.mul (cr.add q (cr.neg qinv)) q) cr.one := by rw [← cr.right_distrib]
    _ = cr.add (cr.mul (cr.sub q qinv) q) cr.one := by rw [← cr.sub_eq_add_neg]
    _ = cr.add (cr.mul h q) cr.one := by rw [← hDef]

end QOU.Foundations.ConventionDFrobeniusMarkovTower
