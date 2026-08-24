import QOU.Optimization.LPWeakDuality
import Mathlib.Data.Real.Basic

/-!
# Linear-programming strong duality (conditional on the finite-dimensional Farkas alternative)

This file completes the LP-duality development begun in
`QOU.Optimization.LPWeakDuality`. There we proved, unconditionally and over any
ordered commutative ring, the *weak* half — `lp_weak_duality`:
`∑ᵢ aᵢλᵢ ≤ ∑ⱼ cⱼxⱼ` for **any** primal-feasible `x` and dual-feasible `λ`. Here we
add the *strong* half: at an optimal primal point the duality gap **closes** and a
complementary optimal dual point exists (Rivin, *Combinatorial optimization in
geometry*, math/9907032 = Adv. Appl. Math. 31 (2003) 242–271, Thm 3.2).

## Why this half is CONDITIONAL, and on what

Strong duality is *not* an ordered-ring identity: it is equivalent to **Farkas'
lemma**, whose proof is a genuine piece of finite-dimensional convex analysis
(closedness of a finitely generated cone + hyperplane separation). Mathlib
currently carries only the *geometric* Farkas lemma for proper cones
(`ProperCone.hyperplane_separation`, `ProperCone.hyperplane_separation_point`,
`Mathlib/Analysis/Convex/Cone/Dual.lean`); the finite-dimensional **matrix**
alternative and LP duality itself are listed as open TODOs in
`Mathlib/Analysis/Convex/Cone/Basic.lean` ("Define linear programs and prove LP
duality as a special case of cone duality"). No usable matrix-Farkas statement is
available to build on.

Rather than assume the LP conclusion, we axiomatize precisely the analytic **input**
— the Farkas / Gale *theorem of the alternative* — as a `Prop`-valued conditional
class `MatrixFarkas A a c` (§3b-cond of `AGENTS.md`). Its single field
`farkas_alternative` is a genuine, true theorem (a feasibility transposition), and
it is a *hypothesis about the data* `(A, a, c)`, not the block's own conclusion. The
strong-duality theorems below are then **fully derived** (sorry-free) from this
class together with the unconditional `lp_weak_duality`.

**2026-08-21 (bean `qou/kl8z`): the class instance is no longer an open import.**
`QOU.Mathlib.FinitelyGeneratedConeClosed` proves Farkas' lemma — a finitely
generated cone is closed, hence separable from any point outside it — and
`QOU.Optimization.MatrixFarkasInstance` registers the instance. Importing that
module makes every theorem below **unconditional**. This file keeps the
conditional framing deliberately: it is how the layer was built, it does not
depend on the analytic development, and the separation stays useful if the
analytic route is ever replaced.

## Contents

* `MatrixFarkas` — conditional class; field = the Farkas/Gale alternative (the
  analytic input, equivalent to strong duality; the open piece).
* `PrimalOptimal`, `DualOptimal` — optimality predicates.
* `lp_dual_feasible_of_lower_bound` — a primal feasible + bounded-below LP has a
  **feasible dual** (`P*` is feasible), derived from the Farkas class.
* `lp_strong_duality` — at a primal-optimal `x` there is a **dual-optimal** `λ` with
  `dualObj a λ = primalObj c x` (zero gap; complementary optimal pair). Main theorem.
* `lp_zero_duality_gap` — the same pair has `dualityGap = 0`.

The base ring here is `ℝ`: the Farkas alternative is an archimedean statement
(separation of convex sets), so this file sits on the archimedean side of the §7c
wall while `lp_weak_duality` stays generic.

-- Ref: [rivin2003] Igor Rivin, "Combinatorial optimization in geometry",
--   math/9907032, Adv. Appl. Math. 31 (2003) 242–271, Thm 3.2 (strong LP duality
--   for the angle-structure / metric programs).
-/

namespace QOU.Optimization

open scoped BigOperators

variable {m n : ℕ}
  {A : Fin m → Fin n → ℝ} {a : Fin m → ℝ} {c : Fin n → ℝ}
  {x : Fin n → ℝ} {l : Fin m → ℝ}

/-- A primal point `x` is **optimal** for `min cᵀx s.t. Ax = a, x ≥ 0` when it is
feasible and no feasible point has smaller objective. -/
def PrimalOptimal (A : Fin m → Fin n → ℝ) (a : Fin m → ℝ) (c : Fin n → ℝ)
    (x : Fin n → ℝ) : Prop :=
  PrimalFeasible A a x ∧ ∀ x', PrimalFeasible A a x' → primalObj c x ≤ primalObj c x'

/-- A dual point `λ` is **optimal** for `max aᵀλ s.t. λᵀA ≤ c` when it is feasible
and no feasible point has larger objective. -/
def DualOptimal (A : Fin m → Fin n → ℝ) (a : Fin m → ℝ) (c : Fin n → ℝ)
    (l : Fin m → ℝ) : Prop :=
  DualFeasible A c l ∧ ∀ l', DualFeasible A c l' → dualObj a l' ≤ dualObj a l

/-- **The finite-dimensional Farkas / Gale alternative** for the standard-form LP
data `(A, a, c)` — the *analytic input* to strong duality, and the piece Mathlib
lists as an open TODO (see the module docstring).

`farkas_alternative γ` reads: *if the primal `{A x = a, x ≥ 0}` is feasible and no
feasible point attains objective `< γ` (so `γ` is a valid lower bound), then the
dual `{λᵀA ≤ c}` has a point with objective `≥ γ`.* This is a genuine theorem of
finite-dimensional convex analysis (a transposition / theorem of the alternative,
equivalent to strong duality); it is stated here as a hypothesis on the data, **not**
proved. An instance of this class is understood as an appeal to Farkas' lemma, not as
a discharged proof obligation (§"Axiomatization is NOT a Proof", `AGENTS.md`).

The primal-feasibility guard is essential for *truth*: without it the statement is
false when both primal and dual are infeasible (e.g. `A = 0, a ≠ 0, dual empty`). -/
class MatrixFarkas (A : Fin m → Fin n → ℝ) (a : Fin m → ℝ) (c : Fin n → ℝ) :
    Prop where
  /-- Farkas / Gale theorem of the alternative (the open analytic input). -/
  farkas_alternative : ∀ γ : ℝ,
    (∃ x₀, PrimalFeasible A a x₀) →
    (¬ ∃ x', PrimalFeasible A a x' ∧ primalObj c x' < γ) →
    ∃ l, DualFeasible A c l ∧ γ ≤ dualObj a l

/-- **A primal-feasible, bounded-below LP has a feasible dual** (`P*` is feasible).
Given any lower bound `v` on the primal objective over the feasible set, the Farkas
alternative supplies a dual-feasible `λ` with `v ≤ aᵀλ`. Conditional on
`MatrixFarkas`; derived, sorry-free. -/
theorem lp_dual_feasible_of_lower_bound [MatrixFarkas A a c]
    (hpf : ∃ x₀, PrimalFeasible A a x₀) (v : ℝ)
    (hlb : ∀ x', PrimalFeasible A a x' → v ≤ primalObj c x') :
    ∃ l, DualFeasible A c l ∧ v ≤ dualObj a l := by
  refine MatrixFarkas.farkas_alternative v hpf ?_
  rintro ⟨x', hx'f, hlt⟩
  exact absurd (hlb x' hx'f) (not_le.mpr hlt)

/-- **LP strong duality (Rivin math/9907032 Thm 3.2).** At a primal-optimal `x`
there is a **dual-optimal** `λ` whose objective equals the primal objective:
`dualObj a λ = primalObj c x`. Hence the duality gap closes and `(x, λ)` is a
complementary optimal pair.

Conditional on the Farkas class `[MatrixFarkas A a c]`; **fully derived, sorry-free**
from it together with the unconditional `lp_weak_duality`. The Farkas field supplies
the `≥ γ` half (a dual certificate at the primal value), weak duality supplies the
`≤ γ` half, and the two pin `dualObj a λ = primalObj c x`; dual optimality of `λ`
then follows from weak duality against every dual-feasible competitor. -/
theorem lp_strong_duality [MatrixFarkas A a c] (hx : PrimalOptimal A a c x) :
    ∃ l, DualOptimal A a c l ∧ dualObj a l = primalObj c x := by
  obtain ⟨hpf, hmin⟩ := hx
  set γ := primalObj c x with hγ
  -- Optimality of `x` ⟹ no feasible point beats `γ`.
  have hinfeas : ¬ ∃ x', PrimalFeasible A a x' ∧ primalObj c x' < γ := by
    rintro ⟨x', hx'f, hlt⟩
    exact absurd (hmin x' hx'f) (not_le.mpr hlt)
  -- Farkas: a dual-feasible `l` with `γ ≤ dualObj a l`.
  obtain ⟨l, hlf, hge⟩ := MatrixFarkas.farkas_alternative γ ⟨x, hpf⟩ hinfeas
  -- Weak duality: `dualObj a l ≤ γ`.
  have hle : dualObj a l ≤ γ := by
    have hwd := lp_weak_duality hpf hlf
    simpa [dualObj, primalObj, hγ] using hwd
  have heq : dualObj a l = γ := le_antisymm hle hge
  refine ⟨l, ⟨hlf, ?_⟩, heq⟩
  -- Dual optimality: every dual-feasible `l'` is bounded by `γ = dualObj a l`.
  intro l' hl'f
  have hwd' := lp_weak_duality hpf hl'f
  have : dualObj a l' ≤ γ := by simpa [dualObj, primalObj, hγ] using hwd'
  rw [heq]
  exact this

/-- **Zero duality gap** at an optimal primal point: the complementary optimal pair
`(x, λ)` from `lp_strong_duality` has `dualityGap c x a λ = 0`. Conditional on
`MatrixFarkas`; derived, sorry-free. -/
theorem lp_zero_duality_gap [MatrixFarkas A a c] (hx : PrimalOptimal A a c x) :
    ∃ l, DualFeasible A c l ∧ dualityGap c x a l = 0 := by
  obtain ⟨l, ⟨hlf, _⟩, heq⟩ := lp_strong_duality hx
  exact ⟨l, hlf, by simp only [dualityGap, heq, sub_self]⟩

end QOU.Optimization
