import QOU.SchurWeyl.HeckeCarrierEquiv
import QOU.SchurWeyl.HeckeSemisimpleReal

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
  have hQ0 : (0 : ℝ) ≤ Q := by linarith
  have hsq : Real.sqrt Q ^ 2 = Q := Real.sq_sqrt hQ0
  have hq1 : 1 < Real.sqrt Q := by
    have : Real.sqrt 1 < Real.sqrt Q := by
      apply Real.sqrt_lt_sqrt (by norm_num) hQ
    simpa using this
  have hqne : Real.sqrt Q ≠ 0 := by positivity
  have hss := isSemisimpleRing_hecke_of_one_lt hq1 n
  have := (skeinIwahoriEquiv (Real.sqrt Q) hqne n).toRingEquiv.isSemisimpleRing
  rwa [hsq] at this

end QOU.SchurWeyl
