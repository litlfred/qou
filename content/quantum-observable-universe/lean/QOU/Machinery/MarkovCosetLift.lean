import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Ring.Finset
import QOU.Machinery.MarkovInductiveCyclicity

/-!
# The coset-sum lift for the inductive Markov-trace cyclicity

`QOU.Machinery.MarkovInductiveCyclicity` proves `cyclic_two_g` — the two-`g` case
of the inductive step — conditionally on two interfaces:

* `hgwg` — the traced double-`g` reduction
  `tr(x·g·w·g·y) = tr(x·(E w)·y) + z·h̄·tr(x·w·y)`, and
* `hCE`  — conditional-expectation compatibility `tr(a·x) = tr(a·(E x))`.

That module grounds each on a **single** `H_{n-1}`-coset (`gwg_trace_lower`,
`gwg_trace_mid`, `ce_trace_mid`) and then says, in its own header:

> The **only** step not mechanised in Lean is the linear lift of the two
> single-coset grounding lemmas to the general `E` on an arbitrary
> `w = a + Σᵢ bᵢ·f·cᵢ` … That lift is standard and mechanical; it is why
> `hgwg`/`hCE` are taken as the (grounded) reduction interface rather than
> re-derived from the coset direct-sum inside this file.

**This module is that lift.** `gwg_trace_cosetSum` and `ce_trace_cosetSum` derive
the two interfaces for a `w` presented in coset form, from the per-coset lemmas
plus linearity of `tr`.

## What this does and does not close

It closes the step the header names, and nothing beyond it. `cyclic_two_g` remains
a conditional theorem: instantiating it still requires exhibiting a concrete tower
— an algebra, a `memB`, a trace with the Markov property, and a decomposition of
each `w` into the coset form assumed here. **Conditional-proved is not
premise-established** (AGENTS.md), and this module does not change that; it removes
one named gap between the grounding lemmas and the interface.

## Why `[Algebra R A]`

`MarkovInductiveCyclicity` works over `[CommRing R] [Ring A]` with no action of `R`
on `A`. That is precisely why `E` had to stay abstract there: `E(b·f·c) = z·b·c` is
not expressible without a scalar action, so the traced identity could only be
*assumed*, not *computed*. Adding `[Algebra R A]` makes `z • (b * c)` a term and the
lift statable. It weakens nothing — every intended instance (a Hecke algebra over
its coefficient ring) has it.
-/

namespace QOU.Machinery.MarkovInductive

variable {R A : Type*} [CommRing R] [Ring A]

/-- `tr` is additive over a `Finset` sum, from binary additivity plus `tr 0 = 0`.

    Stated for a bare additive `tr : A → R` rather than a bundled `AddMonoidHom`,
    to match the interface style the rest of this development uses: the trace
    arrives as a function with hypotheses, not as a structure. -/
theorem tr_finset_sum (tr : A → R)
    (htr_add : ∀ p q : A, tr (p + q) = tr p + tr q) (htr_zero : tr 0 = 0)
    {ι : Type*} (s : Finset ι) (F : ι → A) :
    tr (∑ i ∈ s, F i) = ∑ i ∈ s, tr (F i) := by
  classical
  induction s using Finset.induction with
  | empty => simpa using htr_zero
  | insert i s hi ih => rw [Finset.sum_insert hi, htr_add, ih, Finset.sum_insert hi]

section Algebra

variable [Algebra R A] (memB : A → Prop)

/-- **Lower coset, normalised into the `E`-shape.** `gwg_trace_lower` produces
    `tr(x·a·y) + z·tr(x·a·hh·y)`; with the Hecke element `hh` being the scalar
    `h̄` (i.e. `hh = h̄ • 1`), the second term is `z·h̄·tr(x·a·y)`, which is the
    `hgwg` shape with `E a = a`. -/
theorem gwg_trace_lower_shape (tr : A → R) (g : A) (z hbar : R) (a x y : A)
    (htr_add : ∀ p q : A, tr (p + q) = tr p + tr q)
    (htr_smul : ∀ (r : R) (p : A), tr (r • p) = r * tr p)
    (hfar : g * a = a * g) (hhecke : g * g = 1 + (hbar • (1 : A)) * g)
    (hmarkov : ∀ s t : A, memB s → memB t → tr (s * g * t) = z * tr (s * t))
    (hxah : memB (x * a * (hbar • (1 : A)))) (hy : memB y) :
    tr (x * (g * a * g) * y) = tr (x * a * y) + z * hbar * tr (x * a * y) := by
  rw [gwg_trace_lower memB tr g z (hbar • (1 : A)) a x y htr_add hfar hhecke
        hmarkov hxah hy]
  have e : x * a * (hbar • (1 : A)) * y = hbar • (x * a * y) := by
    simp
  rw [e, htr_smul]
  ring

/-- **Mid coset, normalised into the `E`-shape.** `gwg_trace_mid` produces
    `z·tr(x·b·f·f·c·y)`; the Hecke relation `f² = 1 + h̄·f` splits it as
    `tr(x·(z • (b·c))·y) + z·h̄·tr(x·(b·f·c)·y)` — the `hgwg` shape with
    `E(b·f·c) = z • (b·c)`. -/
theorem gwg_trace_mid_shape (tr : A → R) (g f : A) (z hbar : R) (b c x y : A)
    (htr_add : ∀ p q : A, tr (p + q) = tr p + tr q)
    (htr_smul : ∀ (r : R) (p : A), tr (r • p) = r * tr p)
    (hfarb : g * b = b * g) (hfarc : c * g = g * c) (hbraid : g * f * g = f * g * f)
    (hfsq : f * f = 1 + hbar • f)
    (hmarkov : ∀ s t : A, memB s → memB t → tr (s * g * t) = z * tr (s * t))
    (hxbf : memB (x * b * f)) (hfcy : memB (f * c * y)) :
    tr (x * (g * (b * f * c) * g) * y)
      = tr (x * (z • (b * c)) * y) + z * hbar * tr (x * (b * f * c) * y) := by
  rw [gwg_trace_mid memB tr g f z b c x y hfarb hfarc hbraid hmarkov hxbf hfcy]
  have e : x * b * f * f * c * y = x * b * c * y + hbar • (x * b * f * c * y) := by
    rw [show x * b * f * f * c * y = x * b * (f * f) * c * y from by
          simp only [mul_assoc], hfsq]
    simp [mul_add, add_mul, mul_assoc]
  rw [e, htr_add, htr_smul]
  have e2 : x * (z • (b * c)) * y = z • (x * b * c * y) := by
    simp [mul_assoc]
  rw [e2, htr_smul, show x * (b * f * c) * y = x * b * f * c * y from by
        simp only [mul_assoc]]
  ring

end Algebra

section Lift

variable [Algebra R A]

/-- **The linear lift — `hgwg` for a coset-decomposed `w`.**

    Given the traced `g·w·g` reduction on the lower term `a` and on each mid term
    `bᵢ·f·cᵢ`, linearity of `tr` assembles it for `w = a + Σᵢ bᵢ·f·cᵢ` with
    `E w = a + Σᵢ z • (bᵢ·cᵢ)`.

    This is the step `MarkovInductiveCyclicity`'s header names as the only one not
    mechanised. Its hypotheses are supplied by `gwg_trace_lower_shape` and
    `gwg_trace_mid_shape` above. -/
theorem gwg_trace_cosetSum (tr : A → R) (g f : A) (z hbar : R)
    {ι : Type*} (s : Finset ι) (a : A) (b c : ι → A) (x y : A)
    (htr_add : ∀ p q : A, tr (p + q) = tr p + tr q) (htr_zero : tr 0 = 0)
    (hlow : tr (x * (g * a * g) * y)
              = tr (x * a * y) + z * hbar * tr (x * a * y))
    (hmid : ∀ i ∈ s, tr (x * (g * (b i * f * c i) * g) * y)
              = tr (x * (z • (b i * c i)) * y)
                + z * hbar * tr (x * (b i * f * c i) * y)) :
    tr (x * g * (a + ∑ i ∈ s, b i * f * c i) * g * y)
      = tr (x * (a + ∑ i ∈ s, z • (b i * c i)) * y)
        + z * hbar * tr (x * (a + ∑ i ∈ s, b i * f * c i) * y) := by
  classical
  have hL : x * g * (a + ∑ i ∈ s, b i * f * c i) * g * y
      = x * (g * a * g) * y + ∑ i ∈ s, x * (g * (b i * f * c i) * g) * y := by
    rw [mul_add, Finset.mul_sum, add_mul, Finset.sum_mul, add_mul, Finset.sum_mul]
    simp only [mul_assoc]
  have hE : x * (a + ∑ i ∈ s, z • (b i * c i)) * y
      = x * a * y + ∑ i ∈ s, x * (z • (b i * c i)) * y := by
    rw [mul_add, Finset.mul_sum, add_mul, Finset.sum_mul]
  have hW : x * (a + ∑ i ∈ s, b i * f * c i) * y
      = x * a * y + ∑ i ∈ s, x * (b i * f * c i) * y := by
    rw [mul_add, Finset.mul_sum, add_mul, Finset.sum_mul]
  rw [hL, hE, hW, htr_add, htr_add, htr_add,
      tr_finset_sum tr htr_add htr_zero, tr_finset_sum tr htr_add htr_zero,
      tr_finset_sum tr htr_add htr_zero, hlow,
      Finset.sum_congr rfl hmid, Finset.sum_add_distrib]
  simp only [Finset.mul_sum, mul_add]
  ring

/-- **The linear lift — `hCE` for a coset-decomposed `x`.**

    `ce_trace_mid` gives `tr(a·(b·f·c)) = z·tr(a·(b·c))` on one mid coset. Summing,
    `tr(a·x) = tr(a·(E x))` for `x = a' + Σᵢ bᵢ·f·cᵢ` and `E x = a' + Σᵢ z • (bᵢ·cᵢ)`:
    both sides reduce to `tr(a·a') + Σᵢ z·tr(a·(bᵢ·cᵢ))`. -/
theorem ce_trace_cosetSum (tr : A → R) (f : A) (z : R)
    {ι : Type*} (s : Finset ι) (a a' : A) (b c : ι → A)
    (htr_add : ∀ p q : A, tr (p + q) = tr p + tr q) (htr_zero : tr 0 = 0)
    (htr_smul : ∀ (r : R) (p : A), tr (r • p) = r * tr p)
    (hce : ∀ i ∈ s, tr (a * (b i * f * c i)) = z * tr (a * (b i * c i))) :
    tr (a * (a' + ∑ i ∈ s, b i * f * c i))
      = tr (a * (a' + ∑ i ∈ s, z • (b i * c i))) := by
  classical
  have hX : a * (a' + ∑ i ∈ s, b i * f * c i)
      = a * a' + ∑ i ∈ s, a * (b i * f * c i) := by
    rw [mul_add, Finset.mul_sum]
  have hEx : a * (a' + ∑ i ∈ s, z • (b i * c i))
      = a * a' + ∑ i ∈ s, z • (a * (b i * c i)) := by
    rw [mul_add, Finset.mul_sum]
    simp
  rw [hX, hEx, htr_add, htr_add,
      tr_finset_sum tr htr_add htr_zero, tr_finset_sum tr htr_add htr_zero,
      Finset.sum_congr rfl hce]
  simp only [htr_smul]

end Lift

end QOU.Machinery.MarkovInductive
