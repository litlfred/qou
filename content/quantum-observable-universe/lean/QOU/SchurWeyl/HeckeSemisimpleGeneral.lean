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
instance isSemisimpleRing_blocks (n : ℕ) :
    IsSemisimpleRing (∀ lam : Partition (n + 1),
      Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
        (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) ℝ) :=
  inferInstance

/-- **`H_{n+1}(q)` is semisimple, at every rank (sorry-free, no cited class).**

    Transported along `heckeWedderburn` from the block product.  For every `n`
    and every real `q ∉ {0, 1, -1}`. -/
theorem isSemisimpleRing_hecke (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    IsSemisimpleRing (Hecke ℝ q q⁻¹ n) :=
  (heckeWedderburn q hq0 hq2 n).symm.toRingEquiv.isSemisimpleRing

/-- **The substrate discharges semisimplicity at every rank (sorry-free).**

    For any real `q > 1` — in particular the substrate `q₀ ≈ 1.10998` —
    `QOU.SchurWeyl.Hecke ℝ q q⁻¹ n` is semisimple at every rank.  This is the
    shape in which the substrate parameter discharges the semisimplicity leg of
    the `P ≠ NP`-in-QOU counting argument, with no cited class and no `sorry`.

    The carrier is named explicitly rather than called "the Iwahori–Hecke
    algebra", because this file's scope section distinguishes it from
    `QOU.Hecke.IwahoriHecke`, and the informal name would read as a claim about
    that one. -/
theorem isSemisimpleRing_hecke_of_one_lt {q : ℝ} (hq : 1 < q) (n : ℕ) :
    IsSemisimpleRing (Hecke ℝ q q⁻¹ n) := by
  refine isSemisimpleRing_hecke q (by positivity) ?_ n
  have h1 : 1 < q ^ 2 := by nlinarith
  exact ne_of_gt h1

/-! ## Discharging the cited `WenzlCriterion`

`QOU.Information.PNeqNpEquivalence.WenzlCriterion` is a hypothesis class — its
own docstring says "hypothesis class, not a theorem of this development" — and
it had **no instance anywhere in the corpus**.  Everything downstream of
`semisimple_of_one_lt` was therefore conditional on an assumption with no known
model.  It has one now. -/

/-- **A model for the cited `WenzlCriterion` (sorry-free).**

    For any real `q > 1`, the criterion holds with `semisimple n` instantiated
    as actual semisimplicity of the rank-`n` algebra.  This is what the class
    was asking for and had never been supplied.

    The `WenzlGeneric` hypothesis is not used: over `ℝ`, `1 < q` already gives
    semisimplicity outright, so the criterion is satisfied a fortiori.  Note
    that a *blanket* instance quantified over all `q` would be **false** as the
    class is stated — `WenzlGeneric 0 n` holds vacuously (`0 ^ k = 0 ≠ 1`)
    while `q = 0` is degenerate — which is why this is a theorem taking `hq`,
    not an `instance`. -/
theorem wenzlCriterion_of_one_lt {q : ℝ} (hq : 1 < q) :
    QOU.Information.WenzlCriterion q
      (fun n => IsSemisimpleRing (Hecke ℝ q q⁻¹ n)) :=
  ⟨fun n _ => isSemisimpleRing_hecke_of_one_lt hq n⟩

/-- **`semisimple_of_one_lt`, with the criterion discharged (sorry-free).**

    The composition: no cited class remains between `1 < q` and semisimplicity
    at every rank.

    Scope, so this is not over-read: semisimplicity is a magnitude-axis fact.
    Nothing here bears on the `P ≠ NP` wall, and the counting-to-decision
    transfer is untouched. -/
theorem semisimple_of_one_lt_unconditional {q : ℝ} (hq : 1 < q) (n : ℕ) :
    IsSemisimpleRing (Hecke ℝ q q⁻¹ n) :=
  haveI := wenzlCriterion_of_one_lt hq
  QOU.Information.semisimple_of_one_lt
    (ss := fun n => IsSemisimpleRing (Hecke ℝ q q⁻¹ n)) hq n

end QOU.SchurWeyl
