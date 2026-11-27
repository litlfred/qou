import QOU.Core.CategoricalHamiltonianLegendre

/-!
# QOU.Core.CategoricalHamiltonianLegendre — Display Sibling for `def:categorical-hamiltonian`

Display sibling for `def:categorical-hamiltonian` (`quantum-observable-universes/categorical-hamiltonian`).
The authoritative definitions and proofs live in `QOU.Core.CategoricalHamiltonianLegendre`:
- `QOU.Core.CategoricalHamiltonianLegendre.CategoricalHamiltonianVel` (`[CommRing R]`)
- `QOU.Core.CategoricalHamiltonianLegendre.canonicalHamiltonian` (`[Field K]`)
- `QOU.Core.CategoricalHamiltonianLegendre.three_unit_chart_bridge` (`[Field K]`)

In accordance with the no-shadowing-stub rule and §7c pre-wall base-ring generality, this
sibling imports `QOU.Core.CategoricalHamiltonianLegendre` directly and records generic type-checked
re-export abbreviations over `[CommRing R]` and `[Field K]`.

LaTeX label: `def:categorical-hamiltonian`

## References
- [leitner2026] Ch. 2, `def:categorical-hamiltonian`
-/

set_option autoImplicit false

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- Display re-export of the generic `[CommRing R]` operator Reeb-velocity Legendre transform. -/
abbrev categoricalHamiltonianVel_re_export
    {R : Type*} [CommRing R]
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    {fh : FrobeniusHopfData C}
    (L : CategoricalLagrangian R C fh) : fh.obj ⟶ fh.obj :=
  QOU.Core.CategoricalHamiltonianLegendre.CategoricalHamiltonianVel L

/-- Display re-export of the `[Field K]` phase-space canonical Reeb-momentum Hamiltonian. -/
abbrev canonicalHamiltonian_re_export
    {K : Type*} [Field K] (a₂ a₁ a₀ p_reeb : K) : K :=
  QOU.Core.CategoricalHamiltonianLegendre.canonicalHamiltonian a₂ a₁ a₀ p_reeb

end QOU
