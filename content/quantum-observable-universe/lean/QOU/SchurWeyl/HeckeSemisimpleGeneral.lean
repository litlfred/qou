import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.MathlibExt.MatrixSemisimple
import QOU.Information.PNeqNpEquivalence

/-!
# QOU.SchurWeyl.HeckeSemisimpleGeneral — `H_{n+1}(q)` is semisimple at every rank

Bean `qou-kwoa`.  This file adds no mathematics.  It composes four results that
were already in place and had never been put together, and the composition is
the conclusion the whole `det(twGram)` programme was aiming at:

    IsSemisimpleRing (Hecke ℝ q q⁻¹ n)   for every n, every real q ∉ {0, 1, -1}

sorry-free, no cited class, no instance assumed.

## The four pieces, all pre-existing

* `QOU.SchurWeyl.heckeWedderburn` (SW-7) — the algebra isomorphism
  `H_{n+1}(q) ≃ₐ[ℝ] ∏_{λ ⊢ n+1} M_{d_λ}(ℝ)`, at **every** `n`.  Its own chain is
  sorry-free: `rskBurnsideHolds` (`Σ_λ d_λ² = n!` from Robinson–Schensted),
  `heckeProduct_surjective`, and the dimension squeeze.
* `QOU.MathlibExt.MatrixSemisimple.instIsSemisimpleRing_matrix` — matrix rings
  over a division ring are semisimple, which is Mathlib's `proof_wanted
  IsSemisimpleRing.matrix` filled in for that case.
* Mathlib's finite-product instance for `IsSemisimpleRing`.
* Mathlib's `RingEquiv.isSemisimpleRing`, to transport along the iso.

## Why this was worth checking for before building anything

`qou-kwoa` was opened to formalise Geck–Pfeiffer character theory, because the
`det (twGram) ≠ 0` route needs `tr(L_{T_u})` for general `u` and that is
Mathlib-scale.  It is: see
`docs/audits/2026-09-02-tw-regular-trace-not-combinatorial.md`.  But the
*conclusion* that route was chasing does not need it — the Wedderburn split
reaches the same place by counting, and had been sitting in the corpus
unconsumed.  A corpus-grep before construction turned a multi-session
formalisation into this file.

## Scope — what this does and does not say

**It is about `QOU.SchurWeyl.Hecke ℝ q q⁻¹ n`**, whose relation carries a
separate `qi` parameter, and **not** about `QOU.Hecke.IwahoriHecke K q n`, the
carrier the `T_w` basis and `twGram` are built on.  Those are different
`RingQuot`s of different relations, and bridging them is bean `qou-img9`.  So
this does not retire `twGram`; it means the semisimplicity *conclusion* is
available now, on the `SchurWeyl` presentation, while the `T_w` route remains
the one that reaches `IwahoriHecke` itself.

**Field is `ℝ`, and the genericity hypotheses are exactly right for it.**
`q ≠ 0` and `q² ≠ 1` say `q ∉ {0, 1, -1}`, and over `ℝ` that already forces
`[k]_q ≠ 0` for every `k`: `[k]_q > 0` for `q > 0`, and for `q < 0` the only
real vanishing is `[2]_q = 1 + q` at `q = -1`, which is excluded (`[3]_q` has
negative discriminant, and `[4]_q = (1+q)(1+q²)`).  Over a general field this
would be false and a root-of-unity hypothesis would be needed.

This also does **not** depend on the characteristic bound recorded for the
determinant route (`docs/audits/2026-08-30-tw-gram-determinant-measured.md`):
that bound is about the regular *trace form* vanishing in small characteristic,
and no trace form appears here.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)

/-- The Wedderburn block product is semisimple: a finite product of matrix
    rings over `ℝ`. -/
instance isSemisimpleRing_blocks {K : Type*} [Field K] (n : ℕ) :
    IsSemisimpleRing (∀ lam : Partition (n + 1),
      Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
        (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) K) :=
  inferInstance

/-- **`H_{n+1}(q)` is semisimple, at every rank (sorry-free, no cited class).**

    Transported along `heckeWedderburn` from the block product.  For every `n`
    and every real `q ∉ {0, 1, -1}`. -/
theorem isSemisimpleRing_hecke_generic {K : Type*} [Field K] [CharZero K] (q : K)
    (hq0 : q ≠ 0) (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q) (n : ℕ) :
    IsSemisimpleRing (Hecke K q q⁻¹ n) :=
  (heckeWedderburn q hq0 hq2 n).symm.toRingEquiv.isSemisimpleRing

end QOU.SchurWeyl
