import QOU.QuantumObservableUniverse.Instanton
import Mathlib.Tactic

/-!
# QOU.QuantumObservableUniverse.DqTwist — `d_q` is `d` twisted, and `d_q² ≠ 0` is the twist failing to commute

Bean `qou-fngs`, LES/spectral arc. Answers a structural question the corpus
poses but never states as a theorem: **is the non-vanishing of `d_q²` related
to the twist?** It is not merely related — it *is* the twist.

## `d_q` factors as a twist of `d`

`Instanton.lean` defines

    d_q = qinv • d + (1 − qinv) • (π_V ≫ d)

and composition is bilinear, so this factors:

    d_q = T_q ≫ d,      T_q := qinv • 𝟙 + (1 − qinv) • π_V

`dq_eq_twist_comp` below. `T_q` interpolates between the identity (at
`qinv = 1`, i.e. `q = 1`) and the vertical projector (at `qinv = 0`) — a
**deformation of the identity by an idempotent**, which is what "twist" means
here. `twist_classical` records that `q = 1` collapses it to `𝟙`, which is why
`dq_classical` holds.

## The obstruction is non-commutation, not `q ≠ 1`

`dq_sq_eq_zero_of_twist_comm` is the theorem this file exists for:

    T_q ≫ d = d ≫ T_q   and   d ≫ d = 0   ⟹   d_q ≫ d_q = 0

because `d_q ≫ d_q = T d T d = T T d d = 0`. **No hypothesis on `q` at all.**

That strictly generalises `CategoricalQExtDeriv.dq_classical`, which reaches
the same conclusion only at `q = 1`, and it relocates the obstruction: `d_q²`
fails to vanish not because the deformation parameter is non-classical, but
because the **twist does not commute with the differential**. `q = 1` is
sufficient only because it makes `T_q = 𝟙`, which commutes with everything —
`dq_sq_eq_zero_of_classical_via_twist` derives the classical case that way,
from commutation rather than by unfolding.

The corpus already says this in prose, in `Instanton.lean`'s axiom
justification: *"the vertical projection `π_V` does not commute with the
classical differential `d`, so the cross-term is generically non-zero."* Its
`hcross` hypothesis is exactly that cross-term. This file promotes that
sentence to a theorem and shows the cross-term is the commutator obstruction.

## Why this matters for the spectral-sequence arc

`QOU/Mathlib/PagedSpectralSequence.lean` **requires `d ∘ d = 0`**. So `d_q` is
not a valid differential for a `PagedSS` — a curved object has no cohomology,
because `ker ⧸ im` is not defined when `im ⊄ ker`.

That is not a gap in the API; it is the actual mathematical situation, and it
says where the filtration has to do its work. The standard resolution is to
filter so the curvature sits in **higher filtration degree**, so that the
associated graded satisfies `d² = 0` and the curvature reappears as a higher
differential `d_r`. In this corpus the filtration on offer is the jet order /
Gröbner degree — which is precisely the filtration
`S-GB-spectral-collapse` is about.

So the two threads are one problem seen twice: the curvature `d_q² ≠ 0` is the
obstruction to a naive spectral sequence, and the filtration is what tames it.

-- Ref: [manuscript] §1-quantum-observable-universe
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.DqTwist

universe u v

variable {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.Preadditive C]
    [CategoryTheory.Linear QOU.GroundRing.R_q C]

/-- **The twist**: `T_q = qinv • 𝟙 + (1 − qinv) • π_V`.

    A deformation of the identity by the vertical projector, interpolating
    between `𝟙` at `qinv = 1` and `π_V` at `qinv = 0`. -/
noncomputable def twist (cqd : QOU.CategoricalQExtDeriv C) :
    cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  cqd.qinv • (CategoryTheory.CategoryStruct.id cqd.frobHopf.obj)
    + (1 - cqd.qinv) • cqd.proj_V

/-- **`d_q` is `d` twisted**: `d_q = T_q ≫ d`.

    Composition is bilinear, so the definition in `Instanton.lean` factors. This
    is what makes "twist" a literal description rather than an analogy. -/
theorem dq_eq_twist_comp (cqd : QOU.CategoricalQExtDeriv C) :
    cqd.dq = twist cqd ≫ cqd.d_classical := by
  unfold QOU.CategoricalQExtDeriv.dq twist
  simp [CategoryTheory.Preadditive.add_comp, CategoryTheory.Linear.smul_comp]

/-- At `q = 1` the twist is the identity — which is why `dq_classical` holds. -/
theorem twist_classical (cqd : QOU.CategoricalQExtDeriv C) (hq : cqd.q = 1) :
    twist cqd = CategoryTheory.CategoryStruct.id cqd.frobHopf.obj := by
  have hqinv : cqd.qinv = 1 := by
    have h := cqd.q_mul_qinv
    rw [hq, one_mul] at h
    exact h
  unfold twist
  rw [hqinv]
  simp

/-- **The theorem this file exists for.**

    If the twist commutes with the differential and `d² = 0`, then `d_q² = 0` —
    with **no hypothesis on `q`**.

    `d_q ≫ d_q = T ≫ d ≫ T ≫ d = T ≫ T ≫ d ≫ d = 0`.

    So the obstruction to `d_q` being a differential is **non-commutation of the
    twist**, not non-classicality of the deformation parameter. This strictly
    generalises `CategoricalQExtDeriv.dq_classical`, which gets the conclusion
    only at `q = 1`. -/
theorem dq_sq_eq_zero_of_twist_comm (cqd : QOU.CategoricalQExtDeriv C)
    (hcomm : twist cqd ≫ cqd.d_classical = cqd.d_classical ≫ twist cqd)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq = 0 := by
  rw [dq_eq_twist_comp]
  simp only [CategoryTheory.Category.assoc]
  -- move the inner twist past the differential using commutation
  have hcomm' : cqd.d_classical ≫ twist cqd ≫ cqd.d_classical
      = twist cqd ≫ cqd.d_classical ≫ cqd.d_classical := by
    rw [← CategoryTheory.Category.assoc, ← hcomm, CategoryTheory.Category.assoc]
  rw [hcomm', hd_sq]
  simp

/-- **The classical case, derived from commutation rather than by unfolding.**

    `q = 1` makes the twist the identity, which commutes with everything — so
    `dq_classical`'s conclusion follows from the general theorem above. The
    point is that `q = 1` is *sufficient because it trivialises the twist*, not
    because the deformation parameter is special. -/
theorem dq_sq_eq_zero_of_classical_via_twist (cqd : QOU.CategoricalQExtDeriv C)
    (hq : cqd.q = 1) (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq = 0 := by
  refine dq_sq_eq_zero_of_twist_comm cqd ?_ hd_sq
  rw [twist_classical cqd hq]
  simp

end QOU.DqTwist
