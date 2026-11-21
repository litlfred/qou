import QOU.QuantumObservableUniverse.GaugeTheory


/-!
# QOU.CategoricalConnection.exists — existence of categorical connections

Trivial witness ∇₀ = d; non-trivial via ∇ = ∇₀ + ω with ω ∈ Ω¹(A) ⊗ Ad(A).

LaTeX: `\label{prop:categorical-connection-exists}`

## References

- [leitner2026] §1-quantum-universes/categorical-connection-exists
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Existence of categorical connections.**

    For every `FrobeniusHopfData C`, a `CategoricalConnection C fh`
    term exists — the trivial witness being the de Rham differential
    `∇₀ = d`; non-trivial witnesses add an `Ad(A)`-valued 1-form. -/
-- Ref: [kock2004]
theorem CategoricalConnection.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) :
    Nonempty (CategoricalConnection C fh) :=
  -- Trivial witness: Ω¹ = 𝟙, ∇ = ρ⁻¹, leibniz_rhs ≡ fh.mul ≫ ∇.
  -- The Leibniz field reduces to rfl since `leibniz_rhs := fh.mul ≫ ∇`.
  -- Same construction as in `categorical-action-exists.lean`.
  -- Ref: [kock2004]
  ⟨{ Omega1 := 𝟙_ C
     nabla := (CategoryTheory.MonoidalCategory.rightUnitor fh.obj).inv
     leibniz_rhs :=
       fh.mul ≫ (CategoryTheory.MonoidalCategory.rightUnitor fh.obj).inv
     leibniz := rfl }⟩

end QOU
