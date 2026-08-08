/-
Copyright (c) 2026 litlfred. All rights reserved.

# The higher Leibniz rule for an abstract derivation (Mathlib gap)

Mathlib's `Mathlib/RingTheory/Derivation/Basic.lean` has `leibniz`,
`leibniz_pow`, `leibniz_inv`, `leibniz_div` — but **no iterate**: grep-confirmed
that `Nat.choose` does not occur anywhere under `Mathlib/RingTheory/Derivation/`,
and there is no `iterate_leibniz`. The analytic counterpart exists
(`iteratedDeriv`, Faà di Bruno), but nothing states the purely algebraic

    `Dⁿ(f·g) = Σ_{k≤n} C(n,k) · Dᵏf · D^{n−k}g`

for an abstract `Derivation R A A`.

**Why this file exists — the alien-calculus reason.**
[`AlienDerivation.lean`](../Mathlib/AlienDerivation.lean) advertises in its header
that it formalizes "3. The Stokes automorphism `= exp(Δ_ω)`" and "4. the bridge
identity". Neither was in the file. The obstacle is precisely this lemma: that
`exp(Δ)` is an algebra *automorphism* is the higher Leibniz rule summed against
`1/n!` — the binomial convolution `Σ_k C(n,k) x_k y_{n−k}` is exactly the Cauchy
product of the two exponential series. So the missing §3 was not a missing
paragraph; it was a missing lemma.

`exp_leibniz_of_sq_eq_zero` below is that consequence in the setting where it is
unconditional: `D` with `D² = 0`, where `exp(D) = 1 + D` and multiplicativity
holds precisely when the single cross-term `Df·Dg` vanishes. That is the
one-instanton truncation — the order at which
[`OneInstantonNormalization.lean`](../QBeta/OneInstantonNormalization.lean) works.
The full `exp(Δ)` statement needs a completion or local nilpotency to make the
series converge and is **not** claimed here.

§7c: generic `{R A : Type*} [CommSemiring R] [CommSemiring A] [Algebra R A]` —
no ordering, no `ℝ`. Sorry-free.

-- Ref: [ecalle1981] Fonctions résurgentes, tome I
-- Ref: [sauzin2014] https://arxiv.org/abs/1405.0356
-/
import Mathlib.RingTheory.Derivation.Basic
import Mathlib.Tactic

namespace QOU.MathlibExt.DerivationIterate

open Finset

variable {R A : Type*} [CommSemiring R] [CommSemiring A] [Algebra R A]

/-- **Higher Leibniz rule.**  Iterating a derivation `n` times across a product
    distributes binomially:

    `Dⁿ(f·g) = Σ_{k=0}^{n} C(n,k) · (Dᵏ f) · (D^{n−k} g)`.

    The `n = 1` case is `Derivation.leibniz`; the general case is the algebraic
    shadow of the analytic Leibniz formula, and it is what makes `exp(D)`
    multiplicative.

    Stated with `ℕ`-smul rather than a cast, so the inductive step needs only
    additivity of `D` (`map_nsmul`) and never `Derivation.map_natCast`. -/
theorem iterate_leibniz (D : Derivation R A A) (f g : A) : ∀ n : ℕ,
    (⇑D)^[n] (f * g)
      = ∑ k ∈ range (n + 1), (n.choose k) • ((⇑D)^[k] f * (⇑D)^[n - k] g) := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    -- Differentiate the inductive hypothesis termwise.
    have hstep : ∀ k ∈ range (n + 1),
        D ((n.choose k) • ((⇑D)^[k] f * (⇑D)^[n - k] g))
          = (n.choose k) • ((⇑D)^[k] f * (⇑D)^[n + 1 - k] g)
            + (n.choose k) • ((⇑D)^[k + 1] f * (⇑D)^[n + 1 - (k + 1)] g) := by
      intro k hk
      have hkn : k ≤ n := Nat.lt_succ_iff.mp (mem_range.mp hk)
      have e1 : n + 1 - k = (n - k) + 1 := by omega
      have e2 : n + 1 - (k + 1) = n - k := by omega
      rw [map_nsmul, D.leibniz, e1, e2, smul_add,
        Function.iterate_succ_apply' (⇑D) (n - k) g,
        Function.iterate_succ_apply' (⇑D) k f, smul_eq_mul, smul_eq_mul,
        mul_comm ((⇑D)^[n - k] g) (D ((⇑D)^[k] f))]
    rw [Function.iterate_succ_apply', ih, map_sum, Finset.sum_congr rfl hstep,
      Finset.sum_add_distrib]
    -- Pascal.  Peel `k = 0` off the first sum and the target, peel the top off
    -- the shifted sum, then match the middle range termwise.
    have hmid : (∑ k ∈ range n, (n.choose (k + 1))
                  • ((⇑D)^[k + 1] f * (⇑D)^[n + 1 - (k + 1)] g))
              + (∑ k ∈ range n, (n.choose k)
                  • ((⇑D)^[k + 1] f * (⇑D)^[n + 1 - (k + 1)] g))
              = ∑ k ∈ range n, ((n + 1).choose (k + 1))
                  • ((⇑D)^[k + 1] f * (⇑D)^[n + 1 - (k + 1)] g) := by
      rw [← Finset.sum_add_distrib]
      refine Finset.sum_congr rfl fun k _ => ?_
      rw [← add_smul, add_comm (n.choose (k + 1)) (n.choose k),
        ← Nat.choose_succ_succ n k]
    rw [Finset.sum_range_succ'
        (fun k => (n.choose k) • ((⇑D)^[k] f * (⇑D)^[n + 1 - k] g)) n,
      Finset.sum_range_succ
        (fun k => (n.choose k) • ((⇑D)^[k + 1] f * (⇑D)^[n + 1 - (k + 1)] g)) n,
      Finset.sum_range_succ'
        (fun k => ((n + 1).choose k) • ((⇑D)^[k] f * (⇑D)^[n + 1 - k] g)) (n + 1),
      Finset.sum_range_succ
        (fun k => ((n + 1).choose (k + 1))
          • ((⇑D)^[k + 1] f * (⇑D)^[n + 1 - (k + 1)] g)) n]
    simp only [Nat.choose_zero_right, Nat.choose_self, one_smul]
    rw [← hmid]
    abel

/-- **`exp(D)` is multiplicative exactly when the cross-term vanishes,
    at one-instanton order.**  For `D` with `D² = 0` the exponential truncates to
    `1 + D`, and

    `(1+D)(f·g) = (1+D)f · (1+D)g  ↔  Df · Dg = 0`.

    This is the honest one-instanton statement behind "the Stokes automorphism is
    `exp` of the alien derivative": at first order the automorphism property is
    *equivalent* to the vanishing of the two-instanton cross-term, which is what
    truncating at one instanton assumes.  The unconditional `exp(Δ)` automorphism
    needs a completion or local nilpotency for the series to converge, and is not
    claimed here.

    Note the `D² = 0` hypothesis is not needed for the equivalence itself —
    `1 + D` is the truncation whether or not `D` squares to zero — so it is not
    taken as an argument.  It is recorded in the name because that is the setting
    in which `1 + D` *is* `exp D`. -/
theorem exp_leibniz_iff_cross_vanishes {R A : Type*} [CommSemiring R] [CommRing A]
    [Algebra R A] (D : Derivation R A A) (f g : A) :
    (f * g + D (f * g) = (f + D f) * (g + D g)) ↔ D f * D g = 0 := by
  rw [D.leibniz, smul_eq_mul, smul_eq_mul,
    show (f + D f) * (g + D g) = f * g + (f * D g + g * D f) + D f * D g from by ring]
  exact left_eq_add

/-- **The `n = 1` case is Leibniz.**  Recorded as a consistency check that
    `iterate_leibniz` specialises correctly — a wrong binomial index would show
    up here. -/
theorem iterate_leibniz_one (D : Derivation R A A) (f g : A) :
    (⇑D)^[1] (f * g) = f * D g + g * D f := by
  simp [smul_eq_mul, D.leibniz f g]

/-- **The `n = 2` case, written out.**  `D²(fg) = D²f·g + 2·Df·Dg + f·D²g`.
    The middle coefficient `2` is the first place the binomial content is
    visible, so this is the smallest genuine test of `iterate_leibniz`. -/
theorem iterate_leibniz_two (D : Derivation R A A) (f g : A) :
    (⇑D)^[2] (f * g)
      = (⇑D)^[2] f * g + 2 • (D f * D g) + f * (⇑D)^[2] g := by
  rw [iterate_leibniz D f g 2]
  simp [Finset.sum_range_succ, Function.iterate_succ_apply']
  ring

end QOU.MathlibExt.DerivationIterate
