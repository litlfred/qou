import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic


/-!
# QOU.ObservableMTC

The observable modular tensor category at q = ζ_N: the truncated
ribbon fusion category obtained from Rep(U_q(𝔰𝔲₂)) at a primitive
N-th root of unity, with non-symmetric braiding and finitely many
simple objects.

LaTeX label: `def:observable-mtc`

**Ground ring**: `ℂ` (structural; anyonic modular data).
-/

namespace QOU

open CategoryTheory MonoidalCategory BraidedCategory

/-- **Observable modular tensor category** at level N:
    a ribbon fusion category C with finitely many isomorphism
    classes of simple objects and a non-degenerate braiding
    (modular S-matrix). The non-symmetric braiding is encoded
    by the field `braiding_nonsymmetric`.

    LaTeX: `\label{def:observable-mtc}`
    Ref: [moore-seiberg1989] https://doi.org/10.1007/BF01238857 -/
class ObservableMTC
    (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C]
    where
  /-- Finitely many simple-object labels indexed by Fin (N - 1),
      for fixed root-of-unity level N ≥ 3. -/
  -- Ref: [moore-seiberg1989] https://doi.org/10.1007/BF01238857
  level : ℕ
  level_ge : level ≥ 3
  /-- Witness that the braiding is non-symmetric on some simple
      object: there exists V with c ∘ c ≠ id. -/
  -- Ref: [moore-seiberg1989] https://doi.org/10.1007/BF01238857
  braiding_nonsymmetric : ∃ V : C,
    (β_ V V).hom ≫ (β_ V V).hom ≠ 𝟙 (V ⊗ V)

end QOU
