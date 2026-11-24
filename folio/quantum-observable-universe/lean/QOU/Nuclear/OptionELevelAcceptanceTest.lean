/-
# The Option E acceptance test, formalised

`qou-99qc`. The decay ansatz is `Q_β = |ε(Δ)| · E₀`, with `Δ` an element of
`H₃(q)` and `ε` a functional. Convention D admits exactly two `ε`, the Wenzl
levels `r = 1` (the augmentation, `z = q`) and `r = 2` (`z_D = q³/(q²+1)`) —
`QOU.QBeta.ConventionDAdmissibleRoots` and `QOU.SchurWeyl.WenzlWeightLevelR`.

*Option E* is the proposal to keep an admissible functional and change the
**element**.

**🟧 OWNER RULING, 2026-09-08 (`2a13dbd85d`), verbatim "A. z_D — follow D7":
`ε := the Markov trace at z_D`, i.e. level 2.** The base is `0.4447004` MeV,
`-43.157 %` against CODATA, recorded as a documented honest miss. Nothing below
is invalidated by it — admissibility is still exactly the two levels, and the
ruling *selects* between them — but three things are re-weighted, and the
re-weighting is the reason this note is here rather than in a PR body:

1. **`conventionD_not_multiplicative` is now load-bearing, not a side remark.**
   The canonical `ε` is the one that is NOT multiplicative, so under the ruling
   braid ORDER is a live degree of freedom for the observable.
2. **`monoidHom_order_blind` becomes a statement about a NON-canonical
   functional**, and its value changes accordingly: it explains why the
   augmentation route looked deceptively insensitive to modelling choices — all
   sixteen readings of the properties blocks' recipe share one level-1 number —
   and therefore why agreement there was never evidence about the element.
3. **The acceptance test goes one-sided.** With `ε` pinned there is no second
   endpoint to run to, so `endpoints_not_roots_of_brackets` is stronger than the
   ruling now needs. What remains is that every candidate the corpus has built
   UNDERSHOOTS at level 2 — measured `-15.451 %` (gen-grouped) to `-43.157 %`
   (`Δ_S`) — so a closing element needs a strictly LARGER `|tr_{z_D}|`, by
   `×1.1828` in the best case and `×1.7592` for `Δ_S`.

Those multipliers are arithmetic on the measured residuals, not theorems, and
they are deliberately not dressed as theorems here. The compute probe
`computations/qbeta/qbeta_option_e_required_level_probe.py` measured that every
candidate `Δ` the corpus has built fails the test, and produced two structural
statements that are not about any particular candidate. This file proves those,
so the argument does not rest on the numerics:

* `trAt_eq_quadratic` — on the normal-form basis the Markov trace at parameter
  `z` is a **quadratic** in `z` with explicit coefficients. Hence a fixed `Δ`
  together with a target *determines* `z`: "which element" and "which
  functional" are one question, not two.
* `brackets_forces_interior_root` / `endpoints_not_roots_of_brackets` — if a
  candidate **overshoots** at one admissible level and **undershoots** at the
  other, then the parameter it needs lies strictly *between* them, and neither
  admissible level is a solution. This is the acceptance test in its usable,
  contrapositive form: *a candidate that brackets the target is rejectable
  without solving anything.*
* `monoidHom_order_blind` / `augmentation_difference_order_blind` — a
  **multiplicative** functional is invariant under reordering the letters of a
  word, so it sees only the multiset of crossings. Level 1 is multiplicative
  (`qbeta_augmentation_is_a_markov_trace_probe`), so an Option E element that
  differs from an existing one only by re-ordering, or by a different
  generator assignment, is **at level 1 the same number**.
* `coordSum_sub_trAt_one` — the corpus's `net` is the *coordinate sum*, and it
  differs from the trace at `z = 1` by exactly `h · (e⁻ coordinate)`. So the
  identification "coordinate sum = tr at z = 1" holds exactly on elements with
  vanishing `e⁻`, which is a property of the element, not a convention.

Nothing here selects an element or proposes a value. Base ring is generic
`CommRing` wherever the statement is algebraic; `ℝ` appears only in the
intermediate-value argument, which needs the order and the topology.

-- Ref: [leitner2026] `docs/audits/2026-09-05-qbeta-functional-decision-options.md` §3, Option E
-/
import Mathlib.Tactic
import Mathlib.Topology.Order.IntermediateValue

namespace QOU.QBeta

/-! ### The normal-form basis and the Markov trace on it -/

/-- Coordinates of an element of `H₃(q)` in the normal-form basis
`[γ, σ₀, σ₁, L₋, L₊, e⁻]` used by the corpus's `Δ`-candidate census. -/
structure NFVec (R : Type*) where
  gamma : R
  s0 : R
  s1 : R
  Lminus : R
  Lplus : R
  eminus : R

namespace NFVec

variable {R : Type*} [CommRing R]

/-- The Markov trace at parameter `z`, read off the basis weights
`[1, z, z, z², z², z(hz+1)]`. -/
def trAt (h z : R) (v : NFVec R) : R :=
  v.gamma + z * v.s0 + z * v.s1 + z ^ 2 * v.Lminus + z ^ 2 * v.Lplus
    + z * (h * z + 1) * v.eminus

/-- The **coordinate sum**: every basis element weighted by `1`. This is the
functional the corpus calls `net`. -/
def coordSum (v : NFVec R) : R :=
  v.gamma + v.s0 + v.s1 + v.Lminus + v.Lplus + v.eminus

/-- **The trace is a quadratic in `z`, with explicit coefficients.**

This is the structural fact behind the acceptance test: for a *fixed* element
the map `z ↦ trAt h z v` is a quadratic, so requiring it to take a prescribed
value does not leave a free choice of `z` — it determines `z` up to which of
two roots. "Which element" and "which functional" are therefore one question. -/
theorem trAt_eq_quadratic (h z : R) (v : NFVec R) :
    v.trAt h z =
      v.gamma
        + (v.s0 + v.s1 + v.eminus) * z
        + (v.Lminus + v.Lplus + h * v.eminus) * z ^ 2 := by
  simp only [trAt]
  ring

/-- **The coordinate sum is not the trace at `z = 1`.** They differ by exactly
`h` times the `e⁻` coordinate, because the trace weights `e⁻` by `z(hz+1)`,
which is `h + 1` at `z = 1`, not `1`. -/
theorem coordSum_sub_trAt_one (h : R) (v : NFVec R) :
    v.coordSum - v.trAt h 1 = -(h * v.eminus) := by
  simp only [coordSum, trAt]
  ring

/-- The two functionals agree exactly on elements whose `e⁻` coordinate
vanishes — a property of the element, not a choice of convention. -/
theorem coordSum_eq_trAt_one_of_eminus_eq_zero (h : R) (v : NFVec R)
    (he : v.eminus = 0) : v.coordSum = v.trAt h 1 := by
  have := coordSum_sub_trAt_one h v
  rw [he] at this
  linear_combination this

end NFVec

/-! ### Level 1 is the augmentation

At `z = q` with `h = q - q⁻¹` the basis weights collapse to
`1, q, q, q², q², q³` — the augmentation `σᵢ ↦ q` on the basis
`1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀`. The only weight that is not visibly a power
of `q` is the last, and it is one. -/

/-- **The `e⁻` weight at level 1 is `q³`.** With `h = q - q⁻¹`,
`q·(h·q + 1) = q³` — so the trace at `z = q` really is the augmentation on the
whole basis, not merely on the short words. -/
theorem eminus_weight_at_level_one {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    q * ((q - q⁻¹) * q + 1) = q ^ 3 := by
  field_simp
  ring

/-! ### Multiplicativity forces order-blindness

The augmentation is an algebra map, so it is a product over the letters of a
word; a product over a list is invariant under permuting the list. This is why
level 1 cannot distinguish two words built from the same multiset of crossings
in a different order — and hence why an Option E element must differ in the
**multiset**, not the braid. -/

/-- **A multiplicative functional is blind to the order of a word.**

The commutativity that does the work is the **target's**, not the braid
monoid's. `w.prod = w'.prod` is *false* in `M`: a braid monoid is not
commutative, and a permuted word is a different braid. What is true is that `ε`
carries the product to a product of images, and *that* product lives in a
commutative ring where reordering is free. So order-blindness is a property of
the functional, not of the words — which is why it is level 1 that has it. -/
theorem monoidHom_order_blind {M R : Type*} [Monoid M] [CommMonoid R]
    (ε : M →* R) {w w' : List M} (hperm : w.Perm w') :
    ε w.prod = ε w'.prod := by
  rw [map_list_prod, map_list_prod]
  exact (hperm.map ε).prod_eq

/-- **Order-blindness passes to a difference of two words.**

`Δ = 𝓑_n - 𝓑_p` is a difference of two words. If each is re-ordered — which is
what a different generator assignment or a different interleaving does — the
value of a multiplicative functional on the difference is unchanged. So at
level 1 those variants are not different candidates at all. -/
theorem augmentation_difference_order_blind {M R : Type*} [Monoid M] [CommRing R]
    (ε : M →* R) {n n' p p' : List M} (hn : n.Perm n') (hp : p.Perm p') :
    ε n.prod - ε p.prod = ε n'.prod - ε p'.prod := by
  rw [monoidHom_order_blind ε hn, monoidHom_order_blind ε hp]

/-! ### Which levels *can* be multiplicative

`monoidHom_order_blind` says multiplicativity buys order-blindness. The
converse question — which Markov parameters are multiplicative at all — has a
sharp answer, and it is what separates the two admissible levels.

A unital multiplicative map on `H₃(q)` sends a Hecke generator `σᵢ` to its
Markov weight `z`, and the Hecke relation `σ² = hσ + 1` then forces
`z² = hz + 1`. That quadratic has exactly two roots, and `z_D` is neither.

The corpus already has the `z ↦ 1` case (`QOU.QBeta.CounitSigmaOne`); this is
the general statement it is an instance of. -/

/-- **The Hecke image equation factors.** Over any commutative ring, with
`h = q - q⁻¹`, `z² - hz - 1 = (z - q)(z + q⁻¹)`. -/
theorem hecke_image_factor {R : Type*} [Field R] (q z : R) (hq : q ≠ 0) :
    z ^ 2 - (q - q⁻¹) * z - 1 = (z - q) * (z + q⁻¹) := by
  field_simp
  ring

/-- **Only two Markov parameters can be multiplicative.** If a unital
multiplicative functional sends the Hecke generator to `z`, then `z = q` or
`z = -q⁻¹` — the two eigenvalues of `σ`. -/
theorem multiplicative_forces_eigenvalue {R : Type*} [Field R] (q z : R)
    (hq : q ≠ 0) (hrel : z ^ 2 = (q - q⁻¹) * z + 1) :
    z = q ∨ z = -q⁻¹ := by
  have hz : (z - q) * (z + q⁻¹) = 0 := by
    rw [← hecke_image_factor q z hq]
    linear_combination hrel
  rcases mul_eq_zero.mp hz with h | h
  · exact Or.inl (by linear_combination h)
  · exact Or.inr (by linear_combination h)

/-- **The convention-D parameter is strictly below `q`.** `q³/(q²+1) < q` for
every `q > 0`, since `q³ < q³ + q`. -/
theorem zD_lt_self {q : ℝ} (hq : 0 < q) : q ^ 3 / (q ^ 2 + 1) < q := by
  rw [div_lt_iff₀ (by positivity)]
  nlinarith [sq_nonneg q]

/-- **The convention-D parameter is positive**, hence above `-q⁻¹`. -/
theorem zD_pos {q : ℝ} (hq : 0 < q) : 0 < q ^ 3 / (q ^ 2 + 1) := by positivity

/-- **Level 2 is not multiplicative.**

`z_D = q³/(q²+1)` is neither eigenvalue: it is strictly below `q` and strictly
above `-q⁻¹`. So no unital multiplicative functional has `z_D` as its Markov
parameter, and the argument that makes level 1 order-blind is unavailable at
level 2.

🛑 **Scope.** This *removes the obstruction*; it does **not** prove that level 2
is order-sensitive. Non-multiplicativity permits sensitivity, it does not force
it. That level 2 actually distinguishes two specific same-multiset words is a
measurement (`qbeta_option_e_required_level_probe`, the interleaved vs
gen-grouped models), not a consequence of this theorem. -/
theorem conventionD_not_multiplicative {q : ℝ} (hq : 0 < q) :
    ¬ ((q ^ 3 / (q ^ 2 + 1)) ^ 2 = (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) + 1) := by
  intro hrel
  rcases multiplicative_forces_eigenvalue q _ (ne_of_gt hq) hrel with h | h
  · exact absurd h (ne_of_lt (zD_lt_self hq))
  · have hneg : -q⁻¹ < 0 := by
      simpa using inv_pos.mpr hq
    exact absurd (h ▸ zD_pos hq) (by simpa using not_lt.mpr hneg.le)

/-! ### The acceptance test

If a candidate overshoots the target at one admissible level and undershoots it
at the other, the parameter it needs is strictly between them. Since the
admissible parameters are exactly the two endpoints, such a candidate cannot be
closed at either — and that is checkable from the two endpoint values alone,
with no solving. -/

/-- **Bracketing forces an interior root.** -/
theorem brackets_forces_interior_root {f : ℝ → ℝ} {a b T : ℝ} (hab : a < b)
    (hf : ContinuousOn f (Set.Icc a b)) (hlo : f a < T) (hhi : T < f b) :
    ∃ c ∈ Set.Ioo a b, f c = T := by
  have hsub := intermediate_value_Ioo hab.le hf
  have hmem : T ∈ Set.Ioo (f a) (f b) := ⟨hlo, hhi⟩
  obtain ⟨c, hc, hfc⟩ := hsub hmem
  exact ⟨c, hc, hfc⟩

/-- **The acceptance test, in the form a reader can apply.** A candidate that
brackets the target takes the target value at *neither* admissible parameter.
No continuity is needed for this half: the two strict inequalities are the
whole argument, which is what makes the test cheap. -/
theorem endpoints_not_roots_of_brackets {f : ℝ → ℝ} {a b T : ℝ}
    (hlo : f a < T) (hhi : T < f b) :
    f a ≠ T ∧ f b ≠ T :=
  ⟨ne_of_lt hlo, (ne_of_lt hhi).symm⟩

/-- The quadratic of `trAt_eq_quadratic`, as a function of `z` over `ℝ`. -/
noncomputable def traceCurve (A B C : ℝ) : ℝ → ℝ := fun z => A + B * z + C * z ^ 2

theorem continuous_traceCurve (A B C : ℝ) : Continuous (traceCurve A B C) := by
  unfold traceCurve
  fun_prop

/-- **Capstone.** For the actual trace curve of a fixed element: bracketing the
target across the two admissible parameters forces the required parameter into
the open interval between them, and excludes both admissible parameters.

`a` and `b` stand for the two admissible Markov parameters (`z_D` and `q`), `T`
for `Q_β / E₀`. The hypotheses are exactly what the probe measures per
candidate; the conclusion is what it reports. -/
theorem option_E_rejected_of_brackets {A B C a b T : ℝ} (hab : a < b)
    (hlo : traceCurve A B C a < T) (hhi : T < traceCurve A B C b) :
    (∃ c ∈ Set.Ioo a b, traceCurve A B C c = T) ∧
      traceCurve A B C a ≠ T ∧ traceCurve A B C b ≠ T := by
  refine ⟨brackets_forces_interior_root hab ?_ hlo hhi,
    endpoints_not_roots_of_brackets hlo hhi⟩
  exact (continuous_traceCurve A B C).continuousOn

end QOU.QBeta
