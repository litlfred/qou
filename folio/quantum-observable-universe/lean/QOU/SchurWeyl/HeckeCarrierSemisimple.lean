import QOU.SchurWeyl.HeckeCarrierEquiv
import QOU.SchurWeyl.HeckeSemisimpleGeneral

/-!
# QOU.SchurWeyl.HeckeCarrierSemisimple — the Iwahori carrier is semisimple over any field

Bean `qou-j377`, the last `ℝ` on the semisimplicity arc.

`QOU/SchurWeyl/HeckeSemisimpleGeneral.lean` proves `IsSemisimpleRing (Hecke K q q⁻¹ n)` over
any `[Field K] [CharZero K]` with `q` not a root of unity.  `skeinIwahoriEquiv` carries that
to `QOU.Hecke.IwahoriHecke` — the `T_w` / `twGram` carrier — and is itself already generic.
So this file is one transport.

## The statement is parameterised by the square root, and that is not a defect

`skeinIwahoriEquiv` relates the skein algebra at `q` to the Iwahori algebra at `q ^ 2`.  The
`ℝ` form (`HeckeCarrierSemisimpleReal.lean`) takes the Iwahori parameter `Q` directly and
produces its own `q` as `Real.sqrt Q`, which is available because every `Q > 1` in `ℝ` is a
square.  **A general field affords no such step** — `ℚ` does not contain `√2` — so the
honest general statement takes the square root as the parameter and reads *"the Iwahori
algebra at a square is semisimple"*.

That is a genuine mathematical narrowing, not a limitation of the proof, and it is the whole
residue of the `ℝ` that the general-field tranche left on this arc: the `ℝ` was never
carrying algebra here, only the existence of a square root.  Where a caller does have a
square root — over `ℝ`, or over any field with `Q` a square — nothing is lost.
-/

namespace QOU.SchurWeyl

open QOU.Hecke (IwahoriHecke)

/-- **`QOU.Hecke.IwahoriHecke K (q ^ 2) n` is semisimple, over any field of characteristic
zero with `q` not a root of unity, at every rank.**

The `T_w` / `twGram` carrier, general-field.  Transported from
`isSemisimpleRing_hecke_generic` along `skeinIwahoriEquiv`.

Stated at `q ^ 2` rather than at a general Iwahori parameter `Q` because naming a `q` with
`q ^ 2 = Q` is exactly what a general field cannot do; see the module docstring. -/
theorem isSemisimpleRing_iwahoriHecke_sq {K : Type*} [Field K] [CharZero K] (q : K)
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    IsSemisimpleRing (IwahoriHecke K (q ^ 2) n) :=
  have _ := isSemisimpleRing_hecke_generic q hq0 hq2 n
  (skeinIwahoriEquiv q hq0 n).toRingEquiv.isSemisimpleRing

/-- **The same, at an Iwahori parameter `Q` that is given as a square.**  The shape a caller
holding `Q` wants, once it can exhibit a square root. -/
theorem isSemisimpleRing_iwahoriHecke_of_sq {K : Type*} [Field K] [CharZero K] {Q q : K}
    (hQ : Q = q ^ 2) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    IsSemisimpleRing (IwahoriHecke K Q n) := by
  subst hQ
  exact isSemisimpleRing_iwahoriHecke_sq q hq0 hq2 n

end QOU.SchurWeyl
