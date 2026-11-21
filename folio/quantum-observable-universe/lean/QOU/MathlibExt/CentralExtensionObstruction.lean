import Mathlib.GroupTheory.GroupExtension.Defs
import Mathlib.Tactic.Group

/-!
# Lifting obstruction for a central group extension

Tier T1 of the Yekutieli central-extension-of-gerbes programme (bean `qou-533l`,
task `qou-e8ks`).

Let `1 → A → E → G → 1` be a group extension (`GroupExtension A E G`) whose
kernel `A` is commutative and **central** in `E`, and let `φ : H →* G` be a
homomorphism. Fix a set-theoretic section `σ` of `E → G`. The *obstruction*
of `φ` is the function `c : H → H → A` determined by

  `σ (φ g) * σ (φ h) = inl (c g h) * σ (φ (g * h))`.

We prove, sorry-free:

* `obstruction_cocycle` — `c` satisfies the 2-cocycle identity
  `c (g * h) k * c g h = c h k * c g (h * k)` (trivial action, since `A` is
  central);
* `obstruction_section_change` — changing the section changes `c` by a
  2-coboundary, so its class in `H²(H, A)` is well defined;
* `exists_lift_iff_coboundary` — `φ` lifts to a homomorphism `ψ : H →* E` with
  `rightHom ∘ ψ = φ` **if and only if** `c` is a 2-coboundary:
  `∃ x : H → A, ∀ g h, x h / x (g * h) * x g = c g h`.

The coboundary condition is Mathlib's `IsMulCoboundary₂` specialised to the
trivial action; it is written out here so this file depends only on
`GroupExtension.Defs` (plus the `group` tactic) and not on the
group-cohomology library.

This is the classical group-level case of the statement
"a lift exists iff the obstruction class vanishes". The gerbe-level version
(Yekutieli 2010, Thm 4.17) is the target of later tiers. Here the criterion
is a **derived theorem**, whereas `QOU.YekutieliLifting` carries it as a
structure field.

All types are generic groups; nothing archimedean is used (AGENTS.md §7c).

## Relation to existing corpus Lean

`QOU.Eightfold.ObstructionH2` (with `ObstructionH2Mathlib`) already builds
`H²(Γ; ℤ/3)` with trivial action, the cocycle of a lift, and lift-independence
(`twist_mem_B2`), and identifies its cocycles and coboundaries with Mathlib's.
That covers one coefficient group and has no lift-iff-coboundary theorem. This
file covers any central abelian kernel, works directly on Mathlib's
`GroupExtension`, and proves the criterion `exists_lift_iff_coboundary`.

## Source

Yekutieli, *Central Extensions of Gerbes* (arXiv 0801.0083, held at
`library/arxiv-0801.0083v4/`): Def 3.21 (central extension), Def 4.15
(obstruction class), Thm 4.17 (lift exists iff the class is trivial, **provided
the class is defined**); the torsor example labelled `exa:27` in the source
builds a central extension of gerbes from a central extension of sheaves of
groups.

This file is **not** an instance of Thm 4.17 over a space. It is the
group-cohomology analogue: the same cocycle construction carried out for one
group `H` (equivalently, over the single-object groupoid of `H`), where the
cocycle always exists, so the "is defined" hypothesis does not arise. Over a
space, that hypothesis is a real condition, supplied there by Thm 5.11 when
there are enough acyclic covers. Bridging this file to the sheaf-level theorem
is later tiers (T2-T4).
-/

-- Ref: [manuscript] lifting-and-descent, prop:yekutieli-lifting (group-level case)

namespace QOU.CentralExtension

variable {A E G H : Type*} [CommGroup A] [Group E] [Group G] [Group H]
variable (S : GroupExtension A E G)

/-- An element of `E` lying over `1 ∈ G` is in the image of `inl`. -/
theorem exists_inl_of_rightHom_eq_one {e : E} (he : S.rightHom e = 1) :
    ∃ a : A, S.inl a = e := by
  have hk : e ∈ S.rightHom.ker := he
  rw [← S.range_inl_eq_ker_rightHom] at hk
  exact hk

/-- `inl` maps into the kernel of `rightHom`. -/
theorem rightHom_inl (a : A) : S.rightHom (S.inl a) = 1 := by
  have : S.inl a ∈ S.inl.range := ⟨a, rfl⟩
  rw [S.range_inl_eq_ker_rightHom] at this
  exact this

variable {S}
variable (σ : S.Section) (φ : H →* G)

/-- The element `σ(φ g) σ(φ h) σ(φ(gh))⁻¹` lies over `1`. -/
theorem rightHom_defect (g h : H) :
    S.rightHom (σ (φ g) * σ (φ h) * (σ (φ (g * h)))⁻¹) = 1 := by
  simp only [map_mul, map_inv, GroupExtension.Section.rightHom_section]
  group

/-- The obstruction cochain `c g h ∈ A`, the unique element with
`σ (φ g) * σ (φ h) = inl (c g h) * σ (φ (g * h))`. -/
noncomputable def obstruction (g h : H) : A :=
  (exists_inl_of_rightHom_eq_one S (rightHom_defect σ φ g h)).choose

theorem obstruction_spec (g h : H) :
    σ (φ g) * σ (φ h) = S.inl (obstruction σ φ g h) * σ (φ (g * h)) := by
  have hs := (exists_inl_of_rightHom_eq_one S (rightHom_defect σ φ g h)).choose_spec
  rw [obstruction, hs]
  group

/-- A commutative-group identity used twice below. -/
private theorem comm_aux (a b c d : A) (h : a * b = c * d) : b * a = c * d := by
  rw [mul_comm]; exact h

variable (hcen : ∀ (a : A) (e : E), S.inl a * e = e * S.inl a)
include hcen

/-- **The obstruction is a 2-cocycle** (trivial action; `A` is central). -/
theorem obstruction_cocycle (g h k : H) :
    obstruction σ φ (g * h) k * obstruction σ φ g h =
      obstruction σ φ h k * obstruction σ φ g (h * k) := by
  set c := obstruction σ φ
  have h1 : σ (φ g) * σ (φ h) * σ (φ k) =
      S.inl (c g h * c (g * h) k) * σ (φ (g * h * k)) := by
    calc σ (φ g) * σ (φ h) * σ (φ k)
        = S.inl (c g h) * σ (φ (g * h)) * σ (φ k) := by rw [obstruction_spec σ φ g h]
      _ = S.inl (c g h) * (σ (φ (g * h)) * σ (φ k)) := mul_assoc _ _ _
      _ = S.inl (c g h) * (S.inl (c (g * h) k) * σ (φ (g * h * k))) := by
          rw [obstruction_spec σ φ (g * h) k]
      _ = S.inl (c g h * c (g * h) k) * σ (φ (g * h * k)) := by
          rw [map_mul S.inl]; exact (mul_assoc _ _ _).symm
  have h2 : σ (φ g) * σ (φ h) * σ (φ k) =
      S.inl (c h k * c g (h * k)) * σ (φ (g * h * k)) := by
    calc σ (φ g) * σ (φ h) * σ (φ k)
        = σ (φ g) * (σ (φ h) * σ (φ k)) := mul_assoc _ _ _
      _ = σ (φ g) * (S.inl (c h k) * σ (φ (h * k))) := by rw [obstruction_spec σ φ h k]
      _ = S.inl (c h k) * (σ (φ g) * σ (φ (h * k))) := by
          rw [← mul_assoc, ← hcen, mul_assoc]
      _ = S.inl (c h k) * (S.inl (c g (h * k)) * σ (φ (g * (h * k)))) := by
          rw [obstruction_spec σ φ g (h * k)]
      _ = S.inl (c h k * c g (h * k)) * σ (φ (g * h * k)) := by
          rw [map_mul S.inl, mul_assoc, mul_assoc g h k]
  have h3 := S.inl_injective (mul_right_cancel (h1.symm.trans h2))
  exact comm_aux _ _ _ _ h3

/-- **Lifting criterion.** `φ` lifts through `E → G` iff its obstruction is a
2-coboundary. -/
theorem exists_lift_iff_coboundary :
    (∃ ψ : H →* E, S.rightHom.comp ψ = φ) ↔
      ∃ x : H → A, ∀ g h : H, x h / x (g * h) * x g = obstruction σ φ g h := by
  set c := obstruction σ φ
  constructor
  · rintro ⟨ψ, hψ⟩
    have hy : ∀ g, S.rightHom (σ (φ g) * (ψ g)⁻¹) = 1 := by
      intro g
      have hg : S.rightHom (ψ g) = φ g := by rw [← hψ]; rfl
      rw [map_mul, map_inv, hg, GroupExtension.Section.rightHom_section, mul_inv_cancel]
    choose y hy' using fun g => exists_inl_of_rightHom_eq_one S (hy g)
    have hσ : ∀ g, σ (φ g) = S.inl (y g) * ψ g := fun g => by rw [hy' g]; group
    refine ⟨y, fun g h => ?_⟩
    have key : S.inl (c g h * y (g * h)) * ψ (g * h) =
        S.inl (y g * y h) * ψ (g * h) := by
      calc S.inl (c g h * y (g * h)) * ψ (g * h)
          = S.inl (c g h) * σ (φ (g * h)) := by rw [hσ (g * h), map_mul, mul_assoc]
        _ = σ (φ g) * σ (φ h) := (obstruction_spec σ φ g h).symm
        _ = S.inl (y g) * (ψ g * S.inl (y h)) * ψ h := by
            rw [hσ g, hσ h]; group
        _ = S.inl (y g * y h) * ψ (g * h) := by
            rw [← hcen, map_mul ψ, map_mul S.inl]; group
    have e := S.inl_injective (mul_right_cancel key)
    -- e : c g h * y (g * h) = y g * y h
    rw [eq_mul_inv_of_mul_eq e, div_eq_mul_inv]
    rw [mul_comm (y h), mul_comm (y g * y h)]
    rw [mul_comm (y g) (y h), ← mul_assoc, mul_comm (y (g * h))⁻¹ (y h)]
  · rintro ⟨x, hx⟩
    let f : H → E := fun g => S.inl (x g)⁻¹ * σ (φ g)
    have hA : ∀ g h, (x g)⁻¹ * (x h)⁻¹ * c g h = (x (g * h))⁻¹ := by
      intro g h
      rw [← hx g h, div_eq_mul_inv]
      calc (x g)⁻¹ * (x h)⁻¹ * (x h * (x (g * h))⁻¹ * x g)
          = (x g)⁻¹ * x g * ((x h)⁻¹ * x h) * (x (g * h))⁻¹ := by ac_rfl
        _ = (x (g * h))⁻¹ := by simp
    have hmul : ∀ g h, f (g * h) = f g * f h := by
      intro g h
      calc f (g * h) = S.inl ((x g)⁻¹ * (x h)⁻¹ * c g h) * σ (φ (g * h)) := by
            simp only [f]; rw [hA]
        _ = S.inl (x g)⁻¹ * S.inl (x h)⁻¹ * (S.inl (c g h) * σ (φ (g * h))) := by
            rw [map_mul, map_mul]; group
        _ = S.inl (x g)⁻¹ * S.inl (x h)⁻¹ * (σ (φ g) * σ (φ h)) := by
            rw [obstruction_spec σ φ g h]
        _ = S.inl (x g)⁻¹ * (S.inl (x h)⁻¹ * σ (φ g)) * σ (φ h) := by group
        _ = f g * f h := by
            rw [hcen (x h)⁻¹ (σ (φ g))]; simp only [f]; group
    refine ⟨MonoidHom.mk' f hmul, ?_⟩
    ext g
    simp only [MonoidHom.coe_comp, Function.comp_apply, MonoidHom.mk'_apply, f, map_mul,
      rightHom_inl, GroupExtension.Section.rightHom_section, one_mul]

/-- **Section independence (the obstruction is a class).** Replacing the
section `σ` by any other section `σ'` multiplies the obstruction by the
2-coboundary of some `t : H → A`, so the class of `c` in `H²(H, A)` (trivial
action) does not depend on the choice of section. -/
theorem obstruction_section_change (σ' : S.Section) :
    ∃ t : H → A, ∀ g h : H,
      obstruction σ' φ g h = obstruction σ φ g h * (t h / t (g * h) * t g) := by
  have hu : ∀ g, S.rightHom (σ' (φ g) * (σ (φ g))⁻¹) = 1 := by
    intro g
    rw [map_mul, map_inv, GroupExtension.Section.rightHom_section,
      GroupExtension.Section.rightHom_section, mul_inv_cancel]
  choose t ht using fun g => exists_inl_of_rightHom_eq_one S (hu g)
  have hσ' : ∀ g, σ' (φ g) = S.inl (t g) * σ (φ g) := fun g => by rw [ht g]; group
  refine ⟨t, fun g h => ?_⟩
  have key : S.inl (obstruction σ' φ g h * t (g * h)) * σ (φ (g * h)) =
      S.inl (t g * t h * obstruction σ φ g h) * σ (φ (g * h)) := by
    calc S.inl (obstruction σ' φ g h * t (g * h)) * σ (φ (g * h))
        = S.inl (obstruction σ' φ g h) * σ' (φ (g * h)) := by
          rw [hσ' (g * h), map_mul S.inl, mul_assoc]
      _ = σ' (φ g) * σ' (φ h) := (obstruction_spec σ' φ g h).symm
      _ = S.inl (t g) * (σ (φ g) * S.inl (t h)) * σ (φ h) := by
          rw [hσ' g, hσ' h]; group
      _ = S.inl (t g * t h) * (σ (φ g) * σ (φ h)) := by
          rw [← hcen (t h) (σ (φ g)), map_mul S.inl]; group
      _ = S.inl (t g * t h * obstruction σ φ g h) * σ (φ (g * h)) := by
          rw [obstruction_spec σ φ g h, map_mul S.inl (t g * t h)]; group
  have e := S.inl_injective (mul_right_cancel key)
  -- e : c' * t(gh) = t g * t h * c
  rw [eq_mul_inv_of_mul_eq e, div_eq_mul_inv]
  ac_rfl

end QOU.CentralExtension
