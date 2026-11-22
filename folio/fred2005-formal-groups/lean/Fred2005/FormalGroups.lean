import QOU.FormalGroups.FormalGroupLaw
import QOU.FormalGroups.SplayPoisson

/-!
# Non-commutative formal groups in positive characteristic

Lean names for the definitions of F. Leitner, *Non-Commutative Formal Groups in Positive
Characteristic*, arXiv:math/0602138 (`library/arxiv-math-0602138v1`), the owner's source for
`[fred2005]`. The definitions themselves live in the `qou` package under `QOU.FormalGroups`;
this file names them as the chapter's content blocks refer to them.

| Chapter block | Paper | Declaration |
|---|---|---|
| `def:commutative-formal-group` | §2, formal group; commutative | `CommutativeFormalGroup` |
| `def:non-commutative-formal-group` | §2 ("non-commutative" = not necessarily commutative) | `NoncommutativeFormalGroup` |
| `def:skewed-poisson-structure` | Def. 1.1.3, Poisson structure on a splay | `SkewedPoissonStructure` |
| `thm:skew-poisson-integrates` | Thm. 3.7, the quotient `U = T / J` | `IntegrationQuotient`, `integration_commutator` |
| `def:strong-multiplicativity` | Def. 1.11 (not formalised; ref names the Poisson structure) | `SkewedPoissonStructure` |
| `def:grobner-shirshov-basis` | Prop. 2.4 (general notion in `ugb`) | `UGB.GrobnerShirshov.NormalFormBasis` |

What is not formalised: that `U` is the distribution algebra of a formal group (the content
of Thm. 3.7), strong multiplicativity (Def. 1.11, Prop. 1.13), the PBW theorem (Thm. 1.9) and
the Gröbner basis of `Dist(G)` (Prop. 2.4). The paper works over a field of characteristic
`p` throughout; it contains no lift to `ℤ_p`, no Witt vectors and no F-crystals.

Until 2026-11-21 this file carried opaque structures (`coordRing : Type`, an untyped
`formalGroupLaw` function) and theorems about a lift to `ℤ_p`, a Witt vector lift and a
unit-root F-crystal equivalence, some proved by trivial witnesses (the diagonal
comultiplication, the identity Frobenius). None of that is in the paper, and it is removed.
-/

namespace Fred2005

open QOU.FormalGroups

/-- A formal group law over `R` of dimension `ι` (§2 of arXiv:math/0602138). "Non-commutative"
means not necessarily commutative, as in the paper. -/
abbrev NoncommutativeFormalGroup (R : Type*) [CommRing R] (ι : Type*) [Finite ι] : Type _ :=
  FormalGroupLaw R ι

/-- A commutative formal group law: `F(X, Y) = F(Y, X)`. -/
abbrev CommutativeFormalGroup (R : Type*) [CommRing R] (ι : Type*) [Finite ι] : Type _ :=
  {G : FormalGroupLaw R ι // G.IsComm}

/-- Def. 1.1.3 of arXiv:math/0602138: a Poisson structure on the splay of commutative algebras
`Aᵢ`, i.e. a skew-symmetric bi-derivation with Jacobi identity on the free product `∐ᵢ Aᵢ`
that vanishes on each `Aᵢ`. -/
abbrev SkewedPoissonStructure (R : Type*) [CommRing R] {I : Type*} [DecidableEq I]
    (A : I → Type*) [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)] : Type _ :=
  SplayPoisson R A

/-- Thm. 3.7 of arXiv:math/0602138, the construction: the quotient `U = T / J` of the splay
algebra by `J = (fg − gf − π(f, g))`. -/
abbrev IntegrationQuotient (R : Type*) [CommRing R] {I : Type*} [DecidableEq I]
    (A : I → Type*) [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)]
    (π : SkewedPoissonStructure R A) : Type _ :=
  QOU.FormalGroups.IntegrationQuotient π.toPoissonStructure

/-- In `U = T / J` the bracket becomes the commutator. -/
theorem integration_commutator {R : Type*} [CommRing R] {I : Type*} [DecidableEq I]
    {A : I → Type*} [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)]
    (π : SkewedPoissonStructure R A) (f g : SplayAlgebra R A) :
    integrationMk π.toPoissonStructure f * integrationMk π.toPoissonStructure g -
        integrationMk π.toPoissonStructure g * integrationMk π.toPoissonStructure f =
      integrationMk π.toPoissonStructure (π.toPoissonStructure.bracket f g) :=
  integrationMk_commutator _ f g

end Fred2005
