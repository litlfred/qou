import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Basic
import MathlibExt.CentralExtensionH2

set_option autoImplicit false


/-!
# QOU.YekutieliLiftingCondition — Lifting condition for gerbe extensions

A rigid monoidal category 𝒞 satisfies the Yekutieli lifting condition
if every gerbe object can be lifted, with obstruction classified by
a single cohomology class κ ∈ H²(𝒮, ℬ).

The obstruction space is an abelian group (typically a cohomology group),
and vanishing of the obstruction is necessary and sufficient for the lift.

## References

- [yekutieli2010] Central Extensions of Gerbes, §3
- [leitner2026] §3
-/

namespace QOU

/-- The Yekutieli lifting condition for a category with gerbe structure.

    Given a central extension of gerbes
      1 → ℬ → 𝔊' → 𝔊 → 1
    banded by an abelian sheaf ℬ on a site 𝒮, each object x ∈ Ob(𝔊)
    has an obstruction class κ(x) ∈ H²(𝒮, ℬ), and x admits a lift
    to 𝔊' if and only if κ(x) = 0.

    LaTeX: `\label{def:yekutieli-lifting-condition}` -/
-- Ref: [yekutieli2010] §3, [leitner2026] §3
structure YekutieliLiftingCondition where
  /-- The obstruction space (representing H²(𝒮, ℬ)). -/
  ObstructionSpace : Type*
  /-- The obstruction space is an additive commutative group. -/
  [addCommGroup : AddCommGroup ObstructionSpace]
  /-- The obstruction map: each object (indexed by ℕ for the tower)
      gets an obstruction class in H²(𝒮, ℬ). -/
  obstruction : ℕ → ObstructionSpace
  /-- The type of lifts at level n. -/
  LiftType : ℕ → Type*
  /-- The lifting exists when the obstruction vanishes. -/
  lift_of_zero : ∀ n, obstruction n = 0 → Nonempty (LiftType n)
  /-- Non-zero obstruction prevents lifting. -/
  no_lift_of_nonzero : ∀ n, obstruction n ≠ 0 → IsEmpty (LiftType n)

attribute [instance] YekutieliLiftingCondition.addCommGroup

/-- An object lifts iff its obstruction is zero (the iff formulation).
    Combines lift_of_zero and no_lift_of_nonzero. -/
theorem YekutieliLiftingCondition.lift_iff
    (ylc : YekutieliLiftingCondition)
    (n : ℕ) :
    (ylc.obstruction n = 0) ↔ Nonempty (ylc.LiftType n) := by
  constructor
  · exact ylc.lift_of_zero n
  · intro ⟨_⟩
    by_contra h
    exact (ylc.no_lift_of_nonzero n h).elim ‹_›

/-! ### The condition is satisfied by central group extensions (derived)

The two fields `lift_of_zero` and `no_lift_of_nonzero` are the content of the
definition. The construction below shows they are **satisfiable by derived
theorems, not by assumption**: for any tower of central group extensions
`1 → Aₙ → Eₙ → Gₙ → 1` and homomorphisms `φₙ : Hₙ →* Gₙ`, both fields are
discharged by `QOU.CentralExtension.obstructionClass_eq_one_iff`. The
obstruction space is `∏ₙ H²(Hₙ, Aₙ)` (written additively), and level `n`
places its class `κ(φₙ)` in the `n`-th factor.

This is the group-level (single-object groupoid) case of Yekutieli Thm 4.17;
the gerbe-level case over a site is the subject of bean `qou-533l`, tiers
T3–T4. -/

open QOU.CentralExtension in
/-- **Derived instance** of `def:yekutieli-lifting-condition` for a tower of
central group extensions. No field is assumed: each is proved from the
class-form lifting criterion. -/
noncomputable def YekutieliLiftingCondition.ofCentralExtensions
    {A E G H : ℕ → Type*} [∀ n, CommGroup (A n)] [∀ n, Group (E n)]
    [∀ n, Group (G n)] [∀ n, Group (H n)]
    (S : ∀ n, GroupExtension (A n) (E n) (G n))
    (hcen : ∀ n (a : A n) (e : E n), (S n).inl a * e = e * (S n).inl a)
    (σ : ∀ n, (S n).Section) (φ : ∀ n, H n →* G n) :
    YekutieliLiftingCondition where
  ObstructionSpace := ∀ n, Additive (H2 (H n) (A n))
  obstruction n := Pi.single n (Additive.ofMul (obstructionClass (hcen n) (σ n) (φ n)))
  LiftType n := {ψ : H n →* E n // (S n).rightHom.comp ψ = φ n}
  lift_of_zero n h := by
    have h' : obstructionClass (hcen n) (σ n) (φ n) = 1 := by
      simpa using congrFun h n
    obtain ⟨ψ, hψ⟩ := (obstructionClass_eq_one_iff (hcen n) (σ n) (φ n)).mp h'
    exact ⟨⟨ψ, hψ⟩⟩
  no_lift_of_nonzero n h := by
    refine ⟨fun ⟨ψ, hψ⟩ => h ?_⟩
    have h1 := (obstructionClass_eq_one_iff (hcen n) (σ n) (φ n)).mpr ⟨ψ, hψ⟩
    rw [h1]
    simp

end QOU
