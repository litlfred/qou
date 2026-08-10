/-
# The cyclic quantum dilogarithm — shift law and class-difference corollary

Formalize-first backbone for the ε_m descent implementation (bean
qou-y3xv increment 2; program audit
`docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md`
Addenda 12–16). The compute layers (merged PRs #4490, #4533, #4588)
verified these laws numerically at every level — finite fields, the
Q₂₅ place, and unramified Kummer fields to degree 96; this file
proves them once, generically, so the descent code has a proved
backbone rather than a per-run check.

* **`cyclicQDilog`** — `D_ζ(x) = ∏_{k<m} (1 − ζ^k x)^k` (CGZ
  arXiv:1712.04887 eqn (8); the `k = 0` factor is `1`, so
  `Finset.range m` is the natural index set). Over a GENERIC
  commutative ring per §7c — no archimedean or p-adic structure
  enters the algebra.
* **`cyclicQDilog_shift`** — the CGZ identity (21), the engine of
  their Lemma 2.4(a): with `ζ^m = 1`, the cyclotomic factorization
  `∏_{k<m}(1 − ζ^k y) = 1 − y^m` (what "ζ is a primitive m-th root"
  buys in any concrete instance — kept as an explicit hypothesis so
  the ring stays generic and the statement honest), and `r ≤ m`
  (root choices are mod m, so this is the only range the descent
  uses):

      (1 − x^m)^r · D_ζ(ζ^r x) = (∏_{k<r} (1 − ζ^k x)^m) · D_ζ(x).

* **`cyclicQDilog_class_shift`** — the class-difference law: pushing
  (21) through any monoid hom `χ : R →* M` into a commutative monoid
  that kills m-th powers gives

      χ(1 − x^m)^r · χ(D_ζ(ζ^r x)) = χ(D_ζ(x)),

  i.e. the root-difference law `Δclass = −r·class(1−X)` that every
  probe verified numerically (base place, Kummer level, global
  symbols). This is the exact statement the equivariant-splicing
  descent consumes.

HONESTY (STRICT): sorry-free, no axioms, no `decide`; hypotheses are
the genuine inputs (root-of-unity law + cyclotomic factorization),
not the conclusions; nothing wired.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.Ring

namespace QOU.Machinery.CyclicQuantumDilog

open Finset

variable {R : Type*} [CommRing R]

/-- The cyclic quantum dilogarithm `D_ζ(x) = ∏_{k<m} (1 − ζ^k x)^k`
(CGZ eqn (8)); the `k = 0` factor is `1`. -/
def cyclicQDilog (m : ℕ) (ζ x : R) : R :=
  ∏ k ∈ Finset.range m, (1 - ζ ^ k * x) ^ k

/-- **The CGZ shift identity (21)**, generically: with `ζ^m = 1`, the
cyclotomic factorization, and `r ≤ m`,
`(1 − x^m)^r · D_ζ(ζ^r x) = (∏_{k<r}(1 − ζ^k x)^m) · D_ζ(x)`. -/
theorem cyclicQDilog_shift (m r : ℕ) (ζ x : R) (hζ : ζ ^ m = 1)
    (hcyc : ∀ y : R, ∏ k ∈ Finset.range m, (1 - ζ ^ k * y) = 1 - y ^ m)
    (hr : r ≤ m) :
    (1 - x ^ m) ^ r * cyclicQDilog m ζ (ζ ^ r * x)
      = (∏ k ∈ Finset.range r, (1 - ζ ^ k * x) ^ m) * cyclicQDilog m ζ x := by
  have harg : ∀ k : ℕ, ζ ^ k * (ζ ^ r * x) = ζ ^ (k + r) * x := by
    intro k; rw [pow_add]; ring
  -- ∏_{k<m} (1 − ζ^{k+r} x) = 1 − x^m  (shift the cyclotomic law)
  have hshiftcyc : ∏ k ∈ Finset.range m, (1 - ζ ^ (k + r) * x) = 1 - x ^ m := by
    calc ∏ k ∈ Finset.range m, (1 - ζ ^ (k + r) * x)
        = ∏ k ∈ Finset.range m, (1 - ζ ^ k * (ζ ^ r * x)) :=
          Finset.prod_congr rfl fun k _ => by rw [harg k]
      _ = 1 - (ζ ^ r * x) ^ m := hcyc (ζ ^ r * x)
      _ = 1 - x ^ m := by
          rw [mul_pow, ← pow_mul, mul_comm r m, pow_mul, hζ, one_pow, one_mul]
  -- LHS = ∏_{k<m} (1 − ζ^{k+r} x)^{k+r}
  have hmerge :
      (1 - x ^ m) ^ r * cyclicQDilog m ζ (ζ ^ r * x)
        = ∏ k ∈ Finset.range m, (1 - ζ ^ (k + r) * x) ^ (k + r) := by
    unfold cyclicQDilog
    rw [← hshiftcyc, ← Finset.prod_pow, ← Finset.prod_mul_distrib]
    refine Finset.prod_congr rfl fun k _ => ?_
    rw [harg k, pow_add]
    ring
  -- reindex j = k + r
  have hreindex :
      ∏ k ∈ Finset.range m, (1 - ζ ^ (k + r) * x) ^ (k + r)
        = ∏ j ∈ Finset.Ico r (m + r), (1 - ζ ^ j * x) ^ j := by
    rw [Finset.prod_Ico_eq_prod_range, Nat.add_sub_cancel]
    exact Finset.prod_congr rfl fun k _ => by rw [Nat.add_comm r k]
  -- split at m and fold the wrap-around ζ^{m+t} = ζ^t
  have hwrap :
      ∏ j ∈ Finset.Ico m (m + r), (1 - ζ ^ j * x) ^ j
        = ∏ t ∈ Finset.range r, (1 - ζ ^ t * x) ^ (m + t) := by
    rw [Finset.prod_Ico_eq_prod_range, Nat.add_sub_cancel_left]
    refine Finset.prod_congr rfl fun t _ => ?_
    rw [Nat.add_comm m t, pow_add ζ t m, hζ, mul_one, Nat.add_comm t m]
  have hsplit :
      ∏ j ∈ Finset.Ico r (m + r), (1 - ζ ^ j * x) ^ j
        = (∏ j ∈ Finset.Ico r m, (1 - ζ ^ j * x) ^ j)
          * ∏ t ∈ Finset.range r, (1 - ζ ^ t * x) ^ (m + t) := by
    rw [← Finset.prod_Ico_consecutive _ hr (Nat.le_add_right m r), hwrap]
  -- assemble the right-hand side the same way
  have hrhs :
      (∏ k ∈ Finset.range r, (1 - ζ ^ k * x) ^ m) * cyclicQDilog m ζ x
        = (∏ j ∈ Finset.Ico r m, (1 - ζ ^ j * x) ^ j)
          * ∏ t ∈ Finset.range r, (1 - ζ ^ t * x) ^ (m + t) := by
    unfold cyclicQDilog
    rw [← Finset.prod_range_mul_prod_Ico (fun k => (1 - ζ ^ k * x) ^ k) hr]
    have hlow :
        (∏ k ∈ Finset.range r, (1 - ζ ^ k * x) ^ m)
            * ∏ k ∈ Finset.range r, (1 - ζ ^ k * x) ^ k
          = ∏ t ∈ Finset.range r, (1 - ζ ^ t * x) ^ (m + t) := by
      rw [← Finset.prod_mul_distrib]
      exact Finset.prod_congr rfl fun t _ => by rw [← pow_add]
    calc (∏ k ∈ Finset.range r, (1 - ζ ^ k * x) ^ m)
          * ((∏ k ∈ Finset.range r, (1 - ζ ^ k * x) ^ k)
            * ∏ k ∈ Finset.Ico r m, (1 - ζ ^ k * x) ^ k)
        = ((∏ k ∈ Finset.range r, (1 - ζ ^ k * x) ^ m)
            * ∏ k ∈ Finset.range r, (1 - ζ ^ k * x) ^ k)
          * ∏ k ∈ Finset.Ico r m, (1 - ζ ^ k * x) ^ k := by ring
      _ = (∏ t ∈ Finset.range r, (1 - ζ ^ t * x) ^ (m + t))
          * ∏ k ∈ Finset.Ico r m, (1 - ζ ^ k * x) ^ k := by rw [hlow]
      _ = (∏ j ∈ Finset.Ico r m, (1 - ζ ^ j * x) ^ j)
          * ∏ t ∈ Finset.range r, (1 - ζ ^ t * x) ^ (m + t) := by ring
  rw [hmerge, hreindex, hsplit, hrhs]

/-- **The class-difference law** (the χ-shadow of (21)): for any
monoid hom `χ : R →* M` into a commutative monoid killing m-th powers,
`χ(1 − x^m)^r · χ(D_ζ(ζ^r x)) = χ(D_ζ(x))` — the root-difference law
`Δclass = −r·class(1−X)` verified numerically by every ε_m probe. -/
theorem cyclicQDilog_class_shift {M : Type*} [CommMonoid M]
    (χ : R →* M) (m r : ℕ) (ζ x : R) (hζ : ζ ^ m = 1)
    (hcyc : ∀ y : R, ∏ k ∈ Finset.range m, (1 - ζ ^ k * y) = 1 - y ^ m)
    (hr : r ≤ m) (hkill : ∀ y : R, χ (y ^ m) = 1) :
    χ (1 - x ^ m) ^ r * χ (cyclicQDilog m ζ (ζ ^ r * x))
      = χ (cyclicQDilog m ζ x) := by
  have h := congrArg χ (cyclicQDilog_shift m r ζ x hζ hcyc hr)
  rw [map_mul, map_pow, map_mul, map_prod] at h
  have hone : ∀ k ∈ Finset.range r, χ ((1 - ζ ^ k * x) ^ m) = 1 := by
    intro k _; exact hkill _
  rw [Finset.prod_congr rfl hone, Finset.prod_const_one, one_mul] at h
  exact h

end QOU.Machinery.CyclicQuantumDilog
