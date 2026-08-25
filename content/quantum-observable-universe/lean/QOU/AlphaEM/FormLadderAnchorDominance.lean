/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Order.MinMax
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# The α_EM form ladder: its integers are convention-free, and its residual is anchor-dominated

Bean `qou-4jut` follow-on, under epic `qou-qia8`.  Formalises the two structural
facts behind `computations/alpha-em-form-ladder.witness.json`:

```
1/α  =  q[9]_q[10]_q  +  2g/(4π(g−1))  +  αH(1 − h²α)  +  Δ₂,   g = 4
      H = [2]_q/(8π),   h = q − q⁻¹ (Hecke structure constant),
      Δ₂ = uncomputed archimedean two-loop (weight-3; NOT the −h²Hα² above)
```

with the recorded fixed points

| anchor | fixed point | residual vs the witness's CODATA |
|---|---:|---:|
| proton | 137.035999313169 | 1.6723 ppb |
| muon   | 137.036010116763 | 80.5100 ppb |

## Part 1 — the ladder's integers need no minimal-strand convention

The witness calls its integers "structurally derived (Bring genus 4; crossing
numbers of `T(2,9)`, `T(3,5)`)".  What is proved here is the property that makes
that phrase safe: the **crossing number** of a torus knot,
`c(T(p,q)) = min (p(q−1)) (q(p−1))`, is **symmetric** under `p ↔ q`
(`crossingNumberTorus_symm`), so it assigns one value to `T(p,q) ≅ T(q,p)` with
no convention required.

This is exactly what the *writhe* rule fails to do.  `w(T(m,p)) = (m−1)p` is
**not** symmetric — `writheTorus_not_symm` exhibits `w(T(2,3)) = 3 ≠ 4 =
w(T(3,2))` — which is why
`content/quantum-observable-universe/mass-theory/torus-knot-delta-q-writhe.md`
had to be given the minimal-strand guard `m ≤ p` (Morton–Williams braid index)
earlier in this same PR, and why
`computations/rosso_jones_three_strand_delta_q.py` now raises on a swapped pair.
The α_EM ladder inherits no such hazard: `crossing_number_needs_no_convention`
states the contrast as a single proposition.

**This does not make the ladder correct** — see the honest scope below.  It
removes one specific failure mode (a presentation-dependent integer) that the
neighbouring `δ_q` rule genuinely had.

## Part 2 — the residual is anchor-dominated, and no anchor-blind term fixes it

* `anchor_gap_eq_prediction_gap` — the *difference* of the two anchors'
  residuals equals the difference of their raw predictions: the reference value
  cancels.  So "which anchor" is **independent of the CODATA vintage**.  Not
  idle: the witness scores against `137.035999084` while
  `alpha-k-per-force-assembly.witness.json` carries `137.035999177`, and this
  says the anchor comparison survives that discrepancy untouched.
* `no_anchor_blind_affine_correction_closes_gap` — appending any further term
  that does not itself depend on the anchor (any affine `x ↦ s·x + c`, `s ≠ 0`)
  leaves the two anchors distinct.  So the residual spread cannot be absorbed by
  carrying the α-expansion further — not by the derived `αH(1 − h²α)` already in
  the form, and not by the uncomputed `Δ₂`, since neither depends on the anchor
  except through `q` itself.  Only an anchor-*dependent* ingredient can move it.
* `degenerate_correction_is_vacuous` — the one escape, `s = 0`, does equalise
  them, by discarding the prediction entirely.  Named so the exclusion is not
  over-claimed.
* `anchor_gap_dominates_proton_residual` — on the recorded values the gap is
  more than `40×` the proton-anchored residual.
* `leading_term_residual_dwarfs_full_form` — the leading term **alone** misses
  by more than `5·10⁵×` the full form's proton-anchored residual.  Quoting
  `q[9]_q[10]_q`'s residual as the framework's α_EM accuracy is a category
  error of about six orders of magnitude; this file exists partly because that
  error was made in session and had to be retracted.

## Honest scope

**Scope-(a) throughout, and this file proves nothing about α_EM itself.**
The witness's own caveats stand and are *not* discharged here: the derivation
carries **three unproved classes**; the result is **anchor-dependent** (which is
Part 2's subject, not its refutation); and no coefficient is fitted.  What is
proved is (i) an arithmetic property of the torus crossing number, and (ii) the
structural consequence of the two *recorded* residuals — which enter as explicit
hypotheses or `def`s of measured data, never as derived quantities.

Part 1 is generic and convention-free (`ℕ`, `min`).  The genus term is stated
**division-free over an arbitrary commutative ring** — no `π`, no `Real`, and no
characteristic hypothesis, per §7c and the standing "rewrite so there is no
`/2`" steer; only Part 2's comparisons against recorded decimals use `ℝ`.
-/

namespace QOU.AlphaEM.FormLadder

/-! ### Part 0 — the genus term, generically -/

/-- `T` is *the* genus term at genus `g` (with `p` standing for `π`) exactly when
it satisfies the ladder's defining relation, stated **cleared of denominators**:
`4·p·(g−1)·T = 2·g`.

Writing it this way — rather than as `T = 2g/(4p(g−1))` — costs nothing and buys
everything: it needs no `p ≠ 0`, no `g − 1 ≠ 0`, and **no characteristic
hypothesis**, so it holds over an arbitrary commutative ring.  A quotient form
would force `4 ≠ 0`, i.e. would silently exclude characteristic 2. -/
def IsGenusTerm {R : Type*} [CommRing R] (g p T : R) : Prop :=
  4 * p * (g - 1) * T = 2 * g

/-- **At the Bring genus `g = 4` the defining relation reads `12·p·T = 8`.**

`4` is not a fitted parameter: it is the genus of Bring's surface.  Division-free
and characteristic-free — an iff over any commutative ring. -/
theorem isGenusTerm_four_iff {R : Type*} [CommRing R] (p T : R) :
    IsGenusTerm 4 p T ↔ 12 * p * T = 8 := by
  unfold IsGenusTerm
  have e1 : (4 : R) * p * (4 - 1) * T = 12 * p * T := by ring
  have e2 : (2 : R) * 4 = 8 := by norm_num
  rw [e1, e2]

/-- **The closed form `2/(3p)` satisfies the relation** — stated as the cleared
hypothesis `3·p·T = 2`, so the implication holds over any commutative ring with
no invertibility assumption whatever.

This is the direction that is actually used: given the closed form, it *is* the
genus term.  The converse needs `4` to be cancellable and is therefore stated
separately below. -/
theorem isGenusTerm_four_of_three_mul (R : Type*) [CommRing R] (p T : R)
    (h : 3 * p * T = 2) : IsGenusTerm 4 p T := by
  unfold IsGenusTerm
  have e1 : (4 : R) * p * (4 - 1) * T = 4 * (3 * p * T) := by ring
  rw [e1, h]; ring

/-- **The converse, with its hypothesis named** (`_of_` per the conditional-lemma
convention): recovering `3·p·T = 2` from the ladder relation requires cancelling
`4`, which fails in characteristic 2.  The hypothesis is carried explicitly
rather than hidden in a `Field` instance. -/
theorem three_mul_of_isGenusTerm_four_of_four_cancellable
    (R : Type*) [CommRing R] (p T : R)
    (hcancel : ∀ x y : R, 4 * x = 4 * y → x = y)
    (h : IsGenusTerm 4 p T) : 3 * p * T = 2 := by
  unfold IsGenusTerm at h
  refine hcancel _ _ ?_
  have e1 : (4 : R) * (3 * p * T) = 4 * p * (4 - 1) * T := by ring
  rw [e1, h]; ring

/-! ### Part 1 — the ladder's integers are convention-free -/

/-- The crossing number of the torus knot `T(p, q)`: `min (p(q−1)) (q(p−1))`. -/
def crossingNumberTorus (p q : ℕ) : ℕ := min (p * (q - 1)) (q * (p - 1))

/-- The writhe rule the `δ_q` decoration uses: `w(T(m,p)) = (m−1)p`. -/
def writheTorus (m p : ℕ) : ℕ := (m - 1) * p

/-- **The crossing number is symmetric.**

`T(p,q)` and `T(q,p)` are the same knot, and this formula assigns them the same
integer — with no choice of presentation. -/
theorem crossingNumberTorus_symm (p q : ℕ) :
    crossingNumberTorus p q = crossingNumberTorus q p := by
  unfold crossingNumberTorus
  exact min_comm _ _

/-- **The writhe rule is NOT symmetric.**

`w(T(2,3)) = 3` but `w(T(3,2)) = 4`, for the trefoil either way.  This is the
defect that forced the minimal-strand guard `m ≤ p` on
`torus-knot-delta-q-writhe.md` and on `rosso_jones_three_strand_delta_q.py`. -/
theorem writheTorus_not_symm : writheTorus 2 3 ≠ writheTorus 3 2 := by decide

/-- **The contrast, as one statement.**

On the very same pair, the crossing number agrees under transposition and the
writhe does not.  Hence the α_EM ladder's integers need no minimal-strand
convention, while the `δ_q` writhe exponent does. -/
theorem crossing_number_needs_no_convention :
    crossingNumberTorus 2 3 = crossingNumberTorus 3 2 ∧
    writheTorus 2 3 ≠ writheTorus 3 2 :=
  ⟨crossingNumberTorus_symm 2 3, writheTorus_not_symm⟩

/-- **The two carriers the ladder names**, computed from the formula:
`c(T(2,9)) = 9` and `c(T(3,5)) = 10`. -/
theorem ladder_carrier_crossing_numbers :
    crossingNumberTorus 2 9 = 9 ∧ crossingNumberTorus 3 5 = 10 := by
  refine ⟨?_, ?_⟩ <;> decide

/-- And both are stable under transposition, so neither integer depends on how
the carrier is presented. -/
theorem ladder_carriers_transposition_stable :
    crossingNumberTorus 9 2 = 9 ∧ crossingNumberTorus 5 3 = 10 := by
  refine ⟨?_, ?_⟩ <;> decide

/-! ### Part 2 — anchor dominance -/

/-- Recorded fixed point at the proton anchor (`alpha-em-form-ladder.witness.json`). -/
def predProton : ℝ := 137.035999313169  -- noqa: P31 - RECORDED witness output, not CODATA

/-- Recorded fixed point at the muon anchor. -/
def predMuon : ℝ := 137.036010116763  -- noqa: P31 - RECORDED witness output, not CODATA

/-- The reference value the witness scores against. -/
-- noqa: P31 - the CODATA-2018 Cs-recoil value the RECORDED witness scored
-- against. It must track alpha-em-form-ladder.witness.json, not the table:
-- bumping it here alone would desynchronise the Lean from the residuals
-- below, which were computed against this reference.
def refCodata : ℝ := 137.035999084  -- noqa: P31

/-- Recorded proton-anchored residual, in ppb. -/
def residProtonPpb : ℝ := 1.6723270482102428

/-- Recorded muon-anchored residual, in ppb. -/
def residMuonPpb : ℝ := 80.50996334188073

/-- Residual of the leading term `q[9]_q[10]_q` alone, in ppb — the figure that
must **not** be quoted as the form's accuracy. -/
def residLeadingOnlyPpb : ℝ := -1552805.3

/-- **The anchor gap does not depend on the reference value.**

Subtracting the same reference from both predictions cancels: the difference of
the residuals *is* the difference of the raw predictions.  So the comparison
between the two anchors is untouched by which CODATA vintage is used — relevant
because the ladder witness scores against `137.035999084` while
`alpha-k-per-force-assembly.witness.json` carries `137.035999177`. -/
theorem anchor_gap_eq_prediction_gap (P M C : ℝ) :
    (M - C) - (P - C) = M - P := by ring

/-- **No anchor-blind correction closes the gap.**

A further term appended to the ladder that does not itself depend on the anchor
acts as one affine map `x ↦ s·x + c` on both predictions.  For `s ≠ 0` the two
stay distinct.  So the residual spread cannot be removed by carrying the
α-expansion further, nor by any other anchor-independent ingredient; only an
anchor-*dependent* one can move it. -/
theorem no_anchor_blind_affine_correction_closes_gap
    (P M s c : ℝ) (hne : P ≠ M) (hs : s ≠ 0) :
    s * P + c ≠ s * M + c := by
  intro h
  exact hne (mul_left_cancel₀ hs (by linarith))

/-- **The one escape, named so the exclusion is not over-claimed.**

`s = 0` does equalise the anchors — by discarding the prediction. -/
theorem degenerate_correction_is_vacuous (P M c : ℝ) :
    (0 : ℝ) * P + c = (0 : ℝ) * M + c := by ring

/-- The two recorded predictions are distinct, so the exclusion above applies. -/
theorem predictions_differ : predProton ≠ predMuon := by
  unfold predProton predMuon; norm_num

/-- **The anchor gap dominates the proton-anchored residual** — by more than
`40×` on the recorded values (measured ratio ≈ 47).

This is the quantitative form of "the pin choice is not bookkeeping": it is the
difference between a ~1.7 ppb result and a ~80 ppb one. -/
theorem anchor_gap_dominates_proton_residual :
    residMuonPpb - residProtonPpb > 40 * residProtonPpb := by
  unfold residMuonPpb residProtonPpb; norm_num

/-- **The leading term alone misses by more than `5·10⁵×` the full form's
proton-anchored residual** (measured ratio ≈ 9.3·10⁵).

`q[9]_q[10]_q` is one term of a three-term form; its residual is not the form's
accuracy. -/
theorem leading_term_residual_dwarfs_full_form :
    -residLeadingOnlyPpb > 500000 * residProtonPpb := by
  unfold residLeadingOnlyPpb residProtonPpb; norm_num

end QOU.AlphaEM.FormLadder
