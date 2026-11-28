import QOU.BraidsAndKnots.RationalAssociator.ExplicitLevelFour

/-!
# The level-`5` associator identities in an abstract `ℚ`-algebra

Companion of `ExplicitLevelFive.lean` (audit §17q). The three identities `inversion5`,
`hexagon5` and `pentagon5_lin` are stated in any `ℚ`-algebra, with the Drinfeld–Kohno
relations entering as rewriting rules; they are checked by expansion, truncation, rewriting to
normal form and `module`. They are slow to elaborate (a few minutes) and live in their own
module so that the `U4 5` file can be rebuilt quickly.

No `axiom`, no `sorry`, no analysis.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

section Abstract

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- Every word of length five in elements of `S` vanishes (right-associated form). -/
def Trunc5 (S : Set R) : Prop :=
  ∀ {x y z w v : R}, x ∈ S → y ∈ S → z ∈ S → w ∈ S → v ∈ S → x * (y * (z * (w * v))) = 0

/-- The commutator `x y − y x`. -/
def brk (x y : R) : R := x * y - y * x

/-- The degree-`4` part of `Φ₅(a, b)`. -/
def q4 (a b : R) : R :=
  (1 / 1152 : ℚ) • (brk a b * brk a b)
    - (1 / 1440 : ℚ) • brk a (brk a (brk a b)) - (1 / 5760 : ℚ) • brk b (brk a (brk a b))
    - (1 / 1440 : ℚ) • brk b (brk b (brk a b))

/-- The degree-`2` part of `Φ₅(a, b)`. -/
def u2 (a b : R) : R := (1 / 24 : ℚ) • brk a b

/-- `Φ₅(a, b) = 1 + u₂(a, b) + q₄(a, b)`. -/
def phi5 (a b : R) : R := 1 + u2 a b + q4 a b

/-- `exp(x/2)` truncated at degree `5`. -/
def expHalf5 (x : R) : R :=
  1 + (1 / 2 : ℚ) • x + (1 / 8 : ℚ) • (x * x) + (1 / 48 : ℚ) • (x * (x * x)) +
    (1 / 384 : ℚ) • (x * (x * (x * x)))

omit [Algebra ℚ R] in
/-- A relation `[x, y + z] = 0` read as the rewriting rule `y x ↦ x y + x z − z x`. -/
theorem rule_of_commute {x y z : R} (h : Commute x (y + z)) :
    y * x = x * y + x * z - z * x := by
  have e := h.eq
  rw [mul_add, add_mul] at e
  rw [← sub_eq_zero]
  have : y * x - (x * y + x * z - z * x) = -(x * y + x * z - (y * x + z * x)) := by abel
  rw [this, e, sub_self, neg_zero]

omit [Algebra ℚ R] in
theorem rule_of_commute_w {x y z : R} (h : Commute x (y + z)) (w : R) :
    y * (x * w) = x * (y * w) + x * (z * w) - z * (x * w) := by
  rw [← mul_assoc, rule_of_commute h]; simp only [add_mul, sub_mul, mul_assoc]

omit [Algebra ℚ R] in
theorem rule_of_commute' {x y : R} (h : Commute x y) (w : R) : y * (x * w) = x * (y * w) := by
  rw [← mul_assoc, h.eq.symm, mul_assoc]

/-- **Inversion modulo degree `5`.** -/
theorem inversion5 {a b : R} (h : Trunc5 ({a, b} : Set R)) : phi5 a b * phi5 b a = 1 := by
  unfold Trunc5 at h
  simp (config := { maxSteps := 50000000 }) only [phi5, u2, q4, brk, mul_add, add_mul, mul_sub, sub_mul,
    smul_mul_assoc, mul_smul_comm, one_mul, mul_one, mul_assoc, smul_zero, sub_zero, add_zero,
    mul_zero, smul_add, smul_sub, h, Set.mem_insert_iff, Set.mem_singleton_iff, true_or,
    or_true]
  module

set_option maxHeartbeats 0 in
/-- **The hexagon modulo degree `5`**, from the two three-strand rewriting rules. -/
theorem hexagon5 {p q r : R} (h : Trunc5 ({p, q, r} : Set R))
    (rp : ∀ w : R, r * (p * w) = p * (r * w) + p * (q * w) - q * (p * w))
    (rq : ∀ w : R, r * (q * w) = q * (r * w) + q * (p * w) - p * (q * w))
    (rp' : r * p = p * r + p * q - q * p) (rq' : r * q = q * r + q * p - p * q) :
    expHalf5 (q + r) =
      phi5 q p * expHalf5 q * phi5 r q * expHalf5 r * phi5 p r := by
  unfold Trunc5 at h
  simp (config := { maxSteps := 50000000 }) only [phi5, u2, q4, brk, expHalf5, mul_add, add_mul,
    mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, mul_assoc, smul_zero,
    sub_zero, add_zero, mul_zero, smul_add, smul_sub, h, Set.mem_insert_iff,
    Set.mem_singleton_iff, true_or, or_true]
  simp (config := { maxSteps := 50000000 }) only [rp, rq, rp', rq', mul_add, mul_sub, smul_add,
    smul_sub]
  module

set_option maxHeartbeats 0 in
/-- **The pentagon modulo degree `5`, with the cross terms of degree `≥ 5` removed**, from the
eleven four-strand rewriting rules. Writing `Φ = 1 + u + q` (`u` of degree `2`, `q` of degree
`4`), this is the pentagon read modulo degree `5`. -/
theorem pentagon5_lin {t12 t13 t14 t23 t24 t34 : R}
    (rPAw : ∀ w : R, t12 * (t14 * w) = t14 * (t12 * w) + t14 * (t24 * w) - t24 * (t14 * w))
    (rPA : t12 * t14 = t14 * t12 + t14 * t24 - t24 * t14)
    (rPBw : ∀ w : R, t12 * (t24 * w) = t24 * (t12 * w) + t24 * (t14 * w) - t14 * (t24 * w))
    (rPB : t12 * t24 = t24 * t12 + t24 * t14 - t14 * t24)
    (rPCw : ∀ w : R, t12 * (t34 * w) = t34 * (t12 * w))
    (rPC : t12 * t34 = t34 * t12)
    (rQAw : ∀ w : R, t13 * (t14 * w) = t14 * (t13 * w) + t14 * (t34 * w) - t34 * (t14 * w))
    (rQA : t13 * t14 = t14 * t13 + t14 * t34 - t34 * t14)
    (rQCw : ∀ w : R, t13 * (t34 * w) = t34 * (t13 * w) + t34 * (t14 * w) - t14 * (t34 * w))
    (rQC : t13 * t34 = t34 * t13 + t34 * t14 - t14 * t34)
    (rQBw : ∀ w : R, t13 * (t24 * w) = t24 * (t13 * w))
    (rQB : t13 * t24 = t24 * t13)
    (rRAw : ∀ w : R, t23 * (t14 * w) = t14 * (t23 * w))
    (rRA : t23 * t14 = t14 * t23)
    (rRBw : ∀ w : R, t23 * (t24 * w) = t24 * (t23 * w) + t24 * (t34 * w) - t34 * (t24 * w))
    (rRB : t23 * t24 = t24 * t23 + t24 * t34 - t34 * t24)
    (rRCw : ∀ w : R, t23 * (t34 * w) = t34 * (t23 * w) + t34 * (t24 * w) - t24 * (t34 * w))
    (rRC : t23 * t34 = t34 * t23 + t34 * t24 - t24 * t34)
    (rRPw : ∀ w : R, t23 * (t12 * w) = t12 * (t23 * w) + t12 * (t13 * w) - t13 * (t12 * w))
    (rRP : t23 * t12 = t12 * t23 + t12 * t13 - t13 * t12)
    (rRQw : ∀ w : R, t23 * (t13 * w) = t13 * (t23 * w) + t13 * (t12 * w) - t12 * (t13 * w))
    (rRQ : t23 * t13 = t13 * t23 + t13 * t12 - t12 * t13) :
    u2 t12 (t23 + t24) + q4 t12 (t23 + t24) + (u2 (t13 + t23) t34 + q4 (t13 + t23) t34) +
        u2 t12 (t23 + t24) * u2 (t13 + t23) t34 =
      u2 t23 t34 + q4 t23 t34 + (u2 (t12 + t13) (t24 + t34) + q4 (t12 + t13) (t24 + t34)) +
        (u2 t12 t23 + q4 t12 t23) + u2 t23 t34 * u2 (t12 + t13) (t24 + t34) +
        u2 t23 t34 * u2 t12 t23 + u2 (t12 + t13) (t24 + t34) * u2 t12 t23 := by
  simp (config := { maxSteps := 100000000 }) only [u2, q4, brk, mul_add, add_mul, mul_sub,
    sub_mul, smul_mul_assoc, mul_smul_comm, mul_assoc, smul_add, smul_sub]
  simp (config := { maxSteps := 100000000 }) only [rPAw, rPA, rPBw, rPB, rPCw, rPC, rQAw, rQA,
    rQCw, rQC, rQBw, rQB, rRAw, rRA, rRBw, rRB, rRCw, rRC, rRPw, rRP, rRQw, rRQ, mul_add, mul_sub,
    smul_add, smul_sub]
  module

omit [Algebra ℚ R] in
/-- Two factors `1 + u + q` multiply to `1 + u + q + u' + q' + u u'` once the products of
degree `≥ 6` vanish. -/
theorem mul_two_of {u q u' q' : R} (h1 : u * q' = 0) (h2 : q * u' = 0) (h3 : q * q' = 0) :
    (1 + u + q) * (1 + u' + q') = 1 + (u + q) + (u' + q') + u * u' := by
  simp only [mul_add, add_mul, one_mul, mul_one, h1, h2, h3, add_zero]; abel

end Abstract

end QOU.BraidsAndKnots.RationalAssociator
