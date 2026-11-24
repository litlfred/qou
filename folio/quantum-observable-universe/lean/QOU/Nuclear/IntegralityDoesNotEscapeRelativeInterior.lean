/-
  The S4 relative-interior exclusion, restated WITHOUT convexity — which is
  exactly why an integer program does not escape it.

  THE SETTING. `operator_selection_what_selects_b3.py` (bean `qou-v7qj`)
  excludes every linear objective from selecting the Borromean element `B_3`
  in the operator-selection LP, by the classical FACE argument: a linear
  functional on a polyhedron attains its extrema on a face, so a
  relative-interior minimiser forces the functional to be constant on the
  whole polyhedron.

  THE OBJECTION THAT ARGUMENT INVITES, and it is a fair one. "Attains its
  extrema on a face" is a statement about a CONVEX POLYHEDRON. An integer
  program's feasible set is a set of lattice points, which is not convex, and
  the object that governs it is the integer hull `conv(P ∩ L)` — whose faces
  need not be faces of `P`. A point in the relative interior of `P` really can
  be a vertex of the integer hull, and then a linear objective does select it.
  So "use an ILP" is a genuine structural escape route and has to be closed
  rather than waved away.

  WHAT THIS FILE PROVES, and it is the reason the escape fails. The face
  argument is stronger than its usual statement: **convexity is not what makes
  it work.** What makes it work is TWO-SIDED REACHABILITY — that the feasible
  set contains a point on each side of `x` along a direction `d`. §1 proves
  that from nothing but linearity, over an ARBITRARY set `S`:

      x minimises f on S,  x + a•d ∈ S,  x - b•d ∈ S,  a,b > 0   ⟹   f d = 0

  No polyhedron, no convexity, no topology, no ambient dimension. So it applies
  verbatim to a lattice feasible set — and a DENSE coefficient ring (which is
  what `ℤ[q₀, q₀⁻¹]` is at the substrate pin, since `q₀ < θ_plastic` is below
  every Pisot number) supplies the two points at any interior point. The
  integer hull adds no faces because there is nothing for it to cut off.

  §1 also carries the ONE-SIDED constructive form, which is what the probe
  actually exhibits: a single feasible point with strictly smaller objective
  refutes minimality outright, no second point needed.

  §2 is reading 1 of "the lattice" — over `ℤ⁶` the question does not arise,
  because `B_3` is not in the feasible set at all (its coordinates are
  `ℤ`-Laurent polynomials in `q` at `q₀`, and are not integers).

  §3 is the exact criterion behind the Pisot test, and it is the part that
  keeps the probe free of any decimal expansion of `θ`: `x³ - x` is strictly
  monotone on `[1, ∞)`, so `q₀ < θ` is EXACTLY the sign of `q₀³ - q₀ - 1`.

  🛑 NOT PROVED HERE, and not provable from these ingredients:

  * That `ℤ[q]` is discrete iff `q` is Pisot. That is the classical theorem the
    argument cites; it is not formalised in this corpus and is not attempted.
  * That the smallest Pisot number is the plastic number (Siegel 1944). Also
    cited, also not formalised. §3 proves only the reduction of `q₀ < θ` to a
    sign, given that `θ` is a root.
  * Anything about `B_3` specifically. The numbers — min slack `0.3425`, the
    beating lattice point at `0.8642` against `0.9986` — are MEASUREMENTS in
    the probe. What is here is the implication they feed.

  Sorry-free. No `axiom`, no conditional class, no `native_decide`.

  -- Ref: [leitner2026] computations/meson/operator_selection_ilp_does_not_escape_s4.py
  -- Ref: [leitner2026] computations/meson/operator_selection_what_selects_b3.py
  -- Ref: [leitner2026] docs/audits/2026-08-24-operator-selection-lp-objective-defect.md
-/
import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace QOU.QBeta.IntegralityDoesNotEscapeRelativeInterior

/-! ### 1. The face argument without convexity -/

section FaceArgument

variable {V : Type*} [AddCommGroup V] [Module ℝ V]

/-- **A linear functional minimised at a two-sided-reachable point vanishes on
that direction.**

This is the S4 face argument with the convexity removed, and removing it is the
whole point: `S` here is an ARBITRARY set, so the statement applies to a
polyhedron and to a set of lattice points alike. What does the work is not that
`S` is convex but that it contains a point on each side of `x` along `d`.

Consequence for the ILP question: an integer program cannot escape S4 by
non-convexity, because non-convexity was never what the argument used. It can
only escape by failing to reach both sides — i.e. by the lattice being COARSE
enough near `x` to have no feasible point on one side. A dense coefficient ring
does not do that. -/
theorem linear_min_two_sided_kills_direction
    (f : V →ₗ[ℝ] ℝ) (S : Set V) (x d : V) (a b : ℝ)
    (ha : 0 < a) (hb : 0 < b)
    (hxa : x + a • d ∈ S) (hxb : x - b • d ∈ S)
    (hmin : ∀ y ∈ S, f x ≤ f y) :
    f d = 0 := by
  have h₁ : f x ≤ f x + a * f d := by
    have := hmin _ hxa
    simpa [map_add, map_smul, smul_eq_mul] using this
  have h₂ : f x ≤ f x - b * f d := by
    have := hmin _ hxb
    simpa [map_sub, map_smul, smul_eq_mul] using this
  have hge : 0 ≤ a * f d := by linarith
  have hle : b * f d ≤ 0 := by linarith
  have h1 : 0 ≤ f d := by nlinarith
  have h2 : f d ≤ 0 := by nlinarith
  linarith

/-- **The one-sided constructive form: a single better feasible point refutes
minimality.**

This is what the probe exhibits at `[A6]` — it does not need a two-sided
argument, only one feasible lattice point whose objective is strictly lower.
Stated separately because a constructive refutation is a different (and
cheaper) obligation than the structural one above, and conflating them is how
a measurement gets reported as a theorem. -/
theorem not_minimal_of_descent_direction
    (f : V →ₗ[ℝ] ℝ) (S : Set V) (x d : V) (a : ℝ)
    (ha : 0 < a) (hxa : x + a • d ∈ S) (hfd : f d < 0) :
    ¬ (∀ y ∈ S, f x ≤ f y) := by
  intro hmin
  have := hmin _ hxa
  have hlt : f (x + a • d) < f x := by
    have : f (x + a • d) = f x + a * f d := by
      simp [map_add, map_smul, smul_eq_mul]
    rw [this]
    nlinarith
  linarith

/-- **Nothing but a functional vanishing on `d` can have `x` optimal**, which
is the S4 conclusion stated as a dichotomy: either the objective is blind to
the direction, or `x` is not the optimum. -/
theorem min_iff_blind_on_two_sided_direction
    (f : V →ₗ[ℝ] ℝ) (S : Set V) (x d : V) (a b : ℝ)
    (ha : 0 < a) (hb : 0 < b)
    (hxa : x + a • d ∈ S) (hxb : x - b • d ∈ S)
    (hmin : ∀ y ∈ S, f x ≤ f y) :
    f (a • d) = 0 ∧ f (b • d) = 0 := by
  have h := linear_min_two_sided_kills_direction f S x d a b ha hb hxa hxb hmin
  constructor <;> simp [map_smul, smul_eq_mul, h]

end FaceArgument

/-! ### 2. Reading 1 — a non-integer coordinate is not in the integer lattice -/

/-- **`B_3` is not in `ℤ⁶`, so an ILP over `ℤ⁶` excludes it rather than failing
to select it.**

Stated generally: a point one of whose coordinates is not the image of an
integer is not in the integer lattice. Trivial, and worth having explicitly
because it is a *different kind* of negative from §1 — §1 says a linear
objective cannot pick `B_3` out of the feasible set, this says `B_3` is not in
the feasible set. An agent reading only the first could reasonably think a
cleverer objective might help. -/
theorem not_mem_integer_lattice_of_coord_not_integral
    {ι : Type*} (x : ι → ℝ) (i : ι) (hi : ∀ n : ℤ, x i ≠ (n : ℝ)) :
    ¬ ∃ y : ι → ℤ, ∀ j, x j = (y j : ℝ) := by
  rintro ⟨y, hy⟩
  exact hi (y i) (hy i)

/-! ### 3. The exact Pisot sign test -/

/-- **`x³ - x` is strictly increasing on `[1, ∞)`.**

The cubic `x³ - x - 1` has derivative `3x² - 1 > 0` there; this is the
order-theoretic form of that, proved directly so no calculus is needed. -/
theorem cube_sub_self_strictMono (x y : ℝ) (hx : 1 ≤ x) (hxy : x < y) :
    x ^ 3 - x < y ^ 3 - y := by
  have hy : (1 : ℝ) ≤ y := le_trans hx hxy.le
  have hfac : y ^ 3 - y - (x ^ 3 - x) = (y - x) * (y ^ 2 + x * y + x ^ 2 - 1) := by
    ring
  have hpos : 0 < (y - x) * (y ^ 2 + x * y + x ^ 2 - 1) := by
    apply mul_pos (sub_pos.mpr hxy)
    nlinarith
  linarith [hfac, hpos]

/-- **`q < θ` is EXACTLY the sign of `q³ - q - 1`, given that `θ` is the root.**

This is what lets the probe test "is `q₀` below the smallest Pisot number"
with a single exact rational comparison, and make no floating-point claim
about `θ = 1.324717957...` at all. The hypothesis is only that `θ` is a root
of `x³ - x - 1` with `θ ≥ 1` — Siegel's theorem that this particular root is
the smallest Pisot number is CITED by the probe, not proved here. -/
theorem lt_root_of_cubic_neg (q θ : ℝ) (_hq : 1 ≤ q) (hθ : 1 ≤ θ)
    (hroot : θ ^ 3 - θ - 1 = 0) (hneg : q ^ 3 - q - 1 < 0) :
    q < θ := by
  by_contra hge
  push_neg at hge          -- θ ≤ q
  rcases eq_or_lt_of_le hge with heq | hlt
  · rw [← heq] at hneg; linarith
  · have := cube_sub_self_strictMono θ q hθ hlt
    linarith

/-- The converse direction, so the test is genuinely an iff and a reader
cannot mistake it for one-way evidence. -/
theorem cubic_neg_of_lt_root (q θ : ℝ) (hq : 1 ≤ q) (_hθ : 1 ≤ θ)
    (hroot : θ ^ 3 - θ - 1 = 0) (hlt : q < θ) :
    q ^ 3 - q - 1 < 0 := by
  have := cube_sub_self_strictMono q θ hq hlt
  linarith

end QOU.QBeta.IntegralityDoesNotEscapeRelativeInterior
