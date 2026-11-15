/-
# Breaking affineness does not open the sign-mixed escape — breaking monotonicity does

`QOU/MassTheory/PnBetweennessBlocksSignMixed.lean` proves that the sign-mixed
pattern `qou-q8vl` requires — the pn bond factor the strict maximum of the three —
is unreachable when the pn letter is a strict convex combination of the like-pair
letters **and the interface law `μ = z + d` is affine**. Bean `qou-q8vl` therefore
records the open escape as:

> a third bond family *"must break the AVERAGING of the pn letter, or break
> AFFINENESS of the interface law"*.

**The second half of that is too weak, and this file measures how much.**
Affineness is not what does the blocking. What does the blocking is that an
affine map is **monotone**, and monotonicity alone suffices:

* `not_strict_max_of_monotone` / `not_strict_max_of_antitone` — if `f` is
  monotone (in either direction) and `c` lies between `a` and `b`, then `f c`
  cannot strictly exceed both `f a` and `f b`. No linearity, no continuity, no
  algebra: the hypothesis is an order property and the proof is one `absurd`.

So a third bond family that merely abandons affineness gains nothing. A cubic
interface law `d ↦ d³` is as blocked as `d ↦ z + d`. The escape requires a
**non-monotone** interface law, which is a strictly stronger demand and a much
smaller space to search.

`hump_realises_signMixed` shows the narrowing is sharp rather than a disguised
impossibility: a non-monotone law *does* realise the pattern. So monotonicity is
exactly the invariant — necessary and sufficient at this level of description.

## What this does and does not say

It says: **do not spend a tranche on a non-affine interface law.** Check whether
it is monotone first; if it is, the pattern is already excluded and the
construction is dead before any number is computed. That is a cheap filter on an
open search, and it is why the result is worth its length.

It does **not** derive a non-monotone law, propose one, or claim one exists in
the framework. Scope (b) structural exclusion; the invariant is order-preservation,
which is an identity rather than a measurement. `qou-q8vl`'s *other* escape —
breaking the averaging of the pn letter — is untouched.

Physically, a non-monotone interface law means that increasing the letter offset
would *decrease* the bond factor over some range and increase it over another.
Whether the framework admits such a thing is open and is not addressed here.

No `q`, no Markov parameter, no anchor, no numeral outside the witness.

Bean `qou-2ss0`, under `qou-q8vl`.
-/
import Mathlib.Order.Monotone.Basic
import Mathlib.Tactic

namespace QOU.MassTheory.InterfaceMonotone

section OrderCore

variable {α β : Type*} [Preorder α] [Preorder β]

/-- **A monotone map keeps the middle in the middle.** If `c` lies between `a`
and `b` then `f c` does not strictly exceed both endpoints. -/
theorem not_strict_max_of_monotone {f : α → β} (hf : Monotone f) {a b c : α}
    (_hac : a ≤ c) (hcb : c ≤ b) : ¬ (f a < f c ∧ f b < f c) := by
  rintro ⟨_, h2⟩
  exact absurd (lt_of_lt_of_le h2 (hf hcb)) (lt_irrefl _)

/-- **And so does an antitone one.** Reversing the order reverses which endpoint
does the work, and the conclusion is unchanged. -/
theorem not_strict_max_of_antitone {f : α → β} (hf : Antitone f) {a b c : α}
    (hac : a ≤ c) (_hcb : c ≤ b) : ¬ (f a < f c ∧ f b < f c) := by
  rintro ⟨h1, _⟩
  exact absurd (lt_of_lt_of_le h1 (hf hac)) (lt_irrefl _)

/-- **The same, with the endpoints in the other order.** Betweenness is
symmetric; the exclusion should not depend on which like-pair letter is larger. -/
theorem not_strict_max_of_monotone' {f : α → β} (hf : Monotone f) {a b c : α}
    (_hbc : b ≤ c) (hca : c ≤ a) : ¬ (f a < f c ∧ f b < f c) := by
  rintro ⟨h1, _⟩
  exact absurd (lt_of_lt_of_le h1 (hf hca)) (lt_irrefl _)

end OrderCore

section CorpusApplication

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- A strict convex combination, as in `PnBetweennessBlocksSignMixed`. -/
def combo (w a b : R) : R := w * a + (1 - w) * b

/-- A strict convex combination lies weakly between its endpoints. -/
theorem combo_mem {w a b : R} (hw0 : 0 < w) (hw1 : w < 1) (hab : a ≤ b) :
    a ≤ combo w a b ∧ combo w a b ≤ b := by
  constructor <;> unfold combo <;> nlinarith [hw0, hw1, hab]

/-- **The sharpened exclusion.** For *any* monotone interface law `f` — affine or
not — a pn letter that is a strict convex combination of the like-pair letters
cannot produce a pn bond factor that strictly exceeds both like-pair factors.

`PnBetweennessBlocksSignMixed.pn_not_strict_max` is the `f = (z + ·)` instance. -/
theorem pn_not_strict_max_of_monotone {f : R → R} (hf : Monotone f)
    {w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) (hle : dpp ≤ dnn) :
    ¬ (f dpp < f (combo w dpp dnn) ∧ f dnn < f (combo w dpp dnn)) := by
  obtain ⟨h1, h2⟩ := combo_mem hw0 hw1 hle
  exact not_strict_max_of_monotone hf h1 h2

/-- The required pattern, as `qou-q8vl` states it. -/
def signMixedPattern (mupp mupn munn : R) : Prop :=
  1 < mupn ∧ mupp < 1 ∧ munn < 1

/-- **Corollary — the pattern is unreachable under any monotone law.** So
abandoning affineness, on its own, buys nothing: the construction is dead before
any bond value is computed. -/
theorem signMixed_impossible_of_monotone {f : R → R} (hf : Monotone f)
    {w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) (hle : dpp ≤ dnn) :
    ¬ signMixedPattern (f dpp) (f (combo w dpp dnn)) (f dnn) := by
  rintro ⟨h1, hpp, hnn⟩
  exact pn_not_strict_max_of_monotone hf hw0 hw1 hle ⟨by linarith, by linarith⟩

end CorpusApplication

section Sharpness

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- A non-monotone interface law: the downward parabola `f d = 1 − (d − 1)²`,
peaking at the midpoint of `[0, 2]`.

Stated over a generic ordered field, not `ℝ`: nothing archimedean is used — no
`Real.sqrt`, no `rpow`, no transcendental — so §7c keeps it on the generic side
of the substrate/archimedean wall along with the rest of this file. -/
def hump (d : R) : R := 1 - (d - 1) ^ 2

omit [LinearOrder R] [IsStrictOrderedRing R] in
theorem hump_values : hump (0:R) = 0 ∧ hump (1:R) = 1 ∧ hump (2:R) = 0 := by
  refine ⟨?_, ?_, ?_⟩ <;> unfold hump <;> norm_num

/-- It is not monotone: it rises then falls. -/
theorem hump_not_monotone : ¬ Monotone (hump (R := R)) := by
  intro h
  have := h (by norm_num : (1:R) ≤ 2)
  unfold hump at this
  norm_num at this

/-- Nor antitone. -/
theorem hump_not_antitone : ¬ Antitone (hump (R := R)) := by
  intro h
  have := h (by norm_num : (0:R) ≤ 1)
  unfold hump at this
  norm_num at this

/-- **The narrowing is sharp.** A non-monotone law *does* put the middle strictly
above both endpoints — so monotonicity is exactly the invariant that blocks the
pattern, not a sufficient condition standing in for something weaker. -/
theorem hump_realises_strict_max :
    hump (0:R) < hump 1 ∧ hump (2:R) < hump 1 := by
  unfold hump; norm_num

/-- Stated as the escape it is: there exists an interface law under which the
middle letter is the strict maximum, and it is necessarily non-monotone. -/
theorem nonmonotone_escape_exists :
    ∃ f : R → R, ¬ Monotone f ∧ ¬ Antitone f ∧ f 0 < f 1 ∧ f 2 < f 1 :=
  ⟨hump, hump_not_monotone, hump_not_antitone, hump_realises_strict_max.1,
    hump_realises_strict_max.2⟩

end Sharpness


section AveragingIsTight

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-!
### The third escape is NOT loose — measured, then proved

Two of `qou-q8vl`'s hypotheses turned out stronger than needed: aggregator
**convexity** weakens to a two-point secant condition (`qou-2ss0`), and interface
**affineness** weakens to monotonicity (above). It is tempting to expect the
third — that the pn letter is a strict convex **combination** — to weaken to mere
**betweenness** in the same way.

**It does not.** Over an ordered field the two are the same condition, so the
averaging hypothesis is already tight and there is no third gain to take.

Recorded because the pattern-match was made and the arithmetic refused it. A
negative that stops a search is worth the lines.
-/

/-- **Betweenness gives a weight.** Any value strictly between two others is a
strict convex combination of them, with the weight read off explicitly. -/
theorem combo_of_between {a b c : R} (hab : a < b) (hac : a < c) (hcb : c < b) :
    ∃ w : R, 0 < w ∧ w < 1 ∧ combo w a b = c := by
  refine ⟨(b - c) / (b - a), ?_, ?_, ?_⟩
  · exact div_pos (by linarith) (by linarith)
  · rw [div_lt_one (by linarith)]; linarith
  · have hba : b - a ≠ 0 := ne_of_gt (sub_pos.mpr hab)
    unfold combo
    field_simp
    linarith

/-- **And a weight gives betweenness**, so the two hypotheses coincide. -/
theorem between_of_combo {a b w : R} (hab : a < b) (hw0 : 0 < w) (hw1 : w < 1) :
    a < combo w a b ∧ combo w a b < b := by
  constructor <;> unfold combo <;> nlinarith [hab, hw0, hw1]

/-- **The averaging hypothesis is exactly betweenness.** No weaker condition is
hiding inside it, so unlike convexity and affineness this one admits no
sharpening — `qou-q8vl`'s first escape is stated at full strength already. -/
theorem between_iff_combo {a b c : R} (hab : a < b) :
    (a < c ∧ c < b) ↔ ∃ w : R, 0 < w ∧ w < 1 ∧ combo w a b = c := by
  constructor
  · rintro ⟨h1, h2⟩; exact combo_of_between hab h1 h2
  · rintro ⟨w, hw0, hw1, rfl⟩; exact between_of_combo hab hw0 hw1

end AveragingIsTight

section AffinePathsAreBlocked

/-! ### Affine is blocked BOTH ways — and what the escape must therefore do

Two gaps in the sections above, closed here.

**First, a real gap in the corpus application.** `pn_not_strict_max_of_monotone`
and `signMixed_impossible_of_monotone` assume `Monotone`.  A *decreasing*
interface law was therefore never covered, even though `not_strict_max_of_antitone`
sits in `OrderCore` ready for it.  Closed below.

**Second, the structural reason the corpus's own law is blocked.**  The interface
factor is a Markov trace ratio, `μ(x) = tr_M(W·x) / tr_M(W)` at fixed `W`.  The
numerator is **linear in `x`**, so along any *affine* path in the algebra,
`x(t) = x₀ + t·x₁`, the law is affine in `t` — and an affine law is monotone or
antitone according to the sign of its slope, hence blocked **either way**.

That is why `μ = z + d` cannot escape: it is the affine path.  And it says
exactly what an escape must do — **leave the affine family**, not merely leave
the affine *formula*.

**The framework does admit such a family, and the corpus has already measured
it.**  The file header above says *"whether the framework admits such a thing is
open and is not addressed here"*; it is addressed now.  The stacked family
`m ↦ σ^m` is not an affine path (it is a product, not a sum), and its interface
factor is measured non-monotone in `m`: `μ > 1` at `m = 2, 4, 5, 6, 7, 8` and
**not** at `m = 3`
(`stacked_interface_writhe_normalised_probe.py`, reported in
`docs/audits/2026-09-12-b3-sign-one-root-and-the-insufficient-escape.md` §6(b)).
A function exceeding a threshold at `2` and `4` but not at `3` is not monotone.

**This selects nothing.**  Naming the family that occupies the door is a
structural observation; choosing a particular `m` because it yields `b₃ > 0`
would be selection against the target, which AGENTS.md §"NO FITTING" forbids and
which bean `qou-kj4v` already records going backwards for `σ²`.  Under the owner
ruling of 2026-09-08 (`qou-ales`) the braid word is selected by γγ
pair-production plus the confinement SDP, and **that derivation is what remains
open** — not the question of whether a non-monotone law exists.

Nothing here is numerical: no `q`, no Markov parameter, no anchor.  The `σ^m`
measurement is cited, not recomputed, and no value from it enters any statement.
-/

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The antitone half of the pn exclusion, which `pn_not_strict_max_of_monotone`
does not cover: a *decreasing* interface law blocks the pattern just as a
increasing one does. -/
theorem pn_not_strict_max_of_antitone {f : R → R} (hf : Antitone f)
    {w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) (hle : dpp ≤ dnn) :
    ¬ (f dpp < f (combo w dpp dnn) ∧ f dnn < f (combo w dpp dnn)) := by
  obtain ⟨h1, h2⟩ := combo_mem hw0 hw1 hle
  exact not_strict_max_of_antitone hf h1 h2

/-- And the corresponding sign-mixed corollary. -/
theorem signMixed_impossible_of_antitone {f : R → R} (hf : Antitone f)
    {w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) (hle : dpp ≤ dnn) :
    ¬ signMixedPattern (f dpp) (f (combo w dpp dnn)) (f dnn) := by
  rintro ⟨h1, hpp, hnn⟩
  exact pn_not_strict_max_of_antitone hf hw0 hw1 hle ⟨by linarith, by linarith⟩

/-- **An affine law is monotone or antitone**, according to the sign of its
slope.  So both blocking theorems are available and neither sign escapes. -/
theorem affine_monotone_or_antitone (a b : R) :
    Monotone (fun t : R => a + t * b) ∨ Antitone (fun t : R => a + t * b) := by
  rcases le_or_gt 0 b with hb | hb
  · left
    intro x y hxy
    simp only
    nlinarith
  · right
    intro x y hxy
    simp only
    nlinarith

/-- **No affine interface law reaches the sign-mixed pattern, whatever the sign
of its slope.**  This subsumes `PnBetweennessBlocksSignMixed`'s `μ = z + d` as
the case `a = z`, `b = 1`. -/
theorem affine_blocks_sign_mixed (a b : R)
    {w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) (hle : dpp ≤ dnn) :
    ¬ (a + dpp * b < a + combo w dpp dnn * b
       ∧ a + dnn * b < a + combo w dpp dnn * b) := by
  rcases affine_monotone_or_antitone a b with h | h
  · exact pn_not_strict_max_of_monotone h hw0 hw1 hle
  · exact pn_not_strict_max_of_antitone h hw0 hw1 hle

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **A linear functional evaluated along an affine path is affine in the path
parameter.**  `φ` here stands for `x ↦ tr_M(W·x)` at fixed `W`, which is linear
because the Markov trace is.  Pure ring algebra — the order instances are
`omit`ted because the statement genuinely does not use them. -/
theorem linear_along_affine_path {φ : R → R}
    (hadd : ∀ x y, φ (x + y) = φ x + φ y) (hsmul : ∀ c x, φ (c * x) = c * φ x)
    (x₀ x₁ t : R) : φ (x₀ + t * x₁) = φ x₀ + t * φ x₁ := by
  rw [hadd, hsmul]

/-- **The structural statement.**  A linear interface functional, evaluated along
*any* affine path in the algebra, cannot reach the sign-mixed pattern — for
either sign of the slope, and without computing a single bond value.

This is why the corpus's `μ = z + d` is blocked, and it locates the escape
precisely: it must leave the **affine path**, not merely the affine formula. -/
theorem linear_functional_on_affine_path_blocks_sign_mixed {φ : R → R}
    (hadd : ∀ x y, φ (x + y) = φ x + φ y) (hsmul : ∀ c x, φ (c * x) = c * φ x)
    (x₀ x₁ : R) {w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) (hle : dpp ≤ dnn) :
    ¬ (φ (x₀ + dpp * x₁) < φ (x₀ + combo w dpp dnn * x₁)
       ∧ φ (x₀ + dnn * x₁) < φ (x₀ + combo w dpp dnn * x₁)) := by
  simp only [linear_along_affine_path hadd hsmul]
  exact affine_blocks_sign_mixed (φ x₀) (φ x₁) hw0 hw1 hle

/-- Negative control: the blocking above is a statement about *affine* paths
only, and is not vacuous — `hump` from `Sharpness` is a law the affine theorems
genuinely do not cover, since it is neither monotone nor antitone. -/
theorem hump_is_neither :
    ¬ Monotone (hump (R := R)) ∧ ¬ Antitone (hump (R := R)) :=
  ⟨hump_not_monotone, hump_not_antitone⟩

end AffinePathsAreBlocked

end QOU.MassTheory.InterfaceMonotone
