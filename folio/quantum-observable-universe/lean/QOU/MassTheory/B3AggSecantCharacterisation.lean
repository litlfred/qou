/-
# The 3-body cumulant's sign IS the origin-secant gap

`QOU/MassTheory/AggregatorConvexityDichotomy.lean` proves three one-way
implications about `b3Agg Φ g = Φ (3g) − 3 Φ g`, the connected 3-body Ursell
cumulant of a symmetric binding assembled as `B(A) = Φ (m_A · g)`:

* `b3Agg_nonpos_of_concaveOn` — concave through the origin ⇒ `b₃ ≤ 0`;
* `b3Agg_nonneg_of_convexOn`  — convex through the origin ⇒ `b₃ ≥ 0`;
* `b3Agg_linear_eq_zero`      — affine through the origin ⇒ `b₃ = 0`.

Bean `qou-q8vl` lists "the convexity route" as its one **unanalysed** open item.
This file analyses it, and the finding is that convexity is the wrong invariant:
it is sufficient and **strictly unnecessary**, and the exact invariant is a
two-point condition.

## The identity

Write `s x = Φ x / x` for the slope of the secant from the origin. Then for
`g ≠ 0`

    b3Agg Φ g = 3 g · (s (3g) − s g)

exactly, by `field_simp`. So for `g > 0` the **sign of `b₃` is precisely the sign
of the secant gap** — `b₃ ≥ 0` iff the origin-secant slope does not fall between
`g` and `3g`. That is an `iff`, not an implication, and it mentions only two
points.

## Why this matters to the programme

**It narrows the search.** Global convexity on `Ici 0` is a condition at every
pair of points; what `b₃ > 0` actually requires is that one secant slope not
drop across one fixed scale ratio. `convexOn_sufficient_not_necessary` exhibits
`Φ x = x³ − x²`, which is **not** convex on `Ici 0` (it is concave near the
origin) and nevertheless has `b3Agg Φ 1 = 18 > 0`. So a search restricted to
convex aggregators is looking in a strict subset of the admissible set.

**And it names a trap.** Because the characterisation is an `iff`, the
aggregator's secant behaviour across `(g, 3g)` and the sign of `b₃` are the
*same datum*, not two facts that could corroborate one another. Choosing `Φ` so
that `b₃ > 0` is therefore not evidence that `b₃ > 0` — it is the assumption,
rewritten. Under §"NO FITTING, EXCEPT CAL-1/2/3" that is selection against the
target: the choice is of an *object*, no continuous parameter is tuned, and it
reproduces the measured sign by construction. The convexity route is a
derivation route **only** if the secant condition is derived from something that
does not already know `b₃`; otherwise it is the answer restated.

Nothing here touches the magnitude, proposes an aggregator, or disturbs the
production assembly — which is `B = −α log(...)`, concave, hence `b₃ ≤ 0` by the
existing theorem. Scope (a): this narrows and classifies the search; it derives
no replacement.

Generic over nothing — `ℝ` is required, since the statement is about ordering
and division. No `q`, no Markov parameter, no anchor, no CODATA value.

Bean `qou-2ss0`, under `qou-q8vl`.
-/
import Mathlib.Tactic
import Mathlib.Analysis.Convex.Function

namespace QOU.MassTheory.B3AggSecant

open Set

/-- The connected 3-body cumulant, as in `AggregatorConvexityDichotomy`:
`b₃ = B(3) − 3·B(2) = Φ (3g) − 3 Φ g`. Restated here so this file stands alone. -/
noncomputable def b3Agg (Φ : ℝ → ℝ) (g : ℝ) : ℝ := Φ (3 * g) - 3 * Φ g

/-- The slope of the secant from the origin to `(x, Φ x)`. -/
noncomputable def originSecant (Φ : ℝ → ℝ) (x : ℝ) : ℝ := Φ x / x

/-- **The identity.** For `g ≠ 0` the cumulant is the secant gap, scaled by `3g`. -/
theorem b3Agg_eq_secant_gap (Φ : ℝ → ℝ) {g : ℝ} (hg : g ≠ 0) :
    b3Agg Φ g = 3 * g * (originSecant Φ (3 * g) - originSecant Φ g) := by
  unfold b3Agg originSecant
  field_simp

/-- **The characterisation, non-strict.** For `g > 0`, `b₃ ≥ 0` exactly when the
origin-secant slope does not fall from `g` to `3g`. An `iff` — this replaces the
two one-way convexity implications with the condition they were approximating. -/
theorem b3Agg_nonneg_iff_secant_le (Φ : ℝ → ℝ) {g : ℝ} (hg : 0 < g) :
    0 ≤ b3Agg Φ g ↔ originSecant Φ g ≤ originSecant Φ (3 * g) := by
  rw [b3Agg_eq_secant_gap Φ hg.ne', sub_nonneg.symm]
  constructor
  · intro h
    nlinarith [h, hg]
  · intro h
    have h3 : (0:ℝ) < 3 * g := by linarith
    nlinarith [h, h3]

/-- **The characterisation, strict.** The same statement for a strictly positive
cumulant — the sign the AME2020 comparison actually asks for. -/
theorem b3Agg_pos_iff_secant_lt (Φ : ℝ → ℝ) {g : ℝ} (hg : 0 < g) :
    0 < b3Agg Φ g ↔ originSecant Φ g < originSecant Φ (3 * g) := by
  rw [b3Agg_eq_secant_gap Φ hg.ne', sub_pos.symm]
  constructor
  · intro h
    nlinarith [h, hg]
  · intro h
    have h3 : (0:ℝ) < 3 * g := by linarith
    nlinarith [h, h3]

/-- **The cumulant vanishes exactly when the secant slope is unchanged.** The
affine case `b3Agg_linear_eq_zero` is the instance where the slope is constant. -/
theorem b3Agg_eq_zero_iff_secant_eq (Φ : ℝ → ℝ) {g : ℝ} (hg : 0 < g) :
    b3Agg Φ g = 0 ↔ originSecant Φ g = originSecant Φ (3 * g) := by
  rw [b3Agg_eq_secant_gap Φ hg.ne']
  constructor
  · intro h
    have h3 : (3:ℝ) * g ≠ 0 := by positivity
    have := mul_eq_zero.mp h
    rcases this with h' | h'
    · exact absurd h' h3
    · linarith [sub_eq_zero.mp h']
  · intro h
    rw [h]; ring

section Witness

/-- The witness aggregator `Φ x = x³ − x²`. It passes through the origin, is
**concave near it** (`Φ'' x = 6x − 2 < 0` for `x < 1/3`), and yet has a strictly
positive 3-body cumulant. -/
noncomputable def witnessPhi (x : ℝ) : ℝ := x ^ 3 - x ^ 2

theorem witnessPhi_zero : witnessPhi 0 = 0 := by unfold witnessPhi; norm_num

/-- Its cumulant at `g = 1` is `18 > 0`. -/
theorem witnessPhi_b3Agg : b3Agg witnessPhi 1 = 18 := by
  unfold b3Agg witnessPhi; norm_num

theorem witnessPhi_b3Agg_pos : 0 < b3Agg witnessPhi 1 := by
  rw [witnessPhi_b3Agg]; norm_num

/-- **It is not convex on `Ici 0`.** The midpoint of `[0, 1/3]` lies strictly
above the chord: `Φ (1/6) = −5/216` against a chord value of `−8/216`. -/
theorem witnessPhi_not_convexOn : ¬ ConvexOn ℝ (Ici (0:ℝ)) witnessPhi := by
  intro h
  have h0 : (0:ℝ) ∈ Ici (0:ℝ) := by simp
  have h3 : (1/3 : ℝ) ∈ Ici (0:ℝ) := by simp
  have key := h.2 h0 h3 (by norm_num : (0:ℝ) ≤ 1/2) (by norm_num : (0:ℝ) ≤ 1/2)
      (by norm_num : (1:ℝ)/2 + 1/2 = 1)
  simp only [smul_eq_mul] at key
  unfold witnessPhi at key
  norm_num at key

/-- **Convexity is sufficient and strictly unnecessary.** There is an aggregator
through the origin that is *not* convex on `Ici 0` and still has a strictly
positive 3-body cumulant — so a search for `b₃ > 0` restricted to convex
aggregators is searching a strict subset of what the cumulant admits. -/
theorem convexOn_sufficient_not_necessary :
    ∃ Φ : ℝ → ℝ, Φ 0 = 0 ∧ 0 < b3Agg Φ 1 ∧ ¬ ConvexOn ℝ (Ici (0:ℝ)) Φ :=
  ⟨witnessPhi, witnessPhi_zero, witnessPhi_b3Agg_pos, witnessPhi_not_convexOn⟩

end Witness


section Homogeneity

/-!
### The scaling route — where a *derived* curvature could come from

`sign_carries_no_information_beyond_the_secant` says the convexity route is a
derivation only if the secant condition comes from something that does not
already know `b₃`. **Scaling is such a something.** A homogeneity degree is a
structural property of an assembly law, fixed by how the law behaves under
rescaling the bond weight — not a curvature chosen to fix a sign.

Suggested by Aishwarya–Rotem, *New Brunn–Minkowski and functional inequalities
via convexity of entropy* (`arXiv:2311.05446v3`), whose Brunn–Minkowski results
hold for log-concave measures with a **p-homogeneous potential**. The relevance
here is the shape of the hypothesis, not the inequalities: it is a *scaling*
assumption doing the work that a convexity assumption would otherwise do.
-/

/-- **The scaling identity.** If the aggregator scales by a factor `c` across the
ratio `3`, the cumulant is `(c − 3) Φ g` — no convexity, no differentiability,
no hypothesis on `Φ` anywhere else. -/
theorem b3Agg_of_scales (Φ : ℝ → ℝ) (g c : ℝ) (hc : Φ (3 * g) = c * Φ g) :
    b3Agg Φ g = (c - 3) * Φ g := by
  unfold b3Agg; rw [hc]; ring

/-- **The sign is then the scaling factor against 3, and nothing else.** For a
positive aggregator value, `b₃ > 0` exactly when the law scales by more than the
bond count it is scaling across. -/
theorem b3Agg_pos_iff_scale_gt_three (Φ : ℝ → ℝ) {g c : ℝ}
    (hc : Φ (3 * g) = c * Φ g) (hpos : 0 < Φ g) :
    0 < b3Agg Φ g ↔ 3 < c := by
  rw [b3Agg_of_scales Φ g c hc]
  constructor
  · intro h; nlinarith [h, hpos]
  · intro h; nlinarith [h, hpos]

/-- **`b₃` vanishes exactly at `c = 3`** — superposition, the affine boundary
that `b3Agg_linear_eq_zero` is the linear instance of. -/
theorem b3Agg_eq_zero_iff_scale_eq_three (Φ : ℝ → ℝ) {g c : ℝ}
    (hc : Φ (3 * g) = c * Φ g) (hpos : 0 < Φ g) :
    b3Agg Φ g = 0 ↔ c = 3 := by
  rw [b3Agg_of_scales Φ g c hc, mul_eq_zero]
  constructor
  · rintro (h | h)
    · linarith [sub_eq_zero.mp h]
    · exact absurd h hpos.ne'
  · intro h; left; rw [h]; ring

/-- **The power-law reading.** A `p`-homogeneous aggregator scales by `3 ^ p`, so
`b₃ > 0` iff `p > 1`: the assembly must be *superlinear* in the bond count.
`p = 1` is additive superposition and gives exactly zero; `p < 1` — which is
where a concave law such as a logarithm sits — gives a negative cumulant.

So the open question "why should the aggregator curve upward?" becomes the
sharper and more answerable "**is the assembly law superlinear in the bond
count, and why?**" That is a question about scaling, which the framework can in
principle settle without reference to the measured sign. -/
theorem b3Agg_pos_iff_exponent_gt_one (Φ : ℝ → ℝ) {g p : ℝ}
    (hhom : Φ (3 * g) = (3:ℝ) ^ p * Φ g) (hpos : 0 < Φ g) :
    0 < b3Agg Φ g ↔ 1 < p := by
  rw [b3Agg_pos_iff_scale_gt_three Φ hhom hpos]
  constructor
  · intro h
    have : (3:ℝ) ^ (1:ℝ) < (3:ℝ) ^ p := by rwa [Real.rpow_one]
    exact (Real.rpow_lt_rpow_left_iff (by norm_num : (1:ℝ) < 3)).mp this
  · intro h
    have : (3:ℝ) ^ (1:ℝ) < (3:ℝ) ^ p :=
      (Real.rpow_lt_rpow_left_iff (by norm_num : (1:ℝ) < 3)).mpr h
    rwa [Real.rpow_one] at this

end Homogeneity

/-- **The fit statement, as a theorem rather than a caution.** For `g > 0` the
predicate "`Φ` has a non-negative 3-body cumulant at `g`" is *logically
equivalent* to a property of `Φ` alone — its origin-secant slope not falling
across `(g, 3g)`. The two are one proposition, so exhibiting an aggregator with
the second is not independent evidence for the first. -/
theorem sign_carries_no_information_beyond_the_secant (Φ : ℝ → ℝ) {g : ℝ}
    (hg : 0 < g) :
    (0 ≤ b3Agg Φ g) ↔ (originSecant Φ g ≤ originSecant Φ (3 * g)) :=
  b3Agg_nonneg_iff_secant_le Φ hg


/-! ### Linearity of `b3Agg` and exact threshold of `witnessPhi` (`qou-2ss0`) -/

/-- **Linearity of the 3-body cumulant operator (`qou-2ss0`).** `b3Agg` is linear in the
aggregator `Φ` and vanishes identically on every linear function through the origin. -/
theorem b3Agg_linear_comb_and_origin_line (Φ Ψ : ℝ → ℝ) (a b m g : ℝ) :
    b3Agg (fun x => a * Φ x + b * Ψ x) g = a * b3Agg Φ g + b * b3Agg Ψ g ∧
      b3Agg (fun x => m * x) g = 0 := by
  constructor <;> (unfold b3Agg; ring)

/-- **Exact polynomial factorization and nodes of `witnessPhi` (`qou-2ss0`).**
For `witnessPhi x = x³ - x²`, the 3-body cumulant factors as
`b3Agg witnessPhi g = 6 * g² * (4 * g - 1)`, vanishes at the non-zero threshold `g = 1/4`,
and equals `3/2` at `g = 1/2`. -/
theorem witnessPhi_b3Agg_factorization_and_nodes (g : ℝ) :
    b3Agg witnessPhi g = 6 * g ^ 2 * (4 * g - 1) ∧
      b3Agg witnessPhi (1 / 4) = 0 ∧
      b3Agg witnessPhi (1 / 2) = 3 / 2 := by
  refine ⟨by unfold b3Agg witnessPhi; ring,
    by unfold b3Agg witnessPhi; norm_num,
    by unfold b3Agg witnessPhi; norm_num⟩

end QOU.MassTheory.B3AggSecant
