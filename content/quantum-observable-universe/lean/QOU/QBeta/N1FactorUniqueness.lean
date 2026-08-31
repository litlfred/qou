/-
# QOU.QBeta.N1FactorUniqueness

The three load-bearing steps of `qou-cds1` entries 10 / 10b / 10c, as theorems.

Bean `qou-cds1`.  **The mathematics here is not new** — it is the sibling
result landed in PR #6310 (`entry 10c: the functional equation settles
uniqueness — the phase shift is forced, the constant is free`), reached
symbolically there.  This file re-derives nothing; it converts the three steps
the argument rests on from CAS output into machine-checked statements, and one
of them is a step the CAS demonstrably could not perform.

## Why a proof assistant, and not a second CAS run

Entry 10 records that `sympy.simplify` does **not** reduce

    (cos A + cos B)/2 - cos((A+B)/2)·cos((A-B)/2)

to zero for these arguments — it returns a residual of two uncombined cosines —
and that the identity had to be confirmed numerically instead, at 60 dps, with
the entry noting the author was "one step from" reading the residual as a
refutation.  A non-simplification is not a refutation, and 60-dps agreement is
not a proof.  `barMidpoint_eq` below is that identity, exactly.

## What is forced and what is not

The arc's conditions on the `N = 1` factor are: (i) bar-invariance, where bar
acts as `a ↦ δ - a` with `δ = h²/2`; (ii) the log-separable form
`F = φ(a - c(δ))·K(δ)`; (iii) the convention-C limit `F(a, 0) = cos a`, which
fixes `φ = cos` and `c(0) = 0`.

  * `phase_forced` — (i) forces `c ≡ δ/2` modulo `π`.  Stated as an **iff**, so
    it also records that every such `c` genuinely works; the continuity
    argument that picks `k = 0` from `c(0) = 0` is the arc's, not Lean's.
  * `const_free` — for an **arbitrary** `K`, `cos(a - δ/2)·K` is bar-invariant.
    So the residual freedom is real: it is a theorem that the three conditions
    do not pin the constant, not a failure to find the constraint that would.
    PR #6310 measures that freedom at 59694 ppb against a 7.797 ppb target.

What selects `K = cos(δ/2)` is the arc's entry-2 bar-midpoint rule — parsimony,
not derivation.  Nothing here changes that, and `barMidpoint_eq` is exactly the
statement that the rule's output has the forced phase.

## Base ring (§7c)

`ℝ` throughout, and genuinely so: every statement is about `Real.cos` and the
`2π`-periodicity of the reals.  There is no generic-ring content to separate.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Complex
import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.Tactic

namespace QOU.QBeta.N1FactorUniqueness

open Real

/-- The bar action on the D-frame phase: `a ↦ δ - a`, a reflection about `δ/2`.
Under convention C, `δ = 0` and this is the familiar `a ↦ -a`. -/
def barPhase (δ a : ℝ) : ℝ := δ - a

/-- The candidate `N = 1` factor in the log-separable form the arc requires:
a cosine re-centred by `c`, times a phase-independent constant. -/
noncomputable def candidate (c K a : ℝ) : ℝ := Real.cos (a - c) * K

/-- Bar-invariance of a candidate, as a proposition in `a`. -/
def BarInvariant (δ c K : ℝ) : Prop := ∀ a : ℝ, candidate c K (barPhase δ a) = candidate c K a

/-- **The bar-midpoint identity — the step `sympy.simplify` would not do.**

`(cos a + cos(δ - a))/2 = cos(a - δ/2) · cos(δ/2)`, exactly, for all real `a`
and `δ`.  Entry 10 verified this at 60 dps after the CAS returned a non-zero
residual; it is an identity, and this is the proof. -/
theorem barMidpoint_eq (δ a : ℝ) :
    (Real.cos a + Real.cos (barPhase δ a)) / 2 = Real.cos (a - δ / 2) * Real.cos (δ / 2) := by
  unfold barPhase
  rw [Real.cos_add_cos]
  have h1 : (a + (δ - a)) / 2 = δ / 2 := by ring
  have h2 : (a - (δ - a)) / 2 = a - δ / 2 := by ring
  rw [h1, h2]
  ring

/-- **The constant is FREE.**  For *every* `K`, re-centring by `δ/2` gives a
bar-invariant factor.  So conditions (i)–(iii) leave `K` unconstrained — a
proved negative, not an unfound constraint. -/
theorem const_free (δ K : ℝ) : BarInvariant δ (δ / 2) K := by
  intro a
  unfold candidate barPhase
  have : δ - a - δ / 2 = -(a - δ / 2) := by ring
  rw [this, Real.cos_neg]

/-- **The phase re-centring is FORCED**, modulo `π`.

Bar-invariance for a nonzero `K` holds **iff** `c = δ/2 - kπ` for some integer
`k`.  The arc's continuity argument (`c(0) = 0`, `c` continuous) selects
`k = 0`, giving `c = δ/2`; that selection is outside this statement. -/
theorem phase_forced {δ c K : ℝ} (hK : K ≠ 0) :
    BarInvariant δ c K ↔ ∃ k : ℤ, c = δ / 2 - k * π := by
  constructor
  · intro h
    -- Instantiate at `a = c`: the left factor becomes `cos 0 = 1`.
    have hc := h c
    unfold candidate barPhase at hc
    rw [sub_self, Real.cos_zero] at hc
    have hcos : Real.cos (δ - c - c) = 1 := by
      have := mul_right_cancel₀ hK hc
      linarith [this]
    obtain ⟨n, hn⟩ := (Real.cos_eq_one_iff _).mp hcos
    exact ⟨n, by linarith [hn]⟩
  · rintro ⟨k, rfl⟩ a
    unfold candidate barPhase
    have hL : δ - a - (δ / 2 - k * π) = -(a - δ / 2) + k * π := by ring
    have hR : a - (δ / 2 - k * π) = (a - δ / 2) + k * π := by ring
    rw [hL, hR, Real.cos_add_int_mul_pi, Real.cos_add_int_mul_pi, Real.cos_neg]

/-- The arc's chosen factor `M(a) = cos(a - δ/2)·cos(δ/2)` is bar-invariant —
the entry-2 bar-midpoint rule's output, in the forced phase. -/
theorem barMidpoint_barInvariant (δ : ℝ) : BarInvariant δ (δ / 2) (Real.cos (δ / 2)) :=
  const_free δ _

/-- **The convention-C limit.**  At `δ = 0` the factor is a bare cosine, which
is condition (iii); and there the bar action is `a ↦ -a`, under which `cos` is
already invariant.  This is why C could use a bare cosine and D cannot — the
bar-midpoint rule is *vacuous* in C, not satisfied by accident. -/
theorem c_limit (a : ℝ) :
    (Real.cos a + Real.cos (barPhase 0 a)) / 2 = Real.cos a := by
  rw [barMidpoint_eq]
  norm_num

/-- **CONTROL — the forcing has teeth.**

If bar-invariance held for every `c`, everything above would be vacuous.  It
does not: the *un-recentred* cosine (`c = 0`, the convention-C form) is
bar-invariant only in the degenerate case `δ = 2kπ`.  Stated for arbitrary `δ`
rather than at one sample point, and proved from `phase_forced` itself. -/
theorem uncentred_fails {δ : ℝ} (hδ : ∀ k : ℤ, δ ≠ 2 * k * π) :
    ¬ BarInvariant δ 0 1 := by
  intro h
  obtain ⟨k, hk⟩ := (phase_forced (δ := δ) (c := 0) (K := 1) one_ne_zero).mp h
  exact hδ k (by linarith [hk])

/-- The physically relevant form: for a defect strictly between `0` and `2π` —
which the D-frame `δ = h²/2` is, being small and positive — the un-recentred
cosine is not bar-invariant.  Needs only `0 < π`, no numeric bound. -/
theorem uncentred_fails_of_pos_of_lt {δ : ℝ} (h0 : 0 < δ) (h2 : δ < 2 * π) :
    ¬ BarInvariant δ 0 1 := by
  refine uncentred_fails (fun k hk => ?_)
  subst hk
  have hpi : (0:ℝ) < π := Real.pi_pos
  have hk1 : (0:ℝ) < (k:ℝ) := by nlinarith
  have hk2 : ((k:ℝ)) < 1 := by nlinarith
  have : (0:ℤ) < k := by exact_mod_cast hk1
  have : k < 1 := by exact_mod_cast hk2
  omega

/-- **CONTROL — the C limit is not an accident of `δ = 0` arithmetic.**

Under convention C the bar action is `a ↦ -a` and `cos` is even, so the
bar-midpoint rule returns its input unchanged: the rule is *vacuous* in C.  That
is why C could carry a bare cosine, and the reason its unavailability under D is
structural rather than a gap in the search. -/
theorem c_rule_is_vacuous (a : ℝ) : Real.cos (barPhase 0 a) = Real.cos a := by
  unfold barPhase
  rw [zero_sub, Real.cos_neg]

end QOU.QBeta.N1FactorUniqueness
