import Mathlib.RingTheory.SimpleModule.Basic

/-!
# Semisimplicity along **semilinear** maps

Mathlib's `RingTheory/SimpleModule/Basic.lean` carries the linear statements
(`IsSemisimpleModule.of_injective`, `.of_surjective`) and leaves the semilinear
ones as `proof_wanted`:

```
proof_wanted _root_.LinearMap.isSemisimpleModule_of_injective (_ : Function.Injective l)
    [IsSemisimpleModule S N'] : IsSemisimpleModule R M'
proof_wanted _root_.LinearMap.isSemisimpleModule_of_surjective (_ : Function.Surjective l)
    [IsSemisimpleModule R M'] : IsSemisimpleModule S N'
```

Each carries a TODO naming an API generalisation it was thought to need —
*"generalize `Submodule.equivMapOfInjective` from InvPair to RingHomSurjective"*
and *"generalize `LinearMap.quotKerEquivOfSurjective` to SemilinearMaps"*.
**Neither generalisation is required**, because neither proof needs a semilinear
*equivalence*:

* `LinearMap.isSemisimpleModule_iff_of_bijective` — the theorem sitting directly
  above the two `proof_wanted`s — takes a bijective semilinear **map**, not a
  `≃ₛₗ`. A `≃ₛₗ` is what forces `RingHomInvPair`, i.e. an invertible `σ`; a plain
  map does not.
* So the injective case uses `l.rangeRestrict`, and the surjective case a
  complement of `ker l` rather than the quotient by it.

**One hypothesis is added: `[RingHomSurjective σ]`.** It is absent from the
`proof_wanted`s, and appears to be an oversight rather than a strengthening —
`LinearMap.range` and `Submodule.map` are only defined for a semilinear map
under it, and `isSemisimpleModule_iff_of_bijective` itself carries it.
-/

namespace QOU.MathlibExt.SemilinearSemisimple

variable {R S : Type*} [Ring R] [Ring S]
variable {M' : Type*} [AddCommGroup M'] [Module R M']
variable {N' : Type*} [AddCommGroup N'] [Module S N']
variable {σ : R →+* S} (l : M' →ₛₗ[σ] N')

/-- Semilinear `of_injective`, avoiding any `≃ₛₗ` (and so any `RingHomInvPair`):
`isSemisimpleModule_iff_of_bijective` wants a bijective semilinear MAP, and the
range restriction of an injective `l` is one. -/
theorem isSemisimpleModule_of_injective' [RingHomSurjective σ]
    (hl : Function.Injective l) [IsSemisimpleModule S N'] : IsSemisimpleModule R M' :=
  (LinearMap.isSemisimpleModule_iff_of_bijective l.rangeRestrict
    ⟨fun _ _ h => hl (congrArg Subtype.val h), l.surjective_rangeRestrict⟩).mpr inferInstance

/-- Semilinear `of_surjective`, via a complement of the kernel — so
`quotKerEquivOfSurjective` does not need generalising either. -/
theorem isSemisimpleModule_of_surjective' [RingHomSurjective σ]
    (hl : Function.Surjective l) [IsSemisimpleModule R M'] : IsSemisimpleModule S N' := by
  obtain ⟨P, hP⟩ := exists_isCompl (LinearMap.ker l)
  refine (LinearMap.isSemisimpleModule_iff_of_bijective (l.domRestrict P) ⟨?_, ?_⟩).mp
    inferInstance
  · rintro ⟨a, ha⟩ ⟨b, hb⟩ h
    simp only [LinearMap.domRestrict_apply] at h
    have hker : a - b ∈ LinearMap.ker l := by
      simp only [LinearMap.mem_ker, map_sub, h, sub_self]
    have hPm : a - b ∈ P := P.sub_mem ha hb
    have : a - b = 0 := by
      have hx : a - b ∈ LinearMap.ker l ⊓ P := ⟨hker, hPm⟩
      rw [hP.inf_eq_bot, Submodule.mem_bot] at hx
      exact hx
    exact Subtype.ext (sub_eq_zero.mp this)
  · intro y
    obtain ⟨x, rfl⟩ := hl y
    have hx : x ∈ LinearMap.ker l ⊔ P := by
      rw [hP.codisjoint.eq_top]; exact Submodule.mem_top
    obtain ⟨k, hk, p, hp, rfl⟩ := Submodule.mem_sup.mp hx
    exact ⟨⟨p, hp⟩, by simp [LinearMap.mem_ker.mp hk]⟩

end QOU.MathlibExt.SemilinearSemisimple
