import MathlibExt.CentralExtensionObstruction
import Mathlib.GroupTheory.QuotientGroup.Basic

/-!
# The obstruction class in `H²(H, A)` for a central group extension

Tier T1 of the Yekutieli central-extension-of-gerbes programme (bean
`qou-533l`), second step after `MathlibExt.CentralExtensionObstruction`.

That file proves, for a central extension `1 → A → E → G → 1` and a
homomorphism `φ : H →* G`, that the obstruction cochain `c = obstruction σ φ`
is a 2-cocycle, that changing the section changes it by a coboundary, and that
`φ` lifts iff `c` is a coboundary. Those are statements about cochains. This
file turns them into a statement about a **class in a group**:

* `cocycles H A` — trivial-action 2-cocycles `H → H → A`, a subgroup of the
  commutative group of all 2-cochains;
* `coboundaries H A` — the image of the coboundary homomorphism
  `δ : (H → A) →* (H → H → A)`, `δ x g h = x h / x (g * h) * x g`;
* `H2 H A := cocycles ⧸ coboundaries`, a **commutative group**;
* `obstructionClass hcen σ φ : H2 H A`, the class of the obstruction;
* `obstructionClass_section_indep` — the class does not depend on `σ`;
* `obstructionClass_eq_one_iff` — **`φ` lifts iff its class is `1`**.

So the criterion "a lift exists iff the obstruction class vanishes" is a
derived theorem with the class living in a genuine abelian group, which is
the shape that `def:yekutieli-lifting-condition` asks for (see the bridge
`QOU.YekutieliLiftingCondition.ofCentralExtensions` in the sibling content
block `lifting-and-descent/yekutieli-lifting-condition.lean`).

The group `H2 H A` is the classical second cohomology of `H` with trivial
coefficients in `A`, written out directly so that this file does not need the
`Rep`-based group-cohomology library. Everything is generic: `H` any group,
`A` any commutative group (AGENTS.md §7c); nothing archimedean is used.

## Source

Yekutieli, *Central Extensions of Gerbes* (arXiv 0801.0083, held at
`library/arxiv-0801.0083v4/`), Def 4.15 and Thm 4.17, here in the
group-level (single-object groupoid) case.
-/

-- Ref: [yekutieli2010] Def 4.15, Thm 4.17 (group-level case)

namespace QOU.CentralExtension

section H2

variable (H A : Type*) [Group H] [CommGroup A]

/-- Trivial-action 2-cocycles `c : H → H → A`:
`c (g h) k · c g h = c h k · c g (h k)`. -/
def cocycles : Subgroup (H → H → A) where
  carrier := {c | ∀ g h k : H, c (g * h) k * c g h = c h k * c g (h * k)}
  one_mem' := by intro g h k; simp
  mul_mem' := by
    intro a b ha hb g h k
    simp only [Pi.mul_apply]
    calc a (g * h) k * b (g * h) k * (a g h * b g h)
        = (a (g * h) k * a g h) * (b (g * h) k * b g h) := by ac_rfl
      _ = (a h k * a g (h * k)) * (b h k * b g (h * k)) := by rw [ha, hb]
      _ = a h k * b h k * (a g (h * k) * b g (h * k)) := by ac_rfl
  inv_mem' := by
    intro a ha g h k
    simp only [Pi.inv_apply]
    rw [← mul_inv, ← mul_inv, ha]

/-- The coboundary homomorphism `δ x g h = x h / x (g h) · x g`. -/
def coboundaryHom : (H → A) →* (H → H → A) where
  toFun x := fun g h => x h / x (g * h) * x g
  map_one' := by funext g h; simp
  map_mul' := by
    intro x y; funext g h
    simp only [Pi.mul_apply, div_eq_mul_inv, mul_inv]
    ac_rfl

/-- Trivial-action 2-coboundaries. -/
def coboundaries : Subgroup (H → H → A) := (coboundaryHom H A).range

theorem mem_coboundaries_iff (c : H → H → A) :
    c ∈ coboundaries H A ↔ ∃ x : H → A, ∀ g h : H, x h / x (g * h) * x g = c g h := by
  constructor
  · rintro ⟨x, rfl⟩; exact ⟨x, fun _ _ => rfl⟩
  · rintro ⟨x, hx⟩; exact ⟨x, funext fun g => funext fun h => hx g h⟩

theorem coboundaries_le_cocycles : coboundaries H A ≤ cocycles H A := by
  rintro _ ⟨x, rfl⟩ g h k
  simp only [coboundaryHom, MonoidHom.coe_mk, OneHom.coe_mk, div_eq_mul_inv]
  rw [mul_assoc g h k]
  calc x k * (x (g * (h * k)))⁻¹ * x (g * h) * (x h * (x (g * h))⁻¹ * x g)
      = x k * x h * x g * (x (g * (h * k)))⁻¹ * (x (g * h) * (x (g * h))⁻¹) := by ac_rfl
    _ = x k * x h * x g * (x (g * (h * k)))⁻¹ * (x (h * k) * (x (h * k))⁻¹) := by
        rw [mul_inv_cancel, mul_inv_cancel]
    _ = x k * (x (h * k))⁻¹ * x h * (x (h * k) * (x (g * (h * k)))⁻¹ * x g) := by ac_rfl

/-- **Second cohomology** of `H` with trivial coefficients in `A`:
cocycles modulo coboundaries. A commutative group. -/
def H2 : Type _ := cocycles H A ⧸ (coboundaries H A).subgroupOf (cocycles H A)

instance : CommGroup (H2 H A) := QuotientGroup.Quotient.commGroup _

variable {H A}

/-- The class of a cocycle. -/
def H2.mk (c : cocycles H A) : H2 H A := QuotientGroup.mk c

/-- A cocycle has trivial class iff it is a coboundary. -/
theorem H2.mk_eq_one_iff (c : cocycles H A) :
    H2.mk c = 1 ↔ (c : H → H → A) ∈ coboundaries H A := by
  unfold H2.mk
  rw [QuotientGroup.eq_one_iff, Subgroup.mem_subgroupOf]

/-- Two cocycles have the same class iff they differ by a coboundary. -/
theorem H2.mk_eq_mk_iff (c c' : cocycles H A) :
    H2.mk c = H2.mk c' ↔ (c : H → H → A)⁻¹ * c' ∈ coboundaries H A := by
  unfold H2.mk
  rw [QuotientGroup.eq, Subgroup.mem_subgroupOf]
  rfl

end H2

section Obstruction

variable {A E G H : Type*} [CommGroup A] [Group E] [Group G] [Group H]
variable {S : GroupExtension A E G}
variable (hcen : ∀ (a : A) (e : E), S.inl a * e = e * S.inl a)
variable (σ : S.Section) (φ : H →* G)

/-- The obstruction cochain, packaged as a cocycle. -/
noncomputable def obstructionCocycle : cocycles H A :=
  ⟨obstruction σ φ, fun g h k => obstruction_cocycle σ φ hcen g h k⟩

/-- **The obstruction class** `κ(φ) ∈ H²(H, A)`. -/
noncomputable def obstructionClass : H2 H A :=
  H2.mk (obstructionCocycle hcen σ φ)

/-- **Section independence**: `κ(φ)` does not depend on the section `σ`. -/
theorem obstructionClass_section_indep (σ' : S.Section) :
    obstructionClass hcen σ φ = obstructionClass hcen σ' φ := by
  obtain ⟨t, ht⟩ := obstruction_section_change σ φ hcen σ'
  unfold obstructionClass
  rw [H2.mk_eq_mk_iff, mem_coboundaries_iff]
  refine ⟨t, fun g h => ?_⟩
  show _ = (obstruction σ φ g h)⁻¹ * obstruction σ' φ g h
  rw [ht g h, inv_mul_cancel_left]

/-- **Lifting criterion, class form.** `φ` lifts through `E → G` iff its
obstruction class in `H²(H, A)` is trivial. -/
theorem obstructionClass_eq_one_iff :
    obstructionClass hcen σ φ = 1 ↔ ∃ ψ : H →* E, S.rightHom.comp ψ = φ := by
  unfold obstructionClass
  rw [H2.mk_eq_one_iff, mem_coboundaries_iff, exists_lift_iff_coboundary σ φ hcen]
  rfl

end Obstruction

end QOU.CentralExtension
