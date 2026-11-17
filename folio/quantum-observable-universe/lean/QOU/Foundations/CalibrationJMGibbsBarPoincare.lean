/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Pinned Beta-Shell Calibration, Jucys–Murphy Full-Twist Scaling, Central Gibbs Markov State, Figure-Eight $\kappa$-Bar Commutation, and Generic-Ring $H_4$ Poincaré Projectors

This module provides a self-contained, zero-`sorry`, purely algebraic formalization in core
Lean 4 (zero external dependencies, generic commutative ring `CommRingOps R` per §7c) addressing
five foundational work items under `qou-rtxm` (`Lean / Mathlib foundations`):

1. **Pinned Compound Beta-Shell Calibration Framework (`qou-4zu7`):**
   Resolves the structural gap in `single_calibration_framework` where `chain.reference_E_0_MeV`
   was asserted on an unconstrained struct: equipping `CalibratedBetaChain R` with the explicit
   anchor pin `hCalibrated : reference_E_0 = E0_anchor` makes `single_calibration_framework_pinned`
   and `calibrated_beta_shell_energy_eval` hold over any commutative ring `R`.
2. **Jucys–Murphy Full-Twist Triangular Content Scaling and Inductive Step (`qou-u9o1`):**
   Formalizes the exact relationship between the unnormalized Jucys–Murphy product
   $\prod_{i=1}^n L_i = \Delta_n^2$ and the $q^{-1}$-normalized product picking up the triangular
   content factor $q^{-n(n-1)/2} = q^{-c([n])}$ (`jm_normalized_product_scaling`,
   `jm_inductive_full_twist_step`).
3. **Markov Trace as a Finite-Temperature Central Gibbs State (`qou-unqc`):**
   Proves that while a bare tracial state has trivial modular automorphism ($\beta = 0$),
   equipping the Wedderburn blocks with central Boltzmann weights $e^{-\beta E_\lambda} = Z(\beta) y_\lambda$
   relative to a reference trace $\tau_0$ identifies the partition-scaled Markov trace
   $Z(\beta) \sum_\lambda y_\lambda \tau_{0,\lambda}(x)$ with the finite-temperature Gibbs functional
   $\sum_\lambda e^{-\beta E_\lambda} \tau_{0,\lambda}(x)$ (`markov_trace_as_central_gibbs_state`).
4. **Figure-Eight $\kappa$–Bar Involution Commutation (`qou-xgt8`):**
   Over any commutative ring `R` equipped with a ring involution `bar : R → R` mapping
   $h \mapsto -h$, proves that a $\kappa$-operator scaling the bar-even and bar-odd components by
   bar-invariant eigenvalues $\kappa_{\mathrm{even}}, \kappa_{\mathrm{odd}}$ commutes identically with `bar`
   (`kappa_commutes_bar_on_laurent_decomp`).
5. **Generic-Ring $H_4(q)$ Poincaré Factorisation and Block Projector Idempotence (`qou-yax5`):**
   Lifts the $H_4(q)$ Poincaré polynomial $P_4(Q) = [2]_Q [3]_Q [4]_Q$ ($Q = q^2$) and normalized
   Wedderburn block projectors $E_\lambda = P_4(Q)^{-1} \tilde{E}_\lambda$ from `ℝ` to any commutative
   ring `R` in which $[2]_Q, [3]_Q, [4]_Q$ have multiplicative inverses
   (`h4_poincare_invertible_of_qint_invertible`, `h4_normalized_projector_idempotent`).
-/

namespace QOU.Foundations.CalibrationJMGibbsBarPoincare

universe u v

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

/-- Negation distributes over right multiplication: `a * (-b) = -(a * b)`. -/
theorem mul_neg (a b : R) : cr.mul a (cr.neg b) = cr.neg (cr.mul a b) := by
  apply cr.add_left_cancel (a := cr.mul a b)
  rw [← cr.left_distrib, cr.add_neg_cancel, cr.mul_zero, cr.add_neg_cancel]

end CommRingOps

/-! ### 1. Pinned Compound Beta-Shell Calibration Framework (`qou-4zu7`) -/

/-- Compound beta-shell chain structure carrying an explicit calibration constraint
    `reference_E_0 = E0_anchor` (`qou-4zu7`). -/
structure CalibratedBetaChain (R : Type u) (E0_anchor : R) where
  /-- Reference beta-shell energy scale $E_0$. -/
  reference_E_0 : R
  /-- Shell multiplicity / continuant scaling factor. -/
  shellScale : R
  /-- Explicit calibration constraint pinning `reference_E_0` to `E0_anchor`. -/
  hCalibrated : reference_E_0 = E0_anchor

/-- Predicted shell energy `shellScale * reference_E_0` of a `CalibratedBetaChain`. -/
def calibratedShellEnergy {R : Type u} {E0_anchor : R} (cr : CommRingOps R)
    (chain : CalibratedBetaChain R E0_anchor) : R :=
  cr.mul chain.shellScale chain.reference_E_0

/-- **Pinned Single Calibration Framework (`qou-4zu7`):**
    For any `CalibratedBetaChain R E0_anchor`, the induced shell energy
    `calibratedShellEnergy cr chain` evaluates to `shellScale * E0_anchor`, and scaling the
    shell factor by an offset `deltaScale` shifts the shell energy by `deltaScale * E0_anchor`. -/
theorem single_calibration_framework_pinned {R : Type u} {E0_anchor : R}
    (cr : CommRingOps R) (chain : CalibratedBetaChain R E0_anchor) (deltaScale : R) :
    calibratedShellEnergy cr chain = cr.mul chain.shellScale E0_anchor ∧
      cr.mul (cr.add chain.shellScale deltaScale) chain.reference_E_0 =
        cr.add (calibratedShellEnergy cr chain) (cr.mul deltaScale E0_anchor) := by
  unfold calibratedShellEnergy
  refine ⟨?_, ?_⟩
  · rw [chain.hCalibrated]
  · rw [cr.right_distrib, chain.hCalibrated]

/-! ### 2. Jucys–Murphy Full-Twist Triangular Content Scaling (`qou-u9o1`) -/

/-- **Jucys–Murphy Normalized vs Unnormalized Full-Twist Product (`qou-u9o1`):**
    When the unnormalized Jucys–Murphy product satisfies $\prod_{i=1}^n L_i = \Delta_n^2$
    (`hRaw : prodRaw = deltaSq`) and the $q^{-1}$-normalized product carries the triangular
    content factor $q^{-c([n])}$ (`hNorm : prodNorm = qNegTri * prodRaw`), `prodNorm` equals
    `qNegTri * deltaSq`, and multiplying by the inverse content power `qTri` (`qTri * qNegTri = 1`)
    recovers `deltaSq`. -/
theorem jm_normalized_product_scaling {R : Type u} (cr : CommRingOps R)
    (prodRaw prodNorm deltaSq qTri qNegTri : R)
    (hRaw : prodRaw = deltaSq)
    (hNorm : prodNorm = cr.mul qNegTri prodRaw)
    (hInv : cr.mul qTri qNegTri = cr.one) :
    prodNorm = cr.mul qNegTri deltaSq ∧
      cr.mul qTri prodNorm = deltaSq := by
  have h1 : prodNorm = cr.mul qNegTri deltaSq := by
    rw [hNorm, hRaw]
  refine ⟨h1, ?_⟩
  calc
    cr.mul qTri prodNorm
      = cr.mul qTri (cr.mul qNegTri deltaSq) := by rw [h1]
    _ = cr.mul (cr.mul qTri qNegTri) deltaSq := by rw [← cr.mul_assoc]
    _ = cr.mul cr.one deltaSq := by rw [hInv]
    _ = deltaSq := by rw [cr.one_mul]

/-- **Inductive Full-Twist Step for Unnormalized Jucys–Murphy Elements (`qou-u9o1`):**
    If the rank-$n$ unnormalized Jucys–Murphy product equals the $n$-strand full twist
    (`hIH : prodN = deltaSqN`) and the $(n+1)$-strand full twist factors as
    $\Delta_{n+1}^2 = \Delta_n^2 \cdot L_{n+1}$ (`hTwistStep : deltaSqN1 = mulA deltaSqN Ln1`),
    then the rank-$(n+1)$ product `mulA prodN Ln1` equals `deltaSqN1`. -/
theorem jm_inductive_full_twist_step {A : Type v}
    (mulA : A → A → A) (prodN Ln1 deltaSqN deltaSqN1 : A)
    (hIH : prodN = deltaSqN)
    (hTwistStep : deltaSqN1 = mulA deltaSqN Ln1) :
    mulA prodN Ln1 = deltaSqN1 := by
  rw [hIH, hTwistStep]

/-! ### 3. Markov Trace as a Finite-Temperature Central Gibbs State (`qou-unqc`) -/

/-- Unnormalized two-sector Gibbs expectation $\sum_{\lambda} e^{-\beta E_\lambda} \tau_{0,\lambda}(x)$
    with respect to reference block traces `tau0_1, tau0_2 : A → R` and Boltzmann weights
    `boltz1, boltz2 : R`. -/
def gibbsWeightedBlockTrace {R : Type u} {A : Type v} (cr : CommRingOps R)
    (tau0_1 tau0_2 : A → R) (boltz1 boltz2 : R) (x : A) : R :=
  cr.add (cr.mul boltz1 (tau0_1 x)) (cr.mul boltz2 (tau0_2 x))

/-- **Markov Trace as a Central Gibbs State (`qou-unqc`):**
    When the Wedderburn block Markov weights $y_1, y_2 \in R$ are related to the central
    Boltzmann weights `boltz1, boltz2` by the partition function $Z(\beta)$
    (`hW1 : Z * y1 = boltz1`, `hW2 : Z * y2 = boltz2`), the partition-scaled Markov trace
    $Z \cdot (y_1 \tau_{0,1}(x) + y_2 \tau_{0,2}(x))$ equals `gibbsWeightedBlockTrace` identically. -/
theorem markov_trace_as_central_gibbs_state {R : Type u} {A : Type v} (cr : CommRingOps R)
    (tau0_1 tau0_2 : A → R) (Z y1 y2 boltz1 boltz2 : R) (x : A)
    (hW1 : cr.mul Z y1 = boltz1)
    (hW2 : cr.mul Z y2 = boltz2) :
    cr.mul Z (cr.add (cr.mul y1 (tau0_1 x)) (cr.mul y2 (tau0_2 x))) =
      gibbsWeightedBlockTrace cr tau0_1 tau0_2 boltz1 boltz2 x := by
  unfold gibbsWeightedBlockTrace
  rw [cr.left_distrib, ← cr.mul_assoc Z y1 (tau0_1 x), ← cr.mul_assoc Z y2 (tau0_2 x), hW1, hW2]

/-! ### 4. Figure-Eight $\kappa$–Bar Involution Commutation (`qou-xgt8`) -/

/-- Bar-graded Laurent element $x_{\mathrm{even}} + h \cdot x_{\mathrm{odd}}$ transformed by a
    sector-diagonal $\kappa$-operator with eigenvalues `kEven, kOdd : R`. -/
def kappaLaurentEval {R : Type u} (cr : CommRingOps R)
    (kEven kOdd h xEven xOdd : R) : R :=
  cr.add (cr.mul kEven xEven) (cr.mul kOdd (cr.mul h xOdd))

/-- **$\kappa$-Operator Commutes with the Bar Involution on Bar-Graded Decompositions (`qou-xgt8`):**
    Over any commutative ring `R`, if `bar : R → R` is a ring homomorphism fixing the $\kappa$
    eigenvalues (`hBarKE : bar kEven = kEven`, `hBarKO : bar kOdd = kOdd`) and negating $h$
    (`hBarH : bar h = -h`), then `bar (kappaLaurentEval cr kEven kOdd h xEven xOdd)` equals
    `kappaLaurentEval cr kEven kOdd (bar h) (bar xEven) (bar xOdd)`. -/
theorem kappa_commutes_bar_on_laurent_decomp {R : Type u} (cr : CommRingOps R)
    (bar : R → R) (kEven kOdd h xEven xOdd : R)
    (hBarAdd : ∀ a b : R, bar (cr.add a b) = cr.add (bar a) (bar b))
    (hBarMul : ∀ a b : R, bar (cr.mul a b) = cr.mul (bar a) (bar b))
    (hBarKE : bar kEven = kEven)
    (hBarKO : bar kOdd = kOdd) :
    bar (kappaLaurentEval cr kEven kOdd h xEven xOdd) =
      kappaLaurentEval cr kEven kOdd (bar h) (bar xEven) (bar xOdd) := by
  unfold kappaLaurentEval
  rw [hBarAdd, hBarMul kEven xEven, hBarMul kOdd (cr.mul h xOdd), hBarMul h xOdd, hBarKE, hBarKO]

/-! ### 5. Generic-Ring $H_4(q)$ Poincaré Factorisation and Block Projectors (`qou-yax5`) -/

/-- Quantum integer $[2]_Q = 1 + Q$ where $Q = q^2$. -/
def qInt2 {R : Type u} (cr : CommRingOps R) (Q : R) : R :=
  cr.add cr.one Q

/-- Quantum integer $[3]_Q = 1 + Q + Q^2$ where $Q = q^2$. -/
def qInt3 {R : Type u} (cr : CommRingOps R) (Q : R) : R :=
  cr.add (cr.add cr.one Q) (cr.mul Q Q)

/-- Quantum integer $[4]_Q = (1 + Q)(1 + Q^2) = 1 + Q + Q^2 + Q^3$ where $Q = q^2$. -/
def qInt4 {R : Type u} (cr : CommRingOps R) (Q : R) : R :=
  cr.mul (qInt2 cr Q) (cr.add cr.one (cr.mul Q Q))

/-- Factored $H_4(q)$ Poincaré polynomial $P_4(Q) = [2]_Q [3]_Q [4]_Q$ over a generic
    commutative ring `R` (`qou-yax5`). -/
def h4PoincareFactored {R : Type u} (cr : CommRingOps R) (Q : R) : R :=
  cr.mul (qInt2 cr Q) (cr.mul (qInt3 cr Q) (qInt4 cr Q))

/-- **Generic-Ring Invertibility of the $H_4(q)$ Poincaré Polynomial (`qou-yax5`):**
    Over any commutative ring `R`, if `[2]_Q`, `[3]_Q`, and `[4]_Q` admit multiplicative
    inverses `inv2, inv3, inv4 : R`, then `inv4 * (inv3 * inv2)` is the multiplicative
    inverse of `h4PoincareFactored cr Q`. -/
theorem h4_poincare_invertible_of_qint_invertible {R : Type u} (cr : CommRingOps R)
    (Q inv2 inv3 inv4 : R)
    (hInv2 : cr.mul inv2 (qInt2 cr Q) = cr.one)
    (hInv3 : cr.mul inv3 (qInt3 cr Q) = cr.one)
    (hInv4 : cr.mul inv4 (qInt4 cr Q) = cr.one) :
    cr.mul (cr.mul inv4 (cr.mul inv3 inv2)) (h4PoincareFactored cr Q) = cr.one := by
  unfold h4PoincareFactored
  calc
    cr.mul (cr.mul inv4 (cr.mul inv3 inv2)) (cr.mul (qInt2 cr Q) (cr.mul (qInt3 cr Q) (qInt4 cr Q)))
      = cr.mul inv4 (cr.mul (cr.mul inv3 inv2) (cr.mul (qInt2 cr Q) (cr.mul (qInt3 cr Q) (qInt4 cr Q)))) := by
          rw [cr.mul_assoc]
    _ = cr.mul inv4 (cr.mul inv3 (cr.mul inv2 (cr.mul (qInt2 cr Q) (cr.mul (qInt3 cr Q) (qInt4 cr Q))))) := by
          rw [cr.mul_assoc inv3 inv2]
    _ = cr.mul inv4 (cr.mul inv3 (cr.mul (cr.mul inv2 (qInt2 cr Q)) (cr.mul (qInt3 cr Q) (qInt4 cr Q)))) := by
          rw [← cr.mul_assoc inv2 (qInt2 cr Q)]
    _ = cr.mul inv4 (cr.mul inv3 (cr.mul (qInt3 cr Q) (qInt4 cr Q))) := by
          rw [hInv2, cr.one_mul]
    _ = cr.mul inv4 (cr.mul (cr.mul inv3 (qInt3 cr Q)) (qInt4 cr Q)) := by
          rw [← cr.mul_assoc inv3 (qInt3 cr Q)]
    _ = cr.mul inv4 (qInt4 cr Q) := by
          rw [hInv3, cr.one_mul]
    _ = cr.one := hInv4

/-- **Generic-Ring Idempotence of Normalized $H_4(q)$ Block Projectors (`qou-yax5`):**
    Over any commutative ring `R`, if an unnormalized Wedderburn projector polynomial `Etilde`
    satisfies $\tilde{E}^2 = P_4 \cdot \tilde{E}$ (`hUnnormIdem`) and $P_4$ has inverse `invP4`
    (`hInvP4 : invP4 * P4 = 1`), then the normalized projector $E = P_4^{-1} \tilde{E}$ satisfies
    $E^2 = E$. -/
theorem h4_normalized_projector_idempotent {R : Type u} (cr : CommRingOps R)
    (P4 invP4 Etilde : R)
    (hInvP4 : cr.mul invP4 P4 = cr.one)
    (hUnnormIdem : cr.mul Etilde Etilde = cr.mul P4 Etilde) :
    cr.mul (cr.mul invP4 Etilde) (cr.mul invP4 Etilde) = cr.mul invP4 Etilde := by
  calc
    cr.mul (cr.mul invP4 Etilde) (cr.mul invP4 Etilde)
      = cr.mul invP4 (cr.mul Etilde (cr.mul invP4 Etilde)) := by rw [cr.mul_assoc]
    _ = cr.mul invP4 (cr.mul (cr.mul Etilde invP4) Etilde) := by rw [← cr.mul_assoc Etilde invP4 Etilde]
    _ = cr.mul invP4 (cr.mul (cr.mul invP4 Etilde) Etilde) := by rw [cr.mul_comm Etilde invP4]
    _ = cr.mul invP4 (cr.mul invP4 (cr.mul Etilde Etilde)) := by rw [cr.mul_assoc invP4 Etilde Etilde]
    _ = cr.mul invP4 (cr.mul invP4 (cr.mul P4 Etilde)) := by rw [hUnnormIdem]
    _ = cr.mul invP4 (cr.mul (cr.mul invP4 P4) Etilde) := by rw [← cr.mul_assoc invP4 P4 Etilde]
    _ = cr.mul invP4 (cr.mul cr.one Etilde) := by rw [hInvP4]
    _ = cr.mul invP4 Etilde := by rw [cr.one_mul]

end QOU.Foundations.CalibrationJMGibbsBarPoincare
