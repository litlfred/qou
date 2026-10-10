/-
Copyright (c) 2026 litlfred. All rights reserved.

# The ladder phase against the Wedderburn weights: what is determined, and what is not

Bean `qou-q2oa` (parent `qou-cdx1`, tranche `qou-cds1`). Companion probe
`computations/qbeta/qbeta_ladder_phase_from_wedderburn_weights.py`.

## The question

The Q_β precision ladder's N=1 rung carries the phase

  `alpha = (z - 1) * h / 2`,   `h = q - q⁻¹`

(`QOU.QBeta.phaseTwice z h = (z-1)*h`, carried doubled so the parity
bookkeeping needs no division). Per
`computations/qbeta/qbeta_d_frame_ladder_structure_probe.py` assertion A1 it
is the ONLY place a Markov-trace convention enters the entire ladder.

PR #5187 asserted `alpha = -h/4 - (h/2)*y_(2,1)` and **retracted** it: the
relation was read off the vector `(z, 1/2-z, z)`, which satisfies the
normalisation and **fails** the other two Markov conditions (PR #5185), so
`1/2 - z` is not `y_(2,1)`. The retracted relation was therefore not merely
inaccurate but **tautological** — fed its own instance it returns `alpha`
identically (probe check A0/A0b), so no arithmetic check could have caught
it. Only checking the instance's defining conditions could.

This file asks what `alpha` is against the weights that DO satisfy all three
conditions, and answers in two halves — one negative, one positive.

## The negative half (§3): `alpha` is not a function of the weights

`no_weight_function_gives_phase` is a **structural exclusion with a named
proved invariant** (AGENTS.md §"Before declaring refuted", scope (b)): the
invariant is bar-parity. Every convention-D weight is bar-EVEN — proved in
this corpus as `markovWeightsD_y21_barEven` / `markovWeightsD_y3_barEven`
(`QOU.QBeta.MarkovWeightsConventionD`), and re-verified symbolically for
n = 2..9 in the probe — so any function of the weight vector is bar-invariant.
The phase is not: `phaseTwice_bar_anomaly` gives `bar(alpha) + alpha = h²/2`,
so `alpha` is bar-invariant iff `alpha = h²/4`, i.e. iff `2z - h = 2`. Under D
that fails (`zD_loopMean_sub_two_num`, `quartic_neg_on_Icc_one_two`).

This settles the bean's question in the form the bean itself allows: *"Derive
`alpha` from the weight vector above, or establish that it is not determined
by the weights alone — a clean negative is a result here."*

## The positive half (§1-§2): what the weights DO determine, and how much

The weights determine `alpha` completely **once `h` is supplied**, and the
n-dependence collapses entirely:

1. `chi_sigma_collapse` — for every `λ`, with `mp`/`mm` the multiplicities of
   the `σ₁`-eigenvalues `q` and `-q⁻¹` on `V_λ`,
   `2*χ_λ(σ₁) - h*f^λ = [2]_q * (mp - mm)`, and `mp - mm` is the ORDINARY
   `S_n` character `χ^λ(τ)` at a transposition (the `q → 1` specialisation).
   Pure `field_simp`/`ring`. **This is where the bar-odd `h` cancels.**
2. `loopMean_eq_twoQ_mul_moment` — summing (1) against the two Markov
   conditions `Σ f^λ y_λ = 1` and `Σ χ_λ(σ₁) y_λ = z` gives, over any finite
   index and in ANY convention,
   `2z - h = [2]_q * Ξ`,  `Ξ := Σ_λ χ^λ(τ) * y_λ`.
3. `moment_independent_of_index` — since the left-hand side `2z - h` contains
   no `n`, the moment `Ξ` is **the same for every `n`**. This is a two-line
   consequence, but it is the content: n-independence is forced, not observed.
   (Its value under D is `(1+q⁴)/(1+q²)²` — `zD_loopMean_eq_twoQ_mul_xi`.
   The probe confirms `Ξ_n` computed from the actual weights matches for
   n = 2..9, by Frobenius `Σ_λ χ^λ(μ)s_λ = p_μ` with `μ = (2,1^{n-2})`.)
4. `phaseTwice_eq_moment_form` — hence
   `alpha = (h/4)*([2]_q*Ξ + h - 2)`.

So the bar-odd content of `alpha` comes from the `h` factor and nothing else,
and the weights supply its bar-even multiplier. `MarkovWeightsConventionD`
already named `h` as a permitted source ("it must come from elsewhere — the
`h` factor, the Kashiwara `f̃₁` shift, or the framing"); what is added here is
that the multiplier is **pinned**, and pinned by an n-independent functional.

## Scope — what this does NOT do

* The ansatz `alpha = (z-1)h/2` is **asserted upstream**, not derived here
  (`LadderPhaseMirrorCovariance` calls it "the asserted phase"). §1-§2 derive
  what that ansatz EQUALS in terms of the weights; they do not derive the
  ansatz.
* No `c_k` value, tier, or wiring changes. Every `c_k` conclusion in the
  corpus is convention-C-frame and has NOT been re-derived under D (bean
  `qou-cds1`); nothing here re-derives one. The `qbeta-decay` channel's
  registration is untouched.
* §2 is an identity following from the Markov *defining* conditions. It is
  not an independent determination of `z` from the weights — §3 proves no
  such determination exists.
* No experimental Q_β is inverted anywhere. `alpha` here is an exact rational
  function of `q`; the production `c₃ = (Q_codata/Q_N2 - 1)/u³` is a CODATA
  inversion and a fit in every convention, and is not used.

Base ring (§7c): this whole file is generic `[Field F]` — the σ₁ eigenvalue
`-q⁻¹` forces inverses but nothing archimedean. The one statement that needs
an ordering (that the quartic of §4 really is nonzero at the substrate pin)
is an `ℝ`-specialisation and therefore lives in a separate file,
`QOU.QBeta.LadderPhaseSubstratePin`.

Sorry-free.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import QOU.QBeta.LadderPhaseMirrorCovariance

namespace QOU.QBeta

open Finset

/-! ## §1. The character collapse: where the bar-odd `h` cancels

`σ₁` satisfies the Hecke relation, so on any irreducible `V_λ` it acts with
the two eigenvalues `q` and `-q⁻¹`, with multiplicities `mp` and `mm`
summing to `f^λ = dim V_λ`. Hence `χ_λ(σ₁) = q*mp - q⁻¹*mm`.

The combination `2*χ_λ(σ₁) - h*f^λ` then loses every trace of `h`: -/

variable {F : Type*} [Field F]

/-- The quantum integer `[2]_q = q + q⁻¹`. Bar-EVEN, unlike `h = q - q⁻¹`. -/
noncomputable def twoQ (q : F) : F := q + q⁻¹

/-- **`2·χ_λ(σ₁) - h·f^λ = [2]_q·(mp - mm)`.**

    With `χ_λ(σ₁) = q·mp - q⁻¹·mm` and `f^λ = mp + mm`, the `h = q - q⁻¹`
    multiplying the dimension exactly cancels the bar-odd half of the
    character, leaving the bar-EVEN `[2]_q` against the eigenvalue-multiplicity
    *difference*. That difference is the ordinary symmetric-group character
    `χ^λ(τ)` at a transposition — it is the `q → 1` value of `χ_λ(σ₁)`, where
    `σ₁ ↦ τ`, `q ↦ 1` and `-q⁻¹ ↦ -1`.

    This one identity is the reason a bar-even weight vector can nonetheless
    pin the bar-odd phase: the phase's `h` is not supplied by the weights, and
    everything the weights DO supply enters through `[2]_q`. -/
theorem chi_sigma_collapse (q mp mm : F) (hq : q ≠ 0) :
    2 * (q * mp - q⁻¹ * mm) - (q - q⁻¹) * (mp + mm)
      = twoQ q * (mp - mm) := by
  unfold twoQ
  field_simp
  ring

/-! ## §2. The loop-mean identity, and the collapse of the `n`-dependence -/

/-- **`2z - h = [2]_q · Ξ`**, where `Ξ = Σ_λ χ^λ(τ)·y_λ`.

    Hypotheses are exactly the two Markov conditions the weight vector is
    *defined* by — the normalisation `Σ f^λ y_λ = 1` and the stabilisation
    `Σ χ_λ(σ₁) y_λ = z` — plus the per-block eigenvalue decomposition, which
    is §1's input. No convention is fixed: `z` is arbitrary, so this holds in
    C, in D, and in any other frame.

    Stated over an arbitrary `Finset ι` so it covers every `n` at once; the
    caller supplies `mp`/`mm` as the two `σ₁`-eigenvalue multiplicities and
    the conclusion's moment is `Σ (mp - mm)·y`. -/
theorem loopMean_eq_twoQ_mul_moment {ι : Type*} (s : Finset ι)
    (q z : F) (hq : q ≠ 0) (y mp mm : ι → F)
    (hnorm : ∑ i ∈ s, (mp i + mm i) * y i = 1)
    (hsigma : ∑ i ∈ s, (q * mp i - q⁻¹ * mm i) * y i = z) :
    2 * z - (q - q⁻¹) = twoQ q * ∑ i ∈ s, (mp i - mm i) * y i := by
  have key : ∀ i ∈ s,
      twoQ q * ((mp i - mm i) * y i)
        = 2 * ((q * mp i - q⁻¹ * mm i) * y i)
          - (q - q⁻¹) * ((mp i + mm i) * y i) := by
    intro i _
    have := chi_sigma_collapse q (mp i) (mm i) hq
    linear_combination (y i) * this.symm
  symm
  calc twoQ q * ∑ i ∈ s, (mp i - mm i) * y i
      = ∑ i ∈ s, twoQ q * ((mp i - mm i) * y i) := by
        rw [Finset.mul_sum]
    _ = ∑ i ∈ s, (2 * ((q * mp i - q⁻¹ * mm i) * y i)
          - (q - q⁻¹) * ((mp i + mm i) * y i)) := Finset.sum_congr rfl key
    _ = 2 * (∑ i ∈ s, (q * mp i - q⁻¹ * mm i) * y i)
          - (q - q⁻¹) * ∑ i ∈ s, (mp i + mm i) * y i := by
        simp [Finset.sum_sub_distrib, Finset.mul_sum]
    _ = 2 * z - (q - q⁻¹) := by rw [hnorm, hsigma]; ring

/-- **The transposition moment does not depend on `n`.**

    `2z - h` mentions no index set, so if two different `n` both satisfy §2
    against the same `q` and `z`, their moments agree. The `n`-independence of
    `Ξ` is therefore *forced* by the loop-mean identity rather than observed
    across a table — the probe's n = 2..9 sweep confirms the premise but is
    not what establishes the conclusion.

    (Only `[2]_q ≠ 0` is needed, i.e. `q² + 1 ≠ 0`; over `ℝ` that is
    automatic.) -/
theorem moment_independent_of_index (q z Ξ₁ Ξ₂ : F) (h2 : twoQ q ≠ 0)
    (h₁ : 2 * z - (q - q⁻¹) = twoQ q * Ξ₁)
    (h₂ : 2 * z - (q - q⁻¹) = twoQ q * Ξ₂) : Ξ₁ = Ξ₂ :=
  mul_left_cancel₀ h2 (h₁ ▸ h₂)

/-- **The phase in moment form: `4α = [2]_q·Ξ·h + h² - 2h`.**

    Written on the doubled phase, `2·phaseTwice z h - h² = ([2]_q·Ξ - 2)·h`,
    which is `phaseTwice_projected_eq_loopMean` with the loop mean rewritten
    by §2. Equivalently `α = (h/4)·([2]_q·Ξ + h - 2)`.

    The bar-odd content sits entirely in the outer `h`; `[2]_q` and `Ξ` are
    both bar-even, so this exhibits the phase as `h × (bar-even, and pinned by
    the weights)` — the shape `MarkovWeightsConventionD` predicted without
    pinning. -/
theorem phaseTwice_eq_moment_form (q z Ξ : F)
    (hmom : 2 * z - (q - q⁻¹) = twoQ q * Ξ) :
    2 * phaseTwice z (q - q⁻¹) - (q - q⁻¹) ^ 2
      = (twoQ q * Ξ - 2) * (q - q⁻¹) := by
  rw [phaseTwice_projected_eq_loopMean z (q - q⁻¹)]
  unfold loopMeanTwice
  linear_combination (q - q⁻¹) * hmom

/-! ## §3. The negative half: `alpha` is NOT a function of the weights

This is the scope-(b) structural exclusion, and the invariant it cites is
bar-parity, proved in `QOU.QBeta.MarkovWeightsConventionD`. -/

/-- **The core clash: the phase is not bar-fixed.**

    Under D bar sends `z ↦ z - h` (`zD_bar_eq_negative_loop`: it exchanges the
    two stabilisation loop values), so `phaseTwice (z-h) (-h)` is the phase's
    bar image. It equals the phase itself only when `h*(2z - h - 2) = 0`.

    This is the whole mathematical content of the exclusion below; the wrapper
    that follows adds only the reading. Note it is a genuine restriction:
    without `hne` the two sides DO coincide, so the hypothesis is not
    decorative. -/
theorem phaseTwice_not_bar_fixed (z h : F) (hh : h ≠ 0)
    (hne : 2 * z - h ≠ 2) :
    phaseTwice (z - h) (-h) ≠ phaseTwice z h := by
  intro hEq
  have hprod : h * (2 * z - h - 2) = 0 := by
    unfold phaseTwice at hEq
    linear_combination -hEq
  rcases mul_eq_zero.mp hprod with hc | hc
  · exact hh hc
  · -- `F` is a bare `Field`, with no order, so `linarith` is unavailable here;
    -- the step is a linear identity and `linear_combination` discharges it.
    exact hne (by linear_combination hc)

/-- **No function of the weight vector reproduces the ladder phase.**

    The hypotheses are the real ones and none is decorative:
    * `hbar : zb = z - h` — how bar acts on the Markov parameter under D
      (`zD_bar_eq_negative_loop`: bar exchanges the two stabilisation loop
      values);
    * `hy : ybar = y` — the weight vector is bar-EVEN. Proved for the D-frame
      weights as `markovWeightsD_y21_barEven` / `markovWeightsD_y3_barEven`,
      hence so is any `F` of them;
    * `hF`, `hFbar` — the supposed function `F` reproduces the phase at `q`
      and, because its argument is bar-fixed, returns the SAME value at `q⁻¹`;
    * `hh : h ≠ 0`, `hne : 2z - h ≠ 2` — non-degeneracy.

    The conclusion is `False`: no such `G` exists.

    **Honesty about what `G` and `Y` contribute: nothing logical.** Once `hy`
    is substituted, `hF` and `hFbar` say only that the phase equals its own
    bar image, and the contradiction is `phaseTwice_not_bar_fixed` above.
    `G` and `Y` are carried because they are what makes the statement *read*
    as the exclusion it is — "some function of the weight vector returns the
    phase" — and because the bar-evenness of the weights is what supplies
    `hFbar` in any real application. The mathematics is entirely in the core
    lemma; this is its interpretation, not additional strength.

    Note what this does and does not exclude. It excludes the weights *alone*
    determining `alpha`; it does not touch §2, where `alpha` is recovered from
    the weights **together with `h`**. The two are consistent precisely
    because `h` is exactly the bar-odd datum the weights cannot see — `h`
    distinguishes `q` from `q⁻¹`, and the weights do not. -/
theorem no_weight_function_gives_phase {Y : Type*} (G : Y → F) (y ybar : Y)
    (z zb h : F)
    (hh : h ≠ 0) (hne : 2 * z - h ≠ 2)
    (hbar : zb = z - h) (hy : ybar = y)
    (hF : phaseTwice z h = G y)
    (hFbar : phaseTwice zb (-h) = G ybar) : False := by
  subst hy
  subst hbar
  exact phaseTwice_not_bar_fixed z h hh hne (by rw [hFbar, hF])

/-! ## §4. Convention D: the loop mean and the exclusion's hypothesis, algebraically

Everything here stays over the generic `F`. The archimedean half — that the
quartic below is actually nonzero at the substrate pin, which needs an
ordering — lives in `QOU.QBeta.LadderPhaseSubstratePin`, per §7c's rule that
an `ℝ`-specialisation goes in a separate file. -/

/-- **`2·z_D - h - 2` has numerator `q⁴ - 2q³ - 2q + 1`.**

    `2q³/(q²+1) - (q - q⁻¹) - 2 = (q⁴ - 2q³ - 2q + 1)/(q(q²+1))`, so the
    `§3` hypothesis `2z - h ≠ 2` is exactly the non-vanishing of that quartic.
    Stated denominator-cleared. -/
theorem zD_loopMean_sub_two_num (q : F) (hq : q ≠ 0) (hd : q ^ 2 + 1 ≠ 0) :
    (2 * zD q - (q - q⁻¹) - 2) * (q * (q ^ 2 + 1))
      = q ^ 4 - 2 * q ^ 3 - 2 * q + 1 := by
  unfold zD
  field_simp
  ring

/-- **The D-frame loop mean, in closed form.**

    `2·z_D - h = [2]_q · (q⁴+1)/(q²+1)²`, i.e. the moment `Ξ` of §2 takes the
    value `(1+Q²)/(1+Q)²` with `Q = q²` — for every `n`, by
    `moment_independent_of_index`. Stated denominator-cleared so it is a
    polynomial identity.

    At `n = 3` this value coincides with the single weight `y_(3)`, because
    `χ^(2,1)(τ) = 0`, `y_(1³) = 0` and `[4]_Q = (1+Q)(1+Q²)`. That coincidence
    is special to `n = 3` and should not be read as `Ξ = y_(n)` in general. -/
theorem zD_loopMean_eq_twoQ_mul_xi (q : F) (hq : q ≠ 0) (hd : q ^ 2 + 1 ≠ 0) :
    2 * zD q - (q - q⁻¹) = twoQ q * ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) := by
  unfold zD twoQ
  field_simp
  ring

/-- The same, denominator-cleared: `(2·z_D - h)·q·(q²+1) = q⁴ + 1`. -/
theorem zD_loopMean_num (q : F) (hq : q ≠ 0) (hd : q ^ 2 + 1 ≠ 0) :
    (2 * zD q - (q - q⁻¹)) * (q * (q ^ 2 + 1)) = q ^ 4 + 1 := by
  unfold zD
  field_simp
  ring

end QOU.QBeta
