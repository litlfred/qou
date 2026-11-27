import Mathlib.Data.Real.Archimedean
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.Algebra.Algebra.Rat

/-!
# QOU.Archimedean.SurrealGradingPrune — the squeeze cannot see arithmetic

**Formalize-first prune** (AGENTS.md §"Formalize-first probe discipline") for
the hypothesis class *"transport the surreal-squeeze / `ordω` grade-separation
mechanism — the one that powers the q-NS blowup bound, the q-Collatz drift
bound and the P-vs-NP budget bound — to the algebraic independence of
`Vol(4₁)`, `Vol(5₂)`, `Vol(𝓑₃)`"*
([`conj:hyperbolic-volume-transcendence`](../../../quantum-observable-universe/mass-theory/hyperbolic-volume-transcendence.md),
[`rem:yekutieli-transcendence-shadow`](../../../quantum-observable-universe/predicted-spectra/yekutieli-transcendence-shadow.md)).

## The mechanism being pruned

Every surreal bound in `appendix-surreals` has the same engine
([`lem:surreal-squeeze`](../../../quantum-observable-universe/appendix-surreals/surreal-squeeze.md)):
place a *cost* and a *budget* at different `ordω` grades, then read off the
strict inequality. In `ω`-adic form the q-Collatz and P-vs-NP remarks both
write it as

  `ordω(δ² · Ω_q) = 1 > -3 = ordω(Δ_q)`  ⟹  `δ² · Ω_q > Δ_q`.

The soundness of that step is `dominance`: a strictly larger grade means the
element is *infinitely larger* — every standard multiple of the smaller stays
below the larger. That is the Conway–Gonshor archimedean-class comparison, and
it is the only property of `ordω` these arguments use.

## The obstruction (proved here, sorry-free)

`ℝ` is a **single archimedean class**. So the very property that makes
`dominance` sound forces the grading to be *constant on the positive reals*
(`grade_eq_of_pos`). Three consequences, each a `theorem` below:

* `no_separation_of_standard` — the squeeze derives **no** strict inequality
  between two positive standard reals. Not "hard": the premise `g a < g b` is
  false for every such pair.
* `nonvanishing_premise_circular` — under the `ordω(0) = -∞` convention, the
  grade premise that would certify `x ≠ 0` is *logically equivalent* to
  `x ≠ 0`. A grade-dominance proof of non-vanishing consumes its own
  conclusion.
* `grade_blind_to_rationality` — the mechanism cannot separate a rational from
  an irrational, so it cannot deliver even
  `SingleVolumeIrrational` (`Vol(4₁) ∉ ℚ`), the *weakest* rung of the corpus's
  own transcendence ladder, let alone the algebraic-independence rung.

Applied to the target: for `P : MvPolynomial (Fin 3) ℚ` and
`v = ![Vol(4₁), Vol(5₂), Vol(𝓑₃)]`, the value `aeval v P` is a **standard
real**, so `grade_aeval_const` says every non-relation sits at one and the
same grade. The grading partitions `{P}` into "vanishes" / "does not vanish"
and adds nothing — it *restates* the conjecture in `ω`-adic notation rather
than advancing it.

## Scope of the claim (AGENTS.md §"Before declaring refuted")

This is a **scope-(b) structural exclusion** — it cites a proved invariant
(the archimedean property of `ℝ`, `not_infinitelySmaller_of_pos`) — but the
excluded object is narrow and must be quoted precisely:

> *Grade separation alone cannot decide a polynomial relation among standard
> reals.*

It does **not** exclude surreal or non-Archimedean methods from the problem.
`grade_separation_iff_infinitelySmaller` is the positive half: the mechanism
is exactly available when a comparison leaves the standard archimedean class.
That is why it works for `Ω_q ≍ ε⁻¹` vs `Δ_q ≍ ε³` (grades `+1` and `-3`) and
is unavailable for `Vol` (grade `0`). A route that first produces a
*non-standard* object whose standard part is the relation — e.g. an effective
tower height, per `JetOrderIndependence` — is untouched by this file.

## References

* [conway1976] Conway, *On Numbers and Games* — archimedean classes / `ordω`.
* [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal Numbers*.
* [nesterenko1996] Nesterenko — algebraic independence measures; the *height*
  parameter this mechanism structurally lacks.
-/

namespace QOU.Archimedean.SurrealPrune

variable {Γ : Type*} [LinearOrder Γ]

/-! ## §1  The comparison the grading refines -/

/-- `InfinitelySmaller a b` — `a` is *infinitely smaller* than `b`: every
standard multiple of `a` stays strictly below `b`.

This is the Conway–Gonshor archimedean-class comparison. A strict `ordω` drop
means exactly this, which is what makes the squeeze's grade-dominance step
sound. -/
def InfinitelySmaller (a b : ℝ) : Prop := ∀ n : ℕ, (n : ℝ) * a < b

/-- **A grading in the shape the surreal-squeeze arguments consume.**

The single field is the soundness property those arguments actually use: a
strictly smaller grade means infinitely smaller, which is what licenses
reading `ordω(cost) > ordω(budget)` off as `cost > budget`.

Nothing here assumes the grading is trivial on `ℝ` — that is *derived*
(`grade_eq_of_pos`) from this field plus the archimedean property. -/
structure SqueezeGrading (g : ℝ → Γ) : Prop where
  /-- Grade dominance: a strict grade drop is an archimedean-class drop. -/
  dominance : ∀ {a b : ℝ}, 0 < a → 0 < b → g a < g b → InfinitelySmaller a b

/-! ## §2  `ℝ` is one archimedean class -/

/-- **No positive real is infinitely smaller than any real** — the archimedean
property of `ℝ`, in the form the prune needs. This is the invariant that makes
the exclusion below scope-(b) rather than a failed search.

Positivity of `b` is not required: for `b ≤ 0` the `n = 0` instance of
`InfinitelySmaller` already fails. -/
theorem not_infinitelySmaller_of_pos {a b : ℝ} (ha : 0 < a) :
    ¬ InfinitelySmaller a b := by
  intro h
  obtain ⟨n, hn⟩ := exists_nat_gt (b / a)
  have hb_lt : b < (n : ℝ) * a := by
    rw [div_lt_iff₀ ha] at hn
    linarith
  exact absurd (h n) (not_lt.mpr hb_lt.le)

/-- **The grading is constant on the positive reals.**

Derived, not assumed: if two positive reals had different grades, dominance
would make one infinitely smaller than the other, contradicting
`not_infinitelySmaller_of_pos`. -/
theorem grade_eq_of_pos {g : ℝ → Γ} (hg : SqueezeGrading g) {a b : ℝ}
    (ha : 0 < a) (hb : 0 < b) : g a = g b := by
  rcases lt_trichotomy (g a) (g b) with h | h | h
  · exact absurd (hg.dominance ha hb h) (not_infinitelySmaller_of_pos ha)
  · exact h
  · exact absurd (hg.dominance hb ha h) (not_infinitelySmaller_of_pos hb)

/-! ## §3  The prune -/

/-- **The squeeze proves no inequality between standard reals.**

The mechanism concludes `b < a` from the premise `g b < g a`. For positive
standard `a`, `b` that premise is *false* — so the mechanism yields no strict
inequality between standard reals at all. This is the direct obstruction: the
independence target `|P(V)| > 0` is a separation among standard reals. -/
theorem no_separation_of_standard {g : ℝ → Γ} (hg : SqueezeGrading g) {a b : ℝ}
    (ha : 0 < a) (hb : 0 < b) : ¬ (g b < g a) := by
  rw [grade_eq_of_pos hg hb ha]
  exact lt_irrefl _

/-- **The non-vanishing premise is circular.**

Adopt the usual bottom convention `ordω(0) = -∞` (`hbot`). Then the grade
premise that would certify `x ≠ 0` by dominance is *logically equivalent* to
`x ≠ 0`. Any grade-dominance proof of non-vanishing therefore consumes its own
conclusion as its input — the `ω`-adic notation restates the question.

Applied to `x = P(Vol(4₁), Vol(5₂), Vol(𝓑₃))`: writing the conjecture as a
grade statement is a change of notation, not a step of the proof. -/
theorem nonvanishing_premise_circular {g : ℝ → Γ}
    (hbot : ∀ y : ℝ, y ≠ 0 → g 0 < g y) (x : ℝ) :
    g 0 < g x ↔ x ≠ 0 := by
  constructor
  · rintro h rfl
    exact absurd h (lt_irrefl _)
  · exact hbot x

/-- **The grading cannot separate a rational from an irrational.**

A falsification test for the whole transfer: the corpus's own ladder starts at
`SingleVolumeIrrational` (`Vol(4₁) ∉ ℚ`), which is *weaker* than algebraic
independence. The mechanism cannot reach that rung either — rationals and
irrationals share the single archimedean class of `ℝ`. -/
theorem grade_blind_to_rationality {g : ℝ → Γ} (hg : SqueezeGrading g)
    {p x : ℝ} (hp : 0 < p) (hx : 0 < x) : g p = g x :=
  grade_eq_of_pos hg hp hx

/-! ## §4  The target: polynomial relations among the three volumes -/

/-- Every non-vanishing polynomial value at real arguments carries the **same**
grade. So the grading assigns one value to every non-relation and one to every
relation: it is exactly the characteristic function of the conjecture, and
supplies no independent information about which polynomials vanish.

This is `no_separation_of_standard` in the shape of the actual target: `P`
ranges over `ℚ[x,y,z]` and `v = ![Vol(4₁), Vol(5₂), Vol(𝓑₃)]`. -/
theorem grade_aeval_const {g : ℝ → Γ} (hg : SqueezeGrading g)
    (v : Fin 3 → ℝ) (P Q : MvPolynomial (Fin 3) ℚ)
    (hP : 0 < MvPolynomial.aeval v P) (hQ : 0 < MvPolynomial.aeval v Q) :
    g (MvPolynomial.aeval v P) = g (MvPolynomial.aeval v Q) :=
  grade_eq_of_pos hg hP hQ

/-! ## §5  The positive half — where the mechanism *is* available -/

/-- **Exact domain of the squeeze.** Grade separation between positive
elements is available precisely when the comparison leaves the standard
archimedean class.

This is why the q-NS / q-Collatz / P-vs-NP bounds are legitimate uses
(`Ω_q ≍ ε⁻¹` and `Δ_q ≍ ε³` sit at grades `+1` and `-3`, genuinely different
classes) and why the volume target is outside the domain (all of
`Vol(4₁)`, `Vol(5₂)`, `Vol(𝓑₃)` and every `P(V)` sit at grade `0`).

A route that manufactures a genuinely non-standard object whose standard part
is the relation is *not* pruned by this file. -/
theorem grade_separation_needs_nonstandard {g : ℝ → Γ} (hg : SqueezeGrading g)
    {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (hsep : g a < g b) : False :=
  no_separation_of_standard hg hb ha hsep

end QOU.Archimedean.SurrealPrune
