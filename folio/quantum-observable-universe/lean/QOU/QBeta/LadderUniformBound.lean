/-
# The Q_β ladder exclusion, made INDEPENDENT OF THE SIGN of the rungs

`QOU.QBeta.LadderFactorBound.ladder_lt_of_rungs` already shows the ladder
cannot reach a requirement `F ≥ 1` — but only **under the hypothesis that every
rung lies in `(0, 1]`**, i.e. that every `c_k` is negative.  That hypothesis is
*measured* of the coefficients this corpus happens to record today
(`c₂ = -1`, `c₃ ≈ -2.069`, `c₅ ≈ -1.253`); it is not proved of the family.

**Why that matters right now.**  Bean `qou-cds1` is the open task of
re-deriving the whole `c_k` ladder under convention D.  A re-derivation that
produces a single *positive* coefficient voids `ladder_lt_of_rungs` entirely —
the theorem's hypothesis simply fails and it says nothing at all.  An agent
reading only that file could then reasonably conclude the exclusion had been
lifted, and go looking for the `Q_β` residual in the rungs.

This file removes the sign hypothesis.  The replacement input is
**uniform boundedness of the coefficients**, which is sign-blind:

    if  ∑ |cₖ uᵏ| ≤ S < 1   then   ∏ (1 + cₖ uᵏ) ≤ 1 / (1 - S).

That is the Weierstrass product bound, proved here by induction with no
`Real.exp` and no analysis beyond `nlinarith`.

**Mathlib already has a sibling of it, and this file keeps BOTH on purpose.**
`Finset.norm_prod_one_add_sub_one_le` (`Mathlib/Analysis/SpecialFunctions/
Log/Summable.lean`) gives `‖∏(1 + fᵢ) - 1‖ ≤ exp(∑‖fᵢ‖) - 1` over any
`NormedCommRing`, with **no hypotheses at all** — found by the corpus-grep
checklist, which is exactly what that checklist is for, and it means the
induction below is a re-derivation rather than a necessity.  It is kept because
the two bounds are genuinely different and each is better somewhere:

  * **Mathlib's is the tighter bound on the product.**  `1/(1-S) ≥ exp S` for
    `S ∈ [0,1)` (equal at `0`, and `1/(1-S)` has the larger second
    derivative), so the Weierstrass form here is the *weaker* of the two.
  * **Which is why this file quotes the Weierstrass `C_min`.**  A weaker
    product bound is *easier* for a hypothetical ladder to beat, so it yields
    the **smaller** required coefficient — `2279.45` against the exp route's
    `2493.72`.  Quoting the smaller one concedes more to the thing being
    excluded, which is the honest direction for a refutation.
  * **Mathlib's has no `S < 1` hypothesis**, so it still says something where
    the Weierstrass form goes vacuous — a coefficient blow-up past `S = 1`
    kills the induction below and not `ladder_lt_of_sum_bound_exp`.

`ladder_lt_of_sum_bound_exp` is the Mathlib route to the same exclusion, so
the result holds by **two independent arguments** rather than one.  Composed with the `cos ≤ 1`
cap it gives `ladder_lt_of_sum_bound`: the ladder is below `F` whenever
`1/(1-S) < F`, **whatever the signs of the coefficients**.

`sum_abs_le_of_scaled` is the piece that makes the hypothesis checkable from a
single number: if every rung magnitude is `|cₖ| uᵏ` with `|cₖ| ≤ C` and the
weights `uᵏ` sum to at most `G`, then `∑|cₖuᵏ| ≤ C·G`.  So the whole exclusion
turns on the one scalar `C` — the largest coefficient magnitude the ladder is
allowed — and on the geometric total `G`, which is a property of `u` alone.

**What the corpus numbers then say** (measured in
`computations/qbeta/qbeta_ladder_uniform_coefficient_bound_probe.py`, NOT
asserted here — this file proves the implication only):

    u  = 0.0085172345501561421893          (proton pin)
    G  = ∑_{k≥2} uᵏ = u²/(1-u) = 7.31664602858e-5
    F  = 1.20016236389                     (required factor, LIVE scored cell)
    ⇒  the SMALLEST uniform bound C that could possibly reach F is 2279.45
    ⇒  against the corpus's largest |cₖ| = 2.0693425728, a factor of 1101.5

**THE CONCLUSION IS NOT NEW; THE REASON IS.**  That the `Q_β` L2 residual is a
base/assembly problem rather than a rung problem is *already* the corpus's
stated position, in at least five places — the merged adjudication
`docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` ("the live
open question is not *what is α* but *what object supplies a factor above 1 at
all* — a question about the base or the assembly, not the phase"), beans
`qou-pdix` and `qou-cds1`, `qbeta_eigenphase_rationality_quantization_probe.py`
and its witness.  Nothing here establishes it for the first time.

What every one of those rests on is **(i)** the `cos ≤ 1` cap and **(ii)** the
*measured sign* of today's recorded `c_k`.  None argues from magnitude.  So
this file does not add a conclusion — it replaces a fragile premise with a
robust one, so the conclusion stays standing under `qou-cds1`.  The corpus
position becomes a statement about a single scalar a future agent can check
against a re-derived ladder, rather than a statement about signs that one
positive rung would overturn.

**Scope, deliberately narrow.**  This does NOT prove the re-derived ladder's
coefficients *are* bounded by any particular `C`; `C` is a hypothesis and the
corpus figure for it is a measurement.  It does NOT exhibit the missing factor,
and it does not touch the cosh route, which
`docs/audits/...` re-opened on the ruled base (the 2026-08-22 exclusion was
computed on the retired `z = 1` cell and is void).  It rules out one lever and
names what a future ladder would have to look like to be a lever at all.

Verified `lean`-direct with `-DautoImplicit=false -s 65536`: exit 0, no
diagnostics, no `sorry`, no `axiom`.
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Summable

namespace QOU.QBeta.LadderUniformBound

/-- The total absolute weight of a list is non-negative. -/
theorem sum_abs_nonneg (l : List ℝ) : 0 ≤ (l.map abs).sum :=
  List.sum_nonneg (by
    intro x hx
    obtain ⟨y, _, rfl⟩ := List.mem_map.mp hx
    exact abs_nonneg y)

/-- With total absolute weight below 1, every factor `1 + xᵢ` is positive, so
the product is. -/
theorem prod_one_add_pos (l : List ℝ) (h : (l.map abs).sum < 1) :
    0 < (l.map (fun x => 1 + x)).prod := by
  induction l with
  | nil => simp
  | cons a t ih =>
      have hsplit : ((a :: t).map abs).sum = |a| + (t.map abs).sum := by simp
      rw [hsplit] at h
      have ht0 := sum_abs_nonneg t
      have ha : |a| < 1 := by linarith
      have h1a : 0 < 1 + a := by
        have := neg_abs_le a
        linarith
      have htsum : (t.map abs).sum < 1 := by
        have := abs_nonneg a
        linarith
      simp only [List.map_cons, List.prod_cons]
      exact mul_pos h1a (ih htsum)

/-- **Weierstrass product bound, division-free form.**  A finite product
`∏(1 + xᵢ)` whose terms have total absolute weight `S < 1` satisfies
`∏(1 + xᵢ) · (1 - S) ≤ 1`.  No sign hypothesis on the `xᵢ`, and no division
anywhere — the `1/(1-S)` reading is the immediate consequence and is stated in
the docstring of `ladder_lt_of_sum_bound` rather than in a type. -/
theorem prod_one_add_mul_le_one (l : List ℝ) (h : (l.map abs).sum < 1) :
    (l.map (fun x => 1 + x)).prod * (1 - (l.map abs).sum) ≤ 1 := by
  induction l with
  | nil => simp
  | cons a t ih =>
      have hsplit : ((a :: t).map abs).sum = |a| + (t.map abs).sum := by simp
      rw [hsplit] at h ⊢
      have ht0 := sum_abs_nonneg t
      have haa := abs_nonneg a
      have htsum : (t.map abs).sum < 1 := by linarith
      have hIH := ih htsum
      have hPt := prod_one_add_pos t htsum
      have hupper : (1 + a) ≤ 1 + |a| := by
        have := le_abs_self a; linarith
      have h1a : 0 < 1 + a := by
        have := neg_abs_le a; linarith
      have hrest : (0:ℝ) ≤ 1 - (|a| + (t.map abs).sum) := by linarith
      simp only [List.map_cons, List.prod_cons]
      nlinarith [mul_nonneg (le_of_lt hPt) hrest, sq_nonneg |a|,
        mul_nonneg haa ht0, mul_nonneg (le_of_lt hPt) (mul_nonneg haa ht0),
        mul_nonneg (le_of_lt hPt) (sq_nonneg |a|)]

/-- If every term is bounded by `C` times a non-negative weight, and the
weights total at most `G`, the terms total at most `C * G`.  This is what turns
"every coefficient is `O(1)`" into a single checkable scalar. -/
theorem sum_abs_le_of_scaled (l : List (ℝ × ℝ)) (C G : ℝ) (hC : 0 ≤ C)
    (hb : ∀ p ∈ l, |p.1| ≤ C * p.2 ∧ 0 ≤ p.2)
    (hG : (l.map Prod.snd).sum ≤ G) :
    (l.map (fun p => |p.1|)).sum ≤ C * G := by
  have key : ∀ m : List (ℝ × ℝ), (∀ p ∈ m, |p.1| ≤ C * p.2 ∧ 0 ≤ p.2) →
      (m.map (fun p => |p.1|)).sum ≤ C * (m.map Prod.snd).sum := by
    intro m
    induction m with
    | nil => simp
    | cons a t ih =>
        intro hm
        have ha := hm a (by simp)
        have ht : ∀ p ∈ t, |p.1| ≤ C * p.2 ∧ 0 ≤ p.2 :=
          fun p hp => hm p (by simp [hp])
        have hrest := ih ht
        simp only [List.map_cons, List.sum_cons]
        nlinarith [ha.1]
  have h1 := key l hb
  have hmono : C * (l.map Prod.snd).sum ≤ C * G :=
    mul_le_mul_of_nonneg_left hG hC
  linarith

/-- **The sign-independent ladder exclusion.**  With the cosine cap and a
uniform bound `S` on the total absolute rung weight, the ladder is strictly
below any requirement `F` with `1 < F · (1 - S)` — equivalently `F > 1/(1-S)`
— for rungs of **either sign**. -/
theorem ladder_lt_of_sum_bound (u α F S : ℝ) (l : List ℝ)
    (hu : 0 < u) (hu2 : u ^ 2 < 1)
    (hS : (l.map abs).sum ≤ S) (hS1 : S < 1) (hF : 1 < F * (1 - S)) :
    Real.cos (α - u / 2) * (1 - u ^ 2) * (l.map (fun x => 1 + x)).prod < F := by
  have hSt1 : (l.map abs).sum < 1 := lt_of_le_of_lt hS hS1
  have hP0 := prod_one_add_pos l hSt1
  have hPle := prod_one_add_mul_le_one l hSt1
  have hd' : (0:ℝ) < 1 - S := by nlinarith
  -- prod * (1 - S) ≤ prod * (1 - sum) ≤ 1 < F * (1 - S), so prod < F
  have hstep : (l.map (fun x => 1 + x)).prod * (1 - S) ≤ 1 := by
    nlinarith [mul_le_mul_of_nonneg_left hS (le_of_lt hP0)]
  have hprodF : (l.map (fun x => 1 + x)).prod < F := by nlinarith
  have hu2p : (0:ℝ) < u ^ 2 := pow_pos hu 2
  have hq : (0:ℝ) < 1 - u ^ 2 := by linarith
  have hqP : (0:ℝ) < (1 - u ^ 2) * (l.map (fun x => 1 + x)).prod := mul_pos hq hP0
  have s1 : Real.cos (α - u / 2) * ((1 - u ^ 2) * (l.map (fun x => 1 + x)).prod)
      ≤ 1 * ((1 - u ^ 2) * (l.map (fun x => 1 + x)).prod) :=
    mul_le_mul_of_nonneg_right (Real.cos_le_one _) (le_of_lt hqP)
  have s2 : (1 - u ^ 2) * (l.map (fun x => 1 + x)).prod
      ≤ 1 * (l.map (fun x => 1 + x)).prod :=
    mul_le_mul_of_nonneg_right (by linarith) (le_of_lt hP0)
  have e : Real.cos (α - u / 2) * (1 - u ^ 2) * (l.map (fun x => 1 + x)).prod
      = Real.cos (α - u / 2) * ((1 - u ^ 2) * (l.map (fun x => 1 + x)).prod) := by
    ring
  rw [e]
  linarith

/-- The contrapositive an agent actually wants: a ladder that DOES reach `F`
forces a total absolute rung weight above `S`.  Reading the corpus numbers into
it is the probe's job, not this file's. -/
theorem sum_bound_of_ladder_ge (u α F S : ℝ) (l : List ℝ)
    (hu : 0 < u) (hu2 : u ^ 2 < 1) (hS1 : S < 1) (hF : 1 < F * (1 - S))
    (hreach : F ≤ Real.cos (α - u / 2) * (1 - u ^ 2) * (l.map (fun x => 1 + x)).prod) :
    S < (l.map abs).sum := by
  by_contra hcon
  push_neg at hcon
  exact absurd hreach (not_le.mpr (ladder_lt_of_sum_bound u α F S l hu hu2 hcon hS1 hF))

/-! ## The same exclusion by an independent route, via Mathlib

The corpus-grep checklist turned up `Finset.norm_prod_one_add_sub_one_le`,
which bounds `‖∏(1 + fᵢ) - 1‖` by `exp(∑‖fᵢ‖) - 1` with **no hypotheses** —
neither smallness nor sign.  Composing it with the same `|cos| ≤ 1` cap gives
the exclusion again, from a bound this file did not prove.

Two properties are worth noting.  It needs **no `S < 1` hypothesis**, so it
still says something where the Weierstrass form goes vacuous.  And it routes
through `|·|` rather than through positivity of the product, so it never needs
`prod_one_add_pos` — which is what lets it drop the smallness assumption. -/

/-- **The ladder exclusion via Mathlib's product bound** — an independent route
to `ladder_lt_of_sum_bound`, with no `S < 1` hypothesis and no sign hypothesis
on the rungs. -/
theorem ladder_lt_of_sum_bound_exp (u α F S : ℝ) {ι : Type*} (t : Finset ι)
    (f : ι → ℝ) (hu2 : u ^ 2 < 1)
    (hS : ∑ i ∈ t, |f i| ≤ S) (hF : Real.exp S < F) :
    Real.cos (α - u / 2) * (1 - u ^ 2) * (∏ i ∈ t, (1 + f i)) < F := by
  have hml := Finset.norm_prod_one_add_sub_one_le t f
  simp only [Real.norm_eq_abs] at hml
  set P := ∏ i ∈ t, (1 + f i) with hPdef
  have h1 : |P| - |(1:ℝ)| ≤ |P - 1| := abs_sub_abs_le_abs_sub P 1
  rw [abs_one] at h1
  have hPabs : |P| ≤ Real.exp (∑ x ∈ t, |f x|) := by linarith
  have hmono : Real.exp (∑ x ∈ t, |f x|) ≤ Real.exp S := Real.exp_le_exp.mpr hS
  have hc := Real.abs_cos_le_one (α - u / 2)
  have hq : |1 - u ^ 2| = 1 - u ^ 2 := abs_of_nonneg (by linarith)
  have key : |Real.cos (α - u / 2) * (1 - u ^ 2) * P| ≤ |P| := by
    rw [abs_mul, abs_mul, hq]
    have hcq : |Real.cos (α - u / 2)| * (1 - u ^ 2) ≤ 1 := by
      nlinarith [abs_nonneg (Real.cos (α - u / 2))]
    calc |Real.cos (α - u / 2)| * (1 - u ^ 2) * |P|
        ≤ 1 * |P| := mul_le_mul_of_nonneg_right hcq (abs_nonneg P)
      _ = |P| := one_mul _
  calc Real.cos (α - u / 2) * (1 - u ^ 2) * P
      ≤ |Real.cos (α - u / 2) * (1 - u ^ 2) * P| := le_abs_self _
    _ ≤ |P| := key
    _ ≤ Real.exp (∑ x ∈ t, |f x|) := hPabs
    _ ≤ Real.exp S := hmono
    _ < F := hF

end QOU.QBeta.LadderUniformBound
