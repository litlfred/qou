import QOU.QuantumObservableUniverse.Instanton
import Mathlib.CategoryTheory.Preadditive.Basic


/-!
# QOU.CategoricalInstanton.exists — existence of categorical instantons

There exists a categorical connection whose curvature is `⋆_q`-self-dual:
the **zero-instanton** `F_∇ = 0`.  In a preadditive category the zero
curvature is self-dual for any Hodge involution, since `0 ≫ ⋆_q = 0`.

LaTeX: `\label{prop:categorical-instanton-exists}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-instanton-exists
- [atiyah1978] https://doi.org/10.1098/rspa.1978.0143
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Existence of categorical instantons.**

    In a preadditive monoidal category `C`, for any Frobenius–Hopf object and
    any `q`-Hodge involution `⋆_q` on `A`, there exists a
    `CategoricalInstanton fh` whose curvature is the **zero** morphism — the
    zero-instanton `F_∇ = 0`, which is `⋆_q`-self-dual because `0 ≫ ⋆_q = 0`.

    This replaces the earlier `Nonempty (CategoricalInstanton fh)` proved by an
    *identity*-curvature witness (whose self-duality reduced to the trivial
    `𝟙 ≫ 𝟙 = 𝟙`): the existential now pins the witness to the genuine
    `F_∇ = 0` zero-instanton named in [`prop:categorical-instanton-exists`],
    so self-duality is the real `0 ≫ ⋆_q = 0`. -/
-- Ref: [atiyah1978]
theorem CategoricalInstanton.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (hodge : CatHodgeInvolution fh.obj) :
    ∃ I : CategoricalInstanton fh, I.curvature = 0 :=
  ⟨{ connection := 0
     curvature := 0
     hodge := hodge
     self_dual := by
       -- `IsSelfDual 0` is `0 ≫ ⋆_q = 0`, which holds by `zero_comp`.
       simp only [CatHodgeInvolution.IsSelfDual, CategoryTheory.Limits.zero_comp] }, rfl⟩

end QOU
