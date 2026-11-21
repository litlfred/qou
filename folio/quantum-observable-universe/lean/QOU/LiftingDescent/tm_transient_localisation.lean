import Mathlib.Tactic

/-!
# QOU.LiftingDescent.tm_transient_localisation

Canonical Lean for content block
[`lem:topological-mass-transient-localisation`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md):
*Transient terms are bounded by exceptional-divisor contributions.*

**Block statement.**  The transient component `α − τ̂ₙ(α)` has support in
disjoint discs `Dᵢ` centred at the blow-up points, and the norm of its
multiplicative integral is *bounded by* a sum over the exceptional divisors
`Eᵢ`:

  `‖MI∫_Σ (α − τ̂ₙ(α))‖ ≤ Σᵢ ‖MI∫_{Eᵢ} (∇_A q, L ∧ F⁺)‖`.

The block stated equality until 2026-10-10, when it was restated as the
inequality on owner ruling (bean `tmvac`); the equality is the open
conjecture class below.

## What is derived, and what is not

Everything is a **parameter**.  The multiplicative integrals take values in
an arbitrary (possibly non-commutative) seminormed group `G`, so the
disc product is an ordered `List.prod`.  The proof block's two geometric
steps are explicit hypotheses:

* `hsplit` — the transient integral is the ordered product of the disc
  integrals (support in the disjoint discs `Dᵢ`);
* `hsupp` — each disc integral equals the exceptional-divisor integral
  (the integrand is supported on `Eᵢ ⊂ Dᵢ`).

From these, the **inequality** `‖MI∫_Σ‖ ≤ Σᵢ ‖MI∫_{Eᵢ}‖` is *derived*
(`tm_transient_localisation`) from the triangle inequality of a group
seminorm.

The **equality** the block formerly stated is *not* derivable from these
hypotheses: the proof block's step "the norm of the product equals the sum
of the norms" is false for a general group norm, and
`norm_additivity_not_forced` exhibits data satisfying both hypotheses
(in `Multiplicative ℝ`) for which equality fails.  The equality is
therefore recorded as the content-bearing conjecture class
`TransientLocalisationNormEquality`, with **no instance**.  Closing it
needs a further structural input (e.g. that the disc integrals lie on a
common ray on which the norm is additive — the proof block's appeal to
commutation modulo the central band does not by itself give this).

An earlier revision carried both geometric steps *and* their composite as
fields of a data class that the all-zero instance satisfies, so the
"localisation" said nothing; one earlier still defined
`transientMItotal := 0`.  Bean `tmvac`.

-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
-/

namespace QOU.LiftingDescent

variable {G : Type*} [SeminormedGroup G]

/-- Triangle inequality for an ordered product over `List.range N`. -/
theorem norm_prod_range_le (f : ℕ → G) (N : ℕ) :
    ‖((List.range N).map f).prod‖ ≤ ∑ i ∈ Finset.range N, ‖f i‖ := by
  induction N with
  | zero => simp
  | succ n ih =>
    rw [List.range_succ, List.map_append, List.prod_append, Finset.sum_range_succ]
    simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, mul_one]
    exact (norm_mul_le' _ _).trans (by linarith)

/-- **Transient-term localisation, derived half (inequality).**

Given that the transient multiplicative integral over `Σ` is the ordered
product of the disc integrals (`hsplit`) and that each disc integral is the
exceptional-divisor integral (`hsupp`), its norm is at most the sum of the
exceptional-divisor norms. -/
theorem tm_transient_localisation (MIsig : G) (disc div : ℕ → G) (N : ℕ)
    (hsplit : MIsig = ((List.range N).map disc).prod)
    (hsupp : ∀ i, disc i = div i) :
    ‖MIsig‖ ≤ ∑ i ∈ Finset.range N, ‖div i‖ := by
  have hdisc : disc = div := funext hsupp
  subst hdisc
  rw [hsplit]
  exact norm_prod_range_le disc N

/-- **The equality is not forced by the split.**  There is data in the
seminormed group `Multiplicative ℝ` satisfying both geometric hypotheses
(`hsplit` with `N = 2`, and `hsupp` trivially with `div = disc`) for which
`‖MI∫_Σ‖ ≠ Σᵢ ‖MI∫_{Eᵢ}‖`.  Scope (a): this shows the hypotheses *alone*
do not yield the block's equality; it says nothing about the specific
multiplicative integral of the transient integrand. -/
theorem norm_additivity_not_forced :
    ∃ (MIsig : Multiplicative ℝ) (disc : ℕ → Multiplicative ℝ),
      MIsig = ((List.range 2).map disc).prod ∧
      ‖MIsig‖ ≠ ∑ i ∈ Finset.range 2, ‖disc i‖ := by
  refine ⟨Multiplicative.ofAdd 0,
    fun i => if i = 0 then Multiplicative.ofAdd 1 else Multiplicative.ofAdd (-1), ?_, ?_⟩
  · simp [List.range_succ]
  · simp [Finset.sum_range_succ, norm_ofAdd]
    norm_num

/-- **Conjecture (the block's equality).**  For the multiplicative integral
of the transient integrand, the norm over `Σ` equals the sum of the
exceptional-divisor norms.  Content-bearing, deliberately **without an
instance**: by `norm_additivity_not_forced` it does not follow from the
disc split and support hypotheses alone, and no further input that would
force it is established in the corpus. -/
class TransientLocalisationNormEquality (MIsig : G) (div : ℕ → G) (N : ℕ) : Prop where
  norm_eq : ‖MIsig‖ = ∑ i ∈ Finset.range N, ‖div i‖

end QOU.LiftingDescent
