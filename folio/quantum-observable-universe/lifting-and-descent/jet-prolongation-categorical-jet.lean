import QOU.QuantumObservableUniverse.CategoricalFoundations


/-!
# QOU.LiftingDescent.jp_categorical_jet

The categorical jet object `J¹(A) := A ⊗ Ω¹(A)`, where
`Ω¹(A) = ker(m : A ⊗ A → A)` is the bimodule of Kähler differentials,
lives in the same ambient rigid monoidal category as `A` and inherits
a Frobenius–Hopf structure `(Δ', ε', S')` from `A`.

This sibling extracts the structural inheritance: any `FrobeniusHopfData`
in a monoidal category gives rise to the underlying carrier-object
data needed for the categorical jet construction.  The full
inheritance of the structure maps (`Δ'`, `ε'`, `S'`) at the jet level
is delegated to the categorical-jet construction in the manuscript;
this stub records the existence claim that any `FrobeniusHopfData A`
yields a candidate carrier in the same ambient category.

LaTeX label: `lem:jet-prolongation-categorical-jet`

## References

- [fred2005] Frenkel–Reshetikhin, q-Geometric Langlands, formal-group
  jet schemes underpinning the categorical jet construction
- [kock2004] Kock, *Frobenius Algebras and 2D TQFTs* (background on
  the Frobenius-Hopf data structure inherited at the jet level)
- [manuscript] §3 Lifting and Descent, §"Categorical jet object"
-/

namespace QOU.LiftingDescent

open CategoryTheory

/-- **Categorical jet inherits the ambient category.**

    Any `FrobeniusHopfData A` in a monoidal category `C` exhibits
    its underlying object `obj` as a `C`-object — the carrier on
    top of which the jet construction `J¹(A) := A ⊗ Ω¹(A)` is
    built.  This lemma packages the trivial structural fact that
    `(fhd : FrobeniusHopfData C).obj : C` provides a candidate
    carrier for the categorical jet inheritance.

    The deeper inheritance of `(Δ', ε', S')` to `J¹(A)` is the
    content of the manuscript's §3 construction; the Lean
    formalisation of those structure maps awaits a richer encoding
    of `Ω¹(A)` and the Kähler-differential bimodule. -/
-- Ref: [fred2005], [kock2004]
-- Ref: [manuscript] §3 Lifting and Descent, "Categorical jet object"
def jp_categorical_jet
    {C : Type*} [Category C] [MonoidalCategory C]
    (fhd : QOU.FrobeniusHopfData C) :
    Nonempty C :=
  ⟨fhd.obj⟩

end QOU.LiftingDescent
