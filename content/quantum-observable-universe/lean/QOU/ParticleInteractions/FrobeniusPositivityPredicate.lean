import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.Fin

/-!
# QOU.ParticleInteractions.FrobeniusPositivityPredicate

The Frobenius-positivity predicate, stated exactly as the corpus states it, and
the theorem separating it from the predicate an agent reaches for instead.

## The corpus statement

`stable-atom.md` (`def:stable-atom`) fixes the predicate:

> Let `G(q)` be the Frobenius Gram matrix of the primitive Wedderburn-block
> operators `{e_λ}`. Decompose the normal form in the primitive basis,
> `T_w = Σ_λ x_λ · e_λ` with `x_λ ∈ ℤ_{≥0}`. The atom `K` is **stable at q**
> iff `∃ x ∈ ℤ_{≥0}^N` such that `G(q) x ≥ 0` coordinatewise. That is, the
> Frobenius positivity constraint `(Gx)_γ ≥ 0` holds for every primitive
> constraint `γ` with `x` a nonnegative integer vector.

Two things in that sentence are load-bearing and are easy to drop:

* the inequality is on `G x`, **not** on `x`; and
* `x` are the coordinates in the **primitive Wedderburn basis** `{e_λ}`, not
  the coordinates in the normal-form basis `{T_w}`.

## Why this file exists

Reading `(Gx)_γ ≥ 0` as "every normal-form coefficient is `≥ 0`" is wrong on
both counts, and the mistake is invisible: it type-checks as a positivity
condition, it agrees with the corpus's phrasing whenever a block names a
*channel* ("the `σ_0` channel violates Frobenius positivity"), and it returns a
definite verdict on every input.  It is nonetheless a different predicate, and
`coordPos_imp_frobPos_iff_entriesNonneg` below says exactly when the two
coincide: **never, unless `G` is entrywise nonnegative.**  A Gram matrix with
one negative entry already separates them.

That is not a hypothetical.  A probe on this branch adopted the naive reading,
concluded that `k = 1` (one Hopf link) is infeasible for the proton, and so
contradicted `categorical-proton-properties.md`, which states that a single
Hopf link `L_- = σ_1σ_0` is the minimum structure restoring stability.  The
corpus was right and the reading was wrong.  `exists_coordPos_not_frobPos` is
that failure as a theorem.

## Scope

This is the predicate and its separation, over a generic ordered ring
(AGENTS.md §7c: no `ℝ` unless an archimedean construct is genuinely needed --
an order is, a completion is not).  It does **not** supply `G(q)` for `H_3`,
which is what evaluating stability for a nucleon still requires.  Nothing here
selects a gluon count or adjudicates any `net` value.

-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/stable-atom.md
-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/ilp-solution-count-unwrap.md
-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/categorical-proton-properties.md
-/

namespace QOU.ParticleInteractions

open Finset

-- AGENTS.md §7c: generic ordered ring, not `ℝ`. An ORDER is genuinely needed
-- (the predicate is an inequality); a completion is not, so `ℝ` would be a
-- gratuitous archimedean specialisation. `LinearOrderedCommRing` is deprecated
-- in this Mathlib; the unbundled spelling below is its replacement.
variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
  {N : ℕ}

/-- **Frobenius positivity**, verbatim from `def:stable-atom`: the constraint
`(G x)_γ ≥ 0` holds for every primitive constraint `γ`.

`x` is the coordinate vector in the primitive Wedderburn basis `{e_λ}`; `G` is
the Frobenius Gram matrix of those operators. -/
def FrobPos (G : Fin N → Fin N → R) (x : Fin N → R) : Prop :=
  ∀ γ : Fin N, 0 ≤ ∑ i : Fin N, G γ i * x i

/-- The selection vector is nonnegative -- the `x ∈ ℤ_{≥0}^N` half of the
corpus's condition, relaxed to an ordered ring. -/
def SelectionNonneg (x : Fin N → R) : Prop := ∀ i : Fin N, 0 ≤ x i

/-- **The naive reading**: every coordinate of the vector is itself `≥ 0`.

Definitionally `SelectionNonneg`; named separately because the two play
different roles -- this is what an agent substitutes *for* `FrobPos`, whereas
`SelectionNonneg` is a genuine part of the corpus's condition alongside it. -/
def CoordPos (x : Fin N → R) : Prop := ∀ i : Fin N, 0 ≤ x i

/-- Entrywise nonnegativity of the Gram matrix. -/
def EntriesNonneg (G : Fin N → Fin N → R) : Prop := ∀ γ i, 0 ≤ G γ i

/-! ### The feasible set is a convex cone -/

omit [IsStrictOrderedRing R] in
/-- The zero selection is always Frobenius-positive, so the *relaxed* feasible
set is never empty. This is the formal content of the parenthetical in
`stable-atom-properties.md`, "the continuous LP relaxation is always feasible":
emptiness is never the obstruction, integrality and the decomposition
constraint are. -/
theorem frobPos_zero (G : Fin N → Fin N → R) : FrobPos G (fun _ => 0) := by
  intro γ
  simp

/-- Frobenius positivity is closed under addition. -/
theorem frobPos_add {G : Fin N → Fin N → R} {x y : Fin N → R}
    (hx : FrobPos G x) (hy : FrobPos G y) : FrobPos G (x + y) := by
  intro γ
  have : ∑ i : Fin N, G γ i * (x + y) i
      = (∑ i : Fin N, G γ i * x i) + ∑ i : Fin N, G γ i * y i := by
    rw [← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun i _ => by simp [mul_add]
  rw [this]
  exact add_nonneg (hx γ) (hy γ)

/-- Frobenius positivity is closed under nonnegative scaling. -/
theorem frobPos_smul {G : Fin N → Fin N → R} {x : Fin N → R} {c : R}
    (hc : 0 ≤ c) (hx : FrobPos G x) : FrobPos G (fun i => c * x i) := by
  intro γ
  have : ∑ i : Fin N, G γ i * (c * x i) = c * ∑ i : Fin N, G γ i * x i := by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by ring
  rw [this]
  exact mul_nonneg hc (hx γ)

/-! ### The separation

The two directions of `coordPos_imp_frobPos_iff_entriesNonneg`. -/

/-- If the Gram matrix is entrywise nonnegative then the naive reading is
*sound*: coordinatewise positivity of `x` does imply Frobenius positivity. -/
theorem frobPos_of_entriesNonneg {G : Fin N → Fin N → R} {x : Fin N → R}
    (hG : EntriesNonneg G) (hx : CoordPos x) : FrobPos G x := by
  intro γ
  exact Finset.sum_nonneg fun i _ => mul_nonneg (hG γ i) (hx i)

/-- **The separation.** A single negative Gram entry `G γ₀ i₀ < 0` already
exhibits a coordinatewise-positive vector that is *not* Frobenius-positive:
the indicator of `i₀`.

This is the failure mode the docstring describes, as a theorem. The witness is
the simplest vector there is, so the two predicates are not merely inequivalent
in the abstract -- they part company on the basis. -/
theorem exists_coordPos_not_frobPos {G : Fin N → Fin N → R} {γ₀ i₀ : Fin N}
    (hneg : G γ₀ i₀ < 0) :
    ∃ x : Fin N → R, CoordPos x ∧ ¬ FrobPos G x := by
  refine ⟨fun i => if i = i₀ then 1 else 0, ?_, ?_⟩
  · intro i
    by_cases h : i = i₀ <;> simp [h]
  · intro hfp
    have hsum : ∑ i : Fin N, G γ₀ i * (if i = i₀ then (1 : R) else 0)
        = G γ₀ i₀ := by
      rw [Finset.sum_eq_single i₀]
      · simp
      · intro b _ hb; simp [hb]
      · intro h; exact absurd (Finset.mem_univ i₀) h
    have := hfp γ₀
    rw [hsum] at this
    exact absurd hneg (not_lt.mpr this)

/-- **The characterisation.** Over a nontrivial index set, the naive reading is
sound for *every* selection vector exactly when the Gram matrix is entrywise
nonnegative.

So substituting coordinatewise positivity for Frobenius positivity is not a
harmless simplification that happens to fail on adversarial input: it is
licensed only by a hypothesis on `G` that a Frobenius Gram matrix has no reason
to satisfy, and that must be checked before the substitution is made. -/
theorem coordPos_imp_frobPos_iff_entriesNonneg (G : Fin N → Fin N → R) :
    (∀ x : Fin N → R, CoordPos x → FrobPos G x) ↔ EntriesNonneg G := by
  constructor
  · intro h γ i
    by_contra hlt
    push_neg at hlt
    obtain ⟨x, hcp, hnfp⟩ := exists_coordPos_not_frobPos (G := G) (γ₀ := γ) (i₀ := i) hlt
    exact hnfp (h x hcp)
  · intro hG x hx
    exact frobPos_of_entriesNonneg hG hx

/-- Restated as the contrapositive an agent should actually check: if the Gram
matrix has any negative entry, the naive reading is unsound and its verdicts
carry no information about stability. -/
theorem naive_reading_unsound_of_neg_entry {G : Fin N → Fin N → R}
    {γ₀ i₀ : Fin N} (hneg : G γ₀ i₀ < 0) :
    ¬ (∀ x : Fin N → R, CoordPos x → FrobPos G x) := by
  intro h
  have : EntriesNonneg G := (coordPos_imp_frobPos_iff_entriesNonneg G).mp h
  exact absurd (this γ₀ i₀) (not_le.mpr hneg)

/-- **Stability**, as `def:stable-atom` defines it: some nonnegative selection
vector is Frobenius-positive.

Stated over an ordered ring; the corpus's integrality (`x ∈ ℤ_{≥0}^N`) is the
strictly stronger ILP condition, and `stable-atom-properties.md` is explicit
that the two differ ("the ILP version is strictly stronger"). -/
def StableAt (G : Fin N → Fin N → R) : Prop :=
  ∃ x : Fin N → R, SelectionNonneg x ∧ FrobPos G x

omit [IsStrictOrderedRing R] in
/-- The relaxed stability predicate is trivially satisfied, for every `G`.

This is a *sharpness* result, not a useful one: it shows the corpus's condition
carries content only through the constraint this relaxation drops -- that `x`
be the primitive-basis decomposition of the given normal form `T_w`, with
nonnegative **integer** coordinates. Any formalisation aiming to decide
stability for a nucleon must carry that constraint, or it proves nothing. -/
theorem stableAt_trivial (G : Fin N → Fin N → R) : StableAt G :=
  ⟨fun _ => 0, fun _ => le_refl 0, frobPos_zero G⟩

end QOU.ParticleInteractions
