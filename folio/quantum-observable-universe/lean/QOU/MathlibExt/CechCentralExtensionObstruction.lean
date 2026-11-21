import QOU.MathlibExt.CentralExtensionObstruction

/-!
# Čech lifting obstruction for a central extension (constant coefficients)

Tier T2 of the Yekutieli central-extension-of-gerbes programme (bean `qou-533l`,
task `qou-8km0`). It builds on T1, `QOU.MathlibExt.CentralExtensionObstruction`.

## Setting

Fix a central extension `1 → A → E → G → 1` (`GroupExtension A E G`, with `A`
commutative and central in `E`) and an index set `I` labelling the opens of a
cover. A **Čech 1-cocycle** with values in `G` is a family `g i j : G` with

  `g i j * g j k = g i k`  for all `i j k`.

This is the transition data of a principal `G`-bundle, i.e. a `G`-torsor, in the
case of *constant* coefficients: each double overlap carries one element of `G`.
That is the case where every overlap is connected and the sheaf of groups is the
constant sheaf. Varying coefficients (a presheaf of groups on the nerve) is the
next sub-tier.

Choose any lifts `x i j : E` with `rightHom (x i j) = g i j`. The
**obstruction** `c i j k : A` is defined by

  `inl (c i j k) = x i j * x j k * (x i k)⁻¹`.

## Results, all sorry-free over generic groups

* `cechObstruction_cocycle`: `c` is a Čech 2-cocycle,
  `c i j k * c i k l = c j k l * c i j l`.
* `cechObstruction_lift_change`: different lifts change `c` by a Čech
  coboundary, so its class in `Ȟ²(I; A)` is well defined.
* `exists_cocycle_lift_iff`: the `G`-cocycle lifts to an `E`-valued Čech
  1-cocycle **iff** `c` is a Čech 2-coboundary, `c i j k = a i j * a j k / a i k`.

This is the Čech statement behind Yekutieli 2010, Thm 4.17, specialised to the
torsor gerbe of `exa:27` there with constant coefficients: a `G`-torsor lifts to
an `E`-torsor iff its obstruction class in `Ȟ²` with coefficients in `A` is
trivial. It is **derived**, not carried as a structure field. Sheaf-valued
coefficients (T2b), gerbes (T3) and the general theorem (T4) remain.
-/

-- Ref: [manuscript] lifting-and-descent, prop:yekutieli-lifting (Čech, constant coefficients)

namespace QOU.CentralExtension

variable {A E G I : Type*} [CommGroup A] [Group E] [Group G]
variable {S : GroupExtension A E G}

/-- A Čech 1-cocycle on the index set `I` with values in a group. -/
def IsCechCocycle {K : Type*} [Group K] (g : I → I → K) : Prop :=
  ∀ i j k, g i j * g j k = g i k

variable (x : I → I → E) (g : I → I → G)
variable (hx : ∀ i j, S.rightHom (x i j) = g i j) (hg : IsCechCocycle g)

include hx hg in
theorem rightHom_cech_defect (i j k : I) :
    S.rightHom (x i j * x j k * (x i k)⁻¹) = 1 := by
  rw [map_mul, map_mul, map_inv, hx, hx, hx, hg i j k, mul_inv_cancel]

/-- The Čech obstruction `c i j k`, the unique element of `A` with
`inl (c i j k) = x i j * x j k * (x i k)⁻¹`. -/
noncomputable def cechObstruction (i j k : I) : A :=
  (exists_inl_of_rightHom_eq_one S (rightHom_cech_defect x g hx hg i j k)).choose

theorem cechObstruction_spec (i j k : I) :
    x i j * x j k = S.inl (cechObstruction x g hx hg i j k) * x i k := by
  have hs := (exists_inl_of_rightHom_eq_one S (rightHom_cech_defect x g hx hg i j k)).choose_spec
  rw [cechObstruction, hs]
  group

variable (hcen : ∀ (a : A) (e : E), S.inl a * e = e * S.inl a)
include hcen

/-- **The Čech obstruction is a 2-cocycle.** -/
theorem cechObstruction_cocycle (i j k l : I) :
    cechObstruction x g hx hg i j k * cechObstruction x g hx hg i k l =
      cechObstruction x g hx hg j k l * cechObstruction x g hx hg i j l := by
  set c := cechObstruction x g hx hg
  have h1 : x i j * x j k * x k l = S.inl (c i j k * c i k l) * x i l := by
    calc x i j * x j k * x k l
        = S.inl (c i j k) * x i k * x k l := by rw [cechObstruction_spec x g hx hg i j k]
      _ = S.inl (c i j k) * (x i k * x k l) := mul_assoc _ _ _
      _ = S.inl (c i j k) * (S.inl (c i k l) * x i l) := by
          rw [cechObstruction_spec x g hx hg i k l]
      _ = S.inl (c i j k * c i k l) * x i l := by
          rw [map_mul S.inl]; exact (mul_assoc _ _ _).symm
  have h2 : x i j * x j k * x k l = S.inl (c j k l * c i j l) * x i l := by
    calc x i j * x j k * x k l
        = x i j * (x j k * x k l) := mul_assoc _ _ _
      _ = x i j * (S.inl (c j k l) * x j l) := by rw [cechObstruction_spec x g hx hg j k l]
      _ = S.inl (c j k l) * (x i j * x j l) := by
          rw [← mul_assoc, ← hcen, mul_assoc]
      _ = S.inl (c j k l) * (S.inl (c i j l) * x i l) := by
          rw [cechObstruction_spec x g hx hg i j l]
      _ = S.inl (c j k l * c i j l) * x i l := by
          rw [map_mul S.inl]; exact (mul_assoc _ _ _).symm
  exact S.inl_injective (mul_right_cancel (h1.symm.trans h2))

/-- **Independence of the lifts.** Two families of lifts give obstructions that
differ by a Čech 2-coboundary. -/
theorem cechObstruction_lift_change (x' : I → I → E)
    (hx' : ∀ i j, S.rightHom (x' i j) = g i j) :
    ∃ t : I → I → A, ∀ i j k : I,
      cechObstruction x' g hx' hg i j k =
        cechObstruction x g hx hg i j k * (t i j * t j k / t i k) := by
  have hu : ∀ i j, S.rightHom (x' i j * (x i j)⁻¹) = 1 := by
    intro i j; rw [map_mul, map_inv, hx', hx, mul_inv_cancel]
  choose t ht using fun i j => exists_inl_of_rightHom_eq_one S (hu i j)
  have hx'eq : ∀ i j, x' i j = S.inl (t i j) * x i j := fun i j => by rw [ht i j]; group
  refine ⟨t, fun i j k => ?_⟩
  set c := cechObstruction x g hx hg
  set c' := cechObstruction x' g hx' hg
  have key : S.inl (c' i j k * t i k) * x i k =
      S.inl (t i j * t j k * c i j k) * x i k := by
    calc S.inl (c' i j k * t i k) * x i k
        = S.inl (c' i j k) * x' i k := by
          rw [hx'eq i k, map_mul S.inl, mul_assoc]
      _ = x' i j * x' j k := (cechObstruction_spec x' g hx' hg i j k).symm
      _ = S.inl (t i j) * (x i j * S.inl (t j k)) * x j k := by
          rw [hx'eq i j, hx'eq j k]; group
      _ = S.inl (t i j * t j k) * (x i j * x j k) := by
          rw [← hcen (t j k) (x i j), map_mul S.inl]; group
      _ = S.inl (t i j * t j k * c i j k) * x i k := by
          rw [cechObstruction_spec x g hx hg i j k, map_mul S.inl (t i j * t j k), ← mul_assoc]
  have e := S.inl_injective (mul_right_cancel key)
  rw [eq_mul_inv_of_mul_eq e, div_eq_mul_inv]
  ac_rfl

/-- **Čech lifting criterion.** The `G`-valued Čech 1-cocycle `g` lifts to an
`E`-valued Čech 1-cocycle iff its obstruction is a Čech 2-coboundary. -/
theorem exists_cocycle_lift_iff :
    (∃ h : I → I → E, (∀ i j, S.rightHom (h i j) = g i j) ∧ IsCechCocycle h) ↔
      ∃ a : I → I → A, ∀ i j k : I,
        cechObstruction x g hx hg i j k = a i j * a j k / a i k := by
  set c := cechObstruction x g hx hg
  constructor
  · rintro ⟨h, hh, hcoc⟩
    have hu : ∀ i j, S.rightHom (x i j * (h i j)⁻¹) = 1 := by
      intro i j; rw [map_mul, map_inv, hh, hx, mul_inv_cancel]
    choose a ha using fun i j => exists_inl_of_rightHom_eq_one S (hu i j)
    have hxeq : ∀ i j, x i j = S.inl (a i j) * h i j := fun i j => by rw [ha i j]; group
    refine ⟨a, fun i j k => ?_⟩
    have key : S.inl (c i j k * a i k) * h i k = S.inl (a i j * a j k) * h i k := by
      calc S.inl (c i j k * a i k) * h i k
          = S.inl (c i j k) * x i k := by rw [hxeq i k, map_mul S.inl, mul_assoc]
        _ = x i j * x j k := (cechObstruction_spec x g hx hg i j k).symm
        _ = S.inl (a i j) * (h i j * S.inl (a j k)) * h j k := by
            rw [hxeq i j, hxeq j k]; group
        _ = S.inl (a i j * a j k) * (h i j * h j k) := by
            rw [← hcen (a j k) (h i j), map_mul S.inl]; group
        _ = S.inl (a i j * a j k) * h i k := by rw [hcoc i j k]
    have e := S.inl_injective (mul_right_cancel key)
    rw [eq_mul_inv_of_mul_eq e, div_eq_mul_inv]
  · rintro ⟨a, ha⟩
    refine ⟨fun i j => S.inl (a i j)⁻¹ * x i j, fun i j => ?_, fun i j k => ?_⟩
    · rw [map_mul, rightHom_inl, one_mul, hx]
    · have hA : (a i j)⁻¹ * (a j k)⁻¹ * c i j k = (a i k)⁻¹ := by
        rw [ha i j k, div_eq_mul_inv]
        calc (a i j)⁻¹ * (a j k)⁻¹ * (a i j * a j k * (a i k)⁻¹)
            = (a i j)⁻¹ * a i j * ((a j k)⁻¹ * a j k) * (a i k)⁻¹ := by ac_rfl
          _ = (a i k)⁻¹ := by simp
      calc S.inl (a i j)⁻¹ * x i j * (S.inl (a j k)⁻¹ * x j k)
          = S.inl (a i j)⁻¹ * S.inl (a j k)⁻¹ * (x i j * x j k) := by
            rw [mul_assoc, ← mul_assoc (x i j), ← hcen (a j k)⁻¹ (x i j)]; group
        _ = S.inl (a i j)⁻¹ * S.inl (a j k)⁻¹ * (S.inl (c i j k) * x i k) := by
            rw [cechObstruction_spec x g hx hg i j k]
        _ = S.inl ((a i j)⁻¹ * (a j k)⁻¹ * c i j k) * x i k := by
            rw [map_mul S.inl, map_mul S.inl]; group
        _ = S.inl (a i k)⁻¹ * x i k := by rw [hA]

end QOU.CentralExtension
