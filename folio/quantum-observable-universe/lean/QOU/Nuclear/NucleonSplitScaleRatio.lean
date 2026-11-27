import Mathlib.Tactic

/-!
# One energy scale cannot give both pieces of the nucleon split their literature sizes

Bean `qou-myts`. Context: `NucleonSplitGibbsCoulomb` (`m_n − m_p = 2E·log q − λ/3`) and
`computations/probes/mn_own_identity/LITERATURE-COMPARISON.md` §44–§45.

In every route on record the flavour term and the electromagnetic term are the same energy map `E`
applied to two dimensionless numbers:

* flavour: `E · 2L`, where `L` stands for `log q` (the Gibbs cell);
* electromagnetic: `−E · a · Q`, where `a` is the coupling (`α_em`) and `Q` is the charge-pair gap
  (`1/3` for `uud` against `udd`).

Here `L`, `a`, `Q` and `E` are elements of an arbitrary field. No logarithm and no numerical value
enters.

## What is proved

* `flavour_over_em`: the ratio of the two terms is `−2L/(a·Q)`. It does not depend on `E`.
* `flavour_of_em`: if the energy map is chosen so that the electromagnetic term takes a value `t`,
  then the flavour term is forced to `−(2L/(a·Q))·t`.

So within this class, choosing a scale to give the electromagnetic term its size fixes the size of
the flavour term, and the reverse. Any comparison of their ratio with data tests the class itself,
whatever scale is chosen.

## What is NOT claimed

* Any value of `E`, `L`, `a` or `Q`.
* Anything about classes where the electromagnetic term carries its own scale, for example a
  Coulomb energy `a/r` with a length `r` not proportional to `1/E`.
-/

namespace QOU.Nuclear.NucleonSplitScaleRatio

variable {R : Type*} [Field R]

/-- Flavour term of the split under the energy map `E`. -/
def flavourTerm (E L : R) : R := E * (2 * L)

/-- Electromagnetic term of the split under the same energy map `E`. -/
def emTerm (E a Q : R) : R := -(E * (a * Q))

/-- The ratio of the two terms does not depend on the energy map. -/
theorem flavour_over_em (E L a Q : R) (hE : E ≠ 0) (ha : a ≠ 0) (hQ : Q ≠ 0) :
    flavourTerm E L / emTerm E a Q = -(2 * L / (a * Q)) := by
  unfold flavourTerm emTerm
  field_simp

/-- Fixing the electromagnetic term to `t` fixes the flavour term. -/
theorem flavour_of_em (E L a Q t : R) (ha : a ≠ 0) (hQ : Q ≠ 0)
    (ht : emTerm E a Q = t) :
    flavourTerm E L = -(2 * L / (a * Q)) * t := by
  unfold flavourTerm emTerm at *
  rw [← ht]
  field_simp

end QOU.Nuclear.NucleonSplitScaleRatio
