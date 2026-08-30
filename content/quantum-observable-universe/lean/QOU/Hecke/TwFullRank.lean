import QOU.Hecke.TwBasisField
import QOU.Hecke.FullRank

/-!
# QOU.Hecke.TwFullRank — the rank axiom, discharged for the real algebra

`QOU.Hecke.FullRank` introduced `IsHeckeOfFullRank R n A` — free of rank `n!` —
as the companion condition that `HeckeAlgebra` does not impose, and its
docstring granted the Iwahori basis theorem as an *assumption*:

&gt; *"The Iwahori basis theorem says that abstract algebra has dimension `n!`.
&gt; Granting that (it is **not** formalised here, and nothing below depends on
&gt; it) …"*

Over a field it is now formalised, by `QOU.Hecke.TwBasis.basisTwOfField`, so the
predicate can be discharged for the algebra it was written about rather than
only for the tree's finite-rank models `H3A` / `H4A`
(`QOU.Hecke.FullRankFromWedderburn`, where the dimension is true by construction
of the carrier and carries no Hecke content).

Index convention: `IwahoriHecke K q n` has `n` generators, so it models
`S_{n+1}` and its rank is `(n+1)!`; the predicate's `n` is therefore `n + 1`.

## What this does and does not establish

It fixes the **dimension** of `IwahoriHecke K q n`, which is what the degenerate
models fail — `InstanceH2.rankOneModel` is one-dimensional at every rank. It is
*not* a `HeckeAlgebra` instance, and this file deliberately does not provide
one: `HeckeAlgebra`'s quadratic field is `σ² = (q - q⁻¹)σ + 1`, a different
normalisation from `IwahoriHecke`'s `σ² = (q-1)σ + q`, so the two are related by
a rescaling of `q` rather than by an instance. Reconciling the corpus's Hecke
presentations is bean `qou-img9` and is not attempted here.
-/

namespace QOU.Hecke

universe u

variable {K : Type u} [Field K] (q : K) (n : ℕ)

/-- **The Iwahori rank axiom holds for `IwahoriHecke K q n`, at every rank
    (sorry-free).**  Freeness is automatic over a field; the dimension is
    `QOU.Hecke.TwBasis.finrank_eq_factorial`, which comes from the `T_w` basis
    and is the first statement of the Iwahori basis theorem in this corpus. -/
instance isHeckeOfFullRank_iwahoriHecke :
    IsHeckeOfFullRank K (n + 1) (QOU.Hecke.IwahoriHecke K q n) where
  free := inferInstance
  finrank_eq := QOU.Hecke.TwBasis.finrank_eq_factorial K q n

end QOU.Hecke
