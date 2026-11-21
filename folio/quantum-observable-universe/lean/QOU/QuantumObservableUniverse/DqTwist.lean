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

## The curvature, exactly

`dq_sq_eq_curvature` computes `d_q²` rather than giving a condition for it to
vanish. Writing `κ := d ≫ π_V − π_V ≫ d` for the projector commutator, and
assuming only `d² = 0`:

    d_q ≫ d_q = (1 − q⁻¹) • (T_q ≫ κ ≫ d)

Three things follow, and the third is the one the arc needs.

* `q = 1` kills it through the scalar `(1 − q⁻¹)`, recovering `dq_classical`
  from the **formula** rather than from a commutation hypothesis.
* `κ = 0` kills it for **every** `q`. So the sharp condition is that `π_V`
  commutes with `d` — `twist_comm_iff` shows the twist-commutation hypothesis
  above is exactly `(1 − q⁻¹) • κ = 0`, i.e. the curvature vanishing.
* **The curvature is first order in `(1 − q⁻¹)`.** `d_q` has a degree-zero
  leading term and its failure to square to zero is entirely in degree ≥ 1.
  That is not a remark — it is the filtration statement the arc has been
  reaching for: filter by powers of `(1 − q⁻¹)` and the associated graded
  satisfies `d² = 0`, with the curvature reappearing as a higher differential.

The standing name for an object with `d² ≠ 0` is a **curved** complex, and the
established apparatus for taming one is a Maurer–Cartan element / bounding
cochain — which is what the Floer literature in `library/` (Smith's twisted
complexes and formality, Chanda's invariance *up to a change of local systems*)
supplies as method rather than as content. See
`docs/curved-dq-and-the-floer-cluster.md`.

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

-- Ref: [leitner2026] §1-quantum-observable-universe
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.DqTwist

universe u v

variable {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Preadditive C]
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

/-! ## The curvature computed, not merely bounded

    Everything above gives *conditions* under which `d_q² = 0`. This section
    computes `d_q²`. -/

/-- **The projector commutator** `κ = d ≫ π_V − π_V ≫ d`.

    `Instanton.lean`'s axiom justification names this cross-term in prose —
    *"the vertical projection `π_V` does not commute with the classical
    differential `d`"* — and its `hcross` hypothesis is about it. Here it is
    the object rather than the sentence. -/
noncomputable def projComm (cqd : QOU.CategoricalQExtDeriv C) :
    cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  cqd.d_classical ≫ cqd.proj_V - cqd.proj_V ≫ cqd.d_classical

/-- **Moving `d` past the twist costs `(1 − q⁻¹) • κ`.**

    The identity `𝟙` half of the twist commutes with everything, so the entire
    defect comes from the projector, scaled by the deformation coefficient. -/
theorem d_comp_twist (cqd : QOU.CategoricalQExtDeriv C) :
    cqd.d_classical ≫ twist cqd
      = twist cqd ≫ cqd.d_classical + (1 - cqd.qinv) • projComm cqd := by
  unfold twist projComm
  simp only [CategoryTheory.Preadditive.comp_add, CategoryTheory.Preadditive.add_comp,
    CategoryTheory.Linear.comp_smul, CategoryTheory.Linear.smul_comp, smul_sub,
    CategoryTheory.Category.comp_id, CategoryTheory.Category.id_comp]
  abel

/-- **The twist commutes exactly when the curvature vanishes.**

    So `dq_sq_eq_zero_of_twist_comm`'s hypothesis was never about the twist as
    such: it is `(1 − q⁻¹) • κ = 0`, which `q = 1` achieves through the scalar
    and `κ = 0` achieves through the projector. -/
theorem twist_comm_iff (cqd : QOU.CategoricalQExtDeriv C) :
    twist cqd ≫ cqd.d_classical = cqd.d_classical ≫ twist cqd
      ↔ (1 - cqd.qinv) • projComm cqd = 0 := by
  rw [d_comp_twist]
  constructor
  · intro h
    have := h.symm
    simpa using this
  · intro h
    rw [h, add_zero]

/-- **The curvature of `d_q`, exactly.**

    Assuming only `d² = 0`:

        d_q ≫ d_q = (1 − q⁻¹) • (T_q ≫ κ ≫ d)

    This is strictly stronger than every vanishing criterion above, which it
    implies. Two readings matter:

    * the obstruction is **entirely** the projector commutator, scaled — there
      is no other source of curvature;
    * the scaling is **first order** in `(1 − q⁻¹)`. `d_q` is a degree-zero
      differential whose failure to square to zero lives in filtration degree
      ≥ 1, which is precisely the condition under which filtering makes the
      associated graded a genuine complex and pushes the curvature into a
      higher differential. -/
theorem dq_sq_eq_curvature (cqd : QOU.CategoricalQExtDeriv C)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq
      = (1 - cqd.qinv) • (twist cqd ≫ projComm cqd ≫ cqd.d_classical) := by
  rw [dq_eq_twist_comp]
  have h : (twist cqd ≫ cqd.d_classical) ≫ (twist cqd ≫ cqd.d_classical)
      = twist cqd ≫ (cqd.d_classical ≫ twist cqd) ≫ cqd.d_classical := by
    simp only [CategoryTheory.Category.assoc]
  rw [h, d_comp_twist]
  simp [CategoryTheory.Preadditive.add_comp, CategoryTheory.Linear.smul_comp,
    CategoryTheory.Linear.comp_smul, CategoryTheory.Category.assoc, hd_sq]

/-- **The sharp criterion**: a commuting vertical projector kills the curvature
    for **every** `q`, classical or not.

    Compare `dq_sq_eq_zero_of_classical_via_twist`, which needs `q = 1`. The
    deformation parameter was never the obstruction. -/
theorem dq_sq_eq_zero_of_projComm (cqd : QOU.CategoricalQExtDeriv C)
    (hκ : projComm cqd = 0)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq = 0 := by
  rw [dq_sq_eq_curvature cqd hd_sq, hκ]
  simp

/-- `q = 1` kills the curvature through the **scalar** `(1 − q⁻¹)`, leaving the
    projector commutator untouched. `dq_classical` recovered from the formula. -/
theorem dq_sq_eq_zero_of_q_one (cqd : QOU.CategoricalQExtDeriv C)
    (hq : cqd.q = 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq = 0 := by
  have hqinv : cqd.qinv = 1 := by
    have h := cqd.q_mul_qinv
    rw [hq, one_mul] at h
    exact h
  rw [dq_sq_eq_curvature cqd hd_sq, hqinv]
  simp

end QOU.DqTwist
