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
*not* an instance of the class `QOU.Hecke.HeckeAlgebra`, and this file
deliberately does not provide one: **that class's** quadratic field is
`σ² = (q - q⁻¹)σ + 1`, whereas `IwahoriHecke`'s is `σ² = (q-1)σ + q`, so the two
are related by a rescaling of `q` rather than by an instance.

**Name the class, and do not read `(q-1)σ + q` as the odd one out.** As of
`QOU/MathlibExt/IwahoriHeckeAlgebra.lean` the corpus carries several distinct
declarations spelled `HeckeAlgebra` (measured on `main` 2026-08-31: seven
declaration sites), across **two incompatible quadratic conventions** — and
`(q-1)σ + q` is the one shared by `QOU.Hecke.IwahoriHecke` *and* by
`QOU.MathlibExt.IwahoriHecke.HeckeAlgebra`, which `algEquiv` proves are the same
algebra at the **same** `q`, with no rescaling. The odd one out is the class
`QOU.Hecke.HeckeAlgebra`. The fully-qualified names are all distinct, so nothing
is ambiguous to the compiler — but the bare name resolves differently depending
on the namespace in scope, which is the `markovZ` pattern AGENTS.md documents at
length. Bean `qou-csgy` tracks the rename; reconciling the presentations
themselves is `qou-img9`. Neither is attempted here.
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
