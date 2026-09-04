import QOU.SchurWeyl.HeckeCarrierEquiv
import QOU.SchurWeyl.HeckeSemisimpleReal
import QOU.SchurWeyl.HeckeCarrierSemisimple

/-!
# QOU.SchurWeyl.HeckeCarrierSemisimpleReal — the ℝ specialisation of the carrier equivalence

Beans `qou-img9`, `qou-kwoa`.

`QOU/SchurWeyl/HeckeCarrierEquiv.lean` is generic: `carrierEquiv` over a `CommRing`,
`skeinIwahoriEquiv` over any `Field`.  Its payoff is not, and that is why it is here
rather than there.

`skeinIwahoriEquiv` relates the skein algebra at `q` to the Iwahori algebra at `q²`.
Consumers of `twGram` hold the Iwahori parameter `Q`, so using it means naming a `q` with
`q² = Q` — i.e. `Real.sqrt`, an archimedean construct.  Per §7c the specialisation lives in
a separate file and consumes the generic result; splitting it out is what keeps
`HeckeCarrierEquiv` free of `ℝ`.

The `ℝ` here is *not* an extra restriction on top of `heckeWedderburn`'s: that theorem is
already `ℝ`-only, for the reason measured in `QOU/SchurWeyl/GenericParameter.lean`.
-/

namespace QOU.SchurWeyl

open QOU.Hecke (IwahoriHecke)

/-- **`QOU.Hecke.IwahoriHecke` — the `T_w` / `twGram` carrier — is semisimple at every
    rank (sorry-free).**

    This is the carrier item `QOU/SchurWeyl/HeckeSemisimpleGeneral.lean` recorded as
    *not* reached: that file proves semisimplicity for `QOU.SchurWeyl.Hecke`, and the
    `T_w` basis is built on `QOU.Hecke.IwahoriHecke`.  `skeinIwahoriEquiv` transports it.

    Stated in the Iwahori parameter `Q` directly, which is what consumers of
    `twGram` use. -/
theorem isSemisimpleRing_iwahoriHecke {Q : ℝ} (hQ : 1 < Q) (n : ℕ) :
    IsSemisimpleRing (IwahoriHecke ℝ Q n) := by
  -- The only `ℝ`-specific step is EXHIBITING the square root; the transport itself is
  -- generic (`isSemisimpleRing_iwahoriHecke_of_sq`).  See that file's docstring for why the
  -- general statement has to be parameterised by the root rather than by `Q`.
  have hQ0 : (0 : ℝ) ≤ Q := by linarith
  have hsq : Real.sqrt Q ^ 2 = Q := Real.sq_sqrt hQ0
  have hq1 : 1 < Real.sqrt Q := by
    have : Real.sqrt 1 < Real.sqrt Q := by
      apply Real.sqrt_lt_sqrt (by norm_num) hQ
    simpa using this
  have hqne : Real.sqrt Q ≠ 0 := by positivity
  refine isSemisimpleRing_iwahoriHecke_of_sq hsq.symm hqne ?_ n
  exact QOU.SchurWeyl.GenericParameter.ofSqNeOne hqne (by rw [hsq]; linarith)

end QOU.SchurWeyl
