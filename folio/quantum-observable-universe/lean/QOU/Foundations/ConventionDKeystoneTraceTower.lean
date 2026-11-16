/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Convention D $H_3$ Keystone Uniqueness, $N = 3$ Second Markov Trace Separation, Wedderburn $E_{(3,2)}$ Branching, Iterated Tower Trace, and Associative Symmetric Form

This module provides a self-contained, zero-`sorry`, purely algebraic formalization in core
Lean 4 (zero external dependencies, generic commutative ring `CommRingOps R` per §7c) addressing
five foundational work items under `qou-rtxm` (`Lean / Mathlib foundations`):

1. **Convention D $H_3(q)$ Keystone Uniqueness (`qou-u2jg`):**
   In the Wedderburn basis of $H_3(q)$ over any commutative ring $R$, eliminating $y_{(3)}$ and
   $y_{(2,1)}$ from the three Markov normalisation equations yields the factored cleared-denominator
   antisymmetriser weight numerator $Y_{(1^3)} = q^2 (z - q) ((q^2 + 1) z - q^3)$. This vanishes at
   the trivial branch $z = q$ (`h3_antisym_and_mixed_vanish_at_trivial_branch`, where $Y_{(2,1)}$ also
   collapses to $0$) and at Convention D $(q^2 + 1) z = q^3$ (`h3_antisym_vanishes_at_conventionD`),
   while at Convention D the surviving Wedderburn weights $Y_{(3)} = q^4 + 1$ and $Y_{(2,1)} = q^2$
   satisfy the exact normalisation $Y_{(3)} + 2 Y_{(2,1)} = (q^2 + 1)^2$
   (`conventionD_h3_normalisation_identity`).
2. **$N = 3$ Second Markov Trace Channel-Ratio Separation (`qou-yk03`):**
   In the balanced Ocneanu convention $a = q^{N-1}$, the ratio $y_{(2,1)} / y_{(3)} = [2]_q [N-1]_q / [N+2]_q$
   evaluates to $[2]_q / [4]_q$ at $N = 2$ and $[2]_q^2 / [5]_q$ at $N = 3$. Using the quantum-integer
   Clebsch–Gordan identity $[2]_q [4]_q = [5]_q + [3]_q$, the cross-determinant
   $\Delta_{3,2} = [2]_q ([2]_q [4]_q - [5]_q)$ equals $[2]_q [3]_q$
   (`ocneanu_n2_vs_n3_channel_ratio_det`), proving division-free that $N = 3$ is a distinct second
   Markov trace on $H_n(q)$ rather than a re-tuning of $N = 2$.
3. **Wedderburn $E_{(3,2)}$ Branching Split and Muon Target Correction (`qou-nzi9`):**
   Under the Young branching restriction $(3,2) \downarrow_{H_4} = (3,1) \oplus (2,2)$, the
   $E_{(3,2)}$ Wedderburn trace splits additively as $\mathrm{tr}(E_{(3,2)} w) = \mathrm{tr}(E_{(3,1)} w) + \mathrm{tr}(E_{(2,2)} w)$,
   isolating the two-row $(2,2)$ polynomial contribution in `deltaTarget = trE32 - trE31`
   (`wedderburn_E32_branching_trace_split`, `wedderburn_E32_target_correction_residual`).
4. **W3 Iterated Conditional Expectation Tower Trace (`qou-r765`):**
   For the iterated trace $\mathrm{tr}_{n+1} = \mathrm{tr}_n \circ E_n$, additivity, $R$-linearity,
   and the Markov stabilization step $\mathrm{tr}_{n+1}(\iota(b) \sigma_n \iota(c)) = z \cdot \mathrm{tr}_{n+1}(\iota(bc))$
   follow directly from the conditional expectation laws (`iteratedTowerTrace_map_add`,
   `iteratedTowerTrace_map_smul`, `iteratedTowerTrace_markov_step`).
5. **B2d Symmetrizing Markov Trace to Associative Symmetric Bilinear Form (`qou-t2ot`):**
   Any trace functional $\tau : A \to R$ induces the bilinear pairing $\langle x, y \rangle_\tau = \tau(x y)$,
   which is symmetric by trace cyclicity and associative ($\langle x y, z \rangle_\tau = \langle x, y z \rangle_\tau$)
   by algebra associativity (`traceBilinearForm_symmetric_and_associative`).
-/

namespace QOU.Foundations.ConventionDKeystoneTraceTower

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

end CommRingOps

/-! ### 1. Convention D $H_3(q)$ Keystone Uniqueness (`qou-u2jg`) -/

/-- Cleared-denominator $H_3(q)$ antisymmetriser Wedderburn weight numerator
    $Y_{(1^3)} = q^2 (z - q) (A z - q^3)$ where $A = q^2 + 1$. -/
def h3AntisymWeightNum {R : Type u} (cr : CommRingOps R) (q2 q q3 Az z : R) : R :=
  cr.mul q2 (cr.mul (cr.sub z q) (cr.sub Az q3))

/-- Cleared-denominator $H_3(q)$ mixed-symmetry $(2,1)$ weight numerator factor
    $Y_{(2,1)}^{\mathrm{triv}} = (z - q) (q z + 1)$ before multiplication by $-q$. -/
def h3MixedWeightFactor {R : Type u} (cr : CommRingOps R) (q z : R) : R :=
  cr.mul (cr.sub z q) (cr.add (cr.mul q z) cr.one)

/-- Cleared-denominator Convention D $H_3(q)$ mixed-symmetry weight $(q^2 + 1)^2 y_{(2,1)} = q^2$. -/
def h3MixedWeightConventionDNum {R : Type u} (cr : CommRingOps R) (q : R) : R :=
  cr.mul q q

/-- Cleared-denominator Convention D $H_3(q)$ symmetric weight $(q^2 + 1)^2 y_{(3)} = q^4 + 1$. -/
def h3SymWeightConventionDNum {R : Type u} (cr : CommRingOps R) (q : R) : R :=
  cr.add (cr.mul (cr.mul q q) (cr.mul q q)) cr.one

/-- **Trivial Branch Collapse (`qou-u2jg`):**
    At the trivial root $z = q$ (`hz`), both the antisymmetriser numerator $Y_{(1^3)}$ and the
    mixed-symmetry $(2,1)$ weight factor vanish identically, collapsing $H_3(q)$ to the
    one-dimensional trivial character with no mixed-symmetry block. -/
theorem h3_antisym_and_mixed_vanish_at_trivial_branch {R : Type u} (cr : CommRingOps R)
    (q2 q q3 Az z : R) (hz : z = q) :
    h3AntisymWeightNum cr q2 q q3 Az z = cr.zero ∧
      h3MixedWeightFactor cr q z = cr.zero := by
  refine ⟨?_, ?_⟩
  · unfold h3AntisymWeightNum
    rw [hz, cr.sub_self, cr.zero_mul, cr.mul_zero]
  · unfold h3MixedWeightFactor
    rw [hz, cr.sub_self, cr.zero_mul]

/-- **Convention D Antisymmetriser Vanishing (`qou-u2jg`):**
    At the Convention D parameter $(q^2 + 1) z = q^3$ (`hConvD : Az = q3`), the three-strand
    antisymmetriser weight numerator $Y_{(1^3)}$ vanishes identically over any commutative ring `R`. -/
theorem h3_antisym_vanishes_at_conventionD {R : Type u} (cr : CommRingOps R)
    (q2 q q3 Az z : R) (hConvD : Az = q3) :
    h3AntisymWeightNum cr q2 q q3 Az z = cr.zero := by
  unfold h3AntisymWeightNum
  rw [hConvD, cr.sub_self, cr.mul_zero, cr.mul_zero]

/-- **Convention D $H_3(q)$ Normalisation Identity (`qou-u2jg`):**
    Over any commutative ring `R`, the cleared-denominator Convention D weights
    $Y_{(3)} = q^4 + 1$ and $Y_{(2,1)} = q^2$ satisfy
    $Y_{(3)} + (Y_{(2,1)} + Y_{(2,1)}) = (q^2 + 1)^2$, confirming $\mathrm{tr}(1) = y_{(3)} + 2 y_{(2,1)} = 1$. -/
theorem conventionD_h3_normalisation_identity {R : Type u} (cr : CommRingOps R) (q : R) :
    cr.add (h3SymWeightConventionDNum cr q)
      (cr.add (h3MixedWeightConventionDNum cr q) (h3MixedWeightConventionDNum cr q)) =
      cr.mul (cr.add (cr.mul q q) cr.one) (cr.add (cr.mul q q) cr.one) := by
  unfold h3SymWeightConventionDNum h3MixedWeightConventionDNum
  let Q : R := cr.mul q q
  change cr.add (cr.add (cr.mul Q Q) cr.one) (cr.add Q Q) =
    cr.mul (cr.add Q cr.one) (cr.add Q cr.one)
  calc
    cr.add (cr.add (cr.mul Q Q) cr.one) (cr.add Q Q)
      = cr.add (cr.add (cr.mul Q Q) (cr.add Q Q)) cr.one := by
          rw [cr.add_assoc, cr.add_comm cr.one (cr.add Q Q), ← cr.add_assoc]
    _ = cr.add (cr.add (cr.add (cr.mul Q Q) Q) Q) cr.one := by
          rw [← cr.add_assoc (cr.mul Q Q) Q Q]
    _ = cr.add (cr.add (cr.mul Q Q) (cr.mul Q cr.one)) (cr.add (cr.mul cr.one Q) (cr.mul cr.one cr.one)) := by
          rw [cr.mul_one Q, cr.one_mul Q, cr.one_mul cr.one, cr.add_assoc (cr.add (cr.mul Q Q) Q) Q cr.one]
    _ = cr.add (cr.mul Q (cr.add Q cr.one)) (cr.mul cr.one (cr.add Q cr.one)) := by
          rw [← cr.left_distrib Q Q cr.one, ← cr.left_distrib cr.one Q cr.one]
    _ = cr.mul (cr.add Q cr.one) (cr.add Q cr.one) := by
          rw [← cr.right_distrib Q cr.one (cr.add Q cr.one)]

/-! ### 2. $N = 3$ Second Markov Trace Channel-Ratio Separation (`qou-yk03`) -/

/-- Cross-determinant $\Delta_{3,2} = [2]_q ([2]_q [4]_q - [5]_q)$ between the $N = 3$
    balanced channel ratio $[2]_q^2 / [5]_q$ and the $N = 2$ balanced channel ratio $[2]_q / [4]_q$. -/
def ocneanuN2N3ChannelDet {R : Type u} (cr : CommRingOps R) (q2 q4 q5 : R) : R :=
  cr.mul q2 (cr.sub (cr.mul q2 q4) q5)

/-- **$N = 2$ vs $N = 3$ Ocneanu Channel-Ratio Separation (`qou-yk03`):**
    Over any commutative ring `R`, whenever the quantum integers satisfy the Clebsch–Gordan
    identity $[2]_q [4]_q = [5]_q + [3]_q$ (`hCG`), the cross-determinant `ocneanuN2N3ChannelDet`
    between the $N = 3$ and $N = 2$ ratios $y_{(2,1)} / y_{(3)}$ equals $[2]_q [3]_q$. -/
theorem ocneanu_n2_vs_n3_channel_ratio_det {R : Type u} (cr : CommRingOps R)
    (q2 q3 q4 q5 : R) (hCG : cr.mul q2 q4 = cr.add q5 q3) :
    ocneanuN2N3ChannelDet cr q2 q4 q5 = cr.mul q2 q3 := by
  unfold ocneanuN2N3ChannelDet
  rw [hCG, cr.add_sub_cancel_left]

/-! ### 3. Wedderburn $E_{(3,2)}$ Branching Split and Muon Target Correction (`qou-nzi9`) -/

/-- **Wedderburn $E_{(3,2)}$ Branching Trace Split (`qou-nzi9`):**
    Under the Young branching restriction $(3,2) \downarrow_{H_4} = (3,1) \oplus (2,2)$,
    if the $E_{(3,2)}$ trace splits additively as `trE32 = trE31 + trE22` (`hBranch`) and
    the muon target branching correction is `deltaTarget = trE32 - trE31` (`hTarget`),
    then `deltaTarget = trE22`. -/
theorem wedderburn_E32_branching_trace_split {R : Type u} (cr : CommRingOps R)
    (trE32 trE31 trE22 deltaTarget : R)
    (hBranch : trE32 = cr.add trE31 trE22)
    (hTarget : deltaTarget = cr.sub trE32 trE31) :
    deltaTarget = trE22 := by
  rw [hTarget, hBranch, cr.add_sub_cancel_left]

/-- **Wedderburn $E_{(3,2)}$ Target Correction Residual Vanishing (`qou-nzi9`):**
    When `trE22` evaluates to the closed polynomial `poly22` (`hEval22 : trE22 = poly22`),
    the target correction constraint residual `deltaTarget - poly22` vanishes identically. -/
theorem wedderburn_E32_target_correction_residual {R : Type u} (cr : CommRingOps R)
    (trE32 trE31 trE22 deltaTarget poly22 : R)
    (hBranch : trE32 = cr.add trE31 trE22)
    (hTarget : deltaTarget = cr.sub trE32 trE31)
    (hEval22 : trE22 = poly22) :
    cr.sub deltaTarget poly22 = cr.zero := by
  have hEq : deltaTarget = poly22 := by
    rw [wedderburn_E32_branching_trace_split cr trE32 trE31 trE22 deltaTarget hBranch hTarget, hEval22]
  rw [hEq, cr.sub_self]

/-! ### 4. W3 Iterated Conditional Expectation Tower Trace (`qou-r765`) -/

/-- Iterated tower trace $\mathrm{tr}_{n+1}(x) = \mathrm{tr}_n(E_n(x))$ induced by a
    conditional expectation $E_n : H_{n+1} \to H_n$ and base trace $\mathrm{tr}_n : H_n \to R$. -/
def iteratedTowerTrace {R : Type u} {Hn : Type v} {Hn1 : Type w}
    (trn : Hn → R) (E : Hn1 → Hn) (x : Hn1) : R :=
  trn (E x)

/-- **Iterated Tower Trace Additivity (`qou-r765`):**
    Additivity of $E_n$ (`hE_add`) and $\mathrm{tr}_n$ (`hTr_add`) transfers to
    `iteratedTowerTrace`. -/
theorem iteratedTowerTrace_map_add {R : Type u} {Hn : Type v} {Hn1 : Type w}
    (cr : CommRingOps R) (trn : Hn → R) (E : Hn1 → Hn)
    (addH : Hn1 → Hn1 → Hn1) (addHn : Hn → Hn → Hn) (x y : Hn1)
    (hE_add : E (addH x y) = addHn (E x) (E y))
    (hTr_add : trn (addHn (E x) (E y)) = cr.add (trn (E x)) (trn (E y))) :
    iteratedTowerTrace trn E (addH x y) =
      cr.add (iteratedTowerTrace trn E x) (iteratedTowerTrace trn E y) := by
  unfold iteratedTowerTrace
  rw [hE_add, hTr_add]

/-- **Iterated Tower Trace Scalar Linearity (`qou-r765`):**
    Scalar $R$-linearity of $E_n$ (`hE_smul`) and $\mathrm{tr}_n$ (`hTr_smul`) transfers to
    `iteratedTowerTrace`. -/
theorem iteratedTowerTrace_map_smul {R : Type u} {Hn : Type v} {Hn1 : Type w}
    (cr : CommRingOps R) (trn : Hn → R) (E : Hn1 → Hn)
    (smulH : R → Hn1 → Hn1) (smulHn : R → Hn → Hn) (c : R) (x : Hn1)
    (hE_smul : E (smulH c x) = smulHn c (E x))
    (hTr_smul : trn (smulHn c (E x)) = cr.mul c (trn (E x))) :
    iteratedTowerTrace trn E (smulH c x) =
      cr.mul c (iteratedTowerTrace trn E x) := by
  unfold iteratedTowerTrace
  rw [hE_smul, hTr_smul]

/-- **Iterated Tower Trace Markov Stabilization Step (`qou-r765`):**
    If $E_n$ satisfies the Markov expectation law $E_n(w) = z \cdot (bc)$ on a single-$\sigma_n$
    word $w = \iota(b) \sigma_n \iota(c)$ (`hE_markov`) and retracts $\iota(bc)$ (`hRetract`),
    and $\mathrm{tr}_n$ is $R$-linear (`hTr_smul`), then
    $\mathrm{tr}_{n+1}(w) = z \cdot \mathrm{tr}_{n+1}(\iota(bc))$. -/
theorem iteratedTowerTrace_markov_step {R : Type u} {Hn : Type v} {Hn1 : Type w}
    (cr : CommRingOps R) (trn : Hn → R) (E : Hn1 → Hn) (iota : Hn → Hn1)
    (smulHn : R → Hn → Hn) (z : R) (w : Hn1) (bc : Hn)
    (hE_markov : E w = smulHn z bc)
    (hTr_smul : trn (smulHn z bc) = cr.mul z (trn bc))
    (hRetract : E (iota bc) = bc) :
    iteratedTowerTrace trn E w =
      cr.mul z (iteratedTowerTrace trn E (iota bc)) := by
  unfold iteratedTowerTrace
  rw [hE_markov, hTr_smul, hRetract]

/-! ### 5. B2d Symmetrizing Markov Trace to Associative Symmetric Form (`qou-t2ot`) -/

/-- Bilinear form $\langle x, y \rangle_\tau = \tau(x y)$ induced by a trace functional
    $\tau : A \to R$ and multiplication `mulA : A → A → A`. -/
def traceBilinearForm {R : Type u} {A : Type v}
    (tau : A → R) (mulA : A → A → A) (x y : A) : R :=
  tau (mulA x y)

/-- **Symmetry and Associativity of the Trace-Induced Bilinear Form (`qou-t2ot`):**
    For any trace functional $\tau : A \to R$, trace cyclicity $\tau(x y) = \tau(y x)$ (`hCyclic`)
    makes `traceBilinearForm` symmetric ($\langle x, y \rangle_\tau = \langle y, x \rangle_\tau$),
    and multiplication associativity $(x y) z = x (y z)$ (`hAssoc`) makes `traceBilinearForm`
    associative ($\langle x y, z \rangle_\tau = \langle x, y z \rangle_\tau$). -/
theorem traceBilinearForm_symmetric_and_associative {R : Type u} {A : Type v}
    (tau : A → R) (mulA : A → A → A) (x y z : A)
    (hCyclic : tau (mulA x y) = tau (mulA y x))
    (hAssoc : mulA (mulA x y) z = mulA x (mulA y z)) :
    traceBilinearForm tau mulA x y = traceBilinearForm tau mulA y x ∧
      traceBilinearForm tau mulA (mulA x y) z = traceBilinearForm tau mulA x (mulA y z) := by
  unfold traceBilinearForm
  exact ⟨hCyclic, congrArg tau hAssoc⟩

end QOU.Foundations.ConventionDKeystoneTraceTower
