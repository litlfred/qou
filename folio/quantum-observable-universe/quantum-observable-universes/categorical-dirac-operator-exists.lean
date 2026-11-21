import QOU.QuantumObservableUniverse.GaugeTheory
import QOU.QuantumObservableUniverses.QDifferentialGeometry
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.CategoricalDirac.exists — existence of the categorical Dirac operator

`𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇` exists as a morphism in the `R`-linear
monoidal category `C`: it is the `R`-linear combination of the connection
endomorphism `∇` and its Reeb contraction `ι_ξ∇`, well-defined in any
`R`-linear category (`def:quantum-observable-universe` carries the
`k`-linearity).  The witness genuinely realises the defining formula — the
`dirac` field of the constructed operator **equals** the combination, not a
trivial identity.

LaTeX: `\label{prop:categorical-dirac-operator-exists}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-dirac-operator-exists
- [connes1994] Noncommutative Geometry (Academic Press)
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Existence of the categorical Dirac operator.**

    In an `R`-linear monoidal category `C`, for any connection `∇`, any
    endomorphism representatives `nablaEndo` (`∇`) and `reeb` (`ι_ξ∇`), and
    any unit substrate parameter `q` (`q · qinv = 1`), there exists a
    `CategoricalDiracOperator R C fh` whose Dirac morphism is exactly the
    `R`-linear combination `q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇`.

    This replaces the earlier `Nonempty (CategoricalDiracOperator C fh)`
    proved by a trivial identity witness: the existential now pins the
    `dirac` field to the defining formula, so the witness genuinely realises
    [`def:categorical-dirac-operator`]. -/
-- Ref: [connes1994]
theorem CategoricalDirac.exists
    {R : Type*} [CommRing R]
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C)
    (connection : CategoricalConnection C fh)
    (q qinv : R) (q_unit : q * qinv = 1)
    (nablaEndo reeb : fh.obj ⟶ fh.obj) :
    ∃ D : CategoricalDiracOperator R C fh,
      D.dirac = qinv • nablaEndo + (1 - qinv) • reeb :=
  ⟨{ connection := connection
     q := q
     qinv := qinv
     q_unit := q_unit
     nablaEndo := nablaEndo
     reeb := reeb
     dirac := qinv • nablaEndo + (1 - qinv) • reeb
     dirac_formula := rfl }, rfl⟩

end QOU
